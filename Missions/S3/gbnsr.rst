Go-back-n and selective repeat
==============================

Go-back-n and selective repeat are the basic mechanisms used in
reliable window-based transport-layer protocols. These questions cover these two mechanisms in details. You do not need to upload the time sequence diagrams on the svn repository, bring them with you on paper. 

1. Amazon provides the `S3 storage service <https://s3.amazonaws.com/>`_ where companies and researchers can store lots of information and perform computations on the stored information. Amazon allows users to send files through the Internet, but also by sending hard-disks. Assume that a 1 Terabyte hard-disk can be delivered within 24 hours to Amazon by courier service. What is the minimum bandwidth required to match the bandwidth of this courier service ? 

2. Several large datacenters operators (e.g. `Microsoft <http://www.microsoft.com/showcase/en/us/details/bafe5c0f-8651-4609-8c71-24c733ce628b>`_ and `google <http://www.youtube.com/watch?v=zRwPSFpLX8I>`_) have announced that they install servers as containers with each container hosting up to 2000 servers. Assuming a container with 2000 servers and each storing 500 GBytes of data, what is the time required to move all the data stored in one container over one 10 Gbps link ? What is the bandwidth of a truck that needs 10 hours to move one container from one datacenter to another. 

3. What are the techniques used by a go-back-n sender to recover from :

 - transmission errors
 - losses of data segments
 - losses of acknowledgements

4. Consider a `b` bits per second link between two hosts that has a propagation delay of `t` seconds. Derive a formula that computes the time elapsed between the transmission of the first bit of a `d` bytes segment from a sending host and the reception of the last bit of this segment on the receiving host.

5. Consider a go-back-n sender and a go-back receiver that are directly connected with a 10 Mbps link that has a propagation delay of 100 milliseconds. Assume that the retransmission timer is set to three seconds. If the window has a length of 4 segments, draw a time-sequence diagram showing the transmission of 10 segments (each segment contains 10000 bits):

 - when there are no losses
 - when the third and seventh segments are lost
 - when the second, fourth, sixth, eighth, ... acknowledgements are lost
 - when the third and fourth data segments are reordered (i.e. the fourth arrives before the third)

6. Same question when using selective repeat instead of go-back-n. Note that the answer is not necessarily the same.

7. Consider two high-end servers connected back-to-back by using a 10 Gbps interface. If the delay between the two servers is one millisecond, what is the throughput that can be achieved by a transport protocol that is using 10,000 bits segments and a window of

 - one segment
 - ten segments
 - hundred segments

8. Consider two servers are directly connected by using a `b` bits per second link with a round-trip-time of `r` seconds. The two servers are using a transport protocol that sends segments containing `s` bytes and acknowledgements composed of `a` bytes. Can you derive a formula that computes the smallest window (measured in segments) that is required to ensure that the servers will be able to completely utilise the link ?

9. Same question as above if the two servers are connected through an asymmetrical link that transmits `bu` bits per second in the direction used to send data segments and `bd` bits per second in the direction used to send acknowledgements.

10. The Trivial File Transfer Protocol is a very simple file transfer protocol that is often used by diskless hosts when booting from a server. Read the TFTP specification in :rfc:`1350` and explain how TFTP recovers from transmission errors and losses.

11. Is it possible for a go-back-n receiver to interoperate with a selective-repeat sender ? Justify your answer.

12. Is it possible for a selective-repeat receiver to interoperate with a go-back-n sender ? Justify your answer.

13. The go-back-n and selective repeat mechanisms that are described in the book exclusively rely on cumulative acknowledgements. This implies that a receiver always returns to the sender information about the last segment that was received in-sequence. If there are frequent losses or reordering, a selective repeat receiver could return several times the same cumulative acknowledgment. Can you think of other types of acknowledgements that could be used by a selective repeat receiver to provide additional information about the out-of-sequence segments that it has received. Design such acknowledgements and explain how the sender should react upon reception of this information. 

14. The `goodput` achieved by a transport protocol is usually defined as the number of application layer bytes that are exchanged per unit of time. What are the factors that can influence the `goodput` achieved by a given transport protocol ? 

15. The Transmission Control Protocol (TCP) attaches a 40 bytes header to each segment sent. Assuming an infinite window and no losses nor transmission errors, derive a formula that computes the maximum TCP goodput in function of the size of the segments that are sent.

16. A go-back-n sender uses a window size encoded in a `n` bits field. How many segments can it send without receiving an acknowledgement ?

17. Consider the following situation. A go-back-n receiver has sent a full window of data segments. All the segments have been received correctly and in-order by the receiver, but all the returned acknowledgements have been lost. Show by using a time sequence diagram (e.g. by considering a window of four segments) what happens in this case. Can you fix the problem on the go-back-n sender ?

18. Same question as above, but assume now that both the sender and the receiver implement selective repeat. Note the the answer will be different from the above question.

19. Consider a transport that supports window of one hundred 1250 Bytes segments. What is the maximum bandwidth that this protocol can achieve if the round-trip-time is set to one second ? What happens if, instead of advertising a window of one hundred segments, the receiver decides to advertise a window of 10 segments ?

20. Explain under which circumstances a transport entity could advertise a window of 0 segments ?

21. The socket library is also used to develop applications above the reliable bytestream service provided by TCP. We have installed on the `sirius` server a simple server that provides a simple client-server service. The service operates as follows :

 - the server listens on port `21410` for a TCP connection
 - upon arrival of a TCP connection, the server sends an integer by using the following TLV format :
   
    - the first byte indicates the type of information (1 for ASCII, 2 for boolean)
    - the second and third bytes indicate the length of the information (in bytes)
    - An ASCII TLV has a variable length and the next bytes contain one ASCII charater per byte. A boolean TLV has a length of one byte. The byte is set to `00000000b` for `true` and `00000001b` for false. 
 - the client replies by sending the received integer encoded as a 32 bits integer in `network byte order`
 - the server returns a TLV containing `true` if the integer was correct and a TLV containing `false` otherwise and closes the TCP connection

 Each group of two students must implement a client to interact with this server in C, Java or python. 


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
