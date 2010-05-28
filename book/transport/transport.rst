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
   :scale: 70 

   The transport layer in the reference model


These imperfections of the connectionless network layer service will be better understood once we have explained the network layer in the next chapter. At this point, let us simply assume that these imperfections occur without trying to understand why they occur.

Some transport protocols can be used on top of a connection-oriented network service, such as class 0 of the ISO Transport Protocol (TP0) defined in [X224]_ , but they have not been widely used. We do not discuss such utilisation of a connection-oriented network service in more details in this book.

This chapter is organised as follows. We first explain how it is possible to provide a reliable transport service on top of an unreliable connectionless network service. For this, we explain the main mechanisms found in such protocols. Then, we study in details the two transport protocols that are used in the Internet. We begin with the User Datagram Protocol (UDP) that provides a simple connectionless transport service. Then, we describe the Transmission Control Protocol (TCP) in details, including its congestion control mechanism.

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


.. include:: ../links.rst

.. include:: exercises/ex-transport.rst

.. include:: exercises/cha-transport.rst




