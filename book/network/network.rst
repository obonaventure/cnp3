.. _chapter-network: 

================== 
The network layer
==================

The network layer is a very important layer in computer networks as it is the glue that allows the applications running above the transport layers to use a wide range of different and interconnected networks built with different datalink and physical layers. The network layer enables applications to run above networks built with very different network technologies. 

In this chapter, we first explain the principles of the network layer. These principles include the datagram and virtual circuit modes, the separation between the data plane and the control plane and the algorithms used by routing protocols. Then, we explain in more details the network layer in the Internet, starting with IPv4 and IPv6 and then moving to the routing protocols (RIP, OSPF and BGP).

.. include:: principles.rst


.. todo explain broadcast address IPv4 ?

Internet Protocol
#################

The Internet Protocol (IP) is the network layer protocol of the TCP/IP protocol suite. IP allows the applications running above the transport layer (UDP/TCP) to use a wide range of heterogeneous datalink layers. IP was designed when most point-to-point links were telephone lines with modems. Since then, IP has been able to use Local Area Networks (Ethernet, Token Ring, FDDI, ...), new wide area data link layer technologies (X.25, ATM, Frame Relay, ...) and more recently wireless networks (802.11, 802.15, UMTS, GPRS, ...). The flexibility  of IP and its ability to use various types of underlying data link layer technologies is one of its key advantages.

.. figure:: png/network-fig-051-c.png
   :align: center
   :scale: 70

   IP and the reference model

.. there is a draft on expectations of lower layer

The current version of IP is version 4 specified in :rfc:`791`. We first describe this version and later explain IP version 6 that is expected to replace IP version 4 in the future.

.. include:: ipv4.rst

.. include:: ipv6.rst

.. include:: middleboxes.rst


Routing in IP networks
######################

In a large IP network such as the global Internet, routers need to exchange routing information. The Internet is an interconnection of networks, often called domains, that are under different responsibilities. As of this writing, the Internet is composed on more than 30,000 different domains and this number is still growing. A domain can be a small enterprise that manages a few routers in a single building, a larger enterprise with hundred routers at multiple locations or a large Internet Service Provider that manages thousands of routers. Two classes of routing protocols are used to allow these domains to efficiently exchange routing information. 


.. figure:: png/network-fig-093-c.png
   :align: center
   :scale: 70
   
   Organisation of a small Internet


The first class of routing protocols are the `intradomain routing protocols` (sometimes also called the interior gateway protocols or :term:`IGP`). An intradomain routing protocol is used by all the routers inside a domain to exchange routing information about the destinations that are reachable inside the domain. There are several intradomain routing protocols. Some domains use :term:`RIP`  which is a distance vector protocol. Other domains use link-state routing protocols such as :term:`OSPF` or :term:`IS-IS`. Finally, some domains use static routing or proprietary protocols such as :term:`IGRP` or :term:`EIGRP`.

These intradomain routing protocols usually have two objectives. First, they distribute routing information that corresponds to the shortest path between two routers in the domain. Second, they should allow the routers to quickly recover from link and router failures.

The second class of routing protocols are the `interdomain routing protocols` (sometimes also called the exterior gateway protocols or :term:`EGP`). The objective of an interdomain routing protocol is to distribute routing information between domains. For scalability reasons, an interdomain routing protocol must distribute aggregated routing information and considers each domain as a blackbox.

A very important difference between intradomain and interdomain routing are the `routing policies` that are used by each domain. Inside a single domain, all routers are considered equal and when several routes are available to reach a given destination prefix, the best route is selected based on technical criteria such as the route with the shortest delay, the route with the minimum number of hopsor the route with the highest bandwidth, ... 

When we consider the interconnection of domains that are managed by different organisations, this is not true anymore. Each domain implements its own routing policy. A routing policy is composed of three elements : an `import filter` that specifies which routes can be accepted by a domain, an `export filter` that specifies which routes can be advertised by a domain and a ranking algorithm that selects the best route when a domain knows several routes towards the same destination prefix. As we will see later, another important difference is that the objective of the interdomain routing protocol is to find the `cheapest` route towards each destination. There is only one interdomain routing protocol : :term:`BGP`.


Intradomain routing 
===================

In this section, we briefly describe the key features of the two main intradomain unicast routing protocols : RIP and OSPF. 

.. include:: rip.rst

.. include:: ospf.rst

.. include:: bgp.rst

Summary
#######





.. include:: ../links.rst

.. include:: exercises/ex-network.rst

.. include:: exercises/cha-network.rst
