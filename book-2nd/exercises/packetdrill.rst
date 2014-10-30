.. Copyright |copy| 2014 by Arnaud Schils, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


Injecting TCP segments
----------------------

Packet capture tools like tcpdump_ and Wireshark_ are very useful to observe the segments that transport protocols exchange. They are also very useful to understand and debug network problems as we'll discuss in subsequent labs. TCP is a complex protocol that has evolved a lot since its first specification :rfc:`793`. TCP includes a large number of heuristics that influence the reaction of a TCP implementation to various types of events. A TCP implementation interacts with the application through the ``socket`` API. Recently, several researchers from Google proposed packetdrill_ [CCB+2013]_.  packetdrill_ is a TCP test suite that was designed to develop unit tests to verify the correct operation of a TCP implementation. packetdrill_ interacts with the Linux TCP implementation in two ways :

 - packetdrill_ can issue any system call through the socket interface
 - packetdrill_ can inject any segment in the TCP stack as if it was received from a remote host

A detailed description of packetdrill_ and one example can be found in [CCB+2013]_. packetdrill_ uses a syntax which is a mix between the C language and the tcpdump_syntax. The following example illustrates the three-way handshake with packetdrill_

.. code-block:: console

   // create socket and listen for incoming connections
   0.000 socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
   0.000 setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
   0.000 bind(3, ..., ...) = 0
   0.000 listen(3, 1) = 0

   // inject the first SYN segment in the TCP stack at time 0.200
   // MSS is set to 1000 to simplify computation

   0.200 < S 0:0(0) win 4096 <mss 1000>
   // We expect a SYN+ACK with the default Linux MSS
   0.200 > S. 0:0(0) ack 1 <mss 1460>
   // We reply by injecting a valid ack at time 0.300
   0.300 < . 1:1(0) ack 1 win 4096
   // At that time, the connection is established
   0.300 accept(3, ..., ...) = 4

   // Receive first segment
   0.510 < . 1:1001(1000) ack 1 win 4096

   // Expects one ack in response
   0.510 > . 1:1(0) ack 1001

   // Application reads received data
   0.600 read(4, ..., 1000) = 1000

   // Application writes 1000 bytes
   0.650 write(4, ..., 1000) = 1000
   // Expects that it will send one segment
   0.650 > P. 1:1001(1000) ack 1001

   // We reply with an acknowledgement after 50 msec
   0.700 < . 1001:1001(0) ack 1001 win 257

   // We inject a RST to close connection
   0.701 < R. 1001:1001(0) ack 1001 win 4096


1. To show your understanding of the TCP state machine, use packetdrill_ to develop one script that demonstrates the operation of TCP. Inside each group, ensure that there is at least one script that demonstrates :

 - the simultaneous establishment of a TCP connection when the client and the server generate a SYN almost at the same time
 - the ability of TCP to accept out-of-order segments
 - the Nagle algorithm
 - the operation of TCP when the server announces a very small window
 - the support of delayed acknowledgements (i.e. an acknowledgement is sent for every second segment or after 50 msec of delay when there is no reordering)  
 - the TCP fast retransmit
 - different paths through the TCP state machine when closing a TCP connection (e.g. client sends FIN first, server sends FIN first, client and server send FIN at the same time, ...)
 - the negotiation of the MSS during the three-way handshake
 - the support of the TCP timestamp option
 - the reaction of TCP when out-of-window data is received
 - the reaction of TCP upon reception of a SYN+ACK segment when a connection has not yet been established



.. include:: /links.rst
