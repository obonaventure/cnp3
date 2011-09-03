.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

.. _chapter-transport:

=====================
 The transport layer
=====================


As the transport layer is built on top of the network layer, it is important to know the key features of the network layer service. There are two types of network layer services : connectionless and connection-oriented. The connectionless network layer service is the most widespread. Its main characteristics are :

 - the connectionless network layer service can only transfer SDUs of *limited size* [#fsize]_
 - the connectionless network layer service may discard SDUs
 - the connectionless network layer service may corrupt SDUs
 - the connectionless network layer service may delay, reorder or even duplicate SDUs


.. figure:: png/transport-fig-001-c.png
   :align: center
   :scale: 80 

   The transport layer in the reference model


These imperfections of the connectionless network layer service will become much clearer once we have explained the network layer in the next chapter. At this point, let us simply assume that these imperfections occur without trying to understand why they occur.

Some transport protocols can be used on top of a connection-oriented network service, such as class 0 of the ISO Transport Protocol (TP0) defined in [X224]_ , but they have not been widely used. We do not discuss in further detail such utilisation of a connection-oriented network service in this book.

This chapter is organised as follows. We will first explain how it is possible to provide a reliable transport service on top of an unreliable connectionless network service. For this, we explain the main mechanisms found in such protocols. Then, we will study in detail the two transport protocols that are used in the Internet. We begin with the User Datagram Protocol (UDP) which provides a simple connectionless transport service. Then, we will describe in detail the Transmission Control Protocol (TCP), including its congestion control mechanism.

.. rubric:: Footnotes

.. [#fsize] Many network layer services are unable to carry SDUs that are larger than 64 KBytes. 


.. include:: principles.rst

.. include:: udp.rst

.. include:: tcp.rst



.. dccp RFC 4340 :rfc:`4340`


.. Other transport protocols
.. =========================

.. stcp 
.. xtp 
.. dccp
.. rtp :rfc:`1889`
.. udplite :rfc:`3828`

Summary
#######

In this chapter, we have studied the transport layer. This layer provides two types of services to the application layer. The unreliable connectionless service is the simplest service offered to applications. On the Internet, this is the service offered by UDP. However, most applications prefer to use a reliable and connection-oriented transport service. We have shown that providing this service was much more complex than providing an unreliable service as the transport layer needs to recover from the errors that occur in the network layer. For this, transport layer protocols rely on several mechanisms. First, they use a handshake mechanism, such as the three-way handshake mechanism, to correctly establish a transport connection. Once the connection has been established, transport entities exchange segments. Each segment contains a sequence number, and the transport layer uses acknowledgements to confirm the segments that have been correctly received. In addition, timers are used to recover from segment losses and sliding windows are used to avoid overflowing the buffers of the transport entities. Finally, we explained how a transport connection can be safely released. We then discussed the mechanisms that are used in TCP, the reliable transport protocol, used by most applications on the Internet. Most notably, we described the congestion control mechanism that has been included in TCP since the late 1980s and explained how the reliability mechanisms used by TCP have been tuned over the years.




.. include:: ../links.rst

.. include:: exercises/ex-transport.rst

.. include:: exercises/cha-transport.rst




