The Alternating Bit Protocol
============================

The objective of this set of exercises is to better understand the
basic mechanisms of a transport layer protocol by implementing them in
an emulated environment. The deadline for this exercise is *Tuesday
October 6th, 2009 at 13.00*.


scapy_
------


For this exercise, and many of others, we will extend scapy_. scapy_ is
a packet injection tool developed by `Philippe Biondi`_ and many
others. scapy is open-source and written in python_. It was designed as
a tool to easily create and process specially crafted TCP/IP
packets. We will use scapy as a prototyping tool that allows to easily
implement simple protocols and simple mechanisms.


.. explain layering

scapy_ follows the layering principles used by networking
protocols. It allows to easily create and send packets through the
network. When using scapy_, it is very easy to create any packet and
send them. scapy_ creates packets and bypasses the networking
stack. From a security viewpoint, such operations are privileged and
can only be performed by `root` on Linux. scapy_ is run on the command
line as an interactive tool ::

 debian:~# sudo scapy
 INFO: Can't import python gnuplot wrapper . Won't be able to plot.
 INFO: Can't import PyX. Won't be able to use psdump() or pdfdump().
 WARNING: No route found for IPv6 destination :: (no default route?)
 DEBUG: Loading layer p3
 Welcome to Scapy (2.0.1-dev)
 >>> 

You can ignore the INFO and WARNING lines that, depending on your
installation may indicate that some optional packages have not been
installed.


scapy_ is usually used to create special packets and send them. For
example, the following line allows to create a reference p to a UDP segment containing "ABCD" as its payload ::

  p=UDP()/"ABCD"

Note the utilization of the `/` character to stack the "ABCD" string
on top of the UDP segment that was created with `UDP()` scapy_
contains classes that represent many of the protocols of the TCP/IP
protocol suite, including IP, TCP, UDP, ... UDP is the easiest to
understand. As you know, a UDP header contains a source port, a
destination port, a checksum and a length field. This is exactly the
same in scapy_. scapy_ allows you to see all the fields of a given
header by using `ls` ::

  >>> ls(UDP)
 sport      : ShortEnumField       = (53)
 dport      : ShortEnumField       = (53)
 len        : ShortField           = (None)
 chksum     : XShortField          = (None)

We find back all the fields of the UDP header. When creating a packet,
most of these fields have a default value. In the case of UDP, the
source and destination ports are set to 53, the length and the
checksum are automatically computed based on the payload. You can
change the source and destination ports of the UDP segment as follows
::

 >>> p=UDP(sport=1234,dport=5678)

The `Packet` class contains several methods to inspect packets :

 - pkt.summary()	for a one-line summary
 - pkt.show()	for a developed view of the packet
 - pkt.show2()	same as show but on the assembled packet (checksum is calculated, for instance)

For example ::

 >>> p=UDP(sport=1234,dport=5678)
 >>> p.summary()
 'UDP 1234 > 5678'
 >>> p.show()
 ###[ UDP ]###
  sport= 1234
  dport= 5678
  len= None
  chksum= None
 >>> p=IP()/UDP(sport=1234,dport=5678)
 >>> p.show2()
 ###[ IP ]###
  version= 4L
  ihl= 5L
  tos= 0x0
  len= 28
  id= 1
  flags= 
  frag= 0L
  ttl= 64
  proto= udp
  chksum= 0x7cce
  src= 127.0.0.1
  dst= 127.0.0.1
  \options\
 ###[ UDP ]###
     sport= 1234
     dport= 5678
     len= 8
     chksum= 0xe6db
 >>> 

To build a new protocol with scapy_, you first need to define the
format of the header. Taking UDP as an example and looking at file
`scapy/layers/inet.py`, we see that UDP is defined as follows ::

 class UDP(Packet):
    name = "UDP"
    fields_desc = [ ShortEnumField("sport", 53, UDP_SERVICES),
                    ShortEnumField("dport", 53, UDP_SERVICES),
                    ShortField("len", None),
                    XShortField("chksum", None), ]


The UDP header is composed of 4 short (i.e. 16 bits long) fields : the
source port [#fsport]_, the destination port, the length field and the
checksum. To design your own segment header, you need to define a
similar class. scapy_ knows many basic types of fields that can be
included in a header, such as :

 - `BitField(name, default, n)` where `name` is the `name` of the
   field, `default` the default value when not specified and `n` the
   length of the field in bits
 - `FlagsField(name, default, n, ["A",...])` where `name` is the `name` of the
   field, `default` the default value when not specified, `n` the
   number of bits of the field and the array `[ "A", ...]` contains
   the names of the flags. Compared to `BitField`, the advantage of
   the `FlagsField` is that each bit is a flag that you can set or reset. 
 - `BitEnumField(name, default, n, {0:"A", ...})` where `name` is the
  `name` of the `n` bits field, `default` the default value when not
  specified and the  `{0:"A", ...}` provides the names associated to
  the different bit values. Compared to the `BitField`, the advantage
  of the `BitEnumField` is that you can specify the values of the
  field as an enumeration. 
 - `ShortField(name, default)` where `name` is the `name` of the
   16 bits field, `default` the default value when not specified
 - `ByteField(name, default)` where `name` is the `name` of the
   8 bits field, `default` the default value when not specified



.. explain protocol creation

To create a header for MyProtocol, you first need to define the class
that extends the Packet class. This can be done as follows ::

 class MyProtocol(Packet):
    name = "MyProtocol"
    fields_desc = [ BitEnumField("first", 0, 4, {0:"A", 1:"B"} ),
                    BitField("second",0,4),
		    ShortField("len", None),
		    ByteField("padding",0),
                  ]

The header of this protocol is composed of 32 bits and contain three
field. A first group of 4 bits, then a second one, a 16 bits `len` field
and one byte of padding to ensure that the header takes 32 bits. The
description of this header will be placed in file
`scapy/layers/myprotocol.py` in the scapy_ source distribution.

Besides creating the header, you also need to explain to scapy_ how to
build a packet containing this header. This is done by defining in the
`MyProtocol` class the `post_build` method.  The simplest
implementation of this method is to concatenate the header with the
payload as follows ::

    def post_build(self, p, pay):
        p += pay
        return p

If you want to use a length field as in the example above, you need to
compute the length of the packet and include it in the header. In the
example above, the first byte of the header containing the flags, the
second and third the length and the fourth byte contains the
padding. The length field can be computed automatically and placed in
the appropriate location in the header as follows (the
`struct.pack("!H",l)` call converts the `l` value in unsigned network
byte order format which is the standard format used to send 16 bits
numbers over an IP network - you can reuse this method as it is if you
have a length field in your protocol) ::

    def post_build(self, p, pay):
        p += pay
        l = self.len
        if l is None:
                l = len(p)
                p = p[:1]+struct.pack("!H",l)+p[4:]
        return p

If you want to add a checksum to your protocol, this is also in the
`post_build` that you would add the checksum computation. However,
this requires some advanced knowledge of scapy_ that goes beyond this exercise.

Once the protocol header has been created, you need to tell scapy how
it can intercept the packets using this protocol. As we are building a
transport layer protocol, it will run on top of a networking
protocol. For this exercise, you will run your protocol above IP_ 
Although we haven't yet described how IP works, you need to know that
IP uses a field called `protocol` to indicate the transport protocol
that was used to create the payload of an IP packet. IP protocol
numbers are allocated by IANA_ and the registry can be found at
http://www.iana.org/assignments/protocol-numbers/
For this exercise, we can reuse protocol `210` which is
unallocated. To tell scapy to bind `MyProtocol` to IP protocol 210,
you need to add in `scapy/layers/myprotocol.py` the following line ::

  bind_layers(IP,MyProtocol, proto=210)


Once your protocol has been defined and bound, you can use scapy_ in
interactive mode to send and receive packets containing your
protocol. To send a packet, you can simply use the `send` method
provided by scapy_. For example ::

 >>> send(IP(src="1.2.3.4",dst="5.6.7.8")/MyProtocol(first="A")/"ABC")
 .
 Sent 1 packets.


.. explain FSM and key mechanisms

Defining the header of the protocol is simple in scapy_ with simple
protocols. Besides specifying the format of the header, you also need
to define the behavior of a sender and a receiver implementing your
protocol. scapy_ defines a set of base classes that can be used to
implement simple Finite State Machines. You will use these FSMs to
implement your simple transport protocol. A FSM is implemented as a
python_ class that extends the Automaton class provided by scapy_ A
FSM contains :

 - implementation of the `parse_args` method that is used to parse the
   arguments provided when creating the FSM
 - implementation of the `master_filter` method that specifies how
   scapy_ will capture on the network the packets that must be
   processed by the FSM. 
 - states, conditions and timeouts that implement the FSM

The `parse_args` allows you to specify parameters for your FSM when
creating it. For a sender, you can use something like ::

 class MyProtocolSender(Automaton):
        def parse_args(self, payloads, receiver,**kargs):
                Automaton.parse_args(self, **kargs)
                self.receiver = receiver
                self.q = Queue.Queue()
                for item in payloads:
                        self.q.put(item)

  	def master_filter(self, pkt):
                  return (IP in pkt and pkt[IP].src == self.receiver
                  and MyProtocol in pkt)


This method specifies a set of messages (e.g. a list of Strings) to be
sent and the address of the receiver as a String. It places all the
messages in a Queue to be processed later and remembers the address of
the receiver. The `master_filter` method instructs scapy_ to capture
all the IP packets that it receives from `self.receiver` and contain a
MyProtocol segment.

For a receiver, you could use something like ::

 class Receiver(Automaton):
        def parse_args(self, sender, **kargs):
                Automaton.parse_args(self, **kargs)
                self.sender = sender

	def master_filter(self, pkt):
                return (IP in pkt and pkt[IP].src == self.sender and
                MyProtocol in pkt)

In this case, we only specify the address of the sender as a String.
The `master_filter` method instructs scapy_ to capture all the IP
packets that it receives from `self.sender` and contain a MyProtocol segment.

In scapy_, an automaton has different states. A `start` state and
possibly some `end` and `error` states. There are transitions from one state
to another. These transitions can depend on a specific condition, the
reception of a specific packet or the expiration of a timeout. When a
transition is taken, scapy_ will run the actions that have been bound
to this transition. It is possible to pass parameters from states to
transitions and the opposite. From a programmer's point of view,
states, transitions and actions are methods from an Automaton
subclass. They are decorated to provide meta-information needed in
order for the automaton to work.

A first and simple FSM is to capture all the packets using MyProtocol
and display them. This can be achieved by defining one state which is
the initial one and one receive condition that is associated to this
state and is triggered every time the FSM is in this state and a packet
is received by the `master_filter` specified above ::

	@ATMT.state(initial=1)  ## initial state
	def WAIT_PDU (self):
		print "State: WAIT_PDU"
		pass
		
	@ATMT.receive_condition(WAIT_PDU)
	def wait_pdu (self, pkt):
	        print "received ",pkt.show()
		raise self.WAIT_PDU()		


This FSM is always in the `WAIT_PDU` state. The `wait_pdu()` method is
attached to the `WAIT_PDU` state as a receive condition by using the
`@ATMT.receive_condition(WAIT_PDU)` decorator.  The  `wait_pdu()`
method simply prints all packets using the `MyProtocol` protocol that
it receives by using the `show()` method of the Packet class. The
command `raise` forces the transition to the specified state of the
FSM. If you want to extract the payload of the received packet and print it, you can use ::

        payload = pkt.getlayer(MyProtocol).payload.load
        print "data received [[",payload,"]]"


Transport protocols often use timers and the scapy_ automatons allow
you to easily define timers to for example retransmit an
unacknowledged segment. This is done by using the `@ATMT.timeout()`
and `@ATMT.action()` decorators.

For example, let us consider a simple sender that uses a timer to
protect the segments sent. In the `MyProtocolSender` class shown
above, we could add the following states and transitions ::

	@ATMT.state(initial=1)
	def WAIT_SDU (self):
		try:
			self.payload = self.q.get()
			print "data to be transmitted [[",self.payload,"]]"
                    	self.buffer=IP(dst=self.receiver)/MyProtocol(first="A")/self.payload
                        self.send(self.buffer)
                       raise self.WAIT_CTRL()
		except Queue.Empty:
			sys.exit(0)

	@ATMT.state()
	def WAIT_CTRL(self):
		print "State: WAIT_CTRL"
		
	# other states/transitions not shown

	@ATMT.timeout(WAIT_CTRL, 2)
        def timeout_waiting_for_ctrl(self):
                raise self.WAIT_CTRL()
        
        @ATMT.action(timeout_waiting_for_ctrl)
        def retransmit(self):
                self.send(self.buffer)

The initial state simply processes the Queue containing all the
SDUs as defined in `MyProtocolSender` above. It sends one SDU at a
time then goes to the `WAIT_CTRL` state where the acknowledgments
will be processed (this part is not shown here). Note that the last
segment sent is stored in `self.buffer`. The timeout
`timeout_waiting_for_ctrl` is associated to the `WAIT_CTRL` state and
has a duration of 2 seconds [#ftimeout]_. When the timeout expires,
the action associated to it is executed. In this case, the FSM will
retransmit the packet and the FSM will transition to the `WAIT_CTRL`
state as indicated in the timer definition.

Once a FSM has been written, you can use it from scapy_ by creating an
instance of your FSM and start its `run()` method ::

 Welcome to Scapy (2.0.1-dev)
 >>> s=Sender(("A","B","C"),"192.168.56.102")
 >>> s.run()

You can also use the `next()` method to execute the transitions one by one.

You can find additional information about scapy_ in its official
documentation : http://www.secdev.org/projects/scapy/doc/
However, note that this document was written mainly for security
specialists who already know the bit-level details of many
protocols. Most of the students following this course are unlikely to
have already this experience... The only part of the scapy
documentation that could be useful for this exercise is the
description of the automatons : http://www.secdev.org/projects/scapy/doc/advanced_usage.html#automata


Implementing the Alternating Bit Protocol in scapy_
---------------------------------------------------

The Alternating Bit Protocol (ABP) is the simplest protocol that provides a
reliable data transfer in the transport layer. Your objective for this
week is to implement, by teams of two students, either the Sender or
the receiver part of the ABP. For this, you should probably work as
follows :

 - define in the entire group a common format for the ABP header and
   specify the corresponding ABP class that extends the Packet class
 - divide the group in teams of two students (a team of 3 is allowed
   if the number of students in the group is odd)
 - schedule an interoperability meeting with another team during which
   you can test your Sender with their Receiver (or the opposite)
 - write your implementation in python by changing the `abp.py file in
   `scapy/layers` in the scapy_ distribution provided
 - perform the interoperability test and verify that your
   implementation works correctly

To ease the implementation, we will ignore the utilization of a
checksum in the Alternating Bit Protocol. In the emulated environment
that you will use, losses are unlikely to occur, but you can of course
easily create them inside your sender or receiver FSM. For this, you
can reuse the standard python classes, such as :

 - in the `random` class, you can use the `random.random()` method to
   generate a random number and use it to probabilistically drop a
   packet before sending it in the sender or receiving it in the
   receiver. The drop probability could be a parameter that you
   specify when creating your FSM. This would allow you to easily
   simulate the effect of transmission errors on your protocol.
 - in the `time` class, you can use the `time.sleep()` class to create
   delays when processing messages 


Running scapy_ in the lab
-------------------------


To allow you to write the required scapy_ extensions without losing
too much time with practical problems in installing and configuring
software, we have prepared an emulated environment that runs in the
computing labs. This environment is composed of two User Mode Linux
(UML_) images. A UML image is an emulated machine containing a Linux
kernel, a complete filesystem and the necessary utilities. This UML
image runs as a process on a Linux workstation such as those in the
computing lab.

.. warning::

 Although scapy_ can work on MacOS and Windows, we recommend that you
 use the special version of User Mode Linux that we have prepared
 instead of spending time to install scapy_ on your own
 machines. Please note also that the fact that we use scapy_ for the
 basic networking course cannot be considered as an authorization to
 send specially crafted packets in the campus network or on the
 Internet. Such specially crafted packets may be considered by system
 administrators as a security attack to which they may react.


.. figure:: fig/UML_setup.png
   :align: center
   :scale: 50 

The filesystems and the kernel of the virtual machines are stored
in the directory `/etinfo/applications/INGI2141/uml`. To create the
virtual setup illustrated on the figure execute the following procedure:

#. Copy the boot script of each virtual machines in your working directory ::

	cp /etinfo/applications/INGI2141/uml/start_uml1 ~/INGI2141/UML
	cp /etinfo/applications/INGI2141/uml/start_uml2 ~/INGI2141/UML

#. Open 2 terminals, 1 for each virtual machine

#. In the first terminal, start the virtual machine UML1 by executing
   the script `start_uml1`. 
   In the second terminal, start the virtual machine
   UML2 by executing the script `start_uml2`.

#. Once the machines will have finished their boot process, you can login
   on each machine as root. Each UML machine has an Ethernet interface
   named `eth0` that is directly connected to the other UML
   machine. To check their virtual IP connectivity by pinging the
   IP of the interfaces on the other end of the virtual link by executing the
   following commands ::

	ping 192.168.1.1
	ping 192.168.1.2

You can share files between the virtual machines and the machine where you
are running the User Mode Linux processes in the directory `/mnt/host` of the
virtual machines.

You will also find in the `/root` directory of the emulated machines
the `scapy-2.01` directory that contains a modified scapy_
source code. This version of scapy_ has been modified by adding a new
protocol called ABP (Alternating Bit Protocol) and configuring scapy_
with the necessary hooks to understand this protocol. ABP is located
in file `scapy/layers/abp.py` of the scapy_ archive. You should modify
this file (and only this file) to create :

 - your own header by extending the scapy_ Packet class in file `scapy/layers/abp.py` 
 - your sender [#fstest]_ FSM 
 - your receiver [#frtest]_ FSM 

Once you have modified `abp.py`, you should recompile scapy_ and
reinstall it on the two emulated Linux machines. This can be done by
using ::

  python setup.py  clean
  python setup.py  install
 
These commands should be run in the root of the scapy_
distribution. The second command will reinstall your modified version
of scapy_. Check its output to verify that there are no compilation
errors. As python_ is an interpreted language, you may also detect
errors at runtime. 

.. note::

 As scapy_ does not completely support the loopback interface, you
 should only use it on the Ethernet interfaces of the UML machines. Do
 not waste your time trying to run scapy_ on a loopback interface.


.. rubric:: Footnotes


.. [#fsport] The specification of the UDP source port field in scapy_ contains three parameters. The first one is the name of the field, which can be used to set the value of this field when creating a packet. The second value is the default. The source port is set to `53` when not specified at packet creation time. The last parameter for an enumerated field is the list of names for all UDP services. This list is automatically created by scapy_ from the `/etc/services` file on a Linux host so that you can specify `dns` as source port instead of 53.

.. [#ftimeout] For this exercise, consider a fixed timeout value. We will discuss later on how to correctly choose a timeout value.

.. [#fstest] If your team of two students implements a sender FSM, you can test it by using on the other UML machine a simple FSM that has a single state and prints all received segments (see the example with the `WAIT_PDU`  state) 

.. [#frtest] If your team of two students implements a receiver FSM, you can test it by manually sending segments using `send()` from scapy_



.. include:: ../../book/links.rst
