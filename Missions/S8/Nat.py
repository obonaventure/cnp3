## This file abstracts a *very* simple Nat gateway by 
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

class Nat(Automaton):

	mac_addr_src = { "00:00:E3:00:30:04":'eth0', "00:00:E3:00:30:03":'eth1'}
	mac_addr_dst = { "bcastv4":'ff:ff:ff:ff:ff:ff'}

	def parse_args(self, **kargs):
		Automaton.parse_args(self, **kargs)
		self.mapping={}	
		self.public_addr='216.239.59.104'	
		print "Entering <WAIT_FOR_TCP_PACKET> ..."
        
	def master_filter(self, pkt):
		if (TCP in pkt):
			if(not pkt.src.upper() in self.mac_addr_src.keys()):
				if(not pkt.dst.upper() in self.mac_addr_dst.values()):
					return True

	# Scapy Nat Automata
		
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
		# Packets arrived from the private network
		if (self.mac_addr_src[pkt.dst.upper()] == "eth0"):
			#Look for the entry in the mapping
			#If if doesn't exist, create a new one (with a random port).	

			if((pkt[IP].src,pkt[TCP].sport) in self.mapping.values()):	
				for map_src,map_port in self.mapping.keys():
					if(self.mapping[map_src,map_port] == (pkt[IP].src,pkt[TCP].sport)):
						break
			else:
				print "Nat: Creating a new NAT mapping entry:",pkt[IP].src,"  ",pkt[TCP].sport
				src_port=int(random.random()*65535)	
				self.mapping[(self.public_addr,src_port)]=(pkt[IP].src,pkt[TCP].sport)
				map_src,map_port=self.public_addr,src_port
			
			#extract the destination
			#Fill up the important information for the new packet

			new_ip_packet=IP(src=map_src,dst=pkt[IP].dst,ttl=pkt[IP].ttl)/pkt[TCP]
			new_ip_packet[TCP].sport=map_port
			
			#Remove checksum to force scapy to recompute it
			#and send the packet 

			new_ip_packet[TCP].chksum=None
			self.send(new_ip_packet)
			
		# Packets arrived from the public network
		if (self.mac_addr_src[pkt.dst.upper()] == "eth1"):
			#Try to find the corresponding mapping entry
			try:
				#Extract the source IP and the dport from the mapping
				(src,map_port)=self.mapping[(pkt[IP].dst,pkt[TCP].dport)]
				
				#Build the destination and fill up important information
				new_ip_packet=IP(src=pkt[IP].src,dst=src,ttl=pkt[IP].ttl)/pkt[TCP]
				new_ip_packet[TCP].dport=map_port	
				
				#Remove checksum to force scapy to recompute it
				#and send the packet 
				new_ip_packet[TCP].chksum=None
				self.send(new_ip_packet)	
			
			except KeyError:
				print "Nat: Mapping entry not found:",pkt[IP].dst,"  ",pkt[TCP].dport
