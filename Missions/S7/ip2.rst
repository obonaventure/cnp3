IP Routing protocols
====================


1. In the previous questions, you have worked on the stable state of the routing tables computed by routing protocols. Let us now consider the transient problems that main happen when the network topology changes [#ffailures]_. For this, consider the network topology shown in the figure below and assume that all routers use a distance vector protocol that uses split horizon.

.. figure:: ../S6/fig/routing-fig-004-c.png
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


2. Consider the network shown below. In this network, the metric of each link is set to `1` except link `A-B` whose metric is set to `4` in both directions. In this network, there are two paths with the same cost between `D` and `C`. Old routers would randomly select one of these equal cost paths and install it in their forwarding table. Recent routers are able to use up to `N` equal cost paths towards the same destination. 

 .. figure:: ../S9/fig/BGP-figs-010-c.png
    :align: center
    :scale: 70
   
    A simple network running a link state routing protocol

 On recent routers, a lookup in the forwarding table for a destination address returns a set of outgoing interfaces. How would you design an algorithm that selects the outgoing interface used for each packet, knowing that to avoid reordering, all segments of a given TCP connection should follow the same path ? 

2. Consider again the network shown above. After some time, the routing protocol converges and all routers compute the following routing tables :

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

An important difference between distance vector and link state routing is that link state routers flood link state packets that allow the other routers to recompute their own routing tables while distance vector routers exchange distance vectors. Consider that link `B-C` fails and that router `B` is the first to detect the failure. At this point, `B` cannot reach anymore `A`, `C` and 50% of its paths towards `E` have failed. `C` cannot reach `B` anymore and half of its paths towards `D` have failed.

Router `B` will flood its updated link state packet through the entire network and all routers will recompute their forwarding table. Upon reception of a link state packet, routers usually first flood the received link-state packet and then recompute their forwarding table. Assume that `B` is the first to recompute its forwarding table, followed by `D`, `A`, `C` and finally `E`

#. After each update of a forwarding table, verify which pairs of routers are able to exchange packets. Provide your answer using a table similar to the one shown above.
#. Can you find an ordering of the updates of the forwarding tables that avoids all transient problems ?



.. [#ffailures] The main events that can affect the topology of a network are :
 - the failure of a link. Measurements performed in IP networks have shown that such failures happen frequently and usually for relatively short periods of time
 - the addition of one link in the network. This may be because a new link has been provisioned or more frequently because the link failed some time ago and is now back
 - the failure/crash of a router followed by its reboot. 
 - a change in the metric of a link by reconfiguring the routers attached to the link
 See http://totem.info.ucl.ac.be/lisis_tool/lisis-example/ for an analysis of the failures inside the Abilene network in June 2005 or http://citeseer.ist.psu.edu/old/markopoulou04characterization.html for an analysis of the failures affecting a larger ISP network


.. exercices complementaires : calculer 8/13,  adresse plus basse et plus haute, découper un bloc /9 en deux plus petits blocs, ...



Internet Protocol
-----------------


1. For the following IPv4 subnets, indicate the smallest and the largest IPv4 address inside the subnet :

 - 8.0.0.0/8
 - 172.12.0.0/16
 - 200.123.42.128/25
 - 12.1.2.0/13

2. For the following IPv6 subnets, indicate the smallest and the largest IPv6 address inside the subnet :
 
 - FE80::/64
 - 2001:db8::/48
 - 2001:6a8:3080::/48

3. netkit_ allows to easily perform experiments by using an emulated environment is is composed of virtual machines running User Model Linux. netkit_ allows to setup a small network in a lab and configure it as if you had access to several PCs interconnected by using cables and network equipments.

 A netkit_ lab is defined as a few configuration files and scripts :
  
  `lab.conf` is a textfile that defines the virtual machines and the network topology. A simple `lab.conf` file is shown below ::

    LAB_DESCRIPTION="a string describing the lab"
    LAB_VERSION=1.0
    LAB_AUTHOR="the author of the lab"
    LAB_EMAIL="email address of the author"
    
    h1[0]="lan"
    h2[0]="lan"

  This configuration file requests the creation of two virtual machines, named `h1` and `h2`. Each of these hosts has one network interface (`eth0`) that is connected to the local area network named `"lan"`. netkit_ allows to define several interfaces on a given host and attach them to different local area networks.
  A `host.startup` file for each host (`h1.startup` and `h2.startup` in the example above). This file is a shell script that is executed at the end of the boot of the virtual host. This is typically in this script that the network interfaces are configured and the daemons are launched.
  A directory for each host (`h1` and `h2` in the example above). This directory is used to store configuration files that must be copied on the virtual machine's filesystems when they are first created.

 netkit_ contains several scripts that can be used to run a lab. `lstart` allows to launch a lab and `lhalt` allows to halt the machines at the end of a lab. If you need to exchange files between the virtual machines and the Linux host on which netkit_ runs, note that the virtual hosts mount the directory that contains the running lab in `/hostlab` and your home directory in `/hosthome`.

 For this exercise, you will use a netkit_ lab containing 4 hosts and two routers. The configuration files are available :download:`labs/lab-2routers.tar.gz`. The network topology of this lab is shown in the figure below.

 .. figure:: ../S6/fig/routing-fig-008-c.png
    :align: center 
    :scale: 50

    The two routers lab

 The `lab.conf` file for this lab is shown below ::

  h1[0]="lan1"
  h2[0]="lan1"
  h3[0]="lan2"
  router1[0]="lan1"  
  router1[1]="lan2"
  router2[0]="lan2"
  router2[1]="lan3"
  h4[0]="lan3"

 In this network, we will use subnet `172.12.1.0/24` for `lan1`, `172.12.2.0/24` for `lan2` and `172.12.3.0/24` for `lan3`.

 On Linux, the IP addresses assigned on an interface can be configured by using :manpage:`ifconfig(8)`. When :manpage:`ifconfig(8)` is used without parameters, it lists all the existing interfaces of the host with their configuration. A sample :manpage:`ifconfig(8)` output is shown below ::

  host:~# ifconfig
  eth0	  Link encap:Ethernet  HWaddr FE:3A:59:CD:59:AD  
          Inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::fc3a:59ff:fecd:59ad/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:216 (216.0 b)  TX bytes:258 (258.0 b)
          Interrupt:5 

  lo       Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)

 
 This host has two interfaces : the loopback interface (`lo` with IPv4 address `127.0.0.1` and IPv6 address `::1`) and the `eth0` interface. The `192.168.1.1/24` address and a link local IPv6 address (`fe80::fc3a:59ff:fecd:59ad/64`) have been assigned to interface `eth0`. The broadcast address is used in some particular cases, this is outside the scope of this exercise. :manpage:`ifconfig(8)` also provides statistics such as the number of packets sent and received over this interface. Another important information that is provided by :manpage:`ifconfig(8)` is the hardware address (HWaddr) used by the datalink layer of the interface. On the example above, the `eth0` interface uses the 48 bits `FE:3A:59:CD:59:AD` hardware address.

 You can configure the IPv4 address assigned to an interface by specifying the address and the netmask ::

  ifconfig eth0 192.168.1.2 netmask 255.255.255.128 up

 You can also specify the prefix length ::

  ifconfig eth0 192.168.1.2/25 up

 In both cases, `ifconfig eth0` allows you to verify that the interface has been correctly configured ::

  eth0      Link encap:Ethernet  HWaddr FE:3A:59:CD:59:AD  
            inet addr:192.168.1.2  Bcast:192.168.1.127  Mask:255.255.255.128
            inet6 addr: fe80::fc3a:59ff:fecd:59ad/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            RX packets:3 errors:0 dropped:0 overruns:0 frame:0
            TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000 
            RX bytes:216 (216.0 b)  TX bytes:258 (258.0 b)
            Interrupt:5 

 
 Another important command on Linux is :manpage:`route(8)` that allows to look at the contents of the routing table stored in the Linux kernel and change it. For example, `route -n` returns the contents of the IPv4 routing table. See :manpage:`route(8)` for a detailed description on how you can configure routes by using this tool. 

 a. Use :manpage:`ifconfig(8)` to configure the following IPv4 addresses :
  
   - `172.16.1.11/24` on interface `eth0` on `h1`
   - `172.16.1.12/24` on interface `eth0` on `h2`

 b. Use `route -n` to look at the contents of the routing table on the two hosts.
 c. Verify by using :manpage:`ping(8)` that `h1` can reach `172.16.1.12` 
 d. Use :manpage:`ifconfig(8)` to configure IPv4 address `172.16.1.1/24` on the `eth0` interface of `router1` and `172.16.2.1/24` on the `eth1` interface on this router.
 e. Since hosts `h1` and `h2` are attached to a local area network that contains a single router, this router can act as a default router. Add a default route on `h1` and `h2` so that they can use `router1` as their default router to reach any remote IPv4 address. Verify by using :manpage:`ping(8)` that `h1` can reach address `172.16.2.1`. 
 f. What do you need to configure on `router2`, `h3` and `h4` so that all hosts and routers can reach all hosts and routers in the emulated network ? Add the `ifconfig` and `route` commands in the `.startup` files of all the hosts so that the network is correctly configured when it is started by using `lstart`.

4. Use the network configured above to test how IP packets are fragmented. The `ifconfig` command allows you to specify the Maximum Transmission Unit (MTU), i.e. the largest size of the frames that are allowed on a given interface. The default MTU on the `eth?` interfaces is 1500 bytes. 

 a. Force an MTU of 500 bytes on the three interfaces attached to `lan2`.
 b. Use `ping -s 1000` to send a 1000 bytes ping packet from `h3` to one of the routers attached to `lan2` and capture the packets on the other router by using :manpage:`tcpdump(8)`. In which order does the emulated host sends the IP fragments ?
 c. Use `ping -s 2000` to send a 2000 bytes ping packet from `h1` to `h4` and capture the packets on `lan2` and `lan3` by using :manpage:`tcpdump(8)`. In which order does the emulated host sends the IP fragments ?
 d. From your measurements, how does an emulated host generate the identifiers of the IP packets that it sends ? 
 e. Reset the MTU on the `eth1` interface of router `r1` at 1500 bytes, but leave the MTU on the `eth0` interface of router `r2` at 500 bytes. Check whether host `h1` can ping host `h4`. Use :manpage:`tcpdump(8)` to analyse what is happening.

.. 4. Do the same exercise as above by using IPv6. Assume that the subnet `2001:db8:1::/64` is used for `lan1`, `2001:db8:2::/64` is used for `lan2` and `2001:db8:3::/64` is used for `lan3`. Note that you should use :manpage:`ping6(8)` to ping an IPv6 address instead of :manpage:`ping(8)` 


5. The Routing Information Protocol (RIP) is a distance vector protocol that is often used in small IP networks. There are various implementations of RIP. For this exercise, you will use quagga_, an open-source implementation of several IP routing protocols that runs on Linux and other Unix compatible operating systems. :manpage:`quagga(8)` is in fact a set of daemons that interact together and with the Linux kernel. For this exercise, you will use two of these daemons : :manpage:`zebra(8)` and :manpage:`ripd(8)`. :manpage:`zebra(8)` is the master daemon that handles the interactions between the Linux kernel routing table and the routing protocols. :manpage:`ripd(8)` is the implementation of the RIP protocol. It interacts with the Linux routing tables through the :manpage:`zebra(8)` daemon.

 To use a Linux real or virtual machine as a router, you need to first configure the IP addresses of the interfaces of the machine. Once this configuration has been verified, you can configure the :manpage:`zebra(8)` and :manpage:`ripd(8)` daemons. The configuration files for these daemons reside in `/etc/zebra`. The first configuration file is `/etc/zebra/daemons`. It lists the daemons that are launched when zebra is started by `/etc/init.d/zebra`. To enable :manpage:`ripd(8)` and :manpage:`zebra(8)`, this file will be configured as ::

  # This file tells the zebra package 
  # which daemons to start.
  # Entries are in the format: <daemon>=(yes|no|priority)
  # where 'yes' is equivalent to infinitely low priority, and
  # lower numbers mean higher priority. Read
  # /usr/doc/zebra/README.Debian for details.
  # Daemons are: bgpd zebra ospfd ospf6d ripd ripngd
  zebra=yes
  bgpd=no
  ospfd=yes
  ospf6d=no
  ripd=no
  ripngd=no

 The second configuration file is the `/etc/zebra/zebra.conf` file. It defines the global configuration rules that apply to :manpage:`zebra(8)`. For this exercise, we use the default configuration file, i.e. ::

  ! -*- zebra -*-
  !
  ! zebra configuration file
  !
  hostname zebra
  password zebra
  enable password zebra
  !
  ! Static default route sample.
  !
  !ip route 0.0.0.0/0 203.181.89.241
  !
  log file /var/log/zebra/zebra.log

 In the zebra configuration file, lines beginning with `!` are comments. This configuration defines the hostname as `zebra` and two passwords. The default password (`password zebra`) is the one that must be given when connecting to the :manpage:`zebra(8)` management console over a TCP connection. This management console can be use like a shell on a Unix host to specify commands to the :manpage:`zebra(8)` daemons. The second one (`enable password zebra`) specifies the password to be provided before giving commands that change the configuration of the daemon. It is also possible to specify static routes in this configuration file, but we do not use this facility in this exercise. The last parameter that is specified is the log file where :manpage:`zebra(8)` writes debugging information. Additional information about quagga_ are available from http://http://www.quagga.net/docs/docs-info.php

 The most interesting configuration file for this exercise is the `/etc/zebra/ripd.conf` file. It contains all the parameters that are specific to the operation of the RIP protocol. A sample :manpage:`ripd(8)` configuration file is shown below ::

   !
   hostname ripd
   password zebra
   enable password zebra
   !
   router rip
    network 100.1.0.0/16
    redistribute connected
   !
   log file /var/log/zebra/ripd.log

 This configuration files shown the two different ways to configure :manpage:`ripd(8)`. The statement `router rip` indicates the beginning of the configuration for the RIP routing protocol. The indented lines that follow are part of the configuration of this protocol. The first line, `network 100.1.0.0/16` is used to enable RIP on the interface whose IP subnet matches `100.1.0.0/16`. The second line, `redistribute connected` indicates that all the subnetworks that are directly connected on the router should be advertised. When this configuration line is used, :manpage:`ripd(8)` interacts with the Linux kernel routing table and advertises all the subnetworks that are directly connected on the router. If a new interface is enabled and configured on the router, its subnetwork prefix will be automatically advertised. Similarly, the subnetwork prefix will be automatically removed if the subnetwork interface is shutdown.
 
 To experiment with RIP, you will use the emulated routers shown in the figure below. You can download the entire lab from :download:`labs/lab-5routers-rip.tar.gz`

 .. figure:: ../S6/fig/routing-fig-009-c.png
    :scale: 50
    :align: center 

    The five routers lab

 The `lab.conf` describing the topology and the interfaces used on all hosts is shown below ::

   r1[0]="A"
   r1[1]="B"
   r1[2]="F"
   r1[3]="V"
   r2[0]="A"
   r2[1]="C"
   r2[2]="W"
   r3[0]="B"
   r3[1]="C"
   r3[2]="D"
   r3[3]="X"
   r4[0]="D"
   r4[1]="E"
   r4[2]="Y"
   r5[0]="E"
   r5[1]="F"
   r5[2]="Z"

 There are two types of subnetworks in this topology. The subnetworks from the `172.16.0.0/16` prefix are used on the links between routers while the subnetworks from the `192.168.0.0/16` prefix are used on the local area networks that are attached to a single router.

 A router can be configured in two different ways : by specifying configuration files and by typing the commands directly on the router by using :manpage:`telnet(1)`. The first four routers have been configured in the provided configuration files. Look at `r1.startup` and the configurations files in `r1/tmp/zebra` in the lab's directory for router `r1`. The `r?.startup` files contain the :manpage:`ifconfig(8)` commands that are used to configure the interfaces of each virtual router. The configuration files located in `r?/tmp/zebra` are also copied automatically on the virtual router when it boots.

  a. Launch the lab by using `lstart` and verify that router `r1` can reach `192.168.1.1`, `192.168.2.2`, `192.168.3.3` and `192.168.4.4`. You can also :manpage:`traceroute(8)` to determine what is the route followed by your packets.
  b. The :manpage:`ripd(8)` daemon can also be configured by typing commands over a TCP connection. :manpage:`ripd(8)` listens on port `2602`. On router `r1`, use `telnet 127.0.0.1 2602` to connect to the :manpage:`ripd(8)` daemon. The default password is `zebra`. Once logged on the :manpage:`ripd(8)` daemon, you reach the `>` prompt where you can query the status of the router. By typing `?` at the prompt, you will find the list of supported commands. The `show` command is particularly useful, type `show ?` to obtain the list of its sub options. For example, `show ip rip` will return the routing table that is maintained by the :manpage:`ripd(8)` daemon. 
  c. Disable interface `eth3` on router `r1` by typing `ifconfig eth3 down` on this router. Verify the impact of this command on the routing tables of the other routers in the network. Re-enable this interface by typing `ifconfig eth3 up`.
  d. Do the same with the `eth1` interface on router `r3`.
  e. Edit the `/etc/zebra/ripd.conf` configuration file on router `r5` so that this router becomes part of the network. Verify that `192.168.5.5` is reachable by all routers inside the network.
 
6. The Open Shortest Path First (OSPF) protocol is a link-state protocol that is often used in enterprise IP networks. OSPF is implemented in the :manpage:`ospfd(8)` daemon that is part of quagga_. We use the same topology as in the previous exercise. The netkit lab may be downloaded from :download:`labs/lab-5routers-ospf.tar.gz`.

 The :manpage:`ospfd(8)` daemon supports a more complex configuration that the :manpage:`ripd(8)` daemon. A sample configuration is shown below ::

   !
   hostname ospfd
   password zebra
   enable password zebra 
   !
   interface eth0
     ip ospf cost 1
   interface eth1
     ip ospf cost 1
   interface eth2 
     ip ospf cost 1
   interface eth3 
     ip ospf cost 1
   !
   router ospf
     router-id 192.168.1.1
     network 172.16.1.0/24 area 0.0.0.0
     network 172.16.2.0/24 area 0.0.0.0
     network 172.16.3.0/24 area 0.0.0.0
     network 192.168.1.0/24 area 0.0.0.0
     passive-interface eth3
   !
   log file /var/log/zebra/ospfd.log

 In this configuration file, the `ip ospf cost 1` specify a metric of `1` for each interface. The :manpage:`ospfd(8)` configuration is composed of three parts. First, each router must have one identifier that is unique inside the network. Usually, this identifier is one of the IP addresses assigned to the router. Second, each subnetwork on the router is associated with an area. In this example, we only use the backbone area (i.e. `0.0.0.0`). The last command specifies that the OSPF Hello messages should not be sent over interface `eth3` although its subnetwork will be advertised by the router. Such a command is often used on interfaces that are attached to endhosts to ensure that no problem will occur if a student configures a software OSPF router on his laptop attached to this interface. 

 The netkit_ lab contains already the configuration for routers `r1` - `r4`.

 The :manpage:`ospfd(8)` daemon listens on TCP port `2604`. You can follow the evolution of the OSPF protocol by using the `show ip ospf ?` commands.  

 a. Launch the lab by using `lstart` and verify that the `192.168.1.1`, `192.168.2.2`, `192.168.3.3` and `192.168.4.4` addresses are reachable from any router inside the network.
 b. Configure router `r5` by changing the `/etc/zebra/ospfd.conf` file and restart the daemon. Verify that the `192.168.5.5` address is reachable from any router inside the network.
 c. How can you update the network configuration so that the packets sent by router `r1` to router `r5` use the direct link between the two routers while the packets sent by `r5` are forwarded via `r4` ?
 d. Disable interface `eth3` on router `r1` and see how quickly the network converges ? You can follow the evolution of the routing table on a router by typing `netstat -rnc`. Re-enable interface `eth3` on router `r1`. 
 e. Change the MTU of `eth0` on router `r1` but leave it unchanged on interface `eth0` of router `r2`. What is the impact of this change ? Can you explain why ?
 f. Disable interface `eth1` on router `r3` and see how quickly the network converges ? Re-enable this interface.
 g. Halt router `r2` by using `vcrash r2`. How quickly does the network react to this failure ?


.. include:: ../../book/links.rst


.. exercices complementaires : calculer 8/13,  adresse plus basse et plus haute, découper un bloc /9 en deux plus petits blocs, ...
.. tp forwarding dans un réseau avec des routeurs
.. revoir mieux la configuration de base des uml, elle a posé des problèmes, penser à expliquer les routes par défaut, la configuration des adresses ip de chaque pc a pris du temps, voir comment on peut simplifier cela et mieux l'expliquer

