Go-back-n and selective repeat
==============================

Go-back-n and selective repeat are the basic mechanisms used in
reliable window-based transport-layer protocols. These questions cover these two mechanisms in details. You do not need to upload the time sequence diagrams on the svn repository, bring them with you on paper. 

#. Amazon provides the S3 storage service (https://s3.amazonaws.com/) where companies and researchers can store lots of information and perform computations on the stored information. Amazon allows users to send files through the Internet, but also by sending hard-disks. Assume that a 1 Terabyte hard-disk can be delivered within 24 hours to Amazon by courier service. What is the minimum bandwidth required to match the bandwidth of this courier service ? 

#. What are the techniques used by a go-back-n sender to recover from :

 - transmission errors
 - losses of data segments
 - losses of acknowledgements


#. Consider a go-back-n sender and a go-back receiver that are directly connected. Assume that the one-way delay between the two hosts is one second and the retransmission timer is set to three seconds. If each segment takes 100 milliseconds to reach the destination and the window has a length of 4 segments, draw a time-sequence diagram showing the transmission of 10 segments :

 - when there are no losses
 - when the third and seventh segments are lost
 - when the second, fourth, sixth, eighth, ... acknowledgements are lost
 - when the third and fourth data segments are reordered (i.e. the fourth arrives before the third)

#. Same question when using selective repeat instead of go-back-n. Note that the answer is not necessarily the same.

#. Consider a `b` bits per second link between two hosts that has a propagation delay of `t` seconds. Derive a formula that computes the time elapsed between the transmission of the first bit of a `d` bytes segment from and sending host and the reception of the last bit of this segment on the receiving host.


#. Consider two high-end servers connected back-to-back by using a 10 Gbps interface. If the delay between the two servers is one millisecond, what is the throughput that can be achieved by a transport protocol that is using 10,000 bits segments and a window of

 - one segment
 - ten segments
 - hundred segments

#. Consider two servers are directly connected by using a `b` bits per second link with a round-trip-time of `r` seconds. The two servers are using a transport protocol that sends segments containing `s` bytes and acknowledgements composed of `a` bytes. Can you derive a formula that computes the smallest window (measured in segments) that is required to ensure that the servers will be able to completely utilise the link ?

#. Same question as above if the two servers are connected through and asymmetrical link that transmits `bu` bits per second in the upstream direction and `bd` bits per second in the downstream direction.

#. The Trivial File Transfer Protocol is a very simple file transfer protocol that is often used by diskless hosts when booting from a server. Read the TFTP specification in :rfc:`1350` and explain how TFTP recovers from transmission errors and losses.

#. Is it possible for a go-back-n receiver to interoperate with a selective-repeat sender ? Justify your answer.

#. Is it possible for a selective-repeat receiver to interoperate with a go-back-n sender ? Justify your answer.

#. The go-back-n and selective repeat mechanisms that are described in the book exclusively rely on cumulative acknowledgements. This implies that a receiver always returns to the sender information about the last segment that was received in-sequence. If there are frequent losses or reordering, a selective repeat receiver could return several times the same cumulative acknowledgment. Design an additional type of acknowledgement that would provide more information to the sender aboutCan you think of other types of acknowledgements that could be used by a selective repeat receiver to provide additional information about the out-of-sequence segments that it has received. Explain how the sender should react upon reception of this information. 

#. The `goodput` achieved by a transport protocol is usually defined as the number of application layer bytes that are exchanged per unit of time. What are the factors that can influence the `goodput` achieved by a given transport protocol ? 

#. The Transmission Control Protocol (TCP) attaches a 40 bytes header to each segment sent. Assuming an infinite window and no losses nor transmission errors, derive a formula that computes the maximum TCP goodput in function of the size of the segments that are sent.

#. A go-back-n sender uses a window size encoded in a `n` bits field. How many segments can it send without receiving an acknowledgement ?

#. Consider the following situation. A go-back-n receiver has sent a full window of data segments. All the segments have been received correctly and in-order by the receiver, but all the returned acknowledgements have been lost. Show by using a time sequence diagram (e.g. by considering a window of four segments) what happens in this case. Can you fix the problem on the go-back-n sender ?

#. Same question as above, but assume now that both the sender and the receiver implement selective repeat. Note the the answer will be different from the above question.

#. Explain under which circumstances a transport entity could advertise a window of 0 segments ?

#. 127.0.0.1 ? ::1 ?

#. socket tcp, see Damien

#. dns resolution with sockets ? try v4 and v6 ?

.. include:: ../../book/links.rst


..
  Additional questions for the students

  Explain to the other members of the group the operation of your implementation :
  describe state variables
  describe datastructure used to implement the sending buffer

  As exemple, consider the case where 4 segments (NBITS=4, send 14,15,0,1) are sent and only OK0 is received. Explain in details what happens in this case

  Discuss what should be done to support selective repeat on the receiver and the transmitter side of your implementation

  Issues to be checked in the students's implementation
  - window : how do they check whether the window is full
  - processing of the sequence number (acks, advance of the sequence number, ...)
  - how to store the transmitted segments and their sequence number
  - retransmission : in which order are the retransmitted segments sent ?
