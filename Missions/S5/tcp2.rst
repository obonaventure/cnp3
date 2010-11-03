TCP congestion control
======================

The TCP congestion control mechanisms, defined in :rfc:`5681` plays a key role in today's Internet. Without this mechanism that was first defined and implemented in the late 1980s, the Internet would not have been able to continue to work until now. The objective of this exercise is to allow you to have a better understanding of the operation of TCP's congestion control mechanism by analysing all the segments exchanged over a TCP connection.

1. To understand the operation of the TCP congestion control mechanism, it is useful to draw some time sequence diagrams. Let us consider a simple scenario of a web client connected to the Internet that wishes to retrieve a simple web page from a remote web server. For simplicity, we will assume that the delay between the client and the server is 0.5 seconds and that the packet transmission times on the client and the servers are negligible (e.g. they are both connected to a 1 Gbps network). We will also assume that the client and the server use 1 KBytes segments.

  #. Compute the time required to open a TCP connection, send an HTTP request and retrieve a 16 KBytes web page. This page size is typical of the results returned by search engines like google_ or bing_. An important factor in this delay is the initial size of the TCP congestion window on the server. Assume first that the initial window is set to 1 segment as defined in :rfc:`2001`, 4 KBytes (i.e. 4 segments in this case) as proposed in :rfc:`3390` or 16 KBytes as proposed in a recent `paper <http://ccr.sigcomm.org/drupal/?q=node/621>`_.
  #. Perform the same analysis with an initial window of one segment is the third segment sent by the server is lost and the retransmission timeout is fixed and set to 2 seconds.
  #. Same question as above but assume now that the 6th segment is lost. 
  #. Same question as above, but consider now the loss of the second and seventh acknowledgements sent by the client. 
  #. Does the analysis above changes if the initial window is set to 16 KBytes instead of one segment ?

2. Several MBytes have been sent on a TCP connection and it becomes idle for several minutes. Discuss which values should be used for the congestion window, slow start threshold and retransmission timers.

3. To operate reliably, a transport protocol that uses Go-back-n (resp. selective repeat) cannot use a window that is larger than :math:`{2^n}-1` (resp. :math:`2^{n-1}`) segments. Does this limitation affects TCP ? Explain your answer.

4. Consider the simple network shown in the figure below. In this network, the router between the client and the server can only store on each outgoing interface one packet in addition to the packet that it is currently transmitting. It discards all the packets that arrive while its buffer is full. Assuming that you can neglect the transmission time of acknowledgements and that the server uses an initial window of one segment and has a retransmission timer set to 500 milliseconds, what is the time required to transmit 10 segments from the client to the server. Does the performance increase if the server uses an initial window of 16 segments instead ?

.. figure:: fig/emulated-network-002-c.png
   :align: center

   Simple network


Trace analysis
--------------

1. For the exercises below, we have performed measurements in an emulated [#femulation]_ network similar to the one shown below.


.. figure:: fig/emulated-network-001-c.png
   :align: center

   Emulated network


The emulated network is composed of three UML machines [#fcongestion]_: a client, a server and a router. The client and the server are connected via the router. The client sends data to the server. The link between the router and the client is controlled by using the `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ Linux kernel module. This module allows us to insert additional delays, reduce the link bandwidth and insert random packet losses. 

We used `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ to collect several traces : 

 - :download:`traces/trace0.pcap` 
 - :download:`traces/trace1.pcap`
 - :download:`traces/trace2.pcap`
 - :download:`traces/trace3.pcap`   

.. Note that due to the way `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ has been configured, the delays and the losses are only applied on packets received by `S`, not on packets sent by `S`.

Each team of two students will analyse these traces by using wireshark_ or tcpdump_. For each trace, you should

 1. Identify the TCP options that have been used on the TCP connection
 2. Try to find explanations for the evolution of the round-trip-time on each of these TCP connections. For this, you can use the `round-trip-time` graph of wireshark_, but be careful with their estimation as some versions of wireshark_ are buggy
 3. Verify whether the TCP implementation used implemented `delayed acknowledgements`
 4. Inside each packet trace, find :

   a. one segment that has been retransmitted by using `fast retransmit`. Explain this retransmission in details.
   b. one segment that has been retransmitted thanks to the expiration of TCP's retransmission timeout. Explain why this segment could not have been retransmitted by using `fast retransmit`.

 5. wireshark_ contain several two useful graphs : the `round-trip-time` graph and the `time sequence` graph. Explain how you would compute the same graph from such a trace .
 6. When displaying TCP segments, recent versions of wireshark_ contain `expert analysis` heuristics that indicate whether the segment has been retransmitted, whether it is a duplicate ack or whether the retransmission timeout has expired. Explain how you would implement the same heuristics as wireshark_. 
 7. Can you find which file has been exchanged during the transfer ? 


2. You have been hired as an networking expert by a company. In this company, users of a networked application complain that the network is very slow. The developers of the application argue that any delays are caused by packet losses and a buggy network. The network administrator argues that the network works perfectly and that the delays perceived by the users are caused by the applications or the servers where the application is running. To resolve the case and determine whether the problem is due to the network or the server on which the application is running. The network administrator has collected a representative packet trace that you can download from :download:`traces/trace9.pcap`. By looking at the trace, can you resolve this case and indicate whether the network or the application is the culprit ?



.. rubric:: Footnotes

.. [#femulation] With an emulated network, it is more difficult to obtain quantitative results than with a real network since all the emulated machines need to share the same CPU and memory. This creates interactions between the different emulated machines that do not happen in the real world. However, since the objective of this exercise is only to allow the students to understand the behaviour of the TCP congestion control mechanism, this is not a severe problem.

.. [#fcongestion] For more information about the TCP congestion control schemes implemented in the Linux kernel, see http://linuxgazette.net/135/pfeiffer.html and http://www.cs.helsinki.fi/research/iwtcp/papers/linuxtcp.pdf or the source code of a recent Linux. A description of some of the sysctl variables that allow to tune the TCP implementation in the Linux kernel may be found in http://fasterdata.es.net/TCP-tuning/linux.html. For this exercise, we have configured the Linux kernel to use the NewReno scheme :rfc:`3782` that is very close to the official standard defined in :rfc:`5681`



.. include:: ../../book/links.rst
