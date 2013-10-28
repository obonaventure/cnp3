.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Experimenting with Internet transport protocols
===============================================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=6

Transport protocols play a very important role on today's Internet. Most applications interact directly with them to exchange data. In the previous lab, you have performed DNS queries using dig_. Each DNS request that you sent or reply that you received were placed inside UDP segments.

Packet trace analysis
---------------------

When debugging networking problems or to analyse performance problems, it is sometimes useful to capture the segments that are exchanged between two hosts and to analyse them.  

Several packet trace analysis tools are available, either as commercial or open-source tools. These tools are able to capture all the packets exchanged on a link. Of course, capturing packets require administrator privileges. They can also analyse the content of the captured packets and display information about them. The captured packets can be stored in a file for offline analysis.

tcpdump_ is probably one of the most well known packet capture software. It is able to both capture packets and display their content. tcpdump_ is a text-based tool that can display the value of the most important fields of the captured packets. Additional information about tcpdump_ may be found in :manpage:`tcpdump(1)`. 

.. todo: example plus simple


.. labo avec discard, chargen, telnet, time et autres protocols simples en UDPv6 et en TCP
.. montrer comment ces protocoles fonctionnent sur base de dumps TCP dumpe en mode normal et verbose avec les traces pcap correspondantes

The text below is an example of the output of tcpdump_ for all the TCP segments exchanged during the download of a short webpage over HTTP.

.. code-block:: console

11:58:54.207193 IP6 2001:db8:b0:15:da:b055:0:2.52305 > 2001:db8:be:600d::2.80: Flags [S], seq 544531601, win 2880, options [mss 1440], length 0
11:58:54.207628 IP6 2001:db8:be:600d::2.80 > 2001:db8:b0:15:da:b055:0:2.52305: Flags [S.], seq 1907676151, ack 544531602, win 14400, options [mss 1440], length 0
11:58:54.208344 IP6 2001:db8:b0:15:da:b055:0:2.52305 > 2001:db8:be:600d::2.80: Flags [.], ack 1, win 2880, length 0
11:58:54.208360 IP6 2001:db8:b0:15:da:b055:0:2.52305 > 2001:db8:be:600d::2.80: Flags [P.], seq 1:110, ack 1, win 2880, length 109
11:58:54.208750 IP6 2001:db8:be:600d::2.80 > 2001:db8:b0:15:da:b055:0:2.52305: Flags [.], ack 110, win 14400, length 0
11:58:54.227126 IP6 2001:db8:be:600d::2.80 > 2001:db8:b0:15:da:b055:0:2.52305: Flags [P.], seq 1:491, ack 110, win 14400, length 490
11:58:54.227526 IP6 2001:db8:b0:15:da:b055:0:2.52305 > 2001:db8:be:600d::2.80: Flags [.], ack 491, win 2390, length 0
11:58:54.234242 IP6 2001:db8:b0:15:da:b055:0:2.52305 > 2001:db8:be:600d::2.80: Flags [F.], seq 110, ack 491, win 2390, length 0
11:58:54.234921 IP6 2001:db8:be:600d::2.80 > 2001:db8:b0:15:da:b055:0:2.52305: Flags [F.], seq 491, ack 111, win 14400, length 0
11:58:54.235245 IP6 2001:db8:b0:15:da:b055:0:2.52305 > 2001:db8:be:600d::2.80: Flags [.], ack 492, win 2389, length 0

You can easily recognize in the output above the `SYN` segment containing the `MSS` option, the `SYN+ACK` segment returned by the server and then the few data segments exchanged on the connection.

wireshark_ is more recent than tcpdump_. It evolved from the ethereal packet trace analysis software. It can be used as a text tool like tcpdump_. For a TCP connection, wireshark_ would provide almost the same output as tcpdump_. The main advantage of wireshark_ is that it also includes a graphical user interface that allows to perform various types of analysis on a packet trace.

.. figure:: /../book/transport/exercises/fig/wireshark-open.png
   :align: center
   :scale: 50

   Wireshark : default window

The wireshark window is divided in three parts. The top part of the window is a summary of the first packets from the trace. By clicking on one of the lines, you can show the detailed content of this packet in the middle part of the window. The middle of the window allows you to inspect all the fields of the captured packet. The bottom part of the window is the hexadecimal representation of the packet, with the field selected in the middle window being highlighted.

wireshark_ is very good at displaying packets, but it also contains several analysis tools that can be very useful. The first tool is `Follow TCP stream`. It is part of the `Analyze` menu and allows you to reassemble and display all the payload exchanged during a TCP connection. This tool can be useful if you need to analyse for example the commands exchanged during a SMTP session.

The second tool is the flow graph that is part of the `Statistics` menu. It provides a time sequence diagram of the packets exchanged with some comments about the packet contents. See blow for an example.

.. figure:: /../book/transport/exercises/fig/wireshark-flowgraph.png
   :align: center
   :scale: 50

   Wireshark : flow graph

The third set of tools are the `TCP stream graph` tools that are part of the `Statistics menu`. These tools allow you to plot various types of information extracted from the segments exchanged during a TCP connection. A first interesting graph is the `sequence number graph` that shows the evolution of the sequence number field of the captured segments with time. This graph can be used to detect graphically retransmissions.

.. figure:: /../book/transport/exercises/fig/wireshark-seqgraph.png
   :align: center
   :scale: 50

   Wireshark : sequence number graph

A second interesting graph is the `round-trip-time` graph that shows the evolution of the round-trip-time in function of time. This graph can be used to check whether the round-trip-time remains stable or not. Note that from a packet trace, wireshark_ can plot two `round-trip-time` graphs, One for the flow from the client to the server and the other one. wireshark_ will plot the `round-trip-time` graph that corresponds to the selected packet in the top wireshark_ window. 

.. figure:: /../book/transport/exercises/fig/wireshark-rttgraph.png
   :align: center
   :scale: 50

   Wireshark : round-trip-time graph

Experimenting with UDP
----------------------

For these UDP experiments, you will use a simple lab that contains four hosts. 

.. graphviz::

   graph foo {
      rankdir=LR;
      client1 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>Client1</td></TR>
              </TABLE>>];
      client2 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>Client2</td></TR>
              </TABLE>>];
      webserver [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>webserver</td></TR>
              </TABLE>>];
      router[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>router</td></TR>
              </TABLE>>];
      client1--router;
      client2--router;
      router--webserver;
   }

Two hosts, `Client1` and `Client2` are clients that you will use to send information to the `webserver` host through an intermediate `router`. Thanks to the `router`, you will be able to easily observe the packets that are exchanged and delay or discard some of them to see how the protocol reacts to these events.

.. note:: Discovering IP addresses

  On a netkit_ lab such as this one, it is sometimes necessary to discover the IP addresses of the different hosts. On Linux, the IP addresses associated to an interface are configured by using :manpage:`ifconfig(8)`. The output below shows the configuration of the interfaces of the `router` ::

      #ifconfig
       eth0      Link encap:Ethernet  HWaddr 02:bb:88:79:c7:fb  
                 inet6 addr: fe80::bb:88ff:fe79:c7fb/64 Scope:Link
                 inet6 addr: 2001:db8:b0:15:da:b055:0:1/96 Scope:Global
                 UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                 RX packets:15 errors:0 dropped:0 overruns:0 frame:0
                 TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
                 collisions:0 txqueuelen:1000 
                 RX bytes:1052 (1.0 KiB)  TX bytes:636 (636.0 B)
                 Interrupt:5 

       eth1      Link encap:Ethernet  HWaddr 5a:f7:20:7e:4e:9d  
                 inet6 addr: 2001:db8:be:600d::1/64 Scope:Global
                 inet6 addr: fe80::58f7:20ff:fe7e:4e9d/64 Scope:Link
                 UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                 RX packets:7 errors:0 dropped:0 overruns:0 frame:0
                 TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
                 collisions:0 txqueuelen:1000 
                 RX bytes:488 (488.0 B)  TX bytes:636 (636.0 B)
                 Interrupt:5 

       lo        Link encap:Local Loopback  
                 inet addr:127.0.0.1  Mask:255.0.0.0
                 inet6 addr: ::1/128 Scope:Host
                 UP LOOPBACK RUNNING  MTU:65536  Metric:1
                 RX packets:4 errors:0 dropped:0 overruns:0 frame:0
                 TX packets:4 errors:0 dropped:0 overruns:0 carrier:0
                 collisions:0 txqueuelen:0 
                 RX bytes:200 (200.0 B)  TX bytes:200 (200.0 B)

     
   The output of :manpage:`ifconfig(8)` shows that this `router` has three interfaces. The loopback interface (``lo`` on Linux) is the default software-based interface of all hosts. The ``eth0`` interface is connected to the two clients while the ``eth1`` interface is connected to the webserver. The IP address of the `router` on ``eth0`` (resp. ``eth1``) is ``2001:db8:b0:15:da:b055:0::1`` (resp. ``2001:db8:be:600d::1``).

The `webserver` has been configured as a server that supports the following services :

 - ``http`` over TCP on port ``80``
 - ``echo`` over both UDP and TCP on port ``7``
 - ``discard`` over both UDP and TCP on port ``9``
 - ``daytime`` over both UDP and TCP on port ``13``
 - ``telnet`` over TCP on port ``23``

The last three services were popular services installed on all TCP/IP hosts. However, some of them caused security problems and nowadays they are rarely enabled on real servers. 

``echo`` is a very simple service. When a server receives some information, over UDP or TCP, it simply returns it to the client. ``discard`` is a kind of blackhole. All the information, sent over UDP or TCP, to a ``discard`` server is simply discarded upon reception. ``daytime`` is a very simple protocol that allows to query the current time on the server. The format of the response is described in :rfc:`867`.

Several tools allow to send information over UDP and TCP. :manpage:`telnet` is very useful to interact with TCP servers. :manpage:`nc` (or ``netcat``) is another tool which can be very useful when debugging network problems. It allows to easily contact servers over UDP or TCP, but can also be used to create simple but powerful servers from the command line. Several versions of ``nc``/``netcat`` have been written. See http://en.wikipedia.org/wiki/Netcat for additional details.

Start ``tcpdump`` on ``router`` to capture all UDP segments. The ``tcpdump`` manpage will show you how to only capture UDP segments. 

1. Using ``nc`` on `Client1`, send data to the ``discard`` server running on `webserver`. Observe the segments that are exchanged. How does the client select its source port number ?

2. Using ``nc`` on `Client2`, send data to the ``echo`` server running on `webserver`. Use ``tcpdump`` to verify whether the data returned by the server is the same as the one sent by the client. 


.. note:: Some useful tcpdump options

 ``tcpdump`` contains many options as described in the :manpage:`tcpdump`. Among these, the following ones could prove useful :

 - ``-n`` : instructs ``tcpdump`` to print the addresses of the captured packets and do not try to resolve their names. To resolve names, ``tcpdump`` needs to query the reverse DNS servers and this may interfere with the packet capture or introduce delays. 
 - ``-w filename`` : instructs ``tcpdump`` to save the captured packets into a file for further postprocessing. The packet trace can then be read by using ``tcpdump -r filename`` or with Wireshark_. 
 - ``-v``, or ``-vv`` or even ```-vvv`` : use different levels of verbosity when printing information extracted from the packet 
 - ``-S`` forces TCP print the exact sequence/acknowledgements numbers found in the captured segments. By default, tcpdump_ prints sequence numbers that are relative to the beginning of the connection
 - ``-s snaplen`` indicates the default size for the captured packets. Some versions of tcpdump_ use a default snaplength of 64 or 96 bytes, i.e. they only capture the beginning of the packets. This usually includes all useful headers. You might want to increase this value to capture long data segments.

Experiments with TCP
--------------------

:manpage:`nc` can also be used to interact with TCP servers. TCP is a complex protocol and a TCP implementation such the Linux kernel contains a large number of configuration parameters. To ease your understanding of the basic mechanisms of TCP, we have disabled most of the TCP options on `Client1` and `Client2`.

.. todo:: simplifier configuration server

Start by using :manpage:`tcpdump` on `router` to capture all the packets sent on the interface attached to `webserver`


1. Using :manpage:`nc`, try to open a TCP connection to a port on  `webserver` where there is no listening server, e.g. port ``5``. How does :manpage:`tcpdump` shows the first segment of the three way handshake. How does the TCP stack on `webserver` answers to this segment ? What are the TCP options used 

2. Using :manpage:`nc`, open a TCP connection to the ``echo`` port on `webserver` and send some information. From the :manpage:`tcpdump` output, how does the server closes the TCP connection ? 

3. Perform the same experiment as above, but now by using the ``daytime`` server.

4. Perform the same experiment as above, but now by using ``wget`` to retrieve the homepage on `webserver`. Which version of HTTP is used ? How is the TCP connection closed ?

5. The MSS option is the first option that was specified in TCP. It is used during the three-way-handshake to announce the Maximum Segment Size supported by a host. On Linux, the MSS value is computed from the maximum packet size of the underlying network. You can change the maximum packet size of the underlying network (or Maximum Transmission Unit - MTU) by using the command :manpage:`ifconfig(8)` ::

  ifconfig eth0 mtu 1000

 This command reduces the MTU of interface ``eth0`` to 1000 bytes.  Use :manpage:`tcpdump(8)` to observe whether this change affects the segments sent by the client or by the server when :manpage:`nc(1)` is used with the ``echo`` service.

.. , but this value can be configured by using the ``min_adv_mss`` ``sysctl``. On Linux, the :manpage:`systctl` command allows to tune several configuration parameters of the kernel. The ``sysctl`` parameters that are relevant for the network stack are described in https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt


6. The TCP stack on `Client1` was configured to disable all recent TCP options, including Window Scale, Timestamp and Selective acknowledgements. Enable the Timestamp option using the correct ``sysctl`` and verify with :manpage:`tcpdump(8)` that this extension is actually used

7. The main benefit of TCP is that it can react to delays, losses and packet duplications. In a netkit lab, there are usually no delay and no losses or duplications. Fortunately, various tools can be used on the Linux kernel to emulate various network properties. `Netem <http://www.linuxfoundation.org/collaborate/workgroups/networking/netem>`_ is one of these tools. It can be used on a router to add delay, losses or duplications when a router sends packets. Using the commands described in http://www.linuxfoundation.org/collaborate/workgroups/networking/netem, configure the interface between `router` and `websever` with :
  
  #. A fixed delay of 100 milliseconds
  #. Packet losses of 10%, 50% and 95%
  #. Packet corruption
  #. Packet reordering

 Using :manpage:`nc(1)` with the ``discard`` or ``echo`` service, observe by using :manpage:`tcpdump(8)` how TCP reacts to these events during :
  
  - the three-way handshake
  - the data transmission phase
  - the connection release phase

8. Perform the same experiment with the ``discard`` service, but this time introduce errors on the link between `router` and `Client1`. Is TCP more affected from errors on the data segments or on the acknowledgements ?

9. Using a configuration with netem that includes a non-zero delay, packet losses and reordering, observe the benefits of using Selective Acknowledgements. For this, configure netem on the link between `router` and `webserver` and enable the selective acknowledgements with the ``tcp_sack`` ``sysctl`` on `Client2`. Observe the difference between `Client1`, which does not use the selective acknowledgements and `Client2`.

 

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
   0.701 < R. 1001:1001(0) ack 1001


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
