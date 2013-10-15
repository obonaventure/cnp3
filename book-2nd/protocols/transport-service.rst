.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

*********************
The application layer
*********************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=5

Networked applications rely the transport service. As explained earlier, there are two main types of transport services :

 - the `connectionless` service
 - the `connection-oriented` or `byte-stream` service

The connectionless service allows applications to easily exchange messages or Service Data Units. On the Internet, this service is provided by the UDP protocol that will be explained in the next chapter. The connectionless transport service on the Internet is unreliable, but is able to detect transmission errors. This implies that an application will not receive data that has been corrupted due to transmission errors. 

The connectionless transport service allows networked application to exchange messages. Several networked applications may be running at the same time on a single host. Each of these applications must be able to exchange SDUs with remote applications. To enable these exchanges of SDUs, each networked application running on a host is identified by the following information :

 - the `host` on which the application is running
 - the `port number` on which the application `listens` for SDUs

On the Internet, the `port number` is an integer and the `host` is identified by its network address. There are two types of Internet Addresses :

 - `IP version 4` addresses that are 32 bits wide
 - `IP version 6` addresses that are 128 bits wide

IPv4 addresses are usually represented by using a dotted decimal representation where each decimal number corresponds to one byte of the address, e.g. `203.0.113.56`. IPv6 addresses are usually represented as a set of hexadecimal numbers separated by semicolons, e.g. `2001:db8:3080:2:217:f2ff:fed6:65c0`. Today, most Internet hosts have one IPv4 address. A small fraction of them also have an IPv6 address. In the future, we can expect that more and more hosts will have IPv6 addresses and that some of them will not have an IPv4 address anymore. A host that only has an IPv4 address cannot communicate with a host having only an IPv6 address. The figure below illustrates two that are using the datagram service provided by UDP on hosts that are using IPv4 addresses.


.. figure:: /../book/application/png/app-fig-002-c.png
   :align: center
   :scale: 80 

   The connectionless or datagram service 


.. note:: Textual representation of IPv6 addresses

 It is sometimes necessary to write IPv6 addresses in text format, e.g. when manually configuring addresses or for documentation purposes. The preferred format for writing IPv6 addresses is `x:x:x:x:x:x:x:x`, where the `x` 's are hexadecimal digits representing the eight 16-bit parts of the address. Here are a few examples of IPv6 addresses :

  - abcd:Eef01:2345:6789:abcd:ef01:2345:6789
  - 2001:db8:0:0:8:800:200c:417a
  - fe80:0:0:0:219:e3ff:fed7:1204

 IPv6 addresses often contain a long sequence of bits set to `0`. In this case, a compact notation has been defined. With this notation, `::` is used to indicate one or more groups of 16 bits blocks containing only bits set to `0`. For example, 
 
  - 2001:db8:0:0:8:800:200c:417a  is represented as  `2001:db8::8:800:200c:417a`
  - ff01:0:0:0:0:0:0:101   is represented as `ff01::101` 
  - 0:0:0:0:0:0:0:1 is represented as `::1`
  - 0:0:0:0:0:0:0:0 is represented as `\:\:`



The second transport service is the connection-oriented service. On the Internet, this service is often called the `byte-stream service` as it creates a reliable byte stream between the two applications that are linked by a transport connection. Like the datagram service, the networked applications that use the byte-stream service are identified by the host on which they run and a port number. These hosts can be identified by an address or a name. The figure below illustrates two applications that are using the byte-stream service provided by the TCP protocol on IPv6 hosts. The byte stream service provided by TCP is reliable and bidirectional. 


.. figure:: /../book/application/png/app-fig-003-c.png
   :align: center
   :scale: 80 

   The connection-oriented or byte-stream service 

