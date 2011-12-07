.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

Exercises
#########

1. The host H0 pings its peer H1 in the network depicted in the figure below. Explain precisely what happened in the network since it has started.

.. figure:: svg/ex-switches_w_simple_STP.png
   :align: center
   :scale: 30

2. Consider the switched network shown in the figure below. What is the spanning tree that will be computed by 802.1d in this network assuming that all links have a unit cost ? Indicate the state of each port.

.. figure:: svg/ex-switches.png
   :align: center
   :scale: 70

   A small network composed of Ethernet switches

3. Consider the switched network shown in the figure above. In this network, assume that the LAN between switches `3` and `12` fails. How should the switches update their port/address tables after the link failure ?

4. In the network depicted in the figure below, the host H0 performs a traceroute toward its peer H1 (designated by its name) through a network composed of switches and routers. Explain precisely the frames, packets, and segments exchanged since the network was turned on. You may assign addesses if you need to.

.. figure:: svg/ex-switches_vs_routers.png
   :align: center
   :scale: 100

   The host H0 performs a traceroute toward its peer H1 through a network composed of switches and routers.

5. Many enterprise networks are organized with a set of backbone devices interconnected by using a full mesh of links as shown in the figure below. In this network, what are the benefits and drawbacks of using Ethernet switches and IP routers running OSPF ?

.. figure:: svg/ex-backbone.png
   :align: center
   :scale: 70

   A typical enterprise backbone network 

6. In the network represented on the figure below, can the host H0 communicate with H1 and vice-versa? Explain. Add whatever you need in the network to allow them to communicate.

.. figure:: svg/ex-routing_across_VLANs.png
   :align: center
   :scale: 30

   Can H0 and H1 communicate?

7. Consider the network depicted in the figure below. Both of the hosts H0 and H1 have two interfaces: one connected to the switch S0 and the other one to the switch S1. Will the link between S0 and S1 ever be used? If so, under which assumptions? Provide a comprehensive answer.

.. figure:: svg/ex-switches_wo_STP.png
   :align: center
   :scale: 30

   Will the link between the switches S0 and S1 ever be used?

8. Most commercial Ethernet switches are able to run the Spanning tree protocol independently on each VLAN. What are the benefits of using per-VLAN spanning trees ?
