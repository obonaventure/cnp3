.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. _glossary:
   
Glossary
========

.. glossary::
   :sorted:

   ascii
	The American Standard Code for Information Interchange (ASCII) is a character-encoding scheme that defines a binary representation for characters. The ASCII table contains both printable characters and control characters. ASCII characters were encoded in 7 bits and only contained the characters required to write text in English. Other character sets such as Unicode have been developed later to support all written languages.

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
	The world wide web consortium was created to standardise the protocols and mechanisms used in the global www. It is thus focused on a subset of the application layer. See http://www.w3c.org

   ARPANET	
   	The Advanced Research Project Agency (ARPA) Network is a network that was built by network scientists in USA with funding from the ARPA of the US Ministry of Defense. ARPANET is considered as the grandfather of today's Internet.

   PBL
	Problem-based learning is a teaching approach that relies on problems.

   DNS
        The Domain Name System is a distributed database that allows to map names on IP addresses.
   
   packet
	a packet is the unit of information transfer in the network layer

   segment
	a segment is the unit of information transfer in the transport layer

   frame
	a frame is the unit of information transfer in the datalink layer

   SDU (Service Data Unit)	
        a Service Data Unit is the unit information transferred between applications
 
   Internet
	a public internet, i.e. a network composed of different networks that are running :term:`IPv4` or :term:`IPv6`

   internet
	an internet is an internetwork, i.e. a network composed of different networks. The :term:`Internet` is a very popular internetwork, but other internets have been used in the path.	

   IP
        Internet Protocol is the generic term for the network layer protocol in the TCP/IP protocol suite. :term:`IPv4` is widely used today and :term:`IPv6` is expected to replace :term:`IPv4`

   IPv4
	is the version 4 of the Internet Protocol, the connectionless network layer protocol used in most of the Internet today. IPv4 addresses are encoded as a 32 bits field.

   IPv6
	is the version 6 of the Internet Protocol, the connectionless network layer protocol which is intended to replace :term:`IPv4` . IPv6 addresses are encoded as a 128 bits field.

   TCP/IP
        refers to the :term:`TCP` and :term:`IP` protocols	

   TCP
	The Transmission Control Protocol is a protocol of the transport layer in the TCP/IP protocol suite that provides a reliable bytestream connection-oriented service on top of IP

   UDP
	User Datagram Protocol is a protocol of the transport layer in the TCP/IP protocol suite that provides an unreliable connectionless service that includes a mechanism to detect corruption
	
   OSI	
   	Open Systems Interconnection. A set of networking standards developed by :term:`ISO` including the 7 layers OSI reference model.
	
   SNMP
	The Simple Network Management Protocol is a management protocol defined for TCP/IP networks.

   ASN.1
	The Abstract Syntax Notation One (ASN.1) was designed by ISO and ITU-T. It is a standard and flexible notation that can be used to describe data structures for representing, encoding, transmitting, and decoding data between applications. It was designed to be used in the Presentation layer of the OSI reference model but is now used in other protocols such as :term:`SNMP`.

   ftp
	The File Transfer Protocol defined in :rfc:`959` has been the de facto protocol to exchange files over the Internet before the widespread adoption of HTTP :rfc:`2616`

   ISN
	The Initial Sequence Number of a TCP connection is the sequence number chosen by the client ( resp. server) that is placed in the `SYN` (resp. `SYN+ACK`) segment during the establishment of the TCP connection.

   spoofed packet
   	A packet is said to be spoofed when the sender of the packet has used as source address a different address than its own.

   SYN cookie
        The SYN cookies is a technique used to compute the initial sequence number (ISN)

   TCB
	The Transmission Control Block is the set of variables that are maintained for each established TCP connection by a TCP implementation. 
  
   API
	Application Programming Interface


   socket
	A low-level API originally defined on Berkeley Unix to allow programmers to develop clients and servers. 

   MSS
	A TCP option used by a TCP entity in SYN segments to indicate the Maximum Segment Size that it is able to receive.

   round-trip-time
	The round-trip-time (RTT) is the delay between the transmission of a segment and the reception of the corresponding acknowledgement in a transport protocol.

   CIDR
	Classless Inter Domain Routing is the current address allocation architecture for IPv4. It was defined in :rfc:`1518` and :rfc:`4632`. 

   RIR
	Regional Internet Registry. An organisation that manages IP addresses and AS numbers on behalf of :term:`IANA`.

   RIP
	Routing Information Protocol. An intradomain routing protocol based on distance vectors that is sometimes used in enterprise networks. RIP is defined in :rfc:`2453`.

   OSPF
	Open Shortest Path First. A link-state intradomain routing protocol that  is often used in enterprise and ISP networks. OSPF is defined in and :rfc:`2328`  and :rfc:`5340`
 
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
	The Enhanced Interior Gateway Routing Protocol (EIGRP) is a proprietary intradomain routing protocol that is often used in enterprise networks. EIGRP uses the DUAL algorithm described in [Garcia1993]_.


   IGRP	
   	The Interior Gateway Routing Protocol (IGRP) is a proprietary intradomain routing protocol that uses distance vector. IGRP supports multiple metrics for each route but has been replaced by :term:`EIGRP`

   NAT
	A Network Address Translator is a middlebox that translates IP packets.

   iBGP
   	An iBGP session is a BGP between two routers belonging to the same Autonomous System. Also called an internal BGP session.

   eBGP	
	An eBGP session is a BGP session between two directly connected routers that belong to two different Autonomous Systems. Also called an external BGP session.

   router
	A relay operating in the network layer.

   switch
	A relay operating in the datalink layer.

   hub
	A relay operating in the physical layer.   
	
   AIMD
	Additive Increase, Multiplicative Decrease. A rate adaption algorithm used notably by TCP where a host additively increases its transmission rate when the network is not congested and multiplicatively decreases when congested is detected.

   HTTP
	The HyperText Transport Protocol is defined in :rfc:`2616`

   SMTP
	The Simple Mail Transfer Protocol is defined in :rfc:`821`

   POP
	The Post Office Protocol is defined in :rfc:`1939`

   IMAP
	The Internet Message Access Protocol is defined in :rfc:`3501`

   FTP
	The File Transfer Protocol is defined in :rfc:`959`

   SSH
	The Secure Shell (SSH) Transport Layer Protocol is defined in :rfc:`4253`

   telnet
	The telnet protocol is defined in :rfc:`854`

   X11
	The XWindow system and the associated protocols are defined in [SG1990]_   

   DNS
	The Domain Name System is defined in :rfc:`1035`

   RPC
	Several types of remote procedure calls have been defined. The RPC mechanism defined in :rfc:`5531` is used by applications such as NFS
 
   NFS
	The Network File System is defined in :rfc:`1094`

   NTP
	The Network Time Protocol is defined in :rfc:`1305`
  
   X.25
	A wide area networking technology using virtual circuits that was deployed by telecom operators.

   ATM
	Asynchronous Transfer Mode

   Frame-Relay	     
        A wide area networking 	technology using virtual circuits that is deployed by telecom operators.	     
  
   hosts.txt
	A file that initially contained the list of all Internet hosts with their IPv4 address. As the network grew, this file was replaced by the DNS, but each host still maintains a small hosts.txt file that can be used when DNS is not available.   

   DNS
	The Domain Name System is a distributed database that can be queried by hosts to map names onto IP addresses

   BNF
	 A Backus-Naur Form (BNF) is a formal way to describe a language by using syntactic and lexical rules. BNFs are frequently used to define programming languages, but also to define the messages exchanged between networked applications. :rfc:`5234` explains how a BNF must be written to specify an Internet protocol.

   TLD
	A Top-level domain name. There are two types of TLDs. The ccTLD are the TLD that correspond to a two letters :term:`ISO-3166` country code. The gTLD are the generic TLDs that are not assigned to a country.

   ICANN
	The Internet Corporation for Assigned Names and Numbers (ICANN) coordinates the allocation of domain names, IP addresses and AS numbers as well protocol parameters. It also coordinates the operation and the evolution of the DNS root name servers. 

   root nameserver
   	A name server that is responsible for the root of the domain names hierarchy. There are currently a dozen root nameservers and each DNS resolver See http://www.root-servers.org/ for more information about the operation of these root servers.		  
	
   resolver
	A server that implements the DNS protocol and can resolve queries. A resolver usually serves a set of clients (e.g. all hosts in campus or all clients of a given ISP). It sends DNS queries to nameservers everywhere on behalf of its clients and stores the received answers in its cache. A resolver must know the IP addresses of the root nameservers.

   nameserver
	A server that implements the DNS protocol and can answer queries for names inside its own domain.

   MIME
	The Multipurpose Internet Mail Extensions (MIME) defined in :rfc:`2045` are a set of extensions to the format of email messages that allow to use non-ASCII characters inside mail messages. A MIME message can be composed of several different parts each having a different format.

   POP	
   	The Post Office Protocol (POP), defined :rfc:`1939`, is an application-level protocol that allows a client to download email messages stored on a server. 

   IMAP
	The Internet Message Access Protocol (IMAP), defined in :rfc:`3501`, is an application-level protocol that allows a client to access and manipulate the emails stored on a server. With IMAP, the email messages remain on the server and are not downloaded on the client.
	
   HTML
	The HyperText Markup Language specifies the structure and the syntax of the documents that are exchanged on the world wide web. HTML is maintained by the `HTML working group <http://www.w3.org/html/wg/>`_ of the :term:`W3C` 

   XML
	The eXtensible Markup Language (XML) is a flexible text format derived from SGML. It was originally designed for the electronic publishing industry but is now used by a wide variety of applications that need to exchange structured data. The XML specifications are maintained by `several working groups <http://www.w3.org/XML/>`_ of the :term:`W3C`

   ARP
	The Address Resolution Protocol is a protocol used by IPv4 devices to obtain the datalink layer address that corresponds to an IPv4 address on the local area network. ARP is defined in :rfc:`826`	
 
   ISO
	The International Standardization Organisation

   minicomputer
	A minicomputer is a multi-user system that was typically used in the 1960s/1970s to serve departments. See the corresponding wikipedia article for additional information : http://en.wikipedia.org/wiki/Minicomputer

   MIME document
	A MIME document is a document, encoded by using the :term:`MIME` format.

   modem
	A modem (modulator-demodulator) is a device that encodes (resp. decodes) digital information by modulating (resp. demodulating) an analog signal. Modems are frequently used to transmit digital information over telephone lines and radio links. See http://en.wikipedia.org/wiki/Modem for a survey of various types of modems

   dial-up line
   	A synonym for a regular telephone line, i.e. a line that can be used to dial any telephone number.

   leased line
        A telephone line that is permanently available between two endpoints. 

   ISO-3166
	An :term:`ISO` standard that defines codes to represent countries and their subdivisions. See http://www.iso.org/iso/country_codes.htm    
	
   IANA
	The Internet Assigned Numbers Authority (IANA) is responsible for the coordination of the DNS Root, IP addressing, and other Internet protocol resources
	
   vnc
	A networked application that allows to remotely access a computer's Graphical User Interface. See http://en.wikipedia.org/wiki/Virtual_Network_Computing

   ISP
        An Internet Service Provider, i.e. a network that provides Internet access to its clients. 

   network-byte order
        Internet protocol allow to transport sequences of bytes. These sequences of bytes are sufficient to carry ASCII characters. The network-byte order refers to the Big-Endian encoding for 16 and 32 bits integer. See http://en.wikipedia.org/wiki/Endianness
 
   standard query
        For DNS servers and resolvers, a standard query is a query for a `A` or a `AAAA` record. Such a query typically returns an IP address. 

   inverse query
        For DNS servers and resolvers, an inverse query is a query for the domain name that corresponds to a given IP address. 

   TLS
	Transport Layer Security, defined in :rfc:`5246` is a cryptographic protocol that is used to provide communication security for Internet applications. This protocol is used on top of the transport service but a detailed description is outside the scope of this book.

   NBMA
	A Non Broadcast Mode Multiple Access Network is a subnetwork that supports multiple hosts/routers but does not provide an efficient way of sending broadcast frames to all devices attached to the subnetwork. ATM subnetworks are an example of NBMA networks.
