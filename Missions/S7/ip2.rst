Implementing an IPv4 router
===========================

During this exercise, you will implement a subset of a prototype IPv4 router by using scapy_. Your router will be able to :
 - forward IPv4 packets
 - reply to ICMP `Echo request` messages produced by :manpage:`ping(8)`
 - support :manpage:`traceroute(8)`

The deadline for this exercise is Tuesday November 10th, 13.00.



Preparation of the lab
----------------------

The first step of this exercise is to prepare the configuration of the emulated network that you will use. Your emulated network will be composed of four virtual machines :
 - your router with three interfaces : `eth0`, `eth1` and `eth2`
 - three clients : `client1`, `client2` and `client3`. Each client has an `eth0` interface

The different interfaces have been connected as follows :
 - `eth0` on the router is connected to `eth0` on `client1`
 - `eth1` on the router is connected to `eth0` on `client2`
 - `eth2` on the router is connected to `eth0` on `client3`

The clients will use the IPv4 implementation of the Linux kernel while the router will use your implementation written in scapy_. As you will use the emulated network to send and receive IPv4 packets, you need to configure the interfaces on all clients. On Linux, the IP addresses assigned on an interface can be configured by using :manpage:`ifconfig(8)`. When :manpage:`ifconfig(8)` is used without parameters, it lists all the existing interfaces of the host with their configuration. A sample :manpage:`ifconfig(8)` output is shown below ::

 UML1:~# ifconfig
 eth0      Link encap:Ethernet  HWaddr FE:3A:59:CD:59:AD  
          Inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::fc3a:59ff:fecd:59ad/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:216 (216.0 b)  TX bytes:258 (258.0 b)
          Interrupt:5 
 lo       Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)


This UML host has two interfaces : the loopback interface (`lo` with IPv4 address `127.0.0.1` and IPv6 address `::1`) and the `eth0` interface. The `192.168.1.1/24` address and a link local IPv6 address (`fe80::fc3a:59ff:fecd:59ad/64`) have been assigned to interface `eth0`. The broadcast address is used in some particular cases, this is outside the scope of this exercise. :manpage:`ifconfig(8)` also provides statistics such as the number of packets sent and received over this interface.

Another important information that is provided by :manpage:`ifconfig(8)` is the hardware address (HWaddr) used by the datalink layer of the interface. On the example above, the `eth0` interface uses the 48 bits `FE:3A:59:CD:59:AD` hardware address.

You can configure the IPv4 address assigned to an interface by specifying the address and the netmask ::

 ifconfig eth0 192.168.1.2 netmask 255.255.255.128

or you can also specify the prefix length ::

 ifconfig eth0 192.168.1.2/25

In both cases, `ifconfig eth0` allows you to verify that the interface has been correctly configured ::

 eth0      Link encap:Ethernet  HWaddr FE:3A:59:CD:59:AD  
           inet addr:192.168.1.2  Bcast:192.168.1.127  Mask:255.255.255.128
           inet6 addr: fe80::fc3a:59ff:fecd:59ad/64 Scope:Link
           UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
           RX packets:3 errors:0 dropped:0 overruns:0 frame:0
           TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
           collisions:0 txqueuelen:1000 
           RX bytes:216 (216.0 b)  TX bytes:258 (258.0 b)
           Interrupt:5 

:manpage:`ifconfig` also allows you to configure several IPv4 addresses over a single physical interface. This is useful for some particular configuration and we will use these virtual interfaces to reduce the number of interfaces in our emulated network. The first virtual interface of `eth0` is `eth0:0`, the second `eth0:1`, ... You can configure a different IPv4 address on each virtual interface  ::

 ifconfig eth0:1 10.0.0.1/8 
 ifconfig eth0:1
 eth0:1    Link encap:Ethernet  HWaddr FE:3A:59:CD:59:AD  
           inet addr:10.0.0.1  Bcast:10.255.255.255  Mask:255.0.0.0
           UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
           Interrupt:5 


Use :manpage:`ifconfig(8)` to configure the following IPv4 addresses :
 - `192.168.0.2/24` on `eth0` on `client1`
 - `10.1.0.2/30` on `eth0` on `client2`
 -  one IPv4 address inside `10.0.0.0/25` on `eth0:0` on `client2` 
 -  one IPv4 address inside `8.0.0.0/13` on `eth0:1` on `client2` 
 -  one IPv4 address inside `9.0.0.0/24` on `eth0:2` on `client2` 
 - `10.1.0.6/30` on `eth0` on `client3`
 -  one IPv4 address inside `10.0.0.128/25` on `eth0:0` on `client3` 
 -  one IPv4 address inside `8.8.0.0/16` on `eth0:1` on `client3` 
 -  one IPv4 address inside `9.0.0.0/23` on `eth0:2` on `client3` 

Concerning the addresses of the virtual interfaces on `client2` and `client3`, when there are overlapping prefixes, ensure that the address assigned in largest subnet on one client does not belong to the more specific subnet allocated to the other client. Verify the configuration of these addresses with :manpage:`ifconfig(8)`. For each interface, note its hardware address. Then, use :manpage:`ping(8)` on each virtual machine to verify that the locally assigned IPv4 addresses are working correctly.

As your router will use scapy to process IPv4 packets, you need to disable IPv4 on the Linux kernel. This can be done by installing an :manpage:`iptables(8)` on each interface on your router ::

 iptables -A INPUT -p ip -i eth0 -j DROP
 iptables -A OUTPUT -p ip -i eth0 -j DROP
   


Implementation of a prototype IPv4 router in scapy_
---------------------------------------------------

scapy_ was optimised to allow hosts to easily send crafted IP packets, but it was not designed to implement a router that needs to forward packets. For this, you will need to understand a little bit of the operation of the datalink layer used in the emulated testbed. In the emulated testbed, Ethernet interfaces are emulated on each UML. We will explain in details the operation of Ethernet in the chapter dedicated to Local Area Networks. At this stage, the important information that you must know concerning Ethernet :
 - each Ethernet interface has a unique 48 bits hardware address
 - each Ethernet frame contains the hardware address of the interface on the host that sent the frame and the hardware address of the host that will receive the frame on this Ethernet network
 - Ethernet frames can contain up to 1500 bytes of data
 
You can obtain the 48 bits hardware addresses of the Ethernet interfaces on the emulated testbed by using :manpage:`ifconfig(8)` on each UML.

You can use scapy_ to easily build an Ethernet frame that contains an IPv4 packet and send it over a particular interface. For example, assuming that `client1` uses the `AA:AA:AA:AA:AA:AA` hardware address while `router1` uses address `BB:BB:BB:BB:BB:BB`, you can proceed as follows to send one IP packet from `client1` to the router ::
    
 # build an Ethernet frame containing an IP packet
 frame=Ether(src="AA:AA:AA:AA:AA:AA", dst="BB:BB:BB:BB:BB:BB")/IP(src="192.168.0.2",dst="192.168.0.1")
 # send the frame over the eth0 interface
 sendp(frame, iface="eth0")

Note that the code above uses `sendp` an not `send` to send the Ethernet frame. `send` uses the IP implementation and the routing tables on the local host to decide on which interface the packet should be forward. We will not use `send` in this exercise as your will use the routing tables that you implement in scapy_ and not the kernel's routing tables. 






## This file abstracts a simple forwarding paradigm by using Scapy Automaton Facility
## Laurent Vanbever <Laurent.Vanbever@uclouvain.be>
## UCL - INL <http://inl.info.ucl.ac.be>

# py-radix Library (see http://www.mindrot.org/projects/py-radix/) is mandatory

import Queue,sys,radix
from scapy.packet import *
from scapy.fields import *
from scapy.automaton import *
from scapy.layers.inet import *
from scapy.sendrecv import *

EXT_VERSION = "v0.1"
TIMEOUT = 2

class InternetRouter(Automaton):
	# IP addresses local to the router
	local_ips = ['192.168.0.1', '10.1.0.1', '10.1.0.5', '10.0.2.2', '10.0.2.15']
	
	# Note: We need MAC addresses to forward IP packet, because, by default, the scapy send method works at L3 and rewrite source addresse based on its routing table
	# MAC addresses local to the router corresponding to each interface
	mac_addr_src = { "eth4":'08:00:27:34:bc:67', "eth2":'08:00:27:ec:2e:c9', "eth3":'08:00:27:7f:7b:ef'}
	# Remote MAC addresses corresponding to each interface
	mac_addr_dst = { "eth4":'08:00:27:5a:6e:de', "eth2":'08:00:27:68:d2:88', "eth3":'08:00:27:ec:2d:cd'}
	
	def parse_args(self, **kargs):
		Automaton.parse_args(self, **kargs)
		self.rtree = radix.Radix()
		self.build_rt()
		print "Entering <WAIT_FOR_IP_PACKET> ..."
    
	def master_filter(self, pkt):
		return (IP in pkt and not pkt.src in self.mac_addr_src.values() and not pkt[IP].src in self.local_ips and not pkt[IP].src=='255.255.255.255' and not pkt[IP].src=='0.0.0.0' and not pkt[IP].tos==10)
	

	# We build the radix which contains for each destination prefix, the outgoing interface. The nh is not needed as MAC addresses are statically encoded (see mac_addr_dst variable)
	def build_rt(self):
		self.rtree.add("10.0.0.0/25").data["nh"]="eth2"
		self.rtree.add("10.0.0.128/25").data["nh"]="eth3"
		self.rtree.add("8.0.0.0/13").data["nh"]="eth2"
		self.rtree.add("8.8.0.0/16").data["nh"]="eth3"
		self.rtree.add("9.0.0.0/24").data["nh"]="eth2"
		self.rtree.add("9.0.0.0/23").data["nh"]="eth3"
		self.rtree.add("192.168.0.0/30").data["nh"]="eth4"
		self.rtree.add("10.1.0.0/30").data["nh"]="eth2"
		self.rtree.add("10.1.0.4/30").data["nh"]="eth3"
	
	# Scapy Forwarding Automata
		
	@ATMT.state(initial=1)
	def WAIT_FOR_PACKET_TO_FORWARD(self):
		#print "<WAIT_FOR_IP_PACKET>"
		pass
		
	@ATMT.timeout(WAIT_FOR_PACKET_TO_FORWARD, TIMEOUT)
	def timeout_waiting_for_packet_to_forward(self):
		print "<WAIT_FOR_IP_PACKET/timeout>: Nothing to forward..."
		raise self.WAIT_FOR_PACKET_TO_FORWARD()	

	@ATMT.receive_condition(WAIT_FOR_PACKET_TO_FORWARD)
	def received_local_ICMP(self, pkt):
		if (ICMP in pkt and pkt[IP].dst in self.local_ips and pkt[ICMP].type==8):
			print "<WAIT_FOR_IP_PACKET/ICMP_echo_request>: Sending an ICMP echo-reply back to the source: ", pkt[IP].src
			self.answer = IP(dst=pkt[IP].src)/ICMP(type='echo-reply', seq=pkt[ICMP].seq,id=pkt[ICMP].id)/pkt[Raw]
			self.send(self.answer)
			raise self.WAIT_FOR_PACKET_TO_FORWARD()
			
	@ATMT.receive_condition(WAIT_FOR_PACKET_TO_FORWARD, prio=1)
	def received_local_IP(self, pkt):
		if (pkt[IP].dst in self.local_ips):
			print "<WAIT_FOR_IP_PACKET/IP_local>: Received an IP packet destinated to me",pkt[IP].dst,"from:",pkt[IP].src
			self.ttl = pkt[IP].ttl-1
			if(self.ttl==0):
				print "<WAIT_FOR_IP_PACKET/TTL_Exceeded>: Sending an ICMP dest unreachable to the source: ", pkt[IP].src
				self.answer = IP(dst=pkt[IP].src)/ICMP(type='dest-unreach',code=3)/pkt[IP]
				self.send(self.answer)
			print "<WAIT_FOR_IP_PACKET/IP_local>: Dropping it"
			raise self.WAIT_FOR_PACKET_TO_FORWARD()			

	@ATMT.receive_condition(WAIT_FOR_PACKET_TO_FORWARD, prio=2)			
	def received_fwd_IP(self, pkt):
		if not (pkt[IP].dst in self.local_ips):
			# The packet is not destinated to us, decrement the TTL
			self.ttl = pkt[IP].ttl-1
			# TTL == 0 => exceeded during transit, send a ICMP type=11 code=1 back to the source
			if(self.ttl==0):
				print "<WAIT_FOR_IP_PACKET/TTL_Exceeded>: Sending an ICMP TTL Exceeded to the source: ", pkt[IP].src
				self.answer = IP(dst=pkt[IP].src)/ICMP(type=11,code=0)/pkt[IP]
				self.send(self.answer)
			else:
				# TTL is greater than 0 -> forwarding IP packet
				# We need to create a copy of the IP packet (self.pkt2forward) to forward in order for scapy to recompute the IP checksum 
				self.pkt2forward = IP(src=pkt[IP].src,dst=pkt[IP].dst,ttl=self.ttl)/pkt[IP].payload
				# Return the best match in the radix
				self.outgoing_node = self.rtree.search_best(self.pkt2forward.dst)
				# If the destination is not found in the radix, send a ICMP Destination Unreachable back to the source
				if(self.outgoing_node==None):
					print "<WAIT_FOR_IP_PACKET/Dest_Unreachable>: Destination",pkt[IP].dst,"is unreachable, sending an ICMP destination unreachable to the source:", pkt[IP].src
					self.answer = IP(dst=self.pkt2forward.src)/ICMP(type='dest-unreach',code=0)/self.pkt2forward
					self.send(self.answer)
				# The destination has been found in the radix, forward the IP packet accordingly
				else:
					print "<WAIT_FOR_IP_PACKET/Forward_pkt>: Forwarding IP packet from",pkt[IP].src,"destinated to",pkt[IP].dst, "on outgoing interface" , self.outgoing_node.data["nh"]
					self.oframe = Ether(dst=self.mac_addr_dst[self.outgoing_node.data["nh"]], src=self.mac_addr_src[self.outgoing_node.data["nh"]])/self.pkt2forward
					#debug purpose
					#self.oframe.show()
					sendp(self.oframe, iface=self.outgoing_node.data["nh"], verbose=0)
		Raise self.WAIT_FOR_PACKET_TO_FORWARD()

