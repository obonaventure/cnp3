.. Copyright |copy| 2011 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

=============================
MultiProtocol Label Switching
=============================


In the first half of the 1990s, network bandwidth was growing at a rapid pace. At that time, IP routers were basically powerful computers that processed IP packets entirely in software. The performance of IP routers was

On such software-based routers, the longest prefix match that is used to forwar

Given the growth in network bandwidth, researchers and vendors feared that the MultiProtocol Label Switching (MPLS) was invented

While IP was already deployed in the early 1990s, other networking technologies were being developed. IP was used mainly in research networks and there were only few commercial network operators that were using IP. The public telecommunication operators had developped other networking technologies to carry data. X.25 started in the 1970s and was deployed on a larger scale during the 1980s. X.25 was used mainly to provide data services to enterprises, but some research networks, notably in Europe used IP over X.25. In France, the minitel service was built on top of the Transpac X.25 network. However, X.25 was rather complex and included several mechanisms for error and flow control at different layers. During the 1980s, the quality of the data transmission links improved significantly both in bandwidth and in transmission error rates. These improvements lead to the development of two techniques to carry data over virtual circuits in public telecommunication networks : Frame Relay [Buckwalter2000]_ and Asynchronous Transfer Mode (ATM) [LeBoudec1992]_ [dePrycker1995]_. These two techniques rely on virtual circuits to forward from their source to their destination along a precomputed path. In ATM and Frame relay networks, intermediate nodes are called switches. Frame relay networks carry variable length frames while ATM switches process fixed-size frames [#fcell]_. 

.. In ATM and frame relay networks, when two hosts need to exchange data, they first need to establish a virtual circuit through intermediate switches. This is done by using  that are called cellsreEach frame contains a label and intermediate nod

Forward(interface in, label l) -> interface out, label

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


.. montrer que cela fonctionne en mettant une forme d'algorithme en python par exemple

.. function that from an incoming label returns an operation and a nexthop


.. Label entry

::
 0                   1                   2                   3
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 |                Label                  | TC  |S|       TTL     | 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 

 Figure : The MPLS label 

.. expliquer comment on peut construire un LSP de bout en bout avec un petit exemple

.. expliquer comment faire merger deux LSPs vers la même destination en un routeur, cela motivera LDP qui est mal motivé aujourd'hui



Integrating label swapping and IP
################################# 

Destination-based packet forwarding
===================================

.. expliquer LDP, découverte des voisins (mais c'est anecdotique), surtout le fait qu'il y a une connexion TCP et expliquer comment les label-FEC mapping sont échangés, liberal versus ordered

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

