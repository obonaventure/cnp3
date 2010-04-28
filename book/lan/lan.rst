==============================================
The datalink layer and the Local Area Networks
==============================================


The datalink layer is the lowest layer of the reference model that we discuss in details. As mentioned previously, there are two type of datalink layers. The first datalink layers that appeared are the ones that are used on point-to-point links between endsystems that are directly connected by a physical link. We will briefly discuss one of these datalink layers in this chapter. The second type of datalink layers are the ones used in Local Area Networks. The main difference between the point-to-point and the LAN datalink layers is that the latter need to regulate the access to the Local Area Network which is usually a shared medium. 
This chapter is organised as follows. We first discuss the principles and of datalink layer and the service that it uses from the physical layer. Then we describe in more details several Medium Access Control algorithms that are used by Local Area Networks to regulate the access to the shared medium. Finally we discuss in details several important datalink layer technologies with an emphasis on Ethernet.

Principles
##########

The datalink resides above and uses the service provided by the physical layer. Although there are many different implementations of the physical layer from a technological viewpoint, they all provide a service that enables the datalink layer to send and receive bits to/from another directly connected endsystem. The datlink layer receives packets from the network layer. Two datalink layer entities exchange `frames`. As explained in the previous chapter, most datalink layer technologies impose limitations on the size of the frames. Some technologies impose only a maximum frame size, others enforce both minimum and maximum frames sizes and finally some technologies only support a single frame size. In the latter case, the datalink layer will usually include an adaptation sublayer to allow the network layer to send and receive variable-length packets. This adaptation layer may include fragmentation and reassembly mechanisms.

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

If the physical layer was perfect, the problem would be very simple. The datalinke layer would simply need to define how to encode each frame as a sequence of consecutive bits. The receiver would then be able to easily extract the frames from the received bits. Unfortunately, the imperfections of the physical layer make this framing problem slightly more complex. Several solutions have been proposed and are used in practice in different datalink layer technologies.

Framing
=======

The `framing` problem can be phrased as : "`How does a sender encodes frames so that the receiver can efficiently extract them from the stream of bits that it receives from the physical layer`". 

A first solution to solve the framing problem is to require the physical layer to remain idle for some time after the transmission of each frame. These idle periods can be detected by the receiver and server as a marker to delineate frame boundaries. Unfortunately, this solution is not sufficient for two reasons. First, some datalink layers cannot remain idle and need to always transmit bits. Second, inserting an idle period between frames decrease the maximum bandwidth that can be achieved by the datalink layer.

.. index:: Manchester encoding

Some physical layers provide an alternative to this idle period. All physical alyers are able to send and receive physical symbols that represent values `0` and `1`. However, tor various reasons that are outside the scope of this chapter, several physical layers are able to exchange other physical symbols as well. For example, the Manchester encoding used in several physical layers allows to send four different symbols. The Manchester encoding is a differential encoding scheme in which time is divided in fixed-length periods. Each period is divided in two halves and two different voltage levels can  be applied. To send a symbol, the sender must set one of these two voltage levels during each half period. To send a `1` (resp. `0`), the sender must set a high (resp. low) voltage during the first half of the period and a low (resp. high) voltage during the second half. This encoding ensures that there will be a transition at the middle of each period and allows the receiver to synchronise its clock to the sender's clock. Besides, the encodings for `0` and `1`, the Manchester encoding also supports two additional symbols : `InvH` and `InvB`  where the same voltage level is used during the two half periods. By definition, these two symbols cannot appear in the content of a frame which is only composed of `0` and `1`. Some technologies use these special symbols as markers at the beginning or end of frames.

.. figure:: png/lan-fig-006-c.png
   :align: center
   :scale: 70
   
   Manchester encoding

.. index:: bit stuffing, stuffing (bit)

Multi-symbol encodings cannot be used by all physical layers and a generic solution that can be used with any physical layer that is able to transmit and receive only `0` and `1` is required. This generic solution is called `stuffing` and two variants exist : `bit stuffing` and `character stuffing`. To enable a receiver to easily delineate the frame boundaries, these two techniques reserve special bitstrings as frame boundary markers and encode the frames so that these special bitstrings do not appear inside the frames.

`Bit stuffing` reserves the `01111110` bit string as the frame boundary marker and ensures that there will never be six consecutive `1` bits transmitted inside a frame. With bit stuffing, a frame is sent as follows. First, the sender transmits the marker, i.e. `01111110`. Then, the sender sends all the bits of the frame and inserts an additional bit set to `0` after each sequence of five consecutive `1` bits. This ensures that the sent frame never contains a sequence six consecutive bits set to `1`. As a consequence, the marker pattern does not appear inside the frame sent. The marker is also sent at the end of the frame. The receiver performs the opposite to decode the received frame. It first detects the beginning of the frame with the `01111110` marker. Then, it processes the received bits and counts the number of consecutive bits set to `1`. If a `0` follows five consecutive bits set to `1`, this bit is removed as it was inserted by the sender. If a `1` follows five consecutive bits sets to `1`, it indicates a marker if it is followed by a bit set to `0`.

For example, consider the transmission of packet `0110111111111111111110010`. Then sender will first send the `01111110` marker followed by `011011111`. After these five consecutive bits set to `1`, it inserts a bit set to `0` followed by `11111`. A new `0` is inserted, followed by `11111`. A new `0` is inserted followed by the end of the frame `110010` and the `01111110` marker.

`Bit stuffing` increases the number of bits required to transmit a given frame. The worst case for bit stuffing is of course a long sequence of bits set to `1` inside the frame. If transmission errors occur, stuffed bits or markers can be errored. In these cases, the frame affected by the error and possibly the next frame will be wrongly decoded by the receiver, but it will be able to resynchronise itself at the next valid marker. 


.. index:: character stuffing, stuffing (character)

`Bit stuffing` can be easily implemented in hardware. However, implementing it in software is more complex. As software implementations prefer to process characters than bits, software-based datalink layers usually use `character stuffing`. This technique operates on frames that contain an integer number of characters. Some characters are used as markers to delienate the frame boundaries. Many `character stuffing` techniques use the `DLE`, `STX` and `ETX` characters of the ASCII character set. `DLE STX` (resp. `DLE ETX`) is used to mark the beginning (end) of a frame. When transmitting a frame, the sender adds a `DLE` character after each transmitted `DLE` character. This ensures that none of the markers can appear inside the transmitted frame. The receiver detects the frame boundaries and remove the second `DLE` when it receives two consecutive `DLE` characters. For example, to transmit frame `1 2 3 DLE STX 4`, a sender will first send `DLE STX` as a marker, followed by `1 2 3 DLE`. Then, the sender transmits an additional `DLE` character followed by `STX 4` and the `DLE ETX` marker.

`Character stuffing` like bit stuffing increases the lenght of the transmitted frames. For `character stuffing`, the worst frame is a frame containing many `DLE` characters. When transmission errors occur, the receiver may incorrectly decode one or two frames (e.g. if the errors occur in the markers). However, it will be able to resynchronise itself with the next correctly received markers.

In practice, datalink layer protocols combine one of these techniques with a length indication in the frame header and a checksum or CRC. The checksum/CRC is computed by the sender and placed in the frame before applying bit/character stuffing.

.. Sidebar:: Placing CRCs in trailers or headers

 Transport layer protocols usually place their CRCs or checksums in the segment header. Datalink layer protocols sometimes place their CRC in the frame header, but often in a trailer at the end of the frame. 

 - Datalink layers implemented in hardware, e.g. on network adapters, often place their checksum/CRC in the trailer to allow the sender can use hardware assistance on the interface card to compute the checksum/CRC while the segment is being sent. 
 - when the checksum/CRC is placed in the header, this implies, as segments are sent on the wire one byte after the other starting from the trailer, that the checksum/CRC must be computed before transmitting the segment. It is still possible to use hardware assistance to compute the CRC/checksum, but this is slightly more complex than when the checksum/CRC is placed inside a trailer [#ftso]_. 


Medium Access Control
=====================

Point-to-point datalink layers need to select one of the framing techniques described above and optionnaly add retransmission algorithms such as those explained for the transport layer to provide a reliable service. Datalink layers for Local Area Networks face two additional problems. A LAN is composed of several hosts that are attached to the same shared physical medium. From a physical layer viewpoint, a LAN can be organised in four different ways :

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

In the 1960s computers were mainly mainframes with a few dozens of terminals attached to them. These terminals were usually in the same building as the mainframe and were directly connected to it. In some cases, the terminals were installed in remote locations and connected through modems over dialup lines. At the university of Hawa√Ø, this organisation was not possible. Instead of using telephone lines to connect the distant terminals, they developed the first `packet radio` technology [Abramson1970]_. Until then, computer networks were built on top of either the telephone network or physical cables. AlohaNet showed that it was possible to use radio signals to interconnect computers.

.. index:: ALOHA

The first version of ALOHAnet, described in [Abramson1970]_, operated as follows. First, the terminals and the mainframe exchanged fixed-length frames composed of 704 bits. Each frame contained 80 8-bits characters, some control bits and parity information to detect transmission errors. Two channels in the 400 MHz range were reserved for the operation of ALOHANet. The first channel was used by the mainframe to send frames to all terminals. The second channel was shared among all terminals to send frames to the mainframe. As all terminals share the same transmission channel, there is a risk of collision. To deal with this problem and also transmission errors the mainframe verified the parity bits of the received frame and sent an acknowledgement on its channel for each correctly received frame. The terminals on the other hand had to retransmit the unacknowledged frames. As for TCP, retransmitting these frames immediately upon expiration of a fixed timeout is not a good approach as several terminals may retransmit their frames at the same time leading to a network collapse. A better approach, but still far from perfect, is for each terminal to wait a random amount of time after the expiration of its retransmission timeout. This avoids synchronisation among multiple retransmitting terminals. 


The pseudocode below show the operation of an ALOHANet terminal. We use this python syntax for all Medium Access Control algorithms described in this chapter. The algorithm is run for each new frame that needs to be transmitted. It attempts to transmit a frame at most `max` times (`while loop`). Each transmission attempt is performed as follows. First, the frame is sent. Each frame is protected by a timeout. Then the terminal waits for either a valid acknowledgement frame or the expiration of its timeout. If the terminal receives an acknowledgement, the frame has been delivered correctly and the algorithm terminates. Otherwise, the terminal waits for a random time and attempts to retransmit the frame. 

::
 
 N=1
 while N<= max :
    send(frame)
    wait(ack on return channel or timeout)
    if ack on return channel:
       	break  # transmission was succesfull
    else:
	# timeout 
	wait(random time)
	N=N+1
  else:		
    # Too many transmission attempts

[Abramson1970]_ analysed the performance of ALOHANet under particular assumptions and found that ALOHANet worked well when the channel was lightly loaded. In this case, the frames are rarely retransmitted and the `channel traffic`, i.e. the total number of (correct and retransmitted) frames transmitted per unit of time is close to the `channel utilization`, i.e. the number of correctly transmitted frames per unit of time. Unfortunately, the analysis also reveals that the `channel utilization` reaches its maximum at :math:`\frac{1}{2 \times e}=0.186` times the channel bandwidth. At higher utilization, ALOHANet becomes unstable and the network collapses due to collided retransmissions.


.. sidebar:: Amateur packet radio

 Packet radio technologies have evolved in various directions since the first experiments performed at the University of HawaÔ. The Amateur packet radio service developed by amateur radio operators is of these descendants of ALOHANet. Many amateur radio operators are very interested in new technologies and they often spend countless hours to develop new antennas or transceivers. When the first personnal computers appeared, several amateur radio operators designed radio modems and their own datalink layers protocols [KPD1985]_ [BNT1997]_ . This network grew and it was possible by using only packet radio relays to connect to servers in several European countries. Some amateur radio operators also developed TCP/IP protocol stacks that were used over the packet radio service. Some parts of the `http://www.ampr.org/ <amateur packet radio network>`_ is connected to the global Internet and uses the `44.0.0.0/8`. 

.. index:: slotted ALOHA

Many improvements to ALOHANet were proposed since the publication of [Abramson1970]_ and this technique or some of its variants are still found in wireless networks today. The slotted technique proposed in [Roberts1975]_ is important because it shows that a simple modification can significantly improve the channel utilization. Instead of allowing all terminals to transmit at [Roberts1975]_ Proposed to divide time in slots and allow the terminals to transmit only at the beginning of each slot. Each slot corresponds to the time required to transmit one fixed size frame. In practice, these slots can be imposed by a single clock that is received by all terminales. In ALOHANet, it could have been located on the central mainframe. The analysis in [Roberts1975]_ reveals that this simple modification improved the channel utilization by a factor of two. 
	


.. index:: CSMA, Carrier Sense Multiple Access


Carrier Sense Multiple Access
-----------------------------


ALOHA and slotted ALOHA can be easily implemented. Unfortunately, they can only be used in networks that are very lightly loaded. Designing a network for a very low utilisation is possible, but it clearly increases the cost of the network. To overcome these problems, many Medium Access Control mechanisms have been proposed. These mechanisms improve the channel utilization. Carrier Sense Multiple Access (CSMA) is a significant improvement compared to ALOHA. CSMA requires all nodes to listen to the transmission channel to verify that it is free before transmitting a frame [KT1975]_. When a node sense the channel to be busy, it defers its transmission until the channel becomes free again. The pseudocode below provides a more detailed description of the operation of CSMA. 

.. index:: persistent CSMA, CSMA (persistent)

::
 
 N=1
 while N<= max :
    wait(channel becomes free)
    send(frame)
    wait(ack or timeout)
    if ack :
       	break  # transmission was succesfull
    else :
	# timeout 
	N=N+1
  else:		
    # Too many transmission attempts



The above pseudocode is often called `persistent CSMA` [KT1975]_ as the terminal will continuously listen to the channel and transmit its frame as soon as the channel becomes free. Another important variant of CSMA is the `non-persistent CSMA` [KT1975]_. The main difference between persistant and non-persistent CSMA described in the pseudocode below is that a non-persistent CSMA node does not continuously listens to the channel to determine when it becomes free. When non-persistent CSMA terminal senses the transmission channel to be busy, it waits for a random time before sensing the channel idle. This improves the channel utilization compared to persistent CSMA. With persistent CSMA, when two terminals sense the channel to be busy, they will both transmit (and thus cause a collision) as soon as the channel becomes free. With non-persistent CSMA, this synchronisationdoes not occur as the terminals wait a random time after having sensed the transmission channel. The higher channel utilization achieved by non-persistent CSMA comes at the expense of a slightly higher waiting time in the terminals when the network is lightly loaded. 


.. index:: non-persistent CSMA, CSMA (non-persistent)

::
 
 N=1
 while N<= max :
    listen(channel)
    if free(channel):
       send(frame)	
       wait(ack or timeout)
       if ack :
       	  break  # transmission was succesfull
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

CSMA improves the channel utilization compared to ALOHA. However, there are still collisions that may last for an entire frame duration. Consider for example a network  composed of a 1 kilometer long cable with one terminal at each end and in the middle of the cable. Assume that the two terminals located

.. figure:: png/lan-fig-024-c.png
   :align: center
   :scale: 70
   
   Frame transmission on a shared bus 


.. figure:: png/lan-fig-025-c.png
   :align: center
   :scale: 70
   
   Frame collision on a shared bus 


.. figure:: png/lan-fig-026-c.png
   :align: center
   :scale: 70
   
   The short-frame collision problem


.. figure:: png/lan-fig-027-c.png
   :align: center
   :scale: 70
   
   The worst collision on a shared bus

::
 
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
        wait(interframe delay)
	break
  else:		
    # Too many transmission attempts
	


Carrier Sense Multiple Access with Collision Avoidance
------------------------------------------------------

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
	backoff_time = int(random[0,min(255,7*2N-1)])*T
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


Token Ring
----------


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

Ethernet was designed in the 1970s at the Palo Alto Research Center [Metcalfe1976]_. Several Local Area Network technologies were designed during the same decade, but Ethernet became the most successful. 

[802.3]_


.. Ethernet evolution http://www.networkworld.com/slideshows/2009/042009-terabit-ethernet.html?ts0hb#slide14

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

.. [#ftso] Although TCP places its checksum in the segment header, there are now network interfaces that are able to directly compute the TCP checksum while a segment is transferred from memory to the interface [SH2004]_.


.. include:: lan-footnotes.rst

.. include:: ../links.rst
