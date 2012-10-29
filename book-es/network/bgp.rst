.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. Interdomain routing
Ruteo interdominios
===================

.. As explained earlier, the Internet is composed of more than 30,000 different networks [#fasnum]_ called `domains`. Each domain is composed of a group of routers and hosts that are managed by the same organisation. Example domains include belnet_, sprint_, level3_, geant_, abilene_, cisco_ or google_ ... 

Como se explicó anteriormente, Internet se compone de más de 30.000 diferentes redes [#fasnum]_ llamadas `dominios`. Cada dominio se compone de un grupo de routers y hosts que son administrados por la misma organización. Algunos dominios ejemplo son belnet_, sprint_, level3_, geant_, abilene_, cisco_ o google_ ... 

.. index:: stub domain, transit domain

.. Each domain contains a set of routers. From a routing point of view, these domains can be divided into two classes : the `transit` and the `stub` domains. A `stub` domain sends and receives packets whose source or destination are one of its own hosts. A `transit` domain is a domain that provides a transit service for other domains, i.e. the routers in this domain forward packets whose source and destination do not belong to the transit domain. As of this writing, about 85% of the domains in the Internet are stub domains [#fpotaroo]_. A `stub` domain that is connected to a single transit domain is called a `single-homed stub`. A `multihomed stub` is a `stub` domain connected to two or more transit providers.

Cada dominio contiene un conjunto de routers. Desde el punto de vista de un router, estos dominios pueden dividirse en dos clases: los dominios `de tránsito` los `finales` (o `stub domains`). Un dominio `final` envía y recibe paquetes cuyo origen o destino son sus propios hosts. Un dominio `de tránsito` es un dominio que provee un servicio de tránsito para otros dominios, es decir, los routers en este dominio reenvían paquetes cuyo origen y destino no pertenecen al dominio de tránsito. Al escribirse este documento, alrededor del 85% de los dominios de Internet son dominios `stub` [#fpotaroo]_. Un dominio stub que está conectado a un único dominio de tránsito se llama `single-homed stub`. Un `multihomed stub` es un dominio stub que está conectado a dos o más proveedores de tránsito.

.. figure:: png/network-fig-089-c.png
   :align: center
   :scale: 70

   Dominios de tránsito y stub   
..   Transit and stub domains 

.. The stub domains can be further classified by considering whether they mainly send or receive packets. An `access-rich` stub domain is a domain that contains hosts that mainly receive packets. Typical examples include small ADSL- or cable modem-based Internet Service Providers or enterprise networks. On the other hand, a `content-rich` stub domain is a domain that mainly produces packets. Examples of `content-rich` stub domains include google_, yahoo_, microsoft_, facebook_ or content distribution networks such as akamai_ or limelight_ For the last few years, we have seen a rapid growth of these `content-rich` stub domains. Recent measurements [ATLAS2009]_ indicate that a growing fraction of all the packets exchanged on the Internet are produced in the data centers managed by these content providers.

Los dominios stub pueden clasificarse además considerando si, principalmente, envían o reciben paquetes. Un dominio final rico en acceso (`access-rich stub domain`) es un dominio que contiene hosts que principalmente reciben paquetes. Los ejemplos típicos incluyen pequeñas redes de ISPs sobre ADSL o cable modem. Contrariamente, un dominio final rico en contenidos (`content-rich` stub domain) es un dominio que principalmente produce paquetes. Ejemplos de estos dominios son google_, yahoo_, microsoft_, facebook_, o redes de distribución de contenido como akamai_ o limelight_. Durante los últimos años, hemos visto un rápido crecimiento de estos dominios finales ricos en contenidos. Mediciones recientes [ATLAS2009]_ indican que una proporción creciente de los paquetes intercambiados en Internet son producidos en los `data centers` gestionados por estos proveedores de contenidos.

.. Domains need to be interconnected to allow a host inside a domain to exchange IP packets with hosts located in other domains. From a physical perspective, domains can be interconnected in two different ways. The first solution is to directly connect a router belonging to the first domain with a router inside the second domain. Such links between domains are called private interdomain links or `private peering links`. In practice, for redundancy or performance reasons, distinct physical links are usually established between different routers in the two domains that are interconnected. 

Los dominios necesitan estar interconectados para permitir que un host dentro de un dominio intercambie paquetes IP con hosts ubicados en otros dominios. Desde el punto de vista físico, los dominios pueden interconectarse de dos diferentes formas. La primera solución es conectar directamente un router que pertenece al primer dominio con un router dentro del segundo. Estos enlaces entre dominios se llaman enlaces interdominios privados (`private peering links`). En la práctica, por razones de redundancia o de performance, se establecen diferentes enlaces físicos entre diferentes routers en los dos dominios que se interconectan.

.. figure:: png/network-fig-104-c.png
   :align: center
   :scale: 70
   
   Interconexión de dos dominos mediante un enlace privado de `peering`
..   Interconnection of two domains via a private peering link 

.. Such `private peering links` are useful when, for example, an enterprise or university network needs to be connected to its Internet Service Provider. However, some domains are connected to hundreds of other domains [#fasrank]_ . For some of these domains, using only private peering links would be too costly. A better solution to allow many domains to interconnect cheaply are the `Internet eXchange Points` (:term:`IXP`). An :term:`IXP` is usually some space in a data center that hosts routers belonging to different domains. A domain willing to exchange packets with other domains present at the :term:`IXP` installs one of its routers on the :term:`IXP` and connects it to other routers inside its own network. The IXP contains a Local Area Network to which all the participating routers are connected. When two domains that are present at the IXP wish [#fwish]_ to exchange packets, they simply use the Local Area Network. IXPs are very popular in Europe and many Internet Service Providers and Content providers are present in these IXPs. 

Dichos enlaces privados de `peering` son útiles cuando la red de, por ejemplo, una empresa o universidad, necesita ser conectada a su ISP. Sin embargo, algunos dominios se conectan a cientos de otros dominios [#fasrank]_. Para algunos de estos dominios, el uso exclusivo de enlaces de peering privados sería demasiado costoso. Una mejor solución para permitir a muchos dominios interconectarse en forma económica son los `puntos de intercambio de Internet` (`Internet eXchange Points`, :term:`IXP`). Un :term:`IXP` es, típicamente, algún espacio en un data center que aloja routers, pertenecientes a diferentes dominios. Un dominio que desea intercambiar paquetes con otros dominios presentes en el :term:`IXP` instala uno de sus routers en el :term:`IXP` y los conecta a otros routers dentro de su propia red. El IXP contiene una LAN a la cual están conectados todos los routers participantes. Cuando dos dominios que están presentes en el IXP desean  [#fwish]_ intercabiar paquetes, simplemente usan la LAN. Los IXPs son muy populares en Europa, y muchos ISPs y proveedores de contenidos tienen presencia en estos IXPs.

.. figure:: png/network-fig-103-c.png
   :align: center
   :scale: 70

   Interconexión de dos dominios en un IXP (Internet eXchange Point).
..   Interconnection of two domains at an Internet eXchange Point

.. In the early days of the Internet, domains would simply exchange all the routes they know to allow a host inside one domain to reach any host in the global Internet. However, in today's highly commercial Internet, this is no longer true as interdomain routing mainly needs to take into account the economical relationships between the domains. Furthermore, while intradomain routing usually prefers some routes over others based on their technical merits (e.g. prefer route with the minimum number of hops, prefer route with the minimum delay, prefer high bandwidth routes over low bandwidth ones, etc) interdomain routing mainly deals with economical issues. For interdomain routing, the cost of using a route is often more important than the quality of the route measured by its delay or bandwidth.

En los primeros días de Internet, los dominios intercambiaban simplemente todas las rutas conocidas para que cada host dentro de un dominio pudiera alcanzar cualquier otro host de Internet. Sin embargo, en la Internet altamente comercial de hoy, esto ya no es cierto, porque el ruteo interdominios necesita tener en cuenta principalmente las relaciones económicas entre los dominios. Además, mientras el ruteo intradominio prefiere normalmente unas rutas a otras basándose en sus méritos técnicos (por ejemplo, se prefieren las rutas con número mínimo de saltos, las rutas con el mínimo retardo, las rutas de alto ancho de banda sobre las de bajo ancho de banda, etc.), el ruteo interdominio básicamente trata con los aspectos económicos. Para el ruteo interdominio, el costo de usar una ruta suele ser más importante que la calidad de la ruta medida por su retardo o su ancho de banda.

.. There are different types of economical relationships that can exist between domains. Interdomain routing converts these relationships into peering relationships between domains that are connected via peering links. 

Pueden existir diferentes tipos de relaciones económicas entre dominios. El ruteo interdominios convierte estas relaciones en relaciones de `peering` entre dominios que se conectan mediante enlaces de peering.

.. index:: customer-provider peering relationship

.. The first category of peering relationship is the `customer->provider` relationship. Such a relationship is used when a customer domain pays an Internet Service Provider to be able to exchange packets with the global Internet over an interdomain link. A similar relationship is used when a small Internet Service Provider pays a larger Internet Service Provider to exchange packets with the global Internet.

La primera categoría de relación de peering es la de cliente y proveedor. Dicha relación se conforma cuando un cliente paga a un ISP para poder intercambiar paquetes con la Internet global sobre un enlace interdominios. Se conforma una relación similar cuando un ISP pequeño paga a un ISP mayor por intercambiar paquetes con la Internet global.

.. figure:: png/network-fig-106-c.png
   :align: center
   :scale: 70
   
   Una interred simple con relaciones de `peering`
..   A simple Internet with peering relationships

.. To understand the `customer->provider` relationship, let us consider the simple internetwork shown in the figure above. In this internetwork, `AS7` is a stub domain that is connected to one provider : `AS4`. The contract between `AS4` and `AS7` allows a host inside `AS7` to exchange packets with any host in the internetwork. To enable this exchange of packets, `AS7` must know a route towards any domain and all the domains of the internetwork must know a route via `AS4` that allows them to reach hosts inside `AS7`. From a routing perspective, the commercial contract between `AS7` and `AS4` leads to the following routes being exchanged : 

..  - over a `customer->provider` relationship, the `customer` domain advertises to its `provider`  all its routes and all the routes that it has learned from its own customers. 
.. - over a `provider->customer` relationship, the `provider` advertises all the routes that it knows to its `customer`. 

Para comprender la relación cliente-proveedor, consideremos la interred sencilla mostrada en la figura anterior. En esta interred, `AS7` es un dominio final que se conecta a un proveedor: `AS4`. El contrato entre `AS4` y `AS7` permite a un host dentro de `AS7` intercambiar paquetes con cualquier host de la interred. Para permitir este intercambio de paquetes, `AS7` debe conocer una ruta hacia cualquier dominio, y todos los dominios de la interred deben conocer una ruta a través de `AS4` que les permita llegar a los hosts dentro de `AS7`. Desde el punto de vista del ruteo, el contrato comercial entre `AS7` y `AS4` lleva a que se intercambien las siguientes rutas: 

  - En una relación `cliente -> proveedor`, el dominio `cliente` anuncia a su `proveedor` todas sus rutas, y todas las rutas que ha aprendido de sus propios clientes.
  - En una relación `proveedor -> cliente`, el dominio `proveedor` anuncia todas las rutas que conoce a su `cliente`.

.. The second rule ensures that the customer domain receives a route towards all destinations that are reachable via its provider. The first rule allows the routes of the customer domain to be distributed throughout the Internet.

La segunda regla asegura que el dominio cliente reciba una ruta hacia todos los destinos que sean alcanzables a través de su proveedor. La primera regla permite que las rutas del cliente sean distribuidas por toda Internet.

.. Coming back to the figure above, `AS4` advertises to its two providers `AS1` and `AS2` its own routes and the routes learned from its customer, `AS7`. On the other hand, `AS4` advertises to `AS7` all the routes that it knows. 

Volviendo a la figura anterior, `AS4` anuncia a sus dos proveedores `AS1` y `AS2` sus propias rutas y las aprendidas de su cliente, `AS7`. Por otra parte, `AS4` anuncia todas las rutas que conoce a `AS7`.

.. index:: shared-cost peering relationship

.. The second type of peering relationship is the `shared-cost` peering relationship. Such a relationship usually does not involve a payment from one domain to the other in contrast with the `customer->provider` relationship. A `shared-cost` peering relationship is usually established between domains having a similar size and geographic coverage. For example, consider the figure above. If `AS3` and `AS4` exchange many packets via `AS1`, they both need to pay `AS1`. A cheaper alternative for `AS3` and `AS4` would be to establish a `shared-cost` peering. Such a peering can be established at IXPs where both `AS3` and `AS4` are present or by using private peering links. This `shared-cost` peering should be used to exchange packets between hosts inside `AS3` and hosts inside `AS4`. However, `AS3` does not want to receive on the `AS3-AS4` `shared-cost` peering links packets whose destination belongs to `AS1` as `AS3` would have to pay to send these packets to `AS1`.  

El segundo tipo de relación de peering es la de `costo compartido` (`shared-cost`). Esta relación generalmente no implica un pago de un dominio al otro, al contrario que en la relación `cliente -> proveedor`. Una relación de peering de costo compartido se establece normalmente entre dominios que tienen un tamaño y una cobertura geográfica similares. Por ejemplo, consideremos la figura anterior. Si `AS3` y `AS4` intercambian muchos paquetes a través de `AS1`, ambos deberán pagarle a `AS1`. Una alternativa más barata para `AS3` y `AS4` sería establecer una relación de costo compartido. Dicha relación de peering puede ser establecida en IXPs donde ambos `AS3` y `AS4` tengan presencia, o usando enlaces privados de peering. Este peering de costo compartido debería ser usado para intercambiar paquetes entre hosts dentro de `AS3` y hosts dentro de `AS4`. Sin embargo, `AS3` no quiere recibir, sobre el enlace de costo compartido `AS3-AS4`, paquetes cuyo destino pertenezca a `AS1`, ya que `AS3` tendría que pagar por enviar estos paquetes a `AS1`.  

.. From a routing perspective, over a `shared-cost` peering relationship a domain only advertises its internal routes and the routes that it has learned from its customers. This restriction ensures that only packets destined to the local domain or one of its customers is received over the `shared-cost` peering relationship. This implies that the routes that have been learned from a provider or from another `shared-cost` peer is not advertised over a `shared-cost` peering relationship. This is motivated by economical reasons. If a domain were to advertise the routes that it learned from a provider over a `shared-cost` peering relationship that does not bring revenue, it would have allowed its `shared-cost` peer to use the link with its provider without any payment. If a domain were to advertise the routes it learned over a `shared cost` peering over another `shared-cost` peering relationship, it would have allowed these `shared-cost` peers to use its own network (which may span one or more continents) freely to exchange packets. 

Desde el punto de vista del ruteo, un dominio, sobre el enlace de una relación de costo compartido, sólo anuncia sus rutas internas y las rutas que haya aprendido de sus clientes. Esta restricción asegura que sólo se reciban sobre el enlace de costo compartido aquellos paquetes destinados al dominio local o a alguno de sus clientes. Por lo tanto, no serán anunciadas sobre dicha relación de costo compartido las rutas que hayan sido aprendidas de un proveedor o de otro peer de costo compartido. La motivación es económica: si un dominio anunciara las rutas que aprendió de un proveedor sobre una relación de costo compartido que no trae ganancias, habría permitido a su peer de costo compartido usar el enlace con su proveedor sin ningún pago. Si un dominio anunciara las rutas aprendidas por un enlace de costo compartido, sobre otra relación del mismo tipo, habría permitido a estos peers de costo compartido usar su propia red (que puede extenderse sobre uno o más continentes) libremente para intercambiar paquetes.

.. index:: sibling peering relationship

.. Finally, the last type of peering relationship is the `sibling`. Such a relationship is used when two domains exchange all their routes in both directions. In practice, such a relationship is only used between domains that belong to the same company. 

Finalmente, el tercer tipo de relación de peering es la `fraternal` (`sibling`). Esta relación se establece cuando dos dominios intercambian todas sus rutas en ambas direcciones. En la práctica, este tipo de relación se usa sólo entre dominios que pertenecen a la misma organización.

.. index:: interdomain routing policy

.. These different types of relationships are implemented in the `interdomain routing policies` defined by each domain. The `interdomain routing policy` of a domain is composed of three main parts : 

..  - the `import filter` that specifies, for each peering relationship, the routes that can be accepted from the neighbouring domain (the non-acceptable routes are ignored and the domain never uses them to forward packets) 
..  - the `export filter` that specifies, for each peering relationship, the routes that can be advertised to the neighbouring domain  
..  - the `ranking` algorithm that is used to select the best route among all the routes that the domain has received towards the same destination prefix  


Estos diferentes tipos de relaciones se implementan en las `políticas de ruteo interdominio` definidas por cada dominio. Esta política se compone de tres partes principales: 

  - El `filtro de importación` (`import filter`) especifica, para cada relación de peering, las rutas que pueden ser aceptadas del dominio vecino (las rutas no aceptables serán ignoradas, y el dominio nunca las usará para reenviar paquetes).
  - El `filtro de exportación` (`export filter`) que especifica, para cada relación de peering, las rutas que serán anunciadas al dominio vecino.
  - El algoritmo de `ranking` que se usa para seleccionar la mejor ruta entre todas las que el dominio ha recibido hacia el mismo prefijo destino.

.. index:: import policy, export policy

.. A domain's import and export filters can be defined by using the Route Policy Specification Language (RPSL) specified in :rfc:`2622` [GAVE1999]_ . Some Internet Service Providers, notably in Europe, use RPSL to document [#fripedb]_ their import and export policies. Several tools help to easily convert a RPSL policy into router commands. 

Los filtros de importación y exportacíon de un dominio pueden definirse usando el lenguaje de especificación de políticas de ruteo (`Route Policy Specification Language`, RPSL) especificado en :rfc:`2622` [GAVE1999]_. Algunos ISPs, notablemente en Europa, usan RPSL para documentar [#fripedb]_ sus políticas de importación y exportación. Existen varias herramientas para convertir fácilmente una política RPSL en comandos de configuración de un router. 

.. The figure below provides a simple example of import and export filters for two domains in a simple internetwork. In RPSL, the keyword `ANY` is used to replace any route from any domain. It is typically used by a provider to indicate that it announces all its routes to a customer over a `provider->customer` relationship. This is the case for `AS4`'s export policy. The example below clearly shows the difference between a `provider->customer` and a `shared-cost` peering relationship. `AS4`'s export filter indicates that it announces only its internal routes (`AS4`) and the routes learned from its clients (`AS7`) over its `shared-cost` peering with `AS3`, while it advertises all the routes that it uses (including the routes learned from `AS3`) to `AS7`. 

La figura siguiente ofrece un ejemplo sencillo de filtros de importación y exportación para dos dominios en una interred simple. En RPSL se usa la clave `ANY` para sustituir cualquier ruta de cualquier dominio. Es típicamente usada por un proveedor para indicar que anuncia todas sus rutas a un cliente sobre una relación `proveedor -> cliente`. Éste es el caso de la política de exportación de `AS4`. El ejemplo siguiente muestra claramente la diferencia entre relaciones de peering `proveedor -> cliente` y `costo compartido`. El filtro de exportación de `AS4` indica que anuncia sólo sus rutas internas (`AS4`) y las rutas aprendidas de sus clientes (`AS7`) sobre su relación de peering de costo compartido con `AS3`, mientras que anuncia todas las rutas que usa (incluyendo las rutas aprendidas de `AS3`) a `AS7`. 

.. figure:: png/network-fig-109-c.png
   :align: center
   :scale: 70

   Políticas de importación y exportación   
..    Import and export policies 

.. index:: BGP, Border Gateway Protocol

.. The Border Gateway Protocol
BGP (Border Gateway Protocol)
-----------------------------

.. The Internet uses a single interdomain routing protocol : the Border Gateway Protocol (BGP). The current version of BGP is defined in :rfc:`4271`. BGP differs from the intradomain routing protocols that we have already discussed in several ways. First, BGP is a `path-vector` protocol. When a BGP router advertises a route towards a prefix, it announces the IP prefix and the interdomain path used to reach this prefix. From BGP's point of view, each domain is identified by a unique `Autonomous System` (AS) number [#fasdomain]_ and the interdomain path contains the AS numbers of the transit domains that are used to reach the associated prefix. This interdomain path is called the `AS Path`. Thanks to these AS-Paths, BGP does not suffer from the count-to-infinity problems that affect distance vector routing protocols. Furthermore, the AS-Path can be used to implement some routing policies. Another difference between BGP and the intradomain routing protocols is that a BGP router does not send the entire contents of its routing table to its neighbours regularly. Given the size of the global Internet, routers would be overloaded by the number of BGP messages that they would need to process. BGP uses incremental updates, i.e. it only announces the routes that have changed to its neighbours.

Internet utiliza un único protocolo de ruteo interdominios: `Border Gateway Protocol` (protocolo de pasarelas de frontera, BGP). La versión actual de BGP está definida en :rfc:`4271`. BGP difiere de los protocolos de ruteo intradominio que ya hemos discutido en varias formas. En primer lugar, BGP es un protocolo de `vector de caminos` (`path-vector`). Cuando un router BGP publica una ruta hacia un prefijo destino, anuncia el prefijo IP y el camino interdominio usado para alcanzar este prefijo. Desde el punto de vista de BGP, cada dominio se identifica por un número único de sistema autónomo (`Autonomous System number` o `AS number` [#fasdomain]_), y el camino interdominios contiene los números de AS de los dominios de tránsito que son usados para alcanzar el prefijo asociado. Este camino interdominios se llama camino de sistemas autónomos (`AS-Path`). Gracias a estos AS-Paths, BGP no sufre de los problemas de cuenta al infinito que afectan a los protocolos de ruteo de vector-distancia. Más aún, el AS-Path puede usarse para implementar algunas políticas de ruteo. Otra diferencia entre BGP y los protocolos de ruteo intradominios es que un router BGP no envía regularmente los contenidos completos de su tabla de ruteo a los vecinos. Dado el tamaño de la Internet completa, los routers se verían sobrecargados por la cantidad de mensajes BGP que necesitarían procesar. BGP usa actualizaciones incrementales, es decir, anuncia a sus vecinos solamente las rutas que han cambiado.

.. The figure below shows a simple example of the BGP routes that are exchanged between domains. In this example, prefix `1.0.0.0/8` is announced by `AS1`. `AS1` advertises a BGP route towards this prefix to `AS2`. The AS-Path of this route indicates that `AS1` is the originator of the prefix. When `AS4` receives the BGP route from `AS1`, it re-announces it to `AS2` and adds its AS number to the AS-Path. `AS2` has learned two routes towards prefix `1.0.0.0/8`. It compares the two routes and prefers the route learned from `AS4` based on its own ranking algorithm. `AS2` advertises to `AS5` a route towards `1.0.0.0/8` with its AS-Path set to `AS2:AS4:AS1`. Thanks to the AS-Path, `AS5` knows that if it sends a packet towards `1.0.0.0/8` the packet first passes through `AS2`, then through `AS4` before reaching its destination inside `AS1`.

La figura siguiente muestra un ejemplo simple de rutas BGP que son intercambiadas entre dominios. En este ejemplo, el prefijo  `1.0.0.0/8` es anunciado por `AS1`. `AS1` publica a `AS2` una ruta BGP hacia este prefijo. El AS-Path de esta ruta indica que `AS1` es el originador del prefijo. Cuando `AS4` recibe de `AS1` la ruta BGP, la re-anuncia a `AS2` y agrega su número de AS al AS-Path. `AS2` ha aprendido dos rutas hacia el prefijo `1.0.0.0/8`. Compara ambas rutas y prefiere la aprendida de `AS4` basándose en su propio algoritmo de ranking. `AS2` publica a `AS5` una ruta hacia `1.0.0.0/8` con su AS-Path fijado en `AS2:AS4:AS1`. Gracias al AS-Path, `AS5` sabe que si envía un paquete hacia `1.0.0.0/8`, éste primero pasará a través de `AS2` y luego a través de `AS4`, antes de alcanzar su destino dentro de `AS1`.

.. figure:: png/network-fig-111-c.png
   :align: center
   :scale: 70
  
   Intercambio simple de rutas BGP  

..   Simple exchange of BGP routes 

.. index:: BGP peer

.. BGP routers exchange routes over BGP sessions. A BGP session is established between two routers belonging to two different domains that are directly connected. As explained earlier, the physical connection between the two routers can be implemented as a private peering link or over an Internet eXchange Point. A BGP session between two adjacent routers runs above a TCP connection (the default BGP port is 179). In contrast with intradomain routing protocols that exchange IP packets or UDP segments, BGP runs above TCP because TCP ensures a reliable delivery of the BGP messages sent by each router without forcing the routers to implement acknowledgements, checksums, etc. Furthermore, the two routers consider the peering link to be up as long as the BGP session and the underlying TCP connection remain up [#flifetimebgp]_. The two endpoints of a BGP session are called `BGP peers`.

Los routers BGP intercambian rutas mediante sesiones BGP. Una sesión BGP se establece entre dos routers que pertenecen a diferentes dominios y que están directamente conectados. Como se explicó anteriormente, la conexión física entre los dos routers puede ser implementada como un enlace privado de `peering` o sobre un punto de intercambio IXP. Una sesión BGP entre dos routers adyacentes corre por encima de una conexión TCP (el puerto default de BGP es 179). En contraste con los protocolos de ruteo intradominios que intercambian paquetes IP o segmentos UDP, BGP corre sobre TCP porque éste le asegura la entrega confiable de los mensajes BGP enviados por cada router, sin forzarlos a implementar reconocimientos, checksums, etc. Por otro lado, ambos  routers consideran que el enlace de `peering` está activo mientras la sesión BGP y la conexión TCP subyacente estén activos[#flifetimebgp]_. Los dos extremos de la sesión BGP se llaman `pares BGP` (`BGP peers`).

.. figure:: svg/bgp-peering.*
   :align: center
   :scale: 70
   
   Una sesión BGP entre dos routers directamente conectados
..   A BGP peering session between two directly connected routers

.. In practice, to establish a BGP session between routers `R1` and `R2` in the figure above, the network administrator of `AS3` must first configure on `R1` the IP address of `R2` on the `R1-R2` link and the AS number of `R2`. Router `R1` then regularly tries to establish the BGP session with `R2`. `R2` only agrees to establish the BGP session with `R1` once it has been configured with the IP address of `R1` and its AS number. For security reasons, a router never establishes a BGP session that has not been manually configured on the router. 

En la práctica, para establecer una sesió BGP entre los routers `R1` y `R2` de la figura anterior, el administrador de red del sistema autónomo `AS3` primero debe configurar en `R1` la dirección IP de `R2` sobre el vínculo `R1-R2`, y el número de AS de `R2`. El router `R1`, luego, intenta periódicamente establecer la sesión BGP con `R2`. `R2` sólo accede a establecer la sesión BGP con `R1` una vez que ha sido configurado con la dirección IP de `R1` y su número de AS. Por razones de seguridad, un router nunca establece una sesión BGP que no haya sido manualmente configurada en el router. 

.. index:: BGP OPEN, BGP NOTIFICATION, BGP KEEPALIVE, BGP UPDATE

.. The BGP protocol :rfc:`4271` defines several types of messages that can be exchanged over a BGP session :
..
.. - `OPEN` : this message is sent as soon as the TCP connection between the two routers has been established. It initialises the BGP session and allows the negotiation of some options. Details about this message may be found in :rfc:`4271`
.. - `NOTIFICATION` : this message is used to terminate a BGP session, usually because an error has been detected by the BGP peer. A router that sends or receives a `NOTIFICATION` message immediately shutdowns the corresponding BGP session.
.. - `UPDATE`: this message is used to advertise new or modified routes or to withdraw previously advertised routes.
.. - `KEEPALIVE` : this message is used to ensure a regular exchange of messages on the BGP session, even when no route changes. When a BGP router has not sent an `UPDATE` message during the last 30 seconds, it shall send a `KEEPALIVE` message to confirm to the other peer that it is still up. If a peer does not receive any BGP message during a period of 90 seconds [#fdefaultkeepalive]_, the BGP session is considered to be down and all the routes learned over this session are withdrawn. 

El protocolo BGP [:rfc:`4271`] define varios tipos de mensajes que pueden ser intercambiados sobre una sesión BGP:

 - `OPEN`: Este mensaje se envía apenas se establece la conexión TCP entre los dos router. Inicializa la sesión BGP y permite la negociación de algunas opciones. Los detalles sobre este mensaje se pueden consutar en :rfc:`4271`
 - `NOTIFICATION`: Este mensaje se usa para finalizar una sesión BGP, generalmente porque el `peer` BGP ha detectado un error. Un router que envía o recibe un mensaje `NOTIFICATION` inmediatamente cierra la correspondiente sesión BGP.
 - `UPDATE`: Este mensaje se usa para anunciar rutas nuevas o modificadas, o para retirar rutas que previamente han sido anunciadas.
 - `KEEPALIVE`: Este mensaje se usa para asegurar un intercambio regular de mensajes sobre la sesión BGP, aun cuando no cambien las ruas. Cuando un router BGP no ha enviado un mensaje `UPDATE` durante los últimos 30 segundos, enviará un mensaje `KEEPALIVE` para confirmar al otro `peer` que sigue activo. Si un `peer` no recibe ningún mensaje BGP durante un período de 90 segundos [#fdefaultkeepalive]_, la sesión BGP se considera cerrada y todas las rutas aprendidas sobre esta sesión son retiradas.


.. As explained earlier, BGP relies on incremental updates. This implies that when a BGP session starts, each router first sends BGP `UPDATE` messages to advertise to the other peer all the exportable routes that it knows. Once all these routes have been advertised, the BGP router only sends BGP `UPDATE` messages about a prefix if the route is new, one of its attributes has changed or the route became unreachable and must be withdrawn. The BGP `UPDATE` message allows BGP routers to efficiently exchange such information while minimising the number of bytes exchanged. Each `UPDATE` message contains :

.. - a list of IP prefixes that are withdrawn
.. - a list of IP prefixes that are (re-)advertised
.. - the set of attributes (e.g. AS-Path) associated to the advertised prefixes

Como se explicó anteriormente, BGP se basa en actualizaciones incrementales. Esto implica que, cuando arranca una sesión BGP, cada router primeramente envía mensajes BGP `UPDATE` para anunciar al otro `peer` todas las rutas exportables que conoce.  Una vez que todas estas rutas hayan sido anunciadas, el router BGP sólo envía mensajes BGP `UPDATE` sobre un prefijo si la ruta es nueva, si uno de sus atributos ha cambiado, o si la ruta ha quedado inalcanzable y debe ser retirada. El mensaje BGP `UPDATE` permite a los routers BGP para intercambiar eficientemente dicha información mientras que se minimiza el número de bytes intercambiados. Cada mensaje `UPDATE` contiene:

 - Una lista de prefijos IP que son retirados
 - Una lista de prefijos IP que son (re-)anunciados
 - El conjunto de atributos (por ejemplo, el `AS-Path`) asociado a los prefijos anunciados

.. In the remainder of this chapter, and although all routing information is exchanged using BGP `UPDATE` messages, we assume for simplicity that a BGP message contains only information about one prefix and we use the words :

.. - `Withdraw message` to indicate a BGP `UPDATE` message containing one route that is withdrawn 
.. - `Update message` to indicate a BGP `UPDATE` containing a new or updated route towards one destination prefix with its attributes 

En el resto de este capítulo, y aunque toda la información de ruteo se intercambia usando mensajes BGP `UPDATE`, suponemos por simplicidad que un mensaje BGP contiene sólo información acerca de un prefijo, y usamos las palabras:

 - `Retiro` (`Withdraw message`) para indicar un mensaje BGP `UPDATE` que contiene una ruta que es retirada.
 - `Actualización` (`Update message`) para indicar un mensaje BGP `UPDATE` que contiene una ruta nueva, o actualizada, hacia un prefijo destino con sus atributos. 

.. index:: BGP Adj-RIB-In, BGP Adj-RIB-Out, BGP RIB

.. From a conceptual point of view, a BGP router connected to `N` BGP peers, can be described as being composed of four parts as shown in the figure below.

Desde un punto de vista conceptual, un router BGP conectado a `N` pares BGP puede describirse como compuesto por cuatro partes, como se muestra en la figura siguiente.

.. _bgprouter:

.. figure:: png/network-fig-113-c.png
   :align: center
   :scale: 70
  
   Organización de un router BGP
..   Organisation of a BGP router 

.. In this figure, the router receives BGP messages on the left part of the figure, processes these messages and possibly sends BGP messages on the right part of the figure. A BGP router contains three important data structures :

.. - the `Adj-RIB-In` contains the BGP routes that have been received from each BGP peer. The routes in the `Adj-RIB-In` are filtered by the `import filter` before being placed in the `BGP-Loc-RIB`. There is one `import filter` per BGP peer.
.. - the `Local Routing Information Base` (`Loc-RIB`) contains all the routes that are considered as acceptable by the router. The `Loc-RIB` may contain several routes, learned from different BGP peers, towards the same destination prefix.
.. - the `Forwarding Information Base` (`FIB`) is used by the dataplane to forward packets towards their destination. The `FIB` contains, for each destination, the best route that has been selected by the `BGP decision process`. This decision process is an algorithm that selects, for each destination prefix, the best route according to the router's ranking algorithm that is part of its policy.
.. - the `Adj-RIB-Out` contains the BGP routes that have been advertised to each BGP peer. The `Adj-RIB-Out` for a given peer is built by applying the peer`s `export filter` on the routes that have been installed in the `FIB`. There is one `export filter` per BGP peer. For this reason, the Adj-RIB-Out of a peer may contain different routes than the Adj-RIB-Out of another peer.

En esta figura, el router recibe mensajes BGP en la parte izquierda de la figura, procesa estos mensajes y posiblemente envía mensajes BGP en la parte derecha de la figura. Un router BGP contiene tres importantes estructuras de datos:

 - La `Base de Información de Adyacencias de Ingreso` (`Adjacency Routing Information Base`, `Adj-RIB-In`) contiene las rutas BGP que han sido recibidas de cada `peer` BGP. Las rutas en `Adj-RIB-In` son filtradas por el `filtro de importación` antes de ser ubicadas en `BGP-Loc-RIB`. Hay un `filtro de importación` por cada par BGP.
 - La `Base de Información Local` (`Local Routing Information Base`, `Loc-RIB`) contiene todas las rutas que son consideradas aceptables por el router. La tabla `Loc-RIB` puede contener varias rutas, aprendidas de diferentes pares BGP, hacia el mismo prefijo destino.
 - La `Base de Información de Reenvío` (`Forwarding Information Base`, `FIB`) es usada por el plano de datos para reenviar paquetes hacia su destino. La `FIB` contiene, para cada destino, la mejor ruta que ha sido seleccionada por el `proceso de decisión` de BGP. Este proceso de decisión es un algoritmo que selecciona, para cada prefijo destino, la mejor ruta de acuerdo al algoritmo de `ranking` del router que es parte de su política. 
 - La `Base de Información de Adyacencias de Egreso` (`Adj-RIB-Out`) contiene las rutas BGP que han sido anunciadas a cada par BGP. La base `Adj-RIB-Out` para un par dado se construye aplican el `filtro de exportación` del `peer` sobre las rutas que han sido instaladas en la  the `FIB`. Hay un `filtro de exportación` por cada par BGP. Por esta razón, la base `Adj-RIB-Out` de un par puede contener diferentes rutas que el `Adj-RIB-Out` de otro par.


.. When a BGP session starts, the routers first exchange `OPEN` messages to negotiate the options that apply throughout the entire session. Then, each router extracts from its FIB the routes to be advertised to the peer. It is important to note that, for each known destination prefix, a BGP router can only advertise to a peer the route that it has itself installed inside its `FIB`. The routes that are advertised to a peer must pass the peer's `export filter`. The `export filter` is a set of rules that define which routes can be advertised over the corresponding session, possibly after having modified some of its attributes. One `export filter` is associated to each BGP session. For example, on a `shared-cost peering`, the `export filter` only selects the internal routes and the routes that have been learned from a `customer`. The pseudo-code below shows the initialisation of a BGP session.

Cuando arranca una sesión BGP, los routers primeramente intercambian mensajes `OPEN` para negociar las opciones que se aplicarán durante toda la sesión. Luego, cada router extrae de su `FIB` las rutas que serán anunciadas al `peer`. Es importante notar que, para cada prefijo destino conocido, un router BGP sólo puede anunciar a un `peer` la ruta que él tiene instalada en su `FIB`. Las rutas que son anunciadas a un `peer` deben pasar su filtro de exportación. El filtro de exportación es un conjunto de reglas que definen qué rutas pueden ser anunciadas sobre la sesión correspondiente, posiblemente luego de haber modificado algunos de sus atributos. Con cada sesión BGP se asocia un filtro de exportación. Por ejemplo, en un enlace de costo compartido, el filtro de exportación sólo selecciona las rutas internas y las que han sido aprendidas de un `cliente`. El pseudocódigo siguiente muestra la inicialización de una sesión BGP.

.. code-block:: python

  def inicializar_sesión_BGP(AS_Remoto, IP_Remoto):
    # Inicializar y comenzar sesión BGP
    # Enviar mensaje BGP OPEN a IP_Remoto sobre puerto 179
    # Seguir la máquina de estados BGP
    # Anunciar rutas locales y rutas aprendidas de pares
    for d in BGPLocRIB:
    	B=construir_Update_BGP(d)
	S=aplicar_Filtro_Exportación(AS_Remoto, B)
	if (S != None):
	   enviar_Update(S, AS_Remoto, IP_Remoto)
    # Se ha enviado la tabla RIB completa
    # Se enviarán nuevos Updates para reflejar cambios 
    # locales o distantes en los routers


.. In the above pseudo-code, the `build\_BGP\_UPDATE(d)` procedure extracts from the `BGP Loc-RIB` the best path towards destination `d` (i.e. the route installed in the FIB) and prepares the corresponding BGP `UPDATE` message. This message is then passed to the `export filter` that returns NULL if the route cannot be advertised to the peer or the (possibly modified) BGP `UPDATE` message to be advertised. BGP routers allow network administrators to specify very complex `export filters`, see e.g. [WMS2004]_. A simple `export filter` that implements the equivalent of `split horizon` is shown below.

En el pseudocódigo anterior, el procedimiento `construir\_UPDATE\_BGP(d)` extrae de la base `BGP Loc-RIB` el mejor camino hacia el destino `d` (es decir, la ruta instalada en `FIB`) y prepara el mensaje BGP `UPDATE` correspondiente. Este mensaje luego es pasado al filtro de exportación que devuelve NULL si la ruta no puede ser anunciada al `peer` o si el mensaje `UPDATE`  (posiblemente modificado) no puede ser anunciado. Los routers BGP permiten a los administradores de red especificar filtros de exportación sumamente complejos (ver, por ejemplo, [WMS2004]_). A continuación se muestra un filtro de exportación simple que implementa el equivalente de `horizonte dividido` (`split horizon`).

.. code-block:: python

 def aplicar_filtro_exportacion(AS_Remoto, mensaje_BGP):
   # varificar su AS_Remoto ya recibió la ruta
   if AS_Remoto in mensaje_BGP.ASPath:
      mensaje_BGP=None
      # Pueden configurarse muchas políticas de exportación adicionales: 
      # - Aceptar o rehusar mensaje_BGP
      # - Modificar atributos seleccionados dentro de mensaje_BGP
   return mensaje_BGP

.. At this point, the remote router has received all the exportable BGP routes. After this initial exchange, the router only sends `BGP UPDATE` messages when there is a change (addition of a route, removal of a route or change in the attributes of a route) in one of these exportable routes. Such a change can happen when the router receives a BGP message. The pseudo-code below summarizes the processing of these BGP messages.

En este punto, el router remoto ha recibido todas las rutas BGP exportables. Luego de este intercambio inicial, el router sólo envía mensajes `BGP UPDATE` cuando ocurre un cambio (agregado o eliminación de una ruta, o cambio en los atributos de una ruta) en una de estas rutas exportables. Dicho cambio puede ocurrir cuando el router recibe un mensaje BGP. El pseudocódigo siguiente resume el procesamiento de estos mensajes BGP.

.. code-block:: python

 def mensaje_BGP_recibido(Msg, AS_Remoto) :
     B=aplicar_filtro_importacion(Msg, AS_Remoto)
     if B == None: # Mensaje no aceptable
     	return
     if es_ACTUALIZACION(Msg):
     	ruta_Anterior=mejorRuta(Msg.prefix) 
   	insertar_en_RIB(Msg)
   	correr_Proceso_Decision(RIB)       
	if (mejorRuta(Msg.prefix) != ruta_Anterior) :
	   # la mejor ruta ha cambiado
	   B=construir_mensaje_BGP(Msg.prefix);
    	   S=aplicar_filtro_exportacion(AS_Remoto, B);
    	   if (S != None) : # anunciar la mejor ruta
	     enviar_ACTUALIZACION(S, AS_Remoto, IP_Remoto);     
    	   else if (ruta_Anterior != None) :
	     enviar_RETIRO(Msg.prefix, AS_Remoto, IP_Remoto)		
      else : # Msg es RETIRO
      	  ruta_Anterior=mejor_Ruta(Msg.prefix) 
   	  eliminar_de_RIB(Msg)
	  correr_Proceso_Decision(RIB)
	  if (mejor_Ruta(Msg.prefix) != ruta_Anterior):
	    # mejor ruta ha cambiado
	    B=construir_mensaje_BGP(Msg.prefix)
	    S=aplicar_filtro_exportacion(AS_Remoto, B)
	    if (S != None) : # aún es la una mejor ruta hacia Msg.prefix
	       enviar_ACTUALIZACION(S, AS_Remoto, IP_Remoto);
     	    else if(ruta_Anterior != None) : # Ya no es mejor ruta
	        enviar_RETIRO(Msg.prefix, AS_Remoto, IP_Remoto);
     
.. When a BGP message is received, the router first applies the peer's `import filter` to verify whether the message is acceptable or not. If the message is not acceptable, the processing stops. The pseudo-code below shows a simple `import filter`. This `import filter` accepts all routes, except those that already contain the local AS in their AS-Path. If such a route was used, it would cause a routing loop. Another example of an `import filter` would be a filter used by an Internet Service Provider on a session with a customer to only accept routes towards the IP prefixes assigned to the customer by the provider. On real routers, `import filters` can be much more complex and some `import filters` modify the attributes of the received BGP `UPDATE` [WMS2004]_ .

Cuando se recibe un mensaje BGP, el router primeramente aplica el filtro de importación del `peer`para verificar si el mensaje es aceptable o no. Si el mensaje no es aceptable, se detiene el procesamiento. El pseudocódigo siguiente muestra un filtro de importación sencillo. Este filtro de importación acepta todas las rutas, excepto aquellas que ya contienen el AS local en su `AS-Path`. Si fuera usada una de dichas rutas, causaría un ciclo de ruteo. Otro ejemplo de un filtro de importación sería un filtro usado por un ISP sobre una sesión con un cliente, para aceptar sólo rutas hacia los prefijos IP asignados al cliente por el proveedor. En los routers verdaderos, los filtros de importación pueden ser mucho más complejos, y algunos filtros de importación modifican los atributos del mensaje BGP `UPDATE` [WMS2004]_.

.. code-block:: python

 def aplicar_filtro_importacion(AS_Remoto, mensaje_BGP):
     if mi_AS in mensaje_BGP.ASPath:
     	mensaje_BGP=None
	# Pueden configurarse muchas políticas de importación adicionales: 
	# - Aceptar o rehusar mensaje_BGP
	# - Modificar atributos seleccionados dentro de mensaje_BGP
     return mensaje_BGP
	

.. note:: The bogon filters

..  Another example of frequently used `import filters` are the filters that Internet Service Providers use to ignore bogon routes. In the ISP community, a bogon route is a route that should not be advertised on the global Internet. Typical examples include the private IPv4 prefixes defined in :rfc:`1918`, the loopback prefixes (`127.0.0.1/8` and `::1/128`) or the IP prefixes that have not yet been allocated by IANA. A well managed BGP router should ensure that it never advertises bogons on the global Internet. Detailed information about these bogons may be found at http://www.team-cymru.org/Services/Bogons/

Otro ejemplo de filtros de importación usados frecuentemente son los filtros que usan los ISPs para ignorar rutas `bogon`. En la comunidad de ISPs, una ruta `bogon` es aquella que no debe ser anunciada en la Internet global. Ejemplos típicos son los prefijos IPv4 privados  definidos en :rfc:`1918`, los prefijos de `loopback` (`127.0.0.1/8` y `::1/128`) o los prefijos IP que no hayan sido aún asignados por IANA. Un router BGP bien administrado debe asegurar que nunca anunciará `bogons` a la Internet global. Más detalles sobre `bogons` en http://www.team-cymru.org/Services/Bogons.


.. If the import filter accepts the BGP message, the pseudo-code distinguishes two cases. If this is an `Update message` for prefix `p`, this can be a new route for this prefix or a modification of the route's attributes. The router first retrieves from its `RIB` the best route towards prefix `p`. Then, the new route is inserted in the `RIB` and the `BGP decision process` is run to find whether the best route towards destination `p` changes. A BGP message only needs to be sent to the router's peers if the best route has changed. For each peer, the router applies the  `export filter` to verify whether the route can be advertised. If yes, the filtered BGP message is sent. Otherwise, a `Withdraw message` is sent. When the router receives a `Withdraw message`, it also verifies whether the removal of the route from its `RIB` caused its best route towards this prefix to change. It should be noted that, depending on the content of the `RIB` and the `export filters`, a BGP router may need to send a `Withdraw message` to a peer after having received an `Update message` from another peer and conversely.

Si el filtro de importación acepa el mensaje BGP, el pseudocódigo distingue dos casos. Si se trata de un mensaje de `Actualización` para el prefijo `p`, ésta puede ser una nueva ruta para este prefijo o una modificación de los atributos de la ruta. El router primeramente extrae de su `RIB` la mejor ruta hacia el prefijo `p`. Luego inserta en el `RIB` la nueva ruta y corre el proceso de decisión BGP para determinar si la mejor ruta hacia el destino `p` cambia. Sólo se necesita enviar un mensaje BGP a los pares del router si la mejor ruta ha cambiado. Para cada `peer`, el router aplica el filtro de exportación para verificar si la ruta puede ser anunciada. Si es así, el mensaje BGP filtrado es enviado. Si no, se envía un mensaje de `Retiro`. Cuando el router recibe un mensaje de `Retiro`, también verifica si la eliminación de la ruta de su `RIB` ha causado que cambie su mejor ruta hacia este prefijo. Debe notarse que, dependiendo del contenido de la tabla `RIB` y de los filtros de exportación, un router BGP puede necesitar enviar un mensaje de `Retiro` a un par luego de haber recibido una `Actualización` de otro par, y a la inversa.

.. Let us now discuss in more detail the operation of BGP in an IPv4 network. For this, let us consider the simple network composed of three routers located in three different ASes and shown in the figure below.

Discutamos ahora en mayor detalle la operación de BGP en una red IPv4. Para esto consideremos la red simple compuesta por tres routers en tres AS diferentes como se muestra en la figura siguiente.
.. figure:: svg/bgp-nexthop.*
   :align: center
   :scale: 70
  
   Utilización del atributo `nexthop` de BGP 
.. Utilisation of the BGP nexthop attribute

.. This network contains three routers : `R1`, `R2` and `R3`. Each router is attached to a local IPv4 subnet that it advertises using BGP. There are two BGP sessions, one between `R1` and `R2` and the second between `R2` and `R3`. A `/30` subnet is used on each interdomain link (`195.100.0.0/30` on `R1-R2` and `195.100.0.4/30` on `R2-R3`). The BGP sessions run above TCP connections established between the neighbouring routers (e.g. `195.100.0.1 - 195.100.0.2` for the `R1-R2` session).

Esta red contiene tres routers: `R1`, `R2` y `R3`. Cada router está conectado a una subred local IPv4, la cual anuncia usando BGP. Hay dos sesiones BGP, una entre `R1` y `R2` y la segunda entre `R2` y `R3`. En cada enlace interdominios (`195.100.0.0/30` sobre `R1-R2` y `195.100.0.4/30` sobre `R2-R3`) se usa una subred `/30`. Las sesiones BGP corren sobre conexiones TCP establecidas entre los routers vecinos  (por ejemplo, `195.100.0.1 - 195.100.0.2` para la sesión `R1-R2`).

.. index:: BGP nexthop

.. Let us assume that the `R1-R2` BGP session is the first to be established. A `BGP Update` message sent on such a session contains three fields :
..
.. - the advertised prefix
.. - the `BGP nexthop`
.. - the attributes including the AS-Path 

Supongamos que la sesión BGP que se establece primero es `R1-R2`. Un mensaje `BGP Update` enviado sobre esa sesión contendrá tres campos:

 - El prefijo que se está anunciando
 - El `nexthop` BGP
 - Los atributos, incluyendo el AS-Path 


.. We use the notation `U(prefix, nexthop, attributes)` to represent such a `BGP Update` message in this section. Similarly, `W(prefix)` represents a `BGP withdraw` for the specified prefix. Once the `R1-R2` session has been established, `R1` sends `U(194.100.0.0/24,195.100.0.1,AS10)` to `R2` and `R2` sends `U(194.100.2.0/23,195.100.0.2,AS20)`. At this point, `R1` can reach `194.100.2.0/23` via `195.100.0.2` and `R2` can reach `194.100.0.0/24` via `195.100.0.1`.

En esta sección usaremos la notación `U(prefijo, nexthop, atributos)` para representar dicho mensaje `BGP Update`. Del mismo modo, `W(prefijo)` representará un mensaje `BGP withdraw` para el prefijo especificado. Una vez establecida la sesión `R1-R2`, `R1` envía `U(194.100.0.0/24,195.100.0.1,AS10)` a `R2`, y `R2` envía `U(194.100.2.0/23,195.100.0.2,AS20)`. Llegado este momento, `R1` puede alcanzar `194.100.2.0/23` a través de `195.100.0.2`, y `R2` puede alcanzar `194.100.0.0/24` a través de `195.100.0.1`.

.. Once the `R2-R3` has been established, `R3` sends `U(194.100.1.0/24,195.100.0.6,AS30)`. `R2` announces on the `R2-R3` session all the routes inside its RIB. It thus sends to `R3` : `U(194.100.0.0/24,195.100.0.5,AS20:AS10)` and `U(194.100.2.0/23,195.100.0.5,AS20)`. Note that when `R2` advertises the route that it learned from `R1`, it updates the BGP nexthop and adds its AS number to the AS-Path. `R2` also sends `U(194.100.1.0/24,195.100.0.2,AS20:AS30)` to `R1` on the `R1-R3` session. At this point, all BGP routes have been exchanged and all routers can reach `194.100.0.0/24`, `194.100.2.0/23` and `194.100.1.0/24`.

Una vez establecida la sesión `R2-R3`, `R3` envía `U(194.100.1.0/24,195.100.0.6,AS30)`. `R2` anuncia, sobre la sesión `R2-R3`, todas las rutas contenidas en su RIB. Entonces, envía a `R3` : `U(194.100.0.0/24,195.100.0.5,AS20:AS10)` y `U(194.100.2.0/23,195.100.0.5,AS20)`. Nótese que cuando `R2` anuncia la ruta que aprendió de `R1`, actualiza el nexthop BGP, y agrega su número de AS al AS-Path. `R2` también envía `U(194.100.1.0/24,195.100.0.2,AS20:AS30)` a `R1` sobre la sesión `R1-R3`. En este momento, todas las rutas BGP han sido intercambiadas y todos los routers pueden llegar a `194.100.0.0/24`, `194.100.2.0/23` y `194.100.1.0/24`.

.. If the link between `R2` and `R3` fails, `R3` detects the failure as it did not receive `KEEPALIVE` messages recently from `R2`. At this time, `R3` removes from its RIB all the routes learned over the `R2-R3` BGP session. `R2` also removes from its RIB the routes learned from `R3`. `R2` also sends  `W(194.100.1.0/24)` to `R1` over the `R1-R3` BGP session since it does not have a route anymore towards this prefix.

Si falla el enlace entre `R2` y `R3`, `R3` detectará la falla al no recibir mensajes `KEEPALIVE` recientes de `R2`. En este momento, `R3` elimina de su RIB todas las rutas aprendidas sobre la sesión BGP `R2-R3`. `R2` también elimina de su RIB las rutas aprendidas de `R3`. `R2` envia también  `W(194.100.1.0/24)` a `R1` sobre la sesión BGP `R1-R3` ya que no tiene más una ruta hacia este prefijo.


.. .. note:: Origin of the routes advertised by a BGP router

.. A frequent practical question about the operation of BGP is how a BGP router decides to originate or advertise a route for the first time. In practice, this occurs in two situations :
..
..  - the router has been manually configured by the network operator to always advertise one or several routes on a BGP session. For example, on the BGP session between UCLouvain and its provider, belnet_ , UCLouvain's router always advertises the `130.104.0.0/16` IPv4 prefix assigned to the campus network
..  - the router has been configured by the network operator to advertise over its BGP session some of the routes that it learns with its intradomain routing protocol. For example, an enterprise router may advertise over a BGP session with its provider the routes to remote sites when these routes are reachable and advertised by the intradomain routing protocol
..
.. The first solution is the most frequent. Advertising routes learned from an intradomain routing protocol is not recommended, this is because if the route flaps [#fflap]_, this would cause a large number of BGP messages being exchanged in the global Internet.

.. note:: Origen de las rutas anunciadas por un router BGP

 Una pregunta práctica frecuente sobre la operación de BGP es cómo decide un router BGP originar o anunciar una ruta por primera vez. En la práctica, esto ocurre en dos situaciones:

  - El router ha sido configurado manualmente por el operador de la red para anunciar siempre una o más rutas sobre una sesión BGP. Por ejemplo, sobre la sesión BGP entre UCLouvain y su proveedor, belnet_ , el router de UCLouvain siempre anuncia el prefijo IPv4 `130.104.0.0/16` asignado a la red del campus.
  - El router ha sido configurado por el operador de la red para anunciar sobre su sesión BGP algunas rutas que aprende con su protocolo de ruteo intradominio. Por ejemplo, un router corporativo puede anunciar sobre una sesión BGP con su proveedor las rutas a sitios remotos cuando estas rutas sean alcanzables y anunciadas por el protocolo de ruteo intradominio. 

 La primera solución es la más frecuente. No es recomendable anunciar rutas aprendidas de un protocolo de ruteo intradominio. Esto se debe a que si la ruta oscila (o `hace flap` [#fflap]_), esto causaría una gran cantidad de mensajes BGP intercambiándose por la Internet global. 

.. Most networks that use BGP contain more than one router. For example, consider the network shown in the figure below where `AS20` contains two routers attached to interdomain links : `R2` and `R4`. In this network, two routing protocols are used by `R2` and `R4`. They use an intradomain routing protocol such as OSPF to distribute the routes towards the internal prefixes : `195.100.0.8/30`, `195.100.0.0/30`, ... `R2` and `R4` also use BGP. `R2` receives the routes advertised by `AS10` while `R4` receives the routes advertised by `AS30`. These two routers need to exchange the routes that they have respectively received over their BGP sessions. 

La mayor parte de las redes que usan BGP contienen más de un router. Por ejemplo, consideremos la red que se muestra en la figura siguiente, donde `AS20` contiene dos routers conectados a enlaces interdominio:  `R2` y `R4`. En esta red, `R2` y `R4` utilizan dos protocolos de ruteo. Usan un protocolo de ruteo intradominio, como OSPF, para distribuir las rutas hacia los prefijos internos: `195.100.0.8/30`, `195.100.0.0/30`, ... `R2` y `R4` también usan BGP. `R2` recibe las rutas anunciadas por `AS10` mientras que `R4` recibe las rutas anunciadas por `AS30`. Estos dos routers necesitan intercambiar las rutas que han recibido, respectivamente, sobre sus sesiones BGP.

.. figure:: svg/bgp-larger.*
   :align: center
   :scale: 70
  
   Una red de mayor porte usando BGP 
..   A larger network using BGP

.. A first solution to allow `R2` and `R3` to exchange the interdomain routes that they have learned over their respective BGP sessions would be to configure the intradomain routing protocol to distribute inside `AS20` the routes learned over the BGP sessions. Although current routers support this feature, this is a bad solution for two reasons :

Una primera solución para permitir que `R2` y `R3` intercambien rutas que han aprendido sobre sus respectivas sesiones BGP sería configurar el protocolo de ruteo intradominio para distribuir dentro de `AS20` las rutas aprendidas sobre las sesiones BGP. Aunque los routers corrientes soportan esta característica, es una mala solución por dos razones:

.. 1. Intradomain routing protocols cannot distribute the attributes that are attached to a BGP route. If `R4` received via the intradomain routing protocol a route towards `194.100.0.0/23` that `R2` learned via BGP, it would not know that the route was originated by `AS10` and the only advertisement that it could send to `R3` would contain an incorrect AS-Path
.. 2. Intradomain routing protocols have not been designed to support the hundreds of thousands of routes that a BGP router can receive on today's global Internet.

 1. Los protocolos de ruteo intradominio no pueden distribuir los atributos que se agregan a una ruta BGP. Si `R4` recibiera, a través del protocolo de ruteo intradomino, una ruta hacia `194.100.0.0/23` que `R2` aprendió mediante BGP, no sabría que la ruta fue originada por `AS10` y que el único anuncio que podría enviar a `R3` contendría un AS-Path incorrecto.
 2. Los protocolos de ruteo intradominio no han sido diseñados para soportan los cientos de miles de rutas que puede recibir un router BGP en la Internet global de hoy.


.. index:: eBGP, iBGP

.. The best solution to allow BGP routers to distribute, inside an AS, all the routes learned over BGP sessions is to establish BGP sessions among all the BGP routers inside the AS. In practice, there are two types of BGP sessions :
..
.. - :term:`eBGP` session or `external BGP session`. Such a BGP session is established between two routers that are directly connected and belong to two different domains.
.. - :term:`iBGP` session or `internal BGP session`. Such a BGP session is established between two routers belonging to the same domain. These two routers do not need to be directly connected.

La mejor solución para permitir a los routers BGP distribuir, dentro de un AS, todas las rutas aprendidas por sesiones BGP, es establecer sesiones entre todos los routers BGP dentro del AS. En la práctica, hay dos tipos de sesiones BGP: 

 - Sesión :term:`eBGP` o `sesión BGP externa`. Esta sesión es establecida entre dos routers directamente conectados y pertenecientes a diferentes dominios.
 - Sesión :term:`iBGP` o `sesión BGP externa`. Esta sesión se establece entre dos routers que pertenecen al mismo dominio. Ambos routers no necesitan estar directamente conectados.

.. In practice, each BGP router inside a domain maintains an `iBGP session` with every other BGP router in the domain [#frr]_. This creates a full-mesh of `iBGP sessions` among all BGP routers of the domain. `iBGP sessions`, like `eBGP sessions` run over TCP connections. Note that in contrast with `eBGP sessions` that are established between directly connected routers, `iBGP sessions` are often established between routers that are not directly connected.

En la práctica, cada router BGP dentro de un dominio mantiene una `sesión iBGP` con todos los demás routers BGP en el dominio [#frr]_. Esto crea una trama completamente conectada de sesiones `iBGP` entre todos los routers BGP del dominio. Las sesiones `iBGP`, al igual que las `sesiones eBGP`, corren sobre conexiones TCP. Nótese que, en contraste con las sesiones `eBGP`, que se establecen entre routers directamente conectados, las sesiones `iBGP` suelen establecerse entre routers que no lo están.

.. An important point to note about `iBGP sessions` is that a BGP router only advertises a route over an `iBGP session` provided that :
..
.. - the router uses this route to forward packets, and
.. - the route was learned over one of the router's `eBGP sessions`

Un punto importante a notar sobre las sesiones `iBGP` es que un router BGP sólo anuncia una ruta sobre una sesión `iBGP` cuando: 

 - El roter utiliza esta ruta para reenviar paquetes, y
 - La ruta fue aprendida sobre una de las sesiones `eBGP` del router.

.. A BGP router does not advertise a route that it has learned over an `iBGP session` over another `iBGP session`. Note that a router can, of course, advertise over an `eBGP session` a route that it has learned over an `iBGP session`. This difference between the behaviour of a BGP router over `iBGP` and `eBGP` session is due to the utilisation of a full-mesh of `iBGP sessions`. Consider a network containing three BGP routers : `A`, `B` and `C` interconnected via a full-mesh of iBGP sessions. If router `A` learns a route towards prefix `p` from router `B`, router `A` does not need to advertise the received route to router `C` since router `C` also learns the same route over the `C-B` `iBGP session`.

Un router BGP no anuncia una ruta que ha aprendido sobre una sesión `iBGP` sobre otra sesión `iBGP`. Nótese que un router puede, por supuesto, anunciar sobre una sesión `eBGP` una ruta que ha aprendido sobre una sesión `iBGP`. La diferencia entre la conducta del router BGP sobre las sesiones `iBGP` y `eBGP` se debe a la utilización de una trama completamente conectada de sesiones `iBGP`. Consideremos una red conteniendo tres routers BGP: `A`, `B` y `C`, interconectados a través de una trama completa de sesiones iBGP. Si el router `A` aprende una ruta hacia el prefijo `p` del router `B`, `A` no necesita anunciar la ruta recibida al router `C`, ya que `C` también aprende la misma ruta sobre la sesión `iBGP` `C-B`.

.. To understand the utilisation of an `iBGP session`, let us consider what happens when router `R1` sends `U(194.100.0.0/23,195.100.0.1,AS10)` in the network shown below. This BGP message is processed by `R2` which advertises it over its `iBGP session` with `R4`. The `BGP Update` sent by `R2` contains the same nexthop and the same AS-Path as in the `BGP Update` received by `R2`. `R4` then sends `U(194.100.0.0/23,195.100.0.5,AS20:AS10)` to `R3`. Note that the BGP nexthop and the AS-Path are only updated [#fnexthopself]_ when a BGP route is advertised over an `eBGP session`.

Para comprender la utilización de una sesión `iBGP`, consideremos lo que ocurre cuando el router `R1` envía `U(194.100.0.0/23,195.100.0.1,AS10)` en la red que se muestra a continuación. Este mensaje BGP es procesado por `R2`, quien lo anuncia  sobre su sesión `iBGP` con `R4`. El mensaje `BGP Update` enviado por `R2` contiene el mismo nexthop y el mismo AS-Path que en el mensaje  `BGP Update` recibido por `R2`. `R4` envía entonces `U(194.100.0.0/23,195.100.0.5,AS20:AS10)` a `R3`. nótese que el nexthop BGP y el AS-PATH sólo se actualizan [#fnexthopself]_ cuando una ruta BGP es anunciada sobre una sesión `eBGP`.

.. figure:: svg/ibgp-ebgp.*
   :align: center
   :scale: 70
  
   Sesiones iBGP y eBGP 
..   iBGP and eBGP sessions


.. index:: loopback interface

.. comment:: For me, this note on the loopback isn't quite clear. I remember having trouble with it, when I first read this.

.. .. note:: Loopback interfaces and iBGP sessions
..
.. In addition to their physical interfaces, routers can also be configured with a special loopback interface[#fbgploop]_. A loopback interface is a software interface that is always up. When a loopback interface is configured on a router, the address associated to this interface is advertised by the intradomain routing protocol. Consider for example a router with two point-to-point interfaces and one loopback interface. When a point-to-point interface fails, it becomes unreachable and the router cannot receive anymore packets via this IP address. This is not the case for the loopback interface. It remains reachable as long as at least one of the router's interfaces remains up. `iBGP sessions` are usually established using the router's loopback addresses as endpoints. This allows the `iBGP session` and its underlying TCP connection to remain up even if physical interfaces fail on the routers.

.. note:: Interfaces de loopback y sesiones iBGP

 Además de sus interfaces físicas, los routers también pueden ser configurados con una interfaz especial `de loopback` [#fbgploop]_. Una interfaz de loopback es una interfaz de software, que está siempre activa. Cuando se configura dicha interfaz en un router, la dirección asociada con esta interfaz es anunciada por el protocolo de ruteo intradominio. Consideremos por ejemplo un router con dos interfaces punto a punto y una interfaz de loopback. Cuando falla una interfaz punto a punto, queda inalcanzable, y el router no puede recibir más paquetes a través de esta dirección IP. Éste no es el caso para la interfaz de loopback. Ésta permanece alcanzable mientras al menos una de las demás interfaces del router se mantenga activa. Las sesiones `iBGP` generalmente se establecen usando las direcciones de loopback de los routers como puntos extremos. Esto permite que la sesión `iBGP` y su conexión TCP subyacente se conserven activas aun cuando las interfaces físicas de los routers fallen.


.. comment:: example route not selected ?

Now that routers can learn interdomain routes over iBGP and eBGP sessions, let us examine what happens when router `R3` sends a packet destined to `194.100.1.234`. `R3` forwards this packet to `R4`.  `R4` uses an intradomain routing protocol and BGP. Its BGP routing table contains the following longest prefix match : 

 - `194.100.0.0/23` via `195.100.0.1`

This routes indicates that to forward a packet towards `194.100.0.0/23`, `R4` needs to forward the packet along the route towards `195.100.0.1`. However, `R4` is not directly connected to `195.100.0.1`. `R4` learned a route that matches this address thanks to its intradomain routing protocol that distributed the following routes :

 - `195.100.0.0/30`  via `195.100.0.10`
 - `195.100.0.4/30`  East
 - `195.100.0.8/30`  North
 - `194.100.2.0/23`  via `195.100.0.10`
 - `194.100.0.4/23`  West

To build its forwarding table, `R4` must combine the routes learned from the intradomain routing protocol with the routes learned from BGP. Thanks to its intradomain routing table, for each interdomain route `R4` replaces the BGP nexthop with its shortest path computed by the intradomain routing protocol. In the figure above, `R4` forwards packets to `194.100.0.0/23` via `195.100.0.10` to which it is directly connected via its North interface. `R4` 's resulting forwarding table, which associates an outgoing interface for a directly connected prefix or a directly connected nexthop and an outgoing interface for prefixes learned via BGP, is shown below :

 - `194.100.0.0/23`  via `195.100.0.10` (North)
 - `195.100.0.0/30`  via `195.100.0.10` (North)
 - `195.100.0.4/30`  East
 - `195.100.0.8/30`  North
 - `194.100.2.0/23`  via `195.100.0.10` (North)
 - `194.100.4.0/23`  West

There is thus a coupling between the interdomain and the intradomain routing tables. If the intradomain routes change, e.g. due to link failures or changes in link metrics, then the forwarding table must be updated on each router as the shortest path towards a BGP nexthop may have changed.

The last point to be discussed before looking at the BGP decision process is that a network may contain routers that do not maintain any eBGP session. These routers can be stub routers attached to a single router in the network or core routers that reside on the path between two border routers that are using BGP as illustrated in the figure below.

.. figure:: svg/ibgp-ebgp-2.*
   :align: center
   :scale: 70
   
   How to deal with non-BGP routers ?

In the scenario above, router `R2` needs to be able to forward a packet towards any destination in the `12.0.0.0/8` prefix inside `AS30`. Such a packet would need to be forwarded by router `R5` since this router resides on the path between `R2` and its BGP nexthop attached to `R4`. Two solutions can be used to ensure that `R2` is able to forward such interdomain packets :

 - enable BGP on router `R5` and include this router in the `iBGP` full-mesh. Two iBGP sessions would be added in the figure above : `R2-R5` and `R4-R5`. This solution works and is used by many ASes. However, it forces all routers to have enough resources (CPU and memory) to run BGP and maintain a large forwarding table
 - encapsulate the interdomain packets sent through the AS so that router `R5` never needs to forward a packet whose destination is outside the local AS. Different encapsulation mechanisms exist. MultiProtocol Label Switching (MPLS) :rfc:`3031` and the Layer 2 Tunneling Protocol (L2TP) :rfc:`3931` are frequently used in large domains, but a detailed explanation of these techniques is outside the scope of this section. The simplest encapsulation scheme to understand is in IP in IP defined in :rfc:`2003`. This encapsulation scheme places an IP packet (called the inner packet), including its payload, as the payload of a larger IP packet (called the outer packet). It can be used by border routers to forward packets via routers that do not maintain a BGP routing table. For example, in the figure above, if router `R2` needs to forward a packet towards destination `12.0.0.1`, it can add at the front of this packet an IPv4 header whose source address is set to one of its IPv4 addresses and whose destination address is one of the IPv4 addresses of `R4`. The `Protocol` field of the IP header is set to `4` to indicate that it contains an IPv4 packet. The packet is forwarded by `R5` to `R4` based on the forwarding table that it built thanks to its intradomain routing table. Upon reception of the packet, `R4` removes the outer header and consults its (BGP) forwarding table to forward the packet towards `R3`. 

.. index:: BGP decision process

The BGP decision process
........................

Besides the import and export filters, a key difference between BGP and the intradomain routing protocols is that each domain can define is own ranking algorithm to determine which route is chosen to forward packets when several routes have been learned towards the same prefix. This ranking depends on several BGP attributes that can be attached to a BGP route.


.. index:: BGP local-preference

The first BGP attribute that is used to rank BGP routes is the `local-preference` (local-pref) attribute. This attribute is an unsigned integer that is attached to each BGP route received over an eBGP session by the associated import filter.

When comparing routes towards the same destination prefix, a BGP router always prefers the routes with the highest `local-pref`. If the BGP router knows several routes with the same `local-pref`, it prefers among the routes having this `local-pref` the ones with the shortest AS-Path.

The `local-pref` attribute is often used to prefer some routes over others. This attribute is always present inside `BGP Updates` exchanged over `iBGP sessions`, but never present in the messages exchanged over `eBGP sessions`. 

A common utilisation of `local-pref` is to support backup links. Consider the situation depicted in the figure below. `AS1` would always like to use the high bandwidth link to send and receive packets via `AS2` and only use the backup link upon failure of the primary one.

.. figure:: svg/bgp-backup.*
   :align: center
   :scale: 70
   
   How to create a backup link with BGP ?

As BGP routers always prefer the routes with the highest `local-pref` attribute, this policy can be implemented using the following import filter on `R1`

.. code-block:: text

 import: from  AS2 RA at R1 set localpref=100;
         from  AS2 RB at R1 set localpref=200;
         accept ANY

With this import filter, all the BGP routes learned from `RB` over the high bandwidth links are preferred over the routes learned over the backup link. If the primary link fails, the corresponding routes are removed from `R1`'s RIB and `R1` uses the route learned from `RA`. `R1` reuses the routes via `RB` as soon as they are advertised by `RB` once the `R1-RB` link comes back.

The import filter above modifies the selection of the BGP routes inside `AS1`. Thus, it influences the route followed by the packets forwarded by `AS1`. In addition to using the primary link to send packets, `AS1` would like to receive its packets via the high bandwidth link. For this, `AS2` also needs to set the `local-pref` attribute in its import filter.

.. code-block:: text

  import: from  AS1 R1 at RA set localpref=100;
          from  AS1 R1 at RB set localpref=200;
          accept AS1


Sometimes, the `local-pref` attribute is used to prefer a `cheap` link compared to a more expensive one. For example, in the network below, `AS1` could wish to send and receive packets mainly via its interdomain link with `AS4`.

.. figure:: svg/bgp-prefer.*
   :align: center
   :scale: 70
   
   How to prefer a cheap link over an more expensive one ? 

`AS1` can install the following import filter on `R1` to ensure that it always sends packets via `R2` when it has learned a route via `AS2` and another via `AS4`.

.. code-block:: text

 import: from  AS2 RA at R1 set localpref=100;
         from  AS4 R2 at R1 set localpref=200;
         accept ANY


However, this import filter does not influence how `AS3` , for example, prefers some routes over others. If the link between `AS3` and `AS2` is less expensive than the link between `AS3` and `AS4`, `AS3` could send all its packets via `AS2` and `AS1` would receive packets over its expensive link. An important point to remember about `local-pref` is that it can be used to prefer some routes over others to send packets, but it has no influence on the routes followed by received packets.

Another important utilisation of the `local-pref` attribute is to support the `customer->provider` and `shared-cost` peering relationships. From an economic point of view, there is an important difference between these three types of peering relationships. A domain usually earns money when it sends packets over a `provider->customer` relationship. On the other hand, it must pay its provider when it sends packets over a `customer->provider` relationship. Using a `shared-cost` peering to send packets is usually neutral from an economic perspective. To take into account these economic issues, domains usually configure the import filters on their routers as follows :

 - insert a high `local-pref` attribute in the routes learned from a customer
 - insert a medium `local-pref` attribute in the routes learned over a shared-cost peering
 - insert a low `local-pref` attribute in the routes learned from a provider

With such an import filter, the routers of a domain always prefer to reach destinations via their customers whenever such a route exists. Otherwise, they prefer to use `shared-cost` peering relationships and they only send packets via their providers when they do not know any alternate route. A consequence of setting the `local-pref` attribute like this is that Internet paths are often asymmetrical. Consider for example the internetwork shown in the figure below.

.. figure:: svg/asymetry.*
   :align: center
   :scale: 70
   
   Asymmetry of Internet paths

Consider in this internetwork the routes available inside `AS1` to reach `AS5`. `AS1` learns the `AS4:AS6:AS7:AS5` path from `AS4`, the `AS3:AS8:AS5` path from `AS3` and the `AS2:AS5` path from `AS2`. The first path is chosen since it was from learned from a customer. `AS5` on the other hand receives three paths towards `AS1` via its providers. It may select any of these paths to reach `AS1` , depending on how it prefers one provider over the others.


Coming back to the organisation of a BGP router shown in figure :ref:`bgprouter`, the last part to be discussed is the BGP decision process. The `BGP Decision Process` is the algorithm used by routers to select the route to be installed in the FIB when there are multiple routes towards the same prefix. The BGP decision process receives a set of candidate routes towards the same prefix and uses seven steps. At each step, some routes are removed from the candidate set and the process stops when the set only contains one route [#fbgpmulti]_ :

 1. Ignore routes having an unreachable BGP nexthop
 2. Prefer routes having the highest local-pref
 3. Prefer routes having the shortest AS-Path
 4. Prefer routes having the smallest MED
 5. Prefer routes learned via eBGP sessions over routes learned via iBGP sessions
 6. Prefer routes having the closest next-hop 
 7. Tie breaking rules : prefer routes learned from the router with lowest router id


The first step of the BGP decision process ensures that a BGP router does not install in its FIB a route whose nexthop is considered to be unreachable by the intradomain routing protocol. This could happen, for example, when a router has crashed. The intradomain routing protocol usually advertises the failure of this router before the failure of the BGP sessions that it terminates. This rule implies that the BGP decision process must be re-run each time the intradomain routing protocol reports a change in the reachability of a prefix containing one of more BGP nexthops.

The second rule allows each domain to define its routing preferences. The `local-pref` attribute is set by the import filter of the router that learned a route over an eBGP session. 

In contrast with intradomain routing protocols, BGP does not contain an explicit metric. This is because in the global Internet it is impossible for all domains to agree on a common metric that meets the requirements of all domains. Despite this, BGP routers prefer routes having a short AS-Path attribute over routes with a long AS-Path. This step of the BGP decision process is motivated by the fact that operators expect that a route with a long AS-Path is lower quality than a route with a shorter AS-Path. However, studies have shown that there was not always a strong correlation between the quality of a route and the length of its AS-Path [HFPMC2002]_. 


.. index:: Hot potato routing

Before explaining the fourth step of the BGP decision process, let us first describe the fifth and the sixth steps of the BGP decision process. These two steps are used to implement `hot potato` routing. Intuitively, when a domain implements `hot potato routing`, it tries to forward packets that are destined to addresses outside of its domain, to other domains as quickly as possible. 

To understand `hot potato routing`, let us consider the two domains shown in the figure below. `AS2` advertises prefix `1.0.0.0/8` over the `R2-R6` and `R3-R7` peering links. The routers inside `AS1` learn two routes towards `1.0.0.0/8`: one via `R6-R2` and the second via `R7-R3`.

.. _fig-med:

.. figure:: svg/bgp-med.*
   :align: center
   :scale: 70
   
   Hot and cold potato routing

With the fifth step of the BGP decision process, a router always prefers to use a route learned over an `eBGP session` compared to a route learned over an `iBGP session`. Thus, router `R6` (resp. `R7`)  prefers to use the route via router `R2` (resp. `R3`) to reach prefix `1.0.0.0/8`. 

The sixth step of the BGP decision process takes into account the distance, measured as the length of the shortest intradomain path, between a BGP router and the BGP nexthop for routes learned over `iBGP sessions`. This rule is used on router `R8` in the example above. This router has received two routes towards `1.0.0.0/8`:
 
 - `1.0.0.0/8` via `R7` that is at a distance of `1` from `R8` 
 - `1.0.0.0/8` via `R6` that is at a distance of `50` from `R8`

The first route, via `R7` is the one that router `R8` prefers, as this is the route that minimises the cost of forwarding packets inside `AS1` before sending them to `AS2`.

`Hot potato routing` allows `AS1` to minimise the cost of forwarding packets towards `AS2`. However, there are situations where this is not desirable. For example, assume that `AS1` and `AS2` are domains with routers on both the East and the West coast of the US. In these two domains, the high metric associated to links `R6-R8` and `R0-R2` correspond to the cost of forwarding a packet across the USA. If `AS2` is a customer that pays `AS1`, it would prefer to receive the packets destined to `1.0.0.0/8` via the `R2-R6` link instead of the `R7-R3` link. This is the objective of `cold potato routing`.


.. index:: Multi-Exit Discriminator (MED), Cold potato routing


`Cold potato routing` is implemented using the `Multi-Exit Discriminator (MED)` attribute. This attribute is an optional BGP attribute that may be set [#fmed]_ by border routers when advertising a BGP route over an `eBGP session`. The MED attribute is usually used to indicate over an `eBGP session` the cost to reach the BGP nexthop for the advertised route. The `MED` attribute is set by the router that advertises a route over an `eBGP session`. In the example above, router `R2` sends `U(1.0.0.0/8,R2,AS2,MED=1)` while `R3` sends `U(1.0.0.0/8,R3,AS2,MED=98)`. 

Assume that the BGP session `R7-3` is the first to be established. `R7` sends `U(1.0.0.0/8,R3,AS2,MED=98)` to both `R8` and `R6`. At this point, all routers inside `AS1` send the packets towards `1.0.0.0/8` via `R7-R3`. Then, the `R6-R2` BGP session is established and router `R6` receives `U(1.0.0.0/8,R2,AS2,MED=1)`. Router `R6` runs its decision process for destination `1.0.0.0/8` and selects the route via `R2` as its chosen route to reach this prefix since this is the only route that it knows. `R6` sends `U(1.0.0.0/8,R2,AS2,MED=1)` to routers `R8` and `R7`. They both run their decision process and prefer the route advertised by `R6`, as it contains the smallest `MED`. Now, all routers inside `AS1` forward the packets to `1.0.0.0/8` via link `R6-R2` as expected by `AS2`. As router `R7` no longer uses the BGP route learned via `R3`, it must stop advertising it over `iBGP sessions` and sends `W(1.0.0.0/8)` over its `iBGP sessions` with `R6` and `R8`. However, router `R7` still keeps the route learned from `R3` inside its Adj-RIB-In. If the `R6-R2` link fails, `R6` sends `W(1.0.0.0/8)` over its iBGP sessions and router `R7` responds by sending `U(1.0.0.0/8,R3,AS2,MED=98)` over its iBGP sessions.

In practice, the fifth step of the BGP decision process is slightly more complex, as the routes towards a given prefix can be learned from different ASes. For example, assume that in figure :ref:`fig-med`, `1.0.0.0/8` is also advertised by `AS3` (not shown in the figure) that has peering links with routers `R6` and `R8`. If `AS3` advertises a route whose MED attribute is set to `2` and another with a MED set to `3`, how should `AS1`'s router compare the four BGP routes towards `1.0.0.0/8` ? Is a MED value of `1` from `AS2` better than a MED value of `2` from `AS3` ?  The fifth step of the BGP decision process solves this problem by only comparing the MED attribute of the routes learned from the same neighbour AS. Additional details about the MED attribute may be found in :rfc:`4451`. It should be noted that using the MED attribute may cause some problems in BGP networks as explained in [GW2002]_. In practice, the `MED` attribute is not used on `eBGP sessions` unless the two domains agree to enable it.

.. index: BGP router-id

The last step of the BGP decision allows the selection of a single route when a BGP router has received several routes that are considered as equal by the first six steps of the decision process. This can happen for example in a dual-homed stub attached to two different providers. As shown in the figure below, router `R1` receives two equally good BGP routes towards `1.0.0.0/8`. To break the ties, each router is identified by a unique `router-id` which in practice is one of the IP addresses assigned to the router. On some routers, the lowest router id step in the BGP decision process is replaced by the selection of the oldest route :rfc:`5004`. Preferring the oldest route when breaking ties is used to prefer stable paths over unstable paths. However, a drawback of this approach is that the selection of the BGP routes depends on the arrival times of the corresponding messages. This makes the BGP selection process non-deterministic and can lead to problems that are difficult to debug.

.. figure:: svg/stub-2providers.*
   :align: center
   :scale: 70
   
   A stub connected to two providers


BGP convergence
...............


In the previous sections, we have explained the operation of BGP routers. Compared to intradomain routing protocols, a key feature of BGP is its ability to support interdomain routing policies that are defined by each domain as its import and export filters and ranking process. A domain can define its own routing policies and router vendors have implemented many configuration tweaks to support complex routing policies. However, the routing policy chosen by a domain may interfere with the routing policy chosen by another domain. To understand this issue, let us first consider the simple internetwork shown below.


.. figure:: svg/disagree.*
   :align: center
   :scale: 70
   
   The disagree internetwork 

In this internetwork, we focus on the route towards `1.0.0.0/8` which is advertised by `AS1`. Let us also assume that `AS3` (resp. `AS4`) prefers, e.g. for economic reasons, a route learned from `AS4` (`AS3`) over a route learned from `AS1`. When `AS1` sends `U(1.0.0.0/8,AS1)` to `AS3` and `AS4`, three sequences of exchanges of BGP messages are possible :

 #. `AS3` sends first `U(1.0.0.0/8,AS3:AS1)` to `AS4`. `AS4` has learned two routes towards `1.0.0.0/8`. It runs its BGP decision process and selects the route via `AS3` and does not advertise a route to `AS3`
 #. `AS4` first sends `U(1.0.0.0/8,AS3:AS1)` to `AS3`. `AS3` has learned two routes towards `1.0.0.0/8`. It runs its BGP decision process and selects the route via `AS4` and does not advertise a route to `AS4`
 #. `AS3` sends `U(1.0.0.0/8,AS3:AS1)` to `AS4` and, at the same time, `AS4` sends `U(1.0.0.0/8,AS4:AS1)`.  `AS3` prefers the route via `AS4` and thus sends `W(1.0.0.0/8)` to `AS4`. In the mean time, `AS4` prefers the route via `AS3` and thus sends `W(1.0.0.0/8)` to `AS3`. Upon reception of the `BGP Withdraws`, `AS3` and `AS4` only know the direct route towards `1.0.0.0/8`. `AS3` (resp. `AS4`) sends `U(1.0.0.0/8,AS3:AS1)` (resp. `U(1.0.0.0/8,AS4:AS1)`) to `AS4` (resp. `AS3`). `AS3` and `AS4` could in theory continue to exchange BGP messages for ever. In practice, one of them sends one message faster than the other and BGP converges. 

The example above has shown that the routes selected by BGP routers may sometimes depend on the ordering of the BGP messages that are exchanged. Other similar scenarios may be found in :rfc:`4264`. 

From an operational perspective, the above configuration is annoying since the network operators cannot easily predict which paths are chosen. Unfortunately, there are even more annoying BGP configurations. For example, let us consider the configuration below which is often named `Bad Gadget` [GW1999]_

.. figure:: svg/bad-gadget.*
   :align: center
   :scale: 70
   
   The bad gadget internetwork


In this internetwork, there are four ASes. `AS0` advertises one route towards one prefix and we only analyse the routes towards this prefix. The routing preferences of `AS1`, `AS3` and `AS4` are the following :

 - `AS1` prefers the path `AS3:AS0` over all other paths
 - `AS3` prefers the path `AS4:AS0` over all other paths
 - `AS4` prefers the path `AS1:AS0` over all other paths

`AS0` sends `U(p,AS0)` to `AS1`, `AS3` and `AS4`. As this is the only route known by `AS1`, `AS3` and `AS4` towards `p`, they all select the direct path. Let us now consider one possible exchange of BGP messages :
 
 #. `AS1` sends `U(p, AS1:AS0)` to `AS3` and `AS4`. `AS4` selects the path via `AS1` since this is its preferred path. `AS3` still uses the direct path.
 #. `AS4` advertises `U(p,AS4:AS1:AS0)` to `AS3`.
 #. `AS3` sends `U(p, AS3:AS0)` to `AS1` and `AS4`. `AS1` selects the path via `AS3` since this is its preferred path. `AS4` still uses the path via `AS1`.
 #. As `AS1` has changed its path, it sends `U(p,AS1:AS3:AS0)` to `AS4` and `W(p)` to `AS3` since its new path is via `AS3`. `AS4` switches back to the direct path.
 #. `AS4` sends `U(p,AS4:AS0)` to `AS1` and `AS3`. `AS3` prefers the path via `AS4`.
 #. `AS3` sends `U(p,AS3:AS4:AS0)` to `AS1` and `W(p)` to `AS4`. `AS1` switches back to the direct path and we are back at the first step.

This example shows that the convergence of BGP is unfortunately not always guaranteed as some interdomain routing policies may interfere with each other in complex ways. [GW1999]_ have shown that checking for global convergence is either NP-complete or NP-hard. See [GSW2002]_ for a more detailed discussion.

Fortunately, there are some operational guidelines [GR2001]_ [GGR2001]_ that can guarantee BGP convergence in the global Internet. To ensure that BGP will converge, these guidelines consider that there are two types of peering relationships : `customer->provider` and `shared-cost`. In this case, BGP convergence is guaranteed provided that the following conditions are fulfilled :

 #. The topology composed of all the directed `customer->provider` peering links is an acyclic graph
 #. An AS always prefers a route received from a `customer` over a route received from a `shared-cost` peer or a `provider`.


The first guideline implies that the provider of the provider of `ASx` cannot be a customer of `ASx`. Such a relationship would not make sense from an economic perspective as it would imply circular payments. Furthermore, providers are usually larger than customers.

The second guideline also corresponds to economic preferences. Since a provider earns money when sending packets to one of its customers, it makes sense to prefer such customer learned routes over routes learned from providers. [GR2001]_ also shows that BGP convergence is guaranteed even if an AS associates the same preference to routes learned from a `shared-cost` peer and routes learned from a customer.

From a theoretical perspective, these guidelines should be verified automatically to ensure that BGP will always converge in the global Internet. However, such a verification cannot be performed in practice because this would force all domains to disclose their routing policies (and few are willing to do so) and furthermore the problem is known to be NP-hard [GW1999]. 

In practice, researchers and operators expect that these guidelines are verified [#fgranularity]_ in most domains. Thanks to the large amount of BGP data that has been collected by operators and researchers [#fbgpdata]_, several studies have analysed the AS-level topology of the Internet. [SARK2002]_ is one of the first analysis. More recent studies include [COZ2008]_ and [DKF+2007]_

Based on these studies and [ATLAS2009]_, the AS-level Internet topology can be summarised as shown in the figure below.

.. figure:: svg/bgp-hierarchy.* 
   :align: center
   :scale: 70
   
   The layered structure of the global Internet

.. index:: Tier-1 ISP

The domains on the Internet can be divided in about four categories according to their role and their position in the AS-level topology. 

 - the core of the Internet is composed of a dozen-twenty `Tier-1` ISPs. A `Tier-1` is a domain that has no `provider`. Such an ISP has `shared-cost` peering relationships with all other `Tier-1` ISPs and `provider->customer` relationships with smaller ISPs. Examples of `Tier-1` ISPs include sprint_, level3_ or opentransit_
 - the `Tier-2` ISPs are national or continental ISPs that are customers of `Tier-1` ISPs. These `Tier-2` ISPs have smaller customers and `shared-cost` peering relationships with other `Tier-2` ISPs. Example of `Tier-2` ISPs include France Telecom, Belgacom, British Telecom, ...
 - the `Tier-3` networks are either stub domains such as enterprise or campus networks networks and smaller ISPs. They are customers of Tier-1 and Tier-2 ISPs and have sometimes `shared-cost` peering relationships
 - the large content providers that are managing large datacenters. These content providers are producing a growing fraction of the packets exchanged on the global Internet [ATLAS2009]_. Some of these content providers are customers of Tier-1 or Tier-2 ISPs, but they often try to establish `shared-cost` peering relationships, e.g. at IXPs, with many Tier-1 and Tier-2 ISPs.

Due to this organisation of the Internet and due to the BGP decision process, most AS-level paths on the Internet have a length of 3-5 AS hops. 


.. no note:: BGP security

.. no   explain Youtube attack and briefly discuss the work in SIDR

.. rubric:: Footnotes

.. [#fasnum] An analysis of the evolution of the number of domains on the global Internet during the last ten years may be found in http://www.potaroo.net/tools/asn32/

.. [#fasrank] See http://as-rank.caida.org/ for an  analysis of the interconnections between domains based on measurements collected in the global Internet

.. [#fbgploop] It is important to know that this concept has nothing to do with the loopback interfaces `127.0.0.1` and `::1` of an host. It is unfortunate that one router manufacturer decided to reuse the word loopback with this new meaning.

.. [#fwish] Two routers that are attached to the same IXP only exchange packets when the owners of their domains have an economical incentive to exchange packets on this IXP. Usually, a router on an IXP is only able to exchange packets with a small fraction of the routers that are present on the same IXP.

.. [#fripedb] See ftp://ftp.ripe.net/ripe/dbase for the RIPE database that contains the import and export policies of many European ISPs

.. [#fasdomain] In this text, we consider Autonomous System and domain as synonyms. In practice, a domain may be  divided into several Autonomous Systems, but we ignore this detail. 

.. [#flifetimebgp] The BGP sessions and the underlying TCP connection are typically established by the routers when they boot based on information found in their configuration. The BGP sessions are rarely released, except if the corresponding peering link fails or one of the endpoints crashes or needs to be rebooted. 

.. [#fdefaultkeepalive] 90 seconds is the default delay recommended by :rfc:`4271`. However, two BGP peers can negotiate a different timer during the establishment of their BGP session. Using a too small interval to detect BGP session failures is not recommended. BFD [KW2009]_ can be used to replace BGP's KEEPALIVE mechanism if fast detection of interdomain link failures is required.

.. [#fflap] A link is said to be flapping if it switches several between an operational state and a disabled state within a short period of time. A router attached to such a link would need to frequently send routing messages.

.. [#fnexthopself] Some routers, when they receive a `BGP Update` over an `eBGP session`, set the nexthop of the received route to one of their own addresses. This is called `nexthop-self`. See e.g. [WMS2004]_ for additional details.

.. [#frr] Using a full-mesh of iBGP sessions is suitable in small networks. However, this solution does not scale in large networks containing hundreds or more routers since :math:`\frac{n \times (n-1)}{2}` iBGP sessions must be established in a domain containing :math:`n` BGP routers. Large domains use either Route Reflection :rfc:`4456` or confederations :rfc:`5065` to scale their iBGP, but this goes beyond this introduction.

.. [#fbgpmulti] Some BGP implementations can be configured to install several routes towards a single prefix in their FIB for load-balancing purposes. However, this goes beyond this introduction to BGP.

.. [#fmed] The MED attribute can be used on `customer->provider` peering relationships upon request of the customer. On `shared-cost` peering relationship, the MED attribute is only enabled when there is a explicit agreement between the two peers. 

.. [#fgranularity] Some researchers such as [MUF+2007]_ have shown that modelling the Internet topology at the AS-level requires more than the `shared-cost` and `customer->provider` peering relationships. However, there is no publicly available model that goes beyond these classical peering relationships.

.. [#fbgpdata] BGP data is often collected by establishing BGP sessions between Unix hosts running a BGP daemon and BGP routers in different ASes. The Unix hosts stores all BGP messages received and regular dumps of its BGP routing table. See http://www.routeviews.org, http://www.ripe.net/ris, http://bgp.potaroo.net or http://irl.cs.ucla.edu/topology/


.. [#fpotaroo] Several web sites collect and analyse data about the evolution of BGP in the global Internet. http://bgp.potaroo.net provides lots of statistics and analyses that are updated daily.
