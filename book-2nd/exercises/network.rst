.. Copyright |copy| 2013 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


******************
Building a network
******************
`Multiple choices questions </mcq-network.html>`_


Building forwarding tables
===========================


1. Consider the network shown in the figure below.

.. graphviz::

   graph foo {
    rankdir=LR;
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
      R1--R3 [];
      R2--R1 [];
   }

Assume that the tree nodes are using port-forwarding tables. List in details all the packets that are exchanged when `R3` sends a packet to `R2`. `R2` replies to this packet. Explain all the packets that are transmitted in this network for this exchange. 

2. Consider the network shown in the figure below.

.. graphviz::

   graph foo {
    rankdir=LR;
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
      R1--R3 [];
      R2--R1 [];
      R3--R2;
   }

Assume that the tree nodes are using port-forwarding tables. List in details all the packets that are exchanged when `R3` sends a packet to `R2`. `R2` replies to this packet. Explain all the packets that are transmitted in this network for this exchange. 


3. Consider the network shown in the figure below.

.. graphviz::

   graph foo {
    rankdir=LR;
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
       R4[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R4</td></TR>
              </TABLE>>];
      R1--R3 [];
      R2--R1 [];
      R3--R2;
      R1--R4;
      R3--R4;
   }

Assuming that the network uses source routing, what are the possible paths from `R1` to `R4` ?


4. Consider the network shown in the figure below.

.. graphviz::

   graph foo {
    rankdir=LR;
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
       R4[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R4</td></TR>
              </TABLE>>];
       R5[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R5</td></TR>
              </TABLE>>];
      R1--R3 [];
      R2--R1 [];
      R3--R2;
      R2--R4;
      R2--R5;
      R4--R5;
   }

The network operator uses would like to have the following paths in this network :

 - `R3->R2->R4->R5` and `R1->R2->R5` 

Is it possible to achieve these paths and if so what are the required forwarding tables ?


5. Consider the network shown in the figure below.

.. graphviz::

   graph foo {
    rankdir=LR;
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
       R4[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R4</td></TR>
              </TABLE>>];
       R5[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R5</td></TR>
              </TABLE>>];
      R1--R3 [];
      R2--R1 [];
      R3--R2;
      R2--R4;
      R2--R5;
      R4--R5;
      R3--R4;
   }

The network operator would like to use the following paths :
 
 - `R1->R2->R4` and `R3->R2->R5->R4`

Are these paths possible with link-state or distance vector routing ? If yes, how do configure the link weights. If no, explain your answer.

Same question with label switching.

6. Consider the network shown in the figure below.

.. graphviz::

   graph foo {
    rankdir=LR;
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
       R4[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R4</td></TR>
              </TABLE>>];
       R5[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R5</td></TR>
              </TABLE>>];
      R1--R3 [];
      R2--R1 [];
      R3--R2;
      R1--R5;
      R2--R5;
      R4--R5;
      R2--R4;
   }

The network operator would like to use the following paths :
 
 - `R1->R5->R4` and `R3->R2->R4`

Are these paths possible with link-state or distance vector routing ? If yes, how do configure the link weights. If no, explain your answer.




Routing protocols
=================

1. Routing protocols used in data networks only use positive link weights. What would happen with a distance vector routing protocol in the network below that contains a negative link weight ?

 .. figure:: ../../book/network/svg/ex-simple.png
    :scale: 50 

    A simple network

2. When a network specialist designs a network, one of the problems that he needs to solve is to set the metrics the links in his network. In the USA, the Abilene network interconnects most of the research labs and universities. The figure below shows the topology [#fabilene]_ of this network in 2009.

 .. figure:: /principles/figures/abilene-web-map.png
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

.. figure:: ../../book/network/svg/ex-five-routers.png
   :align: center 
   :scale: 50 

   Simple five nodes network


4. In the five nodes network shown above, can you configure the link weights so that the packets sent by router `E` (resp. `F`) follow the `E->B->A` path (resp. `F->D->B->A`) ?

5. In the above questions, you have worked on the stable state of the routing tables computed by routing protocols. Let us now consider the transient problems that mainly happen when the network topology changes [#ffailures]_. For this, consider the network topology shown in the figure below and assume that all routers use a distance vector protocol that uses split horizon.

 .. figure:: ../../book/network/svg/ex-five-routers-redundant.png
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

 .. figure:: ../../book/network/svg/ex-five-routers-weigth4.png
    :align: center
    :scale: 30
   
    A simple network 

 On recent routers, a lookup in the forwarding table for a destination address returns a set of outgoing interfaces. How would you design an algorithm that selects the outgoing interface used for each packet, knowing that to avoid reordering, all segments of a given TCP connection should follow the same path ? 

7. Consider again the network shown above. After some time, link state routing converges and all routers compute the following routing tables :

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




.. include:: /links.rst
