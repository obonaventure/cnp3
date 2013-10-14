.. Copyright |copy| 2013 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


*****************
Sharing resources
*****************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=4


Exercises
=========

1. Consider the network depicted in the figure below.

 .. graphviz:: graphviz/sharing-rtt.dot



 In this network, compute the minimum round-trip-time between `A` (resp. `B`) and `D`. Perform the computation if the hosts send segments containing 100 bits, 1000 bits and 10,000 bits.

 How is the maximum round-trip-time influenced if the buffers of router `R1` store 10 or 100 packets ?

2. Consider a slightly different variant of the above network. 

 .. graphviz::

   graph foo {
      randkir="LR";
      A [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A</td></TR>
              </TABLE>>];
      B [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>B</td></TR>
              </TABLE>>];
      D [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D</td></TR>
              </TABLE>>];
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
      A--R1 [label="1 Mbps, 0 msec"];
      B--R1 [label="10 Mbps, 10 msec"];
      R1--R2 [label="1 Mbps, 10 msec"];
      R2--D [label="100 Mbps, 0 msec"];
   }

 If hosts `A` and `B` transmit 1000 bits segments and use a sending window of four segments, what is the maximum throughput that they can achieve ?

3. Consider the simple network depicted in the figure below.

 .. graphviz::

   graph foo {
      randkir="LR";
      A [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A</td></TR>
              </TABLE>>];
      B [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>B</td></TR>
              </TABLE>>];
      D [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D</td></TR>
              </TABLE>>];

      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
      A--R1 [label="1 Mbps"];
      B--R1 [label="1 Mbps"];
      R1--R2 [label="1 Mbps, 5 msec"];
      R2--D [label="1 Mbps"];
   }

 In the above network, all links have a 1 Mbps bandwidth and a negligible delay, except the `R1-R2` link. Host `A` uses a sending window of 10 segments. If there is no congestion control, what will be the delay experienced by host `B` if it sends a single segment when the network is in steady state (i.e. host `A` has been transmitting segments during the last seconds).

4. Same question as above, except that router `R1` uses a round-robin scheduler and two queues. The first queue contains all packets sent by host `A` and the second all packets sent by host `B`.


5. When analyzing the reaction of a network using round-robin schedulers, it is sometimes useful to consider that the packets sent by each source are equivalent to a fluid and that each scheduler acts as a tap. Using this analogy, consider the network below. In this network, all the links are 100 Mbps and host `B` is sending packets at 100 Mbps. If A sends at 1, 5, 10, 20, 30, 40, 50, 60, 80 and 100 Mbps, what is the throughput that destination `D` will receive from `A`. Use this data to plot a graph that shows the portion of the traffic sent by host `A` which is received by host `D`. 


  .. graphviz::

      graph foo {
      rankdir="LR";
       A [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A</td></TR>
              </TABLE>>];
       B [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>B</td></TR>
              </TABLE>>];
       D [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D</td></TR>
              </TABLE>>];
       R[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R</td></TR>
              </TABLE>>];
       A--R ;
       B--R;
       R--D;
      }



6. Max-min fairness is the fairness objective for most congestion control schemes that operate in networks. Compute the max-min fair bandwidth allocation in the network below.

  .. graphviz::

      graph foo {
      rankdir="LR";
       A1 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A1</td></TR>
              </TABLE>>];
       A2 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A2</td></TR>
              </TABLE>>];
       B1 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>B1</td></TR>
              </TABLE>>];
       B2 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>B2</td></TR>
              </TABLE>>];
       C1 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>C1</td></TR>
              </TABLE>>];
       C2 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>C2</td></TR>
              </TABLE>>];
       D1 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D1</td></TR>
              </TABLE>>];
       D2 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D2</td></TR>
              </TABLE>>];
       E1 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>E1</td></TR>
              </TABLE>>];
       E2 [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>E2</td></TR>
              </TABLE>>];

       R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
       R3[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R3</td></TR>
              </TABLE>>];
       A1--R1 ;
       B1--R3;
       R1--R2 [label="10 Mbps"];
       C1--R2;
       A2--R2;
       R2--R3 [label="10 Mbps"];
       C2--R3;
       B2--R1;
       D1--R1 [label="1 Mbps"];
       D2--R3 [label="1 Mbps"];
       E1--R1;
       E2--R3;
       }

 In this network, all hosts are attached with a 100 Mbps link, except hosts `D1` and `D2`. Data always flows from the host named `X1` to the host named `X2`.


7. Compute the max-min fair bandwidth allocation in the network below.

 .. figure:: /principles/figures/png/ex-fairness.png
    :align: center


    Simple network topology

8. Consider the simple network depicted in the figure below.

 .. graphviz::

   graph foo {
      randkir="LR";
      A [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A</td></TR>
              </TABLE>>];
      D [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D</td></TR>
              </TABLE>>];

      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
       R2[color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R2</td></TR>
              </TABLE>>];
      A--R1;
      R1--R2 [label="250 kbps"];
      R2--D;
   }

 In this network, hosts are attached via 1 Mbps links while a 250 Kbps link is used between the routers. The propagation delays in the network are negligible. Host `A` sends 1000 bits long segments so that it takes one msec to transmit one segment on the `A-R1` link. Neglecting the transmission delays for the acknowledgements, what is the minimum round-trip time measured on host `A` with such segments ?

9. In the network above, represent by using a table as in the book the transmission of five 1000 bits segment by host `A`. How long does this transmission lasts if there is no congestion control and host `A` uses a sending window of two segments.

10. Same question as above, but now host `A` uses the simple DECBIT congestion control mechanism and a maximum window size of four segments.

11. Consider the network depicted in the figure below.

 .. graphviz::

    graph foo {
      randkir="LR";
      A [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>A</td></TR>
              </TABLE>>];
      B [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>B</td></TR>
              </TABLE>>];
      D [color=white, shape=box label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>D</td></TR>
              </TABLE>>];
      R1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>R1</td></TR>
              </TABLE>>];
      A--R1 [label="1 Mbps, 10 msec"];
      B--R1 [label="1 Mbps, 0 msec"];
      R1--D [label="500 kbps, 0 msec"];
    }

 Hosts `A` and `B` use the simple congestion control scheme described in the book and router `R1` uses the DECBIT mechanism to mark packets as soon as its buffers contain one packet. Hosts `A` and `B` need to send five segments and start exactly at the same time. How long does each hosts needs to wait to receive the acknowledgement for its fifth segment ?

12. CSMA uses acknowledgements but not CSMA/CD. In networks using CSMA/CD how can a host verify that its frame has been received correctly ?

13. In CSMA/CD, would it be possible to increase or decrease the duration of the slottime ? Justify your answer

14. Consider a CSMA/CD network that contains hosts that generate frames at a regular rate. When the transmission rate increases, the amount of collisions increases. For a given network load, measured in bits/sec, would the number of collisions be smaller, equal or larger with short frames than with long frames ?

15. Compare two CSMA sources in a network with some load. When the channel becomes free, the first source is able to transmit its frame within less than one microsecond. The second source is slower and takes half a slotTime to transmit its frame. Compare the collisions that will affect the two sources.

16. What is the capture effect in a network using CSMA/CD ?

17. What is the hidden station problem in a network using CSMA/CA ?


.. include:: /links.rst
