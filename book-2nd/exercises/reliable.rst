.. Copyright |copy| 2013, 2014 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


*****************
Reliable transfer
*****************


Open questions
==============

1. Consider a `b` bits per second link between two hosts that has a propagation delay of `t` seconds. Derive a formula that computes the time elapsed between the transmission of the first bit of a `d` bytes segment from a sending host and the reception of the last bit of this segment on the receiving host.

2. Consider two hosts connected by a physical cable. The two hosts are separated by a distance of 1000 kilometers and the propagation delay is 5 microseconds per kilometer. The bandwidth of the physical cable is 1 Mbps. If the data frames have a length of 1000 bits and the acknowledgements a length of 40 bits, what is the exact value of the round-trip-time, i.e. the delay in seconds between the transmission of the first bit of a data frame and the reception of the last bit of the acknowledgement ? To compute this delay, you can assume that the receiver needs one millisecond to verify a received frame and prepare the corresponding acknowledgement.

3. Transmission links have sometimes different upstream and downstream bandwidths. A typical example are access networks that use ADSL (Assymetric Digital Subscriber Lines). Consider two hosts connected via an ADSL link having an upstream bandwidth of 1 Mbps and a downstream bandwidth of 50 Mbps. The propagation delay between the two hosts is 10 milliseconds. What is the maximum throughput, expressed in frames/second, that the alternating bit protocol can obtain on this link if each data frame has a length of 125 bytes and acknowledgements are 25 bytes long. Same question if the protocol is modified to support 1500 bytes long data frames.


4. How would you set the duration of the retransmission timer in the alternating bit protocol ?

 
5. A version of the Alternating Bit Protocol supporting variable length frames uses a header that contains the following fields :

     - a `number` (0 or 1)
     - a `length` field that indicates the length of the data 
     - a Cyclic Redundancy Check (`CRC`)
 
   To speedup the transmission of the frames, a student proposes to compute the CRC over the data part of the segment but not over the header. What do you think of this optimisation ?

6. Derive a mathematical expression that provides the `goodput`, i.e. the amount of payload bytes that have been transmitted during a period of time, achieved by the Alternating Bit Protocol assuming that :

      - Each frame contains `D` bytes of data and `c` bytes of control information
      - Each acknowledgement contains `c` bytes of control information
      - The bandwidth of the two directions of the link is set to `B` bits per second
      - The delay between the two hosts is `s` seconds in both directions
      - there are no transmission errors

7. Consider a go-back-n sender and a go-back receiver that are directly connected with a 10 Mbps link that has a propagation delay of 100 milliseconds. Assume that the retransmission timer is set to three seconds. If the window has a length of 4 segments, draw a time-sequence diagram showing the transmission of 10 segments (each segment contains 10000 bits):

 - when there are no losses
 - when the third and seventh segments are lost
 - when every second acknowledgement is discarded due to transmission errors

8. Same question when using selective repeat instead of go-back-n. Note that the answer is not necessarily the same.




Practice
========

Reliable protocols depend on error detection algorithms to detect transmission errors. The following questions will reinforce your understanding of these algorithms.

1. Reliable protocols rely on different types of checksums to verify whether frames have been affected by transmission errors. The most frequently used checksums are :

 - the Internet checksum used by UDP, TCP and other Internet protocols which is defined in :rfc:`1071` and implemented in various libraries. See e.g. http://ilab.cs.byu.edu/cs460/code/ftp/ichecksum.py for a python_ implementation
 - the 16 bits or the 32 bits Cyclical Redundancy Checks (CRC) that are often used on disks, in zip archives and in datalink layer protocols. See http://rosettacode.org/wiki/CRC-32 for CRC-32 implementations in various languages.
 - the Fletcher checksum [Fletcher1982]_, see http://drdobbs.com/database/184408761 for implementation details

 By using your knowledge of the Internet checksum, can you find a transmission error that will not be detected by this checksum ?

2. The Cyclic Redundancy Checks (CRCs) are efficient error detection codes that are able to detect :

 - all errors that affect an odd number of bits
 - all errors that affect a sequence of bits which is shorter than the length of the CRC

 Implement a small software that computes the CRC-32 for a text file. Then, modify the contents of the file to change an even number of bits or an odd number of bits inside the file. When modifying the file, remember that an ASCII file is composed of 8 bits characters that are encoded by using the ASCII table that you can find at : http://en.wikipedia.org/wiki/ASCII . You can also write a small program that produces binary files that are a small variation of each other.

3. Checksums and CRCs should not be confused with secure hash functions such as MD5 defined in :rfc:`1321` or SHA-1 described in :rfc:`4634`. Secure hash functions are used to ensure that files or sometimes packets/segments have not been modified. Secure hash functions aim at detecting malicious changes while checksums and CRCs only detect random transmission errors. Use the `shasum <http://linux.die.net/man/1/shasum>`_ or `md5sum <http://linux.die.net/man/1/md5sum>`_ programs on Linux to perform the same tests as above.



Discussion questions
====================


1. Consider two high-end servers connected back-to-back by using a 10 Gbps interface. If the delay between the two servers is one millisecond, what is the throughput that can be achieved by a reliable protocol that is using 10,000 bits frames and a window of

 - one frame
 - ten frames
 - hundred frames

2. Is it possible for a go-back-n receiver to inter-operate with a selective-repeat sender ? Justify your answer.

3. Is it possible for a selective-repeat receiver to inter-operate with a go-back-n sender ? Justify your answer.

.. 4. The go-back-n and selective repeat mechanisms that are described in the book exclusively rely on cumulative acknowledgements. This implies that a receiver always returns to the sender information about the last frame that was received in-sequence. If there are frequent losses, a selective repeat receiver could return several times the same cumulative acknowledgment. Can you think of other types of acknowledgements that could be used by a selective repeat receiver to provide additional information about the out-of-sequence frames that it has received. Design such acknowledgements and explain how the sender should react upon reception of this information. 

4. A go-back-n receiver has sent :math:`2^n` data segments. All the segments have been received correctly and in-order by the receiver, but all the returned acknowledgements have been lost. Show by using a time sequence diagram (e.g. by considering a window of four segments) what happens in this case. Can you fix the problem on the go-back-n sender ?

5. Same question as above, but assume now that both the sender and the receiver implement selective repeat. Note that the answer can be different from the above question.



.. include:: /links.rst
