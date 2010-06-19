Exercises
#########

The network layer contains two types of protocols :

 - the *data plane* protocols such as IP that define the format of the packets that are exchanged between routers and how they must be forwarded
 - the *routing protocols*, that are part of the *control plane*. Routers exchange routing messages in order to build their routing tables and forwarding tables to forward the packets in the data plane



1. Routing protocols used in IP networks only use positive link weights. What would happen with a distance vector routing protocol in the network below that contains a negative link weight ?

.. figure:: exercises/fig/routing-fig-001-c.png 
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

 * Is it possible to configure the link metrics so that the packets sent by the router located in `Los Angeles` to the routers located in respectively `New York` and `Washington` do not follow the same path ? 

 * Is it possible to configure the link weights so that the packets sent by the router located in `Los Angeles` to router located in `New York` follow one path while the packets sent by the router located in `New York` to the router located in  `Los Angeles` follow a completely different path ?

 * Assume that the routers located in `Denver` and `Kansas City` need to exchange lots of packets. Can you configure the link metrics such that the link between these two routers does not carry any packet sent by another router in the network ?

3. In the five nodes network shown below, can you configure the link metrics so that the packets sent by router `E` to router `A` use link `B->A` while the packets sent by router `B` use links `B->D` and `D->A`?

.. figure:: exercises/fig/routing-fig-003-c.png 
   :align: center 
   :scale: 50 

   Simple five nodes network


4. In the five nodes network shown above, can you configure the link weights so that the packets sent by router `E` (resp. `F`) follow the `E->B->A` path (resp. `F->D->B->A`) ?

5. In the above questions, you have worked on the stable state of the routing tables computed by routing protocols. Let us now consider the transient problems that main happen when the network topology changes [#ffailures]_. For this, consider the network topology shown in the figure below and assume that all routers use a distance vector protocol that uses split horizon.

.. figure:: exercises/fig/routing-fig-004-c.png
   :align: center
   :scale: 50

   Simple network 


If you compute the routing tables of all routers in this network, you would obtain a table such as the table below :


 ===========  ========  ========  =======  =======  =======
 Destination   Routes   Routes    Routes   Routes   Routes  
 	       on A     on B      on C     on D     on E
 -----------  --------  --------  -------  -------  -------
 A             0        1 via A   2 via B  3 via C  4 via D
 B 	       1 via B  0     	  1 via B  2 via C  3 via D
 C             2 via B  1 via C	  0        1 via C  2 via D
 D             3 via B  2 via C	  1 via D  0 	    1 via D
 E             4 via B  3 via C	  2 via D  1 via E  0
 ===========  ========  ========  =======  =======  =======

 Distance vector protocols can operate in two different modes : `periodic updates` and `triggered updates`. `Periodic updates` is the default mode for a distance vector protocol. For example, each router could advertise its distance vector every thirty seconds. With the `triggered updates` a router sends its distance vector when its routing table changes (and periodically when there are no changes).  

 * Consider a distance vector protocol using split horizon and `periodic updates`. Assume that the link `B-C` fails. `B` and `C` update their local routing table but they will only advertise it at the end of their period. Select one ordering for the  `periodic updates` and every time a router sends its distance vector, indicate the vector sent to each neighbor and update the table above. How many periods are required to allow the network to converge to a stable state ?

 * Consider the same distance vector protocol, but now with `triggered updates`. When link `B-C` fails, assume that `B` updates its routing table immediately and sends its distance vector to `A` and `D`. Assume that both `A` and `D` process the received distance vector and that `A` sends its own distance vector, ... Indicate all the distance vectors that are exchanged and update the table above each time a distance vector is sent by a router (and received by other routers) until all routers have learned a new route to each destination. How many distance vector messages must be exchanged until the network converges to a stable state ?

6. Consider the network shown below. In this network, the metric of each link is set to `1` except link `A-B` whose metric is set to `4` in both directions. In this network, there are two paths with the same cost between `D` and `C`. Old routers would randomly select one of these equal cost paths and install it in their forwarding table. Recent routers are able to use up to `N` equal cost paths towards the same destination. 

 .. figure:: exercises/fig/BGP-figs-010-c.png
    :align: center
    :scale: 70
   
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


10. Consider the network shown in the figure below and explain the path that will be followed by the packets to reach `194.100.10.0/23`

 .. figure:: exercises/fig/BGP-figs-001-c.png
    :align: center
    :scale: 50
   
    A stub connected to one provider

11. Consider, now, as shown in the figure below that the stub AS is now also connected to provider `AS789`. Via which provider will the packets destined to `194.100.10.0/23` will be received by `AS4567` ? Should `AS123` change its configuration ? 

 .. figure:: exercises/fig/BGP-figs-002-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

12. Consider that stub shown in the figure below decides to advertise two `/24` prefixes instead of its allocated `/23` prefix. 

  #. Via which provider does `AS4567` receive the packets destined to `194.100.11.99` and `194.100.10.1` ? 
  #. How is the reachabilty of these addresses affected when link `R1-R3` fails ?
  #. Propose a configuration on `R1` that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS4567` if one of `AS4567`'s interdomain links fails ?

 .. figure:: exercises/fig/BGP-figs-003-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

13. Researchers and network operators collect and expose lots of BGP data. For this, they establish eBGP sessions between `data collection` routers and production routers located operationnal networks. Several `data collection` routers are available, the most popular ones are :

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



14. Consider the network shown in the figure below and assume that R1` advertises a single prefix. R1` receives a lot of packets from `R9`. Without any help from `R2`, `R9` or `R4`, how could `R1` configure its BGP advertisement such that it receives the packets from `R9` via `R3` ? What happens when a link fails ?

 .. figure:: exercises/fig/BGP-figs-004-c.png
    :align: center
    :scale: 50
   
    A simple internetwork 



15. Consider the network  below.

 .. figure:: exercises/fig/path_explo.png
    :align: center
    :scale: 50
   
    A simple internetwork 

 #. Show which BGP messages are exchanged when router `R1` advertises prefix `10.0.0.0/8`.  
 #. How many and which routes are known by router `R5` ? Which route does it advertise to `R6`?
 #. Assume now that the link between `R1` and `R2` fails.  Show the messages exchanged due to this event.  Which BGP messages are sent to `R6` ?


16. Consider the network shown in the figure below where `R1` advertises a single prefix. In this network, the link between `R1` and `R2` is considered as a backup link. It should only be used only when the primary link (`R1-R4`) fails. This can be implemented on `R2` by setting a low `local-pref` to the routes received on link `R2-R1`

  #. In this network, what are the paths used by all routers to reach `R1` ?
  #. Assume now that the link `R1-R4` fails. Which BGP messages are exchanged and what are now the paths used to reach `R1` ?
  #. Link `R1-R4` comes back. Which BGP messages are exchanged and what do the paths used to reach `R1` become ?

 .. figure:: exercises/fig/BGP-figs-009-c.png
    :align: center
    :scale: 50
   
    A simple internetwork with a backup link 


17. On February 22, 2008, the Pakistan Telecom Authority issued an `order <http://www.teeth.com.pk/blog/wp-content/uploads/2008/02/22-02-08_pta_blocking_of_websities.pdf>`_ to Pakistan ISPs to block access to three IP addresses belonging to `youtube <http://www.youtube.com>`_: `208.65.153.238`, `208.65.153.253`, `208.65.153.251`. One operator noted that these addresses were belonging to the same `/24` prefix. Read http://www.ripe.net/news/study-youtube-hijacking.html to understand what happened really.

 #. What should have done youtube_ to avoid this problem ?
 #. What kind of solutions would you propose to improve the security of interdomain routing ?


.. rubric:: Footnotes

.. [#fabilene] This figure was downloaded from the Abilene observatory http://www.internet2.edu/observatory/archive/data-views.html. This observatory contains a detailed description of the Abilene network including detailed network statistics and all the configuration of the equipment used in the network. 

.. [#ffailures] The main events that can affect the topology of a network are :
 - the failure of a link. Measurements performed in IP networks have shown that such failures happen frequently and usually for relatively short periods of time
 - the addition of one link in the network. This may be because a new link has been provisioned or more frequently because the link failed some time ago and is now back
 - the failure/crash of a router followed by its reboot. 
 - a change in the metric of a link by reconfiguring the routers attached to the link
 See http://totem.info.ucl.ac.be/lisis_tool/lisis-example/ for an analysis of the failures inside the Abilene network in June 2005 or http://citeseer.ist.psu.edu/old/markopoulou04characterization.html for an analysis of the failures affecting a larger ISP network

