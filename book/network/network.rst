================== 
The network layer
==================

.. :rfc:`3927` special addresses

.. http://tools.ietf.org/html/draft-touch-intarea-ipv4-unique-id-01 comment choisir les IP ids

Principles of the network layer
###############################


Datagram mode
=============


Virtual circuit mode
=====================

Routing 
=======



Internet Protocol
#################



IP version 4
============

ip :rfc:`791`


path mtu discovery :rfc:`1191`

dhcp :rfc:`2131

ICMP version 4
==============

:rfc:`792`


NAT


   [RFC2993]   Hain, T., "Architectural Implications of NAT", RFC 2993,
               November 2000.

   [RFC3027]   Holdrege, M. and P. Srisuresh, "Protocol Complications
               with the IP Network Address Translator (NAT)", RFC 3027,
               January 2001.

   [RFC2663]   Srisuresh, P. and M. Holdrege, "IP Network Address
               Translator (NAT) Terminology and Considerations", RFC
               2663, August 1999.

   [RFC3022]   Srisuresh, P. and K. Egevang, "Traditional IP Network
               Address Translator (Traditional NAT)", RFC 3022, January
               2001.

IP version 6
============

R. Hinden, S. Deering, IP Version 6 Addressing Architecture, RFC4291,  February 2006

See http://www.ripe.net/ripe/docs/ripe-388.html for the policy used by RIPE to allocate IP prefixes in Europe

R. Hinden, B. Haberman,   Unique Local IPv6 Unicast Addresses, RFC4193, October 2005

S. Deering, B. Hinden, Internet Protocol, Version 6 (IPv6) Specification , RFC2460, Dec 1998


Several documents have been written about the usage of the Flow label. The last one is

  J. Rajahalme,  A. Conta, B. Carpenter, S. Deering, IPv6 Flow Label Specification, RFC3697, 2004

options 

An example hop-by-hop option is the router alert option defined in
A. Jackson, C. Partridge, IPv6 Router Alert Option  RFC2711, 1999

type 0 routing header

The type 0 routing header was deprecated in 
J. Abley, P. Savola, G. Neville-Neil, Deprecation of Type 0 Routing Headers in IPv6  RFC5095, Dec. 2007

For more information about the security issues with this header, see
Biondi, P. and A. Ebalard, "IPv6 Routing Header  Security", CanSecWest Security Conference 2007,
April 2007. http://www.secdev.org/conf/IPv6_RH_security-csw07.pdf

ICMP version 6
==============

A. Conta, S. Deering, M. Gupta, Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6)     Specification, RFC4443, March 2006

:rfc:`4443`

Intradomain routing in IP networks 
==================================


RIP
---

La version actuelle de RIP East définie dans 
RFC2453 RIP Version 2. G. Malkin. November 1998

Une autre description de RIP East disponible dans : 
Gary Malkin, RIP : an intra-domain routing protocol, Addison-Wesley, 2002 

IP multicast East couvert dans le cours avancé. A ce stade, il suffit de considérer IP multicast (avec TTL=1) comme étant un mécanisme permettant à un routeur connecté sur un réseau local d'envoyer, en une seule transmission, un paquet qui sera reçu par tous les routeurs RIP connectés à ce réseau local.

The Synchronization of Periodic Routing Messages , Floyd, S., and Jacobson, V. IEEE/ACM Transactions on Networking, V.2 N.2, p. 122-136, April 1994.

OSPF
----
Pour plus d 'informations sur OSPF, voir 
:rfc:`2328` OSPF Version 2. J. Moy. April 1998.
ou
J. Moy, OSPF: Anatomy of an Internet Routing Protocol, Addison Wesley, 1998

Interdomain routing in the Internet
===================================

RFC 2622 Routing Policy Specification Language (RPSL). C. Alaettinoglu, C.
     Villamizar, E. Gerich, D. Kessens, D. Meyer, T. Bates, D. Karrenberg,
     M. Terpstra. June 1999.

RFC 2650 Using RPSL in Practice. D. Meyer, J. Schmitz, C. Orange, M.
     Prior, C. Alaettinoglu. August 1999.

Internet Routing Registries contain the routing policies of various ISPs, see :

http://www.ripe.net/ripencc/pub-services/whois.html
http://www.arin.net/whois/index.html
http://www.apnic.net/apnic-bin/whois.pl

 L. Subramanian, S. Agarwal, J. Rexford, and RH Katz. Characterizing the Internet hierarchy from multiple vantage points. In IEEE INFOCOM, 2002


but see recent arbor data


Middleboxes
===========

NAT
---


Firewall
--------


     Cheswick, William R., Bellovin, Steven M., Rubin, Aviel D. Firewalls and internet security - Second edition - Repelling the Wily Hacker, Addison-Wesley 2003
