.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


==================
Reliable transfert
==================

Alternating Bit Protocol
------------------------

The Alternating Bit Protocol is the simplest reliable protocol. The following questions should allow you to get a better understanding of the operation of this protocol.

.. some questions on framing (bit stuffing and character stuffing) ?

1. Consider the Alternating Bit Protocol as described in the first chapter.

 - How does the protocol recover from the loss of a data segment ? 
 - How does the protocol recovers from the loss of an acknowledgement ?

2. How would you set the retransmission timer if you were implementing the Alternating Bit Protocol to exchange files with a server such as the one that you measured above ?

3. What are the factors that affect the performance of the Alternating Bit Protocol ?
 QCM 

4. A version of the Alternating Bit Protocol supporting variable length frames uses a header that contains the following fields :

 - a `number` (0 or 1)
 - a `length` field that indicates the length of the data 
 - a `CRC`
 
 To speedup the transmission of the frames, a student proposes to compute the CRC over the data part of the segment but not over the header. What do you think of this optimisation ?

5. A student proposed to optimise the Alternating Bit Protocol by adding a negative acknowledgment, i.e. the receiver sends a `NAK` control segment when it receives a corrupted data segment. What kind of information should be placed in this control segment and how should the sender react when receiving such a `NAK` ?

6. Derive a mathematical expression that provides the `goodput`, i.e. the amount of payload bytes that have been transmitted during a period of time, achieved by the Alternating Bit Protocol assuming that :

 - Each frame contains `D` bytes of data and `c` bytes of control information
 - Each acknowledgement contains `c` bytes of control information
 - The bandwidth of the two directions of the link is set to `B` bits per second
 - The delay between the two hosts is `s` seconds in both directions
 - there are no transmission errors

7. Links are often considered as symmetrical, i.e. they offer the same bandwidth in both directions. Symmetrical links are widely used in Local Area Networks and in the core of the Internet, but there are many asymmetrical link technologies. The most common example are the various types of ADSL and CATV technologies. Consider an implementation of the Alternating Bit Protocol that is used between two hosts that are directly connected by using an asymmetric link. Assume that a host is sending frames containing 10 bytes of control information and 90 bytes of data and that the acknowledgements are 10 bytes long. If the link delay is negligible, what is the minimum bandwidth required on the return link to ensure that the transmission of acknowledgements is not a bottleneck ?

8. Consider an Alternating Bit Protocol that is used over a link that suffers from deterministic errors. When the error ratio is set to :math:`\frac{1}{p}`, this means that :math:`p-1` bits are transmitted correctly and the :math:`p^{th}` bit is corrupted. Discuss the factors that affect the performance of the Alternating Bit Protocol over such a link.

Go-back-n and selective repeat
------------------------------

Most reliable protocols use a window and either go-back-n or selective repeat as retransmission strategy.

1. What are the techniques used by a go-back-n sender to recover from :

 - transmission errors
 - losses of data segments
 - losses of acknowledgements

2. Consider a `b` bits per second link between two hosts that has a propagation delay of `t` seconds. Derive a formula that computes the time elapsed between the transmission of the first bit of a `d` bytes segment from a sending host and the reception of the last bit of this segment on the receiving host.

3. Consider a go-back-n sender and a go-back receiver that are directly connected with a 10 Mbps link that has a propagation delay of 100 milliseconds. Assume that the retransmission timer is set to three seconds. If the window has a length of 4 segments, draw a time-sequence diagram showing the transmission of 10 segments (each segment contains 10000 bits):

 - when there are no losses
 - when the third and seventh segments are lost
 - when every second acknowledgement is discarded due to transmission errors

4. Same question when using selective repeat instead of go-back-n. Note that the answer is not necessarily the same.

5. Consider two high-end servers connected back-to-back by using a 10 Gbps interface. If the delay between the two servers is one millisecond, what is the throughput that can be achieved by a reliable protocol that is using 10,000 bits frames and a window of

 - one frame
 - ten frames
 - hundred frames

6. Consider two servers are directly connected by using a `b` bits per second link with a round-trip-time of `r` seconds. The two servers are using a transport protocol that sends segments containing `s` bytes and acknowledgements composed of `a` bytes. Can you derive a formula that computes the smallest window (measured in segments) that is required to ensure that the servers will be able to completely utilise the link ?

.. #. Same question as above if the two servers are connected through an asymmetrical link that transmits `bu` bits per second in the direction used to send data segments and `bd` bits per second in the direction used to send acknowledgements.

.. 22. The Trivial File Transfer Protocol is a very simple file transfer protocol that is often used by disk-less hosts when booting from a server. Read the TFTP specification in :rfc:`1350` and explain how TFTP recovers from transmission errors and losses.

7. Is it possible for a go-back-n receiver to inter-operate with a selective-repeat sender ? Justify your answer.

8. Is it possible for a selective-repeat receiver to inter-operate with a go-back-n sender ? Justify your answer.

9. The go-back-n and selective repeat mechanisms that are described in the book exclusively rely on cumulative acknowledgements. This implies that a receiver always returns to the sender information about the last frame that was received in-sequence. If there are frequent losses, a selective repeat receiver could return several times the same cumulative acknowledgment. Can you think of other types of acknowledgements that could be used by a selective repeat receiver to provide additional information about the out-of-sequence frames that it has received. Design such acknowledgements and explain how the sender should react upon reception of this information. 

.. #. A go-back-n sender uses a window size encoded in a `n` bits field. How many segments can it send without receiving an acknowledgement ?

10. A go-back-n receiver has sent a full window of data segments. All the segments have been received correctly and in-order by the receiver, but all the returned acknowledgements have been lost. Show by using a time sequence diagram (e.g. by considering a window of four segments) what happens in this case. Can you fix the problem on the go-back-n sender ?

11. Same question as above, but assume now that both the sender and the receiver implement selective repeat. Note that the answer will be different from the above question.

#. Consider a protocol that supports window of one hundred 1250 Bytes segments. What is the maximum bandwidth that this protocol can achieve if the round-trip-time is set to one second ? What happens if, instead of advertising a window of one hundred frames, the receiver decides to advertise a window of 10 frames ?

Error detection
---------------

Reliable protocols depend on error detection algorithms to detect transmission errors. The following questions will reinforce your understanding of these algorithms.

1. Reliable protocols rely on different types of checksums to verify whether frames have been affected by transmission errors. The most frequently used checksums are :

 - the Internet checksum used by UDP, TCP and other Internet protocols which is defined in :rfc:`1071` and implemented in various modules, e.g. http://ilab.cs.byu.edu/cs460/code/ftp/ichecksum.py for a python_ implementation
 - the 16 bits or the 32 bits Cyclical Redundancy Checks (CRC) that are often used on disks, in zip archives and in datalink layer protocols. See http://docs.python.org/library/binascii.html for a python_ module that contains the 32 bits CRC
 - the Fletcher checksum [Fletcher1982]_, see http://drdobbs.com/database/184408761 for implementation details

 By using your knowledge of the Internet checksum, can you find a transmission error that will not be detected by this checksum ?

2. The CRCs are efficient error detection codes that are able to detect :

 - all errors that affect an odd number of bits
 - all errors that affect a sequence of bits which is shorter than the length of the CRC

 Carry experiments with one implementation of CRC-32 to verify that this is indeed the case.

3. Checksums and CRCs should not be confused with secure hash functions such as MD5 defined in :rfc:`1321` or SHA-1 described in :rfc:`4634`. Secure hash functions are used to ensure that files or sometimes packets/segments have not been modified. Secure hash functions aim at detecting malicious changes while checksums and CRCs only detect random transmission errors. Perform some experiments with hash functions such as those defined in the http://docs.python.org/library/hashlib.html python hashlib module to verify that this is indeed the case.


 
.. how to compute the delay, try with ping to see how often it changes with a remote site

.. 7. On Unix hosts, the :manpage:`ping(8)` command can be used to measure the round-trip-time to send and receive packets from a remote host. Use :manpage:`ping(8)` to measure the round-trip to a remote host. Chose a remote destination which is far from your current location, e.g. a small web server in a distant country. There are implementations of ping in various languages, see e.g. http://pypi.python.org/pypi/ping/0.2 for a python_ implementation of ''ping''



.. what are the factors that affect the performance of the alternating bit protocol ?


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

.. 13. Amazon provides the `S3 storage service <https://s3.amazonaws.com/>`_ where companies and researchers can store lots of information and perform computations on the stored information. Amazon allows users to send files through the Internet, but also by sending hard-disks. Assume that a 1 Terabyte hard-disk can be delivered within 24 hours to Amazon by courier service. What is the minimum bandwidth required to match the bandwidth of this courier service ? 

.. 14. Several large data centers operators (e.g. `Microsoft <http://www.microsoft.com/showcase/en/us/details/bafe5c0f-8651-4609-8c71-24c733ce628b>`_ and `google <http://www.youtube.com/watch?v=zRwPSFpLX8I>`_) have announced that they install servers as containers with each container hosting up to 2000 servers. Assuming a container with 2000 servers and each storing 500 GBytes of data, what is the time required to move all the data stored in one container over one 10 Gbps link ? What is the bandwidth of a truck that needs 10 hours to move one container from one data center to another. 



.. include:: /links.rst
