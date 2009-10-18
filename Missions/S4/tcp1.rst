The Transmission Control Protocol
=================================


The Transmission Control Protocol plays a key role in the TCP/IP protocol suite by providing a reliable byte stream service on top of the unreliable connectionless service provided by IP. During this exercise, you will learn how to establish correctly a TCP connection by playing either the role of a client or the role of a server and also to reliably exchange one data segment over this connection.

The deadline for this exercise is Tuesday October 20th, 13.00.

TCP support in scapy_
---------------------

scapy_ includes all the python_ classes that implement the TCP segment format. These classes are part of the standard scapy_ distribution and can be found in file `scapy/layers/inet.py`. A TCP segment in scapy_ contains the following fields (with the default value of the field between () )::

       >>> ls(TCP)
       sport      : ShortEnumField       = (20)
       dport      : ShortEnumField       = (80)
       seq        : IntField             = (0)
       ack        : IntField             = (0)
       dataofs    : BitField             = (None)
       reserved   : BitField             = (0)
       flags      : FlagsField           = (2)
       window     : ShortField           = (8192)
       chksum     : XShortField          = (None)
       urgptr     : ShortField           = (0)
       options    : TCPOptionsField      = ({})
       >>> 

The TCP flags are defined in scapy_ as :

 - `S` for `SYN`
 - `F` for `FIN`
 - `R` for `RST`
 - `P` for `PSH`
 - `A` for `ACK`
 - `U` for `URG`

scapy_ allows you to easily create a TCP segment. For example, to create a `SYN` segment with sequence number set to `1234`, a window size of 4096 bytes, an acknowledgement field set to `0`, a source port set to `9999` and `80` as destination port,  you would write ::

 p=IP(dst="1.2.3.4",src="5.6.7.8")/TCP(sport=9999,dport=80,flags="S",window=4096,seq=1234,ack=0)

The other fields of the TCP header are set to a default value (`urgptr`) or automatically computed (`chksum`). In this segment, since the `ACK` flag is not set, the receiver will not look at the content of the `ack` field. A `SYN+ACK` segment sent in reply to the previous `SYN` segment could be ::

 p=IP(dst="5.6.7.8",src="1.2.3.4")/TCP(dport=9999,sport=80,flags="SA",
				       window=4096,seq=56789,ack=1235)

Note that in the reply, the source and destination addresses and the source and destination ports have been swapped. When establishing a TCP connection, the utilisation of the `SYN` flag consumes one sequence number. This explains why the `ack` field of the reply segment is set to `1235` while the sequence number of the `SYN` segment was `1234`.

scapy_ allows you to easily set a flag in the header of a TCP segment that you create. However, scapy_ is not as user friendly to check the value of a flag in a received segment. For this, you can use the following function ::

 def is_set(flag, pkt):
    '''
    Verifies whether flag was set in segment pkt
    
    :param pkt: segment to compare flag values 
    :type pkt:  scapy.TCP
    :param flag: character corresponding to the flag 
    :type flag: char
    :return: True if flag was set in pkt, False otherwise
    :rtype: boolean
    '''
    flag_vals = {"F":0x1, "S":0x2, "R":0x4, "P":0x8, "A":0x10, "U":0x20, "E":0x40, "C":0x80 }     
    if flag_vals.has_key(flag) :
        return pkt[TCP].flags & flag_vals[flag]
    else:
        return False

Note that the `pkt[TCP]` is used to force scapy_ to interpret `pkt` as a TCP segment. `pkt[TCP].flags` returns a byte containing the TCP flags of a received segment, while `pkt.flags` returns the *IP* flags of the received segments.

Conversely, you may also want to convert the flags of a received segment in a string. This can be done with the following function ::

 def flags2string(flags):
    '''
    Converts the [TCP].flags field of a received segment in a string
    
    :param flags: the received flags (one byte)
    :return: a string containing the letters corresponding to the set flags
    :rtype: string
    '''
    flag_vals = {"F":0x1, "S":0x2, "R":0x4, "P":0x8, "A":0x10, "U":0x20, "E":0x40, "C":0x80 }   
    flagstring=''
    for f in flag_vals.keys():
        if flags & flag_vals[f] :
            flagstring+=f
     
    return flagstring

scapy_ allows you to easily access the `seq`, `ack` or `window` fields of a received segment. To print the main header fields of a received TCP segment, you can use ::

    
 def print_segment(pkt):
    '''
    prints a TCP segment on stdout 
    
    :param pkt: segment to compare flag values 
    :type pkt:  scapy.TCP
    '''
    if not (TCP in pkt):
       print "Not a TCP segment"
    else:
       print "sport=",pkt[TCP].sport," dport=",pkt[TCP].dport,
       	     " seq=",pkt[TCP].seq," ack=",pkt[TCP].ack, 
	     " len=",len(pkt[TCP].payload),
	     " flags=",flags2string(pkt[TCP].flags), 
	     " win=",pkt[TCP].window

Note that `len(pkt[TCP].payload)` allows you to easily extract the length of the payload of a received TCP segment.

When implementing a Finite State Machine in scapy_, it can sometimes be useful to add some debugging information about the segments that are received. For this, it is interesting to note that scapy_ allows you to define multiple `receive_conditions` for a given state. For example, you can write the following code ::

    @ATMT.state()
    def ESTABLISHED(self):
        pass

    @ATMT.receive_condition(ESTABLISHED,prio=0)
    def printpkt(self,pkt):
    	print_segment(pkt)

    @ATMT.receive_condition(ESTABLISHED,prio=1)
    def data_received(self,pkt):
    # processing of the received segment

You can also specify a `priority` to the `receive_condition`. The default value of the priority is `0` and scapy_ will first run the conditions having the lowest priority value. In the example above, scapy_ will first evaluate the `printpkt` condition and then the `data_received` condition. 


Implementing TCP in scapy_
--------------------------

A complete implementation of TCP in scapy_ is, of course, outside the scope of this exercise. However, even for a simplified implementation such as this one, it is useful to consider some of the problems that must be solved in a real TCP implementation.

A TCP implementation maintains a Transmission Control Block (TCB) for each TCP connection. This TCB is a data structure that contains the complete "`state`"  of each TCP connection. The TCB is described in :rfc:`793`. This TCB contains first the identification of the TCP connection. As the IP address of the local host is already known by scapy_, your implementation will need to store : 

 - `self.remoteip` : the IP address of the remote host
 - `self.remoteport` : the TCP port used for this connection on the remote host
 - `self.localport` : the TCP port used for this connection on the local host. Note that when a client opens a TCP connection, the local port will be chosen in the ephemeral port range ( 49152 <= localport <= 65535 ). 

Your implementation also needs to store information about the segments that it has sent and the segments that it has received. :rfc:`793` defines the following variables :

 - `self.sndnxt` : the sequence number of the next byte in the byte stream (the first byte of a new data segment that you send will use this sequence number)
 - `self.snduna` : the earliest sequence number that has been sent but has not yet been acknowledged
 - `self.rcvnxt` : the sequence number of the next byte that your implementation expects to receive from the remote host. For this exercise, you do not need to maintain a receive buffer and your implementation can discard the out-of-sequence segments that it receives

For this exercise we will limit the number of unacknowledged segments to `one`. You can thus implement the sending buffer by storing the last unacknowledged segment :

 - `self.lastsegment` : last unacknowledged segment

The TCB also needs to contain the current size of the windows :

 - `self.sndwnd` : the current sending window
 - `self.rcvwnd` : the current window advertised by the receiver

For this exercise, you do not need to process the `window` field of the received segments. You can assume that the receiver is always advertising a window of a least one segment.


Practical issues
----------------

For this exercise, you will reuse the UML virtual machines that you have used for the two previous exercises. 

As you are implementing a protocol that is already supported by the Linux kernel, you need to ensure that the Linux kernel will not reply to the TCP segments that your implementation receives. For this, the easiest solution is to configure the firewall [#ffirewall]_ on the UML machine where you are running scapy_ to block all TCP segments. TCP should only be blocked on the interface between the two UML machines. For example, if you run scapy_ on the UML1 and test it against UML2, you could configure UML1's firewall as follows ::

 iptables -A INPUT -p tcp -i eth0 -j DROP
 iptables -A OUTPUT -p tcp -o eth0 -j DROP

The first line configures the firewall to drop all TCP segments destined to the Linux kernel on interface `eth0` while the second line drops all TCP segments sent by the Linux kernel on interface `eth0`. The Linux firewall does not interfere with scapy_, but of course it prevents you from using any TCP-based client or server such as telnet_ on the `eth0` interface. If you run into problems, you can remove all the rules configured in the firewall with ::

 iptables --flush

Additional information about the netfilter_ firewall used on the Linux kernel may be found at `<http://www.netfilter.org/documentation/index.html>`_ or in the :manpage:`iptables(8)` man page.

As most Unix variants, Linux supports the :manpage:`netstat(8)` command. This command allows you to extract various statistics from the networking stack on the Linux kernel. For TCP, `netstat` can list all the active TCP connections with the state of their FSM. `netstat` supports the following options that could be useful during this exercices :

 - `-t` requests information about the TCP connections
 - `-n` requests numeric output (by default, `netstat` sends DNS queries to resolve IP addresses in hosts and uses `/etc/services` to convert port number in service names, `-n` is recommended on the UML machines)
 - `-e` provides more information about the state of the TCP connections
 - `-o` provides information about the timers
 - `-a` provides information about all TCP connections, not only those in the Established state


Deliverables
------------

Each team of two students will either implement [#fgoogle]_: : 

#. One FSM for a TCP client that connects to a TCP server (e.g. a python_ server using the socket API on a Linux kernel), sends reliably one segment of data, receives one segment, acknowledges it and prints it on stdout

#. One FSM for a TCP server that accepts one connection from a client (this client could be a python_ client using the socket API on top of a Linux kernel), receives one data segment, prints it on stdout, acknowledges it and sends reliably one data segment in response

Each group must ensure that at least one team implements a client and one team implements a server.

The two FSMs must correctly process the TCP segments with the `SYN`, `RST` and `ACK` flags. The other flags (notably `FIN`, `PSH` and `URG`) can be ignored for this exercise. 

To simplify the TCP connection establishment, you can ignore the options in the `SYN` segment and assume the default MSS_ size of 536 bytes as defined in :rfc:`793`. 

For the TCP client, your implementation should be structured as follows ::

 class TCP_simpleclient(Automaton):
    
    def parse_args(self, remoteip, remoteport, data, *args, **kargs):
	Automaton.parse_args(self, **kargs)
	# to be completed

    def master_filter(self, pkt):
        return (IP in pkt 
	       # to be completed
	       )

    @ATMT.state(initial=1)
    def INIT(self):
    # to be completed

    @ATMT.state()
    def SYN_SENT(self):
    # to be completed

    @ATMT.state()
    def SYN_RCVD(self):
    # to be completed 
	    
    @ATMT.state()
    def ESTABLISHED(self):
        # to be completed 

    @ATMT.state(final=1)
    def CLOSED(self):
        # send RST segment
        p=IP(dst=self.remoteip)/TCP(seq=self.sndnxt,sport=self.localport,
			            dport=self.remoteport,ack=self.rcvnxt,
				    window=self.sndwnd,flags='R')
        print "Done !"

    # receive_conditions and timeouts to be added


For the TCP server, your implementation should be structured as follows ::

 class TCP_simpleserver(Automaton):
    
    def parse_args(self, remoteip, localport, *args, **kargs):
	Automaton.parse_args(self, **kargs)
        # to be completed 

    def master_filter(self, pkt):
        return (IP in pkt 
	        # to be completed
                )

    @ATMT.state(initial=1)
    def INIT(self):
    # to be completed 

    @ATMT.state()
    def SYN_RCVD(self):
    # to be completed 

    @ATMT.state()
    def SYN_SENT(self):
    # to be completed

    @ATMT.state()
    def ESTABLISHED(self):
    # to be completed 

    @ATMT.state(final=1)
    def CLOSED(self):
        # send RST segment
        p=IP(dst=self.remoteip)/TCP(seq=self.sndnxt,sport=self.localport,
			            dport=self.remoteport,ack=self.rcvnxt,
				    window=self.sndwnd,flags='R')
        print "Done !"

    # receive_conditions and timeouts to be added
  

You do not need to implement the TCP connection release. To release the TCP connection, you can set a long timeout in the `ESTABLISHED` and enter the `CLOSED` state when this timer expires ::

    @ATMT.timeout(ESTABLISHED,30)
    def reset_connection(self):	
    	raise self.CLOSED()
	
Remember that the initial TCP specification :rfc:`793` defines a go-back-n mechanism for TCP. This implies that your implementation can behave as a go-back-n receiver (e.g. ignore out-of-sequence segments) or sender. To simplify the retransmission of segments, consider that you send a single segment at a time. You can advertise a TCP window size of one segment (536 bytes) to limit the number of segments that the remote TCP implementation will send you.

Do not forget to document your code and provide some explanations about the tests you perform with your FSM to verify its interoperability with the TCP implementation of the Linux kernel.

To test your implementation, you can use a simple client or server written by using the socket API.


The socket API
..............

Network applications are often written by using the socket_ API. This API is a relatively low-level API that allows to develop servers and clients. The documentation of the socket_ API in python may be found at http://docs.python.org/library/socket.html

For example, the code below [#fsourcepythondoc]_ provides a simple socket client written in python that opens a TCP connection to a remote server, sends `Hello, world`, prints the received answer on stdout and waits for 10 seconds before closing the connection ::

  #! /usr/bin/env python

  import sys
  import socket    # the socket API in python
  import time

  if len(sys.argv)!=3:
    print "Usage  rcv-tcp.py <host> <port>"
    sys.exit(-1)

  HOST = sys.argv[1]              # any IP address of the server
  PORT = int(sys.argv[2])         # server port

  # creation of the socket. 
  # socket.AF_INET indicates that we will use IPv4
  # socket.SOCK_STREAM indicates that we will use TCP over this socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # open a TCP connection to HOST:PORT
  s.connect((HOST, PORT))

  print "Connected to", HOST

  # sends a string over the TCP connection
  s.send("Hello,world")

  # wait for data, a default buffer of 1024 bytes is provided
  data = s.recv(1024)
  if not data: 
    print "Error : no data received"
  else:
    print "Received: ",data

  time.sleep(10)

  print "Closing connection"

  # release of the connection
  s.close()
    

The code below is for a server that receives a string, prints it on stdout, echoes it back to the client and releases the TCP connection after a delay of 10 seconds ::

  #! /usr/bin/env python

  import sys
  import socket      # the socket API

  if len(sys.argv)!=2:
    print "Usage  rcv-tcp.py <port>"
    sys.exit(-1)

  HOST = ''                       # any IP address of the host
  PORT = int(sys.argv[1])         # server port
  # creation of the socket. 
  # socket.AF_INET indicates that we will use IPv4
  # socket.SOCK_STREAM indicates that we will use TCP over this socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # socket is bound to PORT and will wait for TCP connections
  s.bind(('', PORT))
  # socket listens for maximum 1 TCP connection in the queue
  s.listen(1)
  # s.accept() succeeds when a TCP connection is established
  conn, addr = s.accept()
  print 'Connected by', addr
  # wait for data, a default buffer of 1024 bytes is provided
  data = conn.recv(1024)
  if not data: 
     print "Error : no data received"
  else:
    print "Received: ",data
  # echoes the received data to client
  s.send(data)    
  time.sleep(10)
  print "Closing connection"
  # release of the connection
  conn.close()





.. rubric:: Footnotes

.. [#fsourcepythondoc] This code is adapted from the python_ documentation available at http://docs.python.org/library/socket.html

.. [#ffirewall] A firewall is a software or hardware device that analyses TCP/IP packets and decides, based on a set of rules, to accept or discard the packets received or sent. The rules used by a firewall usually depend on the value of some fields of the packets (e.g. type of transport protocols, ports, ...). We will discuss in more details the operation of firewalls in the network layer chapter. 

.. [#fgoogle] The astute reader or expert googler might notice that some implementations of the TCP FSM have already been written. For example, the scapy distribution contains in the file `scapy/layers/inet.py` a `TCP_client` Automaton. Although this Automaton can work in some cases, it does not completely implement the TCP FSM. A more detailed TCP FSM in scapy_ has been implemented by Adam Pridgen http://www.thecoverofnight.com/projects/code/basic_tcp_sm.py, but this FSM goes beyond this simple exercise.

.. include:: ../../book/links.rst

.. 
   Additional questions to ask to the students



   Points to check during the evaluation of the TCP code

