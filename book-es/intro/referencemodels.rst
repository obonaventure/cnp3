.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. index:: Reference models

Los modelos de referencia
#########################

.. Given the growing complexity of computer networks, during the 1970s network researchers proposed various reference models to facilitate the description of network protocols and services. Of these, the Open Systems Interconnection (OSI) model [Zimmermann80]_ was probably the most influential. It served as the basis for the standardisation work performed within the :term:`ISO` to develop global computer network standards. The reference model that we use in this book can be considered as a simplified version of the OSI reference model [#fiso-tcp]_.

Dada la creciente complejidad de las redes de computadoras, durante los años 70 los investigadores de redes propusieron varios modelos de referencia para facilitar la descripción de protocolos y servicios de redes. De éstos, el modelo de Interconexión de Sistemas Abiertos (`Open Systems Interconnection`, OSI) [Zimmermann80]_ fue probablemente el de mayor influencia.  Sirvió como base para el trabajo de estandarización ejecutado dentro de la organización :term:`ISO` para desarollar estándares globales de redes. El modelo de referencia que usamos en este libro puede ser considerado una versión simplificada del modelo de referencia OSI  [#fiso-tcp]_.

.. index:: Five layers reference model

.. The five layers reference model
.. -------------------------------

El modelo de referencia de cinco capas
--------------------------------------

.. Our reference model is divided into five layers, as shown in the figure below.

Nuestro modelo de referencia se divide en cinco capas, como se muestra en la figura siguiente.

.. figure:: svg/intro-figures-026-c.*
   :align: center
   :scale: 80

   Las cinco capas del modelo de referencia
..   The five layers of the reference model

.. index:: electrical cable, optical fiber, multimode optical fiber, monomode optical fiber 

.. Starting from the bottom, the first layer is the Physical layer. Two communicating devices are linked through a physical medium. This physical medium is used to transfer an electrical or optical signal between two directly connected devices. Several types of physical mediums are used in practice : 

Comenzando desde la base, la primera capa es la Capa Física. Dos dispositivos de comunicaciones se vinculan mediante un medio físico. Este medio físico se usa para transferir una señal eléctrica u óptica entre dos dispositivos directamente conectados. En la práctica se usan varios tipos de medios físicos:

..  - `electrical cable`. Information can be transmitted over different types of electrical cables. The most common ones are the twisted pairs that are used in the telephone network, but also in enterprise networks and coaxial cables. Coaxial cables are still used in cable TV networks, but are no longer used in enterprise networks. Some networking technologies operate over the classical electrical cable.
..  - `optical fiber`. Optical fibers are frequently used in public and enterprise networks when the distance between the communication devices is larger than one kilometer. There are two main types of optical fibers : multimode and monomode. Multimode is much cheaper than monomode fiber because a LED can be used to send a signal over a multimode fiber while a monomode fiber must be driven by a laser. Due to the different modes of propagation of light, monomode fibers are limited to distances of a few kilometers while multimode fibers can be used over distances greater than several tens of kilometers. In both cases, repeaters can be used to regenerate the optical signal at one endpoint of a fiber to send it over another fiber. 
..  - `wireless`. In this case, a radio signal is used to encode the information exchanged between the communicating devices. Many types of modulation techniques are used to send information over a wireless channel and there is lot of innovation in this field with new techniques appearing every year. While most wireless networks rely on radio signals, some use a laser that sends light pulses to a remote detector. These optical techniques allow to create point-to-point links while radio-based techniques, depending on the directionality of the antennas, can be used to build networks containing devices spread over a small geographical area.

- `Cable eléctrico`. La información puede ser transmitida sobre diferentes tipos de cables eléctricos. Los más comunes son los pares retorcidos que se usan en las redes telefónicas, pero también en las redes corporativas, y cables coaxiles. Los cables coaxiles siguen usándose en las redes de TV cable, pero ya no en las redes corporativas. Algunas tecnologías de redes operan sobre el cable eléctrico tradicional.
- `Fibra óptica`. Las fibras ópticas se usan frecuentemente en las redes públicas y corporativas cuando la distancia entre los dispositivos que se comunican es mayor que un kilómetro. Hay dos tipos principales de fibras ópticas: multimodo y monomodo. Las fibras multimodo son mucho más baratas que las monomodo porque en aquéllas se puede utilizar un LED para enviar la señal, mientras que en una fibra monomodo se necesita un LASER. Debido a los diferentes modos de propagación de la luz, las fibras monomodo se limitan a distancias de unos pocos kilómetros, mientras que las fibras multimodo pueden usarse sobre distancias mayores que varias decenas de kilómetros. En ambos casos, pueden usarse repetidores para regenerar la señal óptica en un extremo del segmento de fibra, para enviarla sobre el segmento siguiente.
- `Inalámbrico`. En este caso, se usa una señal de radio para codificar la información intercambiada entre los dispositivos que se comunican. Se usan muchos tipos de técnicas de modulación para enviar información sobre un canal inalámbrico, y nuevas técnicas aparecen todos los años en este campo con mucha innovación. Aunque la mayoría de las redes inalámbricas descansan en señales de radio, algunas usan un LASER que envía pulsos de luz a un detector remoto. Estas técnicas ópticas permiten la creación de vínculos punto a punto, mientras que las técnicas basadas en radio, dependiendo de la direccionalidad de las antenas, pueden ser usadas para construir redes conteniendo dispositivos dispersos en un área geográfica limitada.

.. An important point to note about the Physical layer is the service that it provides. This service is usually an unreliable connection-oriented service that allows the users of the Physical layer to exchange bits. The unit of information transfer in the Physical layer is the bit. The Physical layer service is unreliable because :

Un punto importante para notar sobre la Capa Física es el servicio que provee. Este servicio normalmente es un servicio orientado a conexión y no confiable, que permite a los usuarios de la Capa Física intercambiar bits. La unidad de transferencia de información en la Capa Física es el bit. Su servicio es no confiable porque:

 - la Capa Física puede cambiar el valor de un bit que se transmite; por ejemplo, debido a interferencias electromagnéticas
 - puede entregar `más` bits al receptor de los que fueron enviados por el emisor
 - puede entregar `menos` bits al receptor de los que fueron enviados por el emisor

..  - the Physical layer may change, e.g. due to electromagnetic interferences, the value of a bit being transmitted
..  - the Physical layer may deliver `more` bits to the receiver than the bits sent by the sender
..  - the Physical layer may deliver `fewer` bits to the receiver than the bits sent by the sender

.. The last two points may seem strange at first glance. When two devices are attached through a cable, how is it possible for bits to be created or lost on such a cable ? 

Los últimos dos puntos pueden parecer extraños a primera vista. Cuando dos dispositivos se conectan mediante un cable, ¿cómo es posible que los bits puedan perderse o crearse en dicho cable?

.. This is mainly due to the fact that the communicating devices use their own clock to transmit bits at a given bit rate. Consider a sender having a clock that ticks one million times per second and sends one bit every tick. Every microsecond, the sender sends an electrical or optical signal that encodes one bit. The sender's bit rate is thus 1 Mbps. If the receiver clock ticks exactly [#fsynchro]_ every microsecond, it will also deliver 1 Mbps to its user. However, if the receiver's clock is slightly faster (resp. slower), than it will deliver slightly more (resp. less) than one million bits every second. This explains why the physical layer may lose or create bits.

Esto se debe principalmente al hecho de que los dispositivos que se comunican usan su propio reloj para transmitir bits a una velocidad dada. Consideremos un emisor que tiene un reloj que pulsa a un millón de veces por segundo y envía un bit a cada pulso. Cada microsegundo, el emisor envía una señal eléctrica u óptica que codifica un bit. La velocidad (`bit rate`) del emisor es entonces de 1 Mbps. Si el reloj del receptor pulsa exactamente [#fsynchro]_ cada microsegundo, también entregará 1 Mbps a su usuario. Sin embargo, si el reloj del receptor es ligeramente más rápido (resp. más lento), entonces entregará ligeramente más (resp. menos) de un millón de bits por segundo. Esto explica por qué la Capa Física puede perder o crear bits.

.. .. note:: Bit rate

.. In computer networks, the bit rate of the physical layer is always expressed in bits per second. One Mbps is one million bits per second and one Gbps is one billion bits per second. This is in contrast with memory specifications that are usually expressed in bytes (8 bits), KiloBytes ( 1024 bytes) or MegaBytes (1048576 bytes). Thus transferring one MByte through a 1 Mbps link lasts 8.39 seconds.

.. note:: Bit rate

 En las redes de computadoras, el `bit rate` de la Capa Física siempre se expresa en bits por segundo (`bps`). Un Mbps es un millón de bits por segundo y un Gbps es mil millones de bits por segundo. Esto se diferencia de las especificaciones de memoria, que normalmente se expresan en bytes (8 bits), Kilobytes (1024 bytes), o Megabytes (1048576 byts). Así, transferir un MB (Megabyte) a través de un vínculo de 1 Mbps tarda 8.39 segundos.

  ========        ================
  Bit rate        Bits por segundo
  ========        ================
  1 Kbps	  :math:`10^3`
  1 Mbps	  :math:`10^6`
  1 Gbps	  :math:`10^9`
  1 Tbps	  :math:`10^{12}`
  ========        ===============
  

.. index:: Physical layer, Capa Física


.. figure:: svg/intro-figures-027-c.*
   :align: center
   :scale: 80

   La Capa Física
..   The Physical layer

.. The physical layer allows thus two or more entities that are directly attached to the same transmission medium to exchange bits. Being able to exchange bits is important as virtually any information can be encoded as a sequence of bits. Electrical engineers are used to processing streams of bits, but computer scientists usually prefer to deal with higher level concepts. A similar issue arises with file storage. Storage devices such as hard-disks also store streams of bits. There are hardware devices that process the bit stream produced by a hard-disk, but computer scientists have designed filesystems to allow applications to easily access such storage devices. These filesystems are typically divided into several layers as well. Hard-disks store sectors of 512 bytes or more. Unix filesystems group sectors in larger blocks that can contain data or `inodes` representing the structure of the filesystem. Finally, applications manipulate files and directories that are translated in blocks, sectors and eventually bits by the operating system.

La Capa Física permite que dos o más entidades directamente conectadas al mismo medio de transmisión intercambien bits. Poder intercambiar bits es fundamental, ya que virtualmente cualquier información puede ser codificada como una secuencia de bits. Los ingenieros eléctricos suelen procesar flujos de bits, pero los científicos de la computación normalmente prefieren tratar con conceptos de más alto nivel. Se presenta un caso similar con el almacenamiento de archivos. Los dispositivos de almacenamiento, como discos rígidos, también almacenan flujos de bits. Hay dispositivos de hardware que procesan el flujo de bits producido por un disco rígido, pero los científicos de la computación han diseñado sistemas de archivos para permitir a las aplicaciones acceder fácilmente esos dispositivos de almacenamiento. Estos sistemas de archivos, típicamente, están además divididos en varias capas. Los discos rígidos almacenan sectores de 512 bits, o más. Los sistemas de archivos Unix agrupan los sectores en bloques más grandes, que contienen datos, o `inodos` representando la estructura del sistema de archivos. Finalmente, las aplicaciones manipulan los archivos y directorios que son traducidos, por el sistema operativo, a bloques, sectores y eventualmente bits.

.. index:: Datalink layer, frame, trama

.. Computer networks use a similar approach. Each layer provides a service that is built above the underlying layer and is closer to the needs of the applications. 

Las redes de computadoras usan una estrategia similar. Cada capa provee un servicio que se construye encima de la capa inferior, y está más cerca de las necesidades de la aplicación.

.. The `Datalink layer` builds on the service provided by the underlying physical layer. The `Datalink layer` allows two hosts that are directly connected through the physical layer to exchange information. The unit of information exchanged between two entities in the `Datalink layer` is a frame. A frame is a finite sequence of bits. Some `Datalink layers` use variable-length frames while others only use fixed-length frames. Some `Datalink layers` provide a connection-oriented service while others provide a connectionless service. Some `Datalink layers` provide reliable delivery while others do not guarantee the correct delivery of the information.

La `Capa de Enlace de Datos` aumenta los servicios ofrecidos por la Capa Física subyacente. Permite que dos nodos directamente conectados a través del medio físico intercambien información. La unidad de información intercambiada entre dos entidades de la capa de Enlace de Datos es una `trama` (o `frame`). Una trama es una secuencia finita de bits. Algunas capas de Enlace de Datos usan tramas de longitud variable, mientras que otras usan tramas de longitud fija. Algunas ofrecen un servicio orientado a conexión, mientras que otras proveen un servicio sin conexión. Algunas ofrecen entrega confiable, y otras no garantizan la entrega correcta de la información.

.. An important point to note about the `Datalink layer` is that although the figure below indicates that two entities of the `Datalink layer` exchange frames directly, in reality this is slightly different. When the `Datalink layer` entity on the left needs to transmit a frame, it issues as many `Data.request` primitives to the underlying `physical layer` as there are bits in the frame. The physical layer will then convert the sequence of bits in an electromagnetic or optical signal that will be sent over the physical medium. The `physical layer` on the right hand side of the figure will decode the received signal, recover the bits and issue the corresponding `Data.indication` primitives to its `Datalink layer` entity. If there are no transmission errors, this entity will receive the frame sent earlier. 

Un punto importante para notar sobre la Capa de Enlace de Datos es que, aunque la figura siguiente indica que dos entidades de Enlace intercambian tramas directamente, en la realidad esto es ligeramente diferente. Cuando la entidad de la Capa de Enlace de Datos a la izquierda necesite transmitir una trama, enviará tantas primitivas `Data.request` a la Capa Física subyacente como bits haya en la trama. La capa física entonces convertirá la secuencia de bits en una señal electromagnética u óptica que será enviada por el medio físico. La `Capa Física` sobre el lado derecho de la figura decodificará la señal recibida, recuperando los bits, y emitirá las correspondientes primitivas `Data.indication` a su entidad de Capa de Enlace de Datos. Si no hay errores de transmisión, esta entidad recibirá la trama enviada anteriormente.

.. figure:: svg/intro-figures-028-c.*
   :align: center
   :scale: 80 

   La Capa de Enlace de Datos
..   The Datalink layer


.. index:: Network layer, packet, Capa de Red, paquete

.. The `Datalink layer` allows directly connected hosts to exchange information, but it is often necessary to exchange information between hosts that are not attached to the same physical medium. This is the task of the `network layer`. The `network layer` is built above the `datalink layer`. Network layer entities exchange `packets`. A `packet` is a finite sequence of bytes that is transported by the datalink layer inside one or more frames. A packet usually contains information about its origin and its destination, and usually passes through several intermediate devices called routers on its way from its origin to its destination.

La `Capa de Enlace de Datos` permite que nodos directamente conectados intercambien información; pero frecuentemente es necesario intercambiar información entre nodos que no están conectados al mismo medio físico. Ésta es la tarea de la `Capa de Red`. La Capa de Red se construye encima de la Capa de Enlace de Datos. Las entidades de Capa de Red intercambian `paquetes`. Un paquete es una secuencia finita de bytes que son transportados por la Capa de Enlace de Datos dentro de una o más tramas. Un paquete generalmente contiene información sobre cuáles son su origen y su destino, y generalmente atraviesa varios dispositivos intermedios llamados `routers` en su camino del origen al destino.

.. figure:: svg/intro-figures-029-c.*
   :align: center
   :scale: 80 

   La Capa de Red
..   The network layer

.. index:: Transport layer, segment, Capa de Transporte, Segmento

.. Most realisations of the network layer, including the internet, do not provide a reliable service. However, many applications need to exchange information reliably and so using the network layer service directly would be very difficult for them. Ensuring the reliable delivery of the data produced by applications is the task of the `transport layer`. `Transport layer` entities exchange `segments`. A segment is a finite sequence of bytes that are transported inside one or more packets. A transport layer entity issues segments (or sometimes part of segments) as `Data.request` to the underlying network layer entity. 

La mayoría de las implementaciones de la Capa de Red, incluida la Internet, no ofrecen un servicio confiable. Sin embargo, muchas aplicaciones necesitan intercambiar información de manera confiable, y lograrlo usando el servicio de la Capa de Red directamente sería difícil. Asegurar la entrega confiable de los datos producidos por las aplicaciones es la tarea de la `Capa de Transporte`. Las entidades de la Capa de Transporte intercambian `segmentos`. Un segmento es una secuencia finita de bytes que son transportados dentro de uno o más paquetes. Una entidad de la Capa de Transporte emite segmentos (o, a veces, parte de segmentos) como operaciones `Data.request` a la entidad de la Capa de Red subyacente.

.. There are different types of transport layers. The most widely used transport layers on the Internet are :term:`TCP` ,that provides a reliable connection-oriented bytestream transport service, and :term:`UDP` ,that provides an unreliable connection-less transport service.

Existen diferentes tipos de capas de transporte. Las más usadas en Internet son :term:`TCP`, que provee un servicio de transporte de bytes confiable y orientado a conexión, y :term:`UDP`, que provee un servicio de transporte no confiable y sin conexión.

.. figure:: svg/intro-figures-030-c.*
   :align: center
   :scale: 80 

   La Capa de Transporte
..   The transport layer

.. index:: Application layer, Capa de Aplicación

.. The upper layer of our architecture is the `Application layer`. This layer includes all the mechanisms and data structures that are necessary for the applications. We will use Application Data Unit (ADU) to indicate the data exchanged between two entities of the Application layer.

La capa superior de nuestra arquitectura es la `Capa de Aplicación`. Esta capa incluye todos los mecanismos y estructuras de datos necesarias para las aplicaciones. Usaremos la sigla ADU (`Application Data Unit`, unidad de datos de aplicación) para indicar los datos intercambiados entre dos entidades de la Capa de Aplicación.


.. figure:: svg/intro-figures-031-c.*
   :align: center
   :scale: 50 

   La Capa de Aplicación
..   The Application layer

.. index:: TCP/IP reference model, Modelo de referencia TCP/IP


.. The TCP/IP reference model
.. --------------------------

El modelo de referencia TCP/IP
------------------------------

.. In contrast with OSI, the TCP/IP community did not spend a lot of effort defining a detailed reference model; in fact, the goals of the Internet architecture were only documented after TCP/IP had been deployed [Clark88]_. :rfc:`1122` , which defines the requirements for Internet hosts, mentions four different layers. Starting from the top, these are :

.. - an Application layer
.. - a Transport layer
.. - an Internet layer which is equivalent to the network layer of our reference model
.. - a Link layer which combines the functionalities of the physical and datalink layers of our five-layer reference model

Al contrario que lo ocurrido con OSI, la comunidad de TCP/IP no invirtió mucho esfuerzo en definir un modelo de referencia detallado: de hecho, las metas de la arquitectura de Internet sólo fueron documentadas luego de que TCP/IP hubo sido desplegado [Clark88]_. :rfc:`1122` , que define los requerimientos para los hosts de Internet, menciona cuatro capas diferentes. Comenzando desde arriba, éstas son:

 - una capa de Aplicación
 - una capa de Transporte
 - una capa de Internet, que es equivalente a la Capa de Red de nuestro modelo de referencia
 - una capa de Enlace, que combina las funcionalidades de las capas Física y de Enlace de Datos de nuestro modelo de referencia de cinco capas.

.. Besides this difference in the lower layers, the TCP/IP reference model is very close to the five layers that we use throughout this document.

Aparte de esta diferencia en las capas inferiores, el modelo de referencia TCP/IP se aproxima mucho a las cinco capas que usamos en este documento.

.. index:: OSI reference model, modelo de referencia OSI

.. The OSI reference model
El modelo de referencia OSI
---------------------------

.. Compared to the five layers reference model explained above, the :term:`OSI` reference model defined in [X200]_ is divided in seven layers. The four lower layers are similar to the four lower layers described above. The OSI reference model refined the application layer by dividing it in three layers :

..  - the Session layer. The Session layer contains the protocols and mechanisms that are necessary to organize and to synchronize the dialogue and to manage the data exchange of presentation layer entities. While one of the main functions of the transport layer is to cope with the unreliability of the network layer, the session's layer objective is to hide the possible failures of transport-level connections to the upper layer higher. For this, the Session Layer provides services that allow to establish a session-connection, to support orderly data exchange (including mechanisms that allow to recover from the abrupt release of an underlying transport connection), and to release the connection in an orderly manner. 
..  - the Presentation layer was designed to cope with the different ways of representing information on computers. There are many differences in the way computer store information. Some computers store integers as 32 bits field, others use 64 bits field and the same problem arises with floating point number. For textual information, this is even more complex with the many different character codes that have been used [#funicode]_. The situation is even more complex when considering the exchange of structured information such as database records. To solve this problem, the Presentation layer contains provides for a common representation of the data transferred. The :term:`ASN.1` notation was designed for the Presentation layer and is still used today by some protocols.
..  - the Application layer that contains the mechanisms that do not fit in neither the Presentation nor the Session layer. The OSI Application layer was itself further divided in several generic service elements. 

Comparado con el modelo de referencia de cinco capas explicado anteriormente, el modelo de referencia :term:`OSI` definido en [X200]_ se divide en siete capas. Las cuatro capas inferiores son similares a las cuatro recién descritas. El modelo de referencia OSI refinó la capa de aplicación dividiéndola en tres capas:

- La `Capa de Sesión`. La capa de Sesión contiene los protocolos y mecanismos que se necesitan para organizar y sincronizar el diálogo, y manejar el intercambio de datos, de las entidades de capa de Presentación. Mientras que una de las principales funciones de la capa de Transporte es arreglar la no confiabilidad de la capa de Red, el objetivo de la capa de Sesión es ocultar los posibles fallos de las conexiones de nivel de transporte a la capa superior. Para esto, la capa de Sesión ofrece servicios que permiten establecer una conexión de sesión, para soportar el intercambio ordenado de datos (incluyendo mecanismos que permitan recuperarse del corte abrupto de una conexión de transporte subyacente), y liberar la conexión en forma ordenada.
- La `Capa de Presentación` fue diseñada para tratar con las diferentes formas de representar información en las computadoras. Hay muchas diferencias en la forma en que las computadoras almacenan la información. Algunas almacenan enteros en campos de 32 bits, otras en 64 bits; y el mismo problema surge con los números en punto flotante. Para la información de texto, la situación es aún más compleja con los diferentes códigos de caracteres que han sido usados [#funicode]_. Todavía más, si consideramos el intercambio de información estructurada como registros de bases de datos. Para resolver este problema, la Capa de Presentación contiene mecanismos para una representación común de los datos transferidos. La notación :term:`ASN.1` se diseñó para la capa de Presentación y aún es usada por algunos protocolos. 
- La Capa de Presentación propiamente dicha, finalmente, contiene los mecanismos que no encajan ni en la capa de Presentación ni en la de Sesión. La capa de Aplicación OSI misma fue dividida en varios elementos de servicio génericos.

.. .. note:: Where are the missing layers in TCP/IP reference model ?

.. The TCP/IP reference places the Presentation and the Session layers implicitly in the Application layer. The main motivations for simplifying the upper layers in the TCP/IP reference model were pragmatic. Most Internet applications started as prototypes that evolved and were later standardised. Many of these applications assumed that they would be used to exchange information written in American English and for which the 7 bits US-ASCII character code was sufficient. This was the case for email, but as we'll see in the next chapter, email was able to evolve to support different character encodings. Some applications considered the different data representations explicitly. For example, :term:`ftp` contained mechanisms to convert a file from one format to another and the HTML language was defined to represent web pages. On the other hand, many ISO specifications were developed by committees composed of people who did not all participate in actual implementations. ISO spent a lot of effort analysing the requirements and defining a solution that meets all of these requirements. Unfortunately, some of the specifications were so complex that it was difficult to implement them completely and the standardisation bodies defined recommended profiles that contained the implemented sets of options... 

.. note:: ¿Dónde están las capas faltantes en el modelo de referencia TCP/IP?

 El modelo de referencia TCP/IP ubica las capas de Presentación y de Sesión implícitamente en la capa de Aplicación. Las principales motivaciones para simplificar las capas superiores en el modelo TCP/IP fueron de orden pragmático. La mayoría de las aplicaciones de Internet comenzaron como prototipos que evolucionaron y más tarde se estandarizaron. Muchas de estas aplicaciones asumían que serían usadas para intercambiar información escrita en inglés norteamericano, para lo cual el código de caracteres US-ASCII de 7 bits era suficiente. Éste era el caso para el correo electrónico, pero como veremos en el siguiente capítulo, el correo electrónico fue capaz de evolucionar para soportar diferentes codificaciones de caracteres. Algunas aplicaciones consideraron explícitamente las diferentes representaciones de datos. Por ejemplo, :term:`ftp` contenía mecanismos para convertir un archivo de un formato a otro, y el lenguaje HTML fue definido para representar páginas web. Por otro lado, muchas especificaciones ISO fueron desarrolladas por comisiones compuestas por gente que no participó en su totalidad en las implementaciones reales. ISO invirtió mucho esfuerzo en el análisis de requerimientos y en la definición de una solución que los abordara a todos. Por desgracia, algunas de las especificaciones eran tan complejas que fue difícil implementarlas completamente, y los cuerpos de estandarización definieron perfiles recomendados, que contenían los conjuntos de opciones implementadas.

.. The work within ISO and ITU on protocols and services was 

.. figure:: png/intro-figures-032-c.png
   :align: center
   :scale: 80 

   Las siete capas del modelo de referencia OSI
..    The seven layers of the OSI reference model

.. rubric:: Footnotes


.. .. [#funicode] There is now a rough consensus for the greater use of the Unicode_ character format. Unicode can represent more than 100,000 different characters from the known written languages on Earth. Maybe one day, all computers will only use Unicode to represent all their stored characters and Unicode could become the standard format to exchange characters, but we are not yet at this stage today. 

.. [#funicode] Hoy existe un cierto consenso para el mayor uso del formato de caracteres Unicode_. Unicode puede representar más de 100.000 diferentes caraceres de las lenguas escritas conocidas de la Tierra. Quizás un día, todas las computadoras usarán Unicode para representar todos los caracteres almacenados, y Unicode podría convertirse en el formato estándar para intercambiar caracteres, pero aún no se ha llegado a esta etapa.

.. .. [#fiso-tcp] An interesting historical discussion of the OSI-TCP/IP debate may be found in [Russel06]_

.. [#fiso-tcp] Se puede encontrar una interesante discusión histórica del debate OSI-TCP/IP en [Russel06]_.

.. .. [#fsynchro] Having perfectly synchronised clocks running at a high frequency is very difficult in practice. However, some physical layers introduce a feedback loop that allows the receiver's clock to synchronise itself automatically to the sender's clock. However, not all physical layers include this kind of synchronisation. 

.. [#fsynchro] Mantener relojes corriendo a alta frecuencia perfectamente sincronizados es muy difícil en la práctica. Sin embargo, algunas capas físicas introducen un lazo de feedback que permite que el reloj del receptor se sincronice automáticamente con el reloj del emisor. No todas las capas físicas incluyen esta clase de sincronización. 

.. include:: ../links.rst

