.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. _chapter-datalink:

===========================================
Capa de Enlace y Redes de Área Local (LANs)
===========================================


.. The datalink layer is the lowest layer of the reference model that we discuss in detail. As mentioned previously, there are two types of datalink layers. The first datalink layers that appeared are the ones that are used on point-to-point links between devices that are directly connected by a physical link. We will briefly discuss one of these datalink layers in this chapter. The second type of datalink layers are the ones used in Local Area Networks (LANs). The main difference between the point-to-point and the LAN datalink layers is that the latter need to regulate the access to the Local Area Network which is usually a shared medium. 

La capa de Enlace es la capa más baja del modelo de referencia que discutiremos en detalle. Como se mencionó previamente, hay dos tipos de capas de enlace. Las primeras capas de enlace que aparecieron son las usadas en enlaces punto a punto, entre dispositivos que están directamente conectados por un vínculo físico. Discutiremos brevemente una de estas capas de enlace en este capítulo. El segundo tipo de capas de enlace son las usadas en las Redes de Área Local (LANs). La principal diferencia entre ambas capas es que la última necesita regular el acceso a la LAN, que generalmente es un medio compartido.

.. This chapter is organised as follows. We first discuss the principles of the datalink layer as well as the services that it uses from the physical layer. We then describe in more detail several Medium Access Control algorithms that are used in Local Area Networks to regulate the access to the shared medium. Finally we discuss in detail important datalink layer technologies with an emphasis on Ethernet and WiFi networks.

Este capítulo se organiza de la siguiente forma. Primero discutiremos los principios de la capa de enlace así como los servicios de la capa física que ésta utiliza. Luego describiremos con más detalle varios algoritmos de control de acceso al medio usados en LANs para regular el acceso al medio compartido. Finalmente discutiremos en detalle algunas tecnologías de capa de enlace importantes, con énfasis en Ethernet y redes WiFi.

.. include:: principles.rst

.. include:: technologies.rst




Resumen
#######

.. In this chapter, we first explained the principles of the datalink layer. There are two types of datalink layers : those used over point-to-point links and those used over Local Area Networks. On point-to-point links, the datalink layer must at least provide a framing technique, but some datalink layer protocols also include reliability mechanisms such as those used in the transport layer. We have described the Point-to-Point Protocol that is often used over point-to-point links in the Internet.

En este capítulo hemos explicado, primero, los principios de la capa de enlace de datos. Hay dos tipos de capa de enlace de datos: el usado sobre enlaces punto a punto y el usado sobre Redes de Área Local (LAN). En enlaces punto a punto, la capa de enlace de datos debe al menos ofrecer una técnica de `framing`, aunque algunos protocolos de esta capa también incluyen mecanismos de confiabilidad como los usados en la capa de transporte. Hemos descrito el Protocolo Punto a Punto (PPP) que se usa frecuentemente sobre vínculos punto a punto en Internet.

.. Local Area Networks pose a different problem since several devices share the same transmission channel. In this case, a Medium Access Control algorithm is necessary to regulate the access to the transmission channel because whenever two devices transmit at the same time a collision occurs and none of these frames can be decoded by their recipients. There are two families of MAC algorithms. The statistical or optimistic MAC algorithms reduce the probability of collisions but do not completely prevent them. With such algorithms, when a collision occurs, the collided frames must be retransmitted. We have described the operation of the ALOHA, CSMA, CSMA/CD and CSMA/CA MAC algorithms. Deterministic or pessimistic MAC algorithms avoid all collisions. We have described the Token Ring MAC where stations exchange a token to regulate the access to the transmission channel.

Las Redes de Área Local presentan un problema diferente, ya que varios dispositivos comparten el mismo canal de transmisión. En este caso, es necesario un algoritmo de Control de Acceso al Medio (MAC) para regular el acceso al canal de transmisión, ya que siempre que dos dispositivos transmitan al mismo tiempo ocurrirá una colisión, y entonces ninguna de las tramas podrá ser decodificada por su receptor. Hay dos familias de algoritmos MAC. Los estadísticos, u optimistas, reducen las probabilidades de colisiones, pero no las evitan completamente. Con tales algoritmos, cuando ocurra una colisión, las tramas colisionadas deberán ser retransmitidas. Hemos explicado la operación de los algoritmos MAC optimistas ALOHA, CSMA, CSMA/CD y CSMA/CA. Los algoritmos determinísticos o pesimistas evitan todas las colisiones. Hemos descrito el algoritmo MAC Token Ring, donde las estaciones intercambian un token para regular el acceso al canal de transmisión.

.. Finally, we have described in more detail two successful Local Area Network technologies : Ethernet and WiFi. Ethernet is now the de facto LAN technology. We have analysed the evolution of Ethernet including the operation of hubs and switches. We have also described the Spanning Tree Protocol that must be used when switches are interconnected. For the last few years, WiFi became the de facto wireless technology at home and inside enterprises. We have explained the operation of WiFi networks and described the main 802.11 frames.

Finalmente, hemos descrito en mayor detalle dos tecnologías LAN exitosas: Ethernet y WiFi. Ethernet es hoy la tecnología LAN `de facto`. Hemos analizado la evolución de Ethernet, incluyendo la operación de hubs y switches. También hemos descrito el protocolo STP, `Spanning Tree Protocol`, que debe ser usado cuando se interconectan switches. En los últimos años, WiFi se ha convertido en la tecnología inalámbrica de facto en ambientes domésticos y organizacionales. Hemos explicado la operación de las redes WiFi y hemos descrito las principales tramas 802.11.

.. include:: ../links.rst


.. include:: exercises/ex-lan.rst



