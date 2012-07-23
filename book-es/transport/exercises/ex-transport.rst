.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Exercises
#########

This section is divided in two parts. The first part contains exercises on the principles of transport protocols, including TCP. The second part contains programming challenges packet analysis tools to observe the behaviour of transport protocols.

Principles
==========

1. Consider the Alternating Bit Protocol as described in this chapter

 - How does the protocol recover from the loss of a data segment ? 
 - How does the protocol recovers from the loss of an acknowledgement ?

2. A student proposed to optimise the Alternating Bit Protocol by adding a negative acknowledgment, i.e. the receiver sends a `NAK` control segment when it receives a corrupted data segment. What kind of information should be placed in this control segment and how should the sender react when receiving such a `NAK` ?

3. Transport protocols rely on different types of checksums to verify whether segments have been affected by transmission errors. The most frequently used checksums are :

 - the Internet checksum used by UDP, TCP and other Internet protocols which is defined in :rfc:`1071` and implemented in various modules, e.g. http://ilab.cs.byu.edu/cs460/code/ftp/ichecksum.py for a python_ implementation
 - the 16 bits or the 32 bits Cyclical Redundancy Checks (CRC) that are often used on disks, in zip archives and in datalink layer protocols. See http://docs.python.org/library/binascii.html for a python_ module that contains the 32 bits CRC
 - the Alder checksum defined in :rfc:`2920` for the SCTP protocol but replaced by a CRC later :rfc:`3309`
 - the Fletcher checksum [Fletcher1982]_, see http://drdobbs.com/database/184408761 for implementation details

 By using your knowledge of the Internet checksum, can you find a transmission error that will not be detected by the Internet checksum ?

4. The CRCs are efficient error detection codes that are able to detect :

 - all errors that affect an odd number of bits
 - all errors that affect a sequence of bits which is shorter than the length of the CRC

 Carry experiments with one implementation of CRC-32 to verify that this is indeed the case.

5. Checksums and CRCs should not be confused with secure hash functions such as MD5 defined in :rfc:`1321` or SHA-1 described in :rfc:`4634`. Secure hash functions are used to ensure that files or sometimes packets/segments have not been modified. Secure hash functions aim at detecting malicious changes while checksums and CRCs only detect random transmission errors. Perform some experiments with hash functions such as those defined in the http://docs.python.org/library/hashlib.html python hashlib module to verify that this is indeed the case.

.. Some questions about the checksum versus crc, discuss briefly hash
.. some question about whether the crc must cover the length or not

6. A version of the Alternating Bit Protocol supporting variable length segments uses a header that contains the following fields :

 - a `number` (0 or 1)
 - a `length` field that indicates the length of the data 
 - a `CRC`
 
 To speedup the transmission of the segments, a student proposes to compute the CRC over the data part of the segment but not over the header. What do you think of this optimisation ?
 
.. how to compute the delay, try with ping to see how often it changes with a remote site

7. On Unix hosts, the :manpage:`ping(8)` command can be used to measure the round-trip-time to send and receive packets from a remote host. Use :manpage:`ping(8)` to measure the round-trip to a remote host. Chose a remote destination which is far from your current location, e.g. a small web server in a distant country. There are implementations of ping in various languages, see e.g. http://pypi.python.org/pypi/ping/0.2 for a python_ implementation of ''ping''

8. How would you set the retransmission timer if you were implementing the Alternating Bit Protocol to exchange files with a server such as the one that you measured above ?

9. What are the factors that affect the performance of the Alternating Bit Protocol ?

.. what are the factors that affect the performance of the alternating bit protocol ?

10. Links are often considered as symmetrical, i.e. they offer the same bandwidth in both directions. Symmetrical links are widely used in Local Area Networks and in the core of the Internet, but there are many asymmetrical link technologies. The most common example are the various types of ADSL and CATV technologies. Consider an implementation of the Alternating Bit Protocol that is used between two hosts that are directly connected by using an asymmetric link. Assume that a host is sending segments containing 10 bytes of control information and 90 bytes of data and that the acknowledgements are 10 bytes long. If the round-trip-time is negligible, what is the minimum bandwidth required on the return link to ensure that the transmission of acknowledgements is not a bottleneck ?

11. Derive a mathematical expression that provides the `goodput` achieved by the Alternating Bit Protocol assuming that :

 - Each segment contains `D` bytes of data and `c` bytes of control information
 - Each acknowledgement contains `c` bytes of control information
 - The bandwidth of the two directions of the link is set to `B` bits per second
 - The delay between the two hosts is `s` seconds in both directions

 The `goodput` is defined as the amount of SDUs (measured in bytes) that is successfully transferred during a period of time

12. Consider an Alternating Bit Protocol that is used over a link that suffers from deterministic errors. When the error ratio is set to :math:`\frac{1}{p}`, this means that :math:`p-1` bits are transmitted correctly and the :math:`p^{th}` bit is corrupted. Discuss the factors that affect the performance of the Alternating Bit Protocol over such a link.

.. what is the impact of the segment size when bit errors are random ? (assume regular errors for the computation, every n bits)

.. impact of the uplink bandwidth, what is the highest throughput achievable for a given uplink bandwidth

.. Compute a closed form expression for the goodput of the alternating bit protocol

.. What happens in the alternating bit protocol when acknowledgements are lost

.. Can we build an alternating bit protocol that does not use nak

.. implement a simple protocol over udp socket, check with virginie server sur la sun et client sur linux compile sur les deux et portable 2 langages differents + interop

.. implement alternating bit protocol ? no, only the simple one
.. 
   Additional questions for the students
   When to send a retransmission
   discuss the optimal value of the timeout
   What happens when a data segment is lost ?
   What happens when an ack segment is lost ?

   What are the factors that affect the performance of this protocol when there are no losses - rtt and bandwidth*delay product
   What is the usefulness of a NAK ? difficulty of implementing NAK when reordering is possible
   Retransmission mechanisms : how and when to retransmit (upon expiration of a timeout, upon NAK, pros and cons of each solution)

13. Amazon provides the `S3 storage service <https://s3.amazonaws.com/>`_ where companies and researchers can store lots of information and perform computations on the stored information. Amazon allows users to send files through the Internet, but also by sending hard-disks. Assume that a 1 Terabyte hard-disk can be delivered within 24 hours to Amazon by courier service. What is the minimum bandwidth required to match the bandwidth of this courier service ? 

14. Several large data centers operators (e.g. `Microsoft <http://www.microsoft.com/showcase/en/us/details/bafe5c0f-8651-4609-8c71-24c733ce628b>`_ and `google <http://www.youtube.com/watch?v=zRwPSFpLX8I>`_) have announced that they install servers as containers with each container hosting up to 2000 servers. Assuming a container with 2000 servers and each storing 500 GBytes of data, what is the time required to move all the data stored in one container over one 10 Gbps link ? What is the bandwidth of a truck that needs 10 hours to move one container from one data center to another. 

15. What are the techniques used by a go-back-n sender to recover from :

 - transmission errors
 - losses of data segments
 - losses of acknowledgements

16. Consider a `b` bits per second link between two hosts that has a propagation delay of `t` seconds. Derive a formula that computes the time elapsed between the transmission of the first bit of a `d` bytes segment from a sending host and the reception of the last bit of this segment on the receiving host.

17. Consider a go-back-n sender and a go-back receiver that are directly connected with a 10 Mbps link that has a propagation delay of 100 milliseconds. Assume that the retransmission timer is set to three seconds. If the window has a length of 4 segments, draw a time-sequence diagram showing the transmission of 10 segments (each segment contains 10000 bits):

 - when there are no losses
 - when the third and seventh segments are lost
 - when the second, fourth, sixth, eighth, ... acknowledgements are lost
 - when the third and fourth data segments are reordered (i.e. the fourth arrives before the third)

18. Same question when using selective repeat instead of go-back-n. Note that the answer is not necessarily the same.

19. Consider two high-end servers connected back-to-back by using a 10 Gbps interface. If the delay between the two servers is one millisecond, what is the throughput that can be achieved by a transport protocol that is using 10,000 bits segments and a window of

 - one segment
 - ten segments
 - hundred segments

20. Consider two servers are directly connected by using a `b` bits per second link with a round-trip-time of `r` seconds. The two servers are using a transport protocol that sends segments containing `s` bytes and acknowledgements composed of `a` bytes. Can you derive a formula that computes the smallest window (measured in segments) that is required to ensure that the servers will be able to completely utilise the link ?

21. Same question as above if the two servers are connected through an asymmetrical link that transmits `bu` bits per second in the direction used to send data segments and `bd` bits per second in the direction used to send acknowledgements.

22. The Trivial File Transfer Protocol is a very simple file transfer protocol that is often used by disk-less hosts when booting from a server. Read the TFTP specification in :rfc:`1350` and explain how TFTP recovers from transmission errors and losses.

23. Is it possible for a go-back-n receiver to inter-operate with a selective-repeat sender ? Justify your answer.

24. Is it possible for a selective-repeat receiver to inter-operate with a go-back-n sender ? Justify your answer.

25. The go-back-n and selective repeat mechanisms that are described in the book exclusively rely on cumulative acknowledgements. This implies that a receiver always returns to the sender information about the last segment that was received in-sequence. If there are frequent losses or reordering, a selective repeat receiver could return several times the same cumulative acknowledgment. Can you think of other types of acknowledgements that could be used by a selective repeat receiver to provide additional information about the out-of-sequence segments that it has received. Design such acknowledgements and explain how the sender should react upon reception of this information. 

26. The `goodput` achieved by a transport protocol is usually defined as the number of application layer bytes that are exchanged per unit of time. What are the factors that can influence the `goodput` achieved by a given transport protocol ? 

27. When used with IPv4, Transmission Control Protocol (TCP) attaches 40 bytes of control information to each segment sent. Assuming an infinite window and no losses nor transmission errors, derive a formula that computes the maximum TCP goodput in function of the size of the segments that are sent.

28. A go-back-n sender uses a window size encoded in a `n` bits field. How many segments can it send without receiving an acknowledgement ?

29. Consider the following situation. A go-back-n receiver has sent a full window of data segments. All the segments have been received correctly and in-order by the receiver, but all the returned acknowledgements have been lost. Show by using a time sequence diagram (e.g. by considering a window of four segments) what happens in this case. Can you fix the problem on the go-back-n sender ?

30. Same question as above, but assume now that both the sender and the receiver implement selective repeat. Note the the answer will be different from the above question.

31. Consider a transport that supports window of one hundred 1250 Bytes segments. What is the maximum bandwidth that this protocol can achieve if the round-trip-time is set to one second ? What happens if, instead of advertising a window of one hundred segments, the receiver decides to advertise a window of 10 segments ?

32. Explain under which circumstances a transport entity could advertise a window of 0 segments ?

33. To understand the operation of the TCP congestion control mechanism, it is useful to draw some time sequence diagrams. Let us consider a simple scenario of a web client connected to the Internet that wishes to retrieve a simple web page from a remote web server. For simplicity, we will assume that the delay between the client and the server is 0.5 seconds and that the packet transmission times on the client and the servers are negligible (e.g. they are both connected to a 1 Gbps network). We will also assume that the client and the server use 1 KBytes segments.

  a. Compute the time required to open a TCP connection, send an HTTP request and retrieve a 16 KBytes web page. This page size is typical of the results returned by search engines like google_ or bing_. An important factor in this delay is the initial size of the TCP congestion window on the server. Assume first that the initial window is set to 1 segment as defined in :rfc:`2001`, 4 KBytes (i.e. 4 segments in this case) as proposed in :rfc:`3390` or 16 KBytes as proposed in a recent `paper <http://ccr.sigcomm.org/drupal/?q=node/621>`_.
  b. Perform the same analysis with an initial window of one segment is the third segment sent by the server is lost and the retransmission timeout is fixed and set to 2 seconds.
  c. Same question as above but assume now that the 6th segment is lost. 
  d. Same question as above, but consider now the loss of the second and seventh acknowledgements sent by the client. 
  e. Does the analysis above changes if the initial window is set to 16 KBytes instead of one segment ?

34. Several MBytes have been sent on a TCP connection and it becomes idle for several minutes. Discuss which values should be used for the congestion window, slow start threshold and retransmission timers.

35. To operate reliably, a transport protocol that uses Go-back-n (resp. selective repeat) cannot use a window that is larger than :math:`{2^n}-1` (resp. :math:`2^{n-1}`) segments. Does this limitation affects TCP ? Explain your answer.

36. Consider the simple network shown in the figure below. In this network, the router between the client and the server can only store on each outgoing interface one packet in addition to the packet that it is currently transmitting. It discards all the packets that arrive while its buffer is full. Assuming that you can neglect the transmission time of acknowledgements and that the server uses an initial window of one segment and has a retransmission timer set to 500 milliseconds, what is the time required to transmit 10 segments from the client to the server. Does the performance increases if the server uses an initial window of 16 segments instead ?

.. figure:: /transport/svg/emulated-network-002-c.png
   :align: center

   Simple network

37. The figure below describes the evolution of the congestion window of a TCP connection. Can you find the reasons for the three events that are marked in the figure ?

 .. figure:: /transport/fig/revision-figs-001-c.png
    :align: center
    :scale: 70 

    Evolution of the congestion window

38. The figure below describes the evolution of the congestion window of a TCP connection. Can you find the reasons for the three events that are marked in the figure ?

 .. figure:: /transport/svg/revision-figs-002-c.png
   :align: center
   :scale: 70 

   Evolution of the congestion window

39. A web server serves mainly HTML pages that fit inside 10 TCP segments. Assuming that the transmission time of each segment can be neglected, compute the total transfer time of such a page (in round-trip-times) assuming that :

 - the TCP stack uses an initial window size of 1 segment
 - the TCP stack uses an initial window size of three segments

40. :rfc:`3168` defines mechanism that allow routers to mark packets by setting one bit in the packet header when they are congested. When a TCP destination receives such a marking in a packet, it returns the congestion marking to the source that reacts by halving its congestion window and performs congestion avoidance. Consider a TCP connection where the fourth data segment experiences congestion. Compare the delay to transmit 8 segments in a network where routers discards packets during congestion and a network where routers mark packets during congestion.


.. include:: /links.rst
