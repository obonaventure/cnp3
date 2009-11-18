OSPF and BGP
============


In this set of exercices, you will explore in more details the operation of a link-state routing protocol such as OSPF and the operation of BGP.

The deadline for this set of exercises is Tuesday November 24th, 13.00.

Link state routing
------------------

1 Consider the network shown below. In this network, the metric of each link is set to `1` except link `A-B` whose metric is set to `4` in both directions. In this network, there are two paths with the same cost between `D` and `C`. Old routers would randomly select one of these equal cost paths and install it in their forwarding table. Recent routers are able to use up to `N` equal cost paths towards the same destination. 

 .. figure:: fig/BGP-figs-010-c.png
    :align: center
    :scale: 70
   
    A simple network running OSPF

 #. On recent routers, a lookup in the forwarding table for a destination addresses returns thus a set of outgoing interfaces. How would you design an algorithm that selects the outgoing interface used for each packet, knowing that to avoid reordering, all segments from the same TCP connection should ideally follow the same path ? 

2 Consider again the topology shown above. After some time, OSPF converges and all routers compute the following routing tables :

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

An important difference between OSPF and RIP is that OSPF routers flood link state packets that allow the other routers to recompute their own routing tables while RIP routers exchange distance vectors. Consider that link `B-C` fails and that router `B` is the first to detect the failure. At this point, `B` cannot reach anymore `A`, `C` and half of its paths towards `E` have failed. `C` cannot reach `B` anymore and half of its paths towards `D` have failed.

Router `B` will flood its updated link state packet through the entire network and all routers will recompute their forwarding table. Upon reception of a link state packet, routers usually first flood the received link-state packet and then recompute their forwarding table. Assume that `B` is the first to recompute its forwarding table, followed by `D`, `A`, `C` and finally `E`

#. After each update of a forwarding table, verify which pairs of routers are able to exchange packets. Provide your answer using a table similar to the one shown above.
#. Can you find an ordering of the updates of the forwarding tables that avoids all transient problems ?

BGP
---

1 Consider the network shown in the figure below and explain the path that will be followed by the packets to reach `194.100.10.0/23`

 .. figure:: fig/BGP-figs-001-c.png
    :align: center
    :scale: 50
   
    A stub connected to one provider

2 Consider, now, as shown in the figure below that the stub AS is now connected also to provider `AS789`. Via which provider will the packets destined to `194.100.10.0/23` will be received by `AS4567` ? Propose a modification to the BGP configuration of `AS123` ?

 .. figure:: fig/BGP-figs-002-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

3 Consider that stub shown in the figure below decides to advertise two `/24` prefixes instead of its allocated `/23` prefix. 

  #. Via which provider does `AS4567` receive the packets destined to `194.100.11.99` and `194.100.10.1` ? 
  #. What happens when link `R1-R3` fails ?
  #. What are the consequences these advertisements on the size of the BGP routing maintained by routers in the global Internet ?
  #. Propose a configuration on `R1` that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS4567` if one of `AS4567`'s interdomain links fails ?

 .. figure:: fig/BGP-figs-003-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

4 Researchers and network operators collect and expose lots of BGP data. For this, they establish eBGP sessions between `data collection` routers and production routers located operationnal networks. Several `data collection` routers are available, the most popular ones are :

 - http://www.routeviews.org
 - http://www.ripe.net/ris

For this exercice, you will use one of the `routeviews` BGP routers. You can access this router by using telnet. Once logged on the router, you can use the router's command line interface to analyse its BGP routing table ::

 telnet route-views.routeviews.org
 Trying 128.223.51.103...
 Connected to route-views.routeviews.org.
 Escape character is '^]'.
 C
 **********************************************************************

                    Oregon Exchange BGP Route Viewer
          route-views.oregon-ix.net / route-views.routeviews.org

 route views data is archived on http://archive.routeviews.org

 This hardware is part of a grant from Cisco Systems.
 Please contact help@routeviews.org if you have questions or
 comments about this service, its use, or if you might be able to
 contribute your view. 

 This router has views of the full routing tables from several ASes.
 The list of ASes is documented under "Current Participants" on
 http://www.routeviews.org/.

                          **************

 route-views.routeviews.org is now using AAA for logins.  Login with
 username "rviews".  See http://routeviews.org/aaa.html

 **********************************************************************

 
 User Access Verification

 Username: rviews
 route-views.oregon-ix.net>

This router has eBGP sessions with routers from several ISPs. See http://www.routeviews.org/peers/route-views.oregon-ix.net.txt for an up-to-date list of all eBGP sessions maintained by this router.

Among all the commands supported by this router, the `show ip bgp` command is very useful. This command takes an IPv4 prefix as parameter and allows you to retrieve all the routes that this routers has received in its Adj-RIB-In for the specified prefix.

 #. Use `show ip bgp 130.104.0.0/16` to find the best path used by this router to reach UCLouvain
 #. Knowing that `130.104.0.0/16` is announced by belnet (AS2611), what are, according to this BGP routing tables, the ASes that peer with belnet
 #. Do the same analysis for one of the IPv4 prefixes assigned to Skynet (AS5432) : `62.4.128.0/17`. The output of the `show ip bgp 62.4.128.0/17` reveals something strange as it seems that one of the paths towards this prefix passes twice via `AS5432`. Can you explain this ? ::


   2905 702 1239 5432 5432
     196.7.106.245 from 196.7.106.245 (196.7.106.245)
       Origin IGP, metric 0, localpref 100, valid, external



5 Consider the network shown in the figure below and assume that R1` advertises a single prefix. R1` receives a lot of packets from `R9`. Without any help from `R2`, `R9` or `R4`, how could `R1` configure its BGP advertisement such that it receives the packets from `R9` via `R3` ? What happens when a link fails ?

 .. figure:: fig/BGP-figs-004-c.png
    :align: center
    :scale: 50
   
    A simple internetwork 



6 Consider the network topology shown below.

 .. figure:: path_explo.png
    :align: center
    :scale: 50
   
    A simple internetwork 

 #. Show which BGP messages are exchanged when router `R1` advertises prefix `10.0.0.0/8`.  
 #. How many and which routes are known by router `R5` ? Which route does it advertise to `R6`?
 #. Assume now that the link between `R1` and `R2` fails.  Show the messages exchanged due to this event.  Which BGP messages are sent to `R6` ?


7 Consider the network shown in the figure below where `R1` advertises a single prefix. In this network, the link between `R1` and `R2` is considered as a backup link. It should only be used only when the primary link (`R1-R4`) fails. This can be implemented on `R2` by setting a low `local-pref` to the routes received on link `R2-R1`

  #. In this topology, what are the paths used by all routers to reach `R1` ?
  #. Assume now that the link `R1-R4` fails. Which BGP messages are exchanged and what are now the paths used to reach `R1` ?
  #. Link `R1-R4` comes back. Which BGP messages are exchanged and what are now the paths used to reach `R1` ?

 .. figure:: fig/BGP-figs-009-c.png
    :align: center
    :scale: 50
   
    A simple topology with a backup link 


8 On February 22, 2008, the Pakistan Telecom Authority issued an `order <http://www.teeth.com.pk/blog/wp-content/uploads/2008/02/22-02-08_pta_blocking_of_websities.pdf>`_ to Pakistan ISPs to block access to three IP addresses belonging to `youtube <http://www.youtube.com>`_: `208.65.153.238`, `208.65.153.253`, `208.65.153.251`. One operator noted that these addresses were belonging to the same `/24` prefix. Read http://www.ripe.net/news/study-youtube-hijacking.html to understand what happened really.

 #. What should have done youtube_ to avoid this problem ?
 #. What kind of solutions would you propose to improve the security of interdomain routing ?



.. include:: ../../book/links.rst



