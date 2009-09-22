===================
The transport layer
===================

The application layer 
The transport layer contains essential protocols

.. figure:: fig/transport-fig-001-c.png
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
   see [SPMR09] for how to recomput

In this case, we need a mechanism that allows the receiver of a segment to verify that the SDU contained in

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

   Checksums and CRCs should not be confused with hash functions such as MD5 or SHA-1.



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


.. sidebar:: Computation of the UDP checksum

 The checksum of the UDP segment is computed over :

 - a pseudo header containing the source IP address, the destination IP address and a 32 bits bit field containing a the most significant byte set to 0, the second set to 17 and the length of the UDP segment in the lower two bytes
 - the entire UDP segment, including its header

 This pseudo-header allows the receiver to detect errors that affect the IP source or destination addresses that are placed in the IP layer below. This is a violation of the layer principle that dates from the time when UDP and IP were elements of a single protocol. It should be noted that if the checksum algorithm computes value '0x0000', then value '0xffff' is transmitted. A UDP segment whose checksum is set to '0x0000' is a segment for which the transmitter did not compute a checksum upon transmission. Some NFS_ servers chose to disable UDP checksums for performance reasons, but this caused `problems <http://lynnesblog.telemuse.net/192>`_ that were difficult to diagnose. In practice, there are rarely good reasons to disable UDP checksums.



Several types of applications rely on UDP.



The Transmission Control Protocol
#################################


The Transmission Control Protocol (TCP) was initially defined in :rfc:`793`


explain segment format briefly and main principles of the protocol


.. figure:: fig/transport-fig-058-c.png
   :align: center

   The UDP segment format

TCP connection establishment
============================

describe finite state machine


.. sidebar:: Denial of service

 explain syn DoS, reference :rfc:`4987`
 syn flood affecting panix http://memex.org/meme2-12.html



TCP connection release
======================

.. sidebar:: TIME\_WAIT on busy TCP servers

 see [AW05]_ and [FTY99]_ 

.. tuning timewait http://publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=/com.ibm.websphere.edge.doc/cp/admingd45.htm bad idea



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

.. include:: ../links.rst
