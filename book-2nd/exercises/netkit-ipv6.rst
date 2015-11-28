.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Configuring IPv6
================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=6


During the previous labs, you have mainly used existing netkit_ labs to understand transport layer protocols such as TCP and UDP. This is one usage of netkit_, but not the most interesting one. An advantage of netkit_ compared to the utilisation of real networking devices is that it allows you to build quickly a network, configure it and test its operation. The netkit_ manpages, available from http://wiki.netkit.org/man/man7/netkit.7.html provide many details on the operation of netkit_

netkit_ is composed of a set of scripts that read configuration files and allow you to run scripts and copy files on the virtual machines that represent the routers and the switches. All the information about a netkit_ lab resides in a directory. The first file in such a directory is the `lab.conf <http://wiki.netkit.org/man/man5/lab.conf.5.html>`_ file. This file is a text file that describes the network topology that you want to emulate.

.. graphviz::

   graph foo {
      rankdir=LR;
      hostA [color=white, shape=box label=<<TABLE border="0" cellborder="0"><TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>hostA [2001:db8:be:feed::AA]</td></TR>
              </TABLE>>];
      hostB [color=white, shape=box label=<<TABLE border="0" cellborder="0"><TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>hostB [2001:db8:be:beef::BB]</td></TR>
              </TABLE>>];
      hostC [color=white, shape=box label=<<TABLE border="0" cellborder="0"><TR><TD width="45" height="60" fixedsize="true"><IMG SRC="icons/host.png" scale="true"/></TD></TR><TR><td>hostC [2001:db8:be:b00b::CC]</td></TR>
              </TABLE>>];
      r1[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>r1</td></TR>
              </TABLE>>];
      r2[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>r2</td></TR>
              </TABLE>>];
      r3[shape=box, color=white, label=<<TABLE border="0" cellborder="0">
                       <TR><TD width="75" height="30" fixedsize="true"><IMG SRC="icons/router.png" scale="true"/></TD></TR><TR><td>r3</td></TR>
              </TABLE>>];
      hostA--r1 [label="A"];
      hostB--r2 [label="B"];
      hostC--r3 [label="C"];
      r1--r2 [label="r12"];
      r2--r3 [label="r23"]; 
      r3--r1 [label="r13"];
   }


The network above, with three hosts and three routers can be represented by the following `lab.conf <http://wiki.netkit.org/man/man5/lab.conf.5.html>`_ file.

.. code-block:: console

   # Header
   LAB_DESCRIPTION="Lab to understand the basics of IPv6"
   LAB_VERSION=1
   LAB_AUTHOR="you"
   # List of virtual machines in the lab
   machines="hostA hostB hostC r1 r2 r3"
   # First host, 64 MBytes of RAM
   hostA[M]=64
   # The link between hostA and r1 ends on interface 0 on hostA and r1
   hostA[0]=A
   r1[0]=A
   # The link between hostB and r2
   hostB[0]=B
   r2[0]=B
   # The link between hostC and r3
   hostC[0]=C
   r3[0]=C
   # The link between r1 and r2
   r1[1]=r12
   r2[1]=r12
   # The link between r1 and r3
   r1[2]=r13
   r3[2]=r13
   # The link between r2 and r3
   r2[2]=r23
   r3[1]=r23


To build your own lab, you need to first define the subnetworks that compose the lab. Each subnetwork is identified by a label (`A` for the subnetwork between ``hostA`` and ``r1``). Then, you connect each subnetwork to an interface on a host or router. Each interface is identified by a unique integer. The first interface has number ``0``, the second number ``1``, ... In the virtual machine, interface ``0`` corresponds to interface ``eth0``. By default, a virtual machine has 32 Mbytes of virtual memory. If you need more memory, for example to run tcpdump_, you can extend it with the ``[M]`` parameter. Other parameters are described in the netkit_ man pages.

.. note:: Big brother in your emulated network

   In some scenarios, it might be interesting to have a virtual machine that is present on all links inside the emulated network. This virtual machine could allow you to easily collect packets on any link in the network. For example, if you would like to add such a monitoring machine in the network above, you could add the following configuration.

      .. code-block:: console

         # Add nsa to list of machines
         machines="hostA hostB hostC r1 r2 r3 nsa"
	 # NSA can capture all packets
	 nsa[0]=A
	 nsa[1]=B
	 nsa[2]=C
	 nsa[3]=r12
	 nsa[4]=r23
	 nsa[5]=r13
	 # To analyze all these packets, NSA needs memory
	 nsa[M]=128 


The above ``lab.conf`` file defines the network topology and the configuration of the virtual machines. To allow `lstart <http://wiki.netkit.org/man/man1/lstart.1.html>`_ to start the lab,
you need to create a directory for each virtual machine and a startup script. The directory is named ``machine`` where ``machine`` is the name chosen for the virtual machine. The startup script is specific for each virtual machine and is called ``machine.startup``. For example, to create these directories and files, you could run the following bash script in the directory where the ``lab.conf`` file is stored.

.. code-block:: console


   for vm in hostA hostB hostC r1 r2 r3
   do
     mkdir $vm
     touch $vm.startup
   done


With these files, you can start the lab, but the virtual machines need to be configured before you can exchange packets. For this, you need first to manually assign IPv6 addresses. On Linux, IP addresses are configured by using the :manpage:`ifconfig(8)` command [#fipcommand]_. This command takes a lot of parameters. A typical usage is the following :

.. code-block:: console

   # enable interface eth0
   ifconfig eth0 up
   # add one IPv6 address on this interface
   ifconfig eth0 add 2001:db8:be:feed::AA/64

The first command above activates interface ``eth0``. This command is mandatory before the interface can send/receive packets. The second command configures the IPv6 address associated to this interface. An IPv6 address is always composed of two parts :

 - a subnet identifier
 - a host identifier

The subnet identifier are the high order bits of the IPv6 address. They identify the subnet to which the interface is connected. In the example above, the subnet is 64 bits long and is ``2001:db8:be:feed``. All IPv6 addresses that belong to this subnet can be reached by using the attached subnetwork (i.e. through the datalink layer) without passing through an intermediate router. The low order bits of the address represent the host identifier (``::AA`` in the above configuration) inside the subnet.

Your first objective is to configure the IPv6 addresses of the three endhosts based on the information in the figure above. For this lab, we use only 64 bits subnets. Once an IPv6 address has been configured, you can verify that it is reachable from the host where it has been configured by issuing a :manpage:`ping6(8)` command towards this address on this host.

Once IPv6 has been configured on the endhosts, you need to configure the IPv6 addresses on the three routers. Start by configuring the IPv6 addresses on the interfaces ``eth0`` of these routers. For this, select one identifier in the subnetwork attached to each host and assign one host identifier to the attached router.

The next step is to configure the IPv6 addresses on the links between the routers. Select one subnetwork identifier starting from ``2001:db8:`` for each inter-router subnetwork and configure the IPv6 addresses on the two attached routers.

At this point, all IPv6 addresses should have been configured. Make sure that you recorded in a text file all the commands that you typed. They will be necessary later on to automate the creation of the lab. A good idea would be to create an ``/etc/hosts`` file that contains the mapping between names and all assigned IPv6 addresses. This file is a text file such as the one below.

.. code-block:: console

   ##
   # Host Database
   #
   # localhost is used to configure the loopback interface
   # when the system is booting.  Do not change this entry.
   ##
   127.0.0.1       localhost
   255.255.255.255 broadcasthost
   ::1             localhost 
   2001:db8:be:beef::AA      hostA
   2001:db8:be:feed::BB      hostB
   2001:db8:be:b00b::CC      hostC

Add to the file above the IPv6 addresses that you have configured for the routers. Make sure that a different name is used for each address chosen for a router. This file has the format of the ``/etc/hosts`` that provides name to address mappings when DNS is not in operation (as in this lab since we did not configure any DNS server). You can copy this file on all virtual hosts to have the list of all adresses on each host.

At this point, you have configured all IPv6 addresses, but there are still no routes. Without routes, packets will not be forwarded in the network. You need to manually configure the forwarding tables on the hosts and the routers.

On the hosts, configuring the routing table is simple. You simply need to add a default route towards the router that is directly connected to the host. This can be done by using the :manpage:`route(8)` command [#fipcommand]_.

.. code-block:: console

   #route -A inet6 add default gw 2001:db8:be:feed::11

The commande above adds a `default` route, i.e. a route towards ``::/0`` in the IPv6 routing table (parameter ``-A inet6``) that points to router (`gw` or gateway is an old synonym for router) ``2001:db8:be:feed::11``. This command can be issued on ``hostA`` and router ``r1`` must have been configured with address ``2001:db8:be:feed::11``. You can now add a default route on all virtual hosts.

You can verify that these routes have been inserted in the routing tables by inspecting them with the :manpage:`ip(8)` or :manpage:`route(8)` command.

The next step is to configure the routes on the three routers. For this, you need to first decide the paths that you want to use and make sure that all routers have a route towards at least the subnets attached to the endhosts.

A first approach is to use shortest path routing. In this case, you need to make sure that :

 - ``r1`` has a route to ``2001:db8:be:beef/64`` via ``r2``
 - ``r3`` has a route to ``2001:db8:be:beef/64`` via ``r2``
 - ``r2`` has a route to ``2001:db8:be:feed/64`` via ``r1``
 - ``r3`` has a route to ``2001:db8:be:feed/64`` via ``r1``
 - ``r1`` has a route to ``2001:db8:be:b00b/64`` via ``r3`` 
 - ``r2`` has a route to ``2001:db8:be:b00b/64`` via ``r3``

When you configure such a route, make sure that you use the correct IPv6 address of the gateway. For example, to configure the first route above on ``r1``, you might issue a command such as :

.. code-block:: console

   /sbin/route -A inet6 add 2001:db8:be:feed::/64 gw 2001:db8:bad:1212::22

Assuming that subnet ``2001:db8:bad:1212/64`` has been used on the link between ``r1`` and ``r2`` and that the address of ``r2`` on this subnet is ``2001:db8:bad:1212::22``.

.. note:: Asymmetric paths

   Note that when manually configuring the routes as above, nothing forces you to use symmetric routes. For example, the following paths could be configured in the network above.

     - ``r1`` has a route to ``2001:db8:be:beef/64`` via ``r2``
     - ``r3`` has a route to ``2001:db8:be:beef/64`` via ``r1``
     - ``r2`` has a route to ``2001:db8:be:feed/64`` via ``r3``
     - ``r3`` has a route to ``2001:db8:be:feed/64`` via ``r1``
     - ``r1`` has a route to ``2001:db8:be:b00b/64`` via ``r2`` 
     - ``r2`` has a route to ``2001:db8:be:b00b/64`` via ``r3``

   Feel free to configure such paths in a different lab.


Before testing the lab, make sure that the three routers are configured to forward IPv6 packets, i.e. act as routers. By default, Linux virtual machines are configured as endhosts and do not forward IPv6 packets. You can change this configuration by issuing the following ``sysctl`` :

 .. code-block:: console 

    sysctl -w net.ipv6.conf.all.forwarding=1


Now, you are ready to test the correct operation of your emulated network. For this, you can use the two most common network debugging tools :

 - :manpage:`ping6(8)` 
 - :manpage:`traceroute6(8)`

:manpage:`ping6(8)` sends an ICMP Echo request to a given destination address. If :manpage:`ping6(8)` succeeds, this indicates that both the forward and backward paths operate correctly. :manpage:`traceroute6(8)` sends UDP segments with different HopLimit values to discover the routers on a path towards a given destination address. If :manpage:`ping6(8)` and :manpage:`traceroute6(8)` succeed between all pairs of hosts, your network is correctly configured. Otherwise, try to find the missing or buggy configuration and correct it.


Configuring a network manually takes some time and requires many commands. You probably do not want to issue all these commands each time you start a netkit_ lab. netkit_ helps you to automate the configuration of the virtual machines with two simple tools.

The first way to automate a lab is the startup script. A startup script is a simple shell script that is launched automatically by netkit_ once a virtual machine has booted. This script is named ``machine.startup`` where ``machine`` is the name of the virtual machine. It is placed in the directory that contains the ``lab.conf`` file.

The second way to automate a lab is by automatically copying files on the virtual machines. For each virtual machine, you can provide a hierarchy of directories and files that will be copied by netkit_ when the virtual machine starts. For example, if you want to place the ``hosts`` file automatically as ``/etc/hosts`` on virtual machine ``hostA``, issue the following commands from the directory that contains ``lab.conf``.

.. code-block:: console
   
   mkdir hostA
   cd hostA
   mkdir etc
   cd etc
   cp ../../hosts .

These commands create the hostA/etc directory and copy the hosts file that we created earlier at its final location. This file will be copied as ``/etc/hosts`` in the filesystem used by virtual machine ``hostA``.

Exercise
--------

ICMPv6 :rfc:`4443`, the Internet Control Message Protocol, is a key companion to IPv6. ICMPv6 can report to the sender various types of errors that can occur during the transmission of a packet. :manpage:`traceroute6(8)` exploits one of these messages to determine the path followed by packets towards a given destination.

To demonstrate your understanding of ICMPv6, prepare a lab with a few hosts and routers, prepare and test a scenario that uses a few commands that would cause a host or router to generate one of the following ICMPv6 error messages :

 - `Destination Unreachable` (but not from a router directly connected to the source of the packet)

    - Code ``0`` : No route to destination
    - Code ``3`` : Address unreachable
    - Code ``4`` : Port unreachable

 - `Packet Too Big` (with UDP segments and TCP segments)
 - `Time Exceeded` message (but only Code ``1`` - Fragment reassembly time exceeded)
 

.. Provide in your report a short text that explains why each ICMPv6 error message is generated and show a tcpdump_ output containing this message.




.. rubric:: Footnotes

.. [#fipcommand] You can use the ``ip`` command instead of :manpage:`ifconfig(8)` or :manpage:`route(8)`. See the `Linux IPv6 Howto <http://www.tldp.org/HOWTO/Linux%2BIPv6-HOWTO/chapter-configuration-interface.html>`_ for additional information.


.. include:: /links.rst
