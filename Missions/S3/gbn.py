## This file abstract a simple GBN based transport protocl
## Olivier Bonaventure
## UCL - INL <http://inl.info.ucl.ac.be>

import Queue,sys
from scapy.packet import *
from scapy.fields import *
from scapy.automaton import *
from scapy.layers.inet import *
from math import pow

TIMEOUT = 1

NBITS=4      # number of bits used to encode the sequence number field
assert NBITS<=8

# the header of the simplified Go-Back-N protocol

class GBN(Packet):
    name = "Go-Back-N (INGI2141) "
    fields_desc=[ BitEnumField("type",0,1, {0:"data", 1:"ack"}), # type of segment : data or ack 
                  BitField("padding" , 0 , 7), # padding
                  ShortField("len", None), # segment length in bytes
                  ByteField("num",0),  # sequence number in data, ack number in ack segments, incremented by one in each segment
                  ByteField("win",0) # receiving window (ignored in data) in number of segments
                  ,]

    # automatic computation of the length
    def post_build(self, p, pay):
        p += pay
        l = self.len
        if l is None:
                l = len(p)
                p = p[:1]+struct.pack("!H",l)+p[4:]
        return p

bind_layers(IP,GBN, frag=0, proto=222)

if __name__ == "__main__":
    interact(mydict=globals(), mybanner="INGI2141: GBN ")

## This class implements the sender side of the Alternating Bit Protocol by using scapy Automaton facilities

class GBNSender(Automaton):
	def parse_args(self, payloads, win, receiver,**kargs):
        	Automaton.parse_args(self, **kargs)
                self.win=win # the maximum window size of the sender
                assert self.win<pow(2,NBITS)
        	self.receiver = receiver # the IP address of the receiver
       		self.q = Queue.Queue()
		for item in payloads:
			self.q.put(item)

                ## Additional state variables to be maintained        
                self.buffer={} # empty dictionnary
                self.current=0 # current sequence number
                self.unack=-1 # last unacked segment, -1 is none
                self.currentwin=win # current window advertised by receiver, initialised at win, could be 1 instead

                        
	def master_filter(self, pkt):
        	return (IP in pkt and pkt[IP].src == self.receiver and GBN in pkt)
		
	@ATMT.state(initial=1)
	def BEGIN (self):
            raise self.WAIT_ACK()
            

        @ATMT.state()
        def WAIT_ACK(self):
              # to be completed
              if len(self.buffer.keys())<min(self.win,self.currentwin):
                  try:
                      payload = self.q.get()
                      print "sending [[",payload,"]]"
                      self.buffer[self.current]=payload
                      p=IP(dst=self.receiver)/GBN(type="data",win=(self.win-len(self.buffer.keys()),num=self.current)/payload
                      print "buffer contents"
                      for p in self.buffer.keys():
                          print p," -> ",self.buffer[p]
                      
                      if(self.unack<0):
                          self.unack=self.current
                      self.current=int((self.current+1)%pow(2,NBITS))
                      raise self.WAIT_ACK()
                  except Queue.Empty:
                      if self.unack ==-1:
                          print "Done"
                          sys.exit(0)
                      else:
                          pass
              else:
                  pass
	
	@ATMT.receive_condition(WAIT_ACK)
	def wait_for_ack(self,pkt):
            # to be completed
            print "Received ack : ",pkt.getlayer(GBN).num
            ptype = pkt.getlayer(GBN).type
            if ptype == 0:
                print "Error : data received ",pkt
            else:
                ack=pkt.getlayer(GBN).num
                seq=self.unack
                self.currentwin=pkt.getlayer(GBN).win
                while seq!=int((ack)%pow(2,NBITS)):
                    print "removing ",seq," from buffer "
                    self.buffer.pop(seq)
                    seq=int((seq+1)%pow(2,NBITS))
            if self.current!=int( (ack)%pow(2,NBITS) ):
                self.unack=int( (ack)%pow(2,NBITS) )
            else:
                self.unack=-1   # no unacked segment
            raise self.WAIT_ACK()

	

	@ATMT.timeout(WAIT_ACK, TIMEOUT)
	def timeout_wait_ack(self):
            # to be completed
            # retransmit unacked segments
             seq=self.unack
             while seq!=self.current:
                    print "retransmitting ",seq," from buffer ",self.buffer[seq]
                    send(IP(dst=self.receiver)/GBN(type="data",win=self.win,num=seq)/self.buffer[seq])
                    seq=int((seq+1) % pow(2,NBITS))

             raise self.WAIT_ACK()       
                         


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
            if self.dbg==True:
                print "Waiting for segment ",self.next
            pass
	
	@ATMT.receive_condition(WAIT_SEGMENT)
	def wait_segment (self, pkt):
            if random.random() < self.pdata :
                # received segment was lost/corrupted in the network
                if self.dbg==True:
                    print " Lost : [type=",pkt.getlayer(GBN).type,", num=",pkt.getlayer(GBN).num," ,win=",pkt.getlayer(GBN).win,"]"

                raise self.WAIT_SEGMENT()
                    
            else:
                # segment was received correctly
                if self.dbg==True:
                    print " Received : [type=",pkt.getlayer(GBN).type,", num=",pkt.getlayer(GBN).num," ,win=",pkt.getlayer(GBN).win,"] payload=",pkt.getlayer(GBN).payload

                # check is segment is a data segment    
		ptype = pkt.getlayer(GBN).type
                if ptype==0:
                    if pkt.getlayer(GBN).num==self.next:
                        # this is the segment with the expected sequence number
                        print "data received :",pkt.getlayer(GBN).payload
                        self.next=int((self.next+1) %  pow(2,NBITS))
                    else:
                        # this was not the expected segment
                        if self.dbg==True:
                            print "Out of sequence segment [",pkt.getlayer(GBN).num,"] received "
                else:
                    # we received an ack while we are supposed to receive only data segments
                    print "ERROR: Received ack segment : ",pkt.show()
                    sys.exit(-1)

                # send ack back to sender    
                if random.random() < self.pack :
                    # the ack will be lost, discard it
                    if self.dbg==True:
                        print " Lost ack:",self.next
                else:
                    # the ack will be received correctly
                    if self.dbg==True:
                        print " Sending ack :",self.next
                    send(IP(dst=self.sender)/GBN(type="ack",num=self.next,win=self.win))  
                # transition to WAIT_SEGMENT to receive next segment     
                raise self.WAIT_SEGMENT()

			
