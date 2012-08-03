.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

============
Introducción
============

.. comment:: Second paragraph, first sentence: "Recent estimations...". Suggestion:"Recent estimations have shown continuing growth for over 20 years of the number of hosts connected to the internet". 
.. comment:: First paragraph, third sentence: "In the early 1960s...", is it meant to be "Donald Davies AND Joseph Licklider" or keep the "or"?

.. When the first computers were built during the second world war, they were expensive and isolated. However, after about twenty years, as their prices gradually decreased, the first experiments began to connect computers together. In the early 1960s, researchers including `Paul Baran`_, `Donald Davies`_ or `Joseph Licklider`_ independently published the first papers describing the idea of building computer networks [Baran]_ [Licklider1963]_ . Given the cost of computers, sharing them over a long distance was an interesting idea. In the US, the :term:`ARPANET` started in 1969 and continued until the mid 1980s [LCCD09]_. In France, `Louis Pouzin`_ developed the Cyclades network [Pouzin1975]_. Many other research networks were built during the 1970s [Moore]_. At the same time, the telecommunication and computer industries became interested in computer networks. The telecommunication industry bet on the X25_. The computer industry took a completely different approach by designing Local Area Networks (LAN). Many LAN technologies such as Ethernet or Token Ring were designed at that time. During the 1980s, the need to interconnect more and more computers led most computer vendors to develop their own suite of networking protocols. Xerox developed [XNS]_ , DEC chose DECNet [Malamud1991]_ , IBM developed SNA [McFadyen1976]_ , Microsoft introduced NetBIOS [Winston2003]_ , Apple bet on Appletalk [SAO1990]_ . In the research community, ARPANET was decommissioned and replaced by TCP/IP [LCCD09]_ and the reference implementation was developed inside BSD Unix [McKusick1999]_. Universities who were already running Unix could thus adopt TCP/IP easily and vendors of Unix workstations such as Sun or Silicon Graphics included TCP/IP in their variant of Unix. In parallel, the :term:`ISO`, with support from the governments, worked on developing an open [#fopen]_ Suite of networking protocols. In the end, TCP/IP became the de facto standard that is not only used within the research community. During the 1990s and the early 2000s, the growth of the usage of TCP/IP continued, and today proprietary protocols are seldom used. As shown by the figure below, that provides the estimation of the number of hosts attached to the Internet, the Internet has sustained large growth throughout the last 20+ years.
Cuando se construyeron las primeras computadoras, durante la Segunda Guerra Mundial, eran costosos artefactos que estaban aislados unos de otros. Unos veinte años después, a medida que su precio descendía, comenzaron los primeros experimentos para conectarlas. A principios de los 60, investigadores como `Paul Baran`_, `Donald Davies`_ o `Joseph Licklider`_, publicaron independientemente los primeros papers describiendo la idea de construir redes de computadoras (`networking`) [Baran]_ [Licklider1963]_. Dado el alto costo de las computadoras, la idea de compartirlas cruzando grandes distancias era interesante. En 1969, en los Estados Unidos, se inició el proyecto :term:`ARPANET`, continuando hasta mediados de los 80 [LCCD09]_. En Francia, `Louis Pouzin`_ desarrolló la red Cyclades [Pouzin1975]_. Durante los 70 se construyeron muchas otras redes [Moore]_. Al mismo tiempo, las industrias de las telecomunicaciones y las computadores se interesaron en las redes de computadoras. La industria de las telecomunicaciones apostó a X25_. La industria de la computación tomó un camino completamente diferente, diseñándose Redes de Área Local (`Local Area Networks`, o LANs). Muchas tecnologías de LAN, como Ethernet o Token Ring, se diseñaron en esa época. Durante los 80, la necesidad de interconectar más y más computadoras llevó a la mayoría de los fabricantes de computadoras a desarrollar su propio conjunto de protocolos de redes. Xerox desarrolló [XNS]_ , DEC optó por DECNet [Malamud1991]_ , IBM desarrolló SNA [McFadyen1976]_ , Microsoft introdujo NetBIOS [Winston2003]_ , Apple apostó a Appletalk [SAO1990]_ . En la comunidad de la investigación, ARPANET fue dada de baja y reemplazada por TCP/IP [LCCD09]_, y la implementación de referencia se desarrolló dentro de BSD Unix [McKusick1999]_. Las universidades que ya usaban Unix pudieron así adoptar TCP/IP con facilidad, y los fabricantes de estaciones de trabajo Unix, como Sun y Silicon Graphics, incluyeron TCP/IP dentro de sus variantes de Unix. En paralelo, la organización :term:`ISO`, con soporte de los gobiernos, trabajó para desarrollar un conjunto abierto [#fopen]_ de protocolos de redes. Finalmente, TCP/IP se convirtió en el estándar de facto, usado no solamente en la comunidad científica sino también fuera de ella. Durante los 90 y principios del nuevo siglo, el uso de TCP/IP continuó creciendo, y hoy los protocolos propietarios son raramente usados. Como lo muestra la figura siguiente, donde se ve la estimación de la cantidad de nodos conectados, Internet presenta un crecimiento sostenido durante los últimos 20 años.

.. figure:: png/intro-figures-006-c.png
   :align: center
   :scale: 50 

   Estimación de la cantidad de nodos en Internet
..   Estimation of the number of hosts on the Internet

.. Recent estimations of the number of hosts attached to the Internet show a continuing growth since 20+ years. However, although the number of hosts attached to the Internet is high, it should be compared to the number of mobile phones that are in use today. More and more of these mobile phones will be connected to the Internet. Furthermore, thanks to the availability of TCP/IP implementations requiring limited resources such as uIP_ [Dunkels2003]_, we can expect to see a growth of TCP/IP enabled embedded devices.  

Las estimaciones recientes de la cantidad de nodos conectados a Internet muestra un crecimiento continuo desde hace más de 20 años. Sin embargo, aunque este número es alto, debería compararse con la cantidad de teléfonos móviles que están hoy en uso. Más y más de estos teléfonos móviles serán conectados. Más aún, gracias a la disponibilidad de implementaciones TCP/IP que requieren pocos recursos, como uIP_ [Dunkels2003]_, podemos esperar ver un crecimiento de dispositivos empotrados provistos de TCP/IP. 

.. figure:: png/intro-figures-007-c.png
   :align: center
   :scale: 50 

   Estimación de la cantidad de teléfonos móviles
..   Estimation of the number of mobile phones

.. Before looking at the services provided by computer networks, it is useful to agree on some terminology that is widely used in networking literature. First of all, computer networks are often classified in function of the geographical area that they cover

.. - :term:`LAN` : a local area network typically interconnects hosts that are up to a few or maybe a few tens of kilometers apart. 
.. - :term:`MAN` : a metropolitan area network typically interconnects devices that are up to a few hundred kilometers apart
.. - :term:`WAN` : a wide area network interconnect hosts that can be located anywhere on Earth [#finterplanetary]_

Antes de examinar los servicios provistos por las redes de computadoras, es útil ponernos de acuerdo sobre alguna terminología que es ampliamente usada en la literatura de redes. Para comenzar, las redes se clasifican frecuentemente en función del área geográfica que cubren: 

- :term:`LAN` (`Local Area Network`): una red de área local típicamente interconecta nodos que están una distancia desde unos pocos metros hasta unas pocas decenas de kilómetros. 
- :term:`MAN` (`Metropolitan Area Network`): una red de área metropolitana típicamente interconecta dispositivos que están a una distacia de hasta unos pocos cientos de kilómetros. 
- :term:`WAN` (`Wide Area Network`): una red de área amplia interconecta nodos ubicados en cualquier lugar del planeta [#finterplanetary]_

.. Another classification of computer networks is based on their physical topology. In the following figures, physical links are represented as lines while boxes show computers or other types of networking equipment.

Otra clasificación de las redes de computadoras se basa en su topología física. En las siguientes figuras, los enlaces físicos están representados como líneas, mientras que las cajas indican computadoras u otros tipos de equipamiento de redes. 

.. Computer networks are used to allow several hosts to exchange information between themselves. To allow any host to send messages to any other host in the network, the easiest solution is to organise them as a full-mesh, with a direct and dedicated link between each pair of hosts. Such a physical topology is sometimes used, especially when high performance and high redundancy is required for a small number of hosts. However, it has two major drawbacks :

Las redes de computadoras se usan para permitir que varios nodos intercambien información entre ellos. Para que cualquier nodo pueda enviar mensajes a cualquier otro nodo de la red, la solución más fácil es organizarlos como una malla completa (`full mesh`), con un enlace dedicado y directo entre cada par de nodos. A veces se usa esta topología física, especialmente cuando se requiere alta velocidad y alta redundancia, para un conjunto pequeño de nodos. Sin embargo, tiene dos desventajas:

.. - for a network containing `n` hosts, each host must have `n-1` physical interfaces. In practice, the number of physical interfaces on a node will limit the size of a full-mesh network that can be built
.. - for a network containing `n` hosts, :math:`\frac{n \times (n-1)}{2}` links are required. This is possible when there are a few nodes in the same room, but rarely when they are located several kilometers apart

- Para una red que contiene `n` nodos, cada nodo debe tener `n-1` interfaces físicas. En la práctica, la cantidad de interfaces físicas en un nodo limitará el tamaño de la red de malla completa que se pueda construir.
- Para una red que contiene `n` nodos, se requieren :math:`\frac{n \times (n-1)}{2}` enlaces. Esto es posible cuando hay unos pocos nodos en el mismo recinto, pero raramente lo es cuando están ubicados a varios kilómetros uno del otro.

.. figure:: svg/fullmesh.*
   :align: center
   :scale: 50

   Una red de malla completa 
..   A Full mesh network

.. The second possible physical organisation, which is also used inside computers to connect different extension cards, is the bus. In a bus network, all hosts are attached to a shared medium, usually a cable through a single interface. When one host sends an electrical signal on the bus, the signal is received by all hosts attached to the bus. A drawback of bus-based networks is that if the bus is physically cut, then the network is split into two isolated networks.  For this reason, bus-based networks are sometimes considered to be difficult to operate and maintain, especially when the cable is long and there are many places where it can break. Such a bus-based topology was used in early Ethernet networks. 

La segunda organización física posible, que también se usa dentro de las computadoras para conectar diferentes tarjetas de extensión, es el `bus`. En una red de bus, todos los nodos están conectados a un medio compartido, generalmente un cable, a través de una única interfaz. Cuando un nodo envía una señal eléctrica al bus, ésta es recibida por todos los nodos conectados al mismo. Una desventaja de las redes basadas en bus es que, si el bus se interrumpe físicamente, entonces la red queda desconectada en dos redes aisladas. Por este motivo, las redes basadas en bus a veces se consideran difíciles de operar y mantener, especialmente cuando el cable es largo y hay muchos lugares donde puede romperse. Esta topología basada en bus fue usada antiguamente en las redes Ethernet. 

.. figure:: svg/bus.*
   :align: center
   :scale: 50 

   Una red organizada en bus
..   A network organised as a Bus

.. A third organisation of a computer network is a star topology. In such topologies, hosts have a single physical interface and there is one physical link between each host and the center of the star. The node at the center of the star can be either a piece of equipment that amplifies an electrical signal, or an active device, such as a piece of equipment that understands the format of the messages exchanged through the network. Of course, the failure of the central node implies the failure of the network. However, if one physical link fails (e.g. because the cable has been cut), then only one node is disconnected from the network. In practice, star-shaped networks are easier to operate and maintain than bus-shaped networks. Many network administrators also appreciate the fact that they can control the network from a central point. Administered from a Web interface, or through a console-like connection, the center of the star is a useful point of control (enabling or disabling devices) and an excellent observation point (usage statistics).

Una tercera forma de organización de una red de computadoras es la topología de `estrella`. En estas topologías, los nodos tienen una única interfaz física y hay un único enlace entre cada nodo y el centro de la estrella. El nodo central puede ser una pieza de equipamiento que amplifica señales eléctricas, o un dispositivo activo que comprenda el formato de los mensajes intercambiados a través de la red. Por supuesto, la falla del nodo central implica la falla de la red completa. Sin embargo, si un enlace físico falla (por ejemplo, porque el cable ha sido dañado), entonces sólo un nodo queda desconectado de la red. En la práctica, las redes con forma de estrella son más fáciles de operar y mantener que las redes en forma de bus. Muchos administradores de red aprecian el hecho de que pueden controlar la red desde un punto central. Administrado desde una interfaz web, o a través de una conexión de tipo consola, el centro de la estrella es un punto de control ideal para habilitar o deshabilitar dispositivos y un excelente punto de observación (para recabar estadísticas de uso).

.. figure:: svg/star.*
   :align: center
   :scale: 50 

   Una red organizada en estrella
..   A network organised as a Star

.. comment:: Just an observation: "Ring" here has a capital "R", while the other example, "bus","star" had lower case
.. comment:: I think this paragraph can be improved.

.. A fourth physical organisation of a network is the Ring topology. Like the bus organisation, each host has a single physical interface connecting it to the ring. Any signal sent by a host on the ring will be received by all hosts attached to the ring. From a redundancy point of view, a single ring is not the best solution, as the signal only travels in one direction on the ring; thus if one of the links composing the ring is cut, the entire network fails. In practice, such rings have been used in local area networks, but are now often replaced by star-shaped networks. In metropolitan networks, rings are often used to interconnect multiple locations. In this case, two parallel links, composed of different cables, are often used for redundancy. With such a dual ring, when one ring fails all the traffic can be quickly switched to the other ring.

Una cuarta organización física de una red es la topología de anillo. Como en la organización de bus, cada nodo tiene una única interfaz física conectándolo al anillo. Cualquier señal enviada por un host sobre el anillo será recibida por todos los nodos conectados al anillo. Desde el punto de vista de la redundancia, un anillo único no es la mejor solución, ya que la señal recorre el anillo en un solo sentido. Así, si se corta uno de los enlaces que componen el anillo, toda la red falla. En la práctica, estos anillos han sido usados en redes de área local, pero actualmente están siendo reemplazados por redes de estrella. En redes metropolitanas, los anillos suelen usarse para interconectar múltiples sitios. En este caso, frecuentemente se usan dos anillos paralelos compuestos por diferentes cables, para ofrecer redundancia. Con estos anillos duales, cuando falla uno, todo el tráfico se desplaza rápidamente al segundo. 

.. figure:: svg/ring.*
   :align: center
   :scale: 50 

   Una red organizada en anillo
..   A network organised as a Ring

.. A fifth physical organisation of a network is the tree. Such networks are typically used when a large number of customers must be connected in a very cost-effective manner. Cable TV networks are often organised as trees.

Una quinta organización física de una red es el árbol. Estas redes se usan típicamente cuando debe conectarse un gran número de sistemas en una forma muy efectiva en costo. Las redes de TV cable frecuentemente se organizan en árbol.

.. figure:: svg/tree.*
   :align: center
   :scale: 50 

   Una red organizada en árbol
..   A network organised as a Tree
   
.. In practice, most real networks combine part of these topologies. For example, a campus network can be organised as a ring between the key buildings, while smaller buildings are attached as a tree or a star to important buildings. Or an ISP network may have a full mesh of devices in the core of its network, and trees to connect remote users.

En la práctica, la mayoría de las redes reales combinan partes de estas topologías. Por ejemplo, una red de un campus puede estar organizada en anillo entre los edificios principales, con edificios más pequeños conectados, en árbol o en estrella, a los edificios importantes. O bien, un proveedor de acceso a Internet puede tener una malla completa de dispositivos en el núcleo de su red, con árboles para conectar los usuarios remotos. 

.. comment:: It feels like there is something missing in the following sentence.. necessary for the network to what? function? operate? for the network to be created?

.. Throughout this book, our objective will be to understand the protocols and mechanisms that are necessary for a network such as the one shown below.

A lo largo de este libro, nuestro objetivo será comprender los protocolos y mecanismos que son necesarios para la operación de una red como la que se muestra más abajo. 

.. figure:: svg/internetwork.*
   :align: center
   :scale: 75

   Una red interconectada simple
..   A simple internetwork

.. The figure above illustrates an internetwork, i.e. a network that interconnects other networks. Each network is illustrated as an ellipse containing a few devices. We will explain throughout the book the different types of devices and their respective roles enabling all hosts to exchange information. As well as this, we will discuss how networks are interconnected, and the rules that guide these interconnections. We will also analyse how the bus, ring and mesh topologies are used to build real networks.

La figura anterior muestra una red interconectada (o `internetwork`), es decir, una red que interconecta a otras redes. Cada red se ilustra como una elipse conteniendo un conjunto de dispositivos. Explicaremos a lo largo del libro los diferentes tipos de dispositivos, y sus roles respectivos, que posibilitan que todos los nodos intercambien información. Además discutiremos cómo se interconectan las redes, y las reglas que guían estas interconexiones. También analizaremos cómo se usan las topologías de bus, anillo y malla, para construir las redes del mundo real.

.. The last point of terminology we need to discuss is the transmission modes. When exchanging information through a network, we often distinguish between three transmission modes. In TV and radio transmission, :term:`broadcast` is often used to indicate a technology that sends a video or radio signal to all receivers in a given geographical area. Broadcast is sometimes used in computer networks, but only in local area networks where the number of recipients is limited.

El último punto de la terminología que necesitamos examinar es el relativo a los modos de transmisión. Cuando se intercambia información a través de una red, con frecuencia distinguimos entre tres modos de transmisión. En la transmisión de TV o de radio suele usarse el término `difusión` o :term:`broadcast` para indicar una tecnología que envía una señal de radio o video a todos los receptores en un área geográfica dada. El `broadcast` a veces se usa en las redes de computadoras, pero sólo en las redes de área local, donde el numero de receptores es limitado.

.. The first and most widespread transmission mode is called :term:`unicast` . In the unicast transmission mode, information is sent by one sender to one receiver. Most of today's Internet applications rely on the unicast transmission mode. The example below shows a network with two types of devices : hosts (drawn as computers) and intermediate nodes (drawn as cubes). Hosts exchange information via the intermediate nodes. In the example below, when host `S` uses unicast to send information, it sends it via three intermediate nodes. Each of these nodes receives the information from its upstream node or host, then processes and forwards it to its downstream node or host. This is called `store and forward` and we will see later that this concept is key in computer networks.

El primer modo de transmisión, y el más extendido, es el llamado :term:`unicast`. En el modo de transmisión `unicast`, la información es enviada desde un emisor a un receptor. La mayoría de las aplicaciones de Internet actuales descansan sobre el modo de transmisión unicast. El ejemplo siguiente muestra una red con dos tipos de dispositivos: `hosts` (dibujados como computadoras), y nodos intermedios (dibujados como cubos). Los `hosts` intercambian información a través de los nodos intermedios. En el ejemplo, cuando el host `S` usa unicast para enviar información, lo hace mediante tres nodos intermedios. Cada uno de estos nodos recibe la información desde su nodo o host anterior en el flujo de la información, luego la procesa y la reenvía a su nodo o host siguiente. Esta operación se llama `almacenamiento y reenvío` (`store and forward`), y como veremos más adelante es un concepto clave en redes de computadoras. 

.. figure:: svg/unicast.*
   :align: center
   :scale: 50

   Transmisión unicast
..   Unicast transmission

.. A second transmission mode is :term:`multicast` transmission mode. This mode is used when the same information must be sent to a set of recipients. It was first used in LANs but later became supported in wide area networks. When a sender uses multicast to send information to `N` receivers, the sender sends a single copy of the information and the network nodes duplicate this information whenever necessary, so that it can reach all recipients belonging to the destination group.  

Un segundo modo de transmisión es llamado :term:`multicast`. Este modo se usa cuando la misma información debe ser enviada a un conjunto de destinatarios. Fue primero usado en LANs, pero más tarde fue soportada por las redes WAN. Cuando un emisor usa multicast para enviar información a `N` receptores, envía una única copia de la información, y los nodos replican esta información donde sea necesario para alcanzar a todos los destinatarios pertenecientes al grupo. 

.. figure:: svg/multicast.*
   :align: center
   :scale: 50 

   Transmisión multicast
..   Multicast transmission

.. To understand the importance of multicast transmission, consider source `S` that sends the same information to destinations `A`, `C` and `E`. With unicast, the same information passes three times on intermediate nodes `1` and `2` and twice on node `4`. This is a waste of resources on the intermediate nodes and on the links between them. With multicast transmission, host `S` sends the information to node `1` that forwards it downstream to node `2`. This node creates a copy of the received information and sends one copy directly to host `E` and the other downstream to node `4`. Upon reception of the information, node `4` produces a copy and forwards one to node `A` and another to node `C`. Thanks to multicast, the same information can reach a large number of receivers while being sent only once on each link.

Para comprender la importancia de la transmisión multicast, consideremos el origen `S` que envía la misma información a los destinos `A`, `C` y `E`. Con unicast, la misma infofmación pasa tres veces por los nodos intermedios `1` y `2`, y dos veces por el nodo `4`. Esto es un desperdicio de recursos en los nodos intermedios y en los enlaces entre ellos. Con transmisión multicast, el host `S` envía la información al nodo `1`, quien la reenvía al nodo `2`. Este nodo crea una copia de la información recibida, enviando una copia directamente al host `E` y la otra al nodo `4`. Al recibir la información, el nodo `4` produce una copia y reenvía una al nodo `A` y otra al nodo `C`. Gracias al multicast, la misma información puede alcanzar un gran número de receptores aun cuando sea enviada sólo una vez por cada enlace.

.. The last transmission mode is the :term:`anycast` transmission mode. It was initially defined in :rfc:`1542`. In this transmission mode, a set of receivers is identified. When a source sends information towards this set of receivers, the network ensures that the information is delivered to `one` receiver that belongs to this set. Usually, the receiver closest to the source is the one that receives the information sent by this particular source. The anycast transmission mode is useful to ensure redundancy, as when one of the receivers fails, the network will ensure that information will be delivered to another receiver belonging to the same group. However, in practice supporting the anycast transmission mode can be difficult.

El último modo de transmisión es llamado :term:`anycast`. Inicialmente fue definido en :rfc:`1542`. En este modo de transmisión, se identifica un conjunto de receptores. Cuando un origen envía información hacia este conjunto de receptores, la red asegura que la información sea enviada a `un` receptor que pertenezca al conjunto. Usualmente, quien recibe la información es el receptor más cercano al origen. La transmisión anycast es útil para ofrecer redundancia, ya que cuando uno de los receptores falle, la red asegurará que la información sea enviada a otro receptor del mismo grupo. Sin embargo, en la práctica, soportar el modo de transmisión anycast puede ser difícil.

.. figure:: svg/anycast.*
   :align: center
   :scale: 50 

   Transmisión anycast
..   Anycast transmission

.. In the example above, the three hosts marked with `*` are part of the same anycast group. When host `S` sends information to this anycast group, the network ensures that it will reach one of the members of the anycast group. The dashed lines show a possible delivery via nodes `1`, `2` and `4`. A subsequent anycast transmission from host `S` to the same anycast group could reach the host attached to intermediate node `3` as shown by the plain line. An anycast transmission reaches a member of the anycast group that is chosen by the network in function of the current network conditions. 

En el ejemplo anterior, los tres hosts marcados con `*` son parte del mismo grupo anycast. Cuando el host `S` envía información a este grupo anycast, la red asegura que ésta llegue a uno de los miembros del grupo anycast. Las líneas punteadas muestran una entrega posible, a través de los nodos `1`, `2` y `4`. Una transmisión posterior desde el host `S` al mismo grupo anycast podría llegar al host conectado al nodo intermedio `3`, como indica la línea llena. Una transmisión anycast llega a un miembro cualquiera del grupo, que es elegido por la red en función de las condiciones que estén vigentes en la red en un momento dado.

.. rubric:: Footnotes


.. .. [#fopen] Open in ISO terms was in contrast with the proprietary protocol suites whose specification was not always publicly available. The US government even mandated the usage of the OSI protocols (see :rfc:`1169`), but this was not sufficient to encourage all users to switch to the OSI protocol suite that was considered by many as too complex compared to other protocol suites.

.. [#fopen] "`Abierto`", en términos de la organización ISO, se entendía como opuesto a los conjuntos de protocolos propietarios cuya especificación no siempre estaba públicamente disponible. El gobierno de Estados Unidos hizo obligatorio el uso de los protocolos OSI (ver :rfc:`1169`), pero esto no fue suficiente para alentar a los usuarios a mudarse al conjunto de protocolos OSI, que muchos consideraban demasiado complejo comparado con otros.

.. .. [#finterplanetary] In this book, we focus on networks that are used on Earth. These networks sometimes include satellite links. Besides the network technologies that are used on Earth, researchers develop networking techniques that could be used between nodes located on different planets. Such an Inter Planetary Internet requires different techniques than the ones discussed in this book. See :rfc:`4838` and the references therein for information about these techniques. 

.. [#finterplanetary] En este libro nos enfocamos en las redes que se usan en el planeta Tierra. Estas redes a veces incluyen enlaces satelitales. Además de las tecnologías de redes usadas en la Tierra, los investigadores desarrollan técnicas de conectividad que podrían ser usadas entre nodos ubicados en diferentes planetas. Una `Internet Interplanetaria` requiere técnicas diferentes a las discutidas en este libro. Véase :rfc:`4838` y las referencias allí contenidas para mayor información sobre estas técnicas.

.. .. include:: services-protocols.rst
.. .. include:: referencemodels.rst
.. .. include:: organisation.rst


.. include:: ../links.rst


