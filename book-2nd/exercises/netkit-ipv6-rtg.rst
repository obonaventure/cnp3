.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

IP Address Assignment Methods and Routing
=========================================

.. warning:: 
   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=6

This TP introduces the main methods for IPv6 address assignment and illustrates the operation of two Internet routing protocols (OSPFv3 and RIP). For this, you will use 4 netkit_ labs: ``slaac``, ``dhcpv6``, ``ospfv3`` and ``rip``.

You will need to look into the traffic exchanged in the network links in order to understand the operation of the involved protocols and mechanisms. You can use the packet sniffering tools (such as ``tcpdump`` or ``wireshark``) for that.

 .. note ::

    Some ``tcpdump`` options (for more details and options, check ``man dump``):

    ``-i`` permits to choose an interface. 

    ``-v`` permits to display all packet details.

    ``-s`` permits to capture the entire Ethernet packets (not only the first 68 bytes).


 .. note:: How to use wireshark:

    To install it (under a ``debian`` OS), use :

     .. code:: console

        sudo apt-get install wireshark

    If you have root access to the machine, you can also use ``wireshark`` to visualize traffic captured within a netkit_ lab :

        When you have launched the lab, you can access to your ``$HOME`` directory or the lab directory (in the host machine) from a netkit_ virtual machine. These directories are located in ``/hosthome`` and ``/hostlab`` in netkit_ . Go into ``/hostlab`` :

        .. code:: console

           cd /hostlab

        Now you can launch a ``tcpdump`` capture and save the captured traffic on a file, in the hostlab (or hosthome) directory (option ``-w``). This allows you to start a capture from this file with ``wireshark``.

         .. code:: console

            tcpdump -n -i IF -w aaa.pcap &

        where ``aaa.out`` is the output file, ``IF`` the interface we want to listen on (use ``any`` for all interfaces) and we add the ``&`` symbol to run the sniffer in the background, so we can continue to work in the netkit_ shell.

        You can then launch ``wireshark`` on your computer with the input file ``aaa.out`` :

         .. code:: console

            wireshark -k -i<(tail -f aaa.pcap)&

    Note that this is *not* possible if you are a non-privileged user in the machine. Therefore, if you are running netkit_ from an Intel computer, you should use ``tcpdump`` to look at on-the-fly traffic.


Address Assignment Methods for IPv6
-----------------------------------

The SLAAC lab
~~~~~~~~~~~~~

The first lab (``slaac``) illustrates the operation of the Stateless Address Autoconfiguration (SLAAC) in IPv6. This mechanism allows hosts connecting to an IPv6 link to dynamically acquire a link-local address and, in case a router is present, to be assigned a global-scope IPv6. The link-local address enables a host to exchange packets with any other host in the same IPv6 link. Global-scope IPv6 address enables to communicate with machines beyond the current link.

Launch the ``slaac`` lab in netkit. This lab consists of 4 machines: 3 hosts (``hostA``, ``hostB`` and ``hostC``) and router ``r``, connected as shown in the figure:

  .. figure:: fig/topology-slaac.png
     :align: center
     :scale: 40

The router ``r`` is assigned the IPv6 address ``2001:db8:dead:beef::11/64`` and is configured to send periodically Router Advertisements and reply to Router Sollicitations, via the daemon ``radvd``. You can stop/restart this daemon by way of ``/etc/init.d/radvd`` instructions. Configuration of this daemon is detailed in file ``/etc/radvdv.conf``:

.. code-block:: console

   interface eth0 { 
       AdvSendAdvert on;
       MinRtrAdvInterval 3; 
       MaxRtrAdvInterval 10;
       prefix 2001:db8:dead:beef::/64 
       {
           AdvOnLink on; 
           AdvAutonomous on; 
           AdvRouterAddr on; 
       };
   };

Unlike previous labs, initial host configuration does not configure any particular IPv6 address on interfaces. They will be obtained dynamically. Their interfaces are ``down`` at the startup, so you need to set them up (with ``ifconfig eth0 up``) when you are ready to monitor the address assignment process. Use ``tcpdump`` on a host (for instance, ``hostA``) to capture the traffic in the link (and ``wireshark`` if you have root access to your machine). Look at the exchanged packets when the interfaces are set up. 

1.
    How are global-scope addresses assigned ? Describe the observed router discovery process.   

2.
    How do hosts acquire their link-local addresses ? How do these link-local addresses look like ? 

You can set an interface down and up to observe the acquisition of a new link-local address without restarting the lab.


The DHCPv6 lab
~~~~~~~~~~~~~~

The goal of this lab is to have a better understanding of DHCP. You will have the possibility to watch how this protocol works.

In this lab, you will work on a network with one router (``r1``) running a DHCPv6 server and 2 pcs (``pc1`` and ``pc2``) running DHCPv6 clients.

Here is the topology of the network:

  .. figure:: fig/topology-dhcp.png
     :align: center
     :scale: 60

To use DHCPv6, these machines uses daemons called ``dibbler``.

When the lab is launched, run the server daemon on the router, then run the client daemon on the hosts (``pc1`` and ``pc2``).

 .. code:: console

    /etc/init.d/dibbler-server start
    /etc/init.d/dibbler-client start

Based on the observed traffic, try to figure out:

1.
    Why the server sends periodically multicast messages?

2.
    What kind of messages are exchanged between the server and the clients? (You should identify 4 different types)


Intra-domain routing in the Internet
------------------------------------

The OSPFv3 lab
~~~~~~~~~~~~~~

The Open Shortest Path First (OSPF) protocol is a link-state routing protocol, widely used in today's Internet for intra-domain routing. OSPFv3 (OSPF for IPv6) is specified in :rfc:`5340`. OSPF control packets are sent directly over the IP layer, with protocol number 89, so they can be filtered with ``tcpdump`` with this command: ``tcpdump ip[9]==89``.

In this lab, you will work on a network with routers that use OSPFv3 to build their routing tables.

Here is the topology of the network:

  .. figure:: fig/topology-ospf.png
     :align: center
     :scale: 100


To use OSPF, these routers uses daemons called ``zebra`` and ``ospf6d`` .

Launch the lab. Note that, if you try to ``ping6`` from a router to a non-adjacent one, you will see a destination unreachable. This is because the OSPF deamon is not launched yet. It is interesting that you run ``tcpdump`` (in background) in at least one machine, in order to see the exchanged packets. 

You should launch the ``ospf6d`` daemon in every router, looking at how every new OSPF-enabled router impacts in the monitored traffic. Launch first the daemon on ``bb1``. To do that enter the following command line in the ``bb1`` terminal :

 .. code:: console

    /etc/init.d/zebra start

Then launch the daemon on ``bb2``. 

1.
    Which packets have been exchanged ? 

2.
    Did routing tables change ?

Launch now the deamon on the others routers while looking on the exchanged packets.

3.
    Perform traceroutes from/to different interfaces. 
    Think about the path the traceroute is expected to take, and the path ICMP replies are expected to take.
    Does the traceroute confirm your expetations?

Now we will access the ``ospf6d`` daemon. This will help us to see the OSPF link-state database (LSDB), neighbors and routes.

In netkit, type :

 .. code:: console

    telnet ::1 ospf6d

 .. note:: 
  
    Reminder: ``::1`` is the IPv6 address for localhost. ``ospf6d`` is the name of the daemon that runs OSPF in our router.

A password is asked, ``zebra`` should work.

Now you can ask some cool stuff at the OSPF daemon:

 .. code:: console

    show ipv6 ospf6 database
    show ipv6 ospf6 neighbor
    show ipv6 ospf6 route
    show ipv6 ospf6 interface
    exit

4.
    Is the LSDB the same for all routers ? Should it be ?


Now it is time to play with the topology. You can request the shortest path tree computed by a router (and monitor how it changes) with the command ``show ipv6 ospf6 spf tree`` when connected via ``telnet`` to the ``ospf6d`` daemon.

5.
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

     .. code:: console

        ifconfig IF down

    where ``IF`` is the name of your interface. (If you want to set up an interface down, remember that manually assigned static IP addresses vanish when the interface is down, so you need to assign them manually when you set it up again)

6.
    When you are in the daemon (``telnet ::1 ospf6d``) , change link cost and try some ``traceroute``. Below, the line you should enter in your console:

     .. code:: console

        telnet ::1 ospf6d
        zebra
        enable
        configure terminal
        router ospf6
        interface IF
        ipv6 ospf6 cost X

    where ``IF`` is the interface and ``X`` the new cost.


The RIP lab
~~~~~~~~~~~

The Routing Information Protocol (RIP) is a popular distance-vector protocol. It was widely used for intra-domain routing in the Internet, before being replaced by link-state protocols such as OSPF or IS-IS. RIPng (for IPv6) is specified in :rfc:`2080`. RIPng packets are UDP packets and are sent to port 521, so you can filter RIPng packets at ``tcpdump`` with this command: ``tcpdump udp and port 521``.

In this lab, you will work on a network with routers that use RIPng to build their routing tables.

Here is the topology of the network:

  .. figure:: fig/topology-rip.png
     :align: center
     :scale: 100


To use RIP, these routers use daemons called ``zebra`` and ``ripngd`` .

After launching the lab, and use ``tcpdump`` at the machine ``sniffer``. This machine has 5 interfaces, each of them connected to a different network link (see the topology description at ``lab.conf`` and the interfaces configuration at ``sniffer.startup``).

First of all, launch the ``ripngd`` and ``zebra`` daemons. To do that, type on each router the command :

 .. code:: console

    /etc/init.d/zebra start

After a while, all destinations are available. Why it is not instantaneous?

1.
    Check routing tables. Are they updated ?

2.
    Sniff the RIP packets using ``tcpdump`` and observe them. Is this consistent with what you expected ?


Now it is time to play with the topology.

3.
    Try to make some links fail and observe what is happening. You can do that by stoping one interface on a router :

     .. code:: console

        ifconfig IF down

    where ``IF`` is the name of your interface.

4.
    Observe what is happening. Is the network recovering fast ? Why ?


Assignment
----------

``laberr1``, ``laberr2`` and ``laberr3`` are three netkit_ labs describing networks with four routers (``r1`` to ``r4``). Routes in each network are configured with static routes, but routing is not correct. You can extract the netkit_ labs from the corresponding ZIP files (``laberr1.zip`` for ``laberr1``, and so on).

For each lab, find the errors and correct them, so that every router can reach successfully (e.g. with ``ping6``) every other router in the network.

.. include:: /links.rst
