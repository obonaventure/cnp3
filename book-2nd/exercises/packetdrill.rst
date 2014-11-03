.. Copyright |copy| 2014 by Olivier Bonaventure, Arnaud Schils 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_




Injecting TCP segments
----------------------

:task_id: packetdrill

Packet capture tools like tcpdump_ and Wireshark_ are very useful to observe the segments that transport protocols exchange. They are also very useful to understand and debug network problems as we'll discuss in subsequent labs. TCP is a complex protocol that has evolved a lot since its first specification :rfc:`793`. TCP includes a large number of heuristics that influence the reaction of a TCP implementation to various types of events. A TCP implementation interacts with the application through the ``socket`` API. Recently, several researchers from Google proposed packetdrill_ [CCB+2013]_.  packetdrill_ is a TCP test suite that was designed to develop unit tests to verify the correct operation of a TCP implementation. A detailed description of packetdrill_ in [CCB+2013]_. packetdrill_ uses a syntax which is a mix between the C language and the tcpdump_ syntax. To understand the operation of packetdrill_, it is useful to study several examples in details. The TCP implementation in the Linux kernel supports all the recent TCP extensions to improve its performance. For pedagogical reasons, we disable [#fsysctl]_ most of these extensions to use a simple TCP stack.

Let us start with a very simple example that uses packetdrill_ to open a TCP connection on a server running on the Linux kernel. A packetdrill_ script is a sequence of lines that are executed one after the other. Each of these lines can specify :

 - packetdrill_ executes a system call and verifies its return value
 - packetdrill_ injects [#ftcpdump_pdrill]_ a packet in the instrumented Linux kernel as if it were received from the network
 - packetdrill_ compares a packet transmitted by the instrumented Linux kernel with the packet that the script expects

Each line starts with a `timing` parameter that indicates at what time the event specified on this line should happen. packetdrill_ supports absolute and relative timings. An absolute timing is simply a number that indicates the delay in seconds between the start of the script and the event. A relative timing is indicated by using ``+``  followed by a number. This number is then the delay in seconds between the previous event and the current line. Additional informations may be found in [CCB+2013]_. 

For this first example, we will program packetdrill_ to behave as a client that attempts to create a connection. The first step is thus to prepare a :manpage:`socket` that can be used to accept this connection. This socket can be created by using the four system calls below.

.. code-block:: console

   // create a TCP socket. Since stdin, stdout and stderr are already defined,
   // the kernel will assign file descriptor 3 to this socket
   // 0 is the absolute time at which the socket is created
   0   socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
   // Enable reuse of addresses
   +0  setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
   // binds the created socket to the available addresses
   +0  bind(3, ..., ...) = 0
   // configure the socket to accept incoming connections
   +0  listen(3, 1) = 0


At this point, the socket is ready to accept incoming TCP connections. packetdrill_ needs to inject a TCP segment in the instrumented Linux stack. This can be done with the line below.

.. code-block:: console

   +0  < S 0:0(0) win 1000 <mss 1000>

packetdrill_ uses a syntax that is very close to the tcpdump_ syntax. The ``+0`` timing indicates that the line is executed immediately after the previous event. The ``<`` sign indicates that packetdrill_ injects a TCP segment and the ``S`` character indicates that the ``SYN`` flag must be set. Like tcpdump_, packetdrill_ uses sequence numbers that are relative to initial sequence number. The three numbers that follow are the sequence number of the first byte of the payload of the segment (``0``), the sequence number of the last byte of the payload of the segment (``0`` after the semi-column) and the length of the payload (``0`` between brackets) of the ``SYN`` segment. This segment does not contain a valid acknowledgement but advertises a window of 1000 bytes. All ``SYN`` segments must also include the ``MSS`` option. In this case, we set the MSS to 1000 bytes. The next line of the packetdrill_ script is to verify the reply sent by the instrumented Linux kernel.

.. code-block:: console

   +0  > S. 0:0(0) ack 1 <...>


This TCP segment is sent immediately by the stack. The ``SYN`` flag is set and the dot next to the ``S`` character indicates that the ACK flag is also set. The SYN+ACK segment does not contain any data but its acknowledgement number is set to 1 (relative to the initial sequence number). The packetdrill_ script does not match the window size advertised in the TCP segment nor the TCP options (``<...>``). 


The third segment of the three-way handshake is sent by packetdrill_ after a delay of 0.1 seconds. The connection is now established and the accept system call will succeed.

.. code-block:: console

   +.1 < . 1:1(0) ack 1 win 1000
   +0  accept(3, ..., ...) = 4

The :manpage:`accept` system call returns a new file descriptor, in this case value ``4``. At this point, packetdrill_ can write data on the socket or inject packets. 

.. code-block:: console

   +0 write(4, ..., 10)=10
   +0 > P. 1:11(10) ack 1
   +.1 < . 1:1(0) ack 11 win 1000

packetdrill_ writes 10 bytes of data through the :manpage:`write` system call. The stack immediately sends these 10 bytes inside a segment whose ``Push`` flag is set [#fpush]_. The payload starts at sequence number ``1`` and ends at sequence number ``10``. packetdrill_ replies by injecting an acknowledgement for the entire data after 100 milliseconds.

packetdrill_ can also inject data that will be read by the stack as shown by the lines below.

.. code-block:: console

   +.1 < P. 1:3(2) ack 11 win 4000
   +0 > . 11:11(0) ack 3
   +.2 read(4,...,1000)=2

In the example above, packetdrill_ injects a segment containing two bytes. This segment is acknowledged and after that the :manpage:`read` system call succeeds and reads the available data with a buffer of 1000 bytes. It returns the amount of read bytes, i.e. ``2``.

We can now close the connection gracefully. Let us first issue inject a segment with the ``FIN` flag set.

.. code-block:: console
 
   //Packetdrill closes connection gracefully
   +0 < F. 3:3(0) ack 11 win 4000
   +0 > . 11:11(0) ack 4

packetdrill_ injects the ``FIN`` segment and the instrumented kernel returns an acknowledgement. If packetdrill_ issues the :manpage:`close` system call, the kernel will send a ``FIN`` segment to terminate the connection. packetdrill_ injects an acknowledgement to confirm the end of the connection.

.. code-block:: console

   +0 close(4) = 0
   +0 > F. 11:11(0) ack 4
   +0 < . 4:4(0) ack 12 win 4000


The complete packetdrill_ script is available from :download:`exercices/packetdrill_scripts/connect.pkt`


packetdrill_ can be used to explore in details the operation of the Linux TCP implementation to understand how it reacts to system calls and the reception of packets.



1. A first interesting point to explore is how TCP reacts with out-of-order segments. Consider the packetdrill_ script shown below :

.. code-block:: console

   0   socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
   +0  setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
   +0  bind(3, ..., ...) = 0
   +0  listen(3, 1) = 0

   //TCP three-way handshake
   +0  < S 0:0(0) win 4000 <mss 1000>
   +0  > S. 0:0(0) ack 1 <...>
   +.1 < . 1:1(0) ack 1 win 1000
   +0  accept(3, ..., ...) = 4

   +0 < P. 1:201(200) win 4000
   +0 > . 1:1(0) ack 201

   +0 < P. 231:251(20) win 4000
   +0 > . 1:1(0) ack 201


.. question:: oosegments
   :nb_prop: 3
   :nb_pos: 1

   a. At this step of the script, which would be the result of the read system call ?

   .. positive:: 

      .. code-block:: console
 
         +0 read(4, ..., 250) = 200
   
      .. comment:: Indeed, there are only 200 bytes in sequence waiting in the receiver buffer.

   .. positive:: 

      .. code-block:: console

         +0 read(4, ..., 500) = 200

      .. comment:: Indeed, there are only 200 bytes in sequence waiting in the receiver buffer.

   .. negative:: 

      .. code-block:: console

         +0 read(4, ..., 500) = 250

      .. comment:: Although 250 bytes were sent, only 200 of them have been received in sequence. 

   .. negative:: 

      .. code-block:: console

         +0 read(4, ..., 500) = 250


      .. comment:: Although 250 bytes were sent, only 200 of them have been received in sequence. 

   .. negative::

      .. code-block:: console

         +0 read(4, ..., 500) = 201

      .. comment:: Although 250 bytes were sent, only 200 of them have been received in sequence. 


b. packetdrill_ now issues a FIN segment to indicate that all data has been transmitted. 

   .. code-block:: console 

      +0 < F. 251:251(0) win 257 

.. question:: oosegments2 
   :nb_prop: 3 
   :nb_pos: 1 

   What is the acknowledgement that will be returned by the TCP stack ?

   .. positive::

      .. code-block:: console

         +0 > . 1:1(0) ack 201

      .. comment:: Indeed, this is the last byte that has been received in sequence. 

   .. negative:: 

      .. code-block:: console

         +0 > F. 1:1(0) ack 201

      .. comment:: The FIN flag will only be set if the :manpage:`close` system call has been issued, which is not the case here. 

   .. negative::

      .. code-block:: console

         +0 > . 1:1(0) ack 251

      .. comment:: This segment is incorrect. It indicates that all data up to and including sequence number 250 has been received correctly. This is not true since the bytes 201-230 have not yet been received. 

   .. negative::

      .. code-block:: console

         +0 > F. 1:1(0) ack 251

      .. comment:: This segment is incorrect. It indicates that all data up to and including sequence number 250 has been received correctly. This is not true since the bytes 201-230 have not yet been received. Furthermore, the FIN flag can only be used once the :manpage:`close` system call has been issued. 



.. question:: oosegments3 
   :nb_prop: 3 
   :nb_pos: 1 

   c. At this stage, what are the packets that need to be exchanged to allow the read system call on the kernel to succeed ? 

   .. positive:: 

      .. code-block:: console 

          +0 < P. 201:231(30) win 4000 
	  +0 > . 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

   .. positive:: 

      .. code-block:: console 

          +0 < . 201:231(30) win 4000 
	  +0 > . 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

   .. negative:: 

      .. code-block:: console 

          +0 < . 200:250(50) win 4000 
	  +0 > . 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

      .. comment:: Here, one byte is still missing. 


   .. negative:: 

      .. code-block:: console 

          +0 < P. 1:201(200) win 4000 
	  +0 > . 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

      .. comment:: Here, thirty bytes are still missing. 


   .. negative:: 

      .. code-block:: console 

          +0 < P. 1:250(249) win 4000 
	  +0 > . 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

      .. comment:: Here, one byte is still missing. 


   .. negative:: 

      .. code-block:: console 

          +0 < P. 201:231(30) win 4000 
	  +0 > F. 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

      .. comment:: The FIN flag is only set by the kernel in outgoing packets after the :manpage:`close` system call. 

   .. negative:: 

      .. code-block:: console 

          +0 < . 201:231(30) win 4000 
	  +0 > . 1:1(0) ack 252 
	  +0 read(4, ..., 250) = 250 

      .. comment:: The FIN flag is only set by the kernel in outgoing packets after the :manpage:`close` system call. 

2. A second topic that we can explore with packetdrill_ are the retransmissions when there are packet losses. TCP uses a mix of go-back-n and selective repeat to retransmit the missing segments. When the retransmission timer expires, it retransmits one segment due to the congestion control scheme, see below :

.. code-block:: console

   0   socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
   +0  setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
   +0  bind(3, ..., ...) = 0
   +0  listen(3, 1) = 0

   +0  < S 0:0(0) win 4000 <mss 1000>
   +0  > S. 0:0(0) ack 1 <...>
   +.1 < . 1:1(0) ack 1 win 4000
   +0  accept(3, ..., ...) = 4

   +0  write(4, ..., 1000) = 1000
   +0  > P. 1:1001(1000) ack 1
   +.1 < . 1:1(0) ack 1001 win 4000

   +0  write(4, ..., 2000) = 2000
   +0  > . 1001:2001(1000) ack 1
   +0  > P. 2001:3001(1000) ack 1

   // timeout

   +0.3  > . 1001:2001(1000) ack 1
   +0.6  > . 1001:2001(1000) ack 1
   +1.2  > . 1001:2001(1000) ack 1

Note that TCP applies an exponential backoff to the retransmission timer that doubles after each expiration.


3. The TCP state machine allows two hosts to simultaneously open a TCP connection. In this case, both the clients and the server start the connection by sending a SYN segment. The following packetdrill_ script demonstrates this simultaneous establishment of a connection.

.. code-block:: console

   +0   socket(..., SOCK_STREAM, IPPROTO_TCP) = 3
   +0 fcntl(3, F_GETFL) = 0x2 (flags O_RDWR)
   +0 fcntl(3, F_SETFL, O_RDWR|O_NONBLOCK) = 0

   // Establish connection
   +0 connect(3, ..., ...) = -1 EINPROGRESS (Operation now in progress)
   +0 > S 0:0(0) <...>
   +0 < S 0:0(0) win 5792 <mss 1000>
   +0 > S. 0:0(0) ack 1 <...>
   +0 < . 1:1(0) ack 1 win 5792

   +0 < F. 1:1(0) ack 1 win 5792
   +0 > . 1:1(0) ack 2

   //Kernel closes connection gracefully
   +0 close(3) = 0
   +0 > F. 1:1(0) ack 2 
   +0 < . 2:2(0) ack 2 win 5792


4. A TCP connection can be terminated gracefully by exchaning FIN segments. In practice, since these segments can be exchanged at any time, there are multiple ways to express a graceful connection release in packetdrill_ 

Consider a TCP connection where no data has been exchanged that needs to be gracefully closed. The connection starts as follows :

.. code-block:: console 

   0   socket(..., SOCK_STREAM, IPPROTO_TCP) = 3 
   +0  setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0 
   +0  bind(3, ..., ...) = 0 
   +0  listen(3, 1) = 0 
   +0  < S 0:0(0) win 1000 
   +0  > S. 0:0(0) ack 1 <...>
   +.1 < . 1:1(0) ack 1 win 1000 
   +0  accept(3, ..., ...) = 4 



.. question:: release 
   :nb_pos: 3 
   :nb_prop: 4 

   Select all the packetdrill_ scripts below that correspond to a correct graceful release of this connection.

   .. positive::

      .. code-block:: console 

         +0 close(4) = 0 
         +0 < F. 1:1(0) ack 1 win 257 
         +0 > F. 1:1(0) ack 1 
         +0 > . 2:2(0) ack 2 
         +0 < . 2:2(0) ack 2 win 257 


   .. positive::

      .. code-block:: console 

         +0 close(4) = 0 
         +0 > F. 1:1(0) ack 1 
         +0 < . 2:2(0) ack 2 win 257 
         +0 < F. 1:1(0) ack 2 win 257 
         +0 > . 2:2(0) ack 2 

   .. positive::

      .. code-block:: console 

          +0 < F. 1:1(0) ack 1 win 257 
          +0 close(4) = 0 
          +0 > F. 1:1(0) ack 2 
          +0 < . 2:2(0) ack 2 win 257 

   .. positive::

      .. code-block:: console 

          +0 close(4) = 0 
          +0 < F. 1:1(0) ack 1 win 257 
          +0 > F. 1:1(0) ack 1 
          +0 > . 2:2(0) ack 2 
          +0 < . 2:2(0) ack 2 win 257 


   .. negative::

      .. code-block:: console 

         +0 > F. 1:1(0) ack 1 
         +0 close(4) = 0 
         +0 < F. 1:1(0) ack 1 win 257 
         +0 > . 2:2(0) ack 2 
         +0 < . 2:2(0) ack 2 win 257 

      .. comment:: The server cannot send a FIN segment before the call to close. 

   .. positive::

      .. code-block:: console 

         +0 close(4) = 0 
         +0 > F. 1:1(0) ack 1 
         +0 < F. 1:1(0) ack 2 win 257 
         +0 > . 2:2(0) ack 2 


   .. negative::

      .. code-block:: console 

         +0 close(4) = 0 
         +0 < F. 1:1(0) ack 1 win 257 
         +0 > F. 1:1(0) ack 1 
         +0 < . 2:2(0) ack 2 win 257 

      .. comment:: This connection has not been completely released in the incoming direction (the first segment has not been acknowledged). 

   .. negative::

      .. code-block:: console 

          +0 < F. 1:1(0) ack 1 win 257 
          +0 close(4) = 0 
          +0 > F. 1:1(0) ack 1 
          +0 < . 2:2(0) ack 2 win 257 

      .. comment:: This connection has not been completely released in the incoming direction (the first segment has not been acknowledged). 

   .. negative::

      .. code-block:: console 

          +0 close(4) = 0 
          +0 < F. 1:1(0) ack 1 win 257 
          +0 > F. 1:1(0) ack 1 
          +0 > . 2:2(0) ack 1 
          +0 < . 2:2(0) ack 1 win 257 

      .. comment:: None of the FIN segments have been acknowledged in the above example. 


.. rubric:: Footnotes

.. [#fsysctl] On Linux, most of the parameters to tune the TCP stack are accessible via :manpage:`sysctl`. The :download:`exercices/packetdrill_scripts/sysctl-cnp3.conf` file contains all the sysctl variables that we change to disable these various TCP extensions.

.. [#ftcpdump_pdrill] By default, packetdrill_ uses port 8080 when creating TCP segments. You can thus capture the packets injected by packetdrill_ and the responses from the stack by using. 

   .. code-block:: console

      tcpdump -i any -n port 8080


.. [#fpush] The `Push` flag is one of the TCP flags defined in :rfc:`793`. TCP stacks usually set this flag when transmitting a segment that empties the send buffer. This is the reason why we observe this push flag in our example.
 
.. include:: /links.rst
