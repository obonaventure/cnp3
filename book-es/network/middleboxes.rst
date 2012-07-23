.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. _Middleboxes:

Middleboxes
===========

.. index:: Middlebox

.. When the TCP/IP architecture and the IP protocol were defined, two type of devices were considered in the network layer : endhosts and routers. Endhosts are the sources and destinations of IP packets while routers forward packets. When a router forwards an IP packet, it consults its forwarding table, updates the packet's TTL, recomputes its checksum and forwards it to the next hop. A router does not need to read or change the contents of the packet's payload.

Cuando se definieron la arquitectura TCP/IP y el protocolo IP, se consideraron dos tipos de dispositivos en la Capa de Red: sistemas finales y routers. Los sistemas finales son el origen y destino de los paquetes IP, mientras que los routeres reenvían los paquetes. Cuando un router reenvía un paquete IP, consulta su tabla de ruteo, actualiza el tiempo de vida (`TTL`) del paquete, recomputa su checksum y lo reenvía al siguiente punto de conmutación. Un router no necesita leer ni modificar los contenidos de la carga útil del paquete.

.. However, in today's Internet, there exist devices that are not strictly routers but which process, sometimes modify, and forward IP packets. These devices are often called `middleboxes` :rfc:`3234`. Some middleboxes only operate in the network layer, but most middleboxes are able to analyse the payload of the received packets and extract the transport header, and in some cases the application layer protocols.  
  
Sin embargo, en la Internet de hoy, existen dispositivos que no son estrictamente routers sino que procesan los paquetes IP, a veces modificándolos, y luego los reenvían. Estos dispositivos suelen ser llamados `middleboxes` :rfc:`3234`. Algunos  middleboxes sólo operan en la Capa de Red, pero la mayoría son capaces de analizar la carga útil de los paquetes recibidos y extraer la cabecera de transporte, y en algunos casos, de los protocolos de Capa de Aplicación.

.. figure:: png/network-fig-161-c.png
   :align: center
   :scale: 70
  
   Middleboxes IP y el modelo de referencia 
..   IP middleboxes and the reference model

.. In this section, we briefly describe two type of middleboxes : firewalls and network address translation (NAT) devices. A discussion of the different types of middleboxes with references may be found in :rfc:`3234`.

En esta sección describiremos brevemente dos tipos de middleboxes: `firewalls` (o `cortafuegos`) y dispositivos `NAT` (de `Network Address Translation`, `traducción de direcciones de red`). Se puede encontrar una discusión de los diferentes tipos de middleboxes, con referencias, en :rfc:`3234`.

.. index:: firewall

Firewalls
---------

.. When the Internet was only a research network interconnecting research labs, security was not a concern, and most hosts agreed to exchange packets over TCP connections with most other hosts. However, as more and more users and companies became connected to the Internet, allowing unlimited access to hosts that they managed started to concern companies. Furthermore, at the end of the 1980s, several security issues affected the Internet, such as the first Internet worm [RE1989]_ and some widely publicised security breaches [Stoll1988]_ [CB2003]_ [Cheswick1990]_ .

Mientras Internet no era más que una red experimental que interconectaba laboratorios de investigación, la seguridad informática no era una preocupación, y la mayoría de los hosts estaban de acuerdo en intercambiar paquetes sobre conexiones TCP con la mayoría de los demás. Sin embargo, a medida que se conectaron más y más usuarios y organizaciones, permitir el acceso ilimitado a los hosts empezó a convertirse en un riesgo. Además, a fines de los años 80, Internet se vio afectada por varios problemas de seguridad, tales como el primer gusano de Internet  [RE1989]_ y algunas intrusiones que recibieron amplia publicidad [Stoll1988]_ [CB2003]_ [Cheswick1990]_.
    
.. These security problems convinced the industry that IP networks are a key part of a company's infrastructure, that should be protected by special devices like security guards and fences are used to protect buildings. These special devices were quickly called `firewalls`. A typical firewall has two interfaces :
 
..  - an external interface connected to the global Internet
..  - an internal interface connected to a trusted network

Estos problemas de seguridad convencieron a la industria de que las redes IP eran una parte clave de la infraestructura de las organizaciones, y que debían ser protegidas por dispositivos especiales del mismo modo que se usan guardias de seguridad y muros para proteger los edificios. Estos dispositivos especiales fueron rápidamente bautizados como `cortafuegos` (`firewalls`). Un firewall típico tiene dos interfaces:
 
  - Una interfaz externa conectada a la Internet global
  - Una interfaz interna conectada a la red protegida

.. The first firewalls included configurable packet filters. A packet filter is a set of rules defining the security policy of a network. In practice, these rules are based on the values of fields in the IP or transport layer headers. Any field of the IP or transport header can be used in a firewall rule, but the most common ones are:

.. - filter on the source address. For example, a company may decide to discard all packets received from one of its competitors. In this case, all packets whose source address belong to the competitor's address block would be rejected 
.. - filter on destination address. For example, the hosts of the research lab of a company may receive packets from the global Internet, but not the hosts of the financial department
.. - filter on the `Protocol` number found in the IP header. For example, a company may only allow its hosts to use TCP or UDP, but not other, more experimental, transport protocols
.. - filter on the TCP or UDP port numbers. For example, only the DNS server of a company should received UDP segments whose destination port is set to `53` or only the official SMTP servers of the company can send TCP segments whose source ports are set to `25`
.. - filter on the TCP flags. For example, a simple solution to prohibit external hosts from opening TCP connections with hosts inside the company is to discard all TCP segments received from the external interface with only the `SYN` flag set.

Los primeros firewalls incluían filtros de paquetes configurables. Un filtro de paquetes es un conjunto de reglas que define la política de seguridad de una red. En la práctica, estas reglas se basan en valores de campos en las cabeceras de IP o de transporte. Cualquier campo de estas cabeceras puede ser usado en una regla de firewall, pero las más comunes son las siguientes.

 - Filtrar por dirección origen. Por ejemplo, una empresa puede elegir descartar todos los paquetes recibidos de uno de sus competidores. En este caso, todos los paquetes cuya dirección origen pertenece al bloque de direcciones del competidor serán rechazados.
 - Filtrar por dirección destino. Por ejemplo, los hosts del laboratorio de investigación de una compañía pueden recibir paquetes de la Internet global, pero no los hosts del departamento de finanzas.
 - Filtrar por número de protocolo que se encuentra en la cabecera IP. Por ejemplo, una compañía puede permitir a sus hosts sólo el uso de TCP o UDP, pero no de otros protocolos de transporte, de tipo más experimental.
 - Filtrar por los números de puerto TCP o UDP. Por ejemplo, sólo el servidor DNS de una organización debería recibir segmentos UDP cuyo puerto destino es `53`; o bien, sólo los servidores SMTP oficiales de la organización pueden enviar segmentos TCP cuyo puerto origen sea `25`.
 - Filtrar por las señales o `flags` de TCP. Por ejemplo, una solución simple para prohibir a los hosts externos que abran conexiones con hosts dentro de la compañía es descartar todos los segmentos TCP recibidos por la interfaz externa con sólo el flag `SYN` activo.

.. Such firewalls are often called `stateless` firewalls because they do not maintain any state about the TCP connections that pass through them.
Dichos firewalls suelen ser llamados firewalls `sin estado` o `stateless` porque no mantienen ninguna información de estado relativa a las conexiones TCP que los atraviesan. 

.. Another type of firewalls are `stateful` firewalls. A stateful firewall tracks the state of each TCP connection passing through it and maintains a TCB for each of these TCP connection. This TCB allows it to reassemble the received segments in order to extract their payload and perform verifications in the application layer. Some firewalls are able to inspect the URLs accessed using HTTP and log all URLs visited or block TCP connections where a dangerous URL is exchanged. Some firewalls can verify that SMTP commands are used when a TCP connection is established on port `25` or that a TCP connection on port `80` carries HTTP commands and responses. 

Otro tipo de firewalls son los firewalls `con estado` o `stateful`. Un firewall con estado mantiene el estado de cada conexión TCP que lo atraviesa, y mantiene un TCB para cada una de estas conexiones TCP. Este TCB le permite reensamblar los segmentos recibidos para extraer la carga útil y ejecutar verificaciones en la capa de aplicación. Algunos firewalls son capaces de inspeccionar los URLs accedidos usando HTTP, y crear un registro de todos los URLs visitados, o bloquear conexiones TCP cuando se accede a un URL peligroso. Algunos pueden verificar que se usen comandos SMTP válidos cuando se establece una conexión TCP por el puerto `25`, o que una conexión TCP por el puerto `80` transporte comandos y respuestas HTTP.


.. .. note:: Beyond firewalls

..  Apart from firewalls, different types of "security" devices have been installed at the periphery of corporate networks. Intrusion Detection Systems (IDS), such as the popular snort_ , are stateful devices that are capable of matching reassembled segments against regular expressions corresponding to signatures of viruses, worms or other types of attacks. Deep Packet Inspection (DPI) is another type of middlebox that analyses the packet's payload and is able to reassemble TCP segments in order to detect inappropriate usages. While IDS are mainly used in corporate networks, DPI is mainly used in Internet Service Providers. Some ISPs use DPI to detect and limit the bandwidth consumed by peer-to-peer applications. Some countries such as China or Iran use DPI to detect inappropriate Internet usage.

.. note:: Mas allá de los firewalls

  Además de firewalls, diferentes tipos de dispositivos de "seguridad" han sido instalados en la periferia de las redes corporativas. Los Sistemas de Detección de Intrusiones (`Intrusion Detection Systems`, IDS), como el popular snort_, son dispositivos con estado capaces de buscar coincidencias, en los segmentos reensamblados, con expresiones regulares que corresponden a signaturas de virus, gusanos u otros tipos de ataques. Los middleboxes de Inspección Profunda de Paquetes (`Deep Packet Inspection`, DPI) son otro tipo de middlebox que analiza la carga útil de los paquetes y es capaz de reensamblar segmentos TCP detectando usos inapropiados. Mientras que los IDS son usados principalmente en redes corporativas, los dispositivos DPI suelen ser usados por los Proveedores de Servicios de Internet (ISPs). Algunos ISPs usan DPI para evaluar y limitar el ancho de banda consumido por las aplicaciones peer-to-peer. Algunos países como China o Irán usan DPI para detectar uso inapropiado de Internet.

.. index:: Network Address Translation, NAT

NAT
---

.. Network Address Translation (NAT) was proposed in [TE1993]_ and :rfc:`3022` as a short term solution to deal with the expected shortage of IPv4 addresses in the late 1980s - early 1990s. Combined with CIDR, NAT helped to significantly slow down the consumption of IPv4 addresses. A NAT is a middlebox that interconnects two networks that are using IPv4 addresses from different addressing spaces. Usually, one of these addressing spaces is the public Internet while the other is using the private IPv4 addresses defined in :rfc:`1918`.

La Traducción de Direcciones de Red (`Network Address Translation`, NAT) fue propuesta en [TE1993]_ y :rfc:`3022` como una solución de corto plazo para enfrentar el previsible agotamiento de las direcciones IPv4 a fines de los años 80 y principios de los 90. Combinada con CIDR, NAT ayudó a retardar significativamente el consumo de direcciones IPv4. Un dispositivo NAT es un middlebox que inteconecta  dos redes que usan direcciones IPv4 de diferentes espacios de direccionamiento. Por lo común, uno de estos espacios de direccionamiento es la Internet pública, mientras que el otro usa las direcciones privadas IPv4 definidas en :rfc:`1918`.

.. A very common deployment of NAT is in broadband access routers as shown in the figure below. The broadband access router interconnects a home network, either WiFi or Ethernet based, and the global Internet via one ISP over ADSL or CATV. A single IPv4 address is allocated to the broadband access router and network address translation allows all of the hosts attached to the home network to share a single public IPv4 address.
Una implantación muy común de NAT ocurre en routers de acceso como se muestra en la figura siguiente. El router de acceso interconecta una red doméstica, ya sea basada en WiFi o en Ethernet, y la Internet global, a través de un ISP sobre ADSL o CATV. Se asigna una única dirección IPv4 al router de acceso, y la traducción de direcciones de red permite que todos los hosts conectados a la red doméstica compartan una única dirección IPv4 pública. 

.. figure:: png/network-fig-158-c.png
   :align: center
   :scale: 70
   
   NAT simple con una única dirección IPv4 pública
..   A simple NAT with one public IPv4 address

.. A second type of deployment is in enterprise networks as shown in the figure below. In this case, the NAT functionality is installed on a border router of the enterprise. A private IPv4 address is assigned to each enterprise host while the border router manages a pool containing several public IPv4 addresses. 

Un segundo tipo de implantación es en redes empresariales, como se muestra en la figura siguiente. En este caso, la funcionalidad NAT está instalada en un router frontera de la empresa. Se asigna una dirección IPv4 privada a cada host de la empresa, mientras que el router de frontera administra un pool conteniendo varias direcciones IPv4 públicas.

.. figure:: png/network-fig-159-c.png
   :align: center
   :scale: 70
  
   NAT corporativo con varias direcciones IPv4 
..   An enterprise NAT with several public IPv4 addresses

.. As the name implies, a NAT is a device that "translates" IP addresses. A NAT maintains a mapping table between the private IP addresses used in the internal network and the public IPv4 addresses. NAT allows a large number of hosts to share a pool of IP addresses, as these hosts do not all access the global Internet at the same time. 

Como su nombre lo indica, un dispositivo NAT "traduce" direcciones IP. Mantiene una tabla de mapeo entre las direcciones privadas usadas en la red interna y las direcciones IPv4 públicas. La Traducción de Direcciones permite que una gran cantidad de hosts comparta un pool de direcciones IP, ya que estos hosts no acceden todos a la Internet global al mismo tiempo.

.. The simplest NAT is a middlebox that uses a one-to-one mapping between a private IP address and a public IP address. To understand its operation, let us assume that a NAT, such as the one shown above, has just booted. When the NAT receives the first packet from source `S` in the internal network which is destined to the public Internet, it creates a mapping between internal address `S` and the first address of its pool of public addresses (`P1`). Then, it translates the received packet so that it can be sent to the public Internet. This translation is performed as followed :

.. - the source address of the packet (`S`) is replaced by the mapped public address (`P1`)
.. - the checksum of the IP header is incrementally updated as its content has changed
.. - if the packet carried a TCP or UDP segment, the transport layer checksum found in the included segment must also be updated as it is computed over the segment and a pseudo-header that includes the source and destination addresses

El dispositivo NAT más simple es un middlebox que usa un mapeo uno a uno entre una dirección IP privada y una pública. Para comprender su operación, supongamos que un dispositivo NAT como el mostrado anteriormente acaba de arrancar. Cuando el NAT recibe el primer paquete procedente del origen `S` en la red interna, y destinado a la Internet pública, crea un mapeo entre la dirección interna `S` y la primera dirección de su pool de direcciones públicas (`P1`). Luego, traduce el paquete recibido de modo que pueda ser enviado a la Internet pública. Esta traducción se realiza como sigue:

 - La dirección origen del paquete (`S`) se reemplaza por la dirección pública mapeada (`P1`).
 - El checksum de la cabecera IP se actualiza incrementalmente según cambia su contenido. 
 - Si el paquete transportaba un segmento TCP o UDP, el checksum de la capa de transporte que se encuentra en el segmento incluido también debe ser actualizado, ya que se computa sobre el segmento y un pseudo-header que iuncluye las direcciones origen y destino.

.. When a packet destined to `P1` is received from the public Internet, the NAT consults its mapping table to find `S`. The received packet is translated and forwarded in the internal network. 
Cuando se recibe un paquete destinado a `P1` desde la Internet pública, el NAT consulta su tabla de mapeo buscando `S`. El paquete recibido se traduce y se reenvía a la red interna. 

.. This works as long as the pool of public IP addresses of the NAT does not become empty. In this case, a mapping must be removed from the mapping table to allow a packet from a new host to be translated. This garbage collection can be implemented by adding to each entry in the mapping table a timestamp that contains the last utilisation time of a mapping entry. This timestamp is updated each time the corresponding entry is used. Then, the garbage collection algorithm can remove the oldest mapping entry in the table.

Esto funciona mientras que no se agote el pool de direcciones públicas del NAT. En este caso, se debe eliminar un mapeo de la tabla para permitir la traducción de un paquete originado por un nuevo host. Esta recolección de basura puede implementarse agregando un dato de temporización (`timestamp`) a cada elemento en la tabla de mapeos, que indique el momento de su última utilización. Este timestamp se actualiza cada vez que se usa el correspondiente elemento. Luego, el algoritmo de recolección de basura puede eliminar el elemento más antiguo de la tabla.

.. A drawback of such a simple enterprise NAT is the size of the pool of public IPv4 addresses which is often too small to allow a large number of hosts share such a NAT. In this case, a better solution is to allow the NAT to translate both IP addresses and port numbers. 

Una desventaja de este NAT simple es que el tamaño del pool de direcciones públicas IPv4 es con frecuencia demasiado pequeño para permitir que un gran número de hosts comparta un dispositivo NAT. En este caso, una mejor solución es permitir que NAT traduzca direcciones IP y números de puerto. 

.. Such a NAT maintains a mapping table that maps an internal IP address and TCP port number with an external IP address and TCP port number. When such a NAT receives a packet from the internal network, it performs a lookup in the mapping table with the packet's source IP address and source TCP port number. If a mapping is found, the source IP address and the source TCP port number of the packet are translated with the values found in the mapping table, the checksums are updated and the packet is sent to the global Internet. If no mapping is found, a new mapping is created with the first available couple `(IP address, TCP port number)` and the packet is translated. The entries of the mapping table are either removed at the end of the corresponding TCP connection as the NAT tracks TCP connection state like a stateful firewall or after some idle time.

Este dispositivo NAT mantiene una tabla de traducción que mapea un par `(dirección IP interna, puerto TCP)` con un par `(dirección IP externa, puerto TCP)`. Cuando dicho NAT recibe un paquete desde la red interna, ejecuta una búsqueda en la tabla de mapeos con la dirección IP origen y puerto TCP origen. Si se halla un mapeo, la dirección IP origen y el puerto TCP origen del paquete se traducen con valores hallados en la tabla de mapeos; se actualizan ambos checksums y el paquete se envía a la Internet global. Si no se halla un mapeo, se crea uno nuevo con el primer par `(dirección IP externa, puerto TCP)` disponible y se traduce el paquete. Las entradas de la tabla se eliminan al finalizar la correspondiente conexión TCP (ya que el dispositivo NAT mantiene el estado de la conexión TCP como un firewall con estado) o después de algún tiempo sin actividad. 
When such a NAT receives a packet from the global Internet, it looks up its mapping table for the packet's destination IP address and destination TCP port number. If a mapping is found, the packet is translated and forwarded into the internal network. Otherwise, the packet is discarded as the NAT cannot determine to which particular internal host the packet should be forwarded. For this reason, 

.. With :math:`2^{16}` different port numbers, a NAT may support a large number of hosts with a single public IPv4 address. However, it should be noted that some applications open a large number of TCP connections [Miyakawa2008]_. Each of these TCP connections consumes one mapping entry in the NAT's mapping table. 

Con :math:`2^{16}` diferentes números de puerto, un dispositivo NAT puede soportar una gran cantidad de hosts con una única dirección IPv4. Sin embargo, debe notarse que algunas aplicaciones abren una gran cantidad de conexiones TCP [Miyakawa2008]_. Cada una de estas conexiones TCP consume un elemento de la tabla de mapeos NAT. 

.. index:: Application Level Gateway, ALG

.. NAT allows many hosts to share one or a few public IPv4 addresses. However, using NAT has two important drawbacks. First, it is difficult for external hosts to open TCP connections with hosts that are behind a NAT. Some consider this to be a benefit from a security perspective. However, a NAT should not be confused with a firewall as there are some techniques to traverse NATs. Second, NAT breaks the end-to-end transparency of the network and transport layers. The main problem is when an application layer protocol uses IP addresses in some of the ADUs that it sends. A popular example is ftp defined in :rfc:`959`. In this case, there is a mismatch between the packet header translated by the NAT and the packet payload. The only solution to solve this problem is to place an Application Level Gateway (ALG) on the NAT that understands the application layer protocol and can thus translate the IP addresses and port numbers found in the ADUs. However, defining an ALG for each application is costly and application developers should avoid using IP addresses in the messages exchanged in the application layer :rfc:`3235`.

NAT permite a muchos hosts compartir una, o unas pocas, direcciones IPv4 públicas. Sin embargo, el uso de NAT tiene dos importantes desventajas. Primero, es difícil para los hosts externos abrir conexiones con hosts detrás de un dispositivo NAT. Algunos consideran que ésta es una ventaja desde el punto de vista de la seguridad. Sin embargo, un NAT no debe ser confundido con un firewall ya que existen algunas técnicas que permiten atravesar los dispositivos NAT. Segundo, NAT rompe la transparencia de las capas de red y de transporte. El principal problema es cuando un protocolo de Capa de Aplicación usa direcciones IP en algunas de las ADUs que envía. Un ejemplo conocido es FTP, definido en :rfc:`959`. En este caso, existe una discordancia entre la cabecera traducida por NAT y la carga útil del paquete. La única solución a este problema es ubicar en el NAT un gateway de nivel de aplicación (`Application Level Gateway`, ALG) que comprenda el protocolo de capa de Aplicación y pueda así traducir las direcciones IP y números de puerto hallados en las ADUs. Sin embargo, definir un ALG por cada aplicación es costoso; y los desarrolladores de aplicaciones deberían evitar utilizar direcciones IP en los mensajes intercambiados en la capa de Aplicación :rfc:`3235`.

.. index:: NAT66
.. note:: IPv6 y NAT

 NAT ha tenido mucho éxito con IPv4. Dado el tamaño del espacio de direccionamiento de IPv6, los diseñadores de IPv6 esperaban que NAT nunca sería útil con IPv6. La transparencia de IPv6 ha sido uno sus valores clave comparado con IPv4. Sin embargo, el anticipado agotamiento de direcciones IPv4 llevó a los administradores de redes a considerar IPv6 más seriamente. Uno de los resultados de este análisis es que IETF definió dispositivos NAT :rfc:`3235` que son específicos de IPv6. Otro uso de NAT con IPv6 es permitir a los hosts IPv6 acceder destinos IPv4, y a la inversa. La especificación temprana de IPv6 incluía el mecanismo de traducción de direcciones de red y protocolos (`Network Address Translation - Protocol Translation`, NAT-PT) definido en :rfc:`2766`. Este mecanismo más tarde quedó desaconsejado (`deprecated`) en :rfc:`4966`, pero ha sido revitalizado recientemente con el nombre de NAT64 :rfc:`6144`. Un dispositivo NAT64 es un middlebox que ejecuta la traducción de paquetes IPv6 <--> IPv4 para permitir a los hosts IPv6 contactar a los servidores IPv4 :rfc:`6144`.

.. NAT has been very successful with IPv4. Given the size of the IPv6 addressing space, the IPv6 designers expected that NAT would never be useful with IPv6. The end-to-end transparency of IPv6 has been one of its key selling points compared to IPv4. However, the expected shortage of IPv4 addresses lead enterprise network administrators to consider IPv6 more seriously. One of the results of this analysis is that the IETF defined NAT devices :rfc:`6296` that are IPv6 specific. Another usage of NAT with IPv6 is to allow IPv6 hosts to access IPv4 destinations and conversely. The early IPv6 specifications included the Network Address Translation - Protocol Translation (NAT-PT) mechanism defined in :rfc:`2766`. This mechanism was later deprecated in :rfc:`4966` but has been recently restarted under the name NAT64 :rfc:`6144`. A NAT64 is a middlebox that performs the IPv6<->IPv4 packet translation to allow IPv6 hosts to contact IPv4 servers :rfc:`6144`. 


