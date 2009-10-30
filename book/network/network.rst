================== 
The network layer
==================

.. :rfc:`3927` special addresses

.. http://tools.ietf.org/html/draft-touch-intarea-ipv4-unique-id-01 comment choisir les IP ids

Principles 
###########


.. figure:: fig/network-fig-001-c.png
   :align: center
   :scale: 50
   
   The network layer in the reference model


routers


types of datalink
- point to point
- local area networks


datalink layer service

.. figure:: fig/network-fig-003-c.png
   :align: center
   
   The datalink layer

control plane versus data plane

Organisation of the network layer


The data plane
==============

Datagram mode
-------------
destination based forwarding
hop-by-hop forwarding

explain content of forwarding table


Virtual circuit mode
=====================

more flexible routes than datagram mode
signaling, hop-by-hop or explicit route

discuss how the forwarding table must be built


Routing 
=======


Static routing
--------------

simplest
avoid loop

tables can be computed offline, but in this case the issue is to update the tables with traffic flowing


Distance vector routing
-----------------------

simple, do not provide all details and examples, focus on algorithms

explain limitations and discuss count to infinity


Link state routing
------------------

more complex, explain first discovery, then reliable flooding
and using dijkstra for shortest path computation

Internet Protocol
#################

The Internet Protocol (IP) is the network layer protocol of the TCP/IP protocol suite. IP is the layer that allows the applications running above the transport layer (UDP/TCP) to use a wide range of heterogeneous datalink layers. IP was designed when most point-to-point links were telephone lines with modems. Since then, IP has been able to use Local Area Networks (Ethernet, Token Ring, FDDI, ...), new wide area data link layer technologies (X.25, ATM, FrameRelay, ...) and more recently wireless networks (802.11, 802.15, UMTS, GPRS, ...). The flexibility  of IP and its ability to use various types of underlying data link layer technologies is one of its key advantages.

.. figure:: fig/network-fig-051-c.png
   :align: center
   
   IP and the reference model

.. there is a draft on expectations of lower layer

The current version of IP is version 4 specified in :rfc:`791`. We will first describe this version and later will explain IP version 6 that is expected to replace IP version 4 in the future.

IP version 4
============

IP version 4 is the data plane protocol of the network layer in the TCP/IP protocol suite. The design of IP version 4 was based on the following assumptions :

 - IP will provide an unreliable connectionless service (reliability will be provided by TCP when needed)
 - IP will operate with the datagram transmission mode
 - IP addresses will have a fixed size of 32 bits 
 - IP will be used above different types of datalink layers
 - IP hosts will exchange variable length packets

The addresses are an important part of any network layer protocol. In the late 1970s, the developers of IPv4 designed IPv4 for a research network that would interconnect some research labs and universities. For this utilisation, 32 bits wide addresses were much larger than the expected number of hosts on the Internet. Furthermore, 32 bits addresses could be easily processed on 32 bits CPUs. None of the developers of IPv4 were expecting that IPv4 would become as widely used as it is today.


IPv4 addresses are encoded as a 32 bits field. IPv4 addresses are often represented in `dotted-decimal` format as a sequence of four integers separated by a `.`. The first integer is the decimal representation of the most significant byte of the 32 bits IPv4 address, ... For example, 

 * 1.2.3.4 corresponds to 00000001000000100000001100000100
 * 127.0.0.1 corresponds to 01111111000000000000000000000001
 * 255.255.255.255 corresponds to 11111111111111111111111111111111

.. index:: multihomed host

An IPv4 address is used to identify an interface on a router or a host. A router has thus as many IPv4 addresses as the number of interfaces that it has in the datalink layer. Most hosts have a single datalink layer interface and thus have a single IPv4 address. However, with the growth of wireless, more and more hosts have several datalink layer interfaces (e.g. an Ethernet interface and a WiFi interface). These hosts are said to be `multihomed`. A multihomed host with two interfaces has thus two IPv4 addresses.

An important point to be defined in a network layer protocol is the allocation of the network layer addresses how they are used. A naïve allocation scheme would be to provide an IPv4 address to each host when the host is attached to the Internet on a first come first served basis. With this solution, a host in Belgium could have address 2.3.4.5 while another host located in Africa would use address 2.3.4.6. Unfortunately, this would force all routers to maintain a route for all hosts. The figure below shows a simple enterprise networks with two routers and three hosts and the associated routing tables.

.. figure:: fig/network-fig-056-c.png
   :align: center
   :scale: 50
   
   Scalibility issues when using isolated IP addresses 

.. index:: IP subnet, IP prefix, subnet mask

To preserve the scalability of the routing system, it is important to minimize the number of routes that are stored on each router. A router cannot store and maintain one route for each of the almost 1 billion hosts that are connected to today's Internet. Routers should only maintain routes towards blocks of addresses and not towards individual hosts. For this, hosts are grouped in `subnets` based on their location in the network. A typical subnet will group all the hosts that are attached to the same Local Area Network or part of the same enterprise. An IPv4 address is then composed of two parts : a `subnetwork identifier` and  a `host identifier`. The `subnetwork identifier` is encoded as the high order bits of the address and the host identifier is encoded in the low order bits of the address. This is illustrated in the figure below.

.. figure:: fig/network-fig-054-c.png
   :align: center
   :scale: 50
   
   The subnetwork and host identifiers inside an IPv4 address

When a router needs to forward a packet, it must know the `subnet` of the destination address to be able to consult its forwarding table to forward the packet. :rfc:`791` proposed to use the high-order bits of the address to encode the length of the subnet identifier. This lead to the definition of three `classes` of unicast addresses [#fclasses]_

=======  ==========  =========  =============	=============
Class    High-order  Length of  Number of	Addresses per
         bits        subnet id	networks   	network
-------  ----------  ---------  -------------   -------------
Class A	 `0`	     8 bits	128 		16,777,216 (:math:`2^{24}`)	
Class B	 `10`        16 bits	16,384     	65,536 (:math:`2^{16}`)	
Class C	 `110`	     24 bits	2,097,152  	256 (:math:`2^8`)
=======  ==========  =========  =============	=============

However, these three classes of addresses were not flexible enough. A class `A` subnet was too large for most organisations and a class `C` subnet was too small. Flexbility was added by the introduction of `variable-length subnets` in :rfc:`1519`. With `variable-length` subnets, the subnet identifier can have any size from `1` to `31`. `Variable-length` subnets allow the network operators to use a subnet that matches the number of hosts that will be placed inside the subnet. A subnet identifier or IPv4 prefix is usually [#fnetmask]_ represented as `A.B.C.D/p` where `A.B.C.D` is the network address obtained by concatenating the subnet identifier with a host identifier containing only `0` and `p` is the length of the subnet identifier in bits. The table below provides examples of IP subnets.

============== 	==========  ============  ===============
Subnet      	Number of   Smallest      Highest
	    	addresses   address	  address
--------------	----------  ------------  ---------------
10.0.0.0/8  	16,777,216  10.0.0.0      10.255.255.255	
192.168.0.0/16	65,536	    192.168.0.0   192.168.255.255
198.18.0.0/15	131,072	    198.18.0.0 	  198.19.255.255
192.0.2.0/24	256	    192.0.2.0 	  192.0.2.255
10.0.0.0/30	4	    10.0.0.0	  10.0.0.3
10.0.0.0/31	2	    10.0.0.0	  10.0.0.1
============== 	==========  ============= ===============


The figure below provides a simple example of the utilisation of IPv4 subnets in an enterprise network. In Local Area Networks, the size of the subnet will usually depend on the expected number of hosts attached to the LAN. For point-to-point links, many deployments have used `/30` prefixes, but recent routers are now using `/31` subnets on point-to-point links :rfc:`3021` or even do not use IPv4 addresses on such links [#funnumbered]_. 
 
.. figure:: fig/network-fig-056-c.png
   :align: center
   :scale: 50
   
   IP subnets in a simple enterprise network

A second issue concerning the addresses of the network layer is the allocation scheme that is used to allocated blocks of addresses to organisations. The first allocation scheme was based on the different classes of addresses. The pool of IPv4 addresses was managed by a secretariat (?? SRI ??) that allocated address blocks on a first-come first served basis. Large organisations such as IBM, BBN, but also Stanford or the MIT were able to obtain a class `A` address block. Most organisations requested a class `B` address block that contains 65536 addresses, which was suitable for most enterprises and universities. The table below provides examples of some IPv4 address blocks in the class `B` space. 

==============            ===========================================
Subnet	       		  Organisation
--------------            -------------------------------------------
130.100.0.0/16 		  Ericsson, Sweden
130.101.0.0/16		  University of Akron, USA
130.102.0.0/16		  The University of Queensland, Australia
130.103.0.0/16		  Lotus Development, USA
130.104.0.0/16 		  Université catholique de Louvain, Belgium
130.104.0.0/16		  Open Software Foundation, USA
==============            ===========================================

However, the Internet was a victim of its own success and in the late 1980s, many organisations were requesting blocks of IPv4 addresses and connected to the Internet. Most of these organisations requested class `B` address blocks because class `A` address were too large and in limited supply while class `C` address blocks were considered to be too small. Unfortunately, there were only 16,384 different class `B` address blocks and this address space was being consummed were quickly. Furthermore, the routing tables maintained by the routers were growing quickly and some routers had difficulties in maintaining all these routes in their limited memory [#fciscoags]_.

.. figure:: fig/network-fig-162-c.png
   :align: center
   :scale: 50
   
   Evolution of the size of the routing tables on the Internet (Jul 1988- Dec 1992 - source : :rfc:`1518`)

.. index:: Classless Interdomain Routing

Faced with these two problems, the Internet Engineering Task Force decided to develop the Classless Interdomain Routing (CIDR) architecture :rfc:`1518`. This architecture aims at allowing IP routing to scale better than the class-based architecture. CIDR contains three important modifications compared the :rfc:`791`.

      1. IP address classes are deprecated. All IP equipments must use and support variable-length subnets.
      2. IP address blocks are not allocated anymore on a first-come-basis. Instead, CIDR introduces a hierarchical address allocation scheme.
      3. IP routers must use longest-match 


The last two modifications were introduced to improve the scalability of the IP routing system. The main drawback of the first-come-first-served address block allocation scheme was that neighboring address blocks were allocated to very different organisations and conversely, very different address blocks were allocated to similar organisations. With CIDR, address blocks are allocated by Regional IP Registries (RIR) in an aggregatable manner. A RIR is responsible for a large block of addresses and a region. For example, RIPE_ is the RIR that is responsible for Europe. A RIR allocates smaller address blocks from its large block to Internet Service Providers :rfc:`2050`. Internet Service Providers then allocate smaller address blocks to their customers, ... When an organisation requests an address block, it must provide that it already has or expect to have in the near future, a number of hosts or customers that is equivalent to the size of the requested address block. 

The main advantage of this hierarchical address block allocation scheme is that it allows the routers to maintain fewer routers. For example, consider the address blocks that were allocated to some of the Belgian universities as shown in the table below.

==============            =============================================
Address block   	  Organisation
--------------            ---------------------------------------------
130.104.0.0/16 		  Université catholique de Louvain
134.58.0.0/16		  Katholiek Universiteit Leuven
138.48.0.0/16		  Facultés universitaires Notre-Dame de la Paix
139.165.0.0/16		  Université de Liège
164.15.0.0/16		  Université Libre de Bruxelles
==============            =============================================

These universities are all connected to the Internet exclusively via the `Belgian Research Network <http://www.belnet.be>`_. As each of these universities has received a different address block, the routers of the `Belgian Research Network <http://www.belnet.be>`_ Must announce a route for each university and all routers on the Internet must maintain a route towards each university. In contrast, consider all the high schools and the government institutions that are connected to the Internet via the same `Belgian Research Network <http://www.belnet.be>`_. These high school received their address block after the introduction of CIDR. Their address block is part of the `193.190.0.0/15` address block that is owned by the `Belgian Research Network <http://www.belnet.be>`_. With CIDR, the `Belgian Research Network <http://www.belnet.be>`_ Can announce a single route towards `193.190.0.0/15` that covers all these high schools. 
 
.. index:: multihomed network

However, there is only difficulty with the aggregatable variable length subnets used by CIDR. Consider for example `FEDICT <http://www.fedict.be>`_, a governmental institution that uses the `193.191.244.0/23` address block. Assume that in addition to being connected to the Internet via the `Belgian Research Network <http://www.belnet.be>`_ , `FEDICT <http://www.fedict.be>`_ also wanrts to be connected to another Internet Service Provider. The FEDICT network is then said to be multihomed. This is shown in the figure below.

.. figure:: fig/network-fig-163-c.png
   :align: center
   :scale: 50
   
   Multihoming and CIDR

With such a multihomed network, routers on the Internet would have two routes towards IPv4 address `193.191.245.88` : one route via Belnet (`193.190.0.0/15`) and one route via the other ISP (`193.191.244.0/23`). Both routes match IPv4 address `193.192.145.88`. Since :rfc:`1519` when a router knows several routes towards the same destination address, it must forward packets along the route having the longest prefix length. In the case of `193.191.245.88`, this is the route `193.191.244.0/23` that will be followed to forward the packet. This forwarding rule is called the `longest match` or the `more specific match`. All IPv4 routers implement this forwarding rule.


IPv4 packet forwarding
----------------------

Now that we have clarified the allocation of IPv4 addresses and the utilisation of longest match to forward IPv4 packets, we can have a more detailed look at IPv4 by starting with the format of the IPv4 packets. The IPv4 packet format was defined in :rfc:`791`. Besides a few clarifications and some backward compatible changes, the IPv4 packet format did not change significantly since the publication of :rfc:`791`. All IPv4 packets use the 20 bytes header shown below. Some IPv4 packets contain an optional header extension that will be described later. 

.. figure:: fig/network-fig-064-c.png
   :align: center
   
   The IP version 4 header

The main fields of the IPv4 header are :

 - a 4 bits `version` that indicates the version of IP used to defined the header. Using a version field in the header allows the protocol to evolve as we'll see with IPv5
 -  a 4 bits `IP Header Length (IHL)` that indicates the length of the IP header in 32 bits words. This field allows IPv4 to use options if required, but as it is encoded as a 4 bits field, the IPv4 header cannot occupy more than 64 bytes. 
 - an 8 bits `DS` field that is used for Quality of Service and whose usage will be described later.
 - a 16 bits `length` that indicates the total length of the entire IPv4 packet (header and payload) in bytes. This implies that an IPv4 packet cannot be longer than 65535 bytes.
 - a 32 bits `source address` field that contains the IPv4 address of the source host
 - a 32 bits `destination address` field that contains the IPv4 address of the destination host 
 - a 16 bits `checksum` that protects only the IPv4 header against transmission errors


The other fields of the IPv4 header are used for specific purposes. The first is the 8 bits `Time To Live (TTL)` field. This field was introduced in IPv4 to avoid the risk of having an IPv4 packet caught in an infinite loop due to a transient or permament error in routing tables. Consider for example the situation depicted in the figure below where destination `D` uses address `11.0.0.56`. If `S` sends a packet towards this destination, the packet will be forwarded to router `B` that will forward it to router `C` that will forward it back to router `A`.

.. figure:: fig/network-fig-164-c.png
   :align: center
   
   Forwarding loops in an IP network

Unfortunately, such loops can occur for two reasons in IP networks. First, if the network uses static routing, the loop can be caused by a simple configuration error. Second, if the network uses dynamic routing, such a loop can occur transiently, for example during the convergence of the routing protocol after a link or router failure. The `TTL` field of the IPv4 header ensures that even if there are forwarding loops in the network, packets will not loop forever. The `TTL` field is used as follows. Hosts send their IPv4 packets with a positive `TTL` (usually `64` or more [#finitialttl]_). When a router receives an IPv4 packet, it first decrements the `TTL` by one. If the `TTL` becomes `0`, the packet is discarded. Otherwise, the router performs a lookup in its forwarding table to forward the packet.

A second problem for IPv4 is the heterogeneity of the datalink layer. IPv4 is used above many very different datalink layers. Each datalink layer has its own characteristics and as indicated earlier, each datalink layer is characterised by a maximum frame size. The table below provides some common maximum frame sizes in the datalink layer.

==============      ==================
Datalink layer      Maximum frame size
--------------      ------------------
Ethernet	    1500 bytes
WiFi		    2272 bytes
ATM (AAL5)	    9180 bytes
802.15.4	    102 or 81 bytes
Token Ring
FDDI
==============      ==================

Although IPv4 can send 64 KBytes long packets, none of the datalink layer technologies that are used today are able to send a 64 KBytes IPv4 packet inside a frame. Furthermore, as illustrated in the figure below, another problem is that a host may send a packet that would be too large for one of the datalink layers used by the intermediate routers. 

.. figure:: fig/network-fig-063-c.png
   :align: center
   
   The need for fragmentation and reassembly

.. index:: IPv4 fragmentation and reassembly

To solve these problems, IPv4 includes a fragmentation and reassembly mechanism. Both hosts and intermediate routers may fragment an IPv4 packet if the packet is too long to sent via the datalink layer. In IPv4, fragmentation is completely performed in the IP layer and a large IPv4 will be fragmented in two or more IPv4 packets (called fragments). The IPv4 fragments of a large packet are normal IPv4 packets that are forwarded towards the destination of the large packet by intermediate routers. 

The IPv4 fragmentation mechanism relies on four fields of the IPv4 header : `Length`, `Identification`, the `flags` and the `Fragment Offset`. The IPv4 header contains two flags : `More` and `Don't Fragment (DF)`. When the `DF` flag is set, this indicates that the packet cannot be fragmented.

.. index:: Maximum Transmission Unit (MTU)

The basic operation of the IPv4 fragmentation is as follows. A large packet is fragmented in several fragments. The size of all fragments, except the last one, is equal to the Maximum Transmission Unit of the link used to forward the packet. Each IPv4 packet contains a 16 bits `Identifier` field. The `Identifier` of the large packet is copied in all fragments to allow the destination to reassemble the received fragments together. In each fragment, the `Fragment Offset` indicates, in units of 8 bytes, the position of the payload of the fragment in the payload of the original packet. The `Length` field in each fragment indicates the length of the payload of the fragment as in a normal IPv4 packet. Finally, the `More` flag is set only in the last fragment of a large packet.


The following pseudocode details the IPv4 fragmentation ::


 mtu : maximum size of the packet (including header) of outgoing link
 if p.len <  mtu : 
    forward(p)
 # packet is too large
 if p.flags=='DF' :
    discard(p)
 # packet must be fragmented
 payload=p[IP].payload
 pos=0
 while len(payload) > 0 :
    if len(payload) > mtu :
       toSend=IP(dest=p.dest,src=p.src,
	         ttl=p.ttl, id=p.id, 
	         frag=p.frag+(pos/8),
		 len=mtu, proto=p.proto)/payload[0:mtu]
       pos=pos+mtu
       payload=payload[mtu+1:]	   
    else
       toSend=IP(dest=p.dest,src=p.src,
	         ttl=p.ttl, id=p.id, 
	         frag=p.frag+(pos/8),
		 flags=p.flags,
		 len=len(payload), proto=p.proto)/payload
    forward(toSend)   

The fragments of an IPv4 packet may arrive at the destination in any order as each fragment will be forwarded independently in the network and may follow different paths. Furthermore, some fragments may be lost and never reach the destination.

The reassembly algorithm used by the destination host is roughly as follows. First, the destination can verify whether a received IPv4 packet is a fragment or not by checking the value of the `More` flag and the `Fragment Offset`. If the `Fragment Offset` is set to `0` and the `More` flag is reset, the received packet has not been fragmented. Otherwise, the packet has been fragmented and must be reassembled. The reassembly algorithm relies on the `Identifier` field of the received fragments to associate a fragment with the corresponding packet being reassembled. Furthermore, the `Fragment Offset` field indicates the position of the fragment payload in the original unfragmented packet. Finally, thanks to the `More` flag the destination can determine the total length of the orginal unfragmented packet.

Note that the reassembly algorithm must deal with the unreliability of the IP network. This implies that a fragment may be duplicated or a fragment may never reach the destination. The destination will easily detect fragment duplication thanks to the `Fragment Offset`. To deal with fragment losses, the reassembly algorithm must bound the time during which the fragments of a packet are stored in its buffer while the packet is being reassembled. This can be implemented by starting a timer when the first fragment of a packet is received. If the packet has not been reassembled upon expiration of the timer, all fragments are discarded and the packet is considered to be lost. 




.. index Internet Control Message Protocol, ICMP

ICMP version 4
==============

When IPv4 packets are processed, it is sometimes necessary for intermediate routers or the destination host to inform the sender of the packet of a problem that occured while processing the packet. The TCP/IP protocol suite contains the Internet Control Message Protocol (ICMP). ICMP is defined in :rfc:`792`. ICMP messages are carried as the payload of IP packets (the protocol value reserved for ICMP is `1`). An ICMP message is composed of an 8 bytes header and a variable length payload that usually contains the first bytes of the packet that triggered the transmission of the ICMP message.

.. figure:: fig/network-fig-069-c.png
   :align: center
   
   ICMP version 4 

In the ICMP header, the `Type` and `Code` field indicate the type of problem that was detected by the sender of the ICMP message. The `Checksum` protects the entire ICMP message against transmission errors and the `Data` field contains additional information for some ICMP messages.

The main types of ICMP messages are :

 - `Destination unreachable` : a `Destination unreachable` ICMP message is sent when a packet cannot be delivered to its destination due to routing problems. Different types of unreachability are distinguished :
   - `Network unreachable` : this ICMP message will be sent by a router that does not have a route for the subnet containing the destination address of the packet 
   - `Host unreachable` : this ICMP message will be sent by a router that is attached to the subnet that contains the destination address of the packet, but this destination address cannot be reached at this time
   - `Protocol unreachable` : this ICMP message will be sent by a destination host that has received a packet, but does not support the transport protocol indicated in the packet's `Protocol` field
   - `Port unreachable` : this ICMP message will be sent by a destination host that has received a packet destined to a (usually) UDP port number, but no server process is listening on this port
 - `Fragmentation needed` : this ICMP message will be sent by a router that receives a packet having the `Don't Fragment` flag set that is too large to be sent over the outgoing interface 
 - `Redirect` : this ICMP message can be sent when there are two routers on the same LAN. Consider a LAN with one host and two routers : `R1` and `R2`. Assume that `R1` is also connected to subnet `1.0.0.0/8` while `R2` is connected to subnet `2.0.0.0/8`. If a host on the LAN sends a packet towards `2.0.0.1` to `R1`, `R1` will need to forward the packet again on the LAN to reach `R2`. This is not optimal as the packet is sent twice on the same LAN. In this case, `R1` could send an ICMP `Redirect` message to the host to inform it that it should have sent the packet directly to `R2`. This will allow the host the send the other packets to `2.0.0.1` directly via `R2`. 
 - `Parameter problem` : this ICMP message is sent when a router or a host receives an IP packet containing an error
 - `Time Exceeded` : there are two types of `Time Exceeded` ICMP messages
   - `TTL exceeded` : a `TTL exceeded` message is sent by a router when it discards an IPv4 packet becaused its `TTL` reached `0`.
   - `Reassembly time exceeded` : this ICMP message is sent when a destination has been unable to reassemble all the fragments of a packet before the expiration of its reassembly timer. 
 - `Echo request` and `Echo reply` : these ICMP messages are used by the :manpage:`ping(8)` network debugging software. :manpage:`ping(8)` is often used by network operators to verify that a given IP address is reachable. Each host is supposed [#fpingproblems]_ to reply with an `Echo reply` ICMP message when its receives an  ICMP `Echo request` message. A sample usage of :manpage:`ping(8)` is shown below ::

 ping 130.104.1.1
 PING 130.104.1.1 (130.104.1.1): 56 data bytes
 64 bytes from 130.104.1.1: icmp_seq=0 ttl=243 time=19.961 ms
 64 bytes from 130.104.1.1: icmp_seq=1 ttl=243 time=22.072 ms
 64 bytes from 130.104.1.1: icmp_seq=2 ttl=243 time=23.064 ms
 64 bytes from 130.104.1.1: icmp_seq=3 ttl=243 time=20.026 ms
 64 bytes from 130.104.1.1: icmp_seq=4 ttl=243 time=25.099 ms
 ^C
 --- 130.104.1.1 ping statistics ---
 5 packets transmitted, 5 packets received, 0% packet loss
 round-trip min/avg/max/stddev = 19.961/22.044/25.099/1.938 ms


Echo requEast et Echo reply 

traceroute + example

ping + example

.. sidebar:: Redirection attacks

 explain the problem of redirection attacks and show that redirect should be used with care. introduce man in the middle attack


.. index:: Path MTU discovery

path mtu discovery :rfc:`1191`


Operation of an IPv4 router
---------------------------

decrement ttl
lookup
update checksum

default route


IP version 6
============

In the late 1980s and early 1990s the growth of the Internet was causing several operationnal problems on routers. Many of these routers had a single CPU and up to 1 MB of RAM to store their operating system, packet buffers and routing tables. Given the rate of allocation of IPv4 prefixes to companies and universities willing to join the Internet, the routing tables where growing very quickly and some feared that all IPv4 prefixes would be quickly allocated. In 1987, a study cited in :rfc:`1752` estimated 100,000 networks in the near future. In August 1990, estimates indicated that the class B space would be exhausted by March 1994. 
Two types of solutions were developed to solve this problem. The first short term solution was the introduction of Classless InterDomain Routing (:term:`CIDR`). A second short term solution was the Network Address Translation (:term:`NAT`) mechanism defined in :rfc:`1631` that allowed multiple hosts to share a single public IP address. 

However, in parallel with these short-term solutions, that have allowed the IPv4 Internet to continue to be useable until now, the Internet Engineering Task Force started to work on developing a replacement for IPv4. This work started with an open call for proposal outline in :rfc:`1550`. Several groups responded to this call with proposals for a next generation Internet Protocol (IPng) :

 * TUBA proposed in :rfc:`1347` and :rfc:`1561`
 * PIP proposed in :rfc:`1621`
 * SIPP proposed in :rfc:`1710`

The IETF decided to pursue the development of IPng on the basis on the SIPP proposal. As IP version `5` was already used by the experimental ST-2 protocol defined in :rfc:`1819`, the successor of IP version 4 is IP version 6. The initial IP version 6  in :rfc:`1752` was designed based on the following assumptions :

 * IPv6 addresses are encoded as a 128 bits field
 * The IPv6 header has a simple format that can be easily parsed by hardware devices
 * A host should be able to configure its IPv6 address automatically
 * Security must be part of IPv6

.. sidebar:: IPng address size

When the work on IPng started, it was clear that 32 bits was too small to encode an IPng address and all proposals used longer addresses. However, there were many discussions on the most suitable address length. A first approach, proposed by SIP in :rfc:`1710` was to use 64 bits addresses. A 64 bits address space was 4 billion times larger than the IPv4 address space and furthermore from an implementation viewpoint, 64 bits CPU were starting to appear and 64 bits addresses would naturally fit inside registers. Another approach was to use an existing address format. This was the TUBA proposal (:rfc:`1347`) that reuses the ISO CLNP 20 bytes addresses. The 20 bytes addresses provided room for growth and could 

IPv6 addressing architecture
----------------------------

The experience with IPv4 reveleaded that the scalability of a network layer protocol heavily depends on its addressing architecture. The designers of IPv6 spent a lot of effort defining its addressing architecture :rfc:`3513`. All IPv6 addresses are 128 bits wide. This implies that there are 340,282,366,920,938,463,463,374,607,431,768,211,456 (3.4 × 10^38) different IPv6 addresses. As the surface of the Earth is about 510,072,000 :math:`km^2`, this implies that there are about :math:`6.67 \times 10^{23}` IPv6 addresses per square meter on Earth. Compared to IPv4 that offered only 8 addresses per square kilometer, this is a significant improvement on paper. 

IPv6 supports unicast, multicast and anycast addresses. As with IPv4, an IPv6 unicast address is used to identify one datalink-layer interface on a host. If a host has several datalink layer interfaces (e.g. an Ethernet interface and a WiFi interface), then it needs several IPv6 addresses. In general, an IPv6 unicast address is structured as shown in the figure below.

.. figure:: fig/network-fig-073-c.png
   :align: center
   
   Structure of IPv6 unicast addresses

An IPv6 unicast address is composed of three parts :

 #. A global routing prefix that allows to identify the Internet Service Provider that owns this block of addresses
 #. A subnet identifier that identifies a customer of the ISP
 #. An interface identifier that identifies particular interface on an endsystem 
In today's deployments, interface identifiers are always 64 bits wide. This implies that while there are :math:`2^{128}` different IPv6 addresses, these must be grouped in :math:`2^{64}` subnets. This could appear as a waste of resources, however using 64 bits for the host identifier allows IPv6 addresses to be autoconfigured and also provides some benefits from a security viewpoint as will be explained in section ICMPv6_


.. sidebar:: Textual representation of IPv6 addresses

 It is sometimes necessary to write IPv6 addresses in text format, e.g. when configuring manually addresses of for documentation purposes. The preferred format  is `x:x:x:x:x:x:x:x`, where the `x` are hexadecimal digits of the eight 16-bit parts of the address. Example IPv6 address :

  - ABCD:EF01:2345:6789:ABCD:EF01:2345:6789
  - 2001:DB8:0:0:8:800:200C:417A
  - FE80:0:0:0:219:E3FF:FED7:1204

 IPv6 addresses often contain long sequence of bits set to `0`. In this case, a compact notation has been defined. With this notation, `::` is used to indicate one or more groups of 16 bits blocks containing only bits set to `0`. For example, 
 
  - 2001:DB8:0:0:8:800:200C:417A  is represented as  `2001:DB8::8:800:200C:417A`
  - FF01:0:0:0:0:0:0:101   is represented as `FF01::101` 
  - 0:0:0:0:0:0:0:1 is represented as `::1`
  - 0:0:0:0:0:0:0:0 is represented as `\:\:`

 An IPv6 prefix can be represented as `address/length` where `length` is the length of the prefix in bits. For example, the three notations below correspond to the same IPv6 prefix :

  - 2001:0DB8:0000:CD30:0000:0000:0000:0000/60
  - 2001:0DB8::CD30:0:0:0:0/60
  - 2001:0DB8:0:CD30::/60

.. index:: Provider Independant address
.. index:: Provider Aggregatable address

There are in practice several types of IPv6 unicast address. Most of the `IPv6 unicast addresses <http://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml>`_ are allocated in blocks under the responsibilities of IANA_ The current IPv6 allocations are part of the `2000::/3` address block. Regional Internet Registries (RIR) such as RIPE_ in Europe,  ARIN_ in North-America or AfriNIC in Africa have each received a `block of IPv6 addresses <http://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xhtml>`_ that they suballocate to Internet Service Providers in their region.  The ISPs then suballocate addresses to their customers. 

When considering the allocation of IPv6 addresses, two types of address allocations are often distinguished. The RIRs allocate `provider-independant (PI)` addresses. PI addresses are usually allocated to Internet Service Providers and large companies that are connected to at least two different ISPs [CSP2009]_. Once a PI address block has been allocated to a company, this company can use its address block with the provider of its choice and change of provider at will. Internet Service Providers allocate `provider-aggregatable (PA)` address blocks from their own PI address block to their customers. A company that is connected to only one ISP can only use PA addresses. The drawback of PA addresses is that when a company using a PA address block changes of provider, it needs to change all the addresses that it uses. This can be a nightmare from an operational viewpoint and many companies are lobbying to obtain `PI` address blocks even if they are small and connected to a single provider. The typical size of the IPv6 address blocks are :

 - /32 for an Internet Service Provider
 - /48 for a single company
 - /64 for a single user (e.g. a home user connected via ADSL) 
 - /128 in the rare case when it is known that no more than one endhost will be attached

.. index:: Unique Local Unicast

For the companies that want to use IPv6 without being connected to the IPv6 Internet, :rfc:`4193` defines the `Unique Local Unicast (ULA)` addresses (`FC00::/7`). These ULA addresses play a similar role as the private IPv4 addresses defined in :rfc:`1918`. However, the size of the `FC00::/7` address block allow ULA to be much more flexible than private IPv4 addresses.

Furthermore, the IETF has reserved some IPv6 addresses for a special usage. The two most important ones :

 - `0:0:0:0:0:0:0:1` (`::1` in compact form) is the IPv6 loopback address. This is the address of a logical interface that is always up and runing on IPv6 enabled hosts. This is the equivalent of 127.0.0.1 in IPv4.
 - `0:0:0:0:0:0:0:0` (`\:\:` in compact form) is the unspecified IPv6. This is the IPv6 address that a host can use as source address when trying to aquire an official address.

.. index:: Link Local address

The last type of unicast IPv6 addresses are the `Link Local Unicast` addresses. These addresses are part of the `FE80::/10` address block and are defined in:rfc:`4291`. Each host can compute its own link local address by concatenating the `FE80::/64` prefix with the 64 bits identifier of its interface. Link local addresses can be used when hosts that are attached to the same link (or local area network) need to exchange packets. They are used notably for address discovery and autoconfiguration purposes. Their usage is restricted to each link and a router cannot forward a packet having a link local address as source or destination address. 

.. figure:: fig/network-fig-073-c.png
   :align: center
   
   IPv6 link local address structure

An important consequence of the IPv6 unicast addressing architecture and the utilisation of link-local addresses is that an IPv6 host will have several IPv6 addresses. This implies that an IPv6 stack must be able to handle multiple IPv6 addresses. This was not always the case with IPv4.

:rfc:`4291` defines a special type of IPv6 anycast address. On a subnetwork having prefix `p/n`, the IPv6 address whose `128-n` low-order bits are set to `0` is the anycast address that corresponds to all routers inside this subnetwork. This anycast address can be used by hosts to quickly send a packet to any of the routers inside their own subnetwork.

Finally, :rfc:`4291` defines the structure of the IPv6 multicast addresses [#fmultiiana]_. This structure is depicted in the figure below

.. figure:: fig/network-fig-075-c.png
   :align: center
   
   IPv6 multicast address structure

The low order 112 bits of an IPv6 multicast address are the group's identifier. The high order bits are used as a marker to distinguish multicast addresses from unicast addresses. The 4 bits flag field indicates notably whether the address is temporary or permanent. Finally, the second indicates the boundaries of the forwarding of packets destined to a particular address. A link-local scope indicates that a router should not forward a packet destined to such a multicast address. An organisation local-scope indicates that a packet with the corresponding multicast address should not leave a company. Finally the global scope is intended for multicast groups spanning the global Internet.

Among these addresses some are well known. For example, all endsystem automatically belong to the `FF02::1` multicast group while all routers automatically belong to the `FF02::2` multicast group.

.. _IPv6Packet:

IPv6 packet format
------------------

The IPv6 packet format was heavily inspired by the packet format proposed for the SIPP protocol in :rfc:`1710`. The standard IPv6 header defined in :rfc:`2460` occupies 40 bytes and contains 8 different fields as shown in the figure below.

.. figure:: fig/network-fig-077-c.png
   :align: center
   
   The IP version 6 header

Besides the source and destination addresses of the packet, the IPv6 header contains the following fields :

 - `version` : a 4 bits field set to `6` and intended to allow IP to evolve in the future if needed
 - `Traffic class` : this 8 bits field plays a similar role as the `DSCP` in the IPv4 header
 - `Flow label` : this field was initially intended to be used to tags packets belonging to the same `flow`. However, as of this writing, the flow label is rarely used in practice
 - `Payload length` : this is the size of the IPv6 payload in bytes. As the length is encoded as a 16 bits field, an IPv6 packet can contain up to 65535 bytes of payload.
 - `Next Header` : this 8 bits field indicates the type [#fianaprotocol]_ of header that follows the IPv6 header. It can be a transport layer header (e.g. `6` for TCP or `17` for UDP) or an IPv6 option. Handling options as a next header allows to simplify the processing of IPv6 packets compared to IPv4.
 - `Hop Limit` : this 8 bits field indicates the number of routers that can forward the packet. It is decremented by one by each router and servers that same purpose as the TTL field of the IPv4 header.

In comparison with IPv4, the IPv6 is much simpler and easier to process by a router. A first important difference is that there is no checksum inside the IPv6 header. This is mainly because all datalink layers and transport protocols include a checksum or a CRC to protect their frames/segments against transmission errors. Adding a checksum in the IPv6 header would have forced each router to recompute the checksum off all packets, with a limited benefit in detecting errors. In practice, an IP checksum allows to catch errors that occur inside routers (e.g. due to memory corruption) before the packet reaches its destination. However, this benefit was found to be too small given the reliability of current memories and the cost of computing the checksum on each router.

A second difference with IPv4 is that the IPv6 header does not support fragmentation and reassembly. The experience with IPv4 has shown that fragmenting packets in routers was costly [KM1995]_ and the developers of IPv6 have decided that routers would not fragment packets anymore. If a router receives a packet that is too long to be forwarded, the packet is droppted and the rotuer returns an ICMPv6 messages to inform the sender of the problem and allow it to either fragment the packet or perform Path MTU discovery. In IPv6, packet fragmentation is performed by the source by using IPv6 options.

The third difference are the IPv6 options that are simpler and easier to process than the IPv4 options.

.. sidebar:: Header compression on low bandwidth links

 Given the size of the IPv6 header, it can cause a huge overhead on low bandwidth links, especially when small packets are exchanged such as for Voice over IP applications. In such environments, several techniques are used to reduce the overhead. A first solution is to use data compression in the datalink layer to compress all the information exchanged [Thomborson1992]_. A second solution is to compress the IP and TCP header. These header compression techniques, such as the one defined in :rfc:`2507` take advantage of the redundancy found in successive packets from the same flow to reduce significantly the size of the protocol headers. Another solution is to define a compressed encoding of the IPv6 header that matches the capabilities of the underlying datalink layer :rfc:`4944`. 


.. _IPv6Options:

IPv6 options
------------

In IPv6, each option is considered as one header that contains a multiple of 8 bytes to ensure that IPv6 options in a packet are aligned on 64 bits boundaries. IPv6 defines several types of options :

 - the hop-by-hop options are the options that must be processed by the routers on the path followed by a packet
 - the type 0 routing header that is similar to the IPv4 loose source routing option
 - the fragmentation option that is used when fragmenting an IPv6 packet
 - the destination options 
 - the security options that allow IPv6 hosts to exchanged packet with cryptographic authentication (AH header) or encryption and authentication (ESP header)

:rfc:`2460` provides lots of details on the encodings of different types of options. In this section, we only discus some of them. The reader may consult :rfc:`2460` for more information about the other options. The first point to note is that each option contains a `Next Header` field that indicates the type of the next header that follows the option. A second point to note is that to allow routers to efficiently parse IPv6 packets, the options that must be processed by routers (hop-by-hop options and type 0 routing header) must appear first in the packet. This allows the router to process a packet without being forced to analyse all the packet's options. A third point to note is that hop-by-hop and destination options are encoded by using a `type length value` format. Furthermore, the `type` field includes bits that indicate whether a router that does not understand this option should ignore the option or discard the packet. This allows to introduce new options in the network without forcing all routers to be upgraded at the same time.

.. index:: jumbogram

Two `hop-by-hop` options have been defined. :rfc:`2675` specifies the jumbogram that enables IPv6 to support packets containing a payload larger than 65535 bytes. These jumbo packets have their `payload length` set to `0` and the jumbogram option contains the packet length as a 32 bits field. Such packets can only be sent from a source to a destination if all the routers on the path support this option. However, as of this writing it does not seem that the jumbogram option has been implemented. The router alert option defined in :rfc:`2711` is the second example of `hop-by-hop` option. The packets that contain this option should be processed in a special way by the intermediate routers. This option is used for IP packets that carry Resource Reservation Protocol (RSVP) messages that must be processed by intermediate routers.

.. sidebar:: The security risk of hop-by-hop options


The type 0 routing header defined in :rfc:`2460` is an example of an IPv6 option that must be processed by some routers. This option is encoded as shown below.

.. figure:: fig/network-fig-079-c.png
   :align: center
   
   The Type 0 routing header

The type 0 routing was intended to allow a host to indicate a loose source router that should be followed by a packet by specifying the addresses of some of the routers that must forward this packet. Unfortunately, furtherwork with this routing header, including an entertaining demonstration with scapy_ [BE2007]_ revealed some severe security problems with this routing header. For this reason, loose source routing with the type 0 routing header has been removed from the IPv6 specification :rfc:`5095`.
  
.. index:: IPv6 fragmentation

In IPv6, fragmentation is performed exclusively by the source host and relies on the fragmentation header. This 64 bits header is composed of six fields.

 - a `Next Header` field that indicates the type of the header that follows the fragmentation header
 - a `reserved` field set to `0`. 
 - the `Fragment Offset` is a 13-bit unsigned integer that contains the offset, in 8-octet units, of the data following this header, relative to the start of the original packet. 
 - the `More` flag that is set to `0` in the last fragment of a packet and to `1` in all other fragments. 
 - the 32 bits `Identification` field indicates to which original packet a fragment belongs. When a host sends fragmented packets, it should ensure that it does not reuse the same `identification` field for packets sent to the same destination during a period of `MSL` seconds. This is easier with the 32 bits `identification` used in the IPv6 fragmentation header, than with the 16 bits `identification` field of the IPv4 header.

Some implementations send the fragments in increasing fragment offset order, starting from the first fragment. Others send the fragments in reverse order, starting from the last fragment. The latter solution can be advantageous for the host that needs to reassemble the fragments it can easily allocate the buffer that is required to reassemble all fragments of the packet. When a host receives the first fragment of an IPv6 packet, it cannot know a priori the length of the entire IPv6 packet. 

The figure below provides an example of the fragmentation of an IPv6 packet containing a UDP segment in two IPv6 fragments. The `Next Header` type reserved for the IPv6 fragmentation option is 44. 

.. figure:: fig/network-fig-087-c.png
   :align: center
   :scale: 50
   
   IPv6 fragmentation example

Finally, the last type of IPv6 options are the Encaspulating Security Payload (ESP) defined in :rfc:`4303` and the Authentication Header (AH) defined in :rfc:`4302`. These two headers are used by IPSec :rfc:`4301`. They will be discussed in another chapter.

IPv6 packet forwarding
----------------------

describe operation of a router when a packet is received with pseudocode without options
ignore tclass, flowlabel
longest prefix match forwarding like ipv4
subnet addresses should be up to /64, but routers cannot assume this

.. _ICMPv6:

ICMP version 6
==============

ICMPv6 defined in :rfc:`4443` is the companion protocol for IPv6 as ICMPv4 is the companion protocol for IPv4. ICMPv6 is used by routers to report problems when forwarding IPv6 packets. However, as we will see in section IPEthernet_, ICMPv6 is also used when autoconfiguring addresses.

The traditional utilisation of ICMPv6 is similar to ICMPv4. ICMPv6 messages are carried inside IPv6 packets (the `Next Header` field for ICMPv6 is 58). Each ICMP message contains an 8 bits header with a `type` field, a `code` field and a 16 bits checkcum computed over the entire ICMPv6 message. The message body contains a copy of the IPv6 packet in error.

.. figure:: fig/network-fig-088-c.png
   :align: center
   
   ICMP version 6 packet format

ICMPv6 specifies two classes of messages : error messages that indicate a problem in handling a packet and informational messages. Four types of error messages are defined in :rfc:`4443` :

 - 1 : Destination Unreachable. Such an ICMPv6 message is sent when the destination address of a packet is unreachable. The `code` field of the ICMP header contains additional information about the type of unreachability. The following codes are specified in :rfc:`4443` :

     - 0 : No route to destination. This indicates that the router that sent the ICMPv6 message did not have a route
     - 1 : Communication with destination administratively prohibited. This indicates that a firewall has refused to forward the packet towards its destination. Types 5 and 6
     - 2 : Beyond scope of source address. This message can be sent if the source is using link-local addresses to reach a global unicast address outside its subnet.
     - 3 : Address unreachable. This messages indicates that the packet reached the subnet of the destination, but the host that own this destination address is not reachaed.
     - 4 : Port unreachable. This message indicates that the IPv6 packet was received by the destination, but 

 - 2 : Packet Too Big. The router that sends the ICMPv6 message received an IPv6 packet that is larger than the MTU of the outgoing link. The ICMPv6 messages contains the MTU of this link in bytes. This allows the sending host to implement Path MTU discovery :rfc:`1981`
 - 3 : Time Exceeded. This error message can be sent either by a router or by a host. A router would set `code` to `0` to report the reception of a packet with its `Hop Limit` set to `0`. A host would set `code` to `1` to report that it was unable to reassemble IPv6 fragments received.
 - 4 : Parameter Problem. This ICMPv6 messages is used to report either the reception of an IPv6 packet with an erroneous header field (type `0`) or an unknown `Next Header` or IP option (types `1` and `2`). In this case, the message body contains the erroneous IPv6 packet and the first 32 bits word of the message body is a pointer to the error.

Two types of informational ICMPv6 messages are in :rfc:`4443` : `echo request` and `echo reply` that are used to test the reachability of a destination by using :manpage:`ping6(8)`.

.. send after Ethernet

.. sidebar:: Rate limitation of ICMP messages

 High-end harward based routers use special purpose chips on their interfaces to be able to forward IPv6 packets at line rate. These chips are optimised to process `correct` IP packets. These chips are not able to create an ICMP message. When they receive an IP packet that will trigger an ICMP message, they interrupt the main CPU of the router and the software running on this CPU processes the packet. This CPU is much slower than the hardware acceleration found on the interfaces [Gill2004]_. It would be overload if it had to process IP packets at line rate and generate one ICMP message for each receive packet. To protect this CPU, high-end routers limit the rate at which the hardware can interrupt the main CPU and thus the rate at which ICMP messages can be generated. This implies that not all erroneous IP packets will cause the transmission of an ICMP message. The risk of overloading the main CPU of the router is also the reason why using hop-by-hop IPv6 options, including the router alter option is discouraged [#falert]_. 


.. index:: Middlebox

Middleboxes
===========

When the TCP/IP architecture and the IP protocol was defined, two types of devices were considered in the network layer : endhosts and routers. Endhosts are the sender and receiver of IP packets while routers forward IP packets. When a router forwards an IP packet, it consults its FIB, updates the packets's TTL, recomputes its checksum and forward it to the nexthop. A router does not need to read nor change the contents of the packet's payload.

However, in today's Internet, there exist devices that are not strictly routers but process, sometimes modify and forward IP packets. These devices are often called `middleboxes` :rfc:`3234`. Some middleboxes operate only in the network layer, but most middleboxes are able to analyse the payload of the received packets and extract the transport header and in some cases the application layer protocol. 
  

.. figure:: fig/network-fig-161-c.png
   :align: center
   
   IP middleboxes and the reference model

In this section, we briefly analyse two types of middleboxes : firewalls and network address translation (NAT) devices. A longer list of middleboxes with references may be found in :rfc:`3234`.

not part of the architecture, but added due to practical reasons, most important are nat and firewalls, but also shapers, DPI, ...

.. index:: Network Address Translation, NAT


Firewalls
---------

[CB2003]_ 
    




NAT
---

NAT : Paul :rfc:`1631`

normal, nat-pt

:rfc:`2993`

   [RFC2993]   Hain, T., "Architectural Implications of NAT", RFC 2993,
               November 2000.

:rfc:`3027`

   [RFC3027]   Holdrege, M. and P. Srisuresh, "Protocol Complications
               with the IP Network Address Translator (NAT)", RFC 3027,
               January 2001.

   [RFC2663]   Srisuresh, P. and M. Holdrege, "IP Network Address
               Translator (NAT) Terminology and Considerations", RFC
               2663, August 1999.

:rfc:`3022`

   [RFC3022]   Srisuresh, P. and K. Egevang, "Traditional IP Network
               Address Translator (Traditional NAT)", RFC 3022, January
               2001.


load balancer
-------------


Intradomain routing in IP networks 
==================================


RIP
---

"Command"
 1 : Request
 2 : Response

Version
 1 : Prehistoric 
 2 : Usable

Authentication
Authentication
Optional. Configure all routers
with the same password. Slightly improves security

Distance vector
One Route Entry (20 bytes)
for each route to be advertised

ripng : rfc:`2080`

port 521 UDP

16=infinity


.. figure:: fig/network-fig-094-c.png
   :align: center
   
   RIP message format


.. figure:: fig/network-fig-095-c.png
   :align: center
   
   Format of the RIP route entries

RIP multiprotocol with support for IPX, XNS, etc.

address family http://www.iana.org/assignments/address-family-numbers/



ICMP version 6 



:rfc:`2453`

La version actuelle de RIP East définie dans 
RFC2453 RIP Version 2. G. Malkin. November 1998

Une autre description de RIP East disponible dans : 
Gary Malkin, RIP : an intra-domain routing protocol, Addison-Wesley, 2002 

IP multicast East couvert dans le cours avancé. A ce stade, il suffit de considérer IP multicast (avec TTL=1) comme étant un mécanisme permettant à un routeur connecté sur un réseau local d'envoyer, en une seule transmission, un paquet qui sera reçu par tous les routeurs RIP connectés à ce réseau local.

The Synchronization of Periodic Routing Messages , Floyd, S., and Jacobson, V. IEEE/ACM Transactions on Networking, V.2 N.2, p. 122-136, April 1994.

OSPF
----
Pour plus d'informations sur OSPF, voir 
:rfc:`2328` OSPF Version 2. J. Moy. April 1998.
ou
J. Moy, OSPF: Anatomy of an Internet Routing Protocol, Addison Wesley, 1998

Interdomain routing in the Internet
===================================

:rfc:`2622`

RFC 2622 Routing Policy Specification Language (RPSL). C. Alaettinoglu, C.
     Villamizar, E. Gerich, D. Kessens, D. Meyer, T. Bates, D. Karrenberg,
     M. Terpstra. June 1999.

:rfc:`2650`

RFC 2650 Using RPSL in Practice. D. Meyer, J. Schmitz, C. Orange, M.
     Prior, C. Alaettinoglu. August 1999.

Internet Routing Registries contain the routing policies of various ISPs, see :

http://www.ripe.net/ripencc/pub-services/whois.html
http://www.arin.net/whois/index.html
http://www.apnic.net/apnic-bin/whois.pl

 L. Subramanian, S. Agarwal, J. Rexford, and RH Katz. Characterizing the Internet hierarchy from multiple vantage points. In IEEE INFOCOM, 2002


but see recent arbor data


.. rubric:: Footnotes

.. [#fclasses] In addition to the A, B and C classes, :rfc:`791` also defined the `D` and `E` classes of IPv4 addresses. Class `D` (resp. `E`) addresses are those whose high order bits are set to `1110` (resp. `1111`). Class `D` addresses are used by IP multicast and will be explained later. Class `E` addresses are currently unused, but there are some discussions on possible future utsages [WMH2008]_ [FLM2008]_

.. [#fnetmask] Another way of representing IP subnets is to use netmasks. A netmask is a 32 bits field whose `p` high order bits are set to `1` and the low order bits are set to `0`. The number of high order bits set `1` indicates the length of the subnet identifier. Netmasks are usually represented in the same dotted decimal format as IPv4 addresses. For example `10.0.0.0/8` would be represented as `10.0.0.0 255.0.0.0` while `192.168.1.0/24` would be represented as `192.168.1.0 255.255.255.0`. In some cases, the netmask can be represented in hexadecimal.

.. [#funnunmbered] A point-to-point link to which no IPv4 address has been allocated is called an unnumbered link. See :rfc:`1812` section 2.2.7 for a discussion of such unnumbered links.

.. [#finitialttl] The initial TTL value used to send IP packets vary from one implementation to another. Most current IP implementations use an initial TTL of 64 or more. See http://members.cox.net/~ndav1/self_published/TTL_values.html for additional information.

.. [#fpingproblems] Until a few years ago, all hosts replied to `Echo request` ICMP messages. However, due to the security problems that have affected TCP/IP implementations, many of these implementations can now be configured to disable answering `Echo request` ICMP messages. 

.. ping of death http://insecure.org/sploits/ping-o-death.html

.. [#fciscoags] Example routers from this period include the Cisco AGS http://www.knossos.net.nz/don/wn1.html and AGS+ http://www.ciscopress.com/articles/article.asp?p=25296

.. [#fmultiiana] The full list of allocated IPv6 multicast addresses is available at http://www.iana.org/assignments/ipv6-multicast-addresses

.. [#fianaprotocol] The IANA_ maintains the list of all allocated Next Header types at http://www.iana.org/assignments/protocol-numbers/ The same registry is used for the IPv4 protocol field and for the IPv6 Next Header.

.. [#falert] For a discussion of the issues with the router alert IP option, see http://tools.ietf.org/html/draft-rahman-rtg-router-alert-dangerous-00 or
 http://tools.ietf.org/html/draft-rahman-rtg-router-alert-considerations-03

.. include:: ../links.rst
