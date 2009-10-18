TCP congestion control
======================

The TCP congestion control mechanisms, defined in :rfc:`5681` plays a key role in today's Internet. Without this mechanism that was first defined and implemented in the late 1980s, the Internet would not have been able to continue to work until now. The objective of this exercise is to allow you to have a better understanding of the operation of TCP's congestion control mechanism by analysing all the segments exchanged over a TCP connection.


The deadline for this exercise is Tuesday October 27th, 13.00.


Experimental setup
------------------


For this exercise, we have performed measurements in the emulated [#femulation]_ network shown below.


.. figure


The emulated network is composed of three machines : a client, a server and a router. The client and the server are connected via the router. The server sends 1 MBytes of data to the client by using iperf_. The link between the router and the client is controlled by using the `netem <http://www.linuxfoundation.org/en/Net:Netem>`_ Linux kernel module. This module allows us to insert additional delays, reduce the link bandwidth and insert random losses. 


.. sidebar:: Linux congestion control schemes

 Linux supports several congestion control mechanisms [#fcongestion]_ . For this exercise, we have configured the Linux kernel to use the NewReno scheme :rfc:`3782` that is very close to the official standard defined in :rfc:`5681`




When debugging networking problems or to analyse performance problems, it is sometimes useful to capture the segments that are exchanged between two hosts and to analyse them.  We first used `tcpdump <http://www.tcpdump.org>`_ to capture all the TCP segments that are exchanged between the client and the server. For each measurement, we collected two traces :

 - the first trace contains all the segments sent and received by the client
 - the second trace contains all the segments sent and received by the server

Each trace contains the first xx bytes of each segment (as well as the headers of the protocols in the network and datalink layers, but these headers will not be analysed during this exercise) and the capture time of this segment. By looking at the header of each segment, it is easy to extract the `flags`,  `sequence number` or `acknowledgement numbers` of each segment 

To analyse such as trace, there are basically two possible options :

#. Use a packet trace analysis software such as `tcpdump <http://www.tcpdump.org>`_ or `wireshark <http://www.wireshark.org>`_

#. Develop some scapy_ scripts to extract the information that you need from a packet trace


Several packet trace analysis software are available, either as commercial or open-source tools. These tools are able to capture all the packets exchanged on a link. Of course, capturing packets require administrator privileges. They can also analyse the content of the captured packets and display information about them. The captured packets can be stored in a file for offline analysis.

tcpdump_ is probably one of the most well known packet capture software. It is able to both capture packets and display their content. tcpdump_ is a text-based tool that can display the value of the most important fields of the captured packets. Additional information about tcpdump_ may be found in :manpage:`tcpdump(1)`. The text below is an example of the output of tcpdump_ for the first TCP segments exchanged on an scp transfer between two hosts ::

 21:05:56.230737 IP 192.168.1.101.54150 > 130.104.78.8.22: S 1385328972:1385328972(0) win 65535 <mss 1460,nop,wscale 3,nop,nop,timestamp 274527749 0,sackOK,eol>
 21:05:56.251468 IP 130.104.78.8.22 > 192.168.1.101.54150: S 3627767479:3627767479(0) ack 1385328973 win 49248 <nop,nop,timestamp 1212093352 274527749,mss 1452,nop,wscale 0,nop,nop,sackOK>
 21:05:56.251560 IP 192.168.1.101.54150 > 130.104.78.8.22: . ack 1 win 65535 <nop,nop,timestamp 274527749 1212093352>
 21:05:56.279137 IP 130.104.78.8.22 > 192.168.1.101.54150: P 1:21(20) ack 1 win 49248 <nop,nop,timestamp 1212093355 274527749>
 21:05:56.279241 IP 192.168.1.101.54150 > 130.104.78.8.22: . ack 21 win 65535 <nop,nop,timestamp 274527749 1212093355>
 21:05:56.279534 IP 192.168.1.101.54150 > 130.104.78.8.22: P 1:22(21) ack 21 win  65535 <nop,nop,timestamp 274527749 1212093355> 
 21:05:56.303527 IP 130.104.78.8.22 > 192.168.1.101.54150: . ack 22 win 49248 <nop,nop,timestamp 1212093357 274527749>
 21:05:56.303623 IP 192.168.1.101.54150 > 130.104.78.8.22: P 22:814(792) ack 21 win 65535 <nop,nop,timestamp 274527749 1212093357>


You can easily recognise in the output above the `SYN` segment containing the `MSS`, `window scale`, `timestamp` and `sackOK` options, the `SYN+ACK` segment whose `wscale` option indicates that the server does use use window scaling for this connection and then the first few segments exchanged on the connection.


wireshark_ is more recent than tcpdump_. It evolved from the ethereal packet trace analysis software. It can be used as a text tool like tcpdump_. For a TCP connection, wireshark_ would provide almost the same output as tcpdump_. The main advantage of wireshark_ is that it also includes a graphical user interface that allows to perform various types of analysis on a packet trace.

.. figure:: fig/wireshark-open.png
   :align: center
   :scale: 50

   Wireshark : default window

The wireshark window is divided in three parts. The top part of the window is a summary of the first packets from the trace. By clicking on one of the lines, you can show the detailed content of this packet in the middle part of the window. The middle of the window allows you to inspect all the fields of the captured packet. The bottom part of the window is the hexadecimal representation of the packet, with the field selected in the middle window being highlighted.

wireshark_ is very good at displaying packets, but it also contains several analysis tools that can be very useful. The first tool is `Follow TCP stream`. It is part of the `Analyze` menu and allows you to reassemble and display all the payload exchanged during a TCP connection. This tool can be useful if you need to analyse for example the commands exchanged during a SMTP session.

The second tool is the flow graph that is part of the `Statistics` menu. It provides a time sequence diagram of the packets exchanged with some comments about the packet contents. See blow for an example.

.. figure:: fig/wireshark-flowgraph.png
   :align: center
   :scale: 50

   Wireshark : flow graph

The third set of tools are the `TCP stream graph` tools that are part of the `Statistics menu`. These tools allow you to plot various types of information extracted from the segments exchanged during a TCP connection. A first interesting graphs is the `sequence number graph` that shows the evolution of the sequence number field of the captured segments with time. This graph can be used to detect graphically retransmissions.

.. figure:: fig/wireshark-seqgraph.png
   :align: center
   :scale: 50

   Wireshark : sequence number graph

A second interesting graph is the `round-trip-time` graph that shows the evolution of the round-trip-time in function of time. This graph can be used to check whether the round-trip-time remains stable or not.

.. figure:: fig/wireshark-rttgraph.png
   :align: center
   :scale: 50

   Wireshark : round-trip-time graph


In addition to allowing you to send and receive packets, scapy_ also allows you to easily read packet traces captured by tools such as tcpdump_ or wireshark_ provided that they are in the libpcap_ format. The `rdpcap` method allows you to read an entire trace in memory and convert it into a list of scapy_ packets ::

   >>> l=rdpcap("/mnt/host/tcp.pcap")
   >>> l   
   <tcp.pcap: TCP:2863 UDP:48 ICMP:0 Other:14>

This packet trace contains 2863 TCP segments, 48 UDP segments and 14 other packets. You can easily access any of the TCP segments of the trace ::

 >>> l[1234]
 <Ether  dst=00:19:e3:d7:12:04 src=00:0f:66:5b:53:9a type=0x800 |<IP  version=4L ihl=5L tos=0x0 len=64 id=27625 flags=DF frag=0L ttl=48 proto=tcp chksum=0x4c51 src=130.104.78.8 dst=192.168.1.101 options='' |<TCP  sport=ssh dport=54150 seq=3627769700L ack=1386377058 dataofs=11L reserved=0L flags=A window=49248 chksum=0xcab2 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1212095749, 274527976)), ('NOP', None), ('NOP', None), ('SAck', (1386379938, 1386400098))] |>>>
 >>> ls(l[1234][TCP])      
 sport      : ShortEnumField       = 22              (20)
 dport      : ShortEnumField       = 54150           (80)
 seq        : IntField             = 3627769700L     (0)
 ack        : IntField             = 1386377058      (0)
 dataofs    : BitField             = 11L             (None)
 reserved   : BitField             = 0L              (0)
 flags      : FlagsField           = 16L             (2)
 window     : ShortField           = 49248           (8192)
 chksum     : XShortField          = 51890           (None)
 urgptr     : ShortField           = 0               (0)
 options    : TCPOptionsField      = [('NOP', None), ('NOP', None), ('Timestamp', (1212095749, 274527976)), ('NOP', None), ('NOP', None), ('SAck', (1386379938, 1386400098))] ({})
 >>> l[1234][TCP].window
 49248

You can easily write python scripts to extract information from a libpcap trace. When writing such a script, do not forget that the trace contains the segments sent and received by a host.

During the previous exercise, you have used :manpage:`netstat(8)` To lookup the state of the TCP connections on a given host. On the Linux kernel, there are tools that can provide more information than :manpage:`netstat(8)`. One of these tools is the `TCPProbe <http://www.linuxfoundation.org/en/Net:TcpProbe>`_ kernel module. When installed on a Linux kernel, this kernel module prints one ASCII line containing the following information upon the arrival of each TCP segment :


 #. The timestamp (seconds.nanoseconds)
 #. The source endpoint (address:port)
 #. The destination endpoint (address:port)  
 #. This column should be ignored
 #. The length of payload of the IP packet containing the segment (you need to subtract the length of the TCP header to compute the length of the TCP payload)
 #. The current value of `snd.nxt`
 #. The current value of `snd.una`
 #. The current value of the congestion window `snd.cwnd`
 #. The current value of the slow-start threshold `snd.ssthresh`
 #. The current size of the sending window `snd.wnd`
 #. The current value of the smoothed round-trip-time `srtt`
 #. The current value of `rcv.nxt`
 #. This column should be ignored
 #. The current value of the receive window `rcv.wnd`
 #. This column should be ignored

A sample TCPProbe trace is shown below ::

 14.449378000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fed8c49 0x6fed8689 2 2147483647 5792 8 0x6fe931b6 0x6fe931b6 5840
 14.459272000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fed9799 0x6fed86a1 3 2147483647 5792 7 0x6fe931b6 0x6fe931b6 5840
 14.471374000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6feda2e9 0x6fed8c49 4 2147483647 8688 6 0x6fe931b6 0x6fe931b6 5840
 14.483485000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedae39 0x6fed91f1 5 2147483647 11584 6 0x6fe931b6 0x6fe931b6 5840
 14.495677000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedb989 0x6fed9799 6 2147483647 14480 5 0x6fe931b6 0x6fe931b6 5840
 14.507770000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedc4d9 0x6fed9d41 7 2147483647 17376 5 0x6fe931b6 0x6fe931b6 5840
 14.519939000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6fedd029 0x6feda2e9 8 2147483647 20272 5 0x6fe931b6 0x6fe931b6 5840
 14.532096000 192.168.10.2:48044 192.168.12.2:5001 0 32 0x6feddb79 0x6feda891 9 2147483647 23168 5 0x6fe931b6 0x6fe931b6 5840

As you can see from the trace, the values of `snd.nxt` and `snd.una` are in hexadecimal. The congestion window and the slow-start threshold are expressed in MSS-sized segments. We see clearly in the trace above the congestion window that increases. The slow-start threshold is initialised at `2147483647` when the TCP connection starts. Its value will be updated after the first congestion event.

Deliverables
____________


For this exercises, we have generated nine packet traces corresponding to different network conditions (delay, losses) between the client and the server. You can download these traces from the links below :

 - :download:`traces/trace1.pcap` : milliseconds delay, packet loss ratio
 - :download:`traces/trace2.pcap` :
 - :download:`traces/trace3.pcap` :
 - :download:`traces/trace4.pcap` :
 - :download:`traces/trace5.pcap` :
 - :download:`traces/trace6.pcap` :
 - :download:`traces/trace7.pcap` :
 - :download:`traces/trace8.pcap` :
 - :download:`traces/trace9.pcap` :

Each team of two students will select two different traces from the set above and will analyse these. For each trace, you will compute :

 - the number of segments containing data sent by the client and the server
 - the options used on the TCP connection
 - the evolution of the round-trip-time
 - the number of segments that have been retransmitted (and the number of unnecessary retransmissions)
 - the number of expirations of the retransmission timer
 - the evolution of the congestion window

Based on this analysis, each team will explain to the other members of the group the evolution of a TCP connection.

.. rubric:: Footnotes

.. [#fcongestion] For more information about the TCP congestion control schemes implemented in the Linux kernel, see http://linuxgazette.net/135/pfeiffer.html and http://www.cs.helsinki.fi/research/iwtcp/papers/linuxtcp.pdf or the source code of a recent Linux. A description of some of the sysctl variables that allow to tune the TCP implementation in the Linux kernel may be found in http://fasterdata.es.net/TCP-tuning/linux.html

.. [#femulation] With an emulated network, it is more difficult to obtain quantitative results than with a real network since all the emulated machines need to share the same CPU and memory. This creates interactions between the different emulated machines that do not happen in the real world. However, since the objective of this exercise is only to allow the students to understand the behaviour of the TCP congestion control mechanism, this is not a severe problem.

.. include:: ../../book/links.rst
