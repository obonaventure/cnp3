## This file abstracts a *very* simple Nat64 gateway by 
#  using Scapy Automaton Facility
## Mickael Hoerdt <mickael.hoerdt@uclouvain.be>
## UCL - INL <http://inl.info.ucl.ac.be>

import Queue,sys
import ipaddr
from scapy.packet import *
from scapy.fields import *
from scapy.automaton import *
from scapy.layers.inet import *
from scapy.sendrecv import *

EXT_VERSION = "v0.1"
TIMEOUT = 2

class Nat64(Automaton):

	mac_addr_src = { "eth0":'02:00:E3:00:30:02', "eth1":'02:00:E3:00:30:03'}
	mac_addr_dst = { "bcastv6":'33:33:ff:ff:ff:ff', "bcastv4":'ff:ff:ff:ff:ff:ff'}

	def parse_args(self, **kargs):
		Automaton.parse_args(self, **kargs)
		self.mapping={}	
		self.srcv4='192.168.1.1'	
		self.pref64='0x200300000000000000000000ffffffffL'	
		print "Entering <WAIT_FOR_TCP_PACKET> ..."
        
	def master_filter(self, pkt):
		if (TCP in pkt):
			if(not pkt.src.upper() in self.mac_addr_src.values()):
				if(not pkt.dst.upper() in self.mac_addr_dst.values()):
					return True

	# Scapy Nat64 Automata
		
	@ATMT.state(initial=1)
	def WAIT_FOR_PACKET_TO_TRANSLATE(self):
		#print "<WAIT_FOR_TCP_PACKET>"
		pass
		
	@ATMT.timeout(WAIT_FOR_PACKET_TO_TRANSLATE, TIMEOUT)
	def timeout_waiting_for_packet_to_forward(self):
		print "<WAIT_FOR_TCP_PACKET/timeout>: Nothing to translate..."
		raise self.WAIT_FOR_PACKET_TO_TRANSLATE()	

	@ATMT.receive_condition(WAIT_FOR_PACKET_TO_TRANSLATE, prio=1)
	def received_TCP(self, pkt):
		if (IPv6 in pkt):
			#Look for the entry in the mapping
			#If if doesn't exist, create a new one (with a random port).	

			if((pkt[IPv6].src,pkt[TCP].sport) in self.mapping.values()):	
				for map_src,map_port in self.mapping.keys():
					if(self.mapping[map_src,map_port] == (pkt[IPv6].src,pkt[TCP].sport)):
						break
			else:
				print "IPv6: Creating a new NAT64 mapping entry:",pkt[IPv6].src,"  ",pkt[TCP].sport
				src_port=int(random.random()*65535)	
				self.mapping[(self.srcv4,src_port)]=(pkt[IPv6].src,pkt[TCP].sport)
				map_src,map_port=self.srcv4,src_port
			
			#extract the destination
			#Fill up the important information for the new packet

			dstv4 = str(ipaddr.IPv4(int(hex(ipaddr.IPv6(pkt[IPv6].dst))[18:26],16)).ip_ext_full)
			new_ipv4_packet=IP(src=map_src,dst=dstv4,ttl=pkt[IPv6].hlim)/pkt[TCP]
			new_ipv4_packet[TCP].sport=map_port
			
			#Remove checksum to force scapy to recompute it
			#and send the packet in IPv4

			new_ipv4_packet[TCP].chksum=None
			self.send(new_ipv4_packet)
			
		if (IP in pkt):
			#Try to find the corresponding mapping entry
			try:
				#Extract the source IPv6 and the dport from the mapping
				(srcv6,map_port)=self.mapping[(pkt[IP].dst,pkt[TCP].dport)]
				
				#Build the destination and fill up important information
				dstv6=str(ipaddr.IPv6(int(self.pref64[:18]+hex(ipaddr.IPv4(pkt[IP].src))[2:10]+self.pref64[26:34],16)))
				new_ipv6_packet=IPv6(src=dstv6,dst=srcv6,hlim=pkt[IP].ttl)/pkt[TCP]
				new_ipv6_packet[TCP].dport=map_port	
				
				#Remove checksum to force scapy to recompute it
				#and send the packet in IPv6
				new_ipv6_packet[TCP].chksum=None
				self.send(new_ipv6_packet)	
			
			except KeyError:
				print "IPv4: Mapping entry not found:",pkt[IP].dst,"  ",pkt[TCP].dport
