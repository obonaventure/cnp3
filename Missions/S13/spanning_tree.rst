Ethernet networks 
=================

1. Consider the switched network shown in the figure below. What is the spanning tree that will be computed by 802.1d in this network assuming that all links have a unit cost ? Indicate the state of each port.

 .. figure:: fig/switchesok.png
    :align: center
    :scale: 30 

    A small network composed of Ethernet switches

2. Consider the switched network shown in the figure above.  In this network, assume that the LAN between switches `3` and `12` fails. How should the switches update their port/address tables after the link failure ?

3. Many enterprise networks are organized with a set of backbone devices interconnected by using a full mesh of links as shown in the figure below. In this network, what are the benefits and drawbacks of using Ethernet switches and IP routers running OSPF ?

 .. figure:: fig/backbone.png
    :align: center
    :scale: 80 

    A typical enterprise backbone network 

4. Most commercial Ethernet switches are able to run the Spanning tree protocol independently on each VLAN. What are the benefits of using per-VLAN spanning trees ?


Review exercises
================


TCP 
---

1. The figure below describes the evolution of the congestion window of a TCP connection. Can you find the reasons for the three events that are marked in the figure ?

 .. figure:: fig/revision-figs-001-c.png
    :align: center
    :scale: 70 

    Evolution of the congestion window

2. The figure below describes the evolution of the congestion window of a TCP connection. Can you find the reasons for the three events that are marked in the figure ?

 .. figure:: fig/revision-figs-002-c.png
    :align: center
    :scale: 70 

    Evolution of the congestion window

3. A web server serves mainly HTML pages that fit inside 10 TCP segments. Assuming that the transmission time of each segment can be neglected, compute the total transfer time of such a page (in round-trip-times) assuming that :

 - the TCP stack uses an initial window size of 1 segment
 - the TCP stack uses an initial window size of three segments

 For each of the two initial window size, explain what happens when 

 - The first segment is lost
 - The third segment is lost

4. What are the variables to be maintained by an implementation of the sender (resp. receiver) of an implementation of : 

 - Go-Back-N
 - Selective Repeat
 - TCP

 Explain shortly the role of each of those variables


IP Routing
----------
 
1.  Explain what are the issues that we can encounter with : 

 - Link state protocols
 - Distance vector protocols

 Provide a short explanation of the situation in which each issue occurs, and if possible, explain also how to solve it.  

Border Gateway Protocol
-----------------------

1. In the network below, AS1 has a customer to which it provides connectivity.  Draw the iBGP and eBGP sessions between the routers.  How would you configure the routers of AS1 such that : 

 - The traffic to the customer enters AS1 through link R3-R5, and that link R2-R4 is used only in case of failure.  Gives two solutions, one which requires cooperation with AS2 and another that doesn't.  
 - The traffic to the destinations advertised by AS2 exits AS1 through link R2-R4, and link R3-R5 is used as backup. 

 .. figure:: fig/te.png
    :align: center
    :scale: 80

 In each case, show the BGP messages exchanged in the network, and in particular, those received by AS3.  

2. Consider the network  below.

 - Show which BGP messages are exchanged when router `R1` advertises prefix `10.0.0.0/8`.  
 - How many and which routes are known by router `R5` ? Which route does it advertise to `R6`?
 - Assume now that the link between `R1` and `R2` fails.  Show the messages exchanged due to this event.  Which BGP messages are sent to `R6` ?

 .. figure:: fig/path_explo.png
    :align: center
    :scale: 50

    A simple internetwork 

3. The figure below shows a small Internet. The connection between the ASes correspond to a BGP session. Arrows are for customer-provider (CP) peering (the target being the provider, the source is the customer). The number of dollar signs associate to the CP link gives the cost of using the connection. Dashed lines are shared cost peering. We assume congruence between link and BGP session and that each AS runs one and only one router.

 - What will be the path followed by the packets send from 10.0.123.234 to 4.0.0.3?  
 - What will be the path followed by the packets send from 8.8.8.8 to 10.0.123.234?  
 - What will be the path followed by the packets send from 8.8.8.8 to 11.0.123.212?  
 - What will be the path followed by the packets send from 4.3.2.1 to 10.0.123.234?  

 .. figure:: fig/bgp_business_rel.png
    :align: center
    :scale: 50

Layer2 - Layer3
---------------  

1. In the network below, boxed capital letters denote interfaces (counter-clockwise assigned), while dotted numbers (e.g., .1) denote the decimal value of the last byte of their IP address. For instance, interface C on router1 has as IP 200.40.40.1/24. The routing table of the three routers are as follows (directly connected subnets are not shown since their routing is trivial, but you need to take them into account).

 ::

  router1
  Network		Netmask		Interface		Next-Hop
  100.2.2.0		255.255.255.0	C			200.40.40.2
  0.0.0.0		0.0.0.0		D			200.10.10.13
    
  router2
  Network	Netmask		Interface		Next-Hop
  100.1.1.0	255.255.255.0	A			200.40.40.1
  100.4.4.0	255.255.255.0	D			200.30.30.3
  0.0.0.0	0.0.0.0		B			200.20.20.1
   
  router3
  Network	Netmask		Interface		Next-Hop
  100.1.1.0	255.255.255.0	B			200.10.10.1
  100.3.3.0	255.255.255.0	C			200.40.40.2
  0.0.0.0	0.0.0.0		D			200.30.30.2

 - What is the output of the traceroute command from PC4 to PC2 ?
 - What is the output of the traceroute command from PC3 to PC4 ?
 - What is the output of the traceroute command from PC3 to PC1 ?
 - What is the output of the traceroute command from PC3 to PC2 ?
 - What is the output of the traceroute command from PC1 to a non-existent host (e.g., 100.5.5.55) ? 

 .. figure:: fig/l2-l3.png
    :align: center
    :scale: 70

2. For the network depicted in the figure below (IPv4), give all the traffic generated by the sequence of commands executed on A:

 .. figure:: fig/cross_layer1.png
    :align: center
    :scale: 70

 ::

   sleep 3600
   ping -c 6 10.0.0.6
   ping -c 1 192.0.2.129
   sudo arp -da
   traceroute -n 10.0.0.6
   traceroute -n 192.0.2.129


 Assume that all the nodes use static configuration and that no prior traffic has been exchanged. Links are using IEEE802.3. List all the protocols involved in this run and explain how all the fields are constructed to succeed the exchanges.

3. The same question for the network below (IPv6), but assumes that the hosts have no static configuration.  Routers are configured with static routes.

 .. figure:: fig/cross_layer2.png
    :align: center
    :scale: 70















