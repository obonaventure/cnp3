TCP congestion control
======================

The TCP congestion control mechanisms, defined in :rfc:`5681` plays a key role in today's Internet. Without this mechanism that was first defined and implemented in the late 1980s, the Internet would not have been able to continue to work until now. The objective of this exercise is to allow you to have a better understanding of the operation of TCP's congestion control mechanism by analysing all the segments exchanged over a TCP connection.


#. To understand the operation of the TCP congestion control mechanism, it is useful to draw some time sequence diagrams. Let us consider a simple scenario of a web client connected to the Interne that wishes to retrieve a simple web page from a remote web server. For simplicity, we will assume that the delay between the client and the server is 0.5 seconds and that the packet transmission times on the client and the servers are negligible (e.g. they are both connected to a 1 Gbps network). We will also assume that the client and the server use 1 KBytes segments.

 a. Compute the time required to open a TCP connection, send an HTTP request and retrieve a 16 KBytes web page. This page size is typical of the results returned by search engines like google_ or bing_. An important factor in this delay is the initial size of the TCP congestion window on the server. Assume first that the initial window is set to 1 segment as defined in :rfc:`2001`, 4 KBytes (i.e. 4 segments in this case) as proposed in :rfc:`3390` or 16 KBytes as proposed in a recent `paper<http://ccr.sigcomm.org/drupal/?q=node/621>`_.

 b. Perform the same analysis with an initial window of one segment is the third segment sent by the server is lost and the retransmission timeout is fixed and set to 2 seconds.

 c. Same question as above but assume now that the 6th segment is lost. 

 d. Same question as above, but consider now the loss of the second and seventh acknowledgements sent by the client. 

 e. Does the analysis above changes if the initial window is set to 16 KBytes instead of one segment ?

#. Several MBytes have been sent on a TCP connection and it becomes idle for several minutes. Discuss which values should be used for the congestion window, slow start threshold and retransmission timers.

#. To operate reliably, a transport protocol that uses Go-back-n (resp. selective repeat) cannot use a window that is larger than :math:`{2^n}-1` (resp. :math:`2^{n-1}`) segments. Does this limitation affects TCP ? Explain your answer.

#. Consider the simple network shown in the figure below. In this network, the router between the client and the server can only store on each outgoing interface one packet in addition to the packet that it is currently transmitting. It dscards all the packets that arrive while its buffer is full. Assuming that you can neglect the transmission time of acknowledgements and that the server uses an initial window of one segment and has a retransmission timer set to 500 milliseconds, what is the time required to transmit 10 segments from the client to the server. Does the performance increase if the server uses an initial window of 16 segments instead ?

.. figure:: fig/emulated-network-002-c.png
   :align: center

   Simple network network


Experimental setup
------------------

For this exercise, we have performed measurements in the emulated [#femulation]_ network shown below.


.. figure:: fig/emulated-network-001-c.png
   :align: center

   Emulated network


The emulated network is composed of three UML machines [#fcongestion]_: a client, a server and a router. The client and the server are connected via the router. The client sends 1 MBytes of data to the server by using iperf_. The link between the router and the client is controlled by using the `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ Linux kernel module. This module allows us to insert additional delays, reduce the link bandwidth and insert random packet losses. 

We used `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ To perform three measurements :

#. no losses on the link between `R` and `S`, 100 milliseconds of delay
#. 1% of segment losses on the link between `R` and `S`, 100 milliseconds of delay
#. 10% of segment losses on the link between `R` and `S`, 100 milliseconds of delay

Note that due to the way `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ has been configured, the delays and the losses are only applied on packets received by `S`, not on packets sent by `S`.

For each measurement, we have collected a packet trace that can be analysed by using wireshark_ and two tcpprobe_ traces. You can download these traces from the links below :

 - :download:`traces/0pc_100msec.tar.gz` : 100 milliseconds delay, no packet losses
 - :download:`traces/1pc_100msec.tar.gz` : 100 milliseconds delay, 1% packet losses
 - :download:`traces/10pc_100msec.tar.gz` : 100 milliseconds delay, 10% packet losses

Each team of two students will analyse these three traces, first by using wireshark_ and then by looking at the tcpprobe_ trace to find more detailed explanation. For each trace, you must : 

 1. identify the TCP options that have been used on the TCP connection
 2. try to find explanations for the evolution of the round-trip-time on each of these TCP connections. For this, you can use the `round-trip-time` graph of wireshark_
 3. verify whether the TCP implementation used implemented `delayed acknowledgements`
 3. analyse the packet trace without packet losses and explain the behaviour of TCP congestion control scheme by looking at the tcpprobe_ traces
 4. inside the traces with packet losses, find :

   a. one segment that has been retransmitted by using `fast retransmit`. Explain this retransmission in details.
   b. one segment that has been retransmitted thanks to the expiration of TCP's retransmission timeout. Explain why this segment could not have been retransmitted by using `fast retransmit`.


 6. wireshark_ contain several two useful graphs : the `round-trip-time` graph and the `time sequence` graph. Explain how you would compute the same graph from such a trace 

 7. When displaying TCP segments, recent versions of wireshark_ contain `expert analysis` heuristics that indicate whether the segment has been retransmitted, whether it is a duplicate ack or whether the retransmission timeout has expired. Explain how you would implement the same heuristics as wireshark_. 
 
tcpprobe_
.........

During the previous exercise, you have used :manpage:`netstat(8)` To lookup the state of the TCP connections on a given host. On the Linux kernel, there are tools that can provide more information than :manpage:`netstat(8)`. One of these tools is the `TCPProbe <http://www.linuxfoundation.org/en/Net:TcpProbe>`_ kernel module. When installed on a Linux kernel, this kernel module prints one ASCII line containing the following information upon the arrival and the transmission of each TCP segment :

 #. The timestamp (seconds.nanoseconds)
 #. The source endpoint (address:port)
 #. The destination endpoint (address:port)  
 #. This column should be ignored
 #. This column should be ignored
 #. The current value of `snd.nxt`
 #. The current value of `snd.una`
 #. The current value of the congestion window `snd.cwnd` (in segments)
 #. The current value of the slow-start threshold `snd.ssthresh` (in segments)
 #. The current size of the sending window `snd.wnd` (in bytes)
 #. The current value of the smoothed round-trip-time `srtt` (in multiples of 10 milliseconds)
 #. The current value of `rcv.nxt`
 #. This column should be ignored
 #. The current value of the receive window `rcv.wnd`


A sample TCPProbe trace is shown below ::

 14.449378000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fed8c49 0x6fed8689 2 2147483647 5792 8 0x6fe931b6 0x6fe931b6 5840
 14.459272000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fed9799 0x6fed86a1 3 2147483647 5792 7 0x6fe931b6 0x6fe931b6 5840
 14.471374000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6feda2e9 0x6fed8c49 4 2147483647 8688 6 0x6fe931b6 0x6fe931b6 5840
 14.483485000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedae39 0x6fed91f1 5 2147483647 11584 6 0x6fe931b6 0x6fe931b6 5840
 14.495677000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedb989 0x6fed9799 6 2147483647 14480 5 0x6fe931b6 0x6fe931b6 5840
 14.507770000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedc4d9 0x6fed9d41 7 2147483647 17376 5 0x6fe931b6 0x6fe931b6 5840
 14.519939000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedd029 0x6feda2e9 8 2147483647 20272 5 0x6fe931b6 0x6fe931b6 5840
 14.532096000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6feddb79 0x6feda891 9 2147483647 23168 5 0x6fe931b6 0x6fe931b6 5840

As you can see from the trace, the values of `snd.nxt` and `snd.una` are in hexadecimal. The congestion window and the slow-start threshold are expressed in MSS-sized segments. We see clearly in the trace above the congestion window that increases. The slow-start threshold is initialised at `2147483647` when the TCP connection starts. Its value will be updated after the first congestion event.
Information from a tcpprobe_ trace can be easily plotted by using a tool such as gnuplot. See http://www.linuxfoundation.org/en/Net:TcpProbe for an example gnuplot script to plot the evolution of `snd.cwnd` and `snd.ssthresh`.

.. rubric:: Footnotes

.. [#femulation] With an emulated network, it is more difficult to obtain quantitative results than with a real network since all the emulated machines need to share the same CPU and memory. This creates interactions between the different emulated machines that do not happen in the real world. However, since the objective of this exercise is only to allow the students to understand the behaviour of the TCP congestion control mechanism, this is not a severe problem.

.. [#fcongestion] For more information about the TCP congestion control schemes implemented in the Linux kernel, see http://linuxgazette.net/135/pfeiffer.html and http://www.cs.helsinki.fi/research/iwtcp/papers/linuxtcp.pdf or the source code of a recent Linux. A description of some of the sysctl variables that allow to tune the TCP implementation in the Linux kernel may be found in http://fasterdata.es.net/TCP-tuning/linux.html. For this exercise, we have configured the Linux kernel to use the NewReno scheme :rfc:`3782` that is very close to the official standard defined in :rfc:`5681`



.. include:: ../../book/links.rst
