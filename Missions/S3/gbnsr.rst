Go-back-n and selective repeat
==============================

Go-back-n and selective repeat are the basic mechanisms used in
reliable window-based transport-layer protocols. During this exercise,
you will implement a go-back-n (GBN) sender using scapy_. In each
group, you will write one sender per team of two students.

The deadline for this exercise is Tuesday October 13th, 2009 at 13.00.

Partial implementation of a simplified GBN receiver in scapy_
.............................................................

Our go-back-n protocol relies on a very simple header that can be
implemented by the following scapy_ class ::

 NBITS=4      # number of bits used to encode the sequence number field
 assert NBITS<=8 # precondition

 # the header of the simplified Go-Back-N protocol

 class GBN(Packet):
    name = "Go-Back-N (INGI2141) "
    fields_desc=[ BitEnumField("type",0,1, {0:"data", 1:"ack"}), # type of segment : data or ack 
                  BitField("padding" , 0 , 7), # padding
                  ShortField("len", None), # segment length in bytes
                  ByteField("num",0),  # sequence number in data, ack number in ack segments, incremented by one in each segment
                  ByteField("win",0) # receiving window (ignored in data) in number of segments
		  # real protocol would contain a checksum
                  ,]

    # automatic computation of the length
    def post_build(self, p, pay):
        p += pay
        l = self.len
        if l is None:
                l = len(p)
                p = p[:1]+struct.pack("!H",l)+p[3:]
        return p

 bind_layers(IP,GBN,proto=222)

Our header contains the following information :
 - the first bit indicates whether the segment contains data or only
   an acknowledgment
 - the second and third bytes contain the segment length. This length
   is automatically computed by the `post_build` method
 - the fourth byte contains an 8 bits integer. When used in a `data`
   segment, this integer is the sequence number of the segment. In our
   simple go-back-n protocol, the sequence number is incremented by
   one every time a segment is sent. When used in an `ack` segment, 
   the fourth byte contains the sequence number of the next segment
   that is expected by the receiver. The constant NBITS allows you to
   change the number of bits used to encode the sequence number. Of course, as the sequence number is encoded as a one byte field, the NBITS cannot be larger than 8. Note that the size of the `num` field is not adjusted if you change the NBITS constant.
 - the last byte contains the receiver's window. 


The class `GBNReceiver` below is a simple FSM of a receiver for our
simple go-back-n protocol ::

 ## This class implements the receiver side of the GBN protocol by using scapy Automaton facilities

 class GBNReceiver(Automaton):
	def parse_args(self, window, pdata, pack, debug, sender, **kargs):
		Automaton.parse_args(self, **kargs)
                self.win=window       # window size advertised by receiver in segments
                assert self.win <= pow(2,NBITS)
                self.pdata=pdata      # loss probability for data segments 0<= proba < 1
                assert 0<=pdata and pdata<1
                self.pack=pack        # loss probability for acks  0<= proba < 1
                assert 0<=pack and pack<1
                self.dbg=debug        # True if debug output is requested, false otherwise
		self.sender = sender  # ip address of sender
                self.next=0           # next expected sequence number

	def master_filter(self, pkt):
        	return (IP in pkt and pkt[IP].src == self.sender and GBN in pkt)

	@ATMT.state(initial=1)
	def WAIT_SEGMENT (self):
            if self.dbg:
                print "Waiting for segment ",self.next
            pass
	
	@ATMT.receive_condition(WAIT_SEGMENT)
	def wait_segment (self, pkt):
            if random.random() < self.pdata :
                # received segment was lost/corrupted in the network
                if self.dbg:
                    print " Lost : [type=",pkt.getlayer(GBN).type,",
	num=",pkt.getlayer(GBN).num," ,win=",pkt.getlayer(GBN).win,"]"
	
	        raise self.WAIT_SEGMENT()
                    
            else:
                # segment was received correctly
                if self.dbg:
                    print " Received : [type=",pkt.getlayer(GBN).type,", num=",pkt.getlayer(GBN).num," ,win=",pkt.getlayer(GBN).win,"] payload=",pkt.getlayer(GBN).payload

                # check if segment is a data segment    
		ptype = pkt.getlayer(GBN).type
                if ptype==0:
                    if pkt.getlayer(GBN).num==self.next:
                        # this is the segment with the expected sequence number
                        print "data received :",pkt.getlayer(GBN).payload
                        self.next=int((self.next+1) %  pow(2,NBITS))
                    else:
                        # this was not the expected segment
                        if self.dbg:
                            print "Out of sequence segment [",pkt.getlayer(GBN).num,"] received "
                else:
                    # we received an ack while we are supposed to receive only data segments
                    print "ERROR: Received ack segment : ",pkt.show()
                    sys.exit(-1)

                # send ack back to sender    
                if random.random() < self.pack :
                    # the ack will be lost, discard it
                    if self.dbg:
                        print " Lost ack:",self.next
                else:
                    # the ack will be received correctly
                    if self.dbg:
                        print " Sending ack :",self.next
                    send(IP(dst=self.sender)/GBN(type="ack",num=self.next,win=self.win))  
                # transition to WAIT_SEGMENT to receive next segment     
                raise self.WAIT_SEGMENT()


The `GBNReceiver` constructor takes the following arguments :
 - the receiving window (in segments)
 - the loss probabilities for the `data` and `ack` segments. In our emulated network, the `GBNReceiver` models segment losses by probabilistically discarding the received `data` segments or probabilistically discarding the `ack` segments before sending them
 - a debug flag that causes the FSM to print debugging information when set to `True`
 - the IP address of the sender

The `GBNReceiver` is implemented as a single state FSM. This FSM
receives data segments in the `WAIT_SEGMENT` state. These segments are
handled by the `wait_segment` receive condition that operates as follows.
 - the receive condition first checks whether the received segment should be probabilistically discarded. 
 - the segment is verified to check that it is a `data` segment
 - the FSM verifies that the received segment has the expected sequence number. This is done thanks to the `self.next` state variable that is maintained by the FSM. If the expected sequence number was received `self.next` is incremented by :math:`~1~mod~2^{NBITS}`
 - the acknowledgment is sent. In our simple protocol, the `num` field in the `ack` segment always contains the sequence number of the next expected segment (i.e. the sequence number of the last segment received in sequence :math:`~+1~mod~2^{NBITS}`)


Preliminary questions
......................

The following questions should help you to prepare your implementation of the go-back-n sender FSM.

#. As the sequence number are encoded by using NBITS, there are only :math:`2^{NBITS}` different sequence numbers. How do you compute the sequence number that follows sequence number `x` ?

#. A go-back-n sender must contain a sending buffer where it stores the segments that have been sent without having already been acknowledged. Which kind of python_ data structure [#fpythondata]_ will you use to build this buffer ? ( do not develop your own optimized data structure, reuse a data structure that python already supports - the chosen data structure should allow you to easily associate a sequence number with a corresponding segment/payload, count the number of segments/payloads stored and check whether a given sequence number is already in the sending buffer or not)

#. The maximum capacity of your sending buffer is the window size of your FSM. How do you check whether your sending buffer is full ?

#. When there are no losses, you will need to remove from your sending buffer a `data` segment every time an `ack` segment is received. How do you remove from the chosen data structure `the` segment that is acknowledged by the received `ack` ?

#. `data` segments are protected against losses by using the retransmission timer and the go-back-n mechanism. `ack` segments are protected against losses due to the fact that when an `ack` segment with `num` set to `x` is received, it acknowledges all `data` segments that were sent before segment `x`. Thus, when you receive an `ack`, you may need to remove `0`, `1` or more acknowledged `data` segments from your sending buffer. How do you decide which data segments must be removed from the sending buffer when you receive an acknowledgment ?

#. How can you detect that all the data segments that you have sent have been acknowledged ?

#. When the timer expires, what are the segments that should be retransmitted ? How do you retransmit them ?

Implementation of the sender FSM
................................

To implement the FSM for your go-back-n sender, you can start from the
skeleton FSM below that is composed of two states, one timeout and one
receive condition ::

 ## This class implements the sender side of the go-back-n Protocol by
   using scapy Automaton facilities

 TIMEOUT=1  # default timeout in seconds

 class GBNSender(Automaton):
	def parse_args(self, sdus, win, receiver,**kargs):
        	Automaton.parse_args(self, **kargs)
                self.win=win # the maximum window size of the sender
                assert self.win<pow(2,NBITS)
        	self.receiver = receiver # the IP address of the receiver
       		self.q = Queue.Queue()
		for item in sdus:
			self.q.put(item)

                ## Additional state variables to be maintained        
                       
	# filter for GBN segments	       
	def master_filter(self, pkt):
        	return (IP in pkt and pkt[IP].src == self.receiver and GBN in pkt)
		

	@ATMT.state(initial=1)
	def BEGIN (self):
            raise self.WAIT_ACK()
            

        @ATMT.state()
        def WAIT_ACK(self):
              # to be completed
	
	@ATMT.receive_condition(WAIT_ACK)
	def wait_for_ack(self,pkt):
            # to be completed, wait for acks

	@ATMT.timeout(WAIT_ACK, TIMEOUT)
	def timeout_wait_ack(self):
            # to be completed
            # retransmit unacked segments
            
           
The constructor of the `GBNSender` takes a list of SDUs as arguments and places them in a `Queue <http://docs.python.org/library/queue.html>`_ . This can be used to model the `data.request()` primitives from the sending user. The `payloads` list should be a list of Strings. You can easily create a long list of Strings by using ::

 l=[]
 for f in range(1000) : l.append(str(f))

To extract the next SDU from the Queue, you can use e.g. ::

 try:
      # extract one additional SDU
      payload = self.q.get()
      ...
 except Queue.Empty:
      # All SDUs have been sent
      # stop sender only once all data has been acknowledged


To test your `GBNSender`, you can use the `GBNReceiver` shown above. The `GBNReceiver` expects to receive a first `data` segment with sequence number `0`. Your `GBNSender` must thus start to number the segments that it sends at `0`. You should first try to test it with loss probabilities set to 0 for both `data` and `ack` segments. Then, try to see how your `GBNSender` works when `data` segments are lost and after that add losses for the `ack` segments as well. Do not forget to send a list of SDUs that contains more than :math:`2^{NBITS}` Strings.      

To implement the go-back-n receiver, you can reuse the UML machines that you used for the Alternating Bit Protocol. A new protocol can be added to the scapy_ distribution as follows :

 - create the file `scapy/layers/gbn.py` that will contain your protocol. Reuse the python imports that were defined for the Alternating Bit Protocol and copy the code of the go-back-receiver shown above
 - change the `scapy/config.py` and add "gbn" at the end of the `load_layers` line ::
    
    load_layers = ["l2", "inet", "dhcp", "dns", "dot11", "gprs", "hsrp", "inet6", "ir", "isakmp", "l2tp", "mgcp", "mobileip", "netbios", "netflow", "ntp", "ppp", "radius", "rip", "rtp", "sebek", "skinny", "smb", "snmp", "tftp", "x509", "bluetooth", "dhcp6", "llmnr", "abp", "gbn" ]

 - recompile scapy (`python setup clean` and `python setup install`) and you are ready to implement your go-back-n sender.

Deliverables
............

For this week, you need to provide in your group's subversion repository :

 - one implementation in python per team of two students (if the number of students in the group is odd, one team can be composed of three students). The code should be readable, of course
 - a short description in ASCII of the tests that you performed with your implementation and its limitations

.. rubric:: Footnotes

.. [#fpythondata] The basic data structures of the python_ library are described in http://docs.python.org/tutorial/datastructures.html and http://docs.python.org/library/stdtypes.html



.. include:: ../../book/links.rst


