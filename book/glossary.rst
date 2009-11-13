.. _glossary:
   
Glossary
========

.. glossary::
   :sorted:

   anycast
	a transmission mode where an information is sent from one source to `one` receiver that belongs to a specified group

   unicast
	a transmission mode where an information is sent from one source to one recipient

   multicast
	a transmission mode where an information is sent efficiently to `all` the receivers that belong to a given group


   broadcast
	a transmission mode where is same information is sent to all nodes in the network

   LAN
	Local Area Network

   MAN
	Metropolitan Area Network

   WAN
	Wide Area Network

   
   ISO
	The International Standardization Organisation is an agency of the United Nations that is based in Geneva and develop standards on various topics. Within ISO, country representatives vote to approve or reject standards. Most of the work on the development of ISO standards is done in expert working groups. Additional information about ISO may be obtained from http://www.iso.int 

   ITU
	The International Telecommunication Union is a United Nation's agency whose purpose is to develop standards for the telecommunication industry. It was initially created to standardise the basic telephone system but expanded later towards data networks. The work within ITU is mainly done by network specialists from the telecommunication industry (operators and vendors). See http://www.itu.int for more information

   IETF
	The Internet Engineering Task Force is a non-profit organisation that develops the standards for the protocols used in the Internet. The IETF mainly covers the transport and network layers. Several application layer protocols are also standardised within the IETF. The work in the IETF is organised in working groups. Most of the work is performed by exchanging emails and there are three IETF meetings every year. Participation is open to anyone. See http://www.ietf.org

   W3C
	The world wide web consortium was created to standardise the protocols and mechanisms used in the global www. It is thus focussed on a subset of the application layer. See http://www.w3c.org

   X25
   

   ARPANET	
   	The Advanced Research Project Agency (ARPA) Network is a network that was built by network scientists in USA with funding from the ARPA of the US Ministry of Defense. ARPANET is considered as the grandfather of today's Internet.


   PBL
	Problem-based learning is a teaching approach that relies on problems.

   DNS
        The Domain Name System is a distributed database that allows to map names on IP addresses.
   
   packet
	a packet is the unit of information transfert in the network layer

   SDU (Service Data Unit)	
        a Service Data Unit is the unit information transferred between applications
 
   Internet
	a public internet, i.e. a network composed of different networks that are running :term:`IPv4` or :term:`IPv6`

   internet
	an internet is an internetwork, i.e. a network composed of different networks. The :term:`Internet` is a very popular internetwork, but other internets have beend used in the path.	

   IP
        Internet Protocol is the generic term for the network layer protocol in the TCP/IP protocol suite. :term:`IPv4` is widely used today and :term:`IPv6` is expected to replace :term:`IPv4`

   IPv4
	is the version 4 of the Internet Protocol, the connectionless network layer protocol used in most of the Internet today. IPv4 addresses are encoded as a 32 bits field.

   IPv6
	is the version 6 of the Internet Protocol, the connectionless network layer protocol which is intended to replace :term:`IPv4` . IPv6 addresses are encoded as a 128 bits field.

   TCP
	The Transmission Control Protocol is a protocol of the transport layer in the TCP/IP protocol suite that provides a reliable bytestream connection-oriented service on top of IP

   UDP
	User Datagram Protocol is a protocol of the transport layer in the TCP/IP protocol suite that provides an unreliable connectionless service that includes a mechanism to detect corruption
	
   OSI	
   	Open Systems Interconnection. A set of networking standards developed by :term:`ISO` including the 7 layers OSI reference model.
	
   SNMP
	The Simple Network Management Protocol is a management protocol defined for TCP/IP networks.

   ASN.1
	The Abstract Syntax Notation One (ASN.1) was designed by ISO and ITU-T. It is a stadard and flexible notation that can be used to describe data structures for representing, encoding, transmitting, and decoding data between applications. It was designed to be used in the Presentation layer of the OSI reference model but is now used in other protocols such as :term:`SNMP`.

   ftp
	The File Transfert Protocol defined in :rfc:`959` has been the de facto protocol to exchange files over the Internet before the widespread adoption of :rfc:`http`

   ISN
	The Initial Sequence Number of a TCP connection is the sequence number chosen by the client ( resp. server) that is placed in the `SYN` (resp. `SYN+ACK`) segment during the establishment of the TCP connection.

   spoofed packet
   	A packet is said to be spoofed when the sender of the packet has used as source address a different address than its own.

   SYN cookie
        The SYN cookies is a technique used to compute the ISN_ 

   TCB
	The Transmission Control Block is the set of variables that are maintained for each established TCP connection by a TCP implementation. 

   socket
	A low-level API originally defined on Berkeley Unix to allow programmers to develop clients and servers. 

   MSS
	A TCP option used by a TCP entity in SYN segments to indicate the Maximum Segment Size that it is able to receive.

   round-trip-time
	The round-trip-time (RTT) is the delay between the transmission of a segment and the reception of the corresponding acknowledgement in a transport protocol.

   CIDR
	Classless InterDomain Routing is the current address allocation architecture for IPv4. It was defined in :rfc:`1518` and :rfc:`4632`. 

   RIR
	Regional Internet Registry. An organisation that manages IP addresses and AS numbers on behalf of IANA.

   RIP
	Routing Information Protocol. An intradomain routing protocol based on distance vectors that is sometimes used in entreprise networks. RIP is defined in :rfc:`2453`.

   OSPF
	Open Shortest Path First. A link-state intradomain routing protocol that  is often used in entreprise and ISP networks. OSPF is defined in and :rfc:`2328`  and :rfc:`5340`
 
   IS-IS
	Intermediate System- Intermediate System. A link-state intradomain routing that was initially defined for the ISO CLNP protocol but was extended to support IPv4 and IPv6. IS-IS is often used in ISP networks. It is defined in [ISO10589]_

   IGP
	Interior Gateway Protocol. Synonym of intradomain routing protocol

   EGP
	Exterior Gateway Protocol. Synonym of interdomain routing protocol

   IXP
	Internet eXchange Point. A location where routers belonging to different domains are attached to the same Local Area Network to establish peering sessions and exchange packets. See http://www.euro-ix.net/ or http://en.wikipedia.org/wiki/List_of_Internet_exchange_points_by_size for a partial list of IXPs.

   BGP
	The Border Gateway Protocol is the interdomain routing protocol used in the global Internet.

   EIGRP

	The Enhanced Interior Gateway Routing Protocol (EIGRP) is prorietary intradomain routing protocol that is often used in entreprise networks. EIGRP uses the DUAL algorithm described in [Garcia1993]_.


   IGRP	
   	The Interior Gateway Routing Protocol (IGRP) is a proprietary intradomain routing protocol that uses distance vector. IGRP supports multiple metrics for each route but has been replaced by :term:`EIGRP`

   NAT
	A Network Address Translator is a middlebox that translates IP packets.

   `iBGP session`

   	A BGP session between two routers belonging to the same Autonomous System. Also called an internal BGP session.

   `eBGP session`
   	
	A BGP session between two directly connected routers that belong to two different Autonomous Systems. Also called an external BGP session.

   
	
