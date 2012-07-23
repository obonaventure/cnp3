.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. _chapter-network: 

==============
La Capa de Red
==============

.. The transport layer enables the applications to efficiently and reliably exchange data. Transport layer entities expect to be able to send segment to any destination without having to understand anything about the underlying subnetwork technologies. Many subnetwork technologies exist. Most of them differ in subtle details (frame size, addressing, ...). The network layer is the glue between these subnetworks and the transport layer. It hides to the transport layer all the complexity of the underlying subnetworks and ensures that information can be exchanged between hosts connected to different types of subnetworks.

La capa de Transporte habilita a las aplicaciones para intercambiar datos eficiente y confiablemente. Las entidades de capa de Transporte esperan poder enviar segmentos a cualquier destino sin tener que entender nada de las tecnologías subyacentes. Existen muchas tecnologías de infraestructura por debajo de la capa de Red. La mayoría de ellas difieren en detalles sutiles (tamaño de trama, direccionamiento...). La capa de Red es el adhesivo entre estas sub-redes y la capa de Transporte. Esconde toda la complejidad de las capas subyacentes y asegura que la información pueda ser intercambiada entre los hosts conectados a diferentes tipos de sub-redes.

.. In this chapter, we first explain the principles of the network layer. These principles include the datagram and virtual circuit modes, the separation between the data plane and the control plane and the algorithms used by routing protocols. Then, we explain, in more detail, the network layer in the Internet, starting with IPv4 and IPv6 and then moving to the routing protocols (RIP, OSPF and BGP).

En este capítulo explicaremos primeramente los principios de la capa de Red. Estos principios incluyen los modos de datagramas y de circuitos virtuales, la separación entre el plano de datos y el plano de control, y los algoritmos usados por los protocolos de ruteo. Luego explicaremos en mayor detalle la capa de Red en Internet, comenzando con IPv6 e IPv4 y pasando a los protocolos de ruteo (RIP, OSPF y BGP).

.. include:: principles.rst


El Protocolo de Internet 
########################

.. The Internet Protocol (IP) is the network layer protocol of the TCP/IP protocol suite. IP allows the applications running above the transport layer (UDP/TCP) to use a wide range of heterogeneous datalink layers. IP was designed when most point-to-point links were telephone lines with modems. Since then, IP has been able to use Local Area Networks (Ethernet, Token Ring, FDDI, ...), new wide area data link layer technologies (X.25, ATM, Frame Relay, ...) and more recently wireless networks (802.11, 802.15, UMTS, GPRS, ...). The flexibility  of IP and its ability to use various types of underlying data link layer technologies is one of its key advantages.

El protocolo de Internet (`Internet Protocol`, IP) es el protocolo de la capa de Red del conjunto de protocolos TCP/IP. IP permite a las aplicaciones que corren sobre la capa de transporte (UDP/TCP) usar una amplia gama de capas de enlace de datos heterogéneas. IP fue diseñado cuando la mayoría de los enlaces punto a punto eran líneas telefónicas con modems. Desde entonces, IP ha sido capaz de usar redes de área local (Ethernet, Token Ring, FDDI, ...), nuevas tecnologías de capa de Enlace de área extendida (X.25, ATM, Frame Relay, ...) y más recientemente, redes inalámbricas (802.11, 802.15, UMTS, GPRS, ...). La flexibilidad de IP y su capacidad de usar varios tipos de tecnologías subyacentes de capa de Enlace de datos es una de sus ventajas clave. 

.. figure:: svg/ip-ref.png
   :align: center
   :scale: 70

   IP y el modelo de referencia
..   IP and the reference model

.. there is a draft on expectations of lower layer

.. The current version of IP is version 4 specified in :rfc:`791`. We first describe this version and later explain IP version 6, which is expected to replace IP version 4 in the not so distant future.

La versión actual de IP es la versión 4 especificada en :rfc:`791`. Primeramente describiremos esta versión y luego explicaremos IP versión 6, que se espera reemplace a la versión 4 en un futuro no muy distante.

.. include:: ipv4.rst

.. include:: ipv6.rst

.. include:: middleboxes.rst


.. Routing in IP networks
Ruteo en Redes IP
#################

.. In a large IP network such as the global Internet, routers need to exchange routing information. The Internet is an interconnection of networks, often called domains, that are under different responsibilities. As of this writing, the Internet is composed on more than 30,000 different domains and this number is still growing. A domain can be a small enterprise that manages a few routers in a single building, a larger enterprise with a hundred routers at multiple locations, or a large Internet Service Provider managing thousands of routers. Two classes of routing protocols are used to allow these domains to efficiently exchange routing information. 

En una red IP grande, como la Internet global, los routers necesitan intercambiar información de ruteo. Internet es una interconexión de redes, a veces llamadas dominios, que están bajo diferentes responsabilidades. Al escribir estas líneas, Internet se compone de más de 30.000 diferentes dominios, y este número sigue en alza. Un dominio puede ser una pequeña empresa que administra unos pocos routers en un solo edificio, una empresa mayor con cien routers en diferentes ubicaciones, o un gran proveedor de servicios de Internet (ISP) manejando miles de routers. Dos clases de protocolos de ruteo son las usadas para permitir a estos dominios intercambiar eficientemente la información de ruteo. 

.. figure:: png/network-fig-093-c.png
   :align: center
   :scale: 70
   
   Organización de una pequeña internet
..   Organisation of a small Internet


.. The first class of routing protocols are the `intradomain routing protocols` (sometimes also called the interior gateway protocols or :term:`IGP`). An intradomain routing protocol is used by all routers inside a domain to exchange routing information about the destinations that are reachable inside the domain. There are several intradomain routing protocols. Some domains use :term:`RIP`, which is a distance vector protocol. Other domains use link-state routing protocols such as :term:`OSPF` or :term:`IS-IS`. Finally, some domains use static routing or proprietary protocols such as :term:`IGRP` or :term:`EIGRP`.

La primera clase de protocolos de ruteo son los protocolos de ruteo `intradominio`, a veces llamados protocolos de gateway interior (`Interior Gateway Protocols`, :term:`IGP`). Todos los routers dentro de un dominio utilizan un protocolo de ruteo intradominio para intercambiar información de ruteo sobre los destinos que son alcanzables dentro del dominio. Existen varios protocolos de ruteo intradominio. Algunos dominios usan :term:`RIP`, que es un protocolo de vector de distancia. Otros dominios protocolos de ruteo de estado de enlace como :term:`OSPF` o :term:`IS-IS`. Finalmente, algunos dominios usan ruteo estático o protocolos propietarios como :term:`IGRP` o :term:`EIGRP`.

.. These intradomain routing protocols usually have two objectives. First, they distribute routing information that corresponds to the shortest path between two routers in the domain. Second, they should allow the routers to quickly recover from link and router failures.

Estos protocolos de ruteo intradominio generalmente tienen dos objetivos. Primero, distribuir información de ruteo que corresponda al camino más corto entre dos routers en el dominio. Segundo, permitir a los routers recuperarse rápidamente de las fallas de enlaces y de routers. 

.. The second class of routing protocols are the `interdomain routing protocols` (sometimes also called the exterior gateway protocols or :term:`EGP`). The objective of an interdomain routing protocol is to distribute routing information between domains. For scalability reasons, an interdomain routing protocol must distribute aggregated routing information and considers each domain as a black box.

La segunda clase de protocolos de ruteo son los protocolos de ruteo `interdominio`, a veces llamados protocolos de gateway exterior (`Exterior Gateway Protocols`, :term:`EGP`). El objetivo de un protocolo de ruteo interdominio es distribuir información de ruteo entre dominios. Por razones de escalabilidad, un protocolo interdominio debe distribuir información de ruteo resumida (`aggregated`) y considera a cada dominio como una caja negra.

.. A very important difference between intradomain and interdomain routing are the `routing policies` that are used by each domain. Inside a single domain, all routers are considered equal, and when several routes are available to reach a given destination prefix, the best route is selected based on technical criteria such as the route with the shortest delay, the route with the minimum number of hops or the route with the highest bandwidth.
Una diferencia muy importante entre ruteo intradominio e interdominio son las `políticas de ruteo` que se usan en cada dominio. Dentro de un único dominio, todos los routers se consideran iguales, y cuando hay varias rutas disponibles para alcanzar un prefijo destino dado, se selecciona la mejor ruta con base en criterios técnicos tales como cuál es la ruta con la demora más corta, la ruta con el menor número de saltos, o la que tiene el ancho de banda más alto.


.. When we consider the interconnection of domains that are managed by different organisations, this is no longer true. Each domain implements its own routing policy. A routing policy is composed of three elements : an `import filter` that specifies which routes can be accepted by a domain, an `export filter` that specifies which routes can be advertised by a domain and a ranking algorithm that selects the best route when a domain knows several routes towards the same destination prefix. As we will see later, another important difference is that the objective of the interdomain routing protocol is to find the `cheapest` route towards each destination. There is only one interdomain routing protocol : :term:`BGP`.

Cuando consideramos la interacción de dominios que están administrados por diferentes organizaciones, esto ya no es así. Cada dominio implementa su propia política de ruteo. Una política de ruteo se compone de tres elementos: un filtro de importación (`import filter`) que especifica qué rutas pueden ser aceptadas por un dominio, un filtro de exportación (`export filter`) que especifica qué rutas pueden ser anunciadas por un dominio, y un algoritmo de ranking que, cuando un dominio conoce varias rutas hacia el mismo prefijo destino, selecciona la mejor. Como veremos luego, otra importante diferencia es que el objetivo del protocolo de ruteo interdominio es hallar la ruta más `barata` hacia cada destino. Existe sólo un protocolo de ruteo interdominio: :term:`BGP`.

.. Intradomain routing 
Ruteo intradominio
==================

.. In this section, we briefly describe the key features of the two main intradomain unicast routing protocols : RIP and OSPF.
En esta sección, describiremos brevemente las características clave de los dos principales protocolos de ruteo unicast intradominio: RIP y OSPF.  

.. include:: rip.rst

.. include:: ospf.rst

.. include:: bgp.rst

Resumen
#######


.. include:: exercises/ex-network.rst

.. include:: exercises/cha-network.rst



.. include:: ../links.rst

