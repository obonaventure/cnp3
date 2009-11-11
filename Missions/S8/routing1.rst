<<<<<<< .mine
A Network Address Translator
============================
=======
A NAT gateway.
========================
>>>>>>> .r66

The global Internet is a fully distributed and uncoordinated network.
Historically IP addresses were allocated in a first-come first-served basis. As
a consequence a quick shortage of IPv4 prefixes happened and people started
to have difficulties to obtain an address block. 
As a temporarily solution, IP Network Address
Translation (NAT) was designed to use private IPv4 addresses in corporate or home networks and to map and route them with public source addresses when packets are forwarded over the global Internet. 

In this exercise you'll implement a gateway that allows communications between
hosts that are using :rfc:`1918` private addresses in a private network and hosts that are using public IPv4 addresses. Your gateway will be a simplified version of the NAT box described in :rfc:`1631`. Compared to a real NAT, your NAT will ignore packet fragmentation, DNS and only support TCP. 

The deadline for this exercise is Tuesday November 17th, 13.00.

Lab preparation 
_______________

Before implementing a NAT in scapy_, you need to setup the emulated environment. You will use three virtual machines.
   
   * Your NAT box with 2 interfaces: `eth0` with a private IP address and `eth1` with a public IP address.

   * Host `H1` uses a private IPv4 address on `eth0`

   * Host `H2` uses a public IPv4 address  on `eth0` 

The different interfaces have been connected as follows :

 - `eth0` on NAT is connected to `eth0` on `H1`
 - `eth1` on NAT is connected to `eth0` on `H2`

`H1` and `H2` will use the standard IP implementation of the Linux kernel while `NAT` will use your 
implementation written in scapy_. You will use the emulated network to send and receive public and private IP packets.

The filesystems and the kernel of the virtual machines are stored
in the directory `/etinfo/INGI2141/uml/nat`. To create the
virtual setup illustrated on the figure execute the following procedure:

#. Copy the boot script of `H1`,`H2` and `NAT` virtual machines in your working directory ::

	cp /etinfo/INGI2141/uml/nat/start_h1 ~/INGI2141/UML/NAT
	cp /etinfo/INGI2141/uml/nat/start_h2 ~/INGI2141/UML/NAT
	cp /etinfo/INGI2141/uml/nat/start_nat ~/INGI2141/UML/NAT

#. Open 3 terminals, 1 for each virtual machine 

#. In the first terminal, start the virtual machine `H1` by executing
   the script `start_h1`. 
   In the second terminal, start the virtual machine
   `H2` by executing the script `start_h2`. In the third
   terminal start the virtual machine `NAT` by executing the script `start_nat`

<<<<<<< .mine
#. The interfaces of your boxes have already been configured with the following IPv4 addresses :
=======
#. The interfaces of your boxes are configured with 
the following IPv4 addresses :
>>>>>>> .r66

 - `192.168.1.2/24` on `eth0` on `H1` 
 - `192.168.1.1/24` on `eth0` on `NAT` 
 - `216.239.59.104/24` on `eth1` on `NAT` 
 - `216.239.59.103/24` on `eth1` on `H2` 

#. Check the IP connectivity between `H1` and `NAT` and `H2` and `NAT` by
   using :manpage:`ping(8)` 

You need to configure the routing table on `H1` so that all packets with a destination in 
the public network will be sent via `NAT`. This is can be achieved by adding a default route. To do this use the following command on `H1` ::

  ip route add default gw 192.168.1.1

Your NAT will only support TCP. To ensure that the Linux kernel on `NAT` does not intercept the packets that you will process in scapy_, you need to configure the following filters on `NAT`:: 

   iptables -A INPUT -p ip -i eth1 -j DROP
   iptables -A OUTPUT -p ip -o eth1 -j DROP
   iptables -A INPUT -p ip -i eth0 -j DROP
   iptables -A OUTPUT -p ip -o eth0 -j DROP

To check that your NAT implementation is functioning you 
need to start on a TCP server on `H2`. For this, you can use the 
simple python_ server in file `/root/srv-tcp.py` on `H2`. This server
waits for a TCP connection on the port specified as the first argument.

On `H1` you can use :manpage:`telnet(1)` to contact this server or use the python client in file `/root/cl-tcp.py` 


Implementation issues in scapy_
-------------------------------

To implement a NAT in scapy_, you already know how to process IPv4 packets and TCP segments. To ease your implementation, assume none of the IPv4 packets that you will translate need to be fragmented.

The main difficulty when implementing a NAT is to select a data structure that contains the mapping between a `(private IPv4 address, TCP port)` and a `(public IPv4 address, TCP port)`. This data structure will be accessed every time you receive a packet from `H1` destined to a public IPv4 address, but also when a packet is received from `H2`. Note that, although the emulated network only contains two hosts, your implementation must support any number of hosts on both the private and the public sides.

To design your data structure, consider what happens when :
 
 - client `A` opens 100 TCP connections with different source ports to server `C` on destination port `80`
 - client `A` opens a TCP connection with `source port=1234` to servers `S1` and `S2` on destination port `1234`
 - clients `A` and `B` using private addresses open a TCP connection with `source port=1234` to servers `S1` on destination port `1234`


When implementing your NAT, you will need to solve three problems by using your data structure :

 1. When a packet is received from a private host, how do you translate it ? What happens if there is no suitable mapping entry in your NAT ?
 2. When a packet is received from a public host, how do you translate it ? What happens if there is no suitable mapping entry in your NAT ?
 3. A real NAT will have a finite memory. When do you remove a mapping entry in your data structure ? Discuss your design choice as comments in your code

As the `NAT` virtual machine has been configured with the appropriate IP addresses and routes, you can use the `send()` method to send IP packets in your NAT.

scapy_ allows you to modify any field in an IPv4 packet or TCP segment. For example, if `p` is a packet, you can use ::

       p[IP].dst='1.2.3.4'  # change destination address
       p[IP].chksum=None    # remove IP checksum, scapy_ will recompute it
       			    # when sending it with send()
       p[TCP].dport=1234    # change destination port number
       p[TCP].chksum=None   # remove TCP checksum, scapy will recompute it
       			    # when sending it with send()		     


To capture the packets to be processed by the NAT, you can use a `master_filter` such as the following one ::

	mac_addr_src = { "00:00:E3:00:30:04":'eth0', "00:00:E3:00:30:03":'eth1'}
	# verify that these are the hardware addresses of your NAT
	# with ifconfig

	def master_filter(self, pkt):
	    return( (TCP in pkt) and 
	    	   (not pkt.src.upper() in self.mac_addr_src.keys()) and
		   (not pkt.dst.upper() in self.mac_addr_dst.values()) )

.. note::

   If you create a new IP packet with scapy_, scapy_ sets the unspecified fields to a default value. When translating a packet, you should only change the fields of the IPv4 header and TCP header that need to be translated and leave the other fields unmodified. 


You have written enough scapy_ prototypes to be able to write your implementation without a skeleton.

.. include:: ../../book/links.rst
