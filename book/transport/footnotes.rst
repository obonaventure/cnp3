.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

.. [#fsize] Many network layer services are unable to carry SDUs that are larger than 64 KBytes. 

.. [#fqueuesize] In the application layer, most servers are implemented as processes. The network and transport layer on the other hand are usually implemented inside the operating system and the amount of memory that they can use is limited by the amount of memory allocated to the entire kernel.

.. [#fmtuudp] This limitation is due to the fact that the network layer (IPv4 and IPv6) cannot transport packets that are larger than 64 KBytes. As UDP does not include any segmentation/reassembly mechanism, it cannot split a SDU before sending it.

.. [#fportnum] The complete list of allocated port numbers is maintained by IANA_ . It may be downloaded from http://www.iana.org/assignments/port-numbers

.. [#fephemeral] A discussion of the ephemeral port ranges used by different TCP/UDP implementations may be found in http://www.ncftp.com/ncftpd/doc/misc/ephemeral_ports.html

.. [#ftcpspecs] A detailed presentation of all standardisation documents concerning TCP may be found in :rfc:`4614`

.. [#ftcpusage] Several researchers have analysed the utilisation of TCP and UDP in the global Internet. Most of these studies have been performed by collecting all the packets transmitted over a given link during a period of a few hours or days and then analysing their headers to infer the transport protocol used, the type of application, ... Recent studies include http://www.caida.org/research/traffic-analysis/tcpudpratio/, https://research.sprintlabs.com/packstat/packetoverview.php or http://www.nanog.org/meetings/nanog43/presentations/Labovitz_internetstats_N43.pdf

.. [#ftcpclock] This 32 bits counter was specified in :rfc:`793`. A 32 bits counter that is incremented every 4 microseconds wraps in about 4.5 hours. This period is much larger than the Maximum Segment Lifetime that is fixed at 2 minutes in the Internet (:rfc:`791`, :rfc:`1122`).

.. [#frlogin] On many departmental networks containing Unix workstations, it was common to allow users on one of the hosts to use rlogin_ and rsh_ to run commands on any of the workstations of the network without giving any password. In this case, the remote workstation "authenticated" the client host based on its IP address. This was a bad practice from a security viewpoint.

.. [#ftcpinc] When a TCP entity sends a segment having `x+1` as acknowledgment number, this indicates that it has received all data up to and including sequence number `x` and that it is expecting data having sequence number `x+1`. As the `SYN` flag was set in a segment having sequence number `x`, this implies that setting the `SYN` flag in a segment consumes one sequence number.

.. [#ftcpboth] Of course, such a simultaneous TCP establishment can only occur if the source port chosen by the client is equal to the destination port chosen by the server. This may happen when a host can serve both as a client as a server or in peer-to-peer applications when the communicating hosts do not use ephemeral port numbers. 

.. [#fspoofing] Sending a packet with a different source IP address than the address allocated to the host is called sending a :term:`spoofed packet`.

.. [#ftcpoptions] The full list of all TCP options may be found at http://www.iana.org/assignments/tcp-parameters/

.. [#fackflag] In practice, only the `SYN` segment do not have their `ACK` flag set.

.. [#ftcpurgent] A complete TCP implementation will contain additional information in its TCB, notably to support the `urgent` pointer. However, this part of TCP is not discussed in this book. Refer to :rfc:`793` and :rfc:`2140` for more details about the TCB. 

.. [#fmss] In theory, TCP implementations could send segments as large as the MSS advertised by the remote host during connection establishment. In practice, most implementations use as MSS the minimum between the received MSS and their own MSS. This avoids fragmentation in the underlying IP layer and will be discussed in the next chapter.

.. [#fnagleip] This TCP segment will then be placed in an IP header. We will describe IPv4 and IPv6 in the next chapter. The minimum size of the IPv4 (resp. IPv6) header is 20 bytes (resp. 40 bytes). 

.. [#fmss500] When these measurements were taken, some hosts had a default MSS of 552 bytes (e.g. BSD Unix derivatives) or 536 bytes (the default MSS specified in :rfc:`793`). Today, most TCP implementation derive the MSS from the maximum packet size of the LAN interface they use (Ethernet in most cases). 

.. [#faveragebandwidth] A precise estimation of the maximum bandwidth that can be achieved by a TCP connection should take into account the overhead of the TCP and IP headers as well.

.. [#ftcphosts] See http://fasterdata.es.net/tuning.html for more information on how to tune a TCP implementation

.. [#frttmes] In theory, a TCP implementation could store the timestamp of each data segment transmitted and compute a new estimate for the round-trip-time upon reception of the corresponding acknowledgement. However, using such frequent measurements introduces a lot of noise in practice and many implementations still measure the round-trip-time once per round-trip-time by recording the transmission time of one segment at a time :rfc:`2988`

.. [#ftimestamp] Some security experts have raised concerns that using the real-time clock to set the `TSval` in the timestamp option can leak information such as the system's uptime. Solutions proposed to solve this problem may be found in [CNPI09]_

.. [#tcbtouch] As a TCP client will often establish several parallel or successive connections with the same server, :rfc:`2140` has proposed to reuse for a new connection some information that was collected in the TCB of a previous connection, such as the measured rtt. However, this solution has not been widely implemented. 
