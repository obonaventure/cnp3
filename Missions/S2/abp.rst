The Alternating Bit Protocol
============================

The objective of this set of exercises is to better understand the
basic mechanisms of the alternating bit protocol and the utilisation of the 
socket interface with the connectionless transport service. 

.# Consider the Alternating Bit Protocol as described in the book.
 - How does the protocol recover from the loss of a data segment ? 
 - How does the protocol recovers from the loss of an acknowledgement ?

.# A student proposed to optimise the Alternating Bit Protocol by adding a negative acknowledgment, i.e. the receiver sends a `NAK` control segment when it receives a corrupted data segment. What kind of information should be placed in this control segment and how should the sender react when receiving such as `NAK` ?

.# Transport protocols rely on different types of checksums to verify whether segments have been affected by transmission errors. The most frequently used checksums are :

 - the Internet checksum used by UDP, TCP and other Internet protocols which is defined in :rfc:`1071` and implemented in various modules, e.g. http://ilab.cs.byu.edu/cs460/code/ftp/ichecksum.py for a python implementation
 - the 16 bits or the 32 bits Cyclical Redundancy Checks (CRC) that are often used on disks, in zip archives and in datalink layer protocols. See http://docs.python.org/library/binascii.html for a python module that contains the 32 bits CRC
 - the Alder checksum defined in :rfc:`2920` for the SCTP protocol but replaced by a CRC later
 - the Fletcher checksum 

By using your knowledge of the Internet checksum, can you find a transmission error that will not be detected by the Internet checksum ?

.# The CRCs are efficient error detection codes that are able to detect :
 - all errors that affect an odd number of bits
 - all errors that affect a string a bits which is shorter than the length of the CRC

 Experiment with one implementation of CRC-32 to verify that this is indeed the case

.# Checksums and CRCs should not be confused with secure hash functions such as MD5 defined in :rfc:`1321` or SHA-1 described in :rfc:`4634`. Secure hash functions are used to ensure that files or sometimes packets/segments have not been modified. Secure hash functions aim at detecting malicious changes while checksums and CRCs only detect random transmission errors. Perform some experiments with hash functions such as those defined in the http://docs.python.org/library/hashlib.html python hashlib module to verify that this is indeed the case.

.. Some questions about the checksum versus crc, discuss briefly hash


.. some question about whether the crc must cover the length or not

.# A version of the Alternating Bit Protocol supporting variable length segments uses a header that contains the following fields :
 - a number (0 or 1)
 - a length field that indicates the length of the data 
 - a CRC
 
 To speedup the transmission of the segments, a student proposes to compute the CRC over the data part of the segment but not over the header. What do you think of this optimisation ?
 

.. how to compute the delay, try with ping to see how often it changes with a remote site

.# On Unix hosts, the :manpage:`ping(8)` command can be used to measure the round-trip-time to send and receive packets from a remote host. Use :manpage:`ping(8)` to measure the round-trip to a remote host. Chose a remote destination which is far from your current location, e.g. a small web server in a distant country. There are implementations of ping in various languages, see e.g. http://pypi.python.org/pypi/ping/0.2 for a python implementation of ping


.# How would you set the retransmission timer if you were implementing the Alternating Bit Protocol to exchange files with a server such as the one that you measured above ?


.# What are the factors that affect the performance of the Alternating Bit Protocol ?

.. what are the factors that affect the performance of the alternating bit protocol ?

.# Links are often symmetrical, i.e. they offer the same bandwidth in both directions, but there are some asymmetrical link technologies. The most common example are the various types of ADSL and CATV technologies. Consider an implementation of the Alternating Bit Protocol that is used between two hosts that are directly connected by using an asymmetric link. Assume that a host is sending segments containing 10 bytes of control information and 90 bytes of data and that the acknowledgements are 10 bytes long. If the round-trip-time is negligible, what is the minimum bandwidth required on the return link to ensure that the transmission of acknowledgements is not a bottleneck ?

.# Derive a mathematical expression that provides the `goodput` achieved by the Alternating Bit Protocol assuming that :
 - Each segment contains `D` bytes of data and `c` bytes of control information
 - Each acknowledgement contains `c` bytes of control information
 - The bandwidth of the two directions of the link is set to `B` bits per second
 - The delay between the two hosts is `s` seconds in both directions

 The goodput is defined as the amount of SDUs (measured in bytes) that is successfully transferred during a period of time

.# The socket interface allows you to use the UDP protocol on a Unix host. UDP provides a connectionless unreliable service that in theory allows you to send SDUs of up to 64 KBytes. Implement a small UDP client and a small UDP server (in python, you can start from the example provided in http://docs.python.org/library/socket.html ) and run them on different workstations to determine experimentally the largest SDU that is supported by your language and OS. If possible, use different languages and Operating Systems in each group.

.. socket layer with UDP, what is the larget data that you can send by usinc C, Java or python, is it 64KBytes or less ?

.# By using the socket interface, implement on top of the connectionless unreliable service provided by UDP a simple  client that sends the following message :

::   
       0                   1                   2                   3  
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1  
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
      |   Bit flags   |         16 bits field         |       Zero    |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  
      |                  32 bits field	                              |   
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      | Type=1        |Len (8 bits) |   Character string ...          |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                    Character string (cont.)		      |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |   16 bits Internet checksum |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


In this message, the bit flags should be set to `01010011b`, the value of the 16 bits field must be the square root of the value contained in the 32 bits field, the character string must be an ASCII representation (without any trailing `\0`) of the number contained in the 32 bits character field.

Upon reception of such a message, the server verifies the value of the bit flags, the 16 bits integer, the 32 bits integer, the character string. If they all match and the Internet checksum is correct, it returns a SDU containing `11111111b`. Otherwise it returns `01010101b`

Inside each group, implement at least two different clients and two different servers. The clients and the servers must run on both the Linux workstations and the Sun server (sirius). Verify the interoperability of the clients and the servers inside the group. You can use C, Java or python to write these implementations.

.# Consider an Alternating Bit Protocol that is used over a link that suffers from deterministic errors. When the error ratio is set to :math:`\frac{1}{p}`, this means that :math:`p-1` bits are transmitted correctly and the :math:`p^{th}` bit is corrupted. Discuss the factors that affect the performance of the Alternating Bit Protocol over such a link.

.. what is the impact of the segment size when bit errors are random ? (assume regular errors for the computation, every n bits)

.. impact of the uplink bandwidth, what is the highest throughput achievable for a given uplink bandwidth

.. Compute a closed form expression for the goodput of the alternating bit protocol

.. What happens in the alternating bit protocol when acknowledgements are lost

.. Can we build an alternating bit protocol that does not use nak

.. implement a simple protocol over udp socket, check with virginie

server sur la sun et client sur linux
compile sur les deux et portable

2 langages différents + interop

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



.. include:: ../../book/links.rst


