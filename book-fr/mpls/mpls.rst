.. Copyright |copy| 2011 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

=============================
MultiProtocol Label Switching
=============================


In the first half of the 1990s, network bandwidth was growing at a rapid pace. At that time, IP routers were basically powerful computers that processed IP packets entirely in software. The performance of IP routers was

On such software-based routers, the longest prefix match that is used to forwar

Given the growth in network bandwidth, researchers and vendors feared that the MultiProtocol Label Switching (MPLS) was invented

While IP was already deployed in the early 1990s, other networking technologies were being developed. IP was used mainly in research networks and there were only few commercial network operators that were using IP. The public telecommunication operators had developped other networking technologies to carry data. X.25 started in the 1970s and was deployed on a larger scale during the 1980s. X.25 was used mainly to provide data services to enterprises, but some research networks, notably in Europe used IP over X.25. In France, the minitel service was built on top of the Transpac X.25 network. However, X.25 was rather complex and included several mechanisms for error and flow control at different layers. During the 1980s, the quality of the data transmission links improved significantly both in bandwidth and in transmission error rates. These improvements led to the development of two techniques to carry data over virtual circuits in public telecommunication networks : Frame Relay [Buckwalter2000]_ and Asynchronous Transfer Mode (ATM) [LeBoudec1992]_ [dePrycker1995]_ . These two techniques rely on virtual circuits to forward from their source to their destination along a precomputed path. In ATM and Frame relay networks, intermediate nodes are called switches. Frame relay networks carry variable length frames while ATM switches process fixed-size frames [#fcell]_. 

.. In ATM and frame relay networks, when two hosts need to exchange data, they first need to establish a virtual circuit through intermediate switches. This is done by using  that are called cellsreEach frame contains a label and intermediate nod
.. Forward(interface in, label l) -> interface out, label


The virtual circuits that are used in frame relay and ATM networks have several advantages and some drawbacks. First, once the virtual circuit has been established all the data that is sent over the virtual circuit follows exactly the same path. Thus, there is no reordering on the virtual circuit. Second, thanks to the utilisation of virtual circuits, an ATM or frame relay switch only needs a single memory lookup to forward a frame while an IP router needs to find a longest match. This simple forwarding scheme is a key advantage from an implementation viewpoint. In the early 1990s, this was a strong motivation for the development of the ATM technology. To understand the issue, it is interesting to analyse the delay between packets received at line rate. The table 

 Bandwidth                Packet Size
 ---------                -----------
             	  40 bytes   250 bytes  1500 bytes
 ---------        --------   ---------  ----------
 10 Mbps          32 	     200	1200
 100 Mbps 	  3.2	     20	        120
 622 Mbps	  2.06	     12.9       77.42
 2.4 Gbps	  0.13	     0.83       5
 10 Gbps          0.03	     0.2	1.2


 


.. rubric:: Footnote

.. [#fcell] In ATM networks, the unit of transfer of information is the cell. A cell contains five bytes of header and 48 bytes of payload. Endsystems implement an ATM Adapation Layer that is able to fragment and reassemble variable length packets in a sequence of cells.


.. frame relay
.. ITU-T Rec. Q.922,  "ISDN  Data Link  Layer Specification  for  Frame Mode   Bearer Services,"  1992
.. Buckwalter, J. T. (2000). Frame relay: technology and practice (p. 338). Addison-Wesley. Retrieved from http://books.google.com/books?id=tROBDX-OBrEC&pgis=1

.. Le Boudec, J.-Y. (1992). The Asynchronous Transfer Mode: a tutorial. Computer Networks and ISDN Systems, 24(4), 279-309. Retrieved from http://dx.doi.org/10.1016/0169-7552(92)90114-6

.. Prycker, M. de. (1995). Asynchronous transfer mode: solution for broadband ISDN (p. 380). Prentice Hall. Retrieved from http://books.google.com/books?id=r_JSAAAAMAAJ&pgis=1

:rfc:`3031`  basic mpls architecture
.. (draft-ietf-mpls-arch)	Multiprotocol Label Switching Architecture	2001-01	 RFC 3031 (Proposed Standard) 

:rfc:`3032`

.. (draft-ietf-mpls-label-encaps)	MPLS Label Stack Encoding	2001-01	 RFC 3032 (Proposed Standard) 


Historic : Frame Relay and ATM
:rfc:`3034`
.. (draft-ietf-mpls-fr)	Use of Label Switching on Frame Relay Networks Specification	2001-01	 RFC 3034 (Proposed Standard)			
:rfc:`3035`
.. (draft-ietf-mpls-atm)	MPLS using LDP and ATM VC Switching	2001-01	 RFC 3035 (Proposed Standard)			


.. (draft-ietf-mpls-loop-prevention)	MPLS Loop Prevention Mechanism	2001-02	 RFC 3063 (Experimental)			

.. RFC 3443 
.. (draft-ietf-mpls-ttl)	Time To Live (TTL) Processing in Multi-Protocol Label Switching (MPLS) Networks	2003-01	 RFC 3443 (Proposed Standard) 


.. (draft-andersson-mpls-sig-decision)	The Multiprotocol Label Switching (MPLS) Working Group decision on MPLS signaling protocols	2003-02	 RFC 3468 (Informational) 
CR-LDP and RSVP-TE were developed together, but after some time the IETF decided to pursue the development and implementation of only one protocol.


.. (draft-ietf-mpls-ftn-mib)	Multiprotocol Label Switching (MPLS) Forwarding Equivalence Class To Next Hop Label Forwarding Entry (FEC-To-NHLFE) Management Information Base (MIB)	2004-06	 RFC 3814 (Proposed Standard)			Alex Zinin

.. (draft-ietf-mpls-in-ip-or-gre)	Encapsulating MPLS in IP or Generic Routing Encapsulation (GRE)	2005-03	 RFC 4023 (Proposed Standard) 


.. (draft-ietf-mpls-oam-requirements)	Operations and Management (OAM) Requirements for Multi-Protocol Label Switched (MPLS) Networks	2006-02	 RFC 4377 (Informational) 


.. for traceroute (draft-ietf-mpls-icmp)	ICMP Extensions for Multiprotocol Label Switching	2007-08	 RFC 4950 (Proposed Standard)			Ross Callon

.. (draft-ietf-mpls-ldp-igp-sync)	LDP IGP Synchronization	2009-03	 RFC 5443 (Informational) 


.. (draft-ietf-mpls-cosfield-def)	Multiprotocol Label Switching (MPLS) Label Stack Entry: "EXP" Field Renamed to "Traffic Class" Field	2009-02	 RFC 5462 (Proposed Standard) 


The label swapping forwarding paradigm
######################################

The operation of a switch in a network that uses the label swapping forwarding paradigm can be represented as a simple set of operations. Each packet that must be forwarded contains a label. We use the notation `p.label` as a shortcut for the label contained inside packet `p`. Each switch maintains a label forwarding table that stores for each incoming label the outgoing interface and the outgoing label. Using python syntax, we can represent this table as a list that stores couples containg the outgoing label and the outgoing interface.

.. code-block:: python

   LFT=[100] # number of entries
   LFT[1]=(2,3) # packet with label 1 is forwarded on interface 3 with label 3
   LFT[2]=(1,1) # packet with label 2 is forwarded on interface 1 with label 1
   
With such a forwarding table, the forwarding operation can be expressed as the following python method :

.. code-block:: python

 def forward(packet):
    outlif,outlabel=LFT[packet.label]
    packet.label=outlabel
    send(packet,outif)

A label switch needs to update the label of the packets that it forwards to allow a network to support a large number of virtual circuits. If the label switches were not allowed to update the packet labels, then there would be a direct mapping between each label and one virtual circuit inside a given network. Thus, a technology that uses :math:`n` bits to encode the label could not support more than :math:`~2^{n}` Different virtual circuits. This would be a severe limitation. By allowing each label switch to change the value of the packet label when a packet is forwarded, a maximum of :math:`~2^{n}` virtual circuits can be supported on each link. If :math:`n` is large enough, this is not a limitation in practice. Note that a low-end label switch can support a much smaller number of virtual circuits than :math:`~2^{n}` and still use the `forward` method described above by simply only using labels between `0` and `k` where `k` is the size of its label forwarding table.

Virtual circuits are then established by combining the Label Forwarding Tables of the label switches that are on the path chosen for the virtual circuit.

.. figure:: png/mpls-figs-004-c.png
   :align: center

   Figure : Example virtual circuits

In a large network, the number of virtual circuits that are required may be large and label switches that are located at the core of the network may need to support a large number of virtual circuits. These core label switches often also have high bandwidth interfaces and supporting a large number of circuits at high speed may be difficult from an implementation viewpoint. For scalability reasons, technologies that rely on the label swapping paradigm usually use a hierarchy of virtual circuits. For example ATM uses a two-levels hierarchy with virtual circuits and virtual paths. A virtual path may contain a large number of virtual circuits. In a typical deployment, virtual circuits are used at the network edge and several virtual circuits are grouped together in a single virtual path when entering the core network so that core label switches can forward the labelled packets by inspecting only the virtual path information. Each ATM cell contains two labels : a virtual circuit identifier and a virtual path identifier. Core switches only use the virtual path identifier while edge switches can forward the packet by using the virtual circuit and the virtual path identifiers. 

.. index:: Label Switching Router (LSR), LSR

MultiProtocol Label Switching started as a technique that allows IP packets to be efficiently transmitted by using the label switches of the underlying network, e.g. ATM or Frame Relay. A typical initial deployment of MPLS was a network with IP routers at the edge of the network and ATM switches in the network backbone. A router that supports MPLS is often called a Label Switching Router :rfc:`3031`. We use this terminology in the chapter and reserve the word Router for a traditional router that does not implement MPLS. When an IP packet was received by an ingress LSR at the edge of the network, the LSR had to insert a label inside the packet before forwarding it through the backbone. The packet was then processed by the core LSRs in the backbone before reaching the egress LSR. The egress LSR then removed the packet's label before forwarding it as a normal IP packet ousite the MPLS network. This is illustrated in in the figure below.

.. figure:: png/mpls-figs-006-c.png
   :align: center

   Figure : Core and edge routers in an MPLS network 


Such an utilization of MPLS can be modelled by defining the behaviour of a LSR as three basic operations :

 - `push` : when an edge LSR receives a network packet it pushes a label in front of the packet before forwarding it as a labelled packet
 - `swap` : when a LSR receives a labelled packet, it can change the value of the packet label before forwarding it on the chosen outgoing interface
 - `pop` : when a LSR receives a labelled packet, it can remove the label before forwarding 

The figure below illustrates these operations in a simple network.

.. figure:: png/mpls-figs-007-c.png
   :align: center

   Figure : The basic operations performed on labelled packets


One of the main innovations introduced by MultiProtocol Label Switching compared to the other label switching techniques is that an MPLS packet contains a `stack` of labels that has a potential unlimited depth. All labels are placed before the network-layer packet header and the  `label stack` is encoded in the packet header by adding one `bottom of stack` bit after the label. This `bottom of stack` bit is set only in the label that occupies the bottom position in the stack. As we will see throughout the chapter, this label stack has enabled very innovative and scalable solutions in MPLS networks. MPLS can use different types of labels. In the past, the first deployments used the underlying ATM or frame relay labels. However, today most of the MPLS deployments use the 32 bits shim header defined in :rfc:`3032` and represented below.

::

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 |                Label                  | TC  |S|       TTL     | 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 

 The MPLS shim header 


The MPLS header contains four fields :

 - Label. The MPLS label is encoded as a twenty bits field that represents an unsigned integer. The sixteen smallest values are reserved for specific utilisations [#freserved]. The other MPLS Labels can be used by all LSRs.
 - TC. The Traffic Class is a 3 bits field defined in :rfc:`5462`. This field can be used to specify classes of packets that should be handled differently by the intermediate LSR from a traffic control viewpoint. Its usage will be discussed in chapter XX.
 - Bottom of stack bit (S). This bit is only set in the 
 - Time-to-Live. This field as the same purpose as in the IP header. When an ingress LSR adds a label to a regular IP packet, it copies the TTL of the packet in the MPLS header. Intermediate LSRs decrement the value of the TTL field in the  outer MPLS header and discard the packet if the TTL value becomes smaller than `0` :rfc:`3443`. This allows MPLS LSRs to discard packets when there is a forwarding loop as IP routers would do with regular IP packets. Another utilisation is an MPLS specific `traceroute` that relies on ICMP extensions defined in :rfc:`4950` that can be used by an MPLS LSR to to provide information about the MPLS labels in the ICMP message that it returns after having discard an MPLS packet whose TTL has reached `0`.

The MPLS header is inserted between the datalink layer header and the network layer header. As an example, the figure below shows an Ethernet frame that contains an MPLS header with a label stack containing labels `123` and `456` that is followed by an IP packet. Ethertype `0x8447` is reserved for the transport of MPLS labelled packets in Ethernet frames :rfc:`5332`.

::

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |								   |	
   +          48 bits              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    
   |    Destination Address	   |			           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+       48 bits       	   +
   |                    		Source Address	           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |		Type (0x8847)	   |	Label (123)		   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |	   |  TC |0|    TTL	   | 	Label (456)		   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |	   |  TC |1|    TTL	   |Ver(4) |  IHL  |    DS Field   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |       Total Length            |     Identification		   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |								   |
   ~                        IP packet (cont.)	                   ~
   |								   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |			32 bits		CRC			   |	
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   IPv4 packet with a stack of two MPLS labels in an Ethernet frame


.. [#freserved] See http://www.iana.org/assignments/mpls-label-values/mpls-label-values.xml for the list of the currently reserved MPLS label values.

By using python pseudocode, an MPLS packet can be represented as a packet that contains a stack of labels (with `packet.lstack` representing the label stack). The MPLS Label Forwarding Table used by an MPLS LSR becomes a table that for each label returns a tuple containing an outgoing interface and an operation to be performed on the packet with optional parameters for the push and swap operations:

.. code-block:: python

 def forward(packet) :
    # packet.lstack[0] is the uppermost label of the stack
    outif,operation,l1,l2=LFT[packet.lstack[0]] 
    if operation=="push" :
        packet.lstack.insert(0,l1) # push l1 on top of stack
    elif operation=="swap" :
    	packet.lstack[0]=l1  # swap first label of stack
    else : # operation == "push"
    	packet.lstack.[0]=l1  # swap first label of stack
	packet.lstack.insert(0,l2) # push label on stack
    send(packet,outif)

.. index:: per-platform label space, per-interface label space

.. note:: per-platform and per-interface label spaces

 To ensure The MPLS Label Forwarding Table can be organised in two different ways. A first solution, called `per-interface label space` in :rfc:`3031`, is to assign the MPLS labels independently on each interface. In this case, the same label can be used for different Label Switches Paths on different interfaces. Today, MPLS LSR use the shim header defined in :rfc:`3032`. This header uses twenty bits to encode the MPLS label. This implies that a switch that uses `per-interface label space` could support up to :math:`2^20` different LSPs on each interface. This implies, of course, that a different Label Forwarding Table is used on each interface of the LSR. The second solution, `per-platform label space` :rfc:`3032`, is to ensure that a given MPLS label is never used on two different interfaces. Conceptually, the LSR can use a single LFT that is downloaded on all its interfaces. A drawback of this approach is that an LSR that uses `per-platform label space` cannot support more than :math:`2^20` different LSPs. This could be a limitation on LSRs with a large number of interfaces. Despite of this limitation, most LSRs today support `per-platform label space` because it enables them to efficiently provide fast-restoration services as explained in section XX.


By correctly configuring the Label Forwarding Tables on the LSRs inside a network, it is possible to build Label Switched Paths (LSPs). A LSP is defined in :rfc:`3031` as a sequence of LSRs. The first (resp. last) LSR is the ingress (resp. egress) LSR and the LFTs of all the LSRs are such that if the ingress LSR sends a labelled packet to the second LSR on the LSP, the packet will be label-switched by all the intermediate LSRs listed in the LSR sequence. A common utilisation of LSPs is to establish unidirectonnal LSPs between an ingress LSR and an egress LSR. This is illustrated in the figure below.

.. figure:: png/mpls-figs-008-c.png
   :align: center

   Figure : Unidirectionnal LSPs in a simple network

An interesting point to discuss in such a network is the Label Forwarding Table that will be used by LSR3. In the example above, three LSPs have been established. The first LSP (black plain arrow) goes from LSR1 to LSR4 via LSR3. The second LSR (dotted blue arrow) goes from LS2 to LSR4 via LSR3. The third LSP (dashed red arrow) goes from LSR3 to LSR4. A classical implementation of such LSPs is to create one entry per LSP on each intermediate LSR. For example, LSR3's LFT could be configured as shown by the pseudocode below :

.. code-block:: python

    LSR3.LFT[black]=("East","swap",41)
    LSR3.LFT[blue]=("East","swap",42)
    LSR3.LFT[red]=("East","push",43)

With this configuration of the LFT, LSR4 would receive the packets with a different label on the three LSPs that it terminates. This could allow LSR4 to process differently the packets received on the three LSPs. However, in practice there are many situations where the egress LSR processes all the labelled packets that it receives in the same manner, e.g. because it is the final destination for these packets. In this case, a better solution is to allow several LSPs that have the same destination to share the same MPLS label on the intermediate links. In the example above, the LSR3's LFT could have been configured as shown below :

.. code-block:: python

    LSR3.LFT[black]=("East","swap",40)
    LSR3.LFT[blue]=("East","swap",40)
    LSR3.LFT[red]=("East","push",40)


.. todo explain organisation et rooted LSPs


.. figure:: png/mpls-figs-008-c.png
   :align: center

   Figure : Destination-rooted LSPs in a simple network


Such a configuration minimises the number of labels that are used inside the network. Consider the common deployment of a network with :math:`n` LSRs where a full-mesh of unidirectionnal LSPs must be established. With unidirectionnal LSPs, :math:`{n \times (n-1)}` LSPs must be established and links in the backbone may have to carry a large fraction of these LSPs. With the solution above, LSPs that have the same destination are merged at intermediate LSRs and there are at most :math:`n` different LSPs passing through a link, an important difference from a scalability viewpoint.


:rfc:`3031` 


.. Label entry

.. expliquer comment on peut construire un LSP de bout en bout avec un petit exemple

.. expliquer comment faire merger deux LSPs vers la même destination en un routeur, cela motivera LDP qui est mal motivé aujourd'hui

.. besoin de scalabilite avec des LSP



.. rubric:: Footnotes


Integrating label swapping and IP
################################# 

.. definir FEC
.. creation de LSP




Destination-based packet forwarding
===================================

.. expliquer LDP, découverte des voisins (mais c'est anecdotique), surtout le fait qu'il y a une connexion TCP et expliquer comment les label-FEC mapping sont échangés, liberal versus ordered

.. d�finition d'une FEC

LDP :rfc:`5036`

.. (draft-ietf-mpls-rfc3036bis)	LDP Specification	2007-10	 RFC 5036 (Draft Standard) 


..        0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |  Prefix (2)   |     Address Family            |     PreLen    |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                     Prefix                                    |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

         Address Family
            Two octet quantity containing a value from ADDRESS FAMILY
            NUMBERS in [ASSIGNED_AF] that encodes the address family for
            the address prefix in the Prefix field.

         PreLen
            One octet unsigned integer containing the length in bits of
            the address prefix that follows.  A length of zero indicates
            a prefix that matches all addresses (the default
            destination); in this case, the Prefix itself is zero
            octets).

         Prefix
            An address prefix encoded according to the Address Family
            field, whose length, in bits, was specified in the PreLen
            field, padded to a byte boundary.


from LDP spec

3.5.7.1.1.  Independent Control Mapping

   If an LSR is configured for independent control, a mapping message is
   transmitted by the LSR upon any of the following conditions:



Andersson, et al.           Standards Track                    [Page 67]
 
RFC 5036                   LDP Specification                October 2007


      1. The LSR recognizes a new FEC via the forwarding table, and the
         label advertisement mode is Downstream Unsolicited
         advertisement.

      2. The LSR receives a Request message from an upstream peer for a
         FEC present in the LSR's forwarding table.

      3. The next hop for a FEC changes to another LDP peer, and Loop
         detection is configured.

      4. The attributes of a mapping change.

      5. The receipt of a mapping from the downstream next hop  AND

            a) no upstream mapping has been created  OR
            b) loop detection is configured  OR
            c) the attributes of the mapping have changed.

3.5.7.1.2.  Ordered Control Mapping

   If an LSR is doing Ordered Control, a Mapping message is transmitted
   by downstream LSRs upon any of the following conditions:

      1. The LSR recognizes a new FEC via the forwarding table and is
         the egress for that FEC.

      2. The LSR receives a Request message from an upstream peer for a
         FEC present in the LSR's forwarding table, and the LSR is the
         egress for that FEC OR has a downstream mapping for that FEC.

      3. The next hop for a FEC changes to another LDP peer, and Loop
         Detection is configured.

      4. The attributes of a mapping change.

      5. The receipt of a mapping from the downstream next hop  AND

            a) no upstream mapping has been created   OR
            b) Loop Detection is configured   OR
            c) the attributes of the mapping have changed.

3.5.7.1.3.  Downstream on Demand Label Advertisement

   In general, the upstream LSR is responsible for requesting label
   mappings when operating in Downstream on Demand mode.  However,
   unless some rules are followed, it is possible for neighboring LSRs
   with different advertisement modes to get into a livelock situation
   where everything is functioning properly, but no labels are



Andersson, et al.           Standards Track                    [Page 68]
 
RFC 5036                   LDP Specification                October 2007


   distributed.  For example, consider two LSRs Ru and Rd where Ru is
   the upstream LSR and Rd is the downstream LSR for a particular FEC.
   In this example, Ru is using Downstream Unsolicited advertisement
   mode and Rd is using Downstream on Demand mode.  In this case, Rd may
   assume that Ru will request a label mapping when it wants one and Ru
   may assume that Rd will advertise a label if it wants Ru to use one.
   If Rd and Ru operate as suggested, no labels will be distributed from
   Rd to Ru.

   This livelock situation can be avoided if the following rule is
   observed: an LSR operating in Downstream on Demand mode SHOULD NOT be
   expected to send unsolicited mapping advertisements.  Therefore, if
   the downstream LSR is operating in Downstream on Demand mode, the
   upstream LSR is responsible for requesting label mappings as needed.

3.5.7.1.4.  Downstream Unsolicited Label Advertisement

   In general, the downstream LSR is responsible for advertising a label
   mapping when it wants an upstream LSR to use the label.  An upstream
   LSR may issue a mapping request if it so desires.

   The combination of Downstream Unsolicited mode and Conservative Label
   retention can lead to a situation where an LSR releases the label for
   a FEC that it later needs.  For example, if LSR Rd advertises to LSR
   Ru the label for a FEC for which it is not Ru's next hop, Ru will
   release the label.  If Ru's next hop for the FEC later changes to Rd,
   it needs the previously released label.

   To deal with this situation, either Ru can explicitly request the
   label when it needs it, or Rd can periodically re-advertise it to Ru.
   In many situations Ru will know when it needs the label from Rd.  For
   example, when its next hop for the FEC changes to Rd.  However, there
   could be situations when Ru does not.  For example, Rd may be
   attempting to establish an LSP with non-standard properties.  Forcing
   Ru to explicitly request the label in this situation would require it
   to maintain state about a potential LSP with non-standard properties.

   In situations where Ru knows it needs the label, it is responsible
   for explicitly requesting the label by means of a Label Request
   message.  In situations where Ru may not know that it needs the
   label, Rd is responsible for periodically re-advertising the label to
   Ru.

   For this version of LDP, the only situation where Ru knows it needs a
   label for a FEC from Rd is when Rd is its next hop for the FEC, Ru
   does not have a label from Rd, and the LSP for the FEC is one that
   can be established with TLVs defined in this document.


port numbers

   The UDP port for LDP Hello messages is 646.

   The TCP port for establishing LDP session connections is 646.



3.4.1.  FEC TLV

   Labels are bound to Forwarding Equivalence Classes (FECs).  A FEC is
   a list of one or more FEC elements.  The FEC TLV encodes FEC items.

   Its encoding is:

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0| FEC (0x0100)              |      Length                   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        FEC Element 1                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                                                               |
   ~                                                               ~
   |                                                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        FEC Element n                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   FEC Element 1 to FEC Element n
      There are several types of FEC elements; see Section "FECs".  The
      FEC element encoding depends on the type of FEC element.

      A FEC Element value is encoded as a 1 octet field that specifies
      the element type, and a variable length field that is the type-
      dependent element value.  Note that while the representation of
      the FEC element value is type-dependent, the FEC element encoding
      itself is one where standard LDP TLV encoding is not used.

      The FEC Element value encoding is:

         FEC Element       Type      Value
         type name

           Wildcard        0x01      No value; i.e., 0 value octets;
                                         see below.
           Prefix          0x02      See below.

      Note that this version of LDP supports the use of multiple FEC
      Elements per FEC for the Label Mapping message only.  The use of
      multiple FEC Elements in other messages is not permitted in this
      version, and is a subject for future study.

      Wildcard FEC Element

         To be used only in the Label Withdraw and Label Release
         messages.  Indicates the withdraw/release is to be applied to
         all FECs associated with the label within the following label
         TLV.  Must be the only FEC Element in the FEC TLV.





Andersson, et al.           Standards Track                    [Page 34]
 
RFC 5036                   LDP Specification                October 2007


      Prefix FEC Element value encoding:

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |  Prefix (2)   |     Address Family            |     PreLen    |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                     Prefix                                    |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

         Address Family
            Two octet quantity containing a value from ADDRESS FAMILY
            NUMBERS in [ASSIGNED_AF] that encodes the address family for
            the address prefix in the Prefix field.

         PreLen
            One octet unsigned integer containing the length in bits of
            the address prefix that follows.  A length of zero indicates
            a prefix that matches all addresses (the default
            destination); in this case, the Prefix itself is zero
            octets).

         Prefix
            An address prefix encoded according to the Address Family
            field, whose length, in bits, was specified in the PreLen
            field, padded to a byte boundary.

.. Bien montrer la diff�rence entre un LSP de end-to-end � un LSP �tablir par LDP qui forme un arbre centr� vers la destination. il faudra probablement parler de l'ecmp �galement dans cette discussion


.. (draft-ietf-mpls-ldp-interarea)	LDP Extension for Inter-Area Label Switched Paths (LSPs)	2008-07	 RFC 5283 (Proposed Standard)  
.. don't think that this is required

BGP-free ISP backbones
======================

.. cela pourrait s'intégrer avec la section précédente. Essayer d'expliquer comment on encode les labels dans bgp et ce que cela peut approter de ne pas faire de routage BGP dans un AS. C'est l'occasion de présenter le problème de la défelction qui n'a pas encore été présenté dans le bouquin

:rfc:`3107`
.. (draft-ietf-mpls-bgp4-mpls)	Carrying Label Information in BGP-4	2001-05	 RFC 3107 (Proposed Standard) 


MPLS applications
#################





Traffic engineering
===================

.. durant le cours, j'ai passé du temps à expliquer en détails les contraintes et à quoi elles servent en pratique avec un exemple style réseau maison de pierre. C'est à mon avis bcp plus efficace que de montrer les détails de RSVPTE. cela vaudrait la peine de décrire différents exemples pour montrer à quoi peuvent servivr les infos dans ospf-te. On pourrait aussi leur donner un dijkstra en python par exemple et les faire jouer avec de l'établissement de LSPs et expliquer les problèmes que cela pose. Ils pourraient facilement faire de petites simulations. ce serait bcp plus efficace que des détails sur rsvp.
.. développer ces exemples et formaliser un peu ce que l'on fait au niveau de l'établissement de chemins dans le réseau
.. peut-être que l'on peut aller jusque montrer l"intéreêt des pces dans le cadre des interareas par exemple
.. idem pour fast reroute, je pense que l'on peut les faire calculer plein de choses par eux-mêmes avec un Dijkstra. Une solution serait de voir cette partie pour après les vacances de Paques et que je la prépare avec Pierre sur base de networkx


A network is a directed graph G(V,E) where V is a set of routers and E a set of vertices.

.. expliquer le problème général est les différentes optimisations possibles


IGP weight optimisation

.. Fortz, B., & Thorup, M. (2000). Internet traffic engineering by optimizing OSPF weights. Proceedings IEEE INFOCOM 2000 Conference on Computer Communications Nineteenth Annual Joint Conference of the IEEE Computer and Communications Societies Cat No00CH37064, 2, 519-528. Ieee. Retrieved from http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=832225

ECM

:rfc:`2992`

.. Fortz, B., & Thorup, M. (2002). Optimizing OSPF/IS-IS weights in a changing world. IEEE Journal on Selected Areas in Communications, 20(4), 756-767. Retrieved from http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=1003042

.. expliquer comment on peut calculer la matrice de trafic
.. http://www.maths.adelaide.edu.au/matthew.roughan/traffic_matrices.html


.. mesures de Pascal pour ECMP


:rfc:`2702`
.. (draft-ietf-mpls-traffic-eng)	Requirements for Traffic Engineering Over MPLS	1999-09	 RFC 2702 (Informational)			


.. Xiao, X., Hannan, A., Bailey, B., & Ni, L. (2000). Traffic engineering with MPLS in the Internet. Ieee Network, 14(2), 28-33. Institute of Electrical and Electronics Engineers, Inc, 445 Hoes Ln, Piscataway, NJ, 08854-1331, USA,. Retrieved from http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=826369


:rfc:`3272` te
:rfc:`3209`

.. (draft-ietf-mpls-rsvp-lsp-tunnel)	RSVP-TE: Extensions to RSVP for LSP Tunnels	2001-12	 RFC 3209 (Proposed Standard) 


.. RFC 5712 
.. (draft-ietf-mpls-soft-preemption)	MPLS Traffic Engineering Soft Preemption	2010-01	 RFC 5712 (Proposed Standard)			Adrian Farrel


.. (draft-ietf-mpls-te-scaling-analysis)	An Analysis of Scaling Issues in MPLS-TE Core Networks	2009-02	 RFC 5439 (Informational) 


.. .. (draft-ietf-mpls-diff-ext)	Multi-Protocol Label Switching (MPLS) Support of Differentiated Services	2002-05	 RFC 3270 (Proposed Standard) 

Failure recovery
================

.. Vasseur

.. (draft-ietf-mpls-rsvp-lsp-fastreroute)	Fast Reroute Extensions to RSVP-TE for LSP Tunnels	2005-05	 RFC 4090 (Proposed Standard)		 2	Alex Zininailure

.. (draft-ietf-mpls-recovery-frmwrk)	Framework for Multi-Protocol Label Switching (MPLS)-based Recovery	2003-02	 RFC 3469 (Informational) 

.. (draft-ietf-mpls-rsvp-lsp-fastreroute)	Fast Reroute Extensions to RSVP-TE for LSP Tunnels	2005-05	 RFC 4090 (Proposed Standard)		 2	Alex Zinin
.. (draft-ietf-mpls-lsp-ping)	Detecting Multi-Protocol Label Switched (MPLS) Data Plane Failures	2006-02	 RFC 4379 (Proposed Standard) 

.. probablement expliquer BFD brièvement car c'est un principe important
.. pas encore de RFC apparemment

.. Pierre Francois and Olivier Bonaventure. 2005. An evaluation of IP-based fast reroute techniques. In Proceedings of the 2005 ACM conference on Emerging network experiment and technology (CoNEXT '05). ACM, New York, NY, USA, 244-245. DOI=10.1145/1095921.1095962 http://doi.acm.org/10.1145/1095921.1095962

IP fast reroute
:rfc:`5714`                       IP Fast Reroute Framework



description LFA
:rfc:`5286`

.. Basic Specification for IP Fast Reroute: Loop-Free Alternates

mesures de Pierre pout LFA et autres techniques

Network Links LFA U-turns Tunnel Directed Notvia

Tunnel

Abilene 28 42% 85% 92% 100% -

GEANT 72 66% 93% 100% - -

ISP1 114 54% 71% 71% 100% -

ISP2 26 15% 42% 100% - -

ISP3 265 65% 95% 96% 100% -

.. http://inl.info.ucl.ac.be/publications/evaluation-ip-based-fast-reroute-tech

.. Alex Raj, Oliver C. Ibe, A survey of IP and multiprotocol label switching fast reroute schemes, Computer Networks, Volume 51, Issue 8, 6 June 2007, Pages 1882-1907, ISSN 1389-1286, DOI: 10.1016/j.comnet.2006.09.010.
.. (http://www.sciencedirect.com/science/article/B6VRG-4M524VP-1/2/d867cbd03b32f1970b49a725d7e9cdb0)
.. Keywords: MPLS networks; IP fast reroute; Protection switching; Micro-loop prevention; Loop-free alternate; U-turn alternate

Quality of Service
==================

.. pas sur qu'il faut présenter cela dans la partie MPLS

Virtual Private Networks
========================

Virtual Private Networks (VPNs) are probably the most frequent usage of MultiProtocol Label Switching.


.. l2 versus l3 vpn
.. role bgp
.. pas certain que les route reflectors doivent être vus en détails
.. expliquer rd, rt
.. se limiter à intradomain BGP/MPLS VPN mais montrer qu'il y a des possibilités d'étendre au dela d'un réseau unique

