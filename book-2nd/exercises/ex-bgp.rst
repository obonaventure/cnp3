.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Inter-domain routing and BGP
============================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=6

Exercises
---------

1. Consider the network below in which a stub `AS456` is connected to two providers `AS123` and `AS789`. Via which provider will the packets destined to ``2001:db8:cafe::/47`` will be received by `AS456` ? Should `AS123` change its configuration ? 

  .. figure:: fig/ex-bgp-stub-two-providers.png
     :align: center
     :scale: 100

2. Consider that the AS stub shown in the figure down decides to advertise two /48 prefixes instead of its allocated /47 prefix.

  .. figure:: fig/ex-bgp-stub-two-providers-specific.png
     :align: center
     :scale: 100

  -
       Via which provider does `AS456` receive the packets destined to ``2001:db8:caff::bb`` and ``2001:db8:cafe::aa`` ?
  
  -
       How is the reachability of these addresses affected when link `R1`-`R3` fails ?

  -
       Propose a configuration on R1 that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS4567` if one of `AS4567`'s interdomain links fails.

3. Consider the network shown in the figure below. In this network, each AS contains a single BGP router. Assume that `R1` advertises a single prefix. `R1` receives a lot of packets from `R9`. Without any help from `R2`, `R9` or `R4`, how could `R1` configure its BGP advertisement such that it receives the packets from `R9` via `R3` ? What happens when a link fails ?

  .. figure:: fig/ex-bgp-internetwork.png
     :align: center
     :scale: 100

4. Consider the network shown in the figure below where R1 advertises a single prefix. In this network, the link between R1 and R2 is considered as a backup link. It should only be used only when the primary link (R1-R4) fails. 

  .. figure:: fig/ex-bgp-backup.png
     :align: center
     :scale: 100

  -
       Can you implement this in `R2` ? How ?
 
  - 
       Assuming that `R1`-`R2` is a backup link, what are the paths used by all routers to reach `R1` ?
 
  - 
       Assume now that the link `R1`-`R4` fails. Which BGP messages are exchanged and what are now the paths used to reach `R1` ?
 
  - 
       Link `R1`-`R4` comes back. Which BGP messages are exchanged and what do the paths used to reach R1 become ?


Netkit BGP lab
--------------

This lab, ``bgp_lab``, allows you to experiment with BGP operation. The simulated internetwork consists of 8 BGP routers, each one corresponding to a different Autonomous System (AS). They have the peering relations shown in the figure:

  .. figure:: fig/bgp-topology.png
     :align: center
     :scale: 100

To run BGP, these routers uses daemons called ``zebra`` and ``bgpd`` .

You can launch the lab using ``lstart`` in the lab folder. For monitoring traffic, you can use ``tcpdump`` and ``wireshark``.

In this lab, router ``r9`` announces via BGP an IPv6 prefix throughout the network. You can observe in the routing tables of the other routers that there are entries for the local prefixes and for the prefix announced by ``r9``, in which the nexthop is indicated. But routers have no addional information about prefixes from other routers.

You can have more advanced informations about how BGP runs on the routers by accessing to the ``bgpd`` daemon via ``telnet``:

 .. code:: console

    telnet localhost bgpd

The password is ``zebra``, as usual.

In the ``telnet`` terminal you can use:

 .. code:: console

    show ipv6 bgp summary
    show ip bgp neighbors
    show ip community-list

to get more infos. (Note that neighbors and community list queries use the `ip` command instead of the `ipv6` command). See the ``quagga`` `manual`_ for ``bgpd`` for a more complete description of available commands.

 .. _manual: http://www.nongnu.org/quagga/docs/quagga.html#BGP


You can find the configuration files of the running daemons in the routers' folders. For instance, consider router ``r1``. You can find 3 configuration files in ``lab/r1/etc/quagga``:

- 
    The first one is ``daemons``. This file contains informations about which daemon should be started on our router.

-
    The second one is ``zebra.conf``. This file contains the password that we use to connect to the zebra daemon when we are on the router. (The password asked when accessing ``telnet localhost zebra``)

-   The third one is ``bgpd.conf``. This is the configuration file of our bgpd daemon. The following picture details the meaning of Let's see what all these lines means.

     .. figure:: fig/bgpdconf.png
        :align: center
        :scale: 100

With this in mind, you are able to play with the topology and even create new routers that use BGP. Try some different configurations, try to change how the filters work and observe what happens. On the original lab, for instance, you can cause a failure on the AS9-AS1 link (with the command ``ifconfig ... down``). Observe which BGP messages are exchanged and how the state of router ``r7`` changes. What are your expectations? Are your observations consistent with what you expected ?


.. include:: /links.rst
