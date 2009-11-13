================== 
The network layer
==================



Principles 
###########


.. figure:: fig/network-fig-001-c.png
   :align: center
   :scale: 70
   
   The network layer in the reference model


routers


types of datalink
- point to point
- local area networks

TODO
explain addresses in the datalink layer for LANs !!!! then ARP can be explained in this chapter as well

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
and using Dijkstra for shortest path computation

Internet Protocol
#################

The Internet Protocol (IP) is the network layer protocol of the TCP/IP protocol suite. IP allows the applications running above the transport layer (UDP/TCP) to use a wide range of heterogeneous datalink layers. IP was designed when most point-to-point links were telephone lines with modems. Since then, IP has been able to use Local Area Networks (Ethernet, Token Ring, FDDI, ...), new wide area data link layer technologies (X.25, ATM, Frame Relay, ...) and more recently wireless networks (802.11, 802.15, UMTS, GPRS, ...). The flexibility  of IP and its ability to use various types of underlying data link layer technologies is one of its key advantages.

.. figure:: fig/network-fig-051-c.png
   :align: center
   :scale: 70

   IP and the reference model

.. there is a draft on expectations of lower layer

The current version of IP is version 4 specified in :rfc:`791`. We first describe this version and later explain IP version 6 that is expected to replace IP version 4 in the future.

IP version 4
============

IP version 4 is the data plane protocol of the network layer in the TCP/IP protocol suite. The design of IP version 4 was based on the following assumptions :

 - IP will provide an unreliable connectionless service (reliability will be provided by TCP when needed)
 - IP will operate with the datagram transmission mode
 - IP addresses will have a fixed size of 32 bits 
 - IP will be used above different types of datalink layers
 - IP hosts will exchange variable length packets

The addresses are an important part of any network layer protocol. In the late 1970s, the developers of IPv4 designed IPv4 for a research network that would interconnect some research labs and universities. For this utilisation, 32 bits wide addresses were much larger than the expected number of hosts on the network. Furthermore, 32 bits was a nice address size for software-based routers. None of the developers of IPv4 were expecting that IPv4 would become as widely used as it is today.


IPv4 addresses are encoded as a 32 bits field. IPv4 addresses are often represented in `dotted-decimal` format as a sequence of four integers separated by a `dot`. The first integer is the decimal representation of the most significant byte of the 32 bits IPv4 address, ... For example, 

 * 1.2.3.4 corresponds to 00000001000000100000001100000100
 * 127.0.0.1 corresponds to 01111111000000000000000000000001
 * 255.255.255.255 corresponds to 11111111111111111111111111111111

.. index:: multihomed host

An IPv4 address is used to identify an interface on a router or a host. A router has thus as many IPv4 addresses as the number of interfaces that it has in the datalink layer. Most hosts have a single datalink layer interface and thus have a single IPv4 address. However, with the growth of wireless, more and more hosts have several datalink layer interfaces (e.g. an Ethernet interface and a WiFi interface). These hosts are said to be `multihomed`. A multihomed host with two interfaces has thus two IPv4 addresses.

An important point to be defined in a network layer protocol is the allocation of the network layer addresses. A naive allocation scheme would be to provide an IPv4 address to each host when the host is attached to the Internet on a first come first served basis. With this solution, a host in Belgium could have address 2.3.4.5 while another host located in Africa would use address 2.3.4.6. Unfortunately, this would force all routers to maintain a route for all hosts. The figure below shows a simple enterprise networks with two routers and three hosts and the associated routing tables if such isolated addresses were used.

.. figure:: fig/network-fig-056-c.png
   :align: center
   :scale: 70
   
   Scalability issues when using isolated IP addresses 

.. index:: IP subnet, IP prefix, subnet mask


To preserve the scalability of the routing system, it is important to minimize the number of routes that are stored on each router. A router cannot store and maintain one route for each of the almost 1 billion hosts that are connected to today's Internet. Routers should only maintain routes towards blocks of addresses and not towards individual hosts. For this, hosts are grouped in `subnets` based on their location in the network. A typical subnet will group all the hosts that are part of the same enterprise. An entreprise network is usually composed of several LANs interconnected by routers. A small block of addresses from the entreprise's block is usually assigned to each LAN. An IPv4 address is composed of two parts : a `subnetwork identifier` and  a `host identifier`. The `subnetwork identifier` is composed of the high order bits of the address and the host identifier is encoded in the low order bits of the address. This is illustrated in the figure below.

.. figure:: fig/network-fig-054-c.png
   :align: center
   :scale: 70
   
   The subnetwork and host identifiers inside an IPv4 address

.. index:: Class A IPv4 address, Class B IPv4 address, Class C IPv4 address

When a router needs to forward a packet, it must know the `subnet` of the destination address to be able to consult its forwarding table to forward the packet. :rfc:`791` proposed to use the high-order bits of the address to encode the length of the subnet identifier. This lead to the definition of three `classes` of unicast addresses [#fclasses]_

=======  ==========  =========  =============	=============
Class    High-order  Length of  Number of	Addresses per
         bits        subnet id	networks   	network
=======  ==========  =========  =============	=============
Class A	 `0`	     8 bits	128 		16,777,216 (:math:`2^{24}`)	
Class B	 `10`        16 bits	16,384     	65,536 (:math:`2^{16}`)	
Class C	 `110`	     24 bits	2,097,152  	256 (:math:`2^8`)
=======  ==========  =========  =============	=============

However, these three classes of addresses were not flexible enough. A class `A` subnet was too large for most organisations and a class `C` subnet was too small. Flexibility was added by the introduction of `variable-length subnets` in :rfc:`1519`. With `variable-length` subnets, the subnet identifier can have any size from `1` to `31` bits. `Variable-length` subnets allow the network operators to use a subnet that matches the number of hosts that will be placed inside the subnet. A subnet identifier or IPv4 prefix is usually [#fnetmask]_ represented as `A.B.C.D/p` where `A.B.C.D` is the network address obtained by concatenating the subnet identifier with a host identifier containing only `0` and `p` is the length of the subnet identifier in bits. The table below provides examples of IP subnets.

============== 	==========  ============  ===============
Subnet      	Number of   Smallest      Highest
	    	addresses   address	  address
============== 	==========  ============  ===============
10.0.0.0/8  	16,777,216  10.0.0.0      10.255.255.255	
192.168.0.0/16	65,536	    192.168.0.0   192.168.255.255
198.18.0.0/15	131,072	    198.18.0.0 	  198.19.255.255
192.0.2.0/24	256	    192.0.2.0 	  192.0.2.255
10.0.0.0/30	4	    10.0.0.0	  10.0.0.3
10.0.0.0/31	2	    10.0.0.0	  10.0.0.1
============== 	==========  ============  ===============


The figure below provides a simple example of the utilisation of IPv4 subnets in an enterprise network. The length of the subnet identifier assigned to a LAN will usually depend on the expected number of hosts attached to the LAN. For point-to-point links, many deployments have used `/30` prefixes, but recent routers are now using `/31` subnets on point-to-point links :rfc:`3021` or even do not use IPv4 addresses on such links [#funumbered]_. 
 
.. figure:: fig/network-fig-056-c.png
   :align: center
   :scale: 70
   
   IP subnets in a simple enterprise network

A second issue concerning the addresses of the network layer is the allocation scheme that is used to allocated blocks of addresses to organisations. The first allocation scheme was based on the different classes of addresses. The pool of IPv4 addresses was managed by a secretariat that allocated address blocks on a first-come first served basis. Large organisations such as IBM, BBN, but also Stanford or the MIT were able to obtain a class `A` address block. Most organisations requested a class `B` address block that contains 65536 addresses, which was suitable for most enterprises and universities. The table below provides examples of some IPv4 address blocks in the class `B` space. 

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

However, the Internet was a victim of its own success and in the late 1980s, many organisations were requesting blocks of IPv4 addresses and connected to the Internet. Most of these organisations requested class `B` address blocks because class `A` address were too large and in limited supply while class `C` address blocks were considered to be too small. Unfortunately, there were only 16,384 different class `B` address blocks and this address space was being consumed were quickly. Furthermore, the routing tables maintained by the routers were growing quickly and some routers had difficulties in maintaining all these routes in their limited memory [#fciscoags]_.

.. figure:: fig/network-fig-162-c.png
   :align: center
   :scale: 70
   
   Evolution of the size of the routing tables on the Internet (Jul 1988- Dec 1992 - source : :rfc:`1518`)

.. index:: Classless Interdomain Routing

Faced with these two problems, the Internet Engineering Task Force decided to develop the Classless Interdomain Routing (CIDR) architecture :rfc:`1518`. This architecture aims at allowing IP routing to scale better than the class-based architecture. CIDR contains three important modifications compared to :rfc:`791`.

      1. IP address classes are deprecated. All IP equipments must use and support variable-length subnets.
      2. IP address blocks are not allocated anymore on a first-come-first-served basis. Instead, CIDR introduces a hierarchical address allocation scheme.
      3. IP routers must use longest-prefix match when they lookup a destination address in their forwarding table


The last two modifications were introduced to improve the scalability of the IP routing system. The main drawback of the first-come-first-served address block allocation scheme was that neighboring address blocks were allocated to very different organisations and conversely, very different address blocks were allocated to similar organisations. With CIDR, address blocks are allocated by Regional IP Registries (RIR) in an aggregatable manner. A RIR is responsible for a large block of addresses and a region. For example, RIPE_ is the RIR that is responsible for Europe. A RIR allocates smaller address blocks from its large block to Internet Service Providers :rfc:`2050`. Internet Service Providers then allocate smaller address blocks to their customers, ... When an organisation requests an address block, it must prove that it already has or expects to have in the near future, a number of hosts or customers that is equivalent to the size of the requested address block. 

The main advantage of this hierarchical address block allocation scheme is that it allows the routers to maintain fewer routes. For example, consider the address blocks that were allocated to some of the Belgian universities as shown in the table below.

==============            =============================================
Address block   	  Organisation
==============            =============================================
130.104.0.0/16 		  Université catholique de Louvain
134.58.0.0/16		  Katholiek Universiteit Leuven
138.48.0.0/16		  Facultés universitaires Notre-Dame de la Paix
139.165.0.0/16		  Université de Liège
164.15.0.0/16		  Université Libre de Bruxelles
==============            =============================================

These universities are all connected to the Internet exclusively via  `Belnet <http://www.belnet.be>`_. As each university has been allocated a different address block, the routers of the `Belnet <http://www.belnet.be>`_ must announce one route for each university and all routers on the Internet must maintain a route towards each university. In contrast, consider all the high schools and the government institutions that are connected to the Internet via `Belnet <http://www.belnet.be>`_. An address block was assigned to these institutions after the introduction of CIDR in the `193.190.0.0/15` address block owned by `Belnet <http://www.belnet.be>`_. With CIDR, `Belnet <http://www.belnet.be>`_ can announce a single route towards `193.190.0.0/15` that covers all these high schools. 

 
.. index:: multihomed network

However, there is one difficulty with the aggregatable variable length subnets used by CIDR. Consider for example `FEDICT <http://www.fedict.be>`_, a governmental institution that uses the `193.191.244.0/23` address block. Assume that in addition to being connected to the Internet via `Belnet <http://www.belnet.be>`_ , `FEDICT <http://www.fedict.be>`_ also wants to be connected to another Internet Service Provider. The FEDICT network is then said to be multihomed. This is shown in the figure below.

.. figure:: fig/network-fig-163-c.png
   :align: center
   :scale: 70
   
   Multihoming and CIDR

With such a multihomed network, routers `R1` and `R2` would have two routes towards IPv4 address `193.191.245.88` : one route via Belnet (`193.190.0.0/15`) and one direct route  (`193.191.244.0/23`). Both routes match IPv4 address `193.192.145.88`. Since :rfc:`1519` when a router knows several routes towards the same destination address, it must forward packets along the route having the longest prefix length. In the case of `193.191.245.88`, this is the route `193.191.244.0/23` that will be followed to forward the packet. This forwarding rule is called the `longest prefix match` or the `more specific match`. All IPv4 routers implement this forwarding rule.

The understand the `longest prefix match` forwarding, consider the figure below. With this rule, the route `0.0.0.0/0` plays a particular role. As this route has a prefix length of `0` bits, it will match all destination addresses. This route is often called the `default` route. 
 - a packet with destination `192.168.1.1` received by router `R` is destined to the router itself. It will be delivered to the approriate transport protocol.
 - a packet with destination `11.2.3.4` matches two routes : `11.0.0.0/8` and `0.0.0.0/0`. The packet will be forwarded on the `West` interface.
 - a packet with destination `130.4.3.4` matches one route : `0.0.0.0/0`. The packet will be forwarded on the `North` interface.
 - a packet with destination `4.4.5.6` matches two routes : `4.0.0.0/8` and `0.0.0.0/0`. The packet will be forwarded on the `West` interface.
 - a packet with destination `4.10.11.254` matches three routes : `4.0.0.0/8`, `4.10.11.0/24 and `0.0.0.0/0`. The packet will be forwarded on the `South` interface.


.. figure:: fig/network-fig-067-c.png
   :align: center
   :scale: 70
   
   Longest prefix match example 


The longest prefix match can be implemented by using different data structures. One possibility is to use a trie. The figure below shows a trie that encodes six routes having different outgoing interfaces.


.. figure:: fig/network-fig-068-c.png
   :align: center
   :scale: 70
   
   A trie representing a routing table 


.. index :: 0.0.0.0, 127.0.0.1, private IPv4 addresses, link local IPv4 addresses

.. sidebar:: Special IPv4 addresses

 Most unicast IPv4 addresses can appear as source and destination addresses in packets on the global Internet. However, it is worth to note that some  blocks of IPv4 addresses have a special usage as described in :rfc:`3330`. These include :

  - `0.0.0.0/8` that is reserved for self-identification. A common address in this block is `0.0.0.0` that is sometimes used when a host boots and does not yet know its IPv4 address.
  - `127.0.0.0/8` that is reserved for loopback addresses. Each host implementing IPv4 must have a loopback interface (that is not attached to a datalink layer). By convention, IPv4 address `127.0.0.1` is assigned to this interface. This allows processes running on a host to use TCP/IP to contact other processes running on the same host. This can be very useful for testing purposes. 
  - `10.0.0.0/8`, `172.16.0.0/12` and `192.168.0.0/16` are reserved for private networks that are not directly attached to the Internet. These addresses are often called private addresses or :rfc:`1918` addresses. 
  - `169.254.0.0/16` is used for link-local addresses :rfc:`3927`. Some hosts use an address in this block when they are connected to a network that does not allocate addresses as expected. 




IPv4 packets
------------

Now that we have clarified the allocation of IPv4 addresses and the utilisation of the longest prefix match to forward IPv4 packets, we can have a more detailed look at IPv4 by starting with the format of the IPv4 packets. The IPv4 packet format was defined in :rfc:`791`. Besides a few clarifications and some backward compatible changes, the IPv4 packet format did not change significantly since the publication of :rfc:`791`. All IPv4 packets use the 20 bytes header shown below. Some IPv4 packets contain an optional header extension that will be described later. 

.. figure:: fig/network-fig-064-c.png
   :align: center
   :scale: 70
   
   The IP version 4 header

The main fields of the IPv4 header are :

 - a 4 bits `version` that indicates the version of IP used to build the header. Using a version field in the header allows the protocol to evolve as we'll see with IPv6
 -  a 4 bits `IP Header Length (IHL)` that indicates the length of the IP header in 32 bits words. This field allows IPv4 to use options if required, but as it is encoded as a 4 bits field, the IPv4 header cannot be longer than 64 bytes. 
 - an 8 bits `DS` field that is used for Quality of Service and whose usage will be described later.
 - an 8 bits `Protocol` field that indicates the transport layer protocol that must process the packet's payload at the destination. Common values for this field [#fprotocolnumber]_ are `6` for TCP and `17` for UDP
 - a 16 bits `length` that indicates the total length of the entire IPv4 packet (header and payload) in bytes. This implies that an IPv4 packet cannot be longer than 65535 bytes.
 - a 32 bits `source address` field that contains the IPv4 address of the source host
 - a 32 bits `destination address` field that contains the IPv4 address of the destination host 
 - a 16 bits `checksum` that protects only the IPv4 header against transmission errors

.. index:: Time To Live (IP)

The other fields of the IPv4 header are used for specific purposes. The first is the 8 bits `Time To Live (TTL)` field. This field is used by IPv4 to avoid the risk of having an IPv4 packet caught in an infinite loop due to a transient or permanent error in routing tables [#fttl]_. Consider for example the situation depicted in the figure below where destination `D` uses address `11.0.0.56`. If `S` sends a packet towards this destination, the packet will be forwarded to router `B` that will forward it to router `C` that will forward it back to router `A`...

.. figure:: fig/network-fig-164-c.png
   :align: center
   :scale: 70
   
   Forwarding loops in an IP network

Unfortunately, such loops can occur for two reasons in IP networks. First, if the network uses static routing, the loop can be caused by a simple configuration error. Second, if the network uses dynamic routing, such a loop can occur transiently, for example during the convergence of the routing protocol after a link or router failure. The `TTL` field of the IPv4 header ensures that even if there are forwarding loops in the network, packets will not loop forever. Hosts send their IPv4 packets with a positive `TTL` (usually `64` or more [#finitialttl]_). When a router receives an IPv4 packet, it first decrements the `TTL` by one. If the `TTL` becomes `0`, the packet is discarded and a message is sent back to the packet's source (see section ICMP_). Otherwise, the router performs a lookup in its forwarding table to forward the packet.

.. index:: Maximum Transmission Unit, MTU

A second problem for IPv4 is the heterogeneity of the datalink layer. IPv4 is used above many very different datalink layers. Each datalink layer has its own characteristics and as indicated earlier, each datalink layer is characterised by a maximum frame size. From IP's viewpoint, a datalink layer interface is characterised by its `Maximum Transmission Unit (MTU)`. The MTU of an interface is the largest IPv4 packet (including header) that it can send. The table below provides some common MTU sizes [#f6lowpan]_. 

==============      ==================
Datalink layer      MTU
--------------      ------------------
Ethernet	    1500 bytes
WiFi		    2272 bytes
ATM (AAL5)	    9180 bytes
802.15.4	    102 or 81 bytes
Token Ring	    4464 bytes
FDDI  		    4352 bytes
==============      ==================

Although IPv4 can send 64 KBytes long packets, few datalink layer technologies that are used today are able to send a 64 KBytes IPv4 packet inside a frame. Furthermore, as illustrated in the figure below, another problem is that a host may send a packet that would be too large for one of the datalink layers used by the intermediate routers. 

.. figure:: fig/network-fig-063-c.png
   :align: center
   :scale: 70
   
   The need for fragmentation and reassembly

.. index:: IPv4 fragmentation and reassembly

To solve these problems, IPv4 includes a fragmentation and reassembly mechanism. Both hosts and intermediate routers may fragment an IPv4 packet if the packet is too long to sent via the datalink layer. In IPv4, fragmentation is completely performed in the IP layer and a large IPv4 will be fragmented in two or more IPv4 packets (called fragments). The IPv4 fragments of a large packet are normal IPv4 packets that are forwarded towards the destination of the large packet by intermediate routers. 

The IPv4 fragmentation mechanism relies on four fields of the IPv4 header : `Length`, `Identification`, the `flags` and the `Fragment Offset`. The IPv4 header contains two flags : `More` and `Don't Fragment (DF)`. When the `DF` flag is set, this indicates that the packet cannot be fragmented.


.. index:: Maximum Transmission Unit (MTU)

The basic operation of the IPv4 fragmentation is as follows. A large packet is fragmented in two or more fragments. The size of all fragments, except the last one, is equal to the Maximum Transmission Unit of the link used to forward the packet. Each IPv4 packet contains a 16 bits `Identification` field. When a packet is fragmented, the `Identification` of the large packet is copied in all fragments to allow the destination to reassemble the received fragments together. In each fragment, the `Fragment Offset` indicates, in units of 8 bytes, the position of the payload of the fragment in the payload of the original packet. The `Length` field in each fragment indicates the length of the payload of the fragment as in a normal IPv4 packet. Finally, the `More` flag is set only in the last fragment of a large packet.

.. sidebar:: IPv4 in scapy

 In the pseudo-code used in this section, we use the scapy_ notations for the fields of the IPv4 header. `ihl` is the `IP Header Length`, `tos` is the `DS` byte, `len` is the packet length, `id` the packet identifier, `flags` contains the `DF` and `More` flags, `proto` is the `Protocol` field, `chksum` contains the Internet checksum and `src` (resp. `dst`) the source (resp. destination) IPv4 address. 


The following pseudo-code details the IPv4 fragmentation, assuming that the packet does not contain options ::


 #mtu : maximum size of the packet (including header) of outgoing link
 if p.len <  mtu : 
    send(p)
 # packet is too large
 maxpayload=8*int((mtu-20)/8)  # must be n times 8 bytes
 if p.flags=='DF' :
    discard(p)
 # packet must be fragmented
 payload=p[IP].payload
 pos=0
 while len(payload) > 0 :
    if len(payload) > maxpayload :
       toSend=IP(dest=p.dest,src=p.src,
	         ttl=p.ttl, id=p.id, 
	         frag=p.frag+(pos/8),
		 len=mtu, proto=p.proto)/payload[0:maxpayload]
       pos=pos+maxpayload
       payload=payload[maxpayload+1:]	   
    else
       toSend=IP(dest=p.dest,src=p.src,
	         ttl=p.ttl, id=p.id, 
	         frag=p.frag+(pos/8),
		 flags=p.flags,
		 len=len(payload), proto=p.proto)/payload
    forward(toSend)   

The fragments of an IPv4 packet may arrive at the destination in any order as each fragment will be forwarded independently in the network and may follow different paths. Furthermore, some fragments may be lost and never reach the destination.

The reassembly algorithm used by the destination host is roughly as follows. First, the destination can verify whether a received IPv4 packet is a fragment or not by checking the value of the `More` flag and the `Fragment Offset`. If the `Fragment Offset` is set to `0` and the `More` flag is reset, the received packet has not been fragmented. Otherwise, the packet has been fragmented and must be reassembled. The reassembly algorithm relies on the `Identification` field of the received fragments to associate a fragment with the corresponding packet being reassembled. Furthermore, the `Fragment Offset` field indicates the position of the fragment payload in the original unfragmented packet. Finally, the packet with the `More` flag reset allows the destination to determine the total length of the original unfragmented packet.

Note that the reassembly algorithm must deal with the unreliability of the IP network. This implies that a fragment may be duplicated or a fragment may never reach the destination. The destination will easily detect fragment duplication thanks to the `Fragment Offset`. To deal with fragment losses, the reassembly algorithm must bound the time during which the fragments of a packet are stored in its buffer while the packet is being reassembled. This can be implemented by starting a timer when the first fragment of a packet is received. If the packet has not been reassembled upon expiration of the timer, all fragments are discarded and the packet is considered to be lost. 

.. index:: IP options

The original IP specification defined in :rfc:`791` several types of options that can be added to the IP header. Each option is encoded by using a `type length value` format. They are not widely used today and are thus only briefly described. Additional details may be found in :rfc:`791`.

The most interesting options in IPv4 are the three options that are related to routing. The `Record route` option was defined to allow network managers to determine the path followed by a packet. When the `Record route` option was present, routers on the packet's path had to insert their IP address in the option. This option was implemented, but as the optionnal part of the IPv4 header can only contain 44 bytes, it is impossible to record an entire path on the global Internet. :manpage:`traceroute(8)`, despite its limitations, is a better solution to record the path towards a destination.

The other routing options are the `Strict source route` and the `Loose source route` option. The main idea behind these options is that a host may want, for any reason, to specify the path to be followed by the packets that it sends. The `Strict source route` option allows a host to indicate inside each packet the exact path to be followed. The `Strict source route` option contains a list of IPv4 address and a pointer to indicate the next address in the list. When a router receives a packet containing this option, it does not lookup the destination address in its routing table but forward the packet directly to the next router in the list and advances the pointer. This is illustrated in the figure below where `S` forces its packets to follow the `RA-RB-RD` path.


.. figure:: fig/network-fig-065-c.png
   :align: center
   :scale: 70
   
   Usage of the `Strict source route` option 


The maximum length of the optionnal part of the IPv4 header is a severe limitation for the `Strict source route` option as for the `Record Route` option. The `Loose source route` option does not suffer from this limitation. This option allows the sending host to indicate inside its packet `some` of the routers that must be traversed to reach the destination. This is shown in the figure below. `S` sends a packet containing a list of addresses and a pointer to the next router in the list. Initially, this pointer points to `RB`. When `RA` receives the packet sent by `S`, it looksup in its forwarding table the address pointed in the `Loose source route` option and not the destination address. The packet is then forwarded to router `RB` that recognises its address in the option and advances the pointer. As there is no address listed in the `Loose source route` option anymore, `RB` and other downstream routers forward the packet by performing a lookup for the destination address.

.. figure:: fig/network-fig-066-c.png
   :align: center
   :scale: 70
   
   Usage of the `Loose source route` option 

These two options are usually ignored by routers because they cause security problems.


.. index:: Internet Control Message Protocol, ICMP
.. _ICMP:

ICMP version 4
==============

It is sometimes necessary for intermediate routers or the destination host to inform the sender of the packet of a problem that occurred while processing a packet. In the TCP/IP protocol suite, this reporting is done by the Internet Control Message Protocol (ICMP). ICMP is defined in :rfc:`792`. ICMP messages are carried as the payload of IP packets (the protocol value reserved for ICMP is `1`). An ICMP message is composed of an 8 bytes header and a variable length payload that usually contains the first bytes of the packet that triggered the transmission of the ICMP message.


.. figure:: fig/network-fig-069-c.png
   :align: center
   :scale: 70
   
   ICMP version 4 

In the ICMP header, the `Type` and `Code` fields indicate the type of problem that was detected by the sender of the ICMP message. The `Checksum` protects the entire ICMP message against transmission errors and the `Data` field contains additional information for some ICMP messages.

The main types of ICMP messages are :

 - `Destination unreachable` : a `Destination unreachable` ICMP message is sent when a packet cannot be delivered to its destination due to routing problems. Different types of unreachability are distinguished :

   - `Network unreachable` : this ICMP message will be sent by a router that does not have a route for the subnet containing the destination address of the packet 
   - `Host unreachable` : this ICMP message will be sent by a router that is attached to the subnet that contains the destination address of the packet, but this destination address cannot be reached at this time
   - `Protocol unreachable` : this ICMP message will be sent by a destination host that has received a packet, but does not support the transport protocol indicated in the packet's `Protocol` field
   - `Port unreachable` : this ICMP message will be sent by a destination host that has received a packet destined to a port number, but no server process is bound to this port 

 - `Fragmentation needed` : this ICMP message will be sent by a router that receives a packet with the `Don't Fragment` flag set that is larger than the MTU of the outgoing interface 

 - `Redirect` : this ICMP message can be sent when there are two routers on the same LAN. Consider a LAN with one host and two routers : `R1` and `R2`. Assume that `R1` is also connected to subnet `130.104.0.0/16` while `R2` is connected to subnet `138.48.0.0/16`. If a host on the LAN sends a packet towards `130.104.1.1` to `R2`, `R2` will need to forward the packet again on the LAN to reach `R1`. This is not optimal as the packet is sent twice on the same LAN. In this case, `R2` could send an ICMP `Redirect` message to the host to inform it that it should have sent the packet directly to `R1`. This will allow the host the send the other packets to `130.104.1.1` directly via `R1`. 

 .. figure:: fig/network-fig-165-c.png
   :align: center
   :scale: 70
   
   ICMP redirect

 - `Parameter problem` : this ICMP message is sent when a router or a host receives an IP packet containing an error
 - `Source quench` : a router was supposed to send this message when it had to discard packets due to congestion. However, sending ICMP messages in case of congestion was not the best way to reduce the congestion and since the inclusion of a congestion control scheme in TCP, this ICMP message has been deprecated. 

 - `Time Exceeded` : there are two types of `Time Exceeded` ICMP messages

   - `TTL exceeded` : a `TTL exceeded` message is sent by a router when it discards an IPv4 packet because its `TTL` reached `0`.
   - `Reassembly time exceeded` : this ICMP message is sent when a destination has been unable to reassemble all the fragments of a packet before the expiration of its reassembly timer. 

 - `Echo request` and `Echo reply` : these ICMP messages are used by the :manpage:`ping(8)` network debugging software. 



.. sidebar:: Redirection attacks

 ICMP redirect messages are useful when several routers are attached to the same LAN as hosts. However, they should be used with care as they also create an important security risk. One of the most annoying attack in an IP network is called the `man in the middle attack`. Such an attack occurs if an attacker is able to receive, process, possibly modify and forward all the packets exchanged between a source and a destination. As the attacker receives all the packets it can easily collect passwords or credit card numbers or even inject fake information in an established TCP connection. ICMP redirects unfortunately enable an attacker to easily perform such an attack. In the figure above, consider host `H` that is attached to the same LAN as `A` and `R1`. If `H` sends to `A` an ICMP redirect for prefix `138.48.0.0/16`, `A` will forward to `H` all the packets that it wants to send to this prefix. `H` can then forward them to `R2`. To avoid these attacks, host should ignore ICMP redirect messages.






.. index:: ping

:manpage:`ping(8)` is often used by network operators to verify that a given IP address is reachable. Each host is supposed [#fpingproblems]_ to reply with an ICMP `Echo reply` message when its receives an  ICMP `Echo request` message. A sample usage of :manpage:`ping(8)` is shown below ::

  ping 130.104.1.1
  PING 130.104.1.1 (130.104.1.1): 56 data bytes
  64 bytes from 130.104.1.1: icmp_seq=0 ttl=243 time=19.961 ms
  64 bytes from 130.104.1.1: icmp_seq=1 ttl=243 time=22.072 ms
  64 bytes from 130.104.1.1: icmp_seq=2 ttl=243 time=23.064 ms
  64 bytes from 130.104.1.1: icmp_seq=3 ttl=243 time=20.026 ms
  64 bytes from 130.104.1.1: icmp_seq=4 ttl=243 time=25.099 ms
  --- 130.104.1.1 ping statistics ---
  5 packets transmitted, 5 packets received, 0% packet loss
  round-trip min/avg/max/stddev = 19.961/22.044/25.099/1.938 ms

.. index:: traceroute

Another very useful debugging tool is :manpage:`traceroute(8)`. The traceroute man page describes this tool as `"print the route packets take to network host"`. traceroute uses the `TTL exceeded` ICMP messages to discover the intermediate routers on the path towards a destination. The principle behind traceroute is very simple. When a router receives an IP packet whose `TTL` is set to `1` it decrements the `TTL` and is forced to return to the sending host a `TTL exceeded` ICMP message containing the header and the first bytes of the discarded IP packet. To discover all routers on a network path, a simple solution is to first send a packet whose `TTL` is set to `1`, then a packet whose `TTL` is set to `2`, ... A sample traceroute output is shown below ::

 traceroute www.ietf.org
 traceroute to www.ietf.org (64.170.98.32), 64 hops max, 40 byte packets
  1  CsHalles3.sri.ucl.ac.be (192.168.251.230)  5.376 ms  1.217 ms  1.137 ms
  2  CtHalles.sri.ucl.ac.be (192.168.251.229)  1.444 ms  1.669 ms  1.301 ms
  3  CtPythagore.sri.ucl.ac.be (130.104.254.230)  1.950 ms  4.688 ms  1.319 ms
  4  fe.m20.access.lln.belnet.net (193.191.11.9)  1.578 ms  1.272 ms  1.259 ms
  5  10ge.cr2.brueve.belnet.net (193.191.16.22)  5.461 ms  4.241 ms  4.162 ms
  6  212.3.237.13 (212.3.237.13)  5.347 ms  4.544 ms  4.285 ms
  7  ae-11-11.car1.Brussels1.Level3.net (4.69.136.249)  5.195 ms  4.304 ms  4.329 ms
  8  ae-6-6.ebr1.London1.Level3.net (4.69.136.246)  8.892 ms  8.980 ms  8.830 ms
  9  ae-100-100.ebr2.London1.Level3.net (4.69.141.166)  8.925 ms  8.950 ms  9.006 ms
  10  ae-41-41.ebr1.NewYork1.Level3.net (4.69.137.66)  79.590 ms 
      ae-43-43.ebr1.NewYork1.Level3.net (4.69.137.74)  78.140 ms 
      ae-42-42.ebr1.NewYork1.Level3.net (4.69.137.70)  77.663 ms
  11  ae-2-2.ebr1.Newark1.Level3.net (4.69.132.98)  78.290 ms  83.765 ms  90.006 ms
  12  ae-14-51.car4.Newark1.Level3.net (4.68.99.8)  78.309 ms  78.257 ms  79.709 ms
  13  ex1-tg2-0.eqnwnj.sbcglobal.net (151.164.89.249)  78.460 ms  78.452 ms  78.292 ms
  14  151.164.95.190 (151.164.95.190)  157.198 ms  160.767 ms  159.898 ms
  15  ded-p10-0.pltn13.sbcglobal.net (151.164.191.243)  161.872 ms  156.996 ms  159.425 ms
  16  AMS-1152322.cust-rtr.swbell.net (75.61.192.10)  158.735 ms  158.485 ms  158.588 ms
  17  mail.ietf.org (64.170.98.32)  158.427 ms  158.502 ms  158.567 ms

The above :manpage:`traceroute(8)` output shows a 17 hops path between a host at UCLouvain and one of the main IETF servers. For each hop, traceroute provides the IPv4 address of the router that sent the ICMP message and the measured round-trip-time between the source and this router. traceroute sends three probes with each `TTL` value. In some cases, such as at the 10th hop above, the ICMP messages may be received from different addresses. This is usually because different packets from the same source have followed different paths [#ftraceroutemore]_ in the network. 


.. index:: Path MTU discovery

Another important utilisation of ICMP messages is to discover the maximum MTU that can be used to reach a destination without fragmentation. As explained earlier, when an IPv4 router receives a packet that is larger than the MTU of the outgoing link, it must fragment the packet. Unfortunately, fragmentation is a complex operation and routers cannot perform it at line rate [KM1995]_. Furthermore, when a TCP segment is transported in an IP packet that is fragmented in the network, the loss of a single fragment will force TCP to retransmit the entire segment (and thus all the fragments). If TCP was able to send only packets that do not require fragmentation in the network, it could retransmit only the information that was lost in the network. Finally, IP reassembly causes several challenges at high speed as discussed in :rfc:`4963`.


ICMP, combined with the `Don't fragment (DF)` IPv4 flag, is used by TCP implementations to discover the largest MTU size to be used to reach a destination host without causing network fragmentation. This is the `Path MTU discovery` mechanism defined in :rfc:`1191`. A TCP implementation that includes `Path MTU discovery` (most do) requests the IPv4 layer to send all segments inside IPv4 packets having the `DF` flag set. This prohibits intermediate routers from fragmenting these packets. If a router needs to forward an unfragmentable packet over a link with a smaller MTU, it sends back a `Fragmentation needed` ICMP message to the source indicating the MTU of its outgoing link. This ICMP message contains in its `Data` field the MTU of the router's outgoing link. Upon reception of this ICMP message, the source TCP implementation adjusts its Maximum Segment Size (MSS) so that the packets containing the segments that it sends can be forwarded by this router without requiring fragmentation. 

Operation of IPv4 devices
-------------------------

At this point of the description of IPv4, it is useful to have a detailed look at how an IPv4 implementation sends, receives and forwards IPv4 packets. The simplest case is when a host needs to send a segment in an IPv4 packet. The host performs two operations. First, it must decide on which interface the packet will be sent. Second it must create the corresponding IP packet(s). 

To simplify the discussion in this section, we ignore the utilisation of IPv4 options. This is not a severe limitation as today IPv4 packets rarely contain options. Details about the processing of the IPv4 options may be found in the relevant RFCs such as :rfc:`791`. Furthermore, we also assume that only point-to-point links are used. We defer the explanation of the operation of IPv4 over Local Area Networks until the next chapter.

An IPv4 host having :math:`n` datalink layer interfaces manages :math:`n+1` IPv4 addresses :

 - the `127.0.0.1/32` IPv4 address assigned by convention to its loopback address
 - one `A.B.C.D/p` IPv4 address assigned to each of its :math:`n` datalink layer interfaces

Such a host will maintain a routing table that contains one entry for its loopback address and one entry for each subnet identifier assigned to its interfaces. Furthermore, the host will usually utilise one of its interfaces as the `default` interface when sending packets that are not addressed to a directly connected destination. This is represented by the `default` route : `0.0.0.0/0` that is associated to one interface.

When a transport protocol running on the host requests the transmission of a segment, it usually provides to the IPv4 layer the IPv4 destination address in addition to the segment [#fdfflag]_. The IPv4 implementation will first perform a longest prefix match with the destination address in its routing table. The lookup will return the identification of the interface that must be used to send the packet. The host can then create the IPv4 packet that will contain the segment. The source IPv4 address of the packet will be the IPv4 address of the host on the interface returned by the longest prefix match. The `Protocol` field of the packet is set to the identification of the local transport protocol that created the segment. The `TTL` field of the packet is set to the default `TTL` used by the host. The host must now choose the packet's `Identification`. This `Identification` is important if the packet becomes fragmented in the network as it ensures that the destination will be able to reassemble the received fragments. Ideally, a sending host should never send twice a packet with the same `Identification` to the same destination host to ensure that all fragments are correctly reassembled by the destination. Unfortunately, with a 16 bits `Identification` field and an expected MSL of 2 minutes, this implies that the maximum bandwidth to a given destination is limited to roughly 286 Mbps. With a more realistic 1500 bytes MTU, that bandwidth drops to 6.4 Mbps :rfc:`4963` if fragmentation must be possible [#fiddf]_. This is very low and is another reason why hosts are highly encouraged to avoid fragmentation. If despite of this the MTU of the outgoing interface is smaller than the packet's length, the packet is fragmented. Finally, the packet's checksum is computed before transmission.


When a host receives an IPv4 packet destined to itself, there are several operations that it must perform. First, it must check the packet's checksum. If the checksum is incorrect, the packet is discarded. Then, it must check whether the packet has been fragmented. If yes, the packet is passed to the reassembly algorithm described earlier. Otherwise, the packet must be passed to the upper layer. This is done by looking at the `Protocol` field (`6` for TCP, `17` for UDP). If the host does not implement the transport layer protocol corresponding to the received `Protocol` field, it sends a `Protocol unreachable` ICMP message to the sending host. If the received packet contains an ICMP message (`Protocol` field set to `1`), the processing is more complex. An `Echo-request` ICMP message will trigger the transmission of an `ICMP Echo-reply` message. The other types of ICMP messages indicate an error that was caused by a previously transmitted packet. These ICMP messages are usually forwarded to the transport protocol that sent the erroneous packet. This can be done by inspecting the contents of the ICMP message that includes the header and the first 64 bits of the erroneous packet. If the IP packet did not contain options, which is the case for most IPv4 packets, the transport protocol can find in the first 32 bits of the transport header the source and destination ports to determine the affected transport flow. This is important for Path MTU discovery for example.

When a router receives an IPv4 packet, it must first check the packet's checksum. If the checksum is invalid, it is discarded. Otherwise, the router must check whether the destination address is one of the IPv4 addresses assigned to the router. If so, the router must behave as a host and processes the packet as described above. Although routers mainly forward IPv4 packets, they sometimes need to be accessed as hosts by network operators or network management software. 

If the packet is not addressed to the router, it must be forwarded on an outgoing interface according to the router's routing table. The router first decrements the packet's `TTL`. If the `TTL` reaches `0`, a `TTL Exceeded` ICMP message is sent back to the source. As the packet header has been modified, the checksum must be recomputed. Fortunately, as IPv4 uses an arithmetic checksum, a router can incrementally update the packet's checksum as described in :rfc:`1624`. Then, the router performs a longest prefix match for the packet's destination address in its forwarding table. If the lookup does not return a match, the router must return a `Destination unreachable` ICMP message to the source. Otherwise, the lookup returns the interface over which the packet must be forwarded. Before forwarding the packet over this interface, the router must first compare the length of the packet with the MTU of the outgoing interface. If the packet is smaller than the MTU, it is forwarded. Otherwise, a `Fragmentation needed` ICMP message is sent if the `DF` flag was sent or the packet is fragmented if the `DF` was not set. 


.. sidebar:: Longest prefix match in IP routers

 Performing the longest prefix match at line rate on routers requires highly tuned data structures and algorithms. Consider for example an implementation of the longest match based on a Radix tree on a router with a 10 Gbps link. On such a link, a router can receive 31,250,000 40 bytes IPv4 packets every second. To forward the packets at line rate, the router must process one IPv4 packet every 32 nanoseconds. This cannot be achieved by a software implementation. For a hardware implementation, the main difficulty lies in the number of memory accesses that are necessary to perform the longest prefix match. 32 nanoseconds is very small compared to the memory accesses that are required by a naive longest prefix match implement. Additional information about faster longest prefix match algorithms may be found in [Varghese2005]_.



IP version 6
============

In the late 1980s and early 1990s the growth of the Internet was causing several operational problems on routers. Many of these routers had a single CPU and up to 1 MBytes of RAM to store their operating system, packet buffers and routing tables. Given the rate of allocation of IPv4 prefixes to companies and universities willing to join the Internet, the routing tables where growing very quickly and some feared that all IPv4 prefixes would be quickly allocated. In 1987, a study cited in :rfc:`1752` estimated 100,000 networks in the near future. In August 1990, estimates indicated that the class B space would be exhausted by March 1994. 
Two types of solutions were developed to solve this problem. The first short term solution was the introduction of Classless Inter Domain Routing (:term:`CIDR`). A second short term solution was the Network Address Translation (:term:`NAT`) mechanism defined in :rfc:`1631` that allowed multiple hosts to share a single public IP address. NAT will be explained in section :ref:`Middleboxes`.

However, in parallel with these short-term solutions, that have allowed the IPv4 Internet to continue to be usable until now, the Internet Engineering Task Force started to work on developing a replacement for IPv4. This work started with an open call for proposal outline in :rfc:`1550`. Several groups responded to this call with proposals for a next generation Internet Protocol (IPng) :

 * TUBA proposed in :rfc:`1347` and :rfc:`1561`
 * PIP proposed in :rfc:`1621`
 * SIPP proposed in :rfc:`1710`

The IETF decided to pursue the development of IPng on the basis on the SIPP proposal. As IP version `5` was already used by the experimental ST-2 protocol defined in :rfc:`1819`, the successor of IP version 4 is IP version 6. The initial IP version 6 defined in :rfc:`1752` was designed based on the following assumptions :

 * IPv6 addresses are encoded as a 128 bits field
 * The IPv6 header has a simple format that can be easily parsed by hardware devices
 * A host should be able to configure its IPv6 address automatically
 * Security must be part of IPv6

.. sidebar:: The IPng address size

 When the work on IPng started, it was clear that 32 bits was too small to encode an IPng address and all proposals used longer addresses. However, there were many discussions on the most suitable address length. A first approach, proposed by SIP in :rfc:`1710` was to use 64 bits addresses. A 64 bits address space was 4 billion times larger than the IPv4 address space and furthermore from an implementation viewpoint, 64 bits CPU were being considered and 64 bits addresses would naturally fit inside their registers. Another approach was to use an existing address format. This was the TUBA proposal (:rfc:`1347`) that reuses the ISO CLNP 20 bytes addresses. The 20 bytes addresses provided room for growth, but using ISO CLNP was not favored by the IETF partially due to political reasons, despite the fact that mature CLNP implementations were already available. 128 bits appeared as a reasonable compromise at that time.

IPv6 addressing architecture
----------------------------

The experience with IPv4 revealed that the scalability of a network layer protocol heavily depends on its addressing architecture. The designers of IPv6 spent a lot of effort defining its addressing architecture :rfc:`3513`. All IPv6 addresses are 128 bits wide. This implies that there are 340,282,366,920,938,463,463,374,607,431,768,211,456 (3.4 × 10^38) different IPv6 addresses. As the surface of the Earth is about 510,072,000 :Math:`km^2`, this implies that there are about :math:`6.67 \times 10^{23}` IPv6 addresses per square meter on Earth. Compared to IPv4 that offers only 8 addresses per square kilometer, this is a significant improvement on paper. 

IPv6 supports unicast, multicast and anycast addresses. As with IPv4, an IPv6 unicast address is used to identify one datalink-layer interface on a host. If a host has several datalink layer interfaces (e.g. an Ethernet interface and a WiFi interface), then it needs several IPv6 addresses. In general, an IPv6 unicast address is structured as shown in the figure below.

.. figure:: fig/network-fig-073-c.png
   :align: center
   :scale: 70
   
   Structure of IPv6 unicast addresses

An IPv6 unicast address is composed of three parts :

#. A global routing prefix that is assgined to the Internet Service Provider that owns this block of addresses
#. A subnet identifier that identifies a customer of the ISP
#. An interface identifier that identifies a particular interface on an endsystem 

In today's deployments, interface identifiers are always 64 bits wide. This implies that while there are :math:`2^{128}` different IPv6 addresses, they must be grouped in :math:`2^{64}` subnets. This could appear as a waste of resources, however using 64 bits for the host identifier allows IPv6 addresses to be auto-configured and also provides some benefits from a security viewpoint as will be explained in section ICMPv6_


.. sidebar:: Textual representation of IPv6 addresses

 It is sometimes necessary to write IPv6 addresses in text format, e.g. when manually configuring addresses of for documentation purposes. The preferred format  is `x:x:x:x:x:x:x:x`, where the `x` are hexadecimal digits representing the eight 16-bit parts of the address. Here are a few example IPv6 address :

  - ABCD:EF01:2345:6789:ABCD:EF01:2345:6789
  - 2001:DB8:0:0:8:800:200C:417A
  - FE80:0:0:0:219:E3FF:FED7:1204

 IPv6 addresses often contain a long sequence of bits set to `0`. In this case, a compact notation has been defined. With this notation, `::` is used to indicate one or more groups of 16 bits blocks containing only bits set to `0`. For example, 
 
  - 2001:DB8:0:0:8:800:200C:417A  is represented as  `2001:DB8::8:800:200C:417A`
  - FF01:0:0:0:0:0:0:101   is represented as `FF01::101` 
  - 0:0:0:0:0:0:0:1 is represented as `::1`
  - 0:0:0:0:0:0:0:0 is represented as `\:\:`

 An IPv6 prefix can be represented as `address/length` where `length` is the length of the prefix in bits. For example, the three notations below correspond to the same IPv6 prefix :

  - 2001:0DB8:0000:CD30:0000:0000:0000:0000/60
  - 2001:0DB8::CD30:0:0:0:0/60
  - 2001:0DB8:0:CD30::/60

.. index:: Provider Independent address
.. index:: Provider Aggregatable address

There are in practice several types of IPv6 unicast address. Most of the `IPv6 unicast addresses <http://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml>`_ are allocated in blocks under the responsibility of IANA_ The current IPv6 allocations are part of the `2000::/3` address block. Regional Internet Registries (RIR) such as RIPE_ in Europe,  ARIN_ in North-America or AfriNIC in Africa have each received a `block of IPv6 addresses <http://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xhtml>`_ that they sub-allocate to Internet Service Providers in their region.  The ISPs then sub-allocate addresses to their customers. 

When considering the allocation of IPv6 addresses, two types of address allocations are often distinguished. The RIRs allocate `provider-independent (PI)` addresses. PI addresses are usually allocated to Internet Service Providers and large companies that are connected to at least two different ISPs [CSP2009]_. Once a PI address block has been allocated to a company, this company can use its address block with the provider of its choice and change of provider at will. Internet Service Providers allocate `provider-aggregatable (PA)` address blocks from their own PI address block to their customers. A company that is connected to only one ISP should only use PA addresses. The drawback of PA addresses is that when a company using a PA address block changes of provider, it needs to change all the addresses that it uses. This can be a nightmare from an operational viewpoint and many companies are lobbying to obtain `PI` address blocks even if they are small and connected to a single provider. The typical size of the IPv6 address blocks are :

 - /32 for an Internet Service Provider
 - /48 for a single company
 - /64 for a single user (e.g. a home user connected via ADSL) 
 - /128 in the rare case when it is known that no more than one endhost will be attached

.. index:: Unique Local Unicast IPv6

For the companies that want to use IPv6 without being connected to the IPv6 Internet, :rfc:`4193` defines the `Unique Local Unicast (ULA)` addresses (`FC00::/7`). These ULA addresses play a similar role as the private IPv4 addresses defined in :rfc:`1918`. However, the size of the `FC00::/7` address block allows ULA to be much more flexible than private IPv4 addresses.

.. index:: ::1, ::

Furthermore, the IETF has reserved some IPv6 addresses for a special usage. The two most important ones are :

 - `0:0:0:0:0:0:0:1` (`::1` in compact form) is the IPv6 loopback address. This is the address of a logical interface that is always up and running on IPv6 enabled hosts. This is the equivalent of `127.0.0.1` in IPv4.
 - `0:0:0:0:0:0:0:0` (`\:\:` in compact form) is the unspecified IPv6 address. This is the IPv6 address that a host can use as source address when trying to acquire an official address.

.. index:: Link Local address

The last type of unicast IPv6 addresses are the `Link Local Unicast` addresses. These addresses are part of the `FE80::/10` address block and are defined in :rfc:`4291`. Each host can compute its own link local address by concatenating the `FE80::/64` prefix with the 64 bits identifier of its interface. Link local addresses can be used when hosts that are attached to the same link (or local area network) need to exchange packets. They are used notably for address discovery and auto-configuration purposes. Their usage is restricted to each link and a router cannot forward a packet whose source or destination address is a link local address/

.. figure:: fig/network-fig-074-c.png
   :align: center
   :scale: 70
   
   IPv6 link local address structure

An important consequence of the IPv6 unicast addressing architecture and the utilisation of link-local addresses is that an IPv6 host has several IPv6 addresses. This implies that an IPv6 stack must be able to handle multiple IPv6 addresses. This was not always the case with IPv4.

:rfc:`4291` defines a special type of IPv6 anycast address. On a subnetwork having prefix `p/n`, the IPv6 address whose `128-n` low-order bits are set to `0` is the anycast address that corresponds to all routers inside this subnetwork. This anycast address can be used by hosts to quickly send a packet to any of the routers inside their own subnetwork.

Finally, :rfc:`4291` defines the structure of the IPv6 multicast addresses [#fmultiiana]_. This structure is depicted in the figure below

.. figure:: fig/network-fig-075-c.png
   :align: center
   :scale: 70
   
   IPv6 multicast address structure

The low order 112 bits of an IPv6 multicast address are the group's identifier. The high order bits are used as a marker to distinguish multicast addresses from unicast addresses. The 4 bits flag field indicates notably whether the address is temporary or permanent. Finally, the scope field indicates the boundaries of the forwarding of packets destined to a particular address. A link-local scope indicates that a router should not forward a packet destined to such a multicast address. An organisation local-scope indicates that a packet sent to such a multicast destination address should not leave the organisation. Finally the global scope is intended for multicast groups spanning the global Internet.

Among these addresses some are well known. For example, all endsystem automatically belong to the `FF02::1` multicast group while all routers automatically belong to the `FF02::2` multicast group. We will discuss IPv6 multicast later.

.. _IPv6Packet:

IPv6 packet format
------------------

The IPv6 packet format was heavily inspired by the packet format proposed for the SIPP protocol in :rfc:`1710`. The standard IPv6 header defined in :rfc:`2460` occupies 40 bytes and contains 8 different fields as shown in the figure below.

.. figure:: fig/network-fig-077-c.png
   :align: center
   :scale: 70
   
   The IP version 6 header

Besides the source and destination addresses, the IPv6 header contains the following fields :

 - `version` : a 4 bits field set to `6` and intended to allow IP to evolve in the future if needed
 - `Traffic class` : this 8 bits field plays a similar role as the `DS` byte in the IPv4 header
 - `Flow label` : this field was initially intended to be used to tag packets belonging to the same `flow`. However, as of this writing, there is no clear guidleline on how this field should be used by hosts and routers
 - `Payload length` : this is the size of the packet payload in bytes. As the length is encoded as a 16 bits field, an IPv6 packet can contain up to 65535 bytes of payload.
 - `Next Header` : this 8 bits field indicates the type [#fianaprotocol]_ of header that follows the IPv6 header. It can be a transport layer header (e.g. `6` for TCP or `17` for UDP) or an IPv6 option. Handling options as a next header allows to simplify the processing of IPv6 packets compared to IPv4.
 - `Hop Limit` : this 8 bits field indicates the number of routers that can forward the packet. It is decremented by one by each router and has the same purpose as the TTL field of the IPv4 header.

In comparison with IPv4, the IPv6 packets are much simpler and easier to process by routers. A first important difference is that there is no checksum inside the IPv6 header. This is mainly because all datalink layers and transport protocols include a checksum or a CRC to protect their frames/segments against transmission errors. Adding a checksum in the IPv6 header would have forced each router to recompute the checksum of all packets, with a limited benefit in detecting errors. In practice, an IP checksum allows to catch errors that occur inside routers (e.g. due to memory corruption) before the packet reaches its destination. However, this benefit was found to be too small given the reliability of current memories and the cost of computing the checksum on each router.

A second difference with IPv4 is that the IPv6 header does not support fragmentation and reassembly. The experience with IPv4 has shown that fragmenting packets in routers was costly [KM1995]_ and the developers of IPv6 have decided that routers would not fragment packets anymore. If a router receives a packet that is too long to be forwarded, the packet is dropped and the router returns an ICMPv6 messages to inform the sender of the problem. The sender can then either fragment the packet or perform Path MTU discovery. In IPv6, packet fragmentation is performed only by the source by using IPv6 options.

The third difference are the IPv6 options that are simpler and easier to process than the IPv4 options.

.. sidebar:: Header compression on low bandwidth links

 Given the size of the IPv6 header, it can cause a huge overhead on low bandwidth links, especially when small packets are exchanged such as for Voice over IP applications. In such environments, several techniques can be used to reduce the overhead. A first solution is to use data compression in the datalink layer to compress all the information exchanged [Thomborson1992]_. These techniques are similar to the data compression algorithms used in tools such as :manpage:`compress(1)` or :manpage:`gzip(1)`. The compress streams of bits without taking advantage of the fact that these streams contain IP packets with a known structure. A second solution is to compress the IP and TCP header. These header compression techniques, such as the one defined in :rfc:`2507` take advantage of the redundancy found in successive packets from the same flow to reduce significantly the size of the protocol headers. Another solution is to define a compressed encoding of the IPv6 header that matches the capabilities of the underlying datalink layer :rfc:`4944`. 


.. _IPv6Options:

IPv6 options
------------

In IPv6, each option is considered as one header containing a multiple of 8 bytes to ensure that IPv6 options in a packet are aligned on 64 bits boundaries. IPv6 defines several types of options :

 - the hop-by-hop options are the options that must be processed by the routers on the packet's path 
 - the type 0 routing header that is similar to the IPv4 loose source routing option
 - the fragmentation option that is used when fragmenting an IPv6 packet
 - the destination options 
 - the security options that allow IPv6 hosts to exchange packets with cryptographic authentication (AH header) or encryption and authentication (ESP header)

:rfc:`2460` provides lots of details on the encodings of the different types of options. In this section, we only discus some of them. The reader may consult :rfc:`2460` for more information about the other options. The first point to note is that each option contains a `Next Header` field that indicates the type of the next header that follows the option. A second point to note is that to allow routers to efficiently parse IPv6 packets, the options that must be processed by routers (hop-by-hop options and type 0 routing header) must appear first in the packet. This allows the router to process a packet without being forced to analyse all the packet's options. A third point to note is that hop-by-hop and destination options are encoded by using a `type length value` format. Furthermore, the `type` field contains bits that indicate whether a router that does not understand this option should ignore the option or discard the packet. This allows to introduce new options in the network without forcing all devices to be upgraded to support it at the same time.


.. index:: jumbogram

Two `hop-by-hop` options have been defined. :rfc:`2675` specifies the jumbogram that enables IPv6 to support packets containing a payload larger than 65535 bytes. These jumbo packets have their `payload length` set to `0` and the jumbogram option contains the packet length as a 32 bits field. Such packets can only be sent from a source to a destination if all the routers on the path support this option. However, as of this writing it does not seem that the jumbogram option has been implemented. The router alert option defined in :rfc:`2711` is the second example of a `hop-by-hop` option. The packets that contain this option should be processed in a special way by intermediate routers. This option is used for IP packets that carry Resource Reservation Protocol (RSVP) messages. Its usage will be explained later.


The type 0 routing header defined in :rfc:`2460` is an example of an IPv6 option that must be processed by some routers. This option is encoded as shown below.

.. figure:: fig/network-fig-079-c.png
   :align: center
   :scale: 70
   
   The Type 0 routing header


The type 0 routing option was intended to allow a host to indicate a loose source router that should be followed by a packet by specifying the addresses of some of the routers that must forward this packet. Unfortunately, further work with this routing header, including an entertaining demonstration with scapy_ [BE2007]_ revealed some severe security problems with this routing header. For this reason, loose source routing with the type 0 routing header has been removed from the IPv6 specification :rfc:`5095`.
  
.. index:: IPv6 fragmentation

In IPv6, fragmentation is performed exclusively by the source host and relies on the fragmentation header. This 64 bits header is composed of six fields :

 - a `Next Header` field that indicates the type of the header that follows the fragmentation header
 - a `reserved` field set to `0`. 
 - the `Fragment Offset` is a 13-bit unsigned integer that contains the offset, in 8 bytes units, of the data following this header, relative to the start of the original packet. 
 - the `More` flag that is set to `0` in the last fragment of a packet and to `1` in all other fragments. 
 - the 32 bits `Identification` field indicates to which original packet a fragment belongs. When a host sends fragmented packets, it should ensure that it does not reuse the same `identification` field for packets sent to the same destination during a period of `MSL` seconds. This is easier with the 32 bits `identification` used in the IPv6 fragmentation header, than with the 16 bits `identification` field of the IPv4 header.

Some IPv6 implementations send the fragments of a packet in increasing fragment offset order, starting from the first fragment. Others send the fragments in reverse order, starting from the last fragment. The latter solution can be advantageous for the host that needs to reassemble the fragments as it can easily allocate the buffer that is required to reassemble all fragments of the packet upon reception of the last fragment. When a host receives the first fragment of an IPv6 packet, it cannot know a priori the length of the entire IPv6 packet. 

The figure below provides an example of a fragmented IPv6 packet containing a UDP segment. The `Next Header` type reserved for the IPv6 fragmentation option is 44. 

.. figure:: fig/network-fig-087-c.png
   :align: center
   :scale: 70
   
   IPv6 fragmentation example

Finally, the last type of IPv6 options are the Encaspulating Security Payload (ESP) defined in :rfc:`4303` and the Authentication Header (AH) defined in :rfc:`4302`. These two headers are used by IPSec :rfc:`4301`. They will be discussed in another chapter.


.. _ICMPv6:

ICMP version 6
==============

ICMPv6 defined in :rfc:`4443` is the companion protocol for IPv6 as ICMPv4 is the companion protocol for IPv4. ICMPv6 is used by routers and hosts to report problems when processing IPv6 packets. However, as we will see in chapter :doc:`../lan/lan.rst`, ICMPv6 is also used when auto-configuring addresses.

The traditional utilisation of ICMPv6 is similar to ICMPv4. ICMPv6 messages are carried inside IPv6 packets (the `Next Header` field for ICMPv6 is 58). Each ICMP message contains an 8 bits header with a `type` field, a `code` field and a 16 bits checksum computed over the entire ICMPv6 message. The message body contains a copy of the IPv6 packet in error.

.. figure:: fig/network-fig-088-c.png
   :align: center
   :scale: 70
   
   ICMP version 6 packet format

ICMPv6 specifies two classes of messages : error messages that indicate a problem in handling a packet and informational messages. Four types of error messages are defined in :rfc:`4443` :

 - 1 : Destination Unreachable. Such an ICMPv6 message is sent when the destination address of a packet is unreachable. The `code` field of the ICMP header contains additional information about the type of unreachability. The following codes are specified in :rfc:`4443` 
     - 0 : No route to destination. This indicates that the router that sent the ICMPv6 message did not have a route towards the packet's destination
     - 1 : Communication with destination administratively prohibited. This indicates that a firewall has refused to forward the packet towards its destination. 
     - 2 : Beyond scope of source address. This message can be sent if the source is using link-local addresses to reach a global unicast address outside its subnet.
     - 3 : Address unreachable. This messages indicates that the packet reached the subnet of the destination, but the host that owns this destination address cannot be reached.
     - 4 : Port unreachable. This message indicates that the IPv6 packet was received by the destination, but 
 - 2 : Packet Too Big. The router that sends the ICMPv6 message received an IPv6 packet that is larger than the MTU of the outgoing link. The ICMPv6 message contains the MTU of this link in bytes. This allows the sending host to implement Path MTU discovery :rfc:`1981`
 - 3 : Time Exceeded. This error message can be sent either by a router or by a host. A router would set `code` to `0` to report the reception of a packet whose `Hop Limit` reached `0`. A host would set `code` to `1` to report that it was unable to reassemble received IPv6 fragments.
 - 4 : Parameter Problem. This ICMPv6 messages is used to report either the reception of an IPv6 packet with an erroneous header field (type `0`) or an unknown `Next Header` or IP option (types `1` and `2`). In this case, the message body contains the erroneous IPv6 packet and the first 32 bits of the message body contain a pointer to the error.


.. index:: ping6

Two types of informational ICMPv6 messages are defined in :rfc:`4443` : `echo request` and `echo reply` that are used to test the reachability of a destination by using :manpage:`ping6(8)`.


.. index:: traceroute6

ICMPv6 also allows to discover the path between a source and a destination by using :manpage:`traceroute6(8)`. The output below shows a traceroute between a host at UCLouvain and one of the main IETF servers. Note that this IPv6 path is different than the IPv4 path that was described earlier although the two traceroutes were performed at the same time ::
 
 traceroute6 www.ietf.org
 traceroute6 to www.ietf.org (2001:1890:1112:1::20) from 2001:6a8:3080:2:217:f2ff:fed6:65c0, 30 hops max, 12 byte packets
  1  2001:6a8:3080:2::1  13.821 ms  0.301 ms  0.324 ms
  2  2001:6a8:3000:8000::1  0.651 ms  0.51 ms  0.495 ms
  3  10ge.cr2.bruvil.belnet.net  3.402 ms  3.34 ms  3.33 ms
  4  10ge.cr2.brueve.belnet.net  3.668 ms 10ge.cr2.brueve.belnet.net  3.988 ms 10ge.cr2.brueve.belnet.net  3.699 ms
  5  belnet.rt1.ams.nl.geant2.net  10.598 ms  7.214 ms  10.082 ms
  6  so-7-0-0.rt2.cop.dk.geant2.net  20.19 ms  20.002 ms  20.064 ms
  7  kbn-ipv6-b1.ipv6.telia.net  21.078 ms  20.868 ms  20.864 ms
  8  s-ipv6-b1-link.ipv6.telia.net  31.312 ms  31.113 ms  31.411 ms
  9  s-ipv6-b1-link.ipv6.telia.net  61.986 ms  61.988 ms  61.994 ms
  10  2001:1890:61:8909::1  121.716 ms  121.779 ms  121.177 ms
  11  2001:1890:61:9117::2  203.709 ms  203.305 ms  203.07 ms
  12  mail.ietf.org  204.172 ms  203.755 ms  203.748 ms


.. send after Ethernet


.. sidebar:: Rate limitation of ICMP messages

 High-end hardware based routers use special purpose chips on their interfaces to forward IPv6 packets at line rate. These chips are optimised to process `correct` IP packets. They are not able to create ICMP messages at line rate. When such a chip receives an IP packet that will trigger an ICMP message, it interrupts the main CPU of the router and the software running on this CPU processes the packet. This CPU is much slower than the hardware acceleration found on the interfaces [Gill2004]_. It would be overloaded if it had to process IP packets at line rate and generate one ICMP message for each received packet. To protect this CPU, high-end routers limit the rate at which the hardware can interrupt the main CPU and thus the rate at which ICMP messages can be generated. This implies that not all erroneous IP packets will cause the transmission of an ICMP message. The risk of overloading the main CPU of the router is also the reason why using hop-by-hop IPv6 options, including the router alter option is discouraged [#falert]_. 


.. _Middleboxes:

Middleboxes
===========

.. index:: Middlebox

When the TCP/IP architecture and the IP protocol were defined, two types of devices were considered in the network layer : endhosts and routers. Endhosts are the sources and destinations of IP packets while routers forward packets. When a router forwards an IP packet, it consults its forwarding table, updates the packets' TTL, recomputes its checksum and forward it to the nexthop. A router does not need to read nor change the contents of the packet's payload.

However, in today's Internet, there exist devices that are not strictly routers but process, sometimes modify, and forward IP packets. These devices are often called `middleboxes` :rfc:`3234`. Some middleboxes operate only in the network layer, but most middleboxes are able to analyse the payload of the received packets and extract the transport header and in some cases the application layer protocols.  
  

.. figure:: fig/network-fig-161-c.png
   :align: center
   :scale: 70
   
   IP middleboxes and the reference model

In this section, we briefly describe two types of middleboxes : firewalls and network address translation (NAT) devices. A discussion of the different types of middleboxes with references may be found in :rfc:`3234`.

.. index:: firewall

Firewalls
---------

When the Internet was only a research network interconnecting research labs, security was not a concern and most hosts agreed to exchange packets over TCP connections with most other hosts. However, as companies and more and more users became connected to Internet, allowing unlimited access to the hosts managed by companies was becoming a concern. Furthermore, at the end of the 1980s, several security issues affected the Internet such as the first Internet worm [RE1989]_ and some widely publicised security breaches [Stoll1988]_ [CB2003]_ [Cheswick1990]_

    
These security problems convinced the industry that IP networks are a key part of the infrastructure of a company that should be protected by special devices like security guards and fences are used to protect buildings. These special devices were quickly called `firewalls`. A typical firewall has two interfaces :
 
  - an external interface connected to the global Internet
  - an internal interface connected to a trusted network

The first firewalls included configurable packet filters. A packet filter is a set of rules that define the security policy of a network. In practice, these rules are based on the values of fields of the IP or transport layer headers. Any field of the IP or transport header can be used in a firewall rule, but the most common ones :

 - filter on the source address. For example, a company may decide to discard all packets received from one of its competitors. In this case, all packets whose source address belong to the competitor's address block would be rejected 
 - filter on destination address. For example, the hosts of the research lab of a company may receive packets from the global Internet, but not the hosts of the financial department
 - filter on the `Protocol` number found in the IP header. For example, a company may only allow its hosts to use TCP or UDP, but not other more experimental transport protocols
 - filter on the TCP or UDP port numbers. For example, only the DNS server of a company should received UDP segments whose destination port is set to `53` or only the official SMTP servers of the company can send TCP segments whose source ports are set to `25`
 - filter on the TCP flags. For example, a simple solution to prohibit external hosts from opening TCP connections with hosts inside the company is to discard all TCP segments received from the external interface with only the `SYN` flag set.

Such firewalls are often called `stateless` firewalls because they do not maintain any state about the TCP connections that pass through them.

A second type of firewalls are the `stateful` firewalls. A stateful firewall tracks the state of each TCP connection passing through it. It maintains a TCB for each TCP connection. This TCB allows it to reassemble the received segments to extract their payload and perform verifications in the application layer. Some firewalls are able to inspect the URLs accessed by using HTTP and log all URLs visited or block TCP connections where a dangerous URL is exchanged. Some firewalls can verify that SMTP commands are used when a TCP connection is established on port `25` or that a TCP connection on port `80` carries HTTP commands and responses, ... 


.. sidebar:: Beyond firewalls

 Besides the firewalls, different types of "security" devices have been installed at the periphery of corporate networks. Intrusion Detection Systems (IDS) such as the popular snort_ are stateful devicesthat are capable of matching reassembled segments against regular expressions that correspond to signatures of viruses, worms or other types of attacks. Deep Packet Inspection (DPI) is another type of middlebox that analyse the packet's payload and possibly reassemble TCP segments to detect inappropriate usages. While IDS are mainly used in corporate networks, DPI is mainly used in Internet Service Providers. Some ISPs use DPI to detect and limit the bandwidth consumed by peer-to-peer applications. Some countries such as China or Iran use DPI to detect inappropriate Internet usage.


.. index:: Network Address Translation, NAT

NAT
---

Network Address Translation (NAT) was proposed in [TE1993]_ and :rfc:`3022` as a short term solution to deal with the expected shortage of IPv4 addresses in the late 1980s - early 1990s. Combined with CIDR, NAT allowed to significantly slow the consumption of IPv4 addresses. A NAT is a middlebox that interconnects two networks that are using IPv4 addresses from different addressing spaces. Usually, one of these addressing spaces is the public Internet while the other is using the private IPv4 addresses defined in :rfc:`1918`.

A very common deployment of NAT is in broadband access routers as shown in the figure below. The broadband access router interconnects a home network, either WiFi or Ethernet based and the global Internet via one ISP over ADSL or CATV. A single IPv4 address is allocated to the broadband access router and network address translation allows all the hosts attached to the home network to share a single public IPv4 address.

.. figure:: fig/network-fig-158-c.png
   :align: center
   :scale: 70
   
   A simple NAT with one public IPv4 address

A second type of deployment is in enterprise networks as shown in the figure below. In this case, the NAT functionality is installed on a border router of the enterprise. A private IPv4 address is assigned to each enterprise host while the border router manages a pool containing several public IPv4 addresses. 

.. figure:: fig/network-fig-159-c.png
   :align: center
   :scale: 70
   
   An enterprise NAT with several public IPv4 addresses

As the name implies, a NAT is a device that "translates" IP addresses. A NAT maintains a mapping table between the private IP addresses used in the internal network and the public IPv4 addresses. NAT allows a large number of hosts to share a pool of IP addresses because these hosts do not all access the global Internet at the same time. 

The simplest NAT is a middlebox that uses a one-to-one mapping between a private IP address and a public IP address. To understand its operation, let us assume that a NAT such as the one shown above has booted. When the NAT receives a first packet from source `S` in the internal network destined to the public Internet, it creates a mapping between internal address `S` and the first address of its pool of public addresses (`P1`). Then it translates the received packet so that it can be sent to the public Internet. This translation is performed as followed :

 - the source address of the packet (`S`) is replaced by the mapped public address (`P1`)
 - the checksum of the IP header is incrementally updated as its content has changed
 - if the packet carried a TCP or UDP segment, the transport layer checksum found of the included segment must also be updated as it is computed over the segment and a pseudo-header that includes the source and destination addresses

When a packet destined to `P1` is received from the public Internet, the NAT consults its mapping table to find `S`. The received packet is translated and forwarded in the internal network. 

This works as long as the pool of public IP addresses of the NAT does not become empty. In this case, a mapping must be removed from the mapping table to allow a packet from a new host to be translated. This garbage collection can be implemented by adding to each entry in the mapping table a timestamp that contains the last utilisation time of a mapping entry. This timestamp is updated each time a the corresponding entry is used. Then, the garbage collection algorithm can remove the oldest mapping entry in the table.

A drawback of such as simple enterprise NAT is the size of the pool of public IPv4 addresses that is often too small to allow a large number of hosts to share such a NAT. In this case, a better solution is to allow the NAT to translate both IP addresses and port numbers. 

Such a NAT maintains a mapping table that maps an internal IP address and TCP port number with an external IP address and TCP port number. When such a NAT receives a packet from the internal network, it performs a lookup in the mapping table with the packet's source IP address and source TCP port number. If a mapping is found, the source IP address and the source TCP port number of the packet are translated with the values found in the mapping table, the checksums are updated and the packet is sent to the global Internet. If no mapping is found, a new mapping is created with the first available couple `(IP address, TCP port number)` and the packet is translated. The entries of the mapping table are either removed at the end of the corresponding TCP connection is the NAT tracks TCP connection state like a stateful firewall or after some idle time.

When such a NAT receives a packet from the global Internet, it lookups its mapping table with the packet's destination IP address and destination TCP port number. If a mapping is found, the packet is translated and forwarded in the internal network. Otherwise, the packet is discarded as the NAT cannot determine to which particular internal host the packet should be forwarded. For this reason, 

With :math:`2^{16}` different port numbers, a NAT may support a large number of hosts with a single public IPv4 address. However, it should be noted that some applications open a large number of TCP connections [Miyakawa2008]_. Each of these TCP connections consumes one mapping entry in the NAT's mapping table. 

.. index:: Application Level Gateway, ALG

NAT allows many hosts to share one or a few public IPv4 addresses. However, using NAT has two important drawbacks. First, it is difficult for external hosts to open TCP connections with hosts that are behind a NAT. Some consider this to be a benefit from a security viewpoint. However, a NAT should not be confused with a firewall as there are some techniques to traverse NATs. Second, NAT breaks the end-to-end transparency of the network and transport layers. The main problem is when an application layer protocol uses IP addresses in some of the ADUs that it sends. A popular example is ftp defined in :rfc:`959`. In this case, there is a mismatch between the packet header translated by the NAT and the packet payload. The only solution to solve this problem is to place on the NAT an Application Level Gateway (ALG) that understands the application layer protocol and can thus translate the IP addresses and port numbers found in the ADUs. However, defining an ALG for each application is costly and application developers should avoid using IP addresses in the messages exchanged in the application layer :rfc:`3235`.


.. index:: NAT66
.. sidebar:: IPv6 and NAT

 NAT has been very successful with IPv4. Given the size of the IPv6 addressing space, the IPv6 designers expected that NAT would never be useful with IPv6. The end-to-end transparency of IPv6 has been one of its key selling points compared to IPv4. However, recently the expected shortage of IPv4 addresses lead enterprise network administrators to consider IPv6 more seriously. One of the results of this analysis is that the IETF is considering the definition of NAT devices [WB2008]_ that are IPv6 specific. Another usage of NAT with IPv6 is to allow IPv6 hosts to access IPv4 destinations and conversely. The early IPv6 specifications included the Network Address Translation - Protocol Translation (NAT-PT) mechanism defined in :rfc:`2766`. This mechanism was later deprecated in :rfc:`4966` but has been recently restarted under the name NAT64 [BMvB2009]_. A NAT64 is a middlebox that performs the IPv6<->IPv4 packet translation to allow IPv6 hosts to contact IPv4 servers. 



Routing in IP networks
######################

In a large IP network such as the global Internet, routers need to exchange routing information. The Internet is an interconnection of networks, often called domains, that are under different responsibilites. As of this writing, the Internet is composed on more than 30,000 different domains and this number is still growing. A domain can be a small enterprise that manages a few routers in a single building, a larger entreprise with hundred routers at multiple locations or a large Internet Service Provider that manages thousands of routers. Two classes of routing protocols are used to allow these domains to efficiently exchange routing information. 


.. figure:: fig/network-fig-093-c.png
   :align: center
   :scale: 70
   
   Organisation of a small Internet


The first class of routing protocols are the `intradomain routing protocols` (sometimes also called the interior gateway protocols or :term:`IGP`). An intradomain routing protocol is used by all the routers inside a domain to exchange routing information about the destinations that are reachable inside the domain. There exist several routing protocols. Some domains use :term:`RIP`  which is a distance vector protocols. Other domains use link-state routing protocols such as :term:`OSPF` or :term:`IS-IS`. Finally, some domains use static routing or proprietary protocols such as :term:`IGRP` :term:`EIGRP`   

These intradomain routing protocols usually have two objectives. First, they distribute routing information that corresponds to the shortest path between two routers in the domain. Second, they should allow the routers to quickly recover from link and router failures.

The second class of routing protocols are the `interdomain routing protocols` (sometimes also called the exterio gateway protocols or :term:`EGP`). The objective of an interdomain routing protocol is to distribute routing information between domains. For scalability reasons, an interdomain routing protocol must distribute aggregated routing information and considers each domain as a blackbox.

A very important difference between intradomain and interdomain routing are the `routing policies` that are used by each domain. Inside a single domain, all routers are considered equal and when several routes are available to reach a given destination prefix, the best route is selected based on technical criterias such as the route with the shortest delay, the route with the minimum number of hops, the route with the highest bandwidth, ... When we consider the interconnection of domains that are managed by different organisations, this is not true anymore. Each domain implements its own routing policy. 

As we will see later, the objective of the interdomain routing protocol is to find the `cheapest` route towards each destination. There is only one interdomain routing protocol : :term:`BGP`.


Intradomain routing 
===================

In this section, we briefly describe the key features of the two main intradomain unicast routing protocols : RIP and OSPF. 

.. index:: RIP

RIP
---

The Routing Information Protocol (RIP) is the simplest routing protocol that was standardised for the TCP/IP protocol suite. RIP is defined in :rfc:`2453`. Additional information about RIP may be found in [Malkin1999]_

RIP routers periodically exchange RIP messages. The format of these messages is show below. A RIP message is sent inside a UDP segment with destination port set to `521`. A RIP message contains several fields. The `Cmd` field indicates whether the RIP message is a request or a response. Routers send one of more RIP response messages every 30 seconds. These messages contain the summary of the router's routing table. The RIP requests messages can be used by routers or hosts to query other routers about the content of their routing table. A typical usage is when a router boots and wants to receive quickly the RIP responses from its neighbours to compute its own routing table. The current version of RIP is version 2 defined in :rfc:`2453` for IPv4 and :rfc:`2080` for IPv6. 


.. figure:: fig/network-fig-094-c.png
   :align: center
   :scale: 70
   
   RIP message format


The RIP header contains an authentication field. This authentication can be used by network administrators to ensure that only the RIP messages sent by routers that they manage are used to build the routing tables. :rfc:`2453` only supports a basic authentication scheme where all routers are configured with the same password and include this password in all RIP messages. This is not very secure since an attacker can know the password by capturing a single RIP message. However, this password can protect against configuration errors. Stronger authentication schemes are described in :rfc:`2082` and :rfc:`4822`, but the details of these mechanisms are outside the scope of this section.

Each RIP message contains a set of route entries. Each route entry is encode as a 20 bytes field whose format is shown below. RIP was designed initially to be suitable for different network layer protocols. Some implementations of RIP were used in XNS or IPX networks. The first field of the RIP route entry is the `Address Family Identifier` (`AFI`). This identifier indicates the type of address found in the route entry [#fafi]_. IPv4 uses `AFI=1`. The other important fields of the route entry are the IPv4 prefix, the netmask that indicates the length of the subnet identifier and is encoded as a 32 bits netmask and the metric. Although the metric is encoded as a 32 bits field, the maximum RIP metric is `15`(for RIP, :math:`16=\inf`)


.. figure:: fig/network-fig-095-c.png
   :align: center
   :scale: 70
   
   Format of the RIP IPv4 route entries

With a 20 bytes route entry, it was difficult to use the same format as above to support IPv6. Instead of defining a variable length route entry format, the designers of :rfc:`2080` defined a new format that does not include an `AFI` field. The format of the route entries used by :rfc:`2080` is shown below. `Plen` is the length of the subnet identifier in bits and the metric is encoded as one byte. The maximum metric is still `15`.

.. figure:: fig/network-fig-098-c.png
   :align: center
   :scale: 70
   
   Format of the RIP IPv6 route entries

.. sidebar:: A note on timers

 The first RIP implementations sent their distance vector exactly every 30 seconds. This worked well in most networks, but some researchers noticed that routers were sometimes overloaded because they were processing too many distance vectors at the same time [FJ1994]_. They collected packet traces in these networks and found that after some time the routers' timers became synchronised, i.e. almost all routers were sending their distance vectors at almost the same time. This synchronisation of the transmission times of the distance vectors caused an overload on the routers' CPU but also increased the convergence time of the protocol in some cases. It is mainly due to the fact that all routers set their timers to the same expiration time after having processed the received distance vectors. `Sally Floyd`_ and `Van Jacobson`_ proposed in [FJ1994]_ a simple solution to solve this synchronisation problem. Instead of advertising their distance vector exactly after 30 seconds, a router should send its next distance vector after a a delay of delay chosen randomly in the [15,45] interval :rfc:`2080`. This randomisation of the delays prevents the synchronisations that occur with a fixed delay and is used nowadays by most protocols.

.. index:: OSPF

OSPF
----

OSPF is defined in :rfc:`2328`. The last version of OSPF that supports IPv6 is defined in :rfc:`5340`. Additional informations about OSPF may be found in [Moy1998]_.

areas
LANs (again !)
HELLOs
LSAa
other details 

:rfc:`2991` ECMP


.. sidebar:: How to quickly detect a link failure ?

 triggers from physical layer [FFEB2005]_
 explain fats hello and the difficulty of implementing them
 briefly explain BFD [KW2009]_
 [VPD2004]_
  explain flap and the backoff timers to slowdown things




Interdomain routing
===================

As explained earlier, the Internet is composed of more than 30,000 different networks [#fasnum]_ called `domains`. Each domain is composed of a group of routers and hosts that are managed by the same organisation. Example domains include belnet_, sprint_, level3_, geant_, abilene_ cisco_, google_ ... 

.. index:: stub domain, transit domain

Each domain contains a set of routers. From a routing viewpoint, these domains can be divided in two classes : the `transit` and the `stub` domain. A `stub` domain sends and receive packets whose source or destination are one of its hosts. A `transit` domain is a domain that provides a transit service for other domains, i.e. the routers in this domain forward packets whose source and destinations do not belong to the transit domain. As of this writing, there are about 85% of stub domains in the Internet. A `stub` domain that is connected to a single transit domain is called a `single-homed stub`. A `multihomed stub` is a `stub` domain connected to two or more transit providers.

.. figure:: fig/network-fig-089-c.png
   :align: center
   :scale: 70
   
   Transit and stub domains 

The stub domains can be further classified by considering whether they mainly send or receive packets. An `access-rich` stub domain is a domain that contains a lot of hosts that mainly receive packets. Typical examples include small ADSL- or cable model-based Internet Service Providers or entreprise networks. On the other hand, a `content-rich` stub domain is a domain that mainly produces packets. Examples of `content-rich` stub domains include google_, yahoo_, microsoft_, facebook_ or content distribution networks such as akamai_ or limelight_ During the last years, we have seen a rapid growth of these `content-rich` stub domains. Recent measurements [ATLAS2009]_ indicate that a growing fraction of all the packets exchanged on the Internet are produced in the datacenters managed by these content providers.

Domains need to be interconnected to allow a host inside a domain to exchange IP packets with hosts located in other domains. From a physical viewpoint, domains can be interconnected in two different ways. The first solution is to directly connect a router belonging to the first domain with a router inside the second domain. Such links between domains are called private interdomain links or `private peering links`. In practice, for redundancy of performance reasons, several links are usually established between different routers in the two domains that are interconnected.

.. figure:: fig/network-fig-104-c.png
   :align: center
   :scale: 70
   
   Interconnection of two domains via a private peering link 


Such `private peering links` are useful when for example an entreprise or university network needs to be connected to its Internet Service Provider. However, some domains are connected to hundreds of other domains [#fasrank]_. For some of these domains, using only private peering links would be too costly. A better solution to allow a many domains to interconnect cheaply are the `Internet eXchange Points` (:term:`IXP`). An :term:`IXP` is usually some space in a data center that hosts routers belonging to different domains. A domains willing to exchange packets with other domains present at the :term:`IXP` installs one of its routers on the :term:`IXP` and connects it to other routers inside its own network. The IXP contains a Local Area Network to which all the participating routers are connected. When two domains that are present at the IXP wish to exchange packets, they simply use the Local Area Network. IXPs are very popular in Europe and many Internet Service Providers and Content providers are present on these IXPs.

.. figure:: fig/network-fig-105-c.png
   :align: center
   :scale: 70
   
   Interconnection of two domains at an Internet eXchange Point

In the early days of the Internet, domains would simply exchange all the routes they know to allow a host inside one domain to reach any host in the global Internet. However, in today's highly commercial Internet, this is not true anymore. For economical reasons, there are different types of relationships that can be established between domains that are connected via a peering links. 

Furthermore, while intradomain routing usually prefers some routes over others based on their technical merits (e.g. prefer path with the minimum number of hops, prefer path with the minimum delay, prefer high bandwidth paths over low bandwidth ones, ...) interdomain routing mainly deals with economical issues. For interdomain routing, the cost of using a path is often more important than the quality of the path measured by its delay or bandwidth.

.. index:: customer-provider peering relationship

The first category of peering relationship is the `customer->provider` relationship. Such a relationship is used when a customer domain pays an Internet Service Provider to be able to exchange packets with the global Internet over a peering link. A similar relationship is used when a small Internet Service Provider pays a larger Internet Service Provider to exchange packets with the global Internet. 


.. figure:: fig/network-fig-106-c.png
   :align: center
   :scale: 70
   
   A simple Internet with peering relationships

To understand the `customer->provider` relationship, let us consider the simple internetwork shown in the figure above. In this internetwork, `AS7` is an enterprise domain that is connected to one provider : `AS4`. The contract between `AS4` and `AS7` allows a host inside `AS7` to exchange packets with any host in the internetwork. To enable this exchange of packets, `AS7` must know a route towards any domain and all the domains of the internetwork must learn a route via `AS4` that allows them to reach hosts inside `AS7`. From a routing viewpoint, the commercial contract between `AS7` and `AS4` will lead to the following routes being exchanged :

 - over a `customer->provider` relationship, the `customer` domain advertises to its `provider`  all its routes and all the routes that it has learned from its own customers.
 - over a `provider->customer` relationship, a `provider` advertises all the routes that it knows to its `customer`

The second rule ensures that the customer domain will receive a route towards all destinations that are reachable via its provider. The first rule allows the routes of the customer domain to be distributed through the Internet.

Coming back to the figure above, `AS4` advertises to its two providers `AS1` and `AS2` its own routes and the routes learned from its customer, `AS7`. On the other hand, `AS4` advertises to `AS7` all the routes that it knows. 

.. index:: shared-cost peering relationship

The second type of peering relationship is the `shared-cost` peering relationship. Such a relationship usually does not involve a paiment in contrast with the `customer->provider` relationship. A `shared-cost` peering relationship is usually established between domains having a similar size and geographic coverage. For example, consider the figure above. If `AS3` and `AS4` exchange many packets via `AS1`, they both need to pay `AS1`. A cheaper alternative for `AS3` and `AS4` would be to establish a `shared-cost` peering. Such a peering can be established at IXPs where both `AS3` and `AS4` are present or by using private peering links. This `shared-cost` peering should be used to exchange packets between hosts inside `AS3` and hosts inside `AS4`. However, `AS3` does not want to receive on the `AS3-AS4` `shared-cost` peering links packets whose destination belongs to `AS1` and `AS3` would have to pay to send these packets to `AS1`. 

From a routing viewpoint, over a `shared-cost` peering relationship a domain only advertises its internal routes and the routes that it has learned from its customers. This restriction ensures that only packets destined to the local domain or one of its customers will be received over the `shared-cost` peering relationship. This implies that the routes that have been learned from a provider or from another `shared-cost` peer will not be advertised over a `shared-cost` peering relationship. This is motivated by economical reasons. If a domain was advertising over a `shared-cost` peering relationship that does not bring revenue the routes that it learned from a provider it would have allowed its `shared-cost` peer to use the link with its provider without any payment. If a domain was advertising over a `shared-cost` peering relationship the routes learned over another `shared-cost` peering relationship, it would have allowed these `shared-cost` peers to use its own network (which may span one or more continents) freely to exchange packets.


.. index:: sibling peering relationship

Finally, the last type of peering relationship is the `sibling`. Such a relationship is used when two domains exchange all their routes in both directions. In practice, such a relationship is only used between domains that belong to the same company.

.. index:: interdomain routing policy

These different types of relationships are implemented in the `interdomain routing policies` that are defined by each domain. The `interdomain routing policy` of a domain is composed of three main parts :
 - the `import policy` that specifies, for each peering relationship, the routes that can be accepted from the neighboring domain (the non-acceptable routes are ignored and the domain never uses them to forward packets)
 - the `export policy` that specifies, for each peering relationship, the routes that can be advertised to the neighboring domain 
 - the `ranking` algorithm that is used to prefer some route over others when a domain has received several routes towards the same destination prefix

.. index:: import policy, export policy

A domain's import and export policies can be defined by using the Route Policy Specification Language (RPSL) specified in :rfc:`2622`. Some Internet Service Providers, notably in Europe, use RPSL to document [#fripedb]_ their import and export policies. Several tools allow to easily convert a RPSL policy into router commands. 

The figure below provides a simple example of import and export policies for two domains in a simple internetwork. In a RPSL policy, the keyword `ANY` is used to replace any route from any domain. It is typically used on by a provider to indicate that it announces all its routes to a customer over a `provider->customer` relationship. This is the case for `AS4`'s export policy. The example below shows clearly the difference between a `provider->customer` and a `shared-cost` peering relationship. `AS4`'s export policy indicates that it announces only its internal routes (`AS4`) and the routes learned from its clients (`AS7`) over its `shared-cost` peering with `AS3` while it advertises to `AS7` all the routes that it uses (including the routes learned from `AS3`). 

.. figure:: fig/network-fig-109-c.png
   :align: center
   :scale: 70
   
   Import and export policies 

.. index:: BGP, Border Gateway Protocol

The Border Gateway Protocol
---------------------------


The Internet uses a single interdomain routing protocol : the Border Gateway Protocol (BGP). The current version of BGP is defined in :rfc:`4271`. BGP differs from the intradomain routing protocols that we have already discussed in several ways. First, BGP is a `path-vector` protocol. When a BGP router advertises a route towards a prefix, it announces the IP prefix and the interdomain path used to reach this prefix. From BGP's viewpoint, each domain is identified by a unique `Autonomous System` (AS) number [#fasdomain]_ and the interdomain path contains the AS numbers of the transit domains that are used to reach the associated prefix. This interdomain path is called the `AS Path`. Thanks to these AS-paths, BGP does not suffer from the count-to-infinity problems that affect distance vector routing protocols. Furthermore, the AS-Path can be used to implement some routing policies. Another difference between BGP and the intradomain routing protocols is that a BGP router does not advertise the contents of its routing table to its neighbours regularly. Given the size of the global Internet, routers would be overloaded by the number of BGP messages that they need to process. A BGP router uses incremental updates, i.e. it only announces to its neighbours the routes that have changed.

The figure below shows a simple example of the BGP routes that are exchanged between domains. In this example, prefix `1.0.0.0/8` is announced by `AS1`. `AS1` advertises to `AS2` a BGP route towards this prefix. The AS-Path of this route indicates that `AS1` is the originator of the prefix. When `AS4` receives the BGP route from `AS1`, it reannounces it to `AS2` and adds its AS number in the AS-Path. `AS2` has learned two routes towards prefix `1.0.0.0/8`. It compares the two routes and prefers the route learned from `AS4` based on its own ranking algorithm. `AS2` advertises to `AS5` a route towards `1.0.0.0/8` with its AS-Path set to `AS2:AS4:AS1`. Thanks to the AS-Path, `AS5` knows that if it sends a packet towards `1.0.0.0/8` the packet will first pass through `AS2`, then through `AS4` before reaching its destination inside `AS1`.


.. figure:: fig/network-fig-111-c.png
   :align: center
   :scale: 70
   
   Simple exchange of BGP routes 

.. index:: BGP peer

A BGP peering session is established between two routers belonging to two different domains that are directly connected. As explained earlier, the physical connection between the two routers can be implemented as a private peering link or over an Internet eXchange Point. A BGP session between two adjacent routers runs above a TCP connection (the default BGP port is 179). In contrast with intradomain routing protocols that exchange IP packets or UDP segments, BGP runs above TCP because TCP ensures a reliable delivery of the BGP messages sent by each router without forcing the routers to implement acknowledgements, checksums, ... Furthermore, the two routers will consider the peering link to be up as long as the BGP session and the underlying TCP connection remains up [#flifetimebgp]_. The two endpoints of a BGP session are called `BGP peers`.

.. figure:: fig/network-fig-112-c.png
   :align: center
   :scale: 70
   
   A BGP peering session between two directly connected routers

In practice, to establish a BGP session between routers `R1` on `R2` on the figure above, the network administrator of `AS3` must first configure on `R1` the IP address of `R2` on the `R1-R2` link and the AS number of `R2. Router `R1` will then try to regularly establish the BGP session with `R2`. `R2` will only accept to establish the BGP session with `R1` once it`has been configured with the IP address of `R1` and its AS number. For security reasons, a router never establishes a BGP session that has not been manually configured on the router. 


.. index BGP OPEN, BGP NOTIFICATION, BGP KEEPALIVE, BGP UPDATE

The BGP protocol :rfc:`4271` defines several types of messages that can be exchanged on a BGP session :
 - `OPEN` : this message is sent as soon as the TCP connection between the two routers has been established. It allows to initialise the BGP session and negotiate some options. Details about this message may be found in :rfc:`4271`
 - `NOTIFICATION` : this message is used to terminate a BGP session, usually because an error has been detected by the BGP peer
 - `UPDATE`: this message is used to advertise new or modified routes or to withdraw previsously advertised routes
 - `KEEPALIVE` : when a BGP router has not sent an `UPDATE` message during the last 30 seconds, it shall send a `KEEPALIVE` message to confirm to the other peer that it is still up. If a peer does not receive any BGP message during a period of 90 seconds [#fdefaultkeepalive]_, the BGP session is considered to be down and all the routes learned over this session are withdrawn. 


.. sidebar:: Origin of the routes advertised by a BGP router

 A frequent practical question about the operation of BGP is how a BGP router decides to originate or advertise a route for the first time. In practice, this occurs in two situations :

  - the router has been manually configured by the network operator to always advertise one or several routes on a BGP session. For example, on the BGP session between UCLouvain and its provider, belnet_ , UCLouvain's router always advertises the `130.104.0.0/16` IPv4 prefix assigned to the campus network
  - the router has been configured by the network operator to advertise over its BGP session some of the routes that it learns with its intradomain routing protocol. For example, an entreprise router may advertise over a BGP session with its provider the routes to remote sites when these routes are reachable and advertised by the intradomain routing protocol
 The first solution is the most frequent. Advertising routes learned from an intradomain routing protocol is not recommended as if the route flaps, this will cause a large number of BGP messages being exchanged in the global Internet.


As explained earlier, BGP relies on incremental updates. This implies that when a BGP session starts, each router will first send BGP `UPDATE` messages to advertise to the other peer all the exportable routes that it knows. Once all these routes have been advertised, the BGP router will only send BGP `UPDATE` message about a prefix if the route is new, one of its attributes has changed or the route became unreachable and must be withdrawned. The BGP `UPDATE` message allows BGP routers to efficiently exchange such information while minimising the number of bytes exchanged. Each `UPDATE` message contains :

 - a list of IP prefixes that are withdraw
 - a list of IP prefixes that are (re-)advertised
 - the set of attributes (e.g. AS-Path) associated to the of the advertised prefixes


In the remainder of this chapter, and although all routing information is exchnaged by using BGP `UPDATE` messages, we assume for simplicity that a BGP message contains only information about one prefix and we will use the words :

 - `Withdraw message` to indicate a BGP `UPDATE` message containing one route that is witdrawn
 - `Update message` to indicate a BGP `UPDATE` containing one new or updated route with its attributes 

.. index:: BGP Adj-RIB-In, BGP Adj-RIB-Out, BGP RIB

From a conceptual viewpoint, a BGP router connected to `N` BGP peers, can be described as being composed of four parts as shown in the figure below.


.. _bgprouter:

.. figure:: fig/network-fig-113-c.png
   :align: center
   :scale: 70
   
   Organisation of a BGP router 

In this figure, the router receives BGP messages on the left part of the figure, processes these messages and possibly sends BGP messages on the right part of the figure. A BGP router contains three important data structures :

 - the `Adj-RIB-In` contains the BGP routes that have been received from each BGP peer. The routes in the `Adj-RIB-In` are filtered by the `import filter` before being placed in the `BGP-Loc-RIB`
 - the `Local Routing Information Base` (`Loc-RIB`) contains all the routes that are considered as acceptable by the router. The `Loc-RIB` may contain several routes, learned from different BGP peers, towards the same destination prefix.
 - the `Forwarding Information Base` (`FIB`) is used by the dataplane to forward packets towards their destination. The `FIB` contains, for each destination, the best route that has been selected by the `BGP decision process`. This decision process is an algorithm that selects, for each destination prefix, the best route according to the router's ranking process that is part of its policy.
 - the `Adj-RIB-Out` contains the BGP routes that have been advertised to each BGP peer. The `Adj-RIB-Out` for a given peer is built by applying the peer`s `export filter` on the routes that have been installed in the `FIB`

When a BGP session starts, the routers first exchange `OPEN` messages to negotiate the options that will apply throughout the entire session. Then, each router will advertise to its peer all its exportable routes. A BGP router can only advertise a router that it actually uses to forward packets. Thus, only the routes that have been installed in the `FIB` can be advertised to a peer. These routes are subject to the `export filter`. The `export filter` is a set of rules that define which routes can be advertised over the corresponding session, possibly after having modified some of its attributes. One `export filter` is associated to each BGP session. For example, on a `shared-cost peering`, the `export filter` will only select the internal routes and the routes that have been learned from a `customer`. The pseudocode below shows the initialisation of a BGP session ::

 Initialize_BGP_Session(RemoteAS, RemoteIP)
 { 
 /* Initialize and start BGP session */
 /* Send BGP OPEN Message to RemoteIP on port 179*/
 /* Follow BGP state machine */ 

 /* advertise local routes and routes learned from peers*/
 foreach (destination=d inside BGP Loc-RIB)
 {
  B=build_BGP_UPDATE(d); // best path
  S=apply_export_filter(RemoteAS,B);
  if (S<>NULL)
	{ /* send UPDATE message */
         send_UPDATE(S,RemoteAS, RemoteIP)
        }
  }	
 /* entire RIB was sent */
 /* new UPDATE will be sent only to reflect local or distant
   changes in routes */
 ...
 }



In the above pseudocode, the `build_BGP_UPDATE(d)` procedure extracts from the `BGP Loc-RIB` the best path towards destination `d` (i.e. the route installed in the FIB) and prepares the corresponding BGP `UPDATE` message. This message is then passed to the `export filter` that returns NULL if the route cannot be advertised to the peer or the (possibly modified) BGP `UPDATE` message to be advertised. BGP routers allow network administrators to specify very complex `export filters`, see e.g. [WMS2004]_. A simple `export filter` that implements the equivalent of `split horizon` is shown below ::

 BGPMsg Apply_export_filter(RemoteAS, BGPMsg)
 { /* check if Remote AS already received route */
 if (RemoteAS isin BGPMsg.ASPath)
   BGPMsg==NULL;
  /* Many additional export policies can be configured : */
  /* Accept or refuse the BGPMsg */
  /* Modify selected attributes inside BGPMsg */
 }


Once all exportable routes have been advertised, the router should only over the BGP session the new routes, the routes that become unreachable or the routes whose attribute change. When a BGP router receives a BGP message, this message will be processed as shown by the pseudocode below ::

 Recvd_BGPMsg(Msg, RemoteAS)
 { 
  B=apply_import_filer(Msg,RemoteAS);
  if (B==NULL) /* Msg not acceptable */
	exit();
  if IsUPDATE(Msg)
  { 
   Old_Route=BestRoute(Msg.prefix); 
   Insert_in_RIB(Msg);
   Run_Decision_Process(RIB);
   if (BestRoute(Msg.prefix)<>Old_Route)
   { /* best route changed */
    B=build_BGP_Message(Msg.prefix);
    S=apply_export_filter(RemoteAS,B);
    if (S<>NULL) /* announce best route */
	send_UPDATE(S,RemoteAS);     
    else if (Old_Route<>NULL) 
     send_WITHDRAW(Msg.prefix);
   } 
  if IsWITHDRAW(Msg)
  { 
   Old_Route=BestRoute(Msg.prefix); 
   Remove_from_RIB(Msg);
   Run_Decision_Process(RIB);
   if (Best_Route(Msg.prefix)<>Old_Route)
   { /* best route changed */
     B=build_BGP_Message(d);
     S=apply_export_filter(RemoteAS,B);
     if (S<>NULL) /* still one best route */
       send_UPDATE(S,RemoteAS, RemoteIP);
     else if(Old_Route<>NULL)/* no best route anymore */
       send_WITHDRAW(Msg.prefix,RemoteAS,RemoteIP);
   }
  }
 }     

When a BGP message is received, the router first applies the peer's `import filter` to verify whether the message is acceptable or not. If the message is not acceptable, the processing stops. The pseudocode below shows a simple `import filter`. This `import filter` accepts all routes, except those that already contain the local AS in their AS-Path. If such a route was used, it would cause a routing loop. Another example of an `import filter` would be a filter used by an Internet Service Provider on a session with a customer to only accept routes towards the IP prefixes assigned to the customer by the provider. On real routers, `import filters` can be much more complex and some `import filters` modify the attributes of the received BGP `UPDATE`::

 BGPMsg apply_import_filter(RemoteAS, BGPMsg)
 { /* check that we are not already inside  ASPath */ 
  if (MyAS isin BGPMsg.ASPath)
   BGPMsg==NULL;
  /* Many additional import policies can be configured : */
  /* Accept or refuse the BGPMsg */
  /* Modify selected attributes inside BGPMsg */
 }


.. sidebar:: The bogon filters

 Another example of frequently used `import filters` are the filters that Internet Service Providers use to ignore bogon routes. In the ISP community, a bogon route is a route that should not be advertised on the global Internet. Typical examples include the private IPv4 prefixes defined in :rfc:`1918`, the loopback prefixex (`127.0.0.1/8` and `::1/128`) or the IP prefixes that have not yet been allocated by IANA. A well managed BGP router should ensure that it never advertises bogons on the global Internet. Detailed information about these bogons may be found at http://www.team-cymru.org/Services/Bogons/


If the BGP message is acceptable, we need to distinguish two cases. If this is an `Update message` for prefix `p`, this can be a new route for this prefix or a modification of the route's attributes. The router first retrieves from its `RIB` the best route towards prefix `p`. Then, the new route is inserted in the `RIB` and the `BGP decision process` is run to find the best route towards destination `p` changes. A BGP message only needs to be sent to the router's peers if the best route has changed. For each peer, the router applies the  `export filter` to verify whether the route can be advertised. If yes, the filtered BGP message is sent. Otherwise, a `Withdraw message` is sent. When the router receives a `Withdraw message`, it also verifies whether the removal of the route from its `RIB` caused its best route towards this prefix to change. It should be noted that, depending on the content of the `RIB` and the `export filters`, a BGP router may need to send a `Withdraw message` to a peer after having received an `Update message` from another peer and conversely.


To understand the operation of BGP in an IPv4 network, let us consider the simple network composed of three routers located in three different ASes and shown in the figure below.

.. figure:: fig/network-fig-121-c.png
   :align: center
   :scale: 70
   
   Utilisation of the BGP nexthop attribute


This network contains three routers : `R1`, `R2` and `R3`. Each router is attached to a local IPv4 subnet that it will advertise by using BGP. There are two BGP sessions, one between `R1` and `R2` and the second between `R2` and `R3`. A `/30` subnet is used on each interdomain link (`195.100.0.0/30` on `R1-R2` and 195.100.0.4/30` on `R2-R3`). The BGP sessions run above TCP connections established between the neighbouring routers (e.g. `195.100.0.1 - 195.100.0.2` for the `R1-R2 session).

.. index:: BGP nexthop

Let us assume that the `R1-R2` BGP session is the first to be established. A `BGP Update` message sent on such a session contains three informations :

 - the advertised prefix
 - the `BGP nexthop`
 - the attributes including the AS-Path 

We will use the notation `U(prefix, nexthop, attributes)` to represent such a `BGP Update` message in this section. Similarly, `W(prefix)` will represent a `BGP withdraw` for the specified prefix. On the `R1-R2` session has been established, `R1` sends `U(194.100.0.0/24,195.100.0.1,AS10)` to `R2` and `R2` sends `U(194.100.2.0/23,195.100.0.2,AS20)`. At this point, `R1` can reach `194.100.2.0/23` via `195.100.0.2` and `R2` can reach `194.100.0.0/24` via `195.100.0.1`.

When the `R2-R3` has been established, `R3` sends `U(194.100.1.0/24,195.100.0.6,AS30)`. `R2` will announce on the `R2-R3` session all the routes inside its RIB. I will thus send to `R3` : `U(194.100.0.0/24,195.100.0.5,AS20:AS10)` and `U(194.100.2.0/23,195.100.0.5,AS20)`. Note that when `R2` advertises the route that it learned from `R1`, it updates the BGP nexthop and adds it AS number in the AS-Path. `R2` will also send `U(194.100.1.0/24,195.100.0.2,AS20:AS30)` to `R1` on the `R1`R3` session. At this point, all BGP routes have been exchanged and all routers can reach `194.100.0.0/24`, `194.100.2.0/23` and `194.100.1.0/24`.

If the link between `R2` and `R3` fails, `R3` will detect the failure because it did not receive `KEEPALIVE` messages recently from `R2`. At this time, `R3` will remove from its RIB all the routes learned over the `R2-R3` BGP session. `R2` will also remove from its RIB the routes learned from `R3`. `R2` will also send  `W(194.100.1.0/24)` to `R1` over the `R1-R3` BGP session since it does not have a route anymore towards this prefix.


Most networks that use BGP contain more than one router. For example, consider the network shown in the figure below where `AS20` contains two different routers attached to interdomain links : `R2` and `R4`. In this network, two routing protocols are used by `R2` and `R4`. They use an intradomain routing protocol to distribute the routes towards the internal prefixes : `195.100.0.8/30`, `195.100.0.0/30`, ... `R2` and `R4` also use BGP. `R2` will receive the routes advertised by `AS10` while `R4` will receive the routes advertised by `AS30`. These two routers will need to exchange the routes that they have respectively received over their BGP sessions. 

.. figure:: fig/network-fig-136-c.png
   :align: center
   :scale: 70
   
   A larger network using BGP

A first solution to allow `R2` and `R3` to exchange the interdomain routes that they have learned over their respective BGP sessions would be to configure the intrdomain routing protocol to distribute inside `AS20` the routes learned over BGP sessions. Although routers support this feature, this is a bad solution for two reasons :

 1. Intradomain routing protocols cannot distribute the attributes that are attached to a BGP route. If `R4` received via the intradomain routing protocol a route towards `194.100.0.0/23` that `R2` learned via BGP, it would not know that the route was originated by `AS10` and the only advertisement that it could send to `R3` would contain an invalid AS-Path
 2. Intradomain routing protocols have not been designed to support the hundreds of thousands of routes that a BGP router can receive on today's global Internet.

.. index:: eBGP, iBGP

The best solution to allow BGP routers to distribute, inside an AS, all the routes learned over BGP sessions is to establish BGP sessions among all the BGP routers inside an AS. In practice, we distinguish between two types of BGP sessions :

 - :term:`eBGP session` or `external BGP session`. Such a BGP session is established between two routers that are directly connected and belong to two different domains.
 - :term:`iBGP session` or `internal BGP session`. Such a BGP session is established between two routers belonging to the same domain. 


To understand the utilisation of an iBGP session, let us consider in the network shown below what happens when router `R1` sends `U(194.100.0.0/23,195.100.0.1,AS10)`. This BGP message is processed by `R2` that advertises it over its `iBGP session` with `R4`. The `BGP Update` sent by `R2` contains the same nexthop and the same AS-Path as in the `BGP Update` received by `R2`. `R4` then sends `U(194.100.0.0/23,195.100.0.5,AS20:AS10)` to `R3`. Note that the BGP nexthop and the AS-Path are only updated [#fnexthopself]_ when a BGP route is advertised over an `eBGP session`.

.. figure:: fig/network-fig-138-c.png
   :align: center
   :scale: 70
   
   iBGP and eBGP sessions

In practice, each BGP router inside a domain will maintain an `iBGP session` with each other BGP router in the domain [#frr]_. This will create a full-mesh of `iBGP sessions` among all BGP routers of the domain. `iBGP sessions`, like `eBGP sessions` run over TCP connections. Note that in contrast with `eBGP sessions` that are established between directly connected routers, `iBGP sessions`

An important point to note about `iBGP sessions` is that a BGP router will only advertise a route over an `iBGP session` provided that :

 - the router uses this route to forward packets, and
 - the route was learned over one of the router's `eBGP sessions`

A BGP router does not advertise over an `iBGP session` a route that it has learned over another `iBGP session` while it can, of course, advertise over `eBGP sessions` routes learned over `iBGP sessions`. This difference between the behaviour of a BGP router over `iBGP` and `eBGP` session is due to the utilisation of a full-mesh of `iBGP sessions`. Consider a network containing three BGP routers : `A`, `B` and `C` interconnected via a full-mesh of iBGP sessions. If router `A` learns a route towards prefix `p` from router `B`, router `A` does not need to advertise the received route to router `C` since router `C` will also learn the same route over the `C-B` `iBGP session`.

.. index:: loopback interface

.. sidebar:: Loopback interfaces and iBGP sessions

 In addition to their physical interfaces, routers can also be configured with a special loopback interface. A loopback interface is a software interface that is always up. Thus, the IP address associated to a loopback interface is always reachable while an IP address associated to a physical interface will become unreachable as soon as the corresponding physical interface fails. When a loopback interface is configured on a router, the address associated to this interface is advertised by the intradomain routing protocol inside the domain. `iBGP sessions` are usually established by using the router's loopback addresses as endpoints. This allows the `iBGP session` and its underlying TCP connection to remain up even if physical interfaces fail on the routers.

.. example route not selected ?

Now that routers can learn interdomain routes by using the iBGP and eBGP sessions, let us examine what happens when router `R3` sends a packet destined to `194.100.1.234`. `R3` forwards this packet to `R4`.  `R4` uses an intradomain routing protocol and BGP. Its BGP routing table contains the following longest prefix match : 

 - `194.100.0.0/23` via `195.100.0.1`

This routes indicates that to forward a packet towards `194.100.0.0/23`, `R4` needs to forward the packet along the route towards `195.100.0.1`. However, `R4`is not directly connected to `195.100.0.1`. `R4` learned a route towards this address thanks to its intradomain routing protocol that distributed the following routes :

 - `195.100.0.0/30`  via `195.100.0.10`
 - `195.100.0.4/30`  East
 - `195.100.0.8/30`  North
 - `194.100.2.0/23`  via `195.100.0.10`
 - `194.100.0.4/23`  West

To build its forwarding table, `R4` must combine the routes learned from the intradomain routing protocol with the routes learned from BGP. Thanks to its intradomain routing table, `R4` will replace for each interdomain route the BGP nexthop with its shortest path computed by the intradomain routing protocol. In the figure above, `R4` will thus replace `195.100.0.1` by `195.100.0.10` to which it is directly connected via its North interface. `R4` resulting forwarding table, that associates and outgoing interface for a directly connected prefix or a directly connected nexthop and an outgoing interface for other prefixes, is shown below :

 - `194.100.0.0/23`  via `195.100.0.10` (North)
 - `195.100.0.0/30`  via `195.100.0.10` (North)
 - `195.100.0.4/30`  East
 - `195.100.0.8/30`  North
 - `194.100.2.0/23`  via `195.100.0.10` (North)
 - `194.100.4.0/23`  West

There is thus a coupling between the interdomain and the intradomain routing tables used on routers. If the intradomain routes change, e.g. due to link failures or changes in link metrics, then the forwarding table must be update on each router as the shortest path towards a BGP nexthop may have changed.

The last point to be discussed before looking at the BGP decision process is that a network may contain routers that do not maintain any eBGP sessions. These routers can be stub routers attached to a single router in the network or core routers that reside on the path between two border routers that are using BGP as illustrated in the figure below.

.. figure:: fig/network-fig-138-c.png
   :align: center
   :scale: 70
   
   How to deal with non-BGP routers ?

In the scenario above, router `R2` needs to be able to forward a packet towards any destination in the `12.0.0.0/8` prefix inside `AS30`. Such a packet would need to be forwarded by router `R5` since this router resides on the path between `R2` and its BGP nexthop attached to `R4`. Two solutions can be used to ensure that `R2` will be able to forward such interdomain packets :

 - enable BGP on router `R5` and include this router in the `iBGP` full-mesh. Two iBGP sessions would be added in the figure above : `R2-R5` and `R4-R5`. This solution works and is used by many ASes. However, it forces all routers to have enough ressources (CPU and memory) to run BGP and maintain a large forwarding table
 - encapsulate the interdomain packets sent through the AS so that router `R5` never forward a packet whose destination is outside the local AS. Different encapsulation mechanisms exist. MultiProtocol Label Switching (MPLS) :rfc:`3031` and the Layer 2 Tuneling Protocol (L2TP) :rfc:`3931` are frequently used in large domains, but a detailed explanation of these techniques is outside the scope of this introduction. The simplest encapsulation scheme to understand is in IP in IP defined in :rfc:`2003`. This encapsulation scheme places an IP packet (called the inner packet), including its payload, as the payload of a larger IP packet (called the outer packet). It can be used by border routers to forward packets via routers that do not maintain a BGP routing table. For example, in the figure above, if router `R2` needs to forward a packet towards destination `12.0.0.1`, it can add at the front of this packet an IPv4 header whose source address is set to one of its IPv4 addresses and whose destination address is one of the IPv4 addresses of `R4`. The `Protocol` field of the IP header is set to `4` to indicate that it contains an IPv4 packet. The packet will be forwarded by `R5` to `R4`. Upon reception of the packet, `R4` will remove the outer header and consult its forwarding table to forward the packet towards `R3`. 

.. index:: BGP decision process

The BGP decision process
........................

Besides the import and export filters, a key difference between BGP and the intradomain routing protocols is that each domain can define is own ranking algorithm to determine which routes is preferred when several routes have been learned towards the same prefix. This ranking depends on several BGP attributes that can be attached to a BGP route.


.. index:: BGP local-preference

The first BGP attribute that is used to rank BGP routes is the `local-preference` (local-pref) attribute. This attribute is an unsigned integer that is attached to each BGP route received over an eBGP by the associated import filter.

When comparing routes towards the same destination prefix, a BGP router always prefer the routes with the highest `local-pref`. If the BGP router knows several routes with the same `local-pref`, it will prefer among the routes having this `local-pref` the ones with the shortest AS-Path.

The `local-pref` attribute is often used to prefer some routes over others. This attribute is always present inside `BGP Updates` exchanged over `iBGP sessions, but never present in the messages exchanged over `eBGP sessions`. 

A common utilisation of `local-pref` is to support backup links. Consider the situation depicted in the figure below. `AS1` would like to always use the high bandwidth link to send an receive packets via `AS2` and only use the backup link upon failure of the primary one.

.. figure:: fig/network-fig-122-c.png
   :align: center
   :scale: 70
   
   How to create a backup link with BGP ?

As BGP routers always prefer the routes having the highest `local-pref` attribute, this policy can be implemented by using the following import filter on `R1`::

 import: from  AS2 RA at R1 set localpref=100;
         from  AS2 RB at R1 set localpref=200;
         accept ANY

With this import filter, all the BGP routes learned from `RB` over the high bandwidth links will be preferred over the routes learned over the backup link. If the primary link fails, the corresponding routes are removed from `R1`'s RIB and `R1` will use the route learned from `RA`. `R1` will reuse the routes via `RB` as soon as the `R1-RB` link comes back.

The import filter above modifies the selection of the BGP routes inside `AS1`. Thus, it influences the route followed by the packets forwarded by `AS1`. In addition to using the primary link to send packets, `AS1` would like to receive its packets via the high bandwidth link. For this, `AS2` also needs to set the `local-pref` attribute in its import filter ::

 import: from  AS1 R1 at RA set localpref=100;
         from  AS1 R1 at RB set localpref=200;
         accept AS1

Sometimes, the `local-pref` attribute is used to prefer a `cheap` link compared to a more expensive one. For example, in the network below, `AS1` could wish to send an receive packets mainly via its interdomain link with `AS4`.

.. figure:: fig/network-fig-123-c.png
   :align: center
   :scale: 70
   
   How to prefer a cheap link over an more expensive one ? 

`AS1` can install the following import filter on `R1` to ensure that it always sends packets via `R2` when it has learned a route via `AS2` and via `AS4` ::

 import: from  AS2 RA at R1 set localpref=100;
        from  AS4 R2 at R1 set localpref=200;
        accept ANY


However, this import filter does not influence how `AS3` for example will prefer some routes over others. If the link between `AS3` and `AS2` is less expensive than the link between `AS3` and `AS4`, `AS3` culd send all its packets via `AS2` and `AS1` would receive packets over its expensive link. An important point to remember about `local-pref` is that it can be used to prefer some routes over others to send packets, but it has no influence on the routes followed by received packets.

Another important utilisation of the `local-pref` attribute is to support the `customer->provider` and `shared-cost` peering relationships. From an economic viewpoint, there is an important difference between these three types of peering relationships. A domain usually earns money when it sends packets over a `provider->customer` relationship. On the other hand, it must to pay its provider when it sends packets over a `customer->provider` relationship. Using a `shared-cost` peering to send packets is usually neutral from an economic viewpoint. To take into account these economic issues, domains usually configure the import filters on their routers as follows :

 - insert a high `local-pref` attribute in the routes learned from a customer
 - insert a medium `local-pref` attribute in the routes learned over a shared-cost peering
 - insert a low `local-pref` attribute in the routes learned from a provider

With such an import filter, the routers of a domain will always prefer to reach destinations via their customers whenever such a route exists. Otherwise, they will prefer to use `shared-cost` peering relationships and they will only send packets via their providers when they do not know any alternate route.

Coming back to the organisation of a BGP router shown in figure :ref:`bgprouter`, the part ot be discussed is the BGP decision process. The `BGP Decision Process` is the algorithm used by routers to select the route to be installed in the FIB when there are multiple routes towards the same prefix. The BGP decision process receives a set of candidate routes towards the same prefix and uses seven steps. At each step, some routes are removed from the candidate set and the process stops when the set contains only one route [#fbgpmulti]_ :

 1. Ignore routes with unreachable BGP nexthop
 2. Prefer routes with highest local-pref
 3. Prefer routes with shortest AS-Path
 4. Prefer routes with smallest MED
 5. Prefer routes learned via eBGP over routes learned via iBGP
 6. Prefer routes with closest next-hop 
 7. Tie breaking rules : prefer Routes learned from router with lowest router id


The first step of the BGP decision process ensures that a BGP router will not install in its FIB a route whose nexthop is considered to be unreachable by the intradomain routing protocol. This rule implies that the BGP decision process must be re-run each time the intradomain routing protocol reports a change in the unreachability of a prefix containing one of more BGP nexthops.

The second rule allows each domain to define its routing preferences. The `local-pref` attribute is set by the import filter when a route is first learned over an eBGP session. 

In contrast with intradomain routing protocols, BGP does not contain an explicit metric. This is because in the global Internet it is impossible for all domains to agree on a common metric that meets the requirements of each domain. Despite of this, BGP routers prefer routes having a short AS-Path attribute over routes with a long AS-Path. This step of the BGP decision process is motivated by the fact that we expect a route with a long AS-Path that have a lower quality than a route with a shorter AS-Path. However studies have shown that there was not always a strong correlation between the quality of a route and the length of its AS-Path [HFPMC2002]_. 

.. index:: Hot potato routing

Before explaining the fourth step, let us first describe the fifth and the sixth steps of the BGP decision process. These two steps are used to implement `hot potato` routing. Intuitively, when a domain implements `hot potato routing`, it tries to forward as quickly as possible to other domains packets that are not destined to addresses inside its own domain. 

To understand `hot potato routing`, let us consider the two networks shown in the figure below. `AS2` advertises prefix `1.0.0.0/8` over the `R2-R6` and `R3-R7` peering links. The routers inside `AS1` will learn two routes towards `1.0.0.0/8`: one via `R6-R2` and the second via `R7-R3`.

.. _fig-med:

.. figure:: fig/network-fig-151-c.png
   :align: center
   :scale: 70
   
   Hot and cold potato routing

With the fifth step of the BGP decision process, a router will always prefer to use a route learned over an `eBGP session` compared to a route learned over an `iBGP session`. Thus, router `R6` (resp. `R7`)  will prefer to use the router via router `R2` (resp. `R3`) to reach prefix `1.0.0.0/8`. 

The sixth step of the BGP decision process takes into account the distance, measured as the length of the shortest intradomain path, between a BGP router and the BGP nexthop for routes learned over `iBGP sessions`. This rule is used on router `R8` in the example above. This router has received two routes towards `1.0.0.0/8`:
 
 - `1.0.0.0/8` via `R7` that is at a distance of `1` from `R8` 
 - `1.0.0.0/8` via `R6` that is at a distance of `50` from `R8`

The first route, via `R7` is the one that router `R8` will prefer as this is the route that will minimise the cost of forwarding packets inside `AS1` before sending them to `AS2`.

`Hot potato routing` allows `AS1` to minimise the cost of forwarding a packet towards `AS2`. However, there are situations where this is not desireable. For example, assume that `AS1` and `AS2` are domains with routers on both the East and the West coast of the USA. In these two domains, the high metric associated to links `R6-R8` and `R0-R2` correspond to the cost of forwarding a packet accross the USA. If `AS2` is a customer that pays `AS1`, it would prefer to received the packets destined to `1.0.0.0/8` via the `R2-R6` link instead of the `R7-R3` link. This is the objective of `cold potato routing`.


.. index:: Multi-Exit Discriminator (MED), Cold potato routing


`Cold potato routing` is implemented by using the `Multi-Exit Discriminator (MED)`. This attribute is an optionnal BGP attribute that may be set [#fmed]_ by border routers when advertising a BGP route over an `eBGP session`. The most common utilisation of the MED attribute is to indicate over an `eBGP session` the cost to reach the BGP nexthop for the advertised route. In the example above, router `R2` will send `U(1.0.0.0/8,R2,AS2,MED=1)` while `R3` will send `U(1.0.0.0/8,R3,AS2,MED=98)`. 

Assume that the BGP session `R7-3` is the first to be established. `R7` sends `U(1.0.0.0/8,R3,AS2,MED=98)` to both `R8` and `R6`. At this point, all routers inside `AS1` send the packets towards `1.0.0.0/8` via `R7-R3`. Then, the `R6-R2` BGP session is established and router `R6` receives `U(1.0.0.0/8,R2,AS2,MED=1)`. Router `R6` runs its decision process for destination `1.0.0.0/8` and selects the route via `R2` as its route to reach this prefix. `R6` sends `U(1.0.0.0/8,R2,AS2,MED=1)` to routers `R8` and `R7`. They both run their decision prefer and prefer the route advertised by `R6` as it contains the smallest `MED`. Now, all routers inside `AS1` forward the packets to `1.0.0.0/8` via link `R6-R2` as expected by `AS2`. As router `R7` does not anymore use the BGP route learned via `R3` it must stop advertising it over `iBGP sessions` and sends `W(1.0.0.0/8)` over its `iBGP sessions` with `R6` and `R8`. However, router `R7` still keeps the route learned from `R3` inside its Adj-RIB-In. If the `R6-R2` link fails, `R6` will send `W(1.0.0.0/8)` over its iBGP sessions and router `R7` will respond by sending `U(1.0.0.0/8,R3,AS2,MED=98)` over its iBGP sessions.

In practice, the fifth step of the BGP decision process is slighty more complex because the routes towards a given prefix can be learned from different ASes. For example, assume that in figure :ref:`fig-med`, `1.0.0.0/8` is also advertised by `AS3` (not shown in the figure) that has peering links with routers `R6` and `R8. If `AS3` advertises a route whose MED attribute is set to `2` and another with a MED set to `3`, how should `AS1`'s router compare the four BGP routes towards `1.0.0.0/8` ? Is a MED value of `1` from `AS2` better than a MED value of `2` from `AS3` ?  The fifth step of the BGP decision process solves this problem by only comparing the MED attribute of the routes learned from the same neighbour AS. Additional details about the MED attribute may be found in :rfc:`4451`. It should be noted that using the MED attribute may cause some problems in BGP networks as explained in [GW2002]_

.. index: BGP router-id

The last step of the BGP decision allows to select a single route when a BGP router has received several routes that are considered as equal by the first six steps of the decision process. This can happen for example in a dual-homed stub attached to two different providers. As shown in the figure below, router `R1` will received two equally BGP routes towards `1.0.0.0/8`. To break the ties, each router is identified by a unique `router-id` which in practice is one of the IP addresses assigned to the router. On some routers, the lowest router id step in the BGP decision process is replaced by the selection of the oldest route :rfc:`5004`. Preferring the oldest route when breaking ties is used to prefer stable paths over unstable paths. However, a drawback of this approach is that the selection of the BGP routes will depend on the arrival times of the corresponding messages. This makes the BGP selection process non-deterministic and can lead to problems that are difficult to debug.

.. figure:: fig/network-fig-153-c.png
   :align: center
   :scale: 70
   
   A stub connected to two providers


BGP convergence
...............

Tier-1 ISPs
Dozen of large ISPs interconnected by shared-cost
Provide transit service
Uunet, Level3, OpenTransit, ...
Tier-2 ISPs
Regional or National ISPs 
Customer of T1 ISP(s)
Provider of T3 ISP(s) 
shared-cost with other T2 ISPs
France Telecom, BT, Belgacom
Tier-3 ISPs
Smaller ISPs, Corporate Networks, Content providers
Customers of T2 or T1 ISPs
shared-cost with other T3 ISPs


.. figure:: fig/network-fig-110-c.png
   :align: center
   :scale: 70
   
   The layered structure of the global Internet

[SARK2002]_
[ATLAS2009]_
http://www.caida.org/research/topology/as_core_network/



.. sidebar:: BGP security

   explain Youtube attack and briefly discuss the work in SIDR




.. rubric:: Footnotes

.. [#fclasses] In addition to the A, B and C classes, :rfc:`791` also defined the `D` and `E` classes of IPv4 addresses. Class `D` (resp. `E`) addresses are those whose high order bits are set to `1110` (resp. `1111`). Class `D` addresses are used by IP multicast and will be explained later. Class `E` addresses are currently unused, but there are some discussions on possible future usages [WMH2008]_ [FLM2008]_

.. [#fnetmask] Another way of representing IP subnets is to use netmasks. A netmask is a 32 bits field whose `p` high order bits are set to `1` and the low order bits are set to `0`. The number of high order bits set `1` indicates the length of the subnet identifier. Netmasks are usually represented in the same dotted decimal format as IPv4 addresses. For example `10.0.0.0/8` would be represented as `10.0.0.0 255.0.0.0` while `192.168.1.0/24` would be represented as `192.168.1.0 255.255.255.0`. In some cases, the netmask can be represented in hexadecimal.

.. [#funumbered] A point-to-point link to which no IPv4 address has been allocated is called an unnumbered link. See :rfc:`1812` section 2.2.7 for a discussion of such unnumbered links.

.. [#fprotocolnumber] See http://www.iana.org/assignments/protocol-numbers/ for the list of all assigned `Protocol` numbers

.. [#fttl] The initial IP specification in :rfc:`791` suggested that routers would decrement the `TTL` at least once every second. This would ensure that a packet would never remain for more than `TTL` seconds in the network. However, in practice most router implementations simply chose to decrement the `TTL` by one. 

.. [#finitialttl] The initial TTL value used to send IP packets vary from one implementation to another. Most current IP implementations use an initial TTL of 64 or more. See http://members.cox.net/~ndav1/self_published/TTL_values.html for additional information.

.. [#f6lowpan] Supporting IP over the 802.15.4 datalink layer technology requires special mechanisms. See :rfc:`4944` for a discussion of the special problems posed by 802.15.4

.. [#fpingproblems] Until a few years ago, all hosts replied to `Echo request` ICMP messages. However, due to the security problems that have affected TCP/IP implementations, many of these implementations can now be configured to disable answering `Echo request` ICMP messages. 

.. [#ftraceroutemore] A detailed analysis of traceroute output is outside the scope of this document. Additional information may be found in [ACO+2006]_ and [DT2007]_

.. ping of death http://insecure.org/sploits/ping-o-death.html

.. [#fciscoags] Example routers from this period include the Cisco AGS http://www.knossos.net.nz/don/wn1.html and AGS+ http://www.ciscopress.com/articles/article.asp?p=25296

.. [#fdfflag] A transport protocol implementation can also specify whether the packet must be sent with the `DF` set or set. A TCP implementation using `Path MTU Discovery` would always request the transmission of IPv4 packets with the `DF` flag set.

.. [#fiddf] It should be noted that only the packets that can be fragmented (i.e. whose `DF` flag is reset) must have different `Identification` fields. The `Identification` field is not used in the packets having the `DF` flag set.

.. [#fmultiiana] The full list of allocated IPv6 multicast addresses is available at http://www.iana.org/assignments/ipv6-multicast-addresses

.. [#fianaprotocol] The IANA_ maintains the list of all allocated Next Header types at http://www.iana.org/assignments/protocol-numbers/ The same registry is used for the IPv4 protocol field and for the IPv6 Next Header.

.. [#falert] For a discussion of the issues with the router alert IP option, see http://tools.ietf.org/html/draft-rahman-rtg-router-alert-dangerous-00 or
 http://tools.ietf.org/html/draft-rahman-rtg-router-alert-considerations-03

.. [#fafi] The Address Family Identifiers are maintained by IANA at http://www.iana.org/assignments/address-family-numbers/

.. [#fasnum] An analysis of the evolution of the number of domains on the global Internet during the last ten years may be found in http://www.potaroo.net/tools/asn32/

.. [#fasrank] See http://as-rank.caida.org/ to analysis of the interconnections between domains based on measurements collected in the global Internet

.. [#fripedb] See ftp://ftp.ripe.net/ripe/dbase for the RIPE database that contains the import and export policies of many European ISPs

.. [#fasdomain] In this text, we consider Autonomous System and domain as synonyms. In practice, a domain may be  divided into several Autonomous Systems, but we ignore this detail. 

.. [#flifetimebgp] The TCP connections used to support BGP sessions are typically established. They are rarely released, except if the corresponding peering link fails or one of the endpoints crashes or needs to be rebooted. 

.. [#fdefaultkeepalive] The 90 seconds default is the default delay recommended by :rfc:`4271`. However, two BGP peers can negotiate a different timer during the establishment of a BGP session. Using a too small interval to detect BGP session failures is not recommended. BFD [KW2009]_ can be used to replace BGP's KEEPALIVE mechanism if fast detection of interdomain link failures is required.

.. [#fnexthopself] Some routers, when they receive a `BGP Update` over an `eBGP session`, set the nexthop of the received route to one of their own addresses. `This is called `nexthop-self`. See e.g. [WMS2004]_ for additional details.

.. [#frr] Using a full-mesh of iBGP sessions is suitable in small networks. However, this solution does not scale in large networks containing hundreds or more routers since :math:`O(n^2)` iBGP sessions must be established. Large domains use either Route Reflection :rfc:`4456` or confederations :rfc:`5065` to scale their iBGP, but this goes beyond this introduction.

.. [#fbgpmulti] Some BGP implementations can be configured to install several routes towards a single prefix in their FIB for load-balancing purposes. However, this goes beyond this introduction to BGP.

.. [#fmed] The MED attribute can be used on `customer->provider` peering relationships upon request of the customer. On `shared-cost` peering relationship, the MED attribute is only enabled when there is a explicit agreement between the two peers. 

.. include:: ../links.rst
