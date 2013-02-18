.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. index:: UDP
.. _UDP:

.. The User Datagram Protocol
El Protocolo UDP (User Datagram Protocol)
#########################################

.. The User Datagram Protocol (UDP) is defined in :rfc:`768`. It provides an unreliable connectionless transport service on top of the unreliable network layer connectionless service. The main characteristics of the UDP service are :

.. - the UDP service cannot deliver SDUs that are larger than 65507 bytes [#fmtuudp]_ 
.. - the UDP service does not guarantee the delivery of SDUs (losses and desquencing can occur)
.. - the UDP service will not deliver a corrupted SDU to the destination

El protocolo UDP está definido en :rfc:`768`. Ofrece un servicio de transporte sin conexión, no confiable, encima del servicio sin conexión y no confiable de la capa de Red. Las principales características del servicio UDP son: 

 - El servicio UDP no puede entregar SDUs de tamaño mayor que 65507 bytes [#fmtuudp]_ 
 - No garantiza la entrega de SDUs (pueden ocurrir pérdidas y llegadas fuera de secuencia)
 - El servicio UDP no entregará una SDU corrupta a su destinatario.


.. Compared to the connectionless network layer service, the main advantage of the UDP service is that it allows several applications running on a host to exchange SDUs with several other applications running on remote hosts. Let us consider two hosts, e.g. a client and a server. The network layer service allows the client to send information to the server, but if an application running on the client wants to contact a particular application running on the server, then an additional addressing mechanism is required other than the IP address that identifies a host, in order to differentiate the application running on a host. This additional addressing is provided by `port numbers`. When a server using UDP is enabled on a host, this server registers a `port number`. This `port number` will be used by the clients to contact the server process via UDP. 

Comparado con el servicio de capa de Red sin conexión, la principal ventaja del servicio UDP es que permite a varias aplicaciones corriendo en un mismo host intercambiar SDUS con varias otras aplicaciones corriendo en hosts remotos. Consideremos dos hosts, por ejemplo, un cliente y un servidor. El servicio de la capa de Red permite al cliente enviar información al servidor, pero si una aplicación que corre en el cliente desea contactar a una aplicación en particular que esté corriendo en el servidor, entonces se necesitará un mecanismo adicional de direccionamiento, que sea diferente de la dirección IP que identifica a un host, para poder diferenciar entre las diferentes aplicaciones que corren en el mismo host servidor. Este direccionamiento adicional es provisto por `números de puerto`. Cuando un servidor que usa UDP es habilitado en un host, este servidor registra un `número de puerto`. Este número de puerto será usado por los clientes para contactar al proceso servidor a través de UDP.


.. The figure below shows a typical usage of the UDP port numbers. The client process uses port number `1234` while the server process uses port number `5678`. When the client sends a request, it is identified as originating from port number `1234` on the client host and destined to port number `5678` on the server host. When the server process replies to this request, the server's UDP implementation will send the reply as originating from port  `5678` on the server host and destined to port `1234` on the client host.

La figura siguiente muestra un uso típico de los números de puerto UDP. El proceso cliente utiliza el número de puerto `1234` mientras que el proceso servidor utiliza el número de puerto `5678`. Cuando el cliente envía un requerimiento, establece que su origen es el número de puerto `1234` en el host cliente y que su destino es `5678` en el host servidor. Cuando el proceso servidor responde a este requerimiento, la implementación UDP del servidor enviará la respuesta como originada en el puerto `5678` del servidor, y destinada al puerto `1234` en el host cliente.

.. figure:: svg/udp-ports.png
   :align: center
   :scale: 70 

   Uso de los números de puerto UDP

..   Usage of the UDP port numbers

.. index:: UDP segment



.. UDP uses a single segment format shown in the figure below. 

UDP utiliza un único formato de segmento que se muestra en la figura siguiente.


.. figure:: pkt/udp.png
   :align: center
   :scale: 100

   Formato de cabecera UDP
   
..   UDP Header Format

.. The UDP header contains four fields :

.. - a 16 bits source port
.. - a 16 bits destination port
.. - a 16 bits length field 
.. - a 16 bits checksum


La cabecera UDP contiene cuatro campos:

 - Un número de puerto origen, de 16 bits
 - Un número de puerto destino, de 16 bits
 - Un campo de longitud, de 16 bits
 - Un campo de suma de control (`checksum`), de 16 bits

.. As the port numbers are encoded as a 16 bits field, there can be up to only 65535 different server processes that are bound to a different UDP port at the same time on a given server. In practice, this limit is never reached. However, it is worth noticing that most implementations divide the range of allowed UDP port numbers into three different ranges :

.. - the privileged port numbers (1 < port < 1024 )
.. - the ephemeral port numbers ( officially [#fephemeral]_ 49152 <= port <= 65535 )
.. - the registered port numbers (officially 1024 <= port < 49152)

Dado que los números de puerto se codifican como campos de 16 bits, no pueden existir más de 65535 diferentes procesos que estén ligados a diferentes puertos UDP al mismo tiempo en un mismo servidor. En la práctica, este límite nunca se alcanza. Sin embargo, debe observarse que la mayoría de las implementaciones dividen el rango de números de puerto UDP permitidos en tres diferentes rangos:

 - Los números de puerto privilegiados (1 < puerto < 1024)
 - Los números de puerto efímeros (oficialmente [#fephemeral]_ 49152 <= puerto <= 65535)
 - Los números de puerto registrados (oficialmente 1024 <= puerto < 49152)

..  In most Unix variants, only processes having system administrator privileges can be bound to port numbers smaller than `1024`. Well-known servers such as :term:`DNS`, :term:`NTP` or :term:`RPC` use privileged port numbers. When a client needs to use UDP, it usually does not require a specific port number. In this case, the UDP implementation will allocate the first available port number in the ephemeral range. The range of registered port numbers should be used by servers. In theory, developers of network servers should register their port number officially through IANA, but few developers do this. 

En la mayoría de las variantes de Unix, sólo los procesos que tienen privilegios de administrador pueden ligarse a números de puerto menores que 1024. Los servidores `bien conocidos` (`well-known`), como :term:`DNS`, :term:`NTP` o :term:`RPC`, usan números de puerto privilegiados. Cuando un cliente necesita usar UDP, normalmente no requiere un número de puerto específico. En este caso, la implementación UDP asignará el primer número de puerto disponible en el rango efímero. El rango de números de puerto registrados deberá ser usado por los servidores. En teoría, los desarrolladores de servidores de red deben registrar sus números de puerto oficialmente con IANA [#fportnum]_, pero pocos desarrolladores hacen esto.


.. mention inetd and super servers somewhere ?

.. index:: UDP Checksum, Checksum computation

.. .. note:: Computation of the UDP checksum
.. The checksum of the UDP segment is computed over :
  
..  - a pseudo header containing the source IP address, the destination IP address and a 32 bits bit field containing the most significant byte set to 0, the second set to 17 and the length of the UDP segment in the lower two bytes
..  - the entire UDP segment, including its header

 .. This pseudo-header allows the receiver to detect errors affecting the IP source or destination addresses placed in the IP layer below. This is a violation of the layering principle that dates from the time when UDP and IP were elements of a single protocol. It should be noted that if the checksum algorithm computes value '0x0000', then value '0xffff' is transmitted. A UDP segment whose checksum is set to '0x0000' is a segment for which the transmitter did not compute a checksum upon transmission. Some :term:`NFS` servers chose to disable UDP checksums for performance reasons, but this caused `problems <http://lynnesblog.telemuse.net/192>`_ that were difficult to diagnose. In practice, there are rarely good reasons to disable UDP checksums. A detailed discussion of the implementation of the Internet checksum may be found in :rfc:`1071`

.. note:: Cómputo de la suma de control UDP

  La suma de control del segmento UDP se computa sobre:
 
  - Una pseudo-cabecera conteniendo la dirección IP origen, la dirección IP destino y un campo de 32 bits cuyo byte más significativo está puesto a 0, el segundo fijado en 17, y la longitud del segmento UDP en los dos bytes inferiores
  - El segmento UDP completo, incluyendo la cabecera

Esta pseudo-cabecera permite la detección de errores que afecten a la dirección IP origen o destino almacenada en la capa IP más abajo. Esto es una violación del principio de organización en capas, que proviene de las épocas en que UDP e IP eran elementos de un mismo protocolo. Debe notarse que si el algoritmo de suma de control computa el valor '0x0000', entonces el valor que se transmite es '0xffff'. Un segmento UDP cuya suma de control vale a '0x0000' es un segmento para el cual el transmisor no computó la suma de control al momento de transmitir. Algunos servidores :term:`NFS` deciden deshabilitar las sumas de control UDP por motivos de velocidad, pero esto causaba `problemas <http://lynnesblog.telemuse.net/192>`_ que eran difíciles de diagnosticar. En la práctica, rara vez hay buenos motivos para deshabilitar las sumas de control UDP. Puede encontrarse una discusión de la implementación de la suma de control de Internet en :rfc:`1071`


.. Several types of applications rely on UDP. As a rule of thumb, UDP is used for applications where delay must be minimised or losses can be recovered by the application itself. A first class of the UDP-based applications are applications where the client sends a short request and expects a quick and short answer. The :term:`DNS` is an example of a UDP application that is often used in the wide area. However, in local area networks, many distributed systems rely on Remote Procedure Call (:term:`RPC`) that is often used on top of UDP. In Unix environments, the Network File System (:term:`NFS`) is built on top of RPC and runs frequently on top of UDP. A second class of UDP-based applications are the interactive computer games that need to frequently exchange small messages, such as the player's location or their recent actions. Many of these games use UDP to minimise the delay and can recover from losses. A third class of applications are multimedia applications such as interactive Voice over IP or interactive Video over IP. These interactive applications expect a delay shorter than about 200 milliseconds between the sender and the receiver and can recover from losses directly inside the application. 

Hay varios tipos de aplicaciones que descansan en UDP. Como regla habitual, UDP se usa para aplicaciones donde el retardo debe ser minimizado, o donde las pérdidas deben ser recuperadas por la misma aplicación. Una primera clase de aplicaciones basadas en UDP es la de aquellas donde el cliente envía requerimientos cortos y espera respuestas cortas y rápidas. El :term:`DNS` es un ejemplo de aplicación UDP que se usa frecuentemente en las redes de área amplia. Sin embargo, en las redes de área local, muchos sistemas distribuidos se apoyan en llamadas a procedimientos remotos (`Remote Procedure Call`, :term:`RPC`), que se usan frecuentemente encima de UDP. En ambientes Unix, el sistema de archivos de red :term:`NFS` (`Network File System`) se construye sobre RPC, y suele correr encima de UDP. Una segunda clase de aplicaciones UDP son los juegos interactivos de computadora que necesitan intercambiar mensajes pequeños y frecuentes, tales como la ubicación del jugador, o sus acciones recientes. Muchos de estos juegos usan UDP para minimizar el retardo y pueden recuperarse de pérdidas. Una tercera clase de aplicaciones son las de multimedia como las de voz interactiva sobre IP (`VoIP`) o video interactivo sobre IP. Estas aplicaciones interactivas esperan encontrar un retardo menor que 200 milisegundos entre el emisor y el receptor, y pueden recuperarse de las pérdidas directamente dentro de la aplicación.

.. rubric:: Footnotes


.. .. [#fmtuudp] This limitation is due to the fact that the network layer (IPv4 and IPv6) cannot transport packets that are larger than 64 KBytes. As UDP does not include any segmentation/reassembly mechanism, it cannot split a SDU before sending it.

.. .. [#fportnum] The complete list of allocated port numbers is maintained by IANA_ . It may be downloaded from http://www.iana.org/assignments/port-numbers

.. .. [#fephemeral] A discussion of the ephemeral port ranges used by different TCP/UDP implementations may be found in http://www.ncftp.com/ncftpd/doc/misc/ephemeral_ports.html

.. [#fmtuudp] Esta limitación se debe al hecho de que la capa de Red (IPv4 e IPv6) no puede transportar paquetes que sean mayores que 64 KBytes. Como UDP no incluye mecanismos de segmentación ni reensamblado, no puede dividir una SDU antes de enviarla.

.. [#fportnum] La lista completa de los números de puerto asignados es mantenida por IANA_. Puede descargarse de http://www.iana.org/assignments/port-numbers.

.. [#fephemeral] Puede hallarse una discusión de los rangos de puertos efímeros usados por diferentes implemntaciones TCP/UDP en http://www.ncftp.com/ncftpd/doc/misc/ephemeral_ports.html.

.. include:: /links.rst
