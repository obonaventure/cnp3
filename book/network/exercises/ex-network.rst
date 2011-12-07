.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

Exercises
#########


Principles
==========

.. The network layer contains two types of protocols :

.. - the *data plane* protocols such as IP that define the format of the packets that are exchanged between routers and how they must be forwarded
.. - the *routing protocols*, that are part of the *control plane*. Routers exchange routing messages in order to build their routing tables and forwarding tables to forward the packets in the data plane

1. Routing protocols used in data networks only use positive link weights. What would happen with a distance vector routing protocol in the network below that contains a negative link weight ?

 .. figure:: svg/ex-simple.png
    :align: center 
    :scale: 50 

    Simple network

2. When a network specialist designs a network, one of the problems that he needs to solve is to set the metrics the links in his network. In the USA, the Abilene network interconnects most of the research labs and universities. The figure below shows the topology [#fabilene]_ of this network in 2009.

 .. figure:: exercises/fig/abilene-web-map.png
    :align: center
    :scale: 50 

    The Abilene network 
 
 In this network, assume that all the link weights are set to 1. What is the paths followed by a packet sent by the router located in `Los Angeles` to reach :

   * the router located in `New York` 
   * the router located in `Washington` ?

 Is it possible to configure the link metrics so that the packets sent by the router located in `Los Angeles` to the routers located in respectively `New York` and `Washington` do not follow the same path ? 

 Is it possible to configure the link weights so that the packets sent by the router located in `Los Angeles` to router located in `New York` follow one path while the packets sent by the router located in `New York` to the router located in  `Los Angeles` follow a completely different path ?

 Assume that the routers located in `Denver` and `Kansas City` need to exchange lots of packets. Can you configure the link metrics such that the link between these two routers does not carry any packet sent by another router in the network ?

3. In the five nodes network shown below, can you configure the link metrics so that the packets sent by router `E` to router `A` use link `B->A` while the packets sent by router `B` use links `B->D` and `D->A`?

.. figure:: svg/ex-five-routers.png
   :align: center 
   :scale: 50 

   Simple five nodes network


4. In the five nodes network shown above, can you configure the link weights so that the packets sent by router `E` (resp. `F`) follow the `E->B->A` path (resp. `F->D->B->A`) ?

5. In the above questions, you have worked on the stable state of the routing tables computed by routing protocols. Let us now consider the transient problems that main happen when the network topology changes [#ffailures]_. For this, consider the network topology shown in the figure below and assume that all routers use a distance vector protocol that uses split horizon.

 .. figure:: svg/ex-five-routers-redundant.png
    :align: center
    :scale: 50

    Simple network with redundant links


 If you compute the routing tables of all routers in this network, you would obtain a table such as the table below :


  ===========  ========  ========  =======  =======  =======
  Destination  Routes    Routes    Routes   Routes   Routes  
  	       on A      on B      on C     on D     on E
  -----------  --------  --------  -------  -------  -------
  A            0         1 via A   2 via B  3 via C  4 via D
  B 	       1 via B   0     	   1 via B  2 via C  3 via D
  C            2 via B   1 via C   0        1 via C  2 via D
  D            3 via B   2 via C   1 via D  0 	     1 via D
  E            4 via B   3 via C   2 via D  1 via E  0
  ===========  ========  ========  =======  =======  =======

 Distance vector protocols can operate in two different modes : `periodic updates` and `triggered updates`. `Periodic updates` is the default mode for a distance vector protocol. For example, each router could advertise its distance vector every thirty seconds. With the `triggered updates` a router sends its distance vector when its routing table changes (and periodically when there are no changes).  

 * Consider a distance vector protocol using split horizon and `periodic updates`. Assume that the link `B-C` fails. `B` and `C` update their local routing table but they will only advertise it at the end of their period. Select one ordering for the  `periodic updates` and every time a router sends its distance vector, indicate the vector sent to each neighbor and update the table above. How many periods are required to allow the network to converge to a stable state ?

 * Consider the same distance vector protocol, but now with `triggered updates`. When link `B-C` fails, assume that `B` updates its routing table immediately and sends its distance vector to `A` and `D`. Assume that both `A` and `D` process the received distance vector and that `A` sends its own distance vector, ... Indicate all the distance vectors that are exchanged and update the table above each time a distance vector is sent by a router (and received by other routers) until all routers have learned a new route to each destination. How many distance vector messages must be exchanged until the network converges to a stable state ?

6. Consider the network shown below. In this network, the metric of each link is set to `1` except link `A-B` whose metric is set to `4` in both directions. In this network, there are two paths with the same cost between `D` and `C`. Old routers would randomly select one of these equal cost paths and install it in their forwarding table. Recent routers are able to use up to `N` equal cost paths towards the same destination. 

 .. figure:: svg/ex-five-routers-weigth4.png
    :align: center
    :scale: 30
   
    A simple network running OSPF

 On recent routers, a lookup in the forwarding table for a destination address returns a set of outgoing interfaces. How would you design an algorithm that selects the outgoing interface used for each packet, knowing that to avoid reordering, all segments of a given TCP connection should follow the same path ? 

7. Consider again the network shown above. After some time, OSPF converges and all routers compute the following routing tables :

 ===========  ========  =========  =========  =========  =========
 Destination   Routes   Routes     Routes     Routes   	 Routes  
 	       on A     on B       on C       on D     	 on E
 -----------  --------  ---------  ---------  ---------  ---------
 A             0        2 via C    1 via A    3 via B,E  2 via C
 B 	       2 via C  0     	   1 via B    1 via B    2 via D,C
 C             1 via C  1 via C	   0          2 via B,E  1 via C
 D             3 via C  1 via D	   2 via B,E  0 	 1 via D
 E             2 via C  2 via C,D  1 via E    1 via E    0
 ===========  ========  =========  =========  =========  =========

 An important difference between OSPF and RIP is that OSPF routers flood link state packets that allow the other routers to recompute their own routing tables while RIP routers exchange distance vectors. Consider that link `B-C` fails and that router `B` is the first to detect the failure. At this point, `B` cannot reach anymore `A`, `C` and 50% of its paths towards `E` have failed. `C` cannot reach `B` anymore and half of its paths towards `D` have failed.

 Router `B` will flood its updated link state packet through the entire network and all routers will recompute their forwarding table. Upon reception of a link state packet, routers usually first flood the received link-state packet and then recompute their forwarding table. Assume that `B` is the first to recompute its forwarding table, followed by `D`, `A`, `C` and finally `E`

8. After each update of a forwarding table, verify which pairs of routers are able to exchange packets. Provide your answer using a table similar to the one shown above.

9. Can you find an ordering of the updates of the forwarding tables that avoids all transient problems ?

10. Consider the simple network depicted in the figure below. On each subnet, each router has one IP address whose host identifier is the numerical id of the router (.e.g router `R1` uses addresses `10.1.0.1` and `10.2.0.1`). Assume that all the hosts and routers have been booted and no packet has been sent. Explain in details all the packets and frames that are exchanged when :

 a.  `10.1.0.10` performs a :manpage:`ping(8)` towards `10.3.0.3` 
 b.  `10.1.0.10` performs a :manpage:`traceroute(8)` Towards `10.3.0.3`. Assume that :manpage:`traceroute(8)` is used with the `-n` option so that no reverse DNS lookup is performed for each IP address and that all devices have been rebooted after the first question.

 .. figure:: exercises/png/ip-figs-001-c.png
    :align: center
    :scale: 70
   
    A small network using IPv4

11. Consider the simple network depicted in the figure below. On each subnet, each router has one IPv6 address whose host identifier is the numerical id of the router. Assume that all the hosts and routers have been booted and no packet has been sent. Explain in details all the packets and frames that are exchanged when :

 a.  `2001:db8:cafe::abcd` performs a :manpage:`ping6(8)` towards `2001:db8:dead::3` 
 b.  `2001:db8:cafe::abcd` performs a :manpage:`traceroute6(8)` towards `2001:db8:dead::3`. Assume that :manpage:`traceroute(8)` is used with the `-n` option so that no reverse DNS lookup is performed for each IPv6 address and that all devices have been rebooted after the first question.

 .. figure:: exercises/png/ip-figs-002-c.png
    :align: center
    :scale: 70
   
    A small network using IPv6

12. Many TCP/IP implementations today send an ARP request for their own IP address before sending their first IP packet using this address. Can you explain why this is useful in practice ?

13. Consider now the transmission of IPv4 packets. One security issue with IPv4 is the Address Resolution Protocol (ARP). Can you explain what ARP spoofing or ARP poisoning is and show how host `A` in the network below could intercept all the IP packets sent by host `B` via the default router ? Can router `R` do something to improve the security of ARP ?

 .. figure:: exercises/png/ip-figs-008-c.png
    :align: center
    :scale: 70
   
    A small Ethernet network

14. Consider the network shown in the figure below that is using only static routes as shown in the figure. Assuming that there are only point-to-point links, show all the packets that are exchanged in the network when `S` (`1.0.0.1/8`) performs a :manpage:`traceroute(8)` towards `2.0.0.2`. `S` (resp. `D`) uses `A` (resp. `E`) as its default router. Provide your answer in a table such as the one shown below where each line corresponds to one IP packet.

 ===========  ========   =========  =========== 
 Link	      IP	 IP	    Explanation
 	      source	 dest.	   
 -----------  --------   ---------  -----------  
 ...	      ...	 ...	    ...	      
 ===========  ========   =========  =========== 

  .. figure:: exercises/png/ip-figs-003-c.png
    :align: center
    :scale: 70
   
    A small network

15. IPv4 addresses are scarce and network operators often need to minimise the number of IPv4 addresses that they use when deploying a network.  You are responsible for the entreprise network shown below and must use IP prefix `172.16.12.128/25` for all IP addresses (hosts and routers) in this network. How to you assign IP prefixes to the various subnets to maximise the number of addresses that are available for hosts on the left and right networks. As a practical constraint, note that inside each subnet, the IPv4 addresses whose host identifier bits are all set to `0` or all set to `1` cannot be used. In practice, the address where all host identifiers bits are set to `0` is used to represent the subnetwork itself while the address where all host identifiers bits are set to `1` is reserved for backward compatibility reason for the subnet broadcast address. This implies that on a point-to-point link you can only assign a `/30` prefix and not a `/31` prefix although there are usually only two IPv4 addresses in use on such a link [#frfc3021]_.

 .. figure:: exercises/png/ip-figs-004-c.png
    :align: center
    :scale: 70
   
    A simple enterprise network

16. Hosts are sometimes misconfigured on a subnetwork. Consider the network shown below where all hosts have been manually configured. Discuss which host is able to send a packet to which host ?

 .. figure:: exercises/png/ip-figs-005-c.png
    :align: center
    :scale: 70
   
    Misconfigured hosts on a subnetwork 

17. In the entreprise network shown below, there are many servers on the subnetwork at the top and many servers on the subnetwork shown at the bottom. The links `R0-R2` and `R1-R3` must be used together to sustain the load generated by these servers. How can you configure the static routing tables on the routers and the servers so that 50% of the traffic is sent via each point-to-point link ?

 .. figure:: exercises/png/ip-figs-006-c.png
    :align: center
    :scale: 70
   
    An entreprise network with many servers 

18. Salesman often explain that a Network Address Translator is equivalent to a firewall because it protects the hosts that reside behind the NAT. What is your technical opinion about this ?

19. There are two main types of Network Address Translators (NAT). The simplest NATs use a single public IP address and can serve many hosts using private addresses. Entreprise-grade and carrier-grade NATs often use an IPv4 prefix and can serve an entire enterprise using private addresses. Compare these two types of NATs.

20. A student has installed a NAT router at home and would like to setup a web server on his laptop. What does he need to do to ensure that his web server is reachable from the Internet ?

21. NATs translate port numbers and IP addresses. Sometimes, IPv4 packets are fragmented. Discuss how should a NAT process fragments of IPv4 packets ? Assume that only TCP is used through the NAT. 

22. Same question as above for a firewall.

23. Assume that you use a laptop with a private IPv4 address behind a NAT to surf the web. To reduce cost, the implementor of your NAT chose to discard all ICMP messages that your laptop sends and all ICMP that are received from the Internet. What could be the consequences of this reduced NAT ?


24. Consider the network shown in the figure below and explain the path that will be followed by the packets to reach `194.100.10.0/23`

 .. figure:: svg/ex-bgp-stub-one-provider.png
    :align: center
    :scale: 100
   
    A stub connected to one provider

25. Consider, now, as shown in the figure below that the stub AS is now also connected to provider `AS789`. Via which provider will the packets destined to `194.100.10.0/23` will be received by `AS4567` ? Should `AS123` change its configuration ? 

 .. figure:: svg/ex-bgp-stub-two-providers.png
    :align: center
    :scale: 100
   
    A stub connected to two providers

16. Consider that stub shown in the figure below decides to advertise two `/24` prefixes instead of its allocated `/23` prefix. 

  #. Via which provider does `AS4567` receive the packets destined to `194.100.11.99` and `194.100.10.1` ? 
  #. How is the reachability of these addresses affected when link `R1-R3` fails ?
  #. Propose a configuration on `R1` that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS4567` if one of `AS4567`'s interdomain links fails ?

  .. figure:: svg/ex-bgp-stub-two-providers-specific.png
     :align: center
     :scale: 100
   
     A stub connected to two providers


27. Consider the network shown in the figure below. In this network, each AS contains a single BGP router. Assume that `R1` advertises a single prefix. `R1` receives a lot of packets from `R9`. Without any help from `R2`, `R9` or `R4`, how could `R1` configure its BGP advertisement such that it receives the packets from `R9` via `R3` ? What happens when a link fails ?

 .. figure:: svg/ex-bgp-internetwork.png
    :align: center
    :scale: 50
   
    A simple internetwork 

28. Consider the network show in the figure below.

 .. figure:: svg/ex-bgp-path-explo.png
    :align: center
    :scale: 50
   
    A simple internetwork 

 #. Show which BGP messages are exchanged when router `R1` advertises prefix `10.0.0.0/8`.  
 #. How many and which routes are known by router `R5` ? Which route does it advertise to `R6`?
 #. Assume now that the link between `R1` and `R2` fails.  Show the messages exchanged due to this event.  Which BGP messages are sent to `R6` ?

29. Consider the network shown in the figure below where `R1` advertises a single prefix. In this network, the link between `R1` and `R2` is considered as a backup link. It should only be used only when the primary link (`R1-R4`) fails. This can be implemented on `R2` by setting a low `local-pref` to the routes received on link `R2-R1`

  #. In this network, what are the paths used by all routers to reach `R1` ?
  #. Assume now that the link `R1-R4` fails. Which BGP messages are exchanged and what are now the paths used to reach `R1` ?
  #. Link `R1-R4` comes back. Which BGP messages are exchanged and what do the paths used to reach `R1` become ?

 .. figure:: svg/ex-bgp-backup.png
    :align: center
    :scale: 40
   
    A simple internetwork with a backup link 

30. On February 22, 2008, the Pakistan Telecom Authority issued an `order <http://www.teeth.com.pk/blog/wp-content/uploads/2008/02/22-02-08_pta_blocking_of_websities.pdf>`_ to Pakistan ISPs to block access to three IP addresses belonging to `youtube <http://www.youtube.com>`_: `208.65.153.238`, `208.65.153.253`, `208.65.153.251`. One operator noted that these addresses were belonging to the same `/24` prefix. Read http://www.ripe.net/news/study-youtube-hijacking.html to understand what happened really.

 #. What should have done youtube_ to avoid this problem ?
 #. What kind of solutions would you propose to improve the security of interdomain routing ?

31. There are currently 13 IPv4 addresses that are associated to the root servers of the Domain Name System. However, http://www.root-servers.org/ indicates that there are more than 100 different physical servers that support. This is a large anycast service. How would you configure BGP routers to provide such anycast service ?

32. Consider the network shown in the figure below. In this network, `R0` advertises prefix `p` and all link metrics are set to `1`

 - Draw the iBGP and eBGP sessions
 - Assume that session `R0-R8` is down when `R0` advertises `p` over `R0-R7`. What are the BGP messages exchanged and the routes chosen by each router in the network ?
 - Session `R0-R8` is established and `R0` advertises prefix `p` over this session as well
 - Do the routes selected by each router change if the `MED` attribute is used on the `R7-R6` and `R3-R10` sessions, but not on the `R4-R9` and `R6-R8` sessions ?
 - Is it possible to configure the routers in the `R1 - R6` network such that `R4` reaches prefix `p` via `R6-R8` while `R2`uses the `R3-R10` link ?

 .. figure:: svg/revision-figs-003-c.png
    :align: center
    :scale: 30 

    A simple Internet

33. The BGP `MED` attribute is often set at the IGP cost to reach the BGP nexthop of the advertised prefix. However, routers can also be configured to always use the same `MED` values for all routes advertised over a given session. How would you use it in the figure above so that link `R10-R3` is the primary link while `R7-R6` is a backup link ? Is there an advantage or drawback of using the `MED` attribute for this application compared to `local-pref` ?

34. In the figure above, assume that the managers of `R8` and `R9` would like to use the `R8-R6` link as a backup link, but the managers of `R4` and `R6` do not agree to use the BGP `MED` attribute nor to use a different `local-pref` for the routes learned from `R8` and `R9`. Is there an alternative to `MED` ?

.. rubric:: Footnotes

.. [#fabilene] This figure was downloaded from the Abilene observatory http://www.internet2.edu/observatory/archive/data-views.html. This observatory contains a detailed description of the Abilene network including detailed network statistics and all the configuration of the equipment used in the network. 

.. [#ffailures] The main events that can affect the topology of a network are :
 - the failure of a link. Measurements performed in IP networks have shown that such failures happen frequently and usually for relatively short periods of time
 - the addition of one link in the network. This may be because a new link has been provisioned or more frequently because the link failed some time ago and is now back
 - the failure/crash of a router followed by its reboot. 
 - a change in the metric of a link by reconfiguring the routers attached to the link
 See http://totem.info.ucl.ac.be/lisis_tool/lisis-example/ for an analysis of the failures inside the Abilene network in June 2005 or http://citeseer.ist.psu.edu/old/markopoulou04characterization.html for an analysis of the failures affecting a larger ISP network
.. [#frfc3021] See :rfc:`3021` for a discussion of the utilisation of `/30` IPv4 prefixes on point-to-point links

.. include:: ../../book/links.rst






