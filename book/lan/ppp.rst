.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

.. index:: Point-to-Point Protocol, PPP

The Point-to-Point Protocol
===========================

Many point-to-point datalink layers [#flapb]_ have been developed starting in the 1960s [McFadyen1976]_. In this section, we focus on the protocols that are often used to transport IP packets between hosts or routers that are directly connected by a point-to-point link. This link can be a dedicated physical cable, a leased line through the telephone network or a dial-up connection with modems on the two communicating hosts.

.. index:: Serial Line IP

The first solution to transport IP packets over a serial line was proposed in :rfc:`1055` and is know as `Serial Line IP` (SLIP). SLIP is a simple character stuffing technique applied to IP packets. SLIP defines two special characters : `END` (decimal 192) and `ESC` (decimal 219). `END` appears at the beginning and at the end of each transmitted IP packet and the sender adds `ESC` before each `END` character inside each transmitted IP packet. SLIP only supports the transmission of IP packets and it assumes that the two communicating hosts/routers have been manually configured with each other's IP address. SLIP was mainly used over links offering bandwidth of often less than 20 Kbps.  On such a low bandwidth link, sending 20 bytes of IP header followed by 20 bytes of TCP header for each TCP segment takes a lot of time. This initiated the development of a family of compression techniques to efficiently compress the TCP/IP headers. The first header compression technique proposed in :rfc:`1144` was designed to exploit the redundancy between several consecutive segments that belong to the same TCP connection. In all these segments, the IP addresses and port numbers are always the same. Furthermore, fields such as the sequence and acknowledgement numbers do not change in a random way. :rfc:`1144` defined simple techniques to reduce the redundancy found in successive segments. The development of header compression techniques continued and there are still improvements being developed nowadays :rfc:`5795`.

While SLIP was implemented and used in some environments, it had several limitations discussed in :rfc:`1055`. The `Point-to-Point Protocol` (PPP) was designed shortly after and is specified in :rfc:`1548`. PPP aims at supporting IP and other network layer protocols over various types of serial lines. PPP is in fact a family of three protocols that are used together :
 
 #. The `Point-to-Point Protocol` defines the framing technique to transport network layer packets.
 #. The `Link Control Protocol` that is used to negotiate options and authenticate the session byusing username and password or other types of credentials
 #. The `Network Control Protocol` that is specific for each network layer protocol. It is used to negotiate options that are specific for each protocol. For example, IPv4's NCP :rfc:`1548` can negotiate the IPv4 address to be used, the IPv4 address of the DNS resolver, ... IPv6's NCP is defined in :rfc:`5072`.

The PPP framing :rfc:`1662` was inspired from the datalink layer protocols standardised by ITU-T and ISO. A typical PPP frame is composed of the fields shown in the figure below. A PPP frame starts with a one byte flag containing `01111110`. PPP can use bit stuffing or character stuffing depending on the environment where the protocol is used. The address and control fields are present for backward compatibility reasons. The 16 bits Protocol field contains the identifier [#fpppid]_ of the network layer protocol that is carried in the PPP frame. `0x002d` is used for an IPv4 packet compressed with :rfc:`1144` while `0x002f` is used for an uncompressed IPv4 packet. `0xc021` is used by the Link Control Protocol, `0xc023` is used by the Password Authentication Protocol (PAP). `0x0057` is used for IPv6 packets. PPP supports variable length packets, but LCP can negotiate a maximum packet length. The PPP frame ends with a Frame Check Sequence. The default is a 16 bits CRC, but some implementations can negotiate a 32 bits CRC. The frame ends with the `01111110` flag.

::
  
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |   Flag	   | Address       |    Control    | Protocol      | 
   |   01111110    | 11111111      |    0000011    |               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Protocol     |						   |
   |		   |                                               |
   +-+-+-+-+-+-+-+-+		Network layer Packet		   |	
   |					      			   |
   ~								   ~
   |								   |
   +               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |	           |  Frame Check  Sequence        |	Flag	   |
   |               |         16 bits               |    01111110   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   PPP frame format

.. index:: Extensible Authentication Protocol, EAP

PPP played a key role in allowing Internet Service Providers to provide dial-up access over modems in the late 1990s and early 2000s. ISPs operated modem banks connected to the telephone network. For these ISPs, a key issue was to authenticate each user connected through the telephone network. This authentication was performed by using the `Extensible Authentication Protocol` (EAP) defined in :rfc:`3748`. EAP is a simple but extensible protocol that was initially used by access routers to authentication the users connected through dialup lines. Several authentication methods, starting from the simple username/password pairs to more complex schemes have been defined and implemented. When ISPs started to upgrade their physical infrastructure to provide Internet access over `Assymetric Digitial Subscriber Lines` (ADSL), they tried to reuse their existing authentication (and billing) systems. To meet these requirements, the IETF developed specifications to allow PPP frames to be transported over over networks than the point-to-point links for which PPP was designed. Nowadays, most ADSL deployments use PPP over either ATM :rfc:`2364` or Ethernet :rfc:`2516`. 


.. [#flapb] `LAPB <http://en.wikipedia.org/wiki/LAPB>`_ and `HDLC <http://en.wikipedia.org/wiki/HDLC>`_ were widely used datalink layer protocols. 

.. [#fpppid] The IANA maintains the registry of all assigned PPP protocol fields at : http://www.iana.org/assignments/ppp-numbers
