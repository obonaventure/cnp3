=====================
 The transport layer
=====================


As the transport layer is built on top of the network layer, it is important to know the key features of the network layer service. There are two types of network layer services : connectionless and connection-oriented. The connectionless network layer service is the most widespread. Its main characteristics are :

 - the connectionless network layer service can only transfer SDUs of *limited size* [#fsize]_
 - the connectionless network layer service may discard SDUs
 - the connectionless network layer service may corrupt SDUs
 - the connectionless network layer service may delay, reorder or even duplicate SDUs


.. figure:: png/transport-fig-001-c.png
   :align: center
   :scale: 70 

   The transport layer in the reference model


These imperfections of the connectionless network layer service will be better understood once we have explained the network layer in the next chapter. At this point, let us simply assume that these imperfections occur without trying to understand why they occur.

Some transport protocols can be used on top of a connection-oriented network service, such as class 0 of the ISO Transport Protocol (TP0) defined in [X224]_ , but they have not been widely used. We do not discuss such utilisation of a connection-oriented network service in more details in this book.

This chapter is organised as follows. We first explain how it is possible to provide a reliable transport service on top of an unreliable connectionless network service. For this, we explain the main mechanisms found in such protocols. Then, we study in details the two transport protocols that are used in the Internet. We begin with the User Datagram Protocol (UDP) that provides a simple connectionless transport service. Then, we describe the Transmission Control Protocol (TCP) in details, including its congestion control mechanism.

.. include:: principles.rst

.. include:: udp.rst

.. include:: tcp.rst



.. dccp RFC 4340 :rfc:`4340`


.. Other transport protocols
.. =========================

.. stcp 
.. xtp 
.. dccp
.. rtp :rfc:`1889`
.. udplite :rfc:`3828`

Summary
#######


.. include:: ../links.rst

.. include:: exercises/ex-transport.rst

.. include:: exercises/cha-transport.rst


.. rubric:: Footnotes



.. [#fsize] Many network layer services are unable to carry SDUs that are larger than 64 KBytes. 

.. [#fqueuesize] In the application layer, most servers are implemented as processes. The network and transport layer on the other hand are usually implemented inside the operating system and the amount of memory that they can use is limited by the amount of memory allocated to the entire kernel.

.. [#fsizesliding] The size of the sliding window can be either fixed for a given protocol or negotiated during the connection establishment phase. We'll see later that it is also possible to change the size of the sliding window during the connection's lifetime.

.. [#fautotune] For a discussion on how the sending buffer can change, see e.g. [SMM1998]_

.. [#facklost] Note that if the receive window shrinks, it might happen that the sender has already sent a segment that is not anymore inside its window. This segment will be discarded by the receiver and the sender will retransmit it later.

.. [#fmsl] As we will see in the next chapter, the Internet does not strictly enforce this MSL. However, it is reasonable to expect that most packets on the Internet will not remain in the network during more than 2 minutes. There are a few exceptions to this rule, such as :rfc:`1149` whose implementation is described in http://www.blug.linux.no/rfc1149/ but there are few real links supporting :rfc:`1149` in the Internet.

.. [#fmtuudp] This limitation is due to the fact that the network layer (IPv4 and IPv6) cannot transport packets that are larger than 64 KBytes. As UDP does not include any segmentation/reassembly mechanism, it cannot split a SDU before sending it.

.. [#fportnum] The complete list of allocated port numbers is maintained by IANA_ . It may be downloaded from http://www.iana.org/assignments/port-numbers

.. [#fephemeral] A discussion of the ephemeral port ranges used by different TCP/UDP implementations may be found in http://www.ncftp.com/ncftpd/doc/misc/ephemeral_ports.html

.. [#ftcpspecs] A detailed presentation of all standardisation documents concerning TCP may be found in :rfc:`4614`

.. [#ftcpusage] Several researchers have analysed the utilisation of TCP and UDP in the global Internet. Most of these studies have been performed by collecting all the packets transmitted over a given link during a period of a few hours or days and then analysing their headers to infer the transport protocol used, the type of application, ... Recent studies include http://www.caida.org/research/traffic-analysis/tcpudpratio/, https://research.sprintlabs.com/packstat/packetoverview.php or http://www.nanog.org/meetings/nanog43/presentations/Labovitz_internetstats_N43.pdf

.. [#ftcpclock] This 32 bits counter was specified in :rfc:`793`. A 32 bits counter that is incremented every 4 microseconds wraps in about 4.5 hours. This period is much larger than the Maximum Segment Lifetime that is fixed at 2 minutes in the Internet (:rfc:`791`, :rfc:`1122`).

.. [#frlogin] On many departmental networks containing Unix workstations, it was common to allow users on one of the hosts to use rlogin :rfc:`1258`  to run commands on any of the workstations of the network without giving any password. In this case, the remote workstation "authenticated" the client host based on its IP address. This was a bad practice from a security viewpoint.


.. [#ftcpboth] Of course, such a simultaneous TCP establishment can only occur if the source port chosen by the client is equal to the destination port chosen by the server. This may happen when a host can serve both as a client as a server or in peer-to-peer applications when the communicating hosts do not use ephemeral port numbers. 

.. [#fspoofing] Sending a packet with a different source IP address than the address allocated to the host is called sending a :term:`spoofed packet`.

.. [#ftcpoptions] The full list of all TCP options may be found at http://www.iana.org/assignments/tcp-parameters/

.. [#fackflag] In practice, only the `SYN` segment do not have their `ACK` flag set.

.. [#ftcpurgent] A complete TCP implementation contains additional information in its TCB, notably to support the `urgent` pointer. However, this part of TCP is not discussed in this book. Refer to :rfc:`793` and :rfc:`2140` for more details about the TCB. 

.. [#fmss] In theory, TCP implementations could send segments as large as the MSS advertised by the remote host during connection establishment. In practice, most implementations use as MSS the minimum between the received MSS and their own MSS. This avoids fragmentation in the underlying IP layer and is discussed in the next chapter.

.. [#fnagleip] This TCP segment is then placed in an IP header. We describe IPv4 and IPv6 in the next chapter. The minimum size of the IPv4 (resp. IPv6) header is 20 bytes (resp. 40 bytes). 

.. [#fmss500] When these measurements were taken, some hosts had a default MSS of 552 bytes (e.g. BSD Unix derivatives) or 536 bytes (the default MSS specified in :rfc:`793`). Today, most TCP implementation derive the MSS from the maximum packet size of the LAN interface they use (Ethernet in most cases). 

.. [#faveragebandwidth] A precise estimation of the maximum bandwidth that can be achieved by a TCP connection should take into account the overhead of the TCP and IP headers as well.

.. [#ftcphosts] See http://fasterdata.es.net/tuning.html for more information on how to tune a TCP implementation

.. [#frttmes] In theory, a TCP implementation could store the timestamp of each data segment transmitted and compute a new estimate for the round-trip-time upon reception of the corresponding acknowledgement. However, using such frequent measurements introduces a lot of noise in practice and many implementations still measure the round-trip-time once per round-trip-time by recording the transmission time of one segment at a time :rfc:`2988`

.. [#ftimestamp] Some security experts have raised concerns that using the real-time clock to set the `TSval` in the timestamp option can leak information such as the system's uptime. Solutions proposed to solve this problem may be found in [CNPI09]_

.. [#ftcbtouch] As a TCP client often establishes several parallel or successive connections with the same server, :rfc:`2140` has proposed to reuse for a new connection some information that was collected in the TCB of a previous connection, such as the measured rtt. However, this solution has not been widely implemented. 

.. [#fdelack] If the destination is using delayed acknowledgements, the sending host sends two data segments after each acknowedgement.

.. [#ffifo] We discuss in another chapter other possible organisations of the router's buffers.

.. [#foldtcp] At this time, TCP implementations were mainly following :rfc:`791`. The round-trip-time estimations and the retransmission mechanisms were very simple. TCP was improved after the publication of [Jacobson1988]_

.. [#fcredit] In this section, we focus on congestion control mechanisms that regulate the transmission rate of the hosts. Other types of mechanisms have been proposed in the literature. For example, `credit-based` flow-control has been proposed to avoid congestion in ATM networks [KR1995]_. With a credit-based mechanism, hosts can only send packets once they have received credits from the routers and the credits depend on the occupancy of the router's buffers. 

.. [#fflowslink] For example, the measurements performed in the Sprint network in 2004 reported more than 10k active TCP connections on a link, see https://research.sprintlabs.com/packstat/packetoverview.php. More recent information about backbone links may be obtained from caida_ 's realtime measurements, see e.g.  http://www.caida.org/data/realtime/passive/ 

.. [#fwrap] In this pseudo-code, we assume that TCP uses unlimited sequence and acknowledgement numbers. Furthermore, we do not detail how the `cwnd` is adjusted after the retransmission of the lost segment by fast retransmit. Additional details may be found in :rfc:`5681`.

