.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Inter-domain routing and BGP
============================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues/new


Exercises
---------




1. The interdomain topology below is composed of four domains. For this exercise, we assume that there are no routing policies, i.e. each domain advertise all its best paths to its peers. We focus on the prefix `p` advertised by `AS1`.

.. graphviz::

   graph foo {
      randkir=LR;
      AS1 -- AS3; 
      AS1 -- AS2;
      AS3 -- AS4; 
      AS1 -- AS4;
   }

Assume that the BGP sessions are activated in the following order :

  - `AS1-AS2`
  - `AS3-AS4` 
  - `AS1-AS3`
  - `AS1-AS4`

At each step of this activation sequence, show the BGP messages for prefix `p` that are exchanged and provide the BGP routing table of the different ASes. Assume that BGP always prefers the short AS-Path.

Once the interdomain network has fully converged, analyze the consequence of a failure of the following BGP sessions on the routes towards prefix `p` :

  - `AS1-AS2`
  - `AS1-AS4`



2. Consider the network shown in the figure below. In this network, each AS contains a single BGP router. Assume that `R1` advertises a single prefix. `R1` receives a lot of packets from `R9`. Without any help from `R2`, `R9` or `R4`, how could `R1` configure its BGP advertisement such that it receives the packets from `R9` via `R3` ? What happens when a link fails ?


  .. figure:: fig/ex-bgp-internetwork.png
     :align: center
     :scale: 100


3. Consider the network shown in the figure below where R1 advertises a single prefix. In this network, the link between R1 and R2 is considered as a backup link. It should only be used only when the primary link (R1-R4) fails. 


  .. figure:: fig/ex-bgp-backup.png
     :align: center
     :scale: 100


  - Can you implement this in `R2` ? How ?
 
  - Assuming that `R1`-`R2` is a backup link, what are the paths used by all routers to reach `R1` ?
 
  - Assume now that the link `R1`-`R4` fails. Which BGP messages are exchanged and what are now the paths used to reach `R1` ?
 
  - Link `R1` - `R4` comes back. Which BGP messages are exchanged and what do the paths used to reach `R1` become ?

4. Consider the small Internet show in the figure below.

  .. graphviz::

     digraph foo {
       randkir=LR;
       AS2 -> AS1 [label=<<font color="red">$</font>>, color=red];
       AS2 -> AS3 [label=<<font color="red">$</font>>, color=red];
       AS1 -> AS4 [label=<<font color="red">$</font>>, color=red];
       AS3 -> AS4 [label=<<font color="red">$</font>>, color=red];
       AS5 -> AS4 [label=<<font color="red">$</font>>, color=red];
       AS1 -> AS3 [dir=none,label=<<font color="blue">=</font>>, color=blue];
       AS3 -> AS5 [dir=none,label=<<font color="blue">=</font>>, color=blue];
       AS2 -> AS5 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
       }


  In this small Internet, ``AS5`` advertises prefix ``2001:db8:5/48``. Which BGP messages are exchanged concerning this prefix when the following events occur (one after the other) :

   - the link between ``AS3`` and ``AS5`` fails
   - the link between ``AS1`` and ``AS2`` fails
   - the link between ``AS2`` and ``AS5`` fails

5. Consider the small Internet show in the figure below.

  .. graphviz::

     digraph foo {
       randkir=LR;
       AS3 -> AS2 [label=<<font color="red">$</font>>, color=red];
       AS5 -> AS1 [label=<<font color="red">$</font>>, color=red];
       AS1 -> AS2 [label=<<font color="red">$</font>>, color=red];
       AS1 -> AS4 [dir=none,label=<<font color="blue">=</font>>, color=blue];
       AS4 -> AS2 [dir=none,label=<<font color="blue">=</font>>, color=blue];
       AS5 -> AS4 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
       }

 a. ``AS3`` advertises prefix ``2001:db8:3/48``. Compute the BGP routing tables of all ASes towards this prefix.

 b. After a few months, ``AS3`` decides to become a customer of ``AS4``. Explain which BGP messages are exchanged when the link between ``AS3`` and ``AS4`` becomes active.

 c. After a few months, ``AS3`` decides to become a customer of ``AS5``. Explain which BGP messages are exchanged when the link between ``AS3`` and ``AS5`` becomes active.

 d. ``AS3`` is satisfied with its connectivity via ``AS4`` and ``AS5`` and decides to stop the BGP session with ``AS2``. Explain the BGP messages that are exchanged when this link is disabled.

Netkit BGP lab
--------------


This lab, :download:`/netkit/netkit-lab_bgp.zip`, allows you to experiment with the BGP operation. The simulated internetwork consists of 8 BGP routers, each one corresponding to a different Autonomous System (AS). They have the peering relations shown in the figure:



  .. figure:: fig/bgp-topology.png
     :align: center
     :scale: 100

To run BGP, these routers uses daemons called ``zebra`` and ``bgpd`` .

You can launch the lab using ``lstart`` in the lab folder. For monitoring traffic, you can use ``tcpdump`` and ``wireshark``.

In this lab, router ``r9`` announces via BGP an IPv6 prefix throughout the network. You can observe in the routing tables of the other routers that there are entries for the local prefixes and for the prefix announced by ``r9``, in which the nexthop is indicated. But routers have no addional information about prefixes from other routers.

You can have more advanced informations about how BGP runs on the routers by accessing to the ``bgpd`` daemon via ``telnet``:

 .. code-block:: console

    telnet localhost bgpd

The password is ``zebra``, as usual.

In the ``telnet`` terminal you can use:

 .. code-block:: console

    show ipv6 bgp summary
    show ip bgp neighbors
    show ip community-list


to get more infos. (Note that neighbors and community list queries use the `ip` command instead of the `ipv6` command). See the `quagga manual <http://www.nongnu.org/quagga/docs/quagga.html#BGP>`_ for ``bgpd`` for a more complete description of available commands.

You can find the configuration files of the running daemons in the routers' folders. For instance, consider router ``r1``. You can find 3 configuration files in ``lab/r1/etc/quagga``:

- The first one is ``daemons``. This file contains informations about which daemon should be started on our router.

- The second one is ``zebra.conf``. This file contains the password that we use to connect to the zebra daemon when we are on the router. (The password asked when accessing ``telnet localhost zebra``)

- The third one is ``bgpd.conf``. This is the configuration file of our bgpd daemon. The following picture details the meaning of Let's see what all these lines means.


     .. figure:: fig/bgpdconf.png
        :align: center
        :scale: 100

With this in mind, you are able to play with the topology and even create new routers that use BGP. Try some different configurations, try to change how the filters work and observe what happens. On the original lab, for instance, you can cause a failure on the `AS9`-`AS1` link (with the command ``ifconfig ... down``). Observe which BGP messages are exchanged and how the state of router ``r7`` changes. What are your expectations? Are your observations consistent with what you expected ?



.. include:: /links.rst
