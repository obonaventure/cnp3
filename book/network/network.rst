================== 
The network layer
==================

.. :rfc:`3927` special addresses

.. http://tools.ietf.org/html/draft-touch-intarea-ipv4-unique-id-01 comment choisir les IP ids

Principles 
###########


.. figure:: fig/network-fig-001-c.png
   :align: center
   
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

Virtual circuit mode
=====================

more flexible routes than datagram mode

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


Link state routing
------------------

more complex, explain first discovery, then reliable flooding
and using dijkstra for shortest path computation

Internet Protocol
#################


The Internet Protocol is the network layer protocol of the TCP/IP protocol suite. 

.. figure:: fig/network-fig-051-c.png
   :align: center
   
   IP and the reference model


IP version 4
============



IPv4 addressing architecture
----------------------------

IPv4 addresses are encoded as a 32 bits field. IPv4 addresses are often represented in `dotted-decimal` format as a sequence of four integers separated by a `.`. The first integer is the decimal representation of the most significant byte of the 32 bits IPv4 address, ... For example, 

 * 1.2.3.4 corresponds to 00000001000000100000001100000100
 * 127.0.0.1 corresponds to 01111111000000000000000000000001
 * 255.255.255.255 corresponds to 11111111111111111111111111111111
 
mask

The initial addressing architecture for IPv4 defined 



IPv4 packet forwarding
----------------------

longest match
decrement ttl
update checksum




ip :rfc:`791`

.. figure:: fig/network-fig-064-c.png
   :align: center
   
   The IP version 4 header

IPv4 uses a 20 bytes header that can be optionnally extended by using options. The main fields of the IPv4 header are :

 - a 4 bits `version` that indicates the version of IP used to defined the header. Using a version field in the header allows the protocol to evolve as we'll see with IPv5
 -  a 4 bits `IP Header Length (IHL)` that indicates the length of the IP header in 32 bits words. This field allows IPv4 to use options if required, but as it is encoded as a 4 bits field, the IPv4 header cannot occupy more than 64 bytes. 
 - an 8 bits `DS` field that is used for Quality of Service and whose usage will be described later.
 - a 16 bits `length` that indicates the total length of the entire IPv4 packet (header and payload) in bytes. This implies that an IPv4 packet cannot be longer than 65535 bytes.
 - a 32 bits `source address` field that contains the IPv4 address of the source host
 - a 32 bits `destination address` field that contains the IPv4 address of the destination host 
 - a 16 bits `checksum` that protects only the IPv4 header against transmission errors
 - an 8 bits `Time-to-Live (TTL)` field. Initially, this field was intended to specify the lifetime of the packet, but in practice it indicates the number of hops

pseudocode ipv4 in scapy
decrement p.ttl
if p.ttl==0 send icmp



Fragmentation and reassembly
----------------------------

path mtu discovery :rfc:`1191`

dhcp :rfc:`2131

ICMP version 4
==============

:rfc:`792`

.. figure:: fig/network-fig-069-c.png
   :align: center
   
   ICMP version 4 


Type and Code indicate the type of
error detected
 Destination unreachable
network unreachable
host unreachable
protocol unreachable
port unreachable
fragmentation needed
source route failed
Redirect
Parameter problem
Time exceeded
TTL exceeded
reassembly time exceeded
Echo requEast et Echo reply 

traceroute

ping


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

In IPv6, fragmentation is performed by the source host and relies on the fragmentation header. This 64 bits header is composed of six fields.

 - a `Next Header` field that indicates the type of the header that follows the fragmentation header
 - a `reserved` field set to `0`. 
 - the `Fragment Offset`is a 13-bit unsigned integer that contains the offset, in 8-octet units, of the data following this header, relative to the start of the original packet. 
 - the `More` flag that is set to `0` in the last fragment of a packet and to `1` in all other fragments. 
 - the 32 bits `Identification` field indicates to which original packet a fragment belongs. When a host sends fragmented packets, it should ensure that it does not reuse the same `identification` field for packets sent to the same destination during a period of `MSL` seconds. This is easier with the 32 bits `identification` used in the IPv6 fragmentation header, than with the 16 bits `identification` field of the IPv4 header.

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

.. [#fciscoags] Example routers from this period include the Cisco AGS http://www.knossos.net.nz/don/wn1.html and AGS+ http://www.ciscopress.com/articles/article.asp?p=25296

.. [#fmultiiana] The full list of allocated IPv6 multicast addresses is available at http://www.iana.org/assignments/ipv6-multicast-addresses

.. [#fianaprotocol] The IANA_ maintains the list of all allocated Next Header types at http://www.iana.org/assignments/protocol-numbers/ The same registry is used for the IPv4 protocol field and for the IPv6 Next Header.

.. [#falert] For a discussion of the issues with the router alert IP option, see http://tools.ietf.org/html/draft-rahman-rtg-router-alert-dangerous-00 or
 http://tools.ietf.org/html/draft-rahman-rtg-router-alert-considerations-03

.. include:: ../links.rst
