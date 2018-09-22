.. Copyright |copy| 2013 by Olivier Bonaventure  with the help of Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Experimenting with Internet congestion control
==============================================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=7


For this lab, you will reuse a slightly modified version of the TCP/UDP lab. The filesystem used for this lab contains several new software packages. Make sure to start the lab by using ``lstart`` from the lab's directory. The archive containing the lab directory can be downloaded from :download:`/netkit/netkit-lab_congestion.zip`

Your objective with this lab is to better understand the TCP congestion control scheme and how it influences the performance of TCP.

.. graphviz::

   graph foo {
      rankdir=LR;
      client1 [color=white, shape=box label=<<TABLE border="0" cellborder="0"><TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>Client1 [2001:db8:be:feed::11]</td></TR>
              </TABLE>>];
      client2 [color=white, shape=box label=<<TABLE border="0" cellborder="0"><TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>Client2 [2001:db8:be:beef::11]</td></TR>
              </TABLE>>];
      server [color=white, shape=box label=<<TABLE border="0" cellborder="0"><TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>server [2001:db8:be:b00b::11]</td></TR>
              </TABLE>>];
      router[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>router</td></TR>
              </TABLE>>];
      client1--router;
      client2--router;
      router--server;
   }


During this lab, you will use three software packages that are very useful to understand TCP performance in real IP networks. To simulate network congestion, the bandwidth of the link between the router and the server has been shaped at 1 Mbps.

iperf_ (version 3) is a frequently used network performance testing tool. It is often used by network administrators who need to test the performance of a network between two hosts. To use iperf_, you first need to start the server process by using ``iperf -s`` on host ``server`` on the lab. The server listens on ``5201`` for measurements requests coming from the server. When a measurement starts, the client sends data to the server.

The `iperf manpage <https://software.es.net/iperf/invoking.html>`_ lists all the options of the server and the client. The most interesting ones are :

 - ``-6`` forces the utilisation of IPv6
 - ``--udp`` uses UDP for the measurements instead of TCP which is the default
 - ``--set-mss x`` sets the TCP MSS at x bytes 
 - ``--bandwidth b`` iperf_ tries to send data at b bits/sec (default for UDP is 1 Mbps, unlimited for TCP)
 - ``--verbose`` provides much more detailed output, including TCP_INFO statistics with TCP on Linux
 - ``--window x`` specifies the TCP window size in bytes on both the client and the server
 - ``--reverse`` forces the measurement to be done from the server to the client
 - ``--parallel n`` iperf_ uses n parallel flows to perform the measurement


Experiments
-----------

The experiments below will allow you to verify experimentally the key factors that influence the performance of the TCP congestion control scheme. We use a TCP implementation that supports the TCP congestion control scheme, but not the window scale, timestamp and selective acknowledgement options. You can, of course, enable these options if you want to experiment with them.

#. The round-trip-time is a key factor that influences the performance of TCP in a network. TCP maintains its own estimate of the round-trip-time over a connection. Other tools like :manpage:`ping6(8)` can be used to measure the round-trip-time. Start a lab and use :manpage:`ping6(8)` to measure the round-trip-time. Then, start iperf_ sessions from ``client1`` and ``client2`` and capture the TCP segments on ``router`` with :manpage:`tcpdump(8)`. Analyze the collected trace with tcptrace_ or wireshark_ and observe the evolution of the measured round-trip-time. 

#. An important factor to achieve a high goodput with TCP is the window size. Using the ``--window`` parameter of iperf_, compare the performance achieved by a client with a window of 4 KBytes, 16 KBytes and 32 KBytes. Compare this with the bandwidth delay product in the emulated network.

#. The first factor that influences the performance of the TCP congestion control scheme is the round-trip-time. A TCP connection with a longer round-trip-time will react slower than a connection with a shorter round-trip time. Start an iperf_ server and use netem_ to add a delay of

   - ``10 msec`` on the link between the ``router`` and ``client1``
   - ``200 msec`` on the link between the ``router`` and ``client2``
 
 Using iperf_, verify experimentally that the ``client1`` obtains a higher goodput [#fgoodput]_ than ``client2`` 

#. The TCP congestion control scheme operates on a per TCP connection basis. This implies that a client that uses several parallel TCP connections should be favored compared to a client that uses a single TCP connection. Using the ``--parallel `` parameter of iperf_, verify that this is indeed the case in a lab where ``client1`` and ``client2`` have the same round-trip-time.

#. Another factor that influences the performance of TCP is the size of the transmitted segments. Using the ``-mss`` parameter of iperf_, change the MSS on ``client1`` and verify whether this reduces its performance compared to ``client2`` (assuming, of course, that the round-trip-times are the same for the two clients)

#. In the book, we have explained that the TCP goodput was inversely proportional to the square root of the packet loss ratio. Using netem_, simulate different packet loss ratios and verify this formula.

#. In some cases, the goodput obtained by an application also depends on the performance of the application itself. For example, iperf_ provides the ``--file`` option that reads the data to be sent from a file instead of from memory to verify whether the disk is the bottleneck [#fdisk]_. In our emulated lab, this option cannot be used. However, you can emulate a bottleneck on the client/server by using the ``--bandwidth`` parameter of iperf_. Use this option and analyze the captured packet trace to see how you can identify this behavior from the trace.


Packet traces
-------------

Network administrators often need to debug performance problems in a network by looking only at packet traces. The three packet traces below were collected in an emulated network that is similar to the one we used in the lab. Can you analyze the packet traces and :

 - order them by increasing TCP goodput
 - identify the performance bottleneck inside each trace

The three traces can be downloaded from :

 - :download:`/exercises/traces/congestion1.pcap`
 - :download:`/exercises/traces/congestion2.pcap`
 - :download:`/exercises/traces/congestion3.pcap`

wireshark_ and tcptrace_ should help you to analyze these three traces.



.. rubric:: Footnotes

.. [#fgoodput] The goodput is defined as the total number of bytes transmitted by an application divided by the duration of the transfer. This is the measurement reported by iperf_. It should not be confused with the `throughput` which is measured on the network interfaces and usually includes all the overheads of the different layers.

.. [#fdisk] See http://fasterdata.es.net/performance-testing/network-troubleshooting-tools/iperf-and-iperf3/disk-testing-using-iperf/ for additional information and an example.

.. include:: /links.rst
