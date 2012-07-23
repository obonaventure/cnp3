.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. index:: RIP, Routing Information Protocol

RIP
---

.. The Routing Information Protocol (RIP) is the simplest routing protocol that was standardised for the TCP/IP protocol suite. RIP is defined in :rfc:`2453`. Additional information about RIP may be found in [Malkin1999]_
El protocolo de Información de Ruteo (`Routing Information Protocol`, RIP) es el protocolo de ruteo más simple que fuera estandarizado para el conjunto de protocolos TCP/IP. RIP se define en :rfc:`2453`. Se puede hallar información adicional sobre RIP en [Malkin1999]_.

.. RIP routers periodically exchange RIP messages. The format of these messages is shown below. A RIP message is sent inside a UDP segment whose destination port is set to `521`. A RIP message contains several fields. The `Cmd` field indicates whether the RIP message is a request or a response. Routers send one of more RIP response messages every 30 seconds. These messages contain the distance vectors that summarize the router's routing table. The RIP request messages can be used by routers or hosts to query other routers about the content of their routing table. A typical usage is when a router boots and quickly wants to receive the RIP responses from its neighbours to compute its own routing table. The current version of RIP is version 2 defined in :rfc:`2453` for IPv4 and :rfc:`2080` for IPv6. 

Los routers RIP intercambian mensajes RIP periódicamente. El formato de estos mensajes se muestra más abajo. Un mensaje RIP se envía dentro de un segmento UDP cuyo puerto destino vale `521`. Un mensaje RIP contiene varios campos. El campo `Command` indica si el mensaje RIP es un requerimiento o una respuesta. Los routers envían uno o más mensajes de respuesta cada 30 seconds. Estos mensajes contienen los vectores de distancia que resumen la tabla de ruteo del router. Los mensajes de requerimiento RIP pueden ser usados por los routers o hosts para consultar a otros routers sobre el contenido de su tabla de ruteo. Un uso típico es cuando un router arranca y quiere rápidamente recibir respuestas RIP de sus vecinos para computar su propia tabla de ruteo. La versión actual de RIP es la versión 2 definida en :rfc:`2453` para IPv4 y :rfc:`2080` para IPv6.

.. These messages contain the distance vectors that summarize the router's routing table. The RIP request messages can be used by routers or hosts to query other routers about the content of their routing table. A typical usage is when a router boots and quickly wants to receive the RIP responses from its neighbours to compute its own routing table. The current version of RIP is version 2 defined in :rfc:`2453` for IPv4 and :rfc:`2080` for IPv6. 

.. figure:: pkt/rip-header.png
   :align: center
   :scale: 100

   Formato de mensajes RIP
..   RIP message format


.. The RIP header contains an authentication field. This authentication can be used by network administrators to ensure that only the RIP messages sent by the routers that they manage are used to build the routing tables. :rfc:`2453` only supports a basic authentication scheme where all routers are configured with the same password and include this password in all RIP messages. This is not very secure since an attacker can know the password by capturing a single RIP message. However, this password can protect against configuration errors. Stronger authentication schemes are described in :rfc:`2082` and :rfc:`4822`, but the details of these mechanisms are outside the scope of this section.

La cabecera RIP contiene un campo de autenticación. Esta autenticación puede ser usada por administradores de red para asegurar que sólo los mensajes RIP enviados por los routers que ellos administran sean los usados para construir las tablas de ruteo. :rfc:`2453` sólo soporta un esquema de autenticación básica donde todos los routers se configuran con la misma password e incluyen esta password en todos los mensajes RIP. Esto no es muy seguro, ya que un atacante puede conocer la password capturando un solo mensaje RIP. Sin embargo esta password puede proteger contra errores de configuración. En :rfc:`2082` y :rfc:`4822` se describen esquemas de autenticación más robustos, pero los detalles de estos mecanismos quedan fuera del alcance de esta sección.

.. Each RIP message contains a set of route entries. Each route entry is encoded as a 20 bytes field whose format is shown below. RIP was initially designed to be suitable for different network layer protocols. Some implementations of RIP were used in XNS or IPX networks. The first field of the RIP route entry is the `Address Family Identifier` (`AFI`). This identifier indicates the type of address found in the route entry [#fafi]_. IPv4 uses `AFI=1`. The other important fields of the route entry are the IPv4 prefix, the netmask that indicates the length of the subnet identifier and is encoded as a 32 bits netmask and the metric. Although the metric is encoded as a 32 bits field, the maximum RIP metric is `15` (for RIP, :math:`16=\infty`)

Cada mensaje RIP contiene un conjunto de elementos de ruta. Cada elemento se codifica como un campo de 20 bytes cuyo formato se muestra más abajo. RIP fue inicialmente diseñado para ser adecuado para diferentes protocolos de capa de Red. Algunas implementaciones de RIP se usaron en redes XNS o IPX. El primer campo del elemento de ruta RIP es el identificador de familia de direcciones (`Address Family Identifier`, AFI). Este identificador indica el tipo de dirección que se encuentra en el elemento de ruta [#fafi]_. IPv4 usa `AFI=1`. Los otros campos importantes del elemento de ruta son el prefijo IPv4, la máscara que indica la longitud del identificador de subred, codificada como una palabra de 32 bits, y una métrica. Aunque la métrica está codificada como un campo de 32 bits, la métrica máxima en RIP es `15` (para RIP, :math:`16=\infty`).

.. figure:: pkt/rip-route-entry.png
   :align: center
   :scale: 100

   Formato de los elementos de ruta IPv4 en RIP (:rfc:`2453`)
..   Format of the RIP IPv4 route entries (:rfc:`2453`)

.. With a 20 bytes route entry, it was difficult to use the same format as above to support IPv6. Instead of defining a variable length route entry format, the designers of :rfc:`2080` defined a new format that does not include an `AFI` field. The format of the route entries used by :rfc:`2080` is shown below. `Plen` is the length of the subnet identifier in bits and the metric is encoded as one byte. The maximum metric is still `15`.

Con un elemento de ruta de 20 bytes, era difícil usar el mismo formato que arriba para soportar IPv6. En lugar de definir un formato de elemento de ruta de longitud variable, los diseñadores de :rfc:`2080` definieron un nuevo formato que no incluye un campo AFI. El formato de los elementos de ruta usado por :rfc:`2080` se muestra más abajo. `Prefix len` es la longitud del identificador de subred en bits y la métrica se codifica sobre un byte. La métrica máxima sigue siendo `15`.

.. figure:: pkt/rip-route-entry-v6.png
   :align: center
   :scale: 100

   Formato de los elementos de ruta RIP IPv6
..   Format of the RIP IPv6 route entries

.. .. note:: A note on timers

..  The first RIP implementations sent their distance vector exactly every 30 seconds. This worked well in most networks, but some researchers noticed that routers were sometimes overloaded because they were processing too many distance vectors at the same time [FJ1994]_. They collected packet traces in these networks and found that after some time the routers' timers became synchronised, i.e. almost all routers were sending their distance vectors at almost the same time. This synchronisation of the transmission times of the distance vectors caused an overload on the routers' CPU but also increased the convergence time of the protocol in some cases. This was mainly due to the fact that all routers set their timers to the same expiration time after having processed the received distance vectors. `Sally Floyd`_ and `Van Jacobson`_ proposed in [FJ1994]_ a simple solution to solve this synchronisation problem. Instead of advertising their distance vector exactly after 30 seconds, a router should send its next distance vector after a delay chosen randomly in the [15,45] interval :rfc:`2080`. This randomisation of the delays prevents the synchronisation that occurs with a fixed delay and is now a recommended practice for protocol designers. 

.. note:: Una nota sobre relojes

  Las primeras implementaciones de RIP enviaban su vector de distancias cada 30 segundos. Esto funcionaba bien en la mayoría de las redes, pero algunos investigadores notaron que los routers a veces se sobrecargaban debido a que procesaban demasiados vectores de distancia a la vez [FJ1994]_. Recogieron trazas de paquetes en estas redes y hallaron que, luego de algún tiempo, los routers se sincronizaban, es decir, casi todos los routers estaban enviando sus vectores de distancia casi al mismo tiempo. Esta sincronización de los tiempos de transmisión de los vectores de distancia causaba una sobrecarga de la CPU de los routers pero también aumentaba el tiempo de convergencia del protocolo en algunos casos. Esto se debía principalmente al hecho de que todos los routers fijaban sus relojes al mismo tiempo de expiración luego de haber procesado los vectores de distancia recibidos.  `Sally Floyd`_ y `Van Jacobson`_ propusieron en [FJ1994]_ una solución simple para resolver este problema de sincronización. En lugar de anunciar el vector de distancias exactamente luego de 30 segundos, cada router debía enviar su propio vector luego de una demora, elegida aleatoriamente en el intervalo [15,45] :rfc:`2080`. Esta aleatorización de las demoras evita la sincronización que ocurre con un retardo fijo y ahora es una práctica recomendada para los diseñadores de protocolos. 


.. rubric:: Footnotes


.. .. [#fafi] The Address Family Identifiers are maintained by IANA at http://www.iana.org/assignments/address-family-numbers/
.. [#fafi] Los Identificadores de Familia de Direcciones son mantenidos por IANA en http://www.iana.org/assignments/address-family-numbers.
