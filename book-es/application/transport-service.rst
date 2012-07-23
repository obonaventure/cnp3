.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Servicios de transporte
=======================

.. Networked applications are built on top of the transport service. As explained in the previous chapter, there are two main types of transport services :

.. - the `connectionless` or `datagram` service
.. - the `connection-oriented` or `byte-stream` service

Las aplicaciones de red se construyen encima del servicio de transporte. Como se explicó en el capítulo anterior, hay dos tipos principales de servicios de transporte:

 - El servicio `sin conexión` o `de datagramas`
 - El servicio `orientado a conexión` o de `flujo de bytes`

.. The connectionless service allows applications to easily exchange messages or Service Data Units. On the Internet, this service is provided by the UDP protocol that will be explained in the next chapter. The connectionless transport service on the Internet is unreliable, but is able to detect transmission errors. This implies that an application will not receive an SDU that has been corrupted due to transmission errors. 

El servicio sin conexión permite a las aplicaciones fácilmente intercambiar mensajes o SDUs (`Service Data Units`). En Internet, este servicio es provisto por el protocolo UDP, que será explicado en el próximo capítulo. El servicio de transporte sin conexión en Internet es no confiable, pero es capaz de detectar errores de transmisión. Esto implica que una aplicación no recibirá una SDU que haya sido corrupta debido a errores de transmisión.

.. The connectionless transport service allows networked application to exchange messages. Several networked applications may be running at the same time on a single host. Each of these applications must be able to exchange SDUs with remote applications. To enable these exchanges of SDUs, each networked application running on a host is identified by the following information :

El servicio de transporte sin conexión permite a las aplicaciones de red intercambiar mensajes. Varias aplicaciones de red pueden estar corriendo al mismo tiempo en un mismo host. Cada una de estas aplicaciones debe ser capaz de intercambiar SDUs con aplicaciones remotas. Para habilitar estos intercambios de SDUs, cada aplicación de red corriendo en un host se identifica por la siguiente información:

.. - the `host` on which the application is running
.. - the `port number` on which the application `listens` for SDUs

 - El `host` donde corre la aplicación
 - El `número de puerto` sobre el cual la aplicación `escucha` la llegada de SDUs.

.. On the Internet, the `port number` is an integer and the `host` is identified by its network address. As we will see in chapter :ref:`chapter-network` there are two types of Internet Addresses :

.. - `IP version 4` addresses that are 32 bits wide
.. - `IP version 6` addresses that are 128 bits wide

En Internet, el `número de puerto` es un entero, y el `host` se identifica por su dirección de red. Como veremos en el capítulo :ref:`chapter-network`, existen dos tipos de direcciones de Internet:

 - Direcciones `IP versión 4` de 32 bits 
 - Direcciones `IP versión 6` de 128 bits 

.. IPv4 addresses are usually represented by using a dotted decimal representation where each decimal number corresponds to one byte of the address, e.g. `203.0.113.56`. IPv6 addresses are usually represented as a set of hexadecimal numbers separated by semicolons, e.g. `2001:db8:3080:2:217:f2ff:fed6:65c0`. Today, most Internet hosts have one IPv4 address. A small fraction of them also have an IPv6 address. In the future, we can expect that more and more hosts will have IPv6 addresses and that some of them will not have an IPv4 address anymore. A host that only has an IPv4 address cannot communicate with a host having only an IPv6 address. The figure below illustrates two that are using the datagram service provided by UDP on hosts that are using IPv4 addresses.

Las direcciones IPv4 generalmente se representan con una notación en decimal con puntos, donde cada número decimal corresponde a un byte de la dirección; por ejemplo, `203.0.113.56`. Las direcciones IPv6 generalmente se representan como un conjunto de números hexadecimales separados por dos puntos; por ejemplo, `2001:db8:3080:2:217:f2ff:fed6:65c0`. Hoy, la mayoría de los hosts en Internet tienen una dirección IPv4. Una pequeña fracción de ellos tiene también una dirección IPv6. En el futuro, es de esperar que más y más hosts tendrán direcciones IPv6, y que algunos de ellos dejarán de tener direcciones IPv4. Un host que sólo tiene dirección IPv4 no puede comunicarse con un host que tiene sólo IPv6. La figura a continuación ilustra dos aplicaciones que están usando el servicio de datagramas provisto por UDP sobre hosts que usan direcciones IPv4. 

.. figure:: png/app-fig-002-c.png
   :align: center
   :scale: 80 

   El servicio sin conexión o de datagramas
.. The connectionless or datagram service 

.. The second transport service is the connection-oriented service. On the Internet, this service is often called the `byte-stream service` as it creates a reliable byte stream between the two applications that are linked by a transport connection. Like the datagram service, the networked applications that use the byte-stream service are identified by the host on which they run and a port number. These hosts can be identified by an IPv4 address, an IPv6 address or a name. The figure below illustrates two applications that are using the byte-stream service provided by the TCP protocol on IPv6 hosts. The byte stream service provided by TCP is reliable and bidirectional. 

El segundo servicio de transporte es el orientado a conexión. En Internet, este servicio suele llamarse el `servicio de flujo de bytes` porque crea un flujo confiable de bytes entre las dos aplicaciones que están enlazadas por una conexión de transporte. Como en el servicio de datagramas, las aplicaciones de red que usan el servicio de flujo de bytes se identifican por el host donde se ejecutan, más un número de puerto. Estos hosts pueden identificarse con una dirección IPv4, una dirección IPv6 o un nombre. La figura siguiente ilustra dos aplicaciones que usan el servicio de flujo de bytes provisto por el protocolo TCP sobre hosts IPv6. El servicio de flujo de bytes provisto por TCP es confiable y bidireccional. 

.. figure:: png/app-fig-003-c.png
   :align: center
   :scale: 80 

   El servicio orientado a conexión, o de flujo de bytes
..   The connection-oriented or byte-stream service 
