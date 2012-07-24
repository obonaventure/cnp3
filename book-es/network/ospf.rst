.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. index:: OSPF, Open Shortest Path First

OSPF
----

.. Link-state routing protocols are used in IP networks. Open Shortest Path First (OSPF), defined in :rfc:`2328`, is the link state routing protocol that has been standardised by the IETF. The last version of OSPF, which supports IPv6, is defined in :rfc:`5340`. OSPF is frequently used in enterprise networks and in some ISP networks. However, ISP networks often use the IS-IS link-state routing protocol [ISO10589]_ , which was developed for the ISO CLNP protocol but was adapted to be used in IP :rfc:`1195` networks before the finalisation of the standardisation of OSPF. A detailed analysis of ISIS and OSPF may be found in [BMO2006]_ and [Perlman2000]_.  Additional information about OSPF may be found in [Moy1998]_.

En las redes IP se usan protocolos de ruteo de estado de enlace. El protocolo OSPF (`Open Shortest Path First`), definido en  :rfc:`2328`, es el protocolo de estado de enlace que ha sido estandarizado por IETF. La última versíon de OSPF, que soporta IPv6, está definida en :rfc:`5340`. Con frecuencia, OSPF se usa en redes corporativas y en algunas redes de proveedores de servicio de Internet. Sin embargo, las redes de ISPs a menudo usan el protocolo de estado de enlace IS-IS[ISO10589]_ , que fue desarrollado para el protocolo CLNP de la ISO, pero fue adaptado para ser usado en redes IP :rfc:`1195` antes de terminar la estandarización de OSPF. Se encuentra un análisis detallado de  ISIS y OSPF en [BMO2006]_ y [Perlman2000]_.  Más información sobre OSPF en [Moy1998]_.

.. index:: OSPF area

.. Compared to the basics of link-state routing protocols that we discussed in section :ref:`linkstate`, there are some particularities of OSPF that are worth discussing. First, in a large network, flooding the information about all routers and links to thousands of routers or more may be costly as each router needs to store all the information about the entire network. A better approach would be to introduce hierarchical routing. Hierarchical routing divides the network into regions. All the routers inside a region have detailed information about the topology of the region but only learn aggregated information about the topology of the other regions and their interconnections. OSPF supports a restricted variant of hierarchical routing. In OSPF's terminology, a region is called an `area`. 

En comparación con lo básico de los protocolos de estado de enlace que hemos discutido en la sección :ref:`linkstate`, existen algunas particularidades de OSPF que vale la pena discutir. En primer lugar, en una red grande, inundar la información sobre todos los routers y enlaces hacia miles de routers, o más, puede ser sumamente costoso, ya que cada router necesita almacenar toda la información sobre la red completa. Un mejor enfoque puede ser la introducción de ruteo jerárquico. El ruteo jerárquico divide la red en regiones. Todos los routers dentro de una región tienen información detallada sobre la topología de la región, pero sólo aprenden información agregada sobre la topología de las demás regiones  y sus interconexiones. OSPF soporta una variante restringida del ruteo jerárquico. En la terminología de OSPF, una región recibe el nombre de `área`.

.. OSPF imposes restrictions on how a network can be divided into areas. An area is a set of routers and links that are grouped together. Usually, the topology of an area is chosen so that a packet sent by one router inside the area can reach any other router in the area without leaving the area [#fvirtual]_ . An OSPF area contains two types of routers :rfc:`2328`: 

.. - Internal router : A router whose directly connected networks belong to the area 
.. - Area border routers : A router that is attached to several areas.  

OSPF impone restricciones sobre cómo puede dividirse una red en áreas. Un área es un conjunto de routers y redes que están agrupados.  Generalmente, la topología de un área se elige de manera que un paquete enviado por un router dentro de un área puede alcanzar a cualquier otro router en el área sin abandonarla [#fvirtual]_ . Un área OSPF contiene dos tipos de routers :rfc:`2328`: 

 - Routers internos: Routers cuyas redes directamente conectadas pertenecen al área.
 - Routers de borde de área: Routers que están conectados a varias áreas.

.. For example, the network shown in the figure below has been divided into three areas : `area 1`, containing routers `R1`, `R3`, `R4`, `R5` and `RA`, `area 2` containing `R7`, `R8`, `R9`, `R10`, `RB` and `RC`. OSPF areas are identified by a 32 bit integer, which is sometimes represented as an IP address. Among the OSPF areas, `area 0`, also called the `backbone area` has a special role. The backbone area groups all the area border routers (routers `RA`, `RB` and `RC` in the figure below) and the routers that are directly connected to the backbone routers but do not belong to another area (router `RD` in the figure below). An important restriction imposed by OSPF is that the path between two routers that belong to two different areas (e.g. `R1` and `R8` in the figure below) must pass through the backbone area.

Por ejemplo, la red mostrada en la siguiente figura ha sido dividida en tres áreas: `area 1`, conteniendo los routers  `R1`, `R3`, `R4`, `R5` y `RA`, `area 2` conteniendo a `R7`, `R8`, `R9`, `R10`, `RB` y `RC`. Las áreas OSPF se identifican con un entero de 32 bits, que a veces se repreenta como una dirección IP. Entre las áreas OSPF, el `area 0`, también llamada el `área de backbone` o `backbone area` tiene un rol especial. El área de backbone agrupa a todos los routers de borde  (routers `RA`, `RB` y `RC` en la figura siguiente) y a los routers que están directamente conectados a los routers de backbone pero no pertenecen a otra área (el router `RD` en la figura siguiente). Una restricción importante impuesta por OSPF es que el camino entre dos routers que pertenecen a dos diferentes áreas (por ejemplo, `R1` y `R8` en la figura siguiente) debe pasar por el área de backbone.


.. figure:: png/network-fig-100-c.png
   :align: center
   :scale: 70
   
   Áreas OSPF
.. OSPF areas 

.. Inside each non-backbone area, routers distribute the topology of the area by exchanging link state packets with the other routers in the area. The internal routers do not know the topology of other areas, but each router knows how to reach the backbone area. Inside an area, the routers only exchange link-state packets for all destinations that are reachable inside the area. In OSPF, the inter-area routing is done by exchanging distance vectors. This is illustrated by the network topology shown below.

Dentro de cada área excepto la de backbone, los routers distribuyen la topología del área intercambiando paquetes de estado de enlace con los demás routers del área. Los routes internos no conocen la topología de las otras áreas, pero cada router sabe cómo alcanzar al área de backbone. Dentro de un área, los routers sólo intercambian paquetes de estado de enlace para todos los destinos que son alcanzables dentro del área. En OSPF, el ruteo inter-área se hace intercambiando vectores de distancia. Esto se ilustra en la topología de red que se muestra más abajo.


.. figure:: png/network-fig-102-c.png
   :align: center
   :scale: 70
  
   Ruteo jerárquico con OSPF 
..   Hierarchical routing with OSPF 

.. Let us first consider OSPF routing inside `area 2`. All routers in the area learn a route towards `192.168.1.0/24` and `192.168.10.0/24`. The two area border routers, `RB` and `RC`, create network summary advertisements. Assuming that all links have a unit link metric, these would be:
  
.. - `RB` advertises `192.168.1.0/24` at a distance of `2` and `192.168.10.0/24` at a distance of `3`
.. - `RC` advertises `192.168.1.0/24` at a distance of `3` and `192.168.10.0/24` at a distance of `2`

Consideremos primero el ruteo OSPF dentro del `area 2`. Todos los routers en el área aprenden rutas hacia `192.168.1.0/24` y hacia `192.168.10.0/24`. Los dos routers de borde, `RB` y `RC`, crean anuncios de resumen de red. Suponiendo que todos los enlaces tengan una métrica de enlace unitaria, éstos serían:

  
 - `RB` anuncia `192.168.1.0/24` a una distancia de `2` y `192.168.10.0/24` a una distancia de  `3`
 - `RC` anuncia `192.168.1.0/24` a una distancia de `3` y `192.168.10.0/24` a una distancia de  `2`

.. These summary advertisements are flooded through the backbone area attached to routers `RB` and `RC`. In its routing table, router `RA` selects the summary advertised by `RB` to reach `192.168.1.0/24` and the summary advertised by `RC` to reach `192.168.10.0/24`. Inside `area 1`, router `RA` advertises a summary indicating that `192.168.1.0/24` and `192.168.10.0/24` are both at a distance of `3` from itself.

Estos anuncios de resumen se inundan a través del área de backbone conectada a los routers `RB` y `RC`. En su tabla de ruteo, el router `RA` selecciona el resumen anunciado por `RB` para alcanzar a `192.168.1.0/24`, y el resumen anunciado por `RC` para alcanzar `192.168.10.0/24`. Dentro del `area 1`, el router `RA` anuncia un resumen indicando que `192.168.1.0/24` y `192.168.10.0/24` están ambas a una distancia de `3` de sí mismo.

.. On the other hand, consider the prefixes `10.0.0.0/24` and `10.0.1.0/24` that are inside `area 1`. Router `RA` is the only area border router that is attached to this area. This router can create two different network summary advertisements :

.. - `10.0.0.0/24` at a distance of `1` and `10.0.1.0/24` at a distance of `2` from `RA`
.. - `10.0.0.0/23` at a distance of `2` from `RA`

Por otro lado, consideremos los prefijos `10.0.0.0/24` y `10.0.1.0/24` que están dentro de `area 1`. El router `RA` es el único router de borde que está conectado a esta área. Este router puede crear dos diferentes anuncios de resumen de redes:

 - `10.0.0.0/24` a una distancia de `1` y `10.0.1.0/24` a una distancia de `2` de `RA`
 - `10.0.0.0/23` a una distancia de `2` de `RA`


.. The first summary advertisement provides precise information about the distance used to reach each prefix. However, all routers in the network have to maintain a route towards `10.0.0.0/24` and a route towards `10.0.1.0/24` that are both via router `RA`. The second advertisement would improve the scalability of OSPF by reducing the number of routes that are advertised across area boundaries. However, in practice this requires manual configuration on the border routers.

El primer anuncio de resumen provee información precisa sobre la distancia usada para alcanzar cada prefijo. Sin embargo, todos los routers en la red deben mantener una ruta hacia `10.0.0.0/24` y una ruta hacia `10.0.1.0/24` que pasan, ambas, por el router `RA`. El segundo anuncio mejoraría la escalabilidad de OSPF al reducir el número de rutas que se anuncian a través de las fronteras de área. Sin embargo, en la práctica esto requiere configuración manual de los routers de frontera.

.. index:: OSPF Designated Router

.. The second OSPF particularity that is worth discussing is the support of Local Area Networks (LAN). As shown in the example below, several routers may be attached to the same LAN.

La segunda particularidad de OSPF que vale la pena discutir es el soporte de redes de área local (LAN). Como se muestra en el ejemplo más abajo, varios routers pueden estar conectados a la misma LAN.

.. figure:: png/network-fig-096-c.png
   :align: center
   :scale: 70
   
   Una LAN OSPF conteniendo varios routers
..   An OSPF LAN containing several routers


.. A first solution to support such a LAN with a link-state routing protocol would be to consider that a LAN is equivalent to a full-mesh of point-to-point links as if each router can directly reach any other router on the LAN. However, this approach has two important drawbacks :

.. #. Each router must exchange HELLOs and link state packets with all the other routers on the LAN. This increases the number of OSPF packets that are sent and processed by each router.
.. #. Remote routers, when looking at the topology distributed by OSPF, consider that there is a full-mesh of links between all the LAN routers. Such a full-mesh implies a lot of redundancy in case of failure, while in practice the entire LAN may completely fail. In case of a failure of the entire LAN, all routers need to detect the failures and flood link state packets before the LAN is completely removed from the OSPF topology by remote routers. 

Una primera solución para soportar dicha LAN con un protocolo de ruteo de estado de enlace sería considerar que una LAN es equivalente a una trama completa de enlaces punto a punto, como si cada router pudiera alcanzar directamente a cada otro router sobre la LAN. Sin embargo, este enfoque tiene dos importantes desventajas:

 #. Cada router debe intercambiar paquetes HELLO y de estado de enlace con todos los demás routers de la LAN. Esto incrementa el número de paquetes OSPF que son enviados y procesados por cada router.
 #. Los routers remotos, al ver la topología distribuida por OSPF, consideran que existe una trama completa de enlaces entre todos los routers de la LAN. Dicha trama completa implica mucha redundancia en caso de falla, mientras que en la práctica la LAN completa puede fallar completamente. En caso de una falla de la LAN completa, todos los routers necesitan detectar la falla e inundar paquetes de estado de enlace antes de que la LAN sea completamente retirada de la topología OSPF por los routers remotos.


.. To better represent LANs and reduce the number of OSPF packets that are exchanged, OSPF handles LAN differently. When OSPF routers boot on a LAN, they elect [#felection]_ one of them as the `Designated Router (DR)` :rfc:`2328`. The `DR` router `represents` the local area network, and advertises the LAN's subnet (`138.48.4.0/24` in the example above). Furthermore, LAN routers only exchange HELLO packets with the `DR`. Thanks to the utilisation of a `DR`, the topology of the LAN appears as a set of point-to-point links connected to the `DR` as shown in the figure below. 

Para representar mejor las LANs y reducir el número de paquetes OSPF que son intercambiados, OSPF maneja las LANs en forma diferente. Cuando los routers OSPF arrancan en una LAN,  eligen [#felection]_ uno de ellos como `router designado` (`Designated Router, DR)` :rfc:`2328`. El router `DR` `representa` la red de área local, y anuncia la subred de la LAN (`138.48.4.0/24` en el ejemplo anterior). Además, los routers de la LAN sólo intercambian paquetes HELLO con el `DR`. Gracias a la utilización de un `DR`, la topología de la LAN aparece como un conjunto de enlaces punto a punto conectados al `DR`, como muestra la figura siguiente.

.. figure:: png/network-fig-099-c.png
   :align: center
   :scale: 70
   
   Representación OSPF de una LAN
..   OSPF representation of a LAN

.. tp: :rfc:`2991` ECMP

.. .. note:: How to quickly detect a link failure ?

.. Network operators expect an OSPF network to be able to quickly recover from link or router failures [VPD2004]_. In an OSPF network, the recovery after a failure is performed in three steps [FFEB2005]_ :

.. - the routers that are adjacent to the failure detect it quickly. The default solution is to rely on the regular exchange of HELLO packets. However, the interval between successive HELLOs is often set to 10 seconds... Setting the HELLO timer down to a few milliseconds is difficult as HELLO packets are created and processed by the main CPU of the routers and these routers cannot easily generate and process a HELLO packet every millisecond on each of their interfaces. A better solution is to use a dedicated failure detection protocol such as the Bidirectional Forwarding Detection (BFD) protocol defined in [KW2009]_ that can be implemented directly on the router interfaces. Another solution to be able to detect the failure is to instrument the physical and the datalink layer so that they can interrupt the router when a link fails. Unfortunately, such a solution cannot be used on all types of physical and datalink layers.
..  - the routers that have detected the failure flood their updated link state packets in the network
..  - all routers update their routing table 

.. note:: ¿Cómo detectar un fallo de red con rapidez?

 Los operadores de redes esperan que una red OSPF sea capaz de recuperarse rápidamente de fallos de enlaces o routers [VPD2004]_. En una red OSPF, la recuperación luego de un fallo se ejecuta en tres etapas [FFEB2005]_:

  - Los routers adyacentes al fallo lo detectan rápidamente. La solución por defecto es descansar sobre el intercambio periódico de paquetes. Sin embargo, el intervalo entre HELLOs sucesivos con frecuencia se fija a segundos... Bajar el tiempo del timer de HELLO a unos pocos milisegundos es difícil, ya que los paquetes HELLO son creados y procesados por la CPU principal de los routers, y estos routers no pueden generar y procesar fácilmente los paquetes HELLO a cada milisegundo en cada una de sus interfaces. Una solución mejor es usar un protocolo dedicado de detección de fallos como `BFD` (`Bidirectional Forwarding Detection`), definido en [KW2009]_, que pueda ser implementado directamente en las interfaces de los routers. Otra solución para poder detectar el fallo es instrumentar las capas física y de enlace de datos de manera que puedan interrumpir al router cuando falla un enlace. Desafortunadamente, dicha solución no puede ser usada en todos los tipos de capas físicas y de enlace de datos.
  - Los routers que han detectado el fallo inundan la red con sus paquetes de estado de enlace actualizado.
  - Todos los routes actualizan su tabla de ruteo.


.. rubric:: Footnotes


.. .. [#fvirtual] OSPF can support `virtual links` to connect routers together that belong to the same area but are not directly connected. However, this goes beyond this introduction to OSPF.
.. [#fvirtual] OSPF puede soportar `enlaces virtuales` para interconectar routers que pertenecen a la misma área pero no están directamente conectados. Sin embargo, el tema excede esta introducción a OSPF.

.. .. [#felection] The OSPF Designated Router election procedure is defined in :rfc:`2328`. Each router can be configured with a router priority that influences the election process since the router with the highest priority is preferred when an election is run.
.. [#felection] El procedimiento de OSPF para la elección del Router Designado se define en :rfc:`2328`. Cada router puede ser configurado con una prioridad de router que tiene influencia sobre el proceso de elección, ya que el router con la más alta prioridad es el preferido cuando se celebra una elección.

