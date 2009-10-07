===================
The transport layer
===================

The application layer 
The transport layer contains essential protocols

.. Figure:: fig/transport-fig-001-c.png
   :align: center
   :scale: 50 

   The transport layer in the reference model


As the transport layer is built on top of the network layer, it is important to remember the key features of the network layer service. There are two types of network layer services : connectionless and connection-oriented. The connectionless network layer service is the most widespread. Its main characteristics are :

 - the connectionless network layer service can only support SDUs of *limited size* [#fsize]_
 - the connectionless network layer service may discard SDUs
 - the connectionless network layer service may corrupt SDUs
 - the connectionless network later service may delay, reorder or even duplicate SDUs

These imperfections of the connectionless network layer service will be better understood once we have explained the network layer in the next chapter. At this point, let us simply assume that these imperfections occur without trying to understand why they occur.

Some transport protocols have been developed on top of a connection-oriented network service, such as class 0 of the ISO Transport Protocol (TP0) defined in [X224]_ , but they have not been widely used. We do not discuss such utilisation of a connection-oriented network service in more details in this book.

This chapter is organised as follows. We first explain how it is possible to provide a reliable transport service on top of an unreliable connectionless network service. For this, we build step by step a simple protocol that provides a reliable data transfert and explain the main mechanisms found in such protocols. Then, we study in details the two transport protocols that are used in the Internet. We start from the User Datagram Protocol (UDP) that provides a simple connectionless transport service. Then, we describe the Transmission Control Protocol in details, including its congestion control mechanism.

Principles of a reliable transport protocol
###########################################

In this section, we will design a reliable transport protocol running above a connectionless network layer service. For this, we will first assume that the network layer provides a perfect service, i.e. :

 - the connectionless network layer service never corrupts SDUs
 - the connectionless network layer service never discards SDUs
 - the connectionless network later service never delays, reorders nor duplicate SDUs
 - the connectionless network layer service can support SDUs of *any size*


We will remove these assumptions one after the other in order to better understand the mechanism that inside the transport layer is used to solve each imperfection.

Reliable data transfert on top of a perfect network service
===========================================================

The transport layer entity that we will design will interact with a user in the application layer and also with an entity in the network layer. According to the reference model, these interactions will be performed by using `DATA.req`and DATA.ind` primitives. However, to simplify the presentation and avoid a confusion between a `DATA.req` primitive issued by the user of the transport layer entity and a `DATA.req` issued by the transport layer entity itself, we will use the following terminology :

 - the interactions between the user and the transport layer entity are represented by using the `DATA.req`, `DATA.ind`, ... primitives
 - the interactions between the transport layer entity and the network layer service are represented by using `send` instead of `DATA.req` and `recvd` instead of `DATA.ind` 

This is illustrated in the figure below.

.. figure:: fig/transport-fig-007-c.png
   :align: center

   Interactions between the transport layer and its user and its network layer provider


When running on top of a perfect connectionless network, a transport level entity can simply issue a `send(SDU)` upon arrival of `DATA.req(SDU)`. Similarly, the receiver will issue a `DATA.ind(SDU)` upon reception of a `recvd(SDU)`. Such a simple protocol works when a single SDU is sent. However, consider the case of a client that sends tens of SDUs to a server. If the server is faster that the client, it will be able to receive and process all the segments sent by the client and deliver their content to its user. 

.. figure:: fig/transport-fig-004-c.png
   :align: center

   The simplest transport protocol

However, if the server is slower than the client, problems could arise. If the network layer on the server needs to deliver segments to the transport entity above it faster than the rate at which the transport entity can process them, a queue will build. A similar queue would build if the application above the transport layer does not process the received SDUs quickly enough. These queues have a limited size [#fqueuesize]_ and if they overflow, the corresponding entity will have to discard information that it has received.

.. sidebar:: Scapy as a newtork prototyping tools

   Throughout this section, we use scapy_  as a prototyping tool to build a reliable transport protocol. scapy_ is a packet manipulation tool that was written and is maintained by Philippe Biondi and many others. scapy_ is written in python_ and allows to easily create, manipulate and process many types of network packets. scapy_ can also be easily extended to support new protocols and allows to easily specify the complete finite state machine that implements a protocol. Additional information about scapy are available at : http://www.secdev.org/projects/scapy/

.. Other possibilities : libpcap, libdnet, click

To solve this problem, we need to introduce inside our transport protocol, and despite the fact that the network layer provides a perfect service, a feedback mechanism that allows the receiver to inform the sender that it has processed a segment and that another one can be sent. For this, our transport protocol must support two types of segments :

 - data segments carrying a SDU
 - control segment carrying an acknowledgment that indicate that the previous segment was processed correctly

These two types of segments can be distinguished by using a segment composed of two parts :

 - a `header` that contains one bit so to `0` in data segments and to `1` in control segments
 - the payload containing the SDU supplied by the user application

In the scapy_ framework, this segment format can be expressed as follows ::

 class P1(Packet):
    name = "Protocol1"
    fields_desc=[BitEnumField("type" , 2, {0:"Data", 1:"OK"}, ]
    
    def post_build(self, segment, SDU):
        segment += SDU
        return segment

This scapy code defines a protocol with a header containing one bit. The bit is set to 0 in a data segment and 1 in an OK segment. The `post_build` method is used to indicate how the SDU should be added to build the complete segment.

The transport entity can then be modelled as a finite state machine containing two states for the receiver and two states for the sender. The figure below provides a graphical representation of this state machine with the sender above and the receiver below.

.. figure:: fig/transport-fig-008-c.png
   :align: center


A time-sequence diagramme showing 

.. figure:: fig/transport-fig-009-c.png
   :align: center


The receiver side of this protocol can be expressed by the following python code as a scapy automaton ::

 class P1Sender(Automaton):
	def parse_args(self, sender, **kargs):
		Automaton.parse_args(self, **kargs)
		self.sender = sender
		self.info = "CTRL"

	def master_filter(self, pkt):
        	return (IP in pkt and pkt[IP].src == self.sender and P1 in pkt)

	@ATMT.state(initial=True)
	def WAIT_DATA0 (self):
		print "State: WAIT_DATA0"
		pass
		
	@ATMT.state()
	def WAIT_DATA1 (self):
		print "State: WAIT_DATA1"
		pass
		

	@ATMT.receive_condition(WAIT_FOR_OK)
	def wait_data0 (self, pkt):
		flag = pkt.getlayer(ABP).flags
		payload = pkt.getlayer(ABP).payload.load
		if flag == 0:
			print "data received [[",payload,"]]"
			packet = IP(dst=self.sender)/ABP(flags="ok0")/self.info
			self.send(packet)
			raise self.WAIT_DATA1()
		if flag == 1:
			packet = IP(dst=self.sender)/ABP(flags="ok1")/self.info
			self.send(packet)
			raise self.WAIT_DATA0()
	
	@ATMT.receive_condition(WAIT_DATA1)
	def wait_data1 (self, pkt):
		flag = pkt.getlayer(ABP).flags
		payload = pkt.getlayer(ABP).payload.load
		if flag == 1:
			print "data received [[",payload,"]]"
			packet = IP(dst=self.sender)/ABP(flags="ok1")/self.info
			self.send(packet)
			raise self.WAIT_DATA0()
		if flag == 0:
			packet = IP(dst=self.sender)/ABP(flags="ok0")/self.info
			self.send(packet)
			raise self.WAIT_DATA1()
			


The sender side of this protocol can be expressed by the following python code as a scapy automaton ::

 class P1(Automaton):
	def parse_args(self, payloads, receiver,**kargs):
        	Automaton.parse_args(self, **kargs)
        	self.receiver = receiver
       		self.q = Queue.Queue()
		for item in payloads:
			self.q.put(item)
    
	def master_filter(self, pkt):
        	return (IP in pkt and pkt[IP].src == self.receiver and ABP in pkt)
		
	@ATMT.state(initial=1)
	def WAIT_DATA_REQ0 (self):
		print "State: WAIT_DATA_REQ0"
		pass
	
	@ATMT.condition(WAIT_DATA_REQ0)
	def wait_for_data0(self):
		try:
			self.payload = self.q.get(timeout=TIMEOUT)
			print "data to be transmitted [[",self.payload,"]]"
			raise self.WAIT_FOR_OK0_OR_NAK()
		except Queue.Empty:
			sys.exit(0)
	
	@ATMT.action(wait_for_data0)
	def send_data0(self):
		print "Transition: WAIT_DATA_REQ0 --> WAIT_FOR_OK0_OR_NAK / Sending data0 (Data Request)"
		self.last_packet = IP(dst=self.receiver)/ABP(flags="data0")/self.payload
		self.send(self.last_packet)
	
	@ATMT.state()
	def WAIT_DATA_REQ1 (self):
		print "State: WAIT_DATA_REQ1"
	
	@ATMT.condition(WAIT_DATA_REQ1)
	def wait_for_data1(self):
		try:
			self.payload = self.q.get(timeout=TIMEOUT)
			print "data to be transmitted [[",self.payload,"]]"
			raise self.WAIT_FOR_OK1_OR_NAK()
		except Queue.Empty:
			sys.exit(0)
	
	@ATMT.action(wait_for_data1)
	def send_data1(self):
		print "Transition: WAIT_DATA_REQ1 --> WAIT_FOR_OK1_OR_NAK / Sending data1 (Data Request)"
		self.last_packet = IP(dst=self.receiver)/ABP(flags="data1")/self.payload
		self.send(self.last_packet)
	
	@ATMT.state()
	def WAIT_FOR_OK0_OR_NAK(self):
		print "State: WAIT_FOR_OK0_OR_NAK"
	
	@ATMT.state()
	def WAIT_FOR_OK1_OR_NAK(self):
		print "State: WAIT_FOR_OK1_OR_NAK"
	
	@ATMT.timeout(WAIT_FOR_OK0_OR_NAK, TIMEOUT)
	def timeout_waiting_for_ok0(self):
		raise self.WAIT_FOR_OK0_OR_NAK()
	
	@ATMT.action(timeout_waiting_for_ok0)
	def retransmit_data0(self):
		print "Transition: WAIT_FOR_OK0_OR_NAK --> WAIT_FOR_OK0_OR_NAK / Re-sending data0 (Timeout)"
		self.send(self.last_packet)
	
	@ATMT.timeout(WAIT_FOR_OK1_OR_NAK, TIMEOUT)
	def timeout_waiting_for_ok1(self):
		raise self.WAIT_FOR_OK1_OR_NAK()
	
	@ATMT.action(timeout_waiting_for_ok1)
	def retransmit_data1(self):
		print "Transition: WAIT_FOR_OK1_OR_NAK --> WAIT_FOR_OK1_OR_NAK / Re-sending data1 (Timeout)"
		self.send(self.last_packet)
	
	@ATMT.receive_condition(WAIT_FOR_OK0_OR_NAK)
	def receive_data0(self, pkt):
		flag = pkt.getlayer(ABP).flags
		if flag == 4:
			print "Transition: WAIT_FOR_OK0_OR_NAK --> WAIT_FOR_OK0_OR_NAK / Re-sending data0 (Received nak)"
			self.send(self.last_packet)
			raise self.WAIT_FOR_OK0_OR_NAK()
		if flag == 3:
			print "Transition: WAIT_FOR_OK0_OR_NAK --> WAIT_FOR_OK0_OR_NAK / Re-sending data0 (Received ok1)"
			self.send(self.last_packet)
			raise self.WAIT_FOR_OK0_OR_NAK()
		if flag == 2:
			print "data [[",self.payload,"]] transmitted!"
			print "Transition: WAIT_FOR_OK0_OR_NAK --> WAIT_DATA_REQ1 / Received ok0"
			raise self.WAIT_DATA_REQ1()
	
	@ATMT.receive_condition(WAIT_FOR_OK1_OR_NAK)
	def receive_data1(self, pkt):
		flag = pkt.getlayer(ABP).flags
		if flag == 4:
			print "Transition: WAIT_FOR_OK1_OR_NAK --> WAIT_FOR_OK1_OR_NAK / Re-sending data0 (Received nak)"
			self.send(self.last_packet)
			raise self.WAIT_FOR_OK1_OR_NAK()
		if flag == 2:
			print "Transition: WAIT_FOR_OK1_OR_NAK --> WAIT_FOR_OK1_OR_NAK / Re-sending data0 (Received ok0)"
			self.send(self.last_packet)
			raise self.WAIT_FOR_OK1_OR_NAK()
		if flag == 3:
			print "data [[",self.payload,"]] transmitted!"	
			print "Transition: WAIT_FOR_OK1_OR_NAK --> WAIT_DATA_REQ0 / Received ok1"
			raise self.WAIT_DATA_REQ0()




Reliable data transfert on top of an imperfect network service
==============================================================


Let us first consider a connectionless network service that may corrupt SDUs. Different types of corruption are possible :

 - the size of the SDU may increase or decrease
 - the value some of the bits of the SDU may change

.. sidebar:: Random errors versus malicious modifications

   The protocols of the transport layer are designed to recover from the random errors and losses that may occur in the underlying layers. These random
   see [SPMR09]_ for how to recompute a CRC

In this case, we need a mechanism that allows the receiver of a segment to verify that the SDU contained in

.. index:: Internet checksum

Implementation of the Internet checksum defined in :rfc:`1071` in C ::

 u_short cksum (u_short *buf, int count)
 {
   u_long sum=0;
   while (count--)
   {
     sum = sum + *buf++;
     if(sum & 0xFFFF0000)
     { /* carry, wrap around */
       sum = sum & 0xFFFF;
       sum++;
      }
    }
    return ~(sum & 0xFFFF);
  }




.. sidebar:: The checksum zoo 

   Most of the protocols in the TCP/IP protocol suite rely on the simple Internet checksum to verify that the received segment has not been affected by transmission errors. Despite its popularity and ease of implementation, the Internet checksum is not the only available checksum mechanism. The Cyclical Redundancy Checks (CRC_) are very powerful error detection schemes that are used notably on disks, by many datalink layer protocols and file formats such as zip or png. They can be easily implemented efficiently in hardware and have better error-detection capabilities that Internet checksum [SGP98]_ . However, when the first transport protocols were designed the CRCs were considered to be too complex to implement in software and other checksum mechanisms were chosen. The TCP/IP community chose the Internet checksum, the OSI community chose the Fletcher checksum [Sklower89]_ . There are now efficient techniques to quickly compute CRCs in software [Feldmeier95]_ . The SCTP protocol initially chose the Adler-32 checksum and replaced it with a CRC (see :rfc:`3309`).

.. CRC, checksum, fletcher, crc-32, Internet checksum
.. real checksum http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.55.8520
.. do not invent your own checksum, use existing ones
.. implementations can be optimised by using table lookups
.. crc : http://en.wikipedia.org/wiki/Cyclic_redundancy_check
.. tcp offload engine http://www.10gea.org/tcp-ip-offload-engine-toe.htm
.. stcp used Adler-32 but it now uses CRC :rfc:`3309`

.. sidebar:: Trailer versus header

   When a segment format is designed for a transport protocol, it can be composed of three parts : a header, a payload and a trailer. The header is typically used to place most of the control information. However, the checksum/CRC may be placed either inside the header or inside the trailer.

   - when the checksum/CRC is placed in the trailer, the sender can use hardware assistance on the interface card to compute the checksum/CRC while the segment is being sent. This is an optimisation that is now found on some high speed interfaces
   - when the checksum/CRC is placed in the header, this implies, as segments are sent on the wire one byte after the other starting from the trailer, that the checksum/CRC must be computed before transmitting the segment. It is still possible to use hardware assistance to compute the CRC/checksum, but this is slightly more complex than when the checksum/CRC is placed inside a trailer. 

.. sidebar:: Checksum versus hash functions

   Checksums and CRCs should not be confused with hash functions such as MD5 defined in :rfc:`1321` or `SHA-1 <http://www.itl.nist.gov/fipspubs/fip180-1.htm>`_ .


.. index:: UDP
.. _UDP:

The User Datagram Protocol
##########################


The User Datagram Protocol (UDP) was defined in :rfc:`768`. It provides an unreliable connectionless transport service on top of the unreliable network layer connectionless service. The main characteristics of the UDP service are :

 - the UDP service cannot deliver SDUs that are larger than 65507 bytes [#fmtuudp]_ 
 - the UDP service does not guarantee the delivery of SDUs (losses and desquencing can occur)
 - the UDP service will not deliver a corrupted SDU to the destination

Compared to the connectionless network layer service, the main advantage of the UDP service is that it allows several applications running on a host to exchange SDUs with several other applications running on remote hosts. Consider two hosts, e.g. a client and a server. The network layer service allows the client to send information to the server, but if an application running on the client wants to contact a particular application running on the server, then an additional addressing mechanism is required besides the IP address that identifies a host to identify an application running on a host. This additional addressing is provided by the port numbers. When a server using UDP is enabled on a host, this server requests a port number. This port number will be used by the clients to contact the server process via UDP. 

The figure below shows a typical usage of the UDP port numbers. The client process uses port number `1234` while the server process uses port number `5678`. When the client sends a request, it is identified as originating from port number `1234` on the client host and destined to port number `5678` on the server host. When the server process replies to this request, the server's UDP implementation will send the reply as orginiating from port  `5678` on the server host and destined to port `1234` on the client host.

.. figure:: fig/transport-fig-056-c.png
   :align: center

   Usage of the UDP port numbers

.. index:: UDP segment

The UDP protocol uses a single segment format shown below. The UDP header contains four fiels :

 - a 16 bits source port
 - a 16 bits destination port
 - a 16 bits length field
 - a 16 bits checksum


.. figure:: fig/transport-fig-055-c.png
   :align: center

   The UDP segment format

As the port numbers are encoded as 16 bits field, there can be only up to 65635 different server processes that are listeing to a different UDP port at the same time on a given server. In practice, this limit is never reached. However, it is worth to note that most implementations divide the range of allowed UDP port numbers in three different ranges :

 - the priviledged port numbers (1 < port < 1024 )
 - the ephemeral port numbers ( officially [#fephemeral]_ 49152 <= port <= 65535 )
 - the registered port numbers (officially 1024 <= port < 49152)

In most Unix variants, only processes having system administrator priviledges can be bound to port numbers smaller than `1024`. Well-known servers such as DNS_, NTP_ or RPC_ use priviledged port numbers. When a client needs to use UDP, it usually does not require a specific port number. In this case, the UDP implementation will allocate the first available port number in the ephemeral range. The registered port numbers range should be used by servers. In theory, developers of network servers should register their port number officially through IANA, but few developpers do this. 

.. mention inetd and super servers somewhere ?

.. index:: UDP Checksum, Checksum computation

.. sidebar:: Computation of the UDP checksum

   The checksum of the UDP segment is computed over :

       - a pseudo header containing the source IP address, the destination IP address and a 32 bits bit field containing a the most significant byte set to 0, the second set to 17 and the length of the UDP segment in the lower two bytes
       - the entire UDP segment, including its header

       This pseudo-header allows the receiver to detect errors that affect the IP source or destination addresses that are placed in the IP layer below. This is a violation of the layer principle that dates from the time when UDP and IP were elements of a single protocol. It should be noted that if the checksum algorithm computes value '0x0000', then value '0xffff' is transmitted. A UDP segment whose checksum is set to '0x0000' is a segment for which the transmitter did not compute a checksum upon transmission. Some NFS_ servers chose to disable UDP checksums for performance reasons, but this caused `problems <http://lynnesblog.telemuse.net/192>`_ that were difficult to diagnose. In practice, there are rarely good reasons to disable UDP checksums.


Several types of applications rely on UDP. As a rule of thumb, UDP is used for applications where delay must be minimised or losses can be recovered by the application itself. A first class of UDP-based applications are applications where the client sends a small request and expects quickly a small answer. The DNS_ is an example of such applications that is often used in the wide area. However, in local area networks, many distributed systems rely on Remote Procedure Call (RPC_) that is often used on top of UDP. In Unix enviroments, the Network File System (NFS_) is built on top of RPC and runs frequently on top of UDP. A second class of UDP-based applications are the interactive computer games that need to exchange frequently small informations such as the player's location or recent actions. Many of these games use UDP to minimise the delay and can recover from losses. A third class of applications are the multimedia applications such as interactive Voice over IP or interactive Video over IP. These interactive applications expect a delay shorter than about 200 milliseconds between the sender and the receiver and can recover from losses inside the application. 

.. index:: TCP
.. _TCP:

The Transmission Control Protocol
#################################


The Transmission Control Protocol (TCP) was initially defined in :rfc:`793`. Several parts of the protocol have been improved since the publication of the original protocol specification. However, the basics of the protocol remain and an implementation that only supports :rfc:`793` should interoperate with today's implementation.

TCP provides a reliable bytestream connection-oriented transport service on top of the unreliable connectionless network service provided by IP_. TCP is used my a large number of applications, including :

 - Email_ (SMTP_, POP_, IMAP_)
 - World wide web ( HTTP_, ...)
 - Most file transfert protocols ( ftp_, peer-to-peer file sharing applications , ...)
 - remote computer access : telnet_, ssh_, X11_, VNC_, 
 - non-interactive multimedia applications : youtube_, skype_

On the global Internet, most of the applications used in the wide area rely on TCP. Many studies [#ftcpusage]_ have reported that TCP was responsible for more than 90% of the data exchanged in the global Internet.

.. index:: TCP header
 
To provide this service, TCP relies on a simple segment format. Each TCP segment contains a twenty bytes header described below and optionnaly a payload.

.. figure:: fig/transport-fig-058-c.png
   :align: center

   TCP segment format 

A TCP header contains contains the following fields :

 - Source and destination ports. The source and destination ports play an important role in TCP as they allow to identify the connection to which a TCP segment belongs. When a client opens a TCP connection, it typically selects an ephemeral TCP port number as its source port and contacts the server by using the server's port number. All the segments that will be sent by the client on this connection will have the same source and destination ports. The server will send segments that contain as source (resp. destination) port the destination (resp. source) port of the segments sent by the client. A TCP connection is always identified by five informations :

   - the IP address of the client
   - the IP address of the server
   - the port chosen by the client
   - the destination port of the server
   - TCP

 - the `sequence number` (32 bits), `acknowledgement number` (32 bits) and `window` (16 bits) fields are used to provide a reliable data transfert by using a window-based protocol. In a TCP bytestream, each byte of the stream consummes one sequence number. Their utilisation will be described in more details in :ref:`TCPData`
 - the `Urgent pointer` is used to indicate that some data should be considered as urgent in a TCP bytestream. However, it is rarely used in practice and will not be described here. Additional details may be found in :rfc:`793`, :rfc:`1122` or [StevensTCP]_
 - the flags field contain a set of bit flags that indicate how a segment should be interpreted by the TCP entity that receives it : 

    - the `SYN` flag is used during connection establishment
    - the `FIN` flag is used during connection release
    - the `RST` is used in case of problems or when an invalid segment has been received
    - when the `ACK` flag is set, it indicates that the `acknowledgment` field contains a valid number. Otherwise, the content of the `acknwoledgment` field must be ignored
    - the `URG` flag is used together with the `Urgent pointer`
    - the `PSH` flag is used as a notification from the sender to indicate to the receiver that it should pass all the data it has received to the receiving process. However, in practice TCP implementations do not allow TCP users to indicate when the `PSH` flag should be set and thus there are few real utilizations of this flag. 

 - the `checksum` field contains the value of the Internet checksum computer over the entire TCP segment and a pseudo-header as with UDP
 - the `Reserved` field is reserved for future utilization and must be set to 0
 - the `TCP Header Length` (THL) or `Data Offset` field is a four bits field that indicates the size of the TCP header in 32 bits words. The maximum size of the TCP header is thus 64 bytes.
 - the `Optional header extension` is used to add optional information in the TCP header. Thanks to this header extension, it is possible to add new fields in the TCP header that were not planned in the original specification. This allowed TCP to evolve since the early eighties. The details of the TCP header extension will be explained in :ref:`TCPOpen` and :ref:`TCPData`.
 
.. figure:: fig/transport-fig-057-c.png
   :align: center

   Utilization of the TCP source and destination ports

The rest of this section is organised as follows. We first explain the establishement and the release of a TCP connection, then we discuss the mechanisms that are used by TCP to provide a reliable bytestream service. We end the section with a discussion of network congestion and explain the mechanisms that TCP uses to avod congestion collapse.

.. Urgent pointer not discussed, rarely used, see http://www.ietf.org/id/draft-ietf-tcpm-urgent-data-00.txt for discussion, defined in :rfc:`793` and updated in :rfc:`1122`


.. _TCPOpen:

TCP connection establishment
============================

.. index:: TCP Connection establishment, TCP SYN, TCP SYN+ACK

A TCP connection is established by using a three-way handshake. The connection establishment phase uses the `sequence number` and `acknowledgment number` and the `SYN` flag. When a TCP connection is established, the two communicating hosts negotiate the initial sequence number used on both directions of the connection. For this, each TCP entity maintains a 32 bits counter that is supposed to be incremented by one at least every 4 microseconds and after each connection establishment [#ftcpclock]_. When a client host wants to open a TCP connection with a server host, it creates a TCP segment with :

 - the `SYN` flag set
 - the `sequence number` set to the current value of the 32 bits counter of the client host's TCP entity

Upon reception of this segment (which is often called a `SYN segment`), the server host will reply with a segment containing :

 - the `SYN` flag set
 - the `sequence number` set to the current value of the 32 bits counter of the client host's TCP entity
 - the `ACK` flag set
 - the `acknowledgment number` set to the `sequence number` of the received `SYN` segment incremented by 1 (:math:`~mod~2^{32}`) [#ftcpinc]_

This segment is often called a `SYN+ACK` segment. The acknowledgment confirms to the client that the server has correctly received the `SYN` segment. The `sequence number` of the `SYN+ACK` is used by the server host to verify that the `client` host receives the segment. Upon reception of the `SYN+ACK` segment, the client host will reply with a segment containing :

 - the `ACK` flag set
 - the `acknowledgment number` set to the `sequence number` of the received `SYN+32` segment incremented by 1 ( :math:`~mod~2^{32}`)

At this point, the TCP connection is open and both the client and the server are allowed to send TCP segments containing data. This is illustrated in the figure below. 

.. figure:: fig/transport-fig-059-c.png
   :align: center

   Establishment of a TCP connection

In the figure above, the connection is considered established by the client once it has received the `SYN+ACK` segment while the server considers the connection to be established upon reception of the `ACK` segment. The first data segment sent by the client (server) will have its `sequence number` set to `x+1` (resp. `y+1`). 

.. index:: TCP Initial Sequence Number

.. sidebar:: Computing TCP's initial sequence number

 In the original TCP specification :rfc:`793`, each TCP entity maintained a clock to compute the initial sequence number (ISN_) placed in the `SYN` and `SYN+ACK` segments. This made the iss predictible and caused a security problem. The typical security problem was the following. Consider a server that trusts a host based on its IP address. For example, the server allows this host to login without giving a password [#frlogin]_. Consider now an attacker who knows this particular configuration and is able to send IP packets having the client's address as source. He can send fake TCP segments to the server, but does not receive the server's answers. If he can predict the `ISN` that will be chosen by the server, he can send a fake `SYN` segment and shortly after the fake `ACK` segment that confirms the reception of the `SYN+ACK` segment sent by the server. Once the TCP connection is open, he can use it to send any command on the server. To counter this attack, current TCP implementations add randomness to the `ISN`. One of the solutions, proposed in :rfc:`1948` is to compute the `ISN` as ::
 
  ISN = M + H(localhost, localport, remotehost, remoteport, secret).

 where `M` is the current value of the TCP clock and `H` a cryptographic hash function. `localhost` and `remotehost` (resp. `localport` and `remoteport` ) are the IP addresses (port numbers) of the local and remote host and `secret` is a random number only known by the server. This method allows the server to use different ISNs for different clients at the same time. `Measurements <http://lcamtuf.coredump.cx/newtcp/>`_ performed with the first implementations of this technique showed that it was difficult to implement it correctly, but today's TCP implementation now generate good ISNs.

 
.. index:: TCP RST

A server could, of course, refuse to open a TCP connection upon reception of a `SYN` segment. This refusal may be due to various reasons. There may be no server process that is listening on the destination port of the `SYN` segment. The server could always refuse connection establishments from this particular client (e.g. due to security reasons) or the server may not have enough resources to accept a new TCP connection now. In this case, the server would reply with a TCP segment having its `RST` flag and containing the `sequence number` of the received `SYN` segment as its `acknowledgment number`. This is illustrated in the figure below. We will discuss the various utilizations of the TCP `RST` flag later (see :ref:`TCPReset`).

.. figure:: fig/transport-fig-061-c.png
   :align: center

   TCP connection establishment rejected by peer


The TCP connection establishment can be described as the four states Finite State Machine shown below. In this FSM, `!X` (resp. `?Y`) indicates the transmission of segment `X` (resp. reception of segment `Y`) during the corresponding transition. `Init` is the initial state. 

.. figure:: fig/transport-fig-063-c.png
   :align: center

   TCP FSM for connection establishment

A client host starts in the `Init` state. It then sends a `SYN` segment and enters the `SYN Sent` state where it waits for a `SYN+ACK` segment, replies with an `ACK` segment and enters the `Established` state where data can be exchanged. On the other hand, a server host starts in the `Init` state. When a server process starts to listen to a destination port, the underlying TCP entity creates a TCP control block and a queue to process incoming `SYN` segments. Upon reception of a `SYN` segment, the server's TCP entity replies with a `SYN+ACK` and enters the `SYN RCVD` state. It remains in this state until it receives an `ACK` segment that acknowledges its `SYN+ACK` segment.

Besides these two paths in the TCP connection establishment FSM, there is a third path that corresponds to the case when both the client and the server send a `SYN` segment to open a TCP connection [#ftcpboth]_. In this case, the client and the server send a `SYN` segment and enter the `SYN Sent` state. Upon reception of the `SYN` segment sent by the other host, they reply by sending a `SYN+ACK` segment and enter the `SYN Rcvd` state. The `SYN+ACK` that will arrive from the other host will allow them to transition to the `Established` state. The figure below shows such a simultaneous establishment of a TCP connection.

.. figure:: fig/transport-fig-062-c.png
   :align: center

   Simultaneous establishment of a TCP connection


.. index:: SYN cookies, Denial of Service

.. sidebar:: Denial of Service attacks

 When a TCP entity opens a TCP connection, it creates a Transmission Control Block (TCB). The TCB contains all the state that is maintained by the TCP entity for each TCP connection. During connection establishment, the TCB contains the local IP address, the remote IP address, the local port number, the remote port number, the current local sequence number, the last sequence number received from the remote entity, ... :rfc:`793` Until the mid 1990s, TCP implementations had a limit on the number of TCP connnections that could be in the `SYN Rcvd` state at a given time. Many implementations set this limit to about 100 TCBs. This limit was 100 TCBs was considered sufficient even for heavily load http servers given the small delay between the reception of a `SYN` segment and the reception of the `ACK` segment that terminates the establishment of the TCP connection. When the limit of 100 TCBs in the `SYN Rcvd` state is reached, the TCP entity discard all received TCP `SYN` segments that do not correspond to an existing TCB. 

 This limit of 100 TCBs in the `SYN Rcvd` state Was chosen to protect the TCP entity from the risk of overloading its memory with too many TCBs in the `SYN Rcvd` state. However, it was also the reason for a new type of the Denial of Service (DoS) attack :rfc:`4987`. A DoS attack is defined as an attack where an attacker can render a resource useless in the network. For example, an attacker may cause a DoS attack on a 2 Mbps link used by a company by sending more than 20 Mpbs of packets through this link. In the case of the TCBs, the DoS attack was more subtle. As a TCP entity discards all received `SYN` segments as soon as it has 100 TCBs in the `SYN Rcvd` state, an attacker simply had to send a few 100s of `SYN` segments every second to a server and never reply to the received `SYN+ACK` segments. To avoid being caught, attackers were of course sending these `SYN` segments with a different address than their own IP address [#fspoofing]_. On most TCP implementations, once a TCB entered the `SYN Rcvd` state, it remained in this state for several seconds, waiting for a retransmission of the initial `SYN` segmet. This attack was later called a `SYN flood` attack and the servers of the ISP named panix were among the firsts to `suffer <http://memex.org/meme2-12.html>`_ from it.

 To avoid the `Syn flood` attacks, recent TCP implementations do not anymore enter the `SYN Rcvd` state upon reception of a `SYN segment`. Instead, they reply directly with a `SYN+ACK` segment and wait until the reception of a valid `ACK`. This implementation trick is only possible if the TCP implementation is able to verify that the received `ACK` segment acknowedges the `SYN+ACK` segment sent earlier without storing the `ISN` of this `SYN+ACK` segment in a TCB. The solution to solve this problem, which is known as `SYN cookies <http://cr.yp.to/syncookies.html>`_ is to compute the 32 bits of the `ISN` as follows :

   - the high order bits contain a the low order bits of a counter that is incremented slowly
   - the low order bits contain a hash value computed over the local and remote IP addresses and ports and a random secret only known to the server
   
 The advantage of the `SYN cookies`_ is that by using them, the server does not need to create a TCB_ upon reception of the `SYN` segment and can still check the returned `ACK` segment by recomputing the `SYN cookie`.


.. sidebar:: Retransmitting the first `SYN` segment

   As IP provides an unreliable connectionless service, the `SYN` and `SYN+ACK` segments sent to open a TCP connection could be lost. Current TCP implementations start a retransmission timer when then send the first `SYN` segment. This timer is often set to a three seconds for the first retransmission and then doubles after each retransmission :rfc:`2988`. TCP implementations also enforce a maximum number of retransmissions for the initial `SYN` segment.  


.. index:: TCP Options

As explained earlier, TCP segments may contain an optional header extension. In the `SYN` and `SYN+ACK` segments, these options are used to negotiate some parameters and the utilisation of extensions to the basic TCP specification. 

.. index:: TCP MSS, Maximum Segment Size, MSS

The first parameter which is negotiated during the establishment of a TCP connection is the Maximum Segment Size (MSS). The MSS is the size of the largest segment that a TCP implementation is able to process. According to :rfc:`879`, all TCP implementations must be able to receive TCP segments containing 536 bytes of payload. However, most TCP implementations are able to process larger segments. Such TCP implementations use the TCP MSS Option in the `SYN`/`SYN+ACK` segment to indicate the largest segment that are able to process. The MSS value indicates the maximum size of the payload of the TCP segments. The client (resp. server) stores in its TCB_ the MSS value announced by the server (resp. the client).

Another utilisation of the TCP options during connection establishment is to enable TCP extensions. For example, consider :rfc:`1323` (that will be discussed in :ref:`TCPReliable`). :rfc:`1323` defines TCP extensions to support timestamps and larger windows. If the client supports :rfc:`1323` it adds a :rfc:`1323` option to its `SYN` segment. If the server understands this :rfc:`1323` option and wishes to use it, it replies with an :rfc:`1323` option in the `SYN+ACK` segment and the extension defined in :rfc:`1323` is used throughout the TCP connection. Otherwise, if the server's `SYN+ACK` does not contain the :rfc:`1323` option, the client is not allowed to use this extension and the corresponding TCP header options throughout the TCP connection. TCP's option mechanism is flexible and it allowed to extend TCP while maintaining compatibility with older implementations.

The TCP options are encoded by using a Type Length Value format where :

 - the first byte indicates the `type` of the option.
 - the second byte indicates the total length of the option (including the first two bytes) in bytes
 - the last bytes are specific for each type of option

:rfc:`793` defines the Maximum Segment Size (MSS) TCP option that must be understood by all TCP implementations. This option (type 2) has a length of 4 bytes and contains a 16 bits word that indicates the MSS supported by the sender of the `SYN` segment. The MSS option can only be used in TCP segments having the `SYN` flag set.

:rfc:`793` also defines two special options that must be supported by all TCP implementations. Since the TCP Header Length field contains the length of the TCP header in 32 bits word, The first option is `End of option`. It is encoded as a single byte having value `0x00` and can be used to ensure that the TCP header extension ends on a 32 bits boundary. The `No-Operation`, encoded as a single byte having value `0x01`, can be used when the TCP header extension contains several TCP options that should be aligned on 32 bits boundaries. All other options [#ftcpoptions]_ are encoded with the TLV format. 




.. _TCPRelease:

TCP connection release
======================

.. index:: TCP connection release

TCP, like most 


.. sidebar:: TIME\_WAIT on busy TCP servers

   see [AW05]_ and [FTY99]_ 

.. tuning timewait http://publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=/com.ibm.websphere.edge.doc/cp/admingd45.htm bad idea

two types of release

graceful

abrupt

A TCP entity should never send a RST segment
upon reception of another RST segment


processing TCP RST

.. figure:: fig/transport-fig-067-c.png
   :align: center

   FSM for TCP connection release


.. _TCPData:

TCP reliable data transfert
===========================

sequence number ack number

window, basic and window scaling :rfc:`1323`

rtt estimation, karn/partridge, :rfc:`1323` timestamp option

retransmission mechanisms
 - timer based
 - duplicate acks
 - sack
 - fack 
 - others ?

Nagle

.. _TCPReset:

.. sidebar:: TCP Reset

   Explain TCP reset and the risks of attacks


.. _TCPCongestion:

TCP congestion control
======================


by Nagle describes it briefly


defined in :rfc:`5681`


explain tail-drop and RED


Other congestion control mechanisms
-----------------------------------

Decbit
Framerelay
ATM, ABR, EFCI
XCP ?

Other transport protocols
#########################

.. stcp 
.. xtp 
.. dccp
.. rtp :rfc:`1889`
.. udplite :rfc:`3828`


.. rubric:: Footnotes

.. [#fsize] Many network layer services are unable to carry SDUs that are larger than 64 KBytes. 

.. [#fqueuesize] In the application layer, most servers are implemented as processes. The network and transport layer on the other hand are usually implemented inside the operating system and the amount of memory that they can use is limited by the amount of memory allocated to the entire kernel.

.. [#fmtuudp] This limitation is due to the fact that the network layer (IPv4 and IPv6) cannot transport packets that are larger than 64 KBytes. As UDP does not include any segmentation/reassembly mechanism, it cannot split a SDU before sending it.

.. [#fportnum] The complete list of allocated port numbers is maintained by IANA_ . It may be downloaded from http://www.iana.org/assignments/port-numbers

.. [#fephemeral] A discussion of the ephemeral port ranges used by different TCP/UDP implementations may be found in http://www.ncftp.com/ncftpd/doc/misc/ephemeral_ports.html

.. [#ftcpusage] Several researchers have analysed the utilisation of TCP and UDP in the global Internet. Most of these studies have been performed by collecting all the packets transmitted over a given link during a period of a few hours or days and then analysing their headers to infer the transport protocol used, the type of application, ... Recent studies include http://www.caida.org/research/traffic-analysis/tcpudpratio/, https://research.sprintlabs.com/packstat/packetoverview.php or http://www.nanog.org/meetings/nanog43/presentations/Labovitz_internetstats_N43.pdf

.. [#ftcpclock] This 32 bits counter was specified in :rfc:`793`. A 32 bits counter that is incremented every 4 microseconds wraps in about 4.5 hours. This period is much larger than the Maximum Segment Lifetime that is fixed at 2 minutes in the Internet (:rfc:`791`, :rfc:`1122`).

.. [#frlogin] On many departmental networks containing Unix workstations, it was common to allow users on one of the hosts to use rlogin_ and rsh_ to run commands on any of the workstations of the network without giving any password. In this case, the remote workstation "authenticated" the client host based on its IP address. This was a bad practice from a security viewpoint.

.. [#fctpinc] When a TCP entity sends a segment having `x+1` as acknowledgment number, this indicates that it has received all data up to and including sequence number `x` and that it is expecting data having sequence number `x+1`. As the `SYN` flag was set in a segment having sequence number `x`, this implies that setting the `SYN` flag in a segment consummes one sequence number.

.. [#ftcpboth] Of course, such a simultaneous TCP establishment can only occur if the source port chosen by the client is equal to the destination port chosen by the server. This may happen when a host can serve both as a client as a server or in peer-to-peer applications when the communicating hosts do not use ephemeral port numbers. 

.. [#fspoofing] Sending a packet with a different source IP address than the address allocated to the host is called sending a spoofed packet.

.. [#ftcpoptions] The full list of all TCP options may be found at http://www.iana.org/assignments/tcp-parameters/


.. include:: ../links.rst
