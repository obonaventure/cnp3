==============================================
The datalink layer and the Local Area Networks
==============================================


The datalink layer is the lowest layer of the reference model that we discuss in details. As mentioned previously, there are two type of datalink layers. The first datalink layers that appeared are the ones that are used on point-to-point links between endsystems that are directly connected by a physical link. We will briefly discuss one of these datalink layers in this chapter. The second type of datalink layers are the ones used in Local Area Networks. The main difference between the point-to-point and the LAN datalink layers is that the latter need to regulate the access to the Local Area Network which is usually a shared medium. 
This chapter is organised as follows. We first discuss the principles and of datalink layer and the service that it uses from the physical layer. Then we describe in more details several Medium Access Control algorithms that are used by Local Area Networks to regulate the access to the shared medium. Finally we discuss in details several important datalink layer technologies with an emphasis on Ethernet.

Principles
##########

The datalink resides above and uses the service provided by the physical layer. Although there are many different implementations of the physical layer from a technological viewpoint, they all provide a service that enables the datalink layer to send and receive bits to/from another directly connected endsystem. The datalink layer receives packets from the network layer. Two datalink layer entities exchange `frames`. As explained in the previous chapter, most datalink layer technologies impose limitations on the size of the frames. Some technologies impose only a maximum frame size, others enforce both minimum and maximum frames sizes and finally some technologies only support a single frame size. In the latter case, the datalink layer will usually include an adaptation sublayer to allow the network layer to send and receive variable-length packets. This adaptation layer may include fragmentation and reassembly mechanisms.

.. figure:: png/lan-fig-003-c.png
   :align: center
   :scale: 70
   
   The datalink layer and the reference model

The physical layer service allows to send and receive bits. Compared to the requirements of the applications, it is usually far from imperfect as explained in the introduction :

 - The Physical layer may change, e.g. due to electromagnetic interferences, the value of a bit being transmitted
 - the Physical layer may deliver `more` bits to the receiver than the bits sent by the sender
 - the Physical layer may deliver `fewer` bits to the receiver than the bits sent by the sender

The datalink layer must be able to allow endsystems to exchange frames containing packets despite of these limitations. On point-to-point links and Local Area Networks, the first problem to be solved is how to encode a frame as a sequence of bits so that the receiver can easily recover the received frame despite the limitations of the physical layer.

.. index:: framing

If the physical layer was perfect, the problem would be very simple. The datalink layer would simply need to define how to encode each frame as a sequence of consecutive bits. The receiver would then be able to easily extract the frames from the received bits. Unfortunately, the imperfections of the physical layer make this framing problem slightly more complex. Several solutions have been proposed and are used in practice in different datalink layer technologies.

Framing
=======

The `framing` problem can be phrased as : "`How does a sender encodes frames so that the receiver can efficiently extract them from the stream of bits that it receives from the physical layer`". 

A first solution to solve the framing problem is to require the physical layer to remain idle for some time after the transmission of each frame. These idle periods can be detected by the receiver and server as a marker to delineate frame boundaries. Unfortunately, this solution is not sufficient for two reasons. First, some datalink layers cannot remain idle and need to always transmit bits. Second, inserting an idle period between frames decrease the maximum bandwidth that can be achieved by the datalink layer.

.. index:: Manchester encoding

Some physical layers provide an alternative to this idle period. All physical layers are able to send and receive physical symbols that represent values `0` and `1`. However, tor various reasons that are outside the scope of this chapter, several physical layers are able to exchange other physical symbols as well. For example, the Manchester encoding used in several physical layers allows to send four different symbols. The Manchester encoding is a differential encoding scheme in which time is divided in fixed-length periods. Each period is divided in two halves and two different voltage levels can  be applied. To send a symbol, the sender must set one of these two voltage levels during each half period. To send a `1` (resp. `0`), the sender must set a high (resp. low) voltage during the first half of the period and a low (resp. high) voltage during the second half. This encoding ensures that there will be a transition at the middle of each period and allows the receiver to synchronise its clock to the sender's clock. Besides, the encodings for `0` and `1`, the Manchester encoding also supports two additional symbols : `InvH` and `InvB`  where the same voltage level is used during the two half periods. By definition, these two symbols cannot appear in the content of a frame which is only composed of `0` and `1`. Some technologies use these special symbols as markers at the beginning or end of frames.

.. figure:: png/lan-fig-006-c.png
   :align: center
   :scale: 70
   
   Manchester encoding

.. index:: bit stuffing, stuffing (bit)

Multi-symbol encodings cannot be used by all physical layers and a generic solution that can be used with any physical layer that is able to transmit and receive only `0` and `1` is required. This generic solution is called `stuffing` and two variants exist : `bit stuffing` and `character stuffing`. To enable a receiver to easily delineate the frame boundaries, these two techniques reserve special bit strings as frame boundary markers and encode the frames so that these special bit strings do not appear inside the frames.

`Bit stuffing` reserves the `01111110` bit string as the frame boundary marker and ensures that there will never be six consecutive `1` bits transmitted inside a frame. With bit stuffing, a frame is sent as follows. First, the sender transmits the marker, i.e. `01111110`. Then, the sender sends all the bits of the frame and inserts an additional bit set to `0` after each sequence of five consecutive `1` bits. This ensures that the sent frame never contains a sequence six consecutive bits set to `1`. As a consequence, the marker pattern does not appear inside the frame sent. The marker is also sent at the end of the frame. The receiver performs the opposite to decode the received frame. It first detects the beginning of the frame with the `01111110` marker. Then, it processes the received bits and counts the number of consecutive bits set to `1`. If a `0` follows five consecutive bits set to `1`, this bit is removed as it was inserted by the sender. If a `1` follows five consecutive bits sets to `1`, it indicates a marker if it is followed by a bit set to `0`.

For example, consider the transmission of packet `0110111111111111111110010`. Then sender will first send the `01111110` marker followed by `011011111`. After these five consecutive bits set to `1`, it inserts a bit set to `0` followed by `11111`. A new `0` is inserted, followed by `11111`. A new `0` is inserted followed by the end of the frame `110010` and the `01111110` marker.

`Bit stuffing` increases the number of bits required to transmit a given frame. The worst case for bit stuffing is of course a long sequence of bits set to `1` inside the frame. If transmission errors occur, stuffed bits or markers can be in error. In these cases, the frame affected by the error and possibly the next frame will be wrongly decoded by the receiver, but it will be able to resynchronise itself at the next valid marker. 


.. index:: character stuffing, stuffing (character)

`Bit stuffing` can be easily implemented in hardware. However, implementing it in software is more complex. As software implementations prefer to process characters than bits, software-based datalink layers usually use `character stuffing`. This technique operates on frames that contain an integer number of characters. Some characters are used as markers to delineate the frame boundaries. Many `character stuffing` techniques use the `DLE`, `STX` and `ETX` characters of the ASCII character set. `DLE STX` (resp. `DLE ETX`) is used to mark the beginning (end) of a frame. When transmitting a frame, the sender adds a `DLE` character after each transmitted `DLE` character. This ensures that none of the markers can appear inside the transmitted frame. The receiver detects the frame boundaries and remove the second `DLE` when it receives two consecutive `DLE` characters. For example, to transmit frame `1 2 3 DLE STX 4`, a sender will first send `DLE STX` as a marker, followed by `1 2 3 DLE`. Then, the sender transmits an additional `DLE` character followed by `STX 4` and the `DLE ETX` marker.

`Character stuffing` like bit stuffing increases the length of the transmitted frames. For `character stuffing`, the worst frame is a frame containing many `DLE` characters. When transmission errors occur, the receiver may incorrectly decode one or two frames (e.g. if the errors occur in the markers). However, it will be able to resynchronise itself with the next correctly received markers.

In practice, datalink layer protocols combine one of these techniques with a length indication in the frame header and a checksum or CRC. The checksum/CRC is computed by the sender and placed in the frame before applying bit/character stuffing.


Medium Access Control
=====================

Point-to-point datalink layers need to select one of the framing techniques described above and optionally add retransmission algorithms such as those explained for the transport layer to provide a reliable service. Datalink layers for Local Area Networks face two additional problems. A LAN is composed of several hosts that are attached to the same shared physical medium. From a physical layer viewpoint, a LAN can be organised in four different ways :

 - a bus-shaped network where all hosts are attached to the same physical cable
 - a ring-shaped where all hosts are attached to an upstream and a downstream node so that the entire network forms a ring
 - a star-shaped n
 - a wireless network where all hosts can send and receive frames by using radio signals

These four basic physical organisations of Local Area Networks are shown graphically in the figure below. We will first focus on one physical organisation at a time and will discuss later in the next section how to build networks combining several of these building blocks.

.. figure:: png/lan-fig-007-c.png
   :align: center
   :scale: 70
   
   Bus, ring and star-shaped Local Area Network 

Static allocation methods
-------------------------

FDM and TDM

.. figure:: png/lan-fig-012-c.png
   :align: center
   :scale: 70
   
   Time-division multiplexing in a ring-shaped LAN

explain collision


ALOHANet
--------

.. index:: packet radio

In the 1960s computers were mainly mainframes with a few dozens of terminals attached to them. These terminals were usually in the same building as the mainframe and were directly connected to it. In some cases, the terminals were installed in remote locations and connected through modems over dial-up lines. At the university of Hawaii¯, this organisation was not possible. Instead of using telephone lines to connect the distant terminals, they developed the first `packet radio` technology [Abramson1970]_. Until then, computer networks were built on top of either the telephone network or physical cables. AlohaNet showed that it was possible to use radio signals to interconnect computers.

.. index:: ALOHA

The first version of ALOHAnet, described in [Abramson1970]_, operated as follows. First, the terminals and the mainframe exchanged fixed-length frames composed of 704 bits. Each frame contained 80 8-bits characters, some control bits and parity information to detect transmission errors. Two channels in the 400 MHz range were reserved for the operation of ALOHANet. The first channel was used by the mainframe to send frames to all terminals. The second channel was shared among all terminals to send frames to the mainframe. As all terminals share the same transmission channel, there is a risk of collision. To deal with this problem and also transmission errors the mainframe verified the parity bits of the received frame and sent an acknowledgement on its channel for each correctly received frame. The terminals on the other hand had to retransmit the unacknowledged frames. As for TCP, retransmitting these frames immediately upon expiration of a fixed timeout is not a good approach as several terminals may retransmit their frames at the same time leading to a network collapse. A better approach, but still far from perfect, is for each terminal to wait a random amount of time after the expiration of its retransmission timeout. This avoids synchronisation among multiple retransmitting terminals. 


The pseudo-code below show the operation of an ALOHANet terminal. We use this python syntax for all Medium Access Control algorithms described in this chapter. The algorithm is run for each new frame that needs to be transmitted. It attempts to transmit a frame at most `max` times (`while loop`). Each transmission attempt is performed as follows. First, the frame is sent. Each frame is protected by a timeout. Then the terminal waits for either a valid acknowledgement frame or the expiration of its timeout. If the terminal receives an acknowledgement, the frame has been delivered correctly and the algorithm terminates. Otherwise, the terminal waits for a random time and attempts to retransmit the frame. 

::
 
 N=1
 while N<= max :
    send(frame)
    wait(ack on return channel or timeout)
    if ack on return channel:
       	break  # transmission was successful
    else:
	# timeout 
	wait(random time)
	N=N+1
  else:		
    # Too many transmission attempts

[Abramson1970]_ analysed the performance of ALOHANet under particular assumptions and found that ALOHANet worked well when the channel was lightly loaded. In this case, the frames are rarely retransmitted and the `channel traffic`, i.e. the total number of (correct and retransmitted) frames transmitted per unit of time is close to the `channel utilization`, i.e. the number of correctly transmitted frames per unit of time. Unfortunately, the analysis also reveals that the `channel utilization` reaches its maximum at :math:`\frac{1}{2 \times e}=0.186` times the channel bandwidth. At higher utilization, ALOHANet becomes unstable and the network collapses due to collided retransmissions.


.. sidebar:: Amateur packet radio

 Packet radio technologies have evolved in various directions since the first experiments performed at the University of Hawaii. The Amateur packet radio service developed by amateur radio operators is of these descendants of ALOHANet. Many amateur radio operators are very interested in new technologies and they often spend countless hours to develop new antennas or transceivers. When the first personal computers appeared, several amateur radio operators designed radio modems and their own datalink layers protocols [KPD1985]_ [BNT1997]_ . This network grew and it was possible by using only packet radio relays to connect to servers in several European countries. Some amateur radio operators also developed TCP/IP protocol stacks that were used over the packet radio service. Some parts of the `amateur packet radio network <http://www.ampr.org/>`_ is connected to the global Internet and uses the `44.0.0.0/8`. 

.. index:: slotted ALOHA

Many improvements to ALOHANet were proposed since the publication of [Abramson1970]_ and this technique or some of its variants are still found in wireless networks today. The slotted technique proposed in [Roberts1975]_ is important because it shows that a simple modification can significantly improve the channel utilization. Instead of allowing all terminals to transmit at [Roberts1975]_ Proposed to divide time in slots and allow the terminals to transmit only at the beginning of each slot. Each slot corresponds to the time required to transmit one fixed size frame. In practice, these slots can be imposed by a single clock that is received by all terminals. In ALOHANet, it could have been located on the central mainframe. The analysis in [Roberts1975]_ reveals that this simple modification improved the channel utilization by a factor of two. 
	


.. index:: CSMA, Carrier Sense Multiple Access


Carrier Sense Multiple Access
-----------------------------


ALOHA and slotted ALOHA can be easily implemented. Unfortunately, they can only be used in networks that are very lightly loaded. Designing a network for a very low utilisation is possible, but it clearly increases the cost of the network. To overcome these problems, many Medium Access Control mechanisms have been proposed. These mechanisms improve the channel utilization. Carrier Sense Multiple Access (CSMA) is a significant improvement compared to ALOHA. CSMA requires all nodes to listen to the transmission channel to verify that it is free before transmitting a frame [KT1975]_. When a node sense the channel to be busy, it defers its transmission until the channel becomes free again. The pseudo-code below provides a more detailed description of the operation of CSMA. 

.. index:: persistent CSMA, CSMA (persistent)

::
 
 N=1
 while N<= max :
    wait(channel becomes free)
    send(frame)
    wait(ack or timeout)
    if ack :
       	break  # transmission was successful
    else :
	# timeout 
	N=N+1
  else:		
    # Too many transmission attempts



The above pseudo-code is often called `persistent CSMA` [KT1975]_ as the terminal will continuously listen to the channel and transmit its frame as soon as the channel becomes free. Another important variant of CSMA is the `non-persistent CSMA` [KT1975]_. The main difference between persistent and non-persistent CSMA described in the pseudo-code below is that a non-persistent CSMA node does not continuously listens to the channel to determine when it becomes free. When non-persistent CSMA terminal senses the transmission channel to be busy, it waits for a random time before sensing the channel idle. This improves the channel utilization compared to persistent CSMA. With persistent CSMA, when two terminals sense the channel to be busy, they will both transmit (and thus cause a collision) as soon as the channel becomes free. With non-persistent CSMA, this synchronisation does not occur as the terminals wait a random time after having sensed the transmission channel. The higher channel utilization achieved by non-persistent CSMA comes at the expense of a slightly higher waiting time in the terminals when the network is lightly loaded. 


.. index:: non-persistent CSMA, CSMA (non-persistent)

::
 
 N=1
 while N<= max :
    listen(channel)
    if free(channel):
       send(frame)	
       wait(ack or timeout)
       if ack :
       	  break  # transmission was successful
       else :
	  # timeout 
	  N=N+1
    else:
       wait(random time)
  else:		
    # Too many transmission attempts

[KT1975]_ analyzes in details the performance of several CSMA variants. Under some assumptions about the transmission channel and the traffic, the analysis compares ALOHA, slotted ALOHA, persistent and non-persistent CSMA. Under these assumptions, ALOHA achieves a channel utilization which is only 18.4% of the channel capacity. Slotted ALOHA is able to use 36.6% of this capacity. Persistent CSMA improves the utilization by reaching 52.9% of the capacity while non-persistent CSMA achieves 81.5% of the channel capacity. 

.. index:: 


Carrier Sense Multiple Access with Collision Detection
------------------------------------------------------
.. index:: speed of light

CSMA improves the channel utilization compared to ALOHA. However, the performance can still be improved especially in wired networks. Consider the situation of two terminals that are connected to the same cable. This cable could for example be a coaxial cable as in the early days of Ethernet [Metcalfe1976]_. It could also be based on twisted pairs. Before extending CSMA, it is useful to understand more intuitively how frames are transmitted in such a network and how collisions can occur. The figure below illustrates the physical transmission of a frame on such a cable. To transmit its frame, host A must send an electrical signal on the shared medium. The first step is thus to begin the transmission of the electrical signal. This is point `(1)` in the figure below. This electrical signal will travel along the cable. Although electrical signals travel quickly, we know that information cannot travel faster than the speed of light (i.e. 300.000 kilometers/second). On a coaxial cable, an electrical signal is slightly slower than the speed of light and 200.000 kilometers per second is is reasonable estimation. This implies that if the cable has a length of one kilometer, the electrical signal will take 5 microseconds to travel from one end of the cable to the other. The ends of coaxial cables are equipped with termination points that ensure that the electrical signal is not reflected and returns to its source. This is illustrates at point `(3)` in the figure where the electrical signal has reach the left endpoint and host B. At this point, B starts to receive the frame being transmitted by A. Notice that there is a delay between the transmission of a bit on host A and its reception by host B. If there were other hosts attached to the cable, they would receive the first bit of the frame at slightly different times. As we will see later, this timing difference is key to understand the detailed operation. At point `(4)`, the electrical signal has reached both ends of the cable and occupies it completely. Host A continues to transmit the electrical signal until the of the the frame. As shown at point `(5)`, when the sending host stops its transmission, the electrical signal that corresponds to the end of the frame leaves the coaxial cable. The channel becomes empty again once all the electrical signal has been removed from the cable.


.. figure:: png/lan-fig-024-c.png
   :align: center
   :scale: 70
   
   Frame transmission on a shared bus 

Now that we have looked at how a frame is actually transmitted as an electrical signal on a shared bus, it is interesting to look in more details at what happens when two hosts transmit a frame almost at the same time. This is illustrated in the figure below where hosts A and B start their transmission at the same time (point `(1)`). At this time, if host C senses the channel, it will consider it to be free. This will not last a long time and at point `(2)` the electrical signals from both host A and host B reach host C. The combined electrical signal (shown graphically as the superposition of the two curves in the figure) cannot be decoded by host C. Host C detects a collision since its receives a signal that it cannot decode. Since host C cannot decode the frames, it cannot determine which hosts are sending the colliding frames. Note that host A (and host B) will detect the collision later than host C (point `(3)` in the figure below).

.. figure:: png/lan-fig-025-c.png
   :align: center
   :scale: 70
   
   Frame collision on a shared bus 

.. index:: collision detection, jamming

As shown above, hosts can detect collisions when they receive an electrical signal that they cannot decode. In a wired network, a host is able to detect such a collision both while it is listening (e.g. like host C in the figure above) and also while it is sending its own frame. When a host transmits a frame, it can compare the electrical signal that it transmits with the electrical signal that it sense on the wire. At points `(1)` and `(2)` in the figure above, host A senses only its own signal. At point `(3)`, it senses an electrical signal that differs from its own signal and can thus detect the collision. At this point, its frame is corrupted and it can stop its transmission. The ability to detect collisions is the starting point for the `Carrier Sense Multiple Access with Collision Detection (CSMA/CD)` Medium Access Control algorithm that is used in Ethernet networks [Metcalfe1976]_ [802.3]_ . When an Ethernet host detects a collision while it is transmitting it immediately stops its transmission. Compared with pure CSMA, CSMA/CD is an important improvement since when collision occurs, they only last until colliding hosts have detected it and stop their transmission. In practice, when a host detects a collision, it sends a special jamming signal on the cable to ensure that all hosts have detected the collision.

When considering these collisions, it is useful to analyse what would be the worst collision on a shared bus network. Let us consider a wire with two hosts attached at both ends as shown in the figure below. Host A starts to transmit its frame. Its electrical signal is propagated on the cable. This propagation time depends on the physical length of the cable and the speed of the electrical signal. Let us use :math:`\tau` to represent this delay in seconds. Slightly less than :math:`\tau` seconds after the beginning of the transmission of A's frame, B decides to start to transmit its own frame. After :math:`\epsilon` seconds, B senses A's frame, detects the collision and stops transmitting. The beginning of B's frame is propagated on the cable until it reaches host A. Host A is thus able to detect the collision at time :math:`\tau-\epsilon+\tau \approx 2\times\tau`. An important point to note is that a collision can only occur during the first :math:`2\times\tau` seconds of its transmission. If a collision did not occur during this period, it cannot occur afterwards since the transmission channel is busy after :math:`\tau` seconds and hosts sense the transmission channel before transmitting their frame. 


.. figure:: png/lan-fig-027-c.png
   :align: center
   :scale: 70
   
   The worst collision on a shared bus

Furthermore, on the wired networks where CSMA/CD is used collisions are almost the only cause of transmission errors that affect frames. Transmission errors that only affect a few bits inside a frame seldom occur in these wired networks. For this reason, the designers of CSMA/CD choose to completely remove the acknowledgement frames in the datalink layer. When a host transmits a frame, it verifies whether its transmission has been affected by a collision. If not, given the negligible Bit Error Ratio of the underlying network, it assumes that the frame was received correctly by its destination. Otherwise the frame is retransmitted after some delay.

Removing acknowledgements is an interesting optimisation since it reduces both the number of control frames exchanged on the network and the number of frames that need to be processed by the hosts. However, to use this optimisation, we must ensure that all hosts will be able to detect all the collisions that affect their frames. The problem is important for short frames. Let us consider two hosts, A and B, that are sending a small frame to host C as illustrated in the figure below. If the frames sent by A and B are very short, the situation illustrated below may occur. Hosts A and B send their frame and stop transmitting (point `(1)`). When the two short frames arrive at the location of host C, they collide and host C cannot decode them (point `(2)`). The two frames are absorbed by the ends of the wire. Neither host A nor host B have detected the collision. They both consider that their frame has been received correctly by its destination.


.. figure:: png/lan-fig-026-c.png
   :align: center
   :scale: 70
   
   The short-frame collision problem

.. index:: slot time (Ethernet)

To solve this problem, networks using CSMA/CD require hosts to transmit during at least :math:`2\times\tau` seconds. Since the network transmission speed is fixed for a given network technology, this implies that a technology that uses CSMA/CD enforces a minimum frame size. In the most popular CSMA/CD technology, Ethernet, :math:`2\times\tau` is called the `slot time` [#fslottime]_. 

.. index:: binary exponential back-off (CSMA/CD)

The last innovation introduced for CSMA/CD is the computation of the timeout between the detection of a collision and the retransmission of the collided frame. As for ALOHA, this timeout cannot be fixed, otherwise hosts could become synchronised and always retransmit at the same time that would lead to synchronised collisions. Setting such a timeout is always a compromise between the network access delay and the amount of collisions. A short timeout would lead to a low network access delay but with a higher risk of collisions. On the other hand, a long timeout would cause a long network access delay but a lower risk of collisions. The `binary exponential back-off` algorithm was introduced in CSMA/CD networks to solve this problem.

To understand `binary exponential back-off`, let us consider a collision that was caused by exactly two hosts. Once it has detected the collision, a host can either retransmit its frame immediately or defer its transmission for some time. If each colliding host flips a coin to decide whether to retransmit immediately or to defer its retransmission, four cases are possible :

 1. Both hosts retransmit immediately and a new collision occurs
 2. The first host retransmits immediately and the second defers its retransmission
 3. The second host retransmits immediately and the first defers its retransmission
 4. Both hosts defer their retransmission and a new collision will occur

In the second and third cases, both hosts have flipped different coins. The delay chosen by the host that defers its retransmission should be long enough to ensure that its retransmission will not collide with the immediate retransmission of the other host. However the delay should not be longer than necessary to avoid the collision since if both hosts decide to defer their transmission the network will be idle during this delay. The `slot time` is the optimal delay since it is the shortest delay that ensures that the first host will be able to retransmit its frame completely without any collision. 

If two hosts are competing, the algorithm above will avoid a second collision 50% of the time. However, if the network is heavily loaded, several hosts may be competing at the same time. In this case, the hosts should be able to automatically adapt their retransmission delay. The `binary exponential back-off` performs this adaptation based on the number of collisions that have affected a frame. After the first collision, the host flips a coin and waits 0 or 1 `slot time`. After the second collision, it generates a random number and waits 0, 1, 2 or 3 `slot times`... The duration of the waiting time is thus doubled after each collision. The complete pseudo-code for the CSMA/CD algorithm is shown in the figure below. 


.. code-block:: python
 
 N=1
 while N<= max :
    wait(channel becomes free)
    send(frame)   
    wait until (end of frame) or (collision)	
    if collision detected:
	stop transmitting
	send(jamming)
	k = min (10, N)
	r = random(0, 2k - 1) * slotTime;
	wait(r*slotTime)
	N=N+1
    else :	
        wait(inter-frame delay)
	break
  else:		
    # Too many transmission attempts
	

The inter-frame delay used in this pseudo-code is a short delay that corresponds to the time required by a network adapter to switch from transmit to receive mode. It is also used to prevent a host from sending a continuous stream of frames without leaving any transmission opportunities for other hosts on the network. Unfortunately, there are still conditions whether CSMA/CD is not completely fair [RY1994]_. Consider for example a network with two hosts : a server sending long frames and a client sending acknowledgments. Measurements reported in [RY1994]_ have shown that there situations where the client could suffer from repeated collisions that lead it to wait for long periods of time due to the exponential back-off algorithm. How



Carrier Sense Multiple Access with Collision Avoidance
------------------------------------------------------

TODO

receiver

::
 
 While (true)
 {
  Wait for data frame;
	if not(duplicate)
		{ deliver (frame) }
  wait during SIFS;
  send ack (frame) ;
 }

.. figure:: png/lan-fig-031-c.png
   :align: center
   :scale: 70
   
   Basic scenario with CSMA/CA


.. figure:: png/lan-fig-032-c.png
   :align: center
   :scale: 70
   
   Effect of collision with CSMA/CA

.. figure:: png/lan-fig-034-c.png
   :align: center
   :scale: 70
   
   Detailed example with CSMA/CA


.. figure:: png/lan-fig-035-c.png
   :align: center
   :scale: 70
   
   The hidden station problem 


.. figure:: png/lan-fig-036-c.png
   :align: center
   :scale: 70
   
   Reservations with CSMA/CA







sender

::

 N=1;
 while ( N<= max) do
	if (channel is empty)
	{ wait until channel free during t>=EIFS; }
	else
	{ wait until endofframe;
	  wait until channel free during t>=DIFS; }
	back-off_time = int(random[0,min(255,7*2N-1)])*T
     wait(backoff_time)
	if (channel still free)
	{ send data  frame ;
	     wait for ack or timeout:
	    if ack received
		 exit while;
	   else /* timeout retransmission is needed */
		N=N+1; }
 end do
	

.. 802.15.4 ?


Token Ring and FDDI
-------------------




Datalink layer technologies
###########################
In this section, we review the key characteristics of the several datalink layer technologies. We discuss in more details the technologies that are widely used and briefly mention other interesting technologies. A detailed survey of all datalink layer technologies would be outside the scope of this book.

The Point-to-Point Protocol
===========================

Many point-to-point datalink layers have been developed starting in the 1960s. 

:rfc:`1548`

Goal
Allow the transmission of network layer (IP but also other protocols) packets over serial lines
modems, leased lines, ISDN, ...
Architecture
PPP is composed of three different protocols
PPP 
transmission of data frames (e.g. IP packets)
LCP : Link Control Protocol
Negotiation of some options and authentication (username, password) and end of connection
NCP : Network Control Protocol
Negotiation of options related to the network layer protocol used above PPP
(ex: IP address, IP address of DNS resolver, ...)


Ethernet
========

Ethernet was designed in the 1970s at the Palo Alto Research Center [Metcalfe1976]_. The first prototype [#fethernethistory]_ used a coaxial cable as the shared medium and provided a 3 Mbps bandwidth. Ethernet was improved during the late 1970s and in 1980s, three companies : Digital Equipment, intel and Xerox published the first official Ethernet specification [DIX]_. This specification defines several important parameters for Ethernet networks. The first decision was to standardise the commercial Ethernet at 10 Mbps. The second decision was the duration of the `slot time`. In Ethernet, a long `slot time` enables networks spanning a long distance but forces the host to use a larger minimum frame size. The compromise was a `slot time` of 51.2 microseconds, which corresponds to a minimum frame size of 64 bytes. The third decision was the frame format.

The experimental 3 Mbps Ethernet network built at Xerox used short frames containing 8 bits source and destination addresses fields, a 16 bits type indication, up to 554 bytes of payload and a 16 bits CRC. Using 8 bits was suitable for an experimental network, but it was clearly too small for commercial deployments. Although the initial Ethernet specification [DIX]_ only allowed up to 1024 hosts on an Ethernet network, it also recommended three important changes compared to networking technologies available at that time. The first change was to require each host attached to an Ethernet network to have a unique datalink layer address. Until then, datalink layer addresses were configured manually on each hosts. [DP1981]_ went against that state of the art and noted "`Suitable installation-specific administrative procedures are also needed for assigning numbers to hosts on a network. If a host is moved from one network to another it may be necessary to change its host  number if its former number is in use on the new network. This is easier said than done, as each network must have an administrator who must record the continuously changing state of the system (often on a piece of paper tacked to the wall !). It is anticipated that in future office environments, hosts locations will change as often as telephones are changed in present-day offices.`" The second change introduced by Ethernet was to encode each address as a 48 bits field [DP1981]_. 48 bits addresses were huge compared to the networking technologies available in the 1980s, but the huge address space had several advantages [DP1981]_ including the ability to allocated large blocks of addresses to manufacturers. Eventually, other LAN technologies opted for 48 bits addresses as well [802]_. The third change introduced by Ethernet was the definition of `broadcast` and `multicast` addresses. The need for `multicast` Ethernet was foreseen in [DP1981]_ and thanks to the size of the addressing space it was possible to reserve a large block of multicast addresses for each manufacturer.

.. index:: Organisation Unique Identifier, OUI

The datalink layer addresses used in Ethernet networks are often called MAC addresses. They are structured as shown in the figure below. The first bit of the address indicates whether the address identifies a network adapter or a multicast group. The upper 24 bits are used to encode an Organisation Unique Identifier (OUI). This OUI identifies a block a addresses that has been allocated by the secretariat [#foui]_ that is responsible for the uniqueness of Ethernet addresses to a manufacturer. Once a manufacturer has received an OUI, it can build and sell products with one of the 16 millions addresses in this block.

.. figure:: png/lan-fig-039-c.png
   :align: center
   :scale: 70
   
   48 bits Ethernet address format

.. index:: EtherType, Ethernet Type field

The original 10 Mbps Ethernet specification [DIX]_ defined a simple frame format where each frame is composed of five fields. The Ethernet frame starts with a preamble (not shown in the figure below) that is used by the physical layer of the receiver to synchronise its clock to the sender's clock. The first field of the frame is the destination address. As this address is placed at the beginning of the frame, a host can quickly verify whether it is the frame recipient and if not cancel the processing of the arriving frame. The second field is the source address. While the destination address can be either a unicast or a multicast/broadcast address, the source address must always be a unicast address. The third field is a 16 bits integer that indicates which type of network layer packet is carried inside the frame. This field is often called the `EtherType`. Frequently used `EtherType` values [#fethertype]_ include `0x0800` for IPv4, `0x86DD` for IPv6 [#fipv6ether]_ and `0x806` for the Address Resolution Protocol (ARP). The fourth part of the Ethernet frame is the payload. The minimum length of the payload is 46 bytes to ensure a minimum frame size, including the header of 512 bits. The Ethernet payload cannot be longer than 1500 bytes. This size was found reasonable when the first Ethernet specification was written. At that time, Xerox had been using its experimental 3 Mbps Ethernet that offered 554 bytes of payload and :rfc:`1122` required a minimum MTU of 572 bytes. 1500 bytes was large enough to support these needs without forcing the network adapters to contain too large memories. Furthermore, simulations and measurements studies performed in Ethernet networks revealed that the CSMA/CD was able to achieve a very high utilization. This is illustrated in the figure below based on [SH1980]_ that shows the channel utilization achieved in Ethernet networks containing different number of hosts that are sending frames of different sizes.


.. figure:: png/lan-fig-102-c.png
   :align: center
   :scale: 70
   
   Impact of the frame length of the maximum utilisation [SH1980]_


The last field of the Ethernet frame is a 32 bits Cyclical Redundancy Check (CRC). This CRC is able to catch a much larger number of transmission errors than the Internet checksum used by IP, UDP and TCP [SGP98]_. The format of the Ethernet frame is shown below.


.. Ethernet evolution http://www.networkworld.com/slideshows/2009/042009-terabit-ethernet.html?ts0hb#slide14

.. index:: Ethernet DIX frame format

::

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |								   |	
   +    48 bits                      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    
   |    Destination Address	     |			           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    48 bits   		   +
   |                    		  Source Address	   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |		Type (16 bits)	     |				   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+				   |
   |								   |
   ~ 			Payload (46-1500 bytes)			   |
   |								   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |			32 bits		CRC			   |	
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   Ethernet DIX frame format

.. Sidebar:: Where should CRCs be located ?

 Transport layer protocols usually place their CRCs or checksums in the segment header. Datalink layer protocols sometimes place their CRC in the frame header, but often in a trailer at the end of the frame. 

 - Datalink layers implemented in hardware, e.g. on network adapters, often place their checksum/CRC in the trailer to allow the sender can use hardware assistance on the interface card to compute the checksum/CRC while the segment is being sent. 
 - when the checksum/CRC is placed in the header, this implies, as segments are sent on the wire one byte after the other starting from the trailer, that the checksum/CRC must be computed before transmitting the segment. It is still possible to use hardware assistance to compute the CRC/checksum, but this is slightly more complex than when the checksum/CRC is placed inside a trailer [#ftso]_. 

.. index:: Logical Link Control (LLC), LLC

The Ethernet frame format shown above is specified in [DIX]_. This is the format used to send both IPv4 :rfc:`894` and IPv6 packets :rfc:`2464`. After the publication of [DIX]_, the Institute of Electrical and Electronics Engineers (IEEE) started to standardise several Local Area Network technologies. IEEE worked on several competing LAN technologies, starting with Ethernet, Token Ring and Token Bus. These three technologies were completely different, but they all agreed to use the 48 bits MAC addresses specified initially for Ethernet [802]_. While developing its Ethernet standard [802.3]_, the IEEE 802.3 working group was confronted with a problem. Ethernet mandated a minimum payload size of 46 bytes, while some companies were looking for a LAN technology that could easily transport short frames containing only a few bytes of payload. To send a five bytes payload, a host had to send a 46 bytes payload, but since the Ethernet header [DIX]_ does not contain a length field, it was impossible for the receiver to determine how many useful bytes were placed inside the payload field. To solve this problem, the IEEE decided to replace the `Type` field of the Ethernet [DIX]_ header with a length field [#ftypelen]_. This `Length` field contained the number of useful bytes in the frame payload. Unfortunately, when IEEE added the `Length` field, they also removed the `Type` field that indicated the payload type. Without this field, it became impossible for a receiving host to identify the type of packet received inside a frame. To solve this new problem, IEEE developed a completely new sublayer called the Logical Link Control [802.2]_. Several protocols were defined in this sublayer. One of them provided a slightly different version of the `Type` field of the original Ethernet frame format. Another contained acknowledgements and retransmissions to provide a reliable service...

.. sidebar:: The Ethernet service

 An Ethernet network provides an unreliable connectionless. It supports three different transmission modes : `unicast`, `multicast` and `broadcast`. While the Ethernet service is unreliable in theory, a good Ethernet network should in practice provide a service that :
  - delivers frames to their destination with a very high probability of succesful delivery
  - does not reorder the transmitted frames
 The first point is related to the utilisation of CSMA/CD that allows hosts to detect all collisions. The second point is due to the physical organisation of the network as a shared bus.

::

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |								   |	
   +    48 bits                      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    
   |    Destination Address	     |			           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    48 bits   		   +
   |                    		  Source Address	   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |	  Length (16 bits)	     |				   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+				   |
   |								   |
   ~ 		Payload and padding (46-1500 bytes)		   |
   |								   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |			32 bits		CRC			   |	
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   Ethernet 802.3 frame format

.. index:: 10Base5, 10Base2, 10BaseT


Several different physical layers were defined for Ethernet networks. The first physical layer, usually called 10Base5, provided 10 Mbps over a thick coaxial cable. The characteristics of the cable and the transceivers used enabled the utilisation of 500 meters long segments. 10Base5 also allowed the utilisation of repeaters between segments. The segment physical layer was 10Base2. This physical layer used a thin coaxial cable that was easier to install than the 10Base5 cable, but could not be longer than 185 meters. A 10BaseF physical layer was also defined to transport Ethernet over point-to-point optical links. The major change to the physical layer was the support of twisted pairs in the 10BaseT specification. Twisted pair cables are traditionally used to support telephone service in office buildings. Most office buildings today are built with several twisted pairs cable installed between any room and a central room per building or per floor in large buildings. These central rooms serve as concentration points for the telephone service but also for LANs. 

.. index:: Ethernet hub


The introduction of the twisted pairs lead to two major changes to Ethernet. The first change concerns the physical topology of the network. 10Base2 and 10Base5 networks are shared buses, the coaxial cable typically enters each room that contains a connected computer. A 10BaseT network is a star-shaped network. All the devices connected to the network are attached via a twisted pair cable that ends in the central room. From a maintenance viewpoint, this is a major improvement. The physical cable was a weak point in 10Base2 and 10Base5 networks. Any physical dammage on the cable broke the entire network and when such a failure occured, the network administrator had to manually check the entire physical cable to detect where it was dammaged. With 10BaseT, when one twisted is dammaged, only the device connected to this twisted is affected and this does not affect the other devices. The second major change introduced by 10BaseT was that is was impossible to build a 10BaseT network by simply connected all the twisted pairs together. All the twisted pairs had to be connected to a relay that operates in the physical layer and was later called an `Ethernet hub`. A `hub` is thus a physical layer relay that receives an electrical signal on of al its interfaces, regenerates the signal and transmits it over its other interfaces. Some `hubs` are also able to convert the electrical signal from one physical layer to another (e.g. 10BaseT to 10Base2 conversion).


.. figure:: png/lan-fig-060-c.png
   :align: center
   :scale: 70
   
   Ethernet hubs in the reference model

.. index:: collision domain

Computers can be directly attached to Ethernet hubs. Ethernet hubs themselves can be attached to other Ethernet hubs to build a larger network. However, some important guidelines must be followed when building a complex network with hubs. First, the network topology must be a tree. As hubs are relays in the physical layer, adding a link between `Hub2` and `Hub3` in the network below would create an electrical shortcut that would completely dirsrupt the network. This implies that there cannot be any redundancy in a hub-based network. A failure of a hub or of a link between two hubs would split the network into two isolated networks. Second, as hubs are relays in the physical layer, collisions can happen and must be handled by CSMA/CD as in a 10Base5 network. This implies that the maximum delay between any pair of devices in the network cannot be longer than the 51.2 microseconds `slot time`. If the delay is longer, collisions between short frames may not be correctly detected. If practice, this constraint limits the geographical spread of 10BaseT networks containing hubs.


.. figure:: png/lan-fig-061-c.png
   :align: center
   :scale: 70
   
   A hierarchical Ethernet network composed of hubs

.. index:: 100BaseTX, Fast Ethernet

In the late 1980s, 10 Mbps became too slow for some applications and network manufacturers developed several LAN technologies that offered higher bandwidth such as the 100 Mbps FDDI LAN that used optical fibers. The development of 10Base5, 10Base2 and 10BaseT showed that Ethernet could be adapted to different physical layers. Several manufacturers started to work on 100 Mbps Ethernet and convinced IEEE to standardise this new technology that was initially called `Fast Ethernet`. `Fast Ethernet` was designed under the following constraints. First, `Fast Ethernet` had to use twisted pairs. Although it was easier from a physical layer viewpoint to support higher bandwidth on coaxial cables than on twisted pairs, coaxial cables had too many drawbacks from deployment and maintenance viewpoints. Second, `Fast Ethernet` had to be compatible with the existing 10 Mbps Ethernets to allow `Fast Ethernet` technology to be used initially as a backbone technology to interconnect. The second requirement forced `Fast Ethernet` to use the same frame format as 10 Mbps Ethernet. This implied that the minimum `Fast Ethernet` frame size remained at 512 bits. To preserve CSMA/CD with this minimum frame size and 100 Mbps instead of 10 Mbps, the duration of the `slot time` was decreased to 5.12 microseconds.



Ethernet Switches
-----------------

.. index:: Ethernet switch, Ethernet bridge, bridge, switch

Increasing the physical layer bandwidth as in `Fast Ethernet` was only of the solutions to improve the performance of Ethernet LANs. A second solution was to replace the hubs by more intelligent devices. As `Ethernet hubs` operate, they can only regenerate the electrical signal to extend the geographical reach of the network. `Ethernet switches` [#fbridges]_ are relays that operate in the datalink layer. An `Ethernet switch` understands the format of the Ethernet frames and can selectively decide to forward some frames over a given interface.

If the `Ethernet hubs` were replaced by devices that operate in the datalink layer, these devices would be able to 


.. figure:: png/lan-fig-060-c.png
   :align: center
   :scale: 70
   
   Ethernet switches in the reference model

::

 Arrival of frame F on port P
 src=F.Source_Address;
 dst=F.Destination_Address;
 UpdateTable(src, P); // src heard on port P
 if (dst==broadcast) || (dst is multicast)
 {
 for(Port p!=P)       // forward all ports
 ForwardFrame(F,p);
 }
 else
 {  
  if(dst isin AddressPortTable)
 {
   ForwardFrame(F,AddressPortTable(dst));
 }
 else
 {
  for(Port p!=P)    // forward all ports
     ForwardFrame(F,p);
 }
 }
  

The Spanning Tree Protocol (802.1d) 
------------------------------------





802.11
======

Todo


802.15.4
========

Todo


Token Ring
==========

Todo

FDDI
====

Todo

Asynchronous Transfer Mode
==========================

Todo

.. rubric:: Footnotes

.. [#ftso] Although TCP places its checksum in the segment header, there are now network interfaces that are able to directly compute the TCP checksum while a segment is transferred from the host memory to the network interface [SH2004]_.

.. [#fslottime] This name should not be confused with the duration of a transmission slot in slotted ALOHA. In CSMA/CD networks, the slot time is the time during which a collision can occur at the beginning of the transmission of a frame. In slotted ALOHA, the duration of a slot is the transmission time of an entire frame.

.. [#fethernethistory] Additional information about the history of the Ethernet technology may be found at http://ethernethistory.typepad.com/

.. [#foui] Initially, the OUIs were allocated by Xerox [DP1981]_. However, once Ethernet became an IEEE and later an ISO standard, the allocation of the OUIs moved to IEEE. The list of all OUI allocations may be found at http://standards.ieee.org/regauth/oui/index.shtml

.. [#fethertype] The official list of all assigned Ethernet type values is available from http://standards.ieee.org/regauth/ethertype/eth.txt

.. [#fipv6ether] The attentive reader may question the need for different `EtherTypes` for IPv4 and IPv6 while the IP header already contains a version field that can be used to distinguish between IPv4 and IPv6 packets. Theoretically, IPv4 and IPv6 could have used the same `EtherType`. Unfortunately, developers of the early IPv6 implementations found that some devices did not check the version field of the IPv4 packets that they received and parsed frames whose `EtherType` was set to `0x0800` as IPv4 packets. Sending IPv6 packets to such devices would have caused disruptions. To avoid this problem, the IETF decided to apply for a distinct `EtherType` value for IPv6.

.. [#ftypelen] Fortunately, IEEE was able to define the [802.3]_ frame format while maintaining backward compatibility with the Ethernet [DIX]_ frame format. The trick was to only assign values above 1500 as `EtherType` values. When a host receives a frame, it can determine whether the frame's format by checking its `EtherType/Length` field. A value lower smaller than `1501` is clearly a length indicator and thus an [802.3]_ frame. A value larger than `1501` can only be type and thus a [DIX]_ frame.

.. [#fbridges] The first Ethernet relays that operated in the datalink layers were called `bridges`. In practice, the main difference between switches and bridges is that bridges were usually implemented in software while switches are hardware-based devices. Throughout this text, we always use `switch` when referring to a relay in the datalink layer, but you might still see the word `bridge`.

.. include:: ../links.rst
