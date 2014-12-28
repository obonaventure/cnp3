.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. index:: UDP
.. _UDP:

The User Datagram Protocol
==========================

The User Datagram Protocol (UDP) is defined in :rfc:`768`. It provides an unreliable connectionless transport service on top of the unreliable network layer connectionless service. The main characteristics of the UDP service are :

 - the UDP service cannot deliver SDUs that are larger than 65467 bytes [#fmtuudp]_ 
 - the UDP service does not guarantee the delivery of SDUs (losses and desequencing can occur)
 - the UDP service will not deliver a corrupted SDU to the destination

Compared to the connectionless network layer service, the main advantage of the UDP service is that it allows several applications running on a host to exchange SDUs with several other applications running on remote hosts. Let us consider two hosts, e.g. a client and a server. The network layer service allows the client to send information to the server, but if an application running on the client wants to contact a particular application running on the server, then an additional addressing mechanism is required other than the IP address that identifies a host, in order to differentiate the application running on a host. This additional addressing is provided by `port numbers`. When a server using UDP is enabled on a host, this server registers a `port number`. This `port number` will be used by the clients to contact the server process via UDP. 

The figure below shows a typical usage of the UDP port numbers. The client process uses port number `1234` while the server process uses port number `5678`. When the client sends a request, it is identified as originating from port number `1234` on the client host and destined to port number `5678` on the server host. When the server process replies to this request, the server's UDP implementation will send the reply as originating from port  `5678` on the server host and destined to port `1234` on the client host.

.. figure:: /../book/transport/svg/udp-ports.png
   :align: center
   :scale: 70 

   Usage of the UDP port numbers

.. index:: UDP segment



UDP uses a single segment format shown in the figure below. 

.. figure:: /../book/transport/pkt/udp.png
   :align: center
   :scale: 100

   UDP Header Format

The UDP header contains four fields :

 - a 16 bits source port
 - a 16 bits destination port
 - a 16 bits length field 
 - a 16 bits checksum

As the port numbers are encoded as a 16 bits field, there can be up to only 65535 different server processes that are bound to a different UDP port at the same time on a given server. In practice, this limit is never reached. However, it is worth noticing that most implementations divide the range of allowed UDP port numbers into three different ranges :

 - the privileged port numbers (1 < port < 1024 )
 - the ephemeral port numbers ( officially [#fephemeral]_ 49152 <= port <= 65535 )
 - the registered port numbers (officially 1024 <= port < 49152)

In most Unix variants, only processes having system administrator privileges can be bound to port numbers smaller than `1024`. Well-known servers such as :term:`DNS`, :term:`NTP` or :term:`RPC` use privileged port numbers. When a client needs to use UDP, it usually does not require a specific port number. In this case, the UDP implementation will allocate the first available port number in the ephemeral range. The range of registered port numbers should be used by servers. In theory, developers of network servers should register their port number officially through IANA, but few developers do this. 

.. mention inetd and super servers somewhere ?

.. index:: UDP Checksum, Checksum computation

.. note:: Computation of the UDP checksum

 The checksum of the UDP segment is computed over :
 
  - a pseudo header :rfc:`2460` containing the source address, the destination address, the packet length encoded as a 32 bits number and a 32 bits bit field containing the three most significant bytes set to 0 and the low order byte set to 17
  - the entire UDP segment, including its header

 This pseudo-header allows the receiver to detect errors affecting the source or destination addresses placed in the IP layer below. This is a violation of the layering principle that dates from the time when UDP and IP were elements of a single protocol. It should be noted that if the checksum algorithm computes value '0x0000', then value '0xffff' is transmitted. A UDP segment whose checksum is set to '0x0000' is a segment for which the transmitter did not compute a checksum upon transmission. Some :term:`NFS` servers chose to disable UDP checksums for performance reasons when running over IPv4, but this caused `problems <http://lynnesblog.telemuse.net/192>`_ that were difficult to diagnose. Over IPv6, the UDP checksum cannot be disabled. A detailed discussion of the implementation of the Internet checksum may be found in :rfc:`1071`


Several types of applications rely on UDP. As a rule of thumb, UDP is used for applications where delay must be minimised or losses can be recovered by the application itself. A first class of the UDP-based applications are applications where the client sends a short request and expects a quick and short answer. The :term:`DNS` is an example of a UDP application that is often used in the wide area. However, in local area networks, many distributed systems rely on Remote Procedure Call (:term:`RPC`) that is often used on top of UDP. In Unix environments, the Network File System (:term:`NFS`) is built on top of RPC and runs frequently on top of UDP. A second class of UDP-based applications are the interactive computer games that need to frequently exchange small messages, such as the player's location or their recent actions. Many of these games use UDP to minimise the delay and can recover from losses. A third class of applications are multimedia applications such as interactive Voice over IP or interactive Video over IP. These interactive applications expect a delay shorter than about 200 milliseconds between the sender and the receiver and can recover from losses directly inside the application. 



.. rubric:: Footnotes


.. [#fmtuudp] This limitation is due to the fact that the network layer cannot transport packets that are larger than 64 KBytes. As UDP does not include any segmentation/reassembly mechanism, it cannot split a SDU before sending it. The UDP header consumes 8 bytes and the IPv6 header 60. With IPv4, the IPv4 header only consumes 20 bytes and thus the maximum UDP payload size is 65507 bytes.

.. [#fportnum] The complete list of allocated port numbers is maintained by IANA_ . It may be downloaded from http://www.iana.org/assignments/port-numbers

.. [#fephemeral] A discussion of the ephemeral port ranges used by different TCP/UDP implementations may be found in http://www.ncftp.com/ncftpd/doc/misc/ephemeral_ports.html


.. include:: /links.rst
