.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


Configuring DNS and HTTP servers
================================

Configuring DNS and HTTP servers can be complex on real hosts. To allow you to learn network configurations without risking breaking anything, we will use Netkit_. Netkit_ is network emulator based on User Mode Linux. It allows to easily set up an emulated network composed of virtual Linux machines, that can act as end-host or routers.  


.. note:: Where can I find Netkit?

 Netkit_ is available at http://www.netkit.org. For the labs, we have built a custom netkit image which is installed on the INGI servers [#fimage]_ . 

There are two ways to use Netkit_ : The manual way, and by using pre-configured labs.  In the first case, you boot and control each machine individually, using the commands starting with a "v" (for virtual machine).   In the second case, you can start a whole network in a single operation.  The commands for controlling the lab start with a "l".  The man pages of those commands is available from http://wiki.netkit.org/man/man7/netkit.7.html

.. You must be careful not to forgot to stop your virtual machines and labs, using either `vhalt` or `lhalt`.  

.. Netkit has already been installed in the student labs, in `/etinfo/applications/netkit` . All you have to do in order to use it is to set the following environment variables :


.. export NETKIT_HOME=/etinfo/applications/netkit
..  export MANPATH=:$NETKIT_HOME/man
.. export PATH=$NETKIT_HOME/bin:$PATH
.. It is usually convenient to put those lines in your shell initialization file.  

A netkit_ lab is simply a directory containing at least a configuration file called `lab.conf`, and one directory for each virtual machine.  

.. In the case the lab available on iCampus, the network is composed of two pcs, `pc1` and `pc2`, both of them being connected to a router `r1`.  The lab.conf file contains the following lines : 

.. .. code-block:: text

..    pc1[0]=A
..  pc2[0]=B
.. r1[0]=A
..  r1[1]=B


.. This means that `pc1` and `r1` are connected to a "virtual LAN" named `A` via their interface `eth0`, while `pc2` and `r1` are connected to the "virtual LAN" `B` via respectively their interfaces `eth0` and `eth1`.  

The directory of each device is initially empty, but will be used by Netkit_ to store their filesystem. 

The lab directory can contain optional files. Some labs will include configuration files while others will use scripts that are executed when the virtual machines boot.

.. In the lab provided to you, the "pc1.startup" file contains the shell instructions to be executed on startup of the virtual machine.  In this specific case, the script configures the interface `eth0` to allow traffic exchanges between `pc1` and `r1`, as well as the routing table entry to join `pc2`.   

Starting a lab consists thus simply in unpacking the provided archive, going into the lab directory and typing `lstart` to start the network.  

.. .. note:: File sharing between virtual machines and host

 

.. In the netkit lab (:download:`exercises/netkit/netkit_lab_2hosts_1rtr_ipv4.tar.tar.gz`, you can find a simple python_ client/server application that establishes TCP connections. Feel free to re-use this code to perform your analysis.    

.. note:: netkit tools

 As the virtual machines run Linux, standard networking tools such as :manpage:`ping(8)`, tcpdump_, netstat_ etc. are available.  

 Another useful hint is that is it possible to share files between the Netkit_ virtual machines and the local host. Virtual machines can access to the directory of the lab they belong to. This directory is mounted in their filesystem at the path  `/hostlab`.  

.. Note that capturing network traces can be facilitated by using the `uml_dump` extension available at https://netkit-ng.github.io/umldump.html .  This extension is already installed in the Netkit installation on the student lab.  In order to capture the traffic exchanged on a given 'virtual LAN', you simply need to issue the command `vdump <LAN name>` on the host. If you want to pipe the trace to wireshark, you can use `vdump A | wireshark -i - -k`



Starting Netkit in the lab
--------------------------

Netkit_ has been installed in the INGI labs. In order to run the Netkit network emulator, launch the following commands:

 .. code-block:: console
    
    ssh -Y <ingilogin>@permeke.info.ucl.ac.be
    export PATH=$PATH:/etinfo/applications/netkit/bin

To launch a single host instance, use the command ``vstart``:

 .. code-block:: console
   
    vstart hostname

To launch the DNS lab[#fdnslab]_, use the following commands:

 .. code-block:: console
 
    cp -r /etinfo/applications/netkit/dnslab/ $HOME/	# do not forget the trailing /'s
    lstart -f -d $HOME/dnslab

An interesting option for ``lstart`` is this one in order to use Gnome-Terminal instead of Xterm windows:

 .. code-block:: console
 
    lstart -f -d $HOME/dnslab -o --xterm=gnome

To stop the lab, please stop all the involved instances by using the command ``halt`` inside each virtual machine.

Do not forget to cleanup the virtual disks when you are finished:

 .. code-block:: console

    rm -f $HOME/dnslab/\*.disk

Note that you can also use ``lcrash`` command in order to immediately stop all your instances and remove all virtual disks.

 .. code-block:: console

    lcrash -d $HOME/dnslab

Exploring DNS
-------------

In this lab, you will experiment with the Domain Name system. Several DNS servers and resolvers are preconfigured in the Netkit_ which is provided. 

Below, you can find a graph where the DNS topology we will use is depicted.

  .. figure:: fig/dns-lab.png
     :align: center
     :scale: 40

To begin experimentation, start the lab by using the commands explained above. In this lab, the DNS servers are correctly configured. We ask you to find the IP address of the following fully qualified domain names (FQDN):

  - ``pc2.nanoinside.net``
  - ``dnsorg.org``
  - ``dnsroot``

For this, you should use the ``dig`` command whose syntax is :

 .. code-block:: console

    dig @server -t type FQDN

If no server is specified, ``dig`` uses the default resolver that you can find in the configuration file ``/etc/resolv.conf``.

While doing these requests, observe the packets that are exchanged between the differents DNS server with the ``+trace`` option. Is this what you expected? Sketch the Questions/responses on the figure below.

  .. figure:: fig/dns-lab.png
     :align: center
     :scale: 50

You have learned that DNS can work in two ways: Forward and Reverse. We will now resolve IPv6 addresses into their corresponding DNS names. Find the FQDN domain name of the following IPv6 addresses :

 - ``2001:db8:ba1:b0a::22``
 - ``2001:db8:ba1:b0a::2``

Again, you should use the ``dig`` command but with the ``-x`` option.

 .. code-block:: console

    dig @server -x ipv6

with as parameter the IPv6 address you want to resolve.

Using DNS to access a website
-----------------------------

Now that you have played a bit with deployed DNS servers and resolvers, we will now try to add a DNS entry that will point to some IP address and setup a website that can be reached through the added DNS entry.

We will create the website on ``pc2`` and we will call it ``helloworld.nanoinside.net``. You thus have to add a DNS entry so that ``helloworld.nanoinside.net`` points to the IP address of ``pc2``. See https://help.ubuntu.com/community/BIND9ServerHowto for a tutorial on how to configure ``bind9``.

Once the DNS entry is set up, it is time to configure the web server. ``Apache2`` is installed. See http://tuxtweaks.com/2009/07/how-to-configure-apache-linux/ for a tutorial. The final goal is to see "Hello world !" when accessing the website:

 .. code-block:: console

    $ curl -s helloworld.nanoinside.net
    Hello world !

The configuration files of apache are located in ``/etc/apache2/``

Enjoy !

.. rubric:: Footnotes

.. [#fimage] The image that we use is a custom Netkit_ filesystem with a recent 64 bits Linux kernel. If you wish to test it on your own Linux machine, you can install Netkit_ as explained on http://wiki.netkit.org/ and download the filesystem and kernel images from http://cnp3book.info.ucl.ac.be/netkit/netkit-images.zip  Note that this archive has a compressed size of more than 1 GByte ! 

.. [#fdnslab] The files used by the DNS lab are available from :download:`/netkit/netkit-lab_dns.zip` if you would like to use them on your laptop.

.. include:: /links.rst
