.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. Services and protocols

Servicios y protocolos
######################

.. An important aspect to understand before studying computer networks is the difference between a *service* and a *protocol*. 

Un aspecto importante de entender antes de estudiar redes de computadoras es la diferencia entre un *servicio* y un *protocolo*.

.. In order to understand the difference between the two, it is useful to start with real world examples. The traditional Post provides a service where a postman delivers letters to recipients. The Post defines precisely which types of letters (size, weight, etc) can be delivered by using the Standard Mail service. Furthermore, the format of the envelope is specified (position of the sender and recipient addresses, position of the stamp). Someone who wants to send a letter must either place the letter at a Post Office or inside one of the dedicated mailboxes. The letter will then be collected and delivered to its final recipient. Note that for the regular service the Post usually does not guarantee the delivery of each particular letter, some letters may be lost, and some letters are delivered to the wrong mailbox. If a letter is important, then the sender can use the registered service to ensure that the letter will be delivered to its recipient. Some Post services also provide an acknowledged service or an express mail service that is faster than the regular service.

Para comprender la diferencia entre los dos, es útil comenzar con ejemplos del mundo real. El `Correo` tradicional provee un servicio donde un cartero entrega cartas a los destinatarios. El Correo define con precisión qué tipos de cartas pueden ser entregadas (por su tamaño, peso, etc.) usando el servicio de Correo Simple. Además se especifica el formato del sobre (posición de la dirección de remitente y destinatario, posición de la estampilla). Alguien que quiera enviar una carta debe, o bien despachar la carta en la Oficina de Correos, o colocarla dentro de un buzón del Correo. La carta será recogida y entregada a su destinatario final. Nótese que para el servicio regular, el Correo por lo general no garantiza el envío de cada carta. Algunas cartas pueden perderse, y algunas pueden ser entregadas en un buzón equivocado. Si una carta es importante, entonces el remitente puede usar el servicio certificado para asegurarse de que será entregada al destinatario. Algunos servicios de Correo también proveen un servicio de aviso de retorno, o un servicio expreso que es más rápido que el servicio regular.

.. In computer networks, the notion of service is more formally defined in [X200]_ . It can be better understood by considering a computer network, whatever its size or complexity, as a black box that provides a service to `users` , as shown in the figure below. These users could be human users or processes running on a computer system. 

En las redes de computadoras, la noción de servicio está definida más formalmente en [X200]_. Puede comprenderse mejor considerando una red de computadoras, de cualquier tamaño o complejidad, como una caja negra que provee un servicio a `usuarios`, como se muestra en la figura siguiente. Estos usuarios podrían ser usuarios humanos o procesos corriendo en un sistema de computación.

.. _fig-users:

.. figure:: svg/intro-figures-014-c.*
   :align: center
   :scale: 80 

   Usuarios y proveedor de servicio
..   Users and service provider

.. index:: address, dirección

.. Many users can be attached to the same service provider. Through this provider, each user must be able to exchange messages with any other user. To be able to deliver these messages, the service provider must be able to unambiguously identify each user. In computer networks, each user is identified by a unique `address`, we will discuss later how these addresses are built and used. At this point, and when considering unicast transmission, the main characteristic of these `addresses` is that they are unique. Two different users attached to the network cannot use the same address. 

Muchos usuarios pueden relacionarse con el mismo proveedor de servicio. A través de este proveedor, cada usuario debe ser capaz de intercambiar mensajes con otro usuario. Para poder entregar estos mensajes, el proveedor del servicio debe ser capaz de identificar sin ambigüedad a cada usuario. En las redes de computadoras, cada usuario se identifica por una `dirección` única. Más adelante discutiremos cómo se construyen y usan estas direcciones. A esta altura, y cuando consideremos transmisión unicast, la principal característica de estas `direcciones` es que son únicas. Dos diferentes usuarios conectados a la misma red no pueden usar la misma dirección.

.. index:: service access point, punto de acceso al servicio

.. Throughout this book, we will define a service as a set of capabilities provided by a system (and its underlying elements) to its user. A user interacts with a service through a `service access point`. Note that as shown in the figure above, users interact with one service provider. In practice, the service provider is distributed over several hosts, but these are implementation details that are not important at this stage. These interactions between a user and a service provider are expressed in [X200]_ by using primitives, as show in the figure below. These primitives are an abstract representation of the interactions between a user and a service provider. In practice, these interactions could be implemented as system calls for example.

A lo largo de este libro, definiremos un servicio como un conjunto de capacidades provistas por un sistema (y sus elementos subyacentes) a sus usuarios. Un usuario interactúa con un servicio a través de un `punto de acceso al servicio`. Nótese que, como se muestra en la figura anterior, los usuarios interactúan con un proveedor de servicio. En la práctica, el proveedor de servicio estará distribuido en varios nodos; pero éstos son detalles de implementación que no son importantes en este momento. Estas interacciones entre usuario y proveedor de servicio están expresadas en [X200]_ usando primitivas, como se ve en la figura siguiente. Estas primitivas son una representación abstracta de las interacciones entre un usuario y un proveedor de servicio. En la práctica, estas interacciones podrían ser implementadas, por ejemplo, como llamadas a sistema (`system calls`).

.. figure:: svg/intro-figures-016-c.*
   :align: center
   :scale: 80 

   Los cuatro tipos de primitivas
..   The four types of primitives

.. index:: service primitives, primitivas de servicio

.. Four types of primitives are defined :

Se definen cuatro tipos de primitivas:

 - `X.request`. Este tipo de primitiva corresponde a una solicitud emitida por un usuario a un proveedor de servicio.
 - `X.indication`. Indicación generada por el proveedor de red y enviada a un usuario (frecuentemente relacionada con una primitiva `X.request` anterior y remota)
 - `X.response`. Generada por un usuario como respuesta a una primitiva anterior de tipo `X.indication`. 
 - `X.confirm`. Enviada por el proveedor del servicio para confirmar a un usuario que una primitiva anterior suya de tipo `X.request` ha sido exitosamente procesada.
 

..  - `X.request`. This type of primitive corresponds to a request issued by a user to a service provider
..  - `X.indication`. This type of primitive is generated by the network provider and delivered to a user (often related to an earlier and remote `X.request` primitive)
..  - `X.response`. This type of primitive is generated by a user to answer to an earlier `X.indication` primitive 
..  - `X.confirm`. This type of primitive is delivered by the service provide to confirm to a user that a previous `X.request` primitive has been successfully processed.

.. index:: Connectionless service, servicio sin conexión
.. index:: Service Data Unit, SDU, Unidad de Servicio de Datos

.. Primitives can be combined to model different types of services. The simplest service in computer networks is called the `connectionless service` [#fconnectionless]_. This service can be modelled by using two primitives :

Las primitivas pueden combinarse para modelar diferentes tipos de servicio. El servicio más simple en redes de computadoras se llama `servicio sin conexión` [#fconnectionless]_. Este servicio se puede modelar usando dos primitivas:

 - `Data.request(origen,destino,SDU)`. Esta primitiva es emitida por un usuario que especifica, como parámetros, su dirección (origen del mensaje), la dirección del destinatario del mensaje, y el mensaje en sí. Usaremos el término `SDU` (`Service Data Unit`, Unidad de Servicio de Datos) para referirnos al mensaje que es intercambiado transparentemente entre dos usuarios de un servicio.
 - `Data.indication(origen,destino,SDU)`. Esta primitiva es enviada por un proveedor de servicio a un usuario. Contiene como parámetros una SDU además de las direcciones de los usuarios emisor y destinatario.

.. - `Data.request(source,destination,SDU)`. This primitive is issued by a user that specifies, as parameters, its (source) address, the address of the recipient of the message and the message itself. We will use `Service Data Unit` (SDU) to name the message that is exchanged transparently between two users of a service.
.. - `Data.indication(source,destination,SDU)`. This primitive is delivered by a service provider to a user. It contains as parameters a `Service Data Unit` as well as the addresses of the sender and the destination users. 

.. index:: time-sequence diagram, diagrama de secuencia de tiempo

.. When discussing the service provided in a computer network, it is often useful to be able to describe the interactions between the users and the provider graphically. A frequently used representation is the `time-sequence diagram`. In this chapter and later throughout the book, we will often use diagrams such as the figure below. A time-sequence diagram describes the interactions between two users and a service provider. By convention, the users are represented in the left and right parts of the diagram while the service provider occupies the middle of the diagram. In such a time-sequence diagram, time flows from the top, to the bottom of the diagram. Each primitive is represented by a plain horizontal arrow, to which the name of the primitive is attached. The dashed lines are used to represent the possible relationship between two (or more) primitives. Such a diagram provides information about the ordering of the different primitives, but the distance between two primitives does not represent a precise amount of time.

Al discutir el servicio provisto en una red de computadoras, con frecuencia es útil poder describir las interacciones entre los usuarios y el proveedor, gráficamente. Una representación usada a menudo es el `diagrama de secuencia de tiempo`. En este capítulo, y más adelante en el libro, usaremos frecuentemente diagramas como el de la figura siguiente. Un diagrama de secuencia de tiempo describe las interacciones entre dos usuarios y un proveedor de servicio. Por convención, los usuarios se representan en las partes izquierda y derecha del diagrama, mientras que el proveedor del servicio ocupa la parte media. En estos diagramas, el tiempo fluye desde arriba hacia abajo. Cada primitiva se representa con una flecha horizontal llena, a la cual se adjunta el nombre de la primitiva. Las líneas punteadas se usan para representar la posible relación entre dos o más primitivas. Estos diagramas proveen información sobre el ordenamiento de las diferentes primitivas, pero la distancia entre ellas no representa una cantidad precisa de tiempo.

.. index:: connectionless service, servicio sin conexión

.. The figure below provides a representation of the connectionless service as a `time-sequence diagram`. The user on the left, having address `S`, issues a `Data.request` primitive containing SDU `M` that must be delivered by the service provider to destination `D`. The dashed line between the two primitives indicates that the `Data.indication` primitive that is delivered to the user on the right corresponds to the `Data.request` primitive sent by the user on the left.

La figura siguiente ofrece una representación del servicio sin conexión como un `diagrama de secuencia de tiempo`. El usuario a la izquierda, que tiene dirección `S`, emite una primitiva `Data.request` conteniendo la SDU `M`, que debe ser enviada por el proveedor del servicio al destino `D`. La línea punteada entre las dos primitivas indica que la primitiva `Data.indication` que es enviada al usuario de la derecha corresponde a la primitiva `Data.request` enviada por el usuario a la izquierda.

.. figure:: svg/intro-figures-017-c.*
   :align: center
   :scale: 80 

   Un servicio simple sin conexión
..   A simple connectionless service

.. index:: reliable connectionless service, unreliable connectionless service, servicio confiable sin conexión, servicio sin conexión no confiable

.. There are several possible implementations of the connectionless service, which we will discuss later in this book. Before studying these realisations, it is useful to discuss the possible characteristics of the connectionless service. A `reliable connectionless service` is a service where the service provider guarantees that all SDUs submitted in `Data.requests` by a user will eventually be delivered to their destination. Such a service would be very useful for users, but guaranteeing perfect delivery is difficult in practice. For this reason, computer networks usually support an `unreliable connectionless service`.

Hay varias posibles implementaciones del servicio sin conexión, el cual discutiremos más adelante en este libro. Antes de estudiar estas implementaciones, es útil discutir las posibles características del servicio sin conexión. Un `servicio sin conexión, confiable` es aquél donde el proveedor del servicio garantiza que todas las SDUs enviadas en `Data.requests` por un usuario serán eventualmente entregadas a su destino. Este servicio sería muy útil para los usuarios, pero garantizar entrega perfecta es difícil en la práctica. Por este motvo, las redes de computadoras usualmente soportan un `servicio sin conexión, no confiable`.

.. An `unreliable connectionless` service may suffer from various types of problems compared to a `reliable connectionless service`. First of all, an `unreliable connectionless service` does not guarantee the delivery of all SDUs. This can be expressed graphically by using the time-sequence diagram below.

Un `servicio sin conexión, no confiable` puede sufrir varios tipos de problemas en comparación con un `servicio sin conexión, confiable`. Para empezar, un `servicio sin conexión, no confiable` no garantiza el envío de todas las SDUs. Esto puede expresarse gráficamente usando el diagrama de secuencia de tiempo siguiente.

.. figure:: svg/intro-figures-034-c.*
   :align: center
   :scale: 80 

   Un servicio sin conexión, no confiable, puede perder SDUs
..   An unreliable connectionless service may loose SDUs

.. In practice, an `unreliable connectionless service` will usually deliver a large fraction of the SDUs. However, since the delivery of SDUs is not guaranteed, the user must be able to recover from the loss of any SDU. 

En la práctica, un `servicio sin conexión no confiable` entregará una gran proporción de las SDUs. Sin embargo, como la entrega de SDUs no está garantizada, el usuario debe ser capaz de recuperarse de la pérdida de cualquier SDU.

.. comment:: I have already altered it here below, but suggestion: "Some unreliable connectionless service providers may deliver a SDU, sent by a user, multiple times to the same recipient."

.. A second imperfection that may affect an `unreliable connectionless service` is that it may duplicate SDUs. Some unreliable connectionless service providers may deliver an SDU sent by a user twice or even more. This is illustrated by the time-sequence diagram below.

Una segunda imperfección que puede afectar a un `servicio sin conexión no confiable` es que puede duplicar SDUs. Algunos proveedores de servicio sin conexión no confiable pueden entregar una SDU enviada por un usuario dos o más veces. Esto se ilustra por el diagrama de secuencia de tiempo siguiente.

.. figure:: svg/intro-figures-033-c.*
   :align: center
   :scale: 80 

   Un servicio sin conexión no confiable puede duplicar SDUs
..   An unreliable connectionless service may duplicate SDUs

.. Finally, some unreliable connectionless service providers may deliver to a destination a different SDU than the one that was supplied in the `Data.request`. This is illustrated in the figure below. 

Finalmente, algunos proveedores de servicio sin conexión no confiable pueden entregar en el destino una SDU diferente de la que fue provista en el `Data.request`. Esto se ilustra en la figura siguiente. 

.. figure:: svg/intro-figures-035-c.*
   :align: center
   :scale: 80 

   Un servicio sin conexión no confiable puede entregar SDUs erróneas
..   An unreliable connectionless service may deliver erroneous SDUs

.. When a user interacts with a service provider, it must precisely know the limitations of the underlying service to be able to overcome any problem that may arise. This requires a precise definition of the characteristics of the underlying service.

Cuando un usuario interactúa con un proveedor de servicio, debe conocer con precisión las limitaciones del servicio subyacente para poder reaccionar a cualquier problema que pueda presentarse. Esto requiere una definición precisa de las características del servicio subyacente.

.. index:: ordering of SDUs, ordenamiento de SDUs

.. Another important characteristic of the connectionless service is whether it preserves the ordering of the SDUs sent by one user. From the user's viewpoint, this is often a desirable characteristic. This is illustrated in the figure below.

Otra importante característica del servicio sin conexión es si preserva el orden de las SDUs enviadas por un usuario. Desde el punto de vista del usuario, esto a menudo es una característica deseable. Esto se ilustra en la figura siguiente.

.. figure:: png/intro-figures-036-c.png
   :align: center
   :scale: 80 

   Un servicio sin conexión que preserva el orden de SDUs enviadas por un usuario dado
..   A connectionless service that preserves the ordering of SDUs sent by a given user

.. However, many connectionless services, and in particular the unreliable services, do not guarantee that they will always preserve the ordering of the SDUs sent by each user. This is illustrated in the figure below.

Sin embargo, muchos servicios sin conexión, y en particular los no confiables, no garantizan que siempre preservarán el orden de las SDUs enviadas por cada usuario. Esto se ilustra en la figura siguiente.

.. figure:: svg/intro-figures-037-c.*
   :align: center
   :scale: 80 

   Un servicio sin conexión que no preserva el orden de las SDUs enviadas por un usuario dado
..   A connectionless service that does not preserve the ordering of SDUs sent by a given user

.. index:: confirmed connectionless service, servicio sin conexión confirmado

.. The `connectionless service` is widely used in computer networks as we will see later in this book. Several variations to this basic service have been proposed. One of these is the `confirmed connectionless service`. This service uses a `Data.confirm` primitive in addition to the classical `Data.request` and `Data.indication` primitives. This primitive is issued by the service provider to confirm to a user the delivery of a previously sent SDU to its recipient. Note that, like the registered service of the post office, the `Data.confirm` only indicates that the SDU has been delivered to the destination user. The `Data.confirm` primitive does not indicate whether the SDU has been processed by the destination user. This `confirmed connectionless service` is illustrated in the figure below.

El `servicio sin conexión` es ampliamente usado en redes de computadoras, como veremos más adelante. Se han propuesto varias variaciones a este servicio básico. Una de éstas es el `servicio confirmado sin conexión`. Este servicio usa una primitiva `Data.confirm` agregada a las primitivas clásicas `Data.request` y `Data.indication`. Esta primitiva es enviada por el proveedor del servicio para confirmarle a un usuario la entrega de una SDU, previamente enviada, a su destinatario. Nótese que, como el servicio certificado de la oficina de correos, el `Data.confirm` solamente indica que la SDU ha sido entregada al destinatario. No indica, en cambio, si la SDU ha sido procesada por él. Este servicio `confirmado sin conexión` se ilustra en la figura siguiente.


.. figure:: svg/intro-figures-018-c.*
   :align: center
   :scale: 80 

   Un servicio confirmado sin conexión
..   A confirmed connectionless service

.. index:: connection-oriented service

.. The `connectionless service` we have described earlier is frequently used by users who need to exchange small SDUs. Users needing to either send or receive several different and potentially large SDUs, or who need structured exchanges often prefer the `connection-oriented service`. 

El `servicio sin conexión` que hemos descrito anteriormente es utilizado a menudo por usuarios que necesitan intercambiar SDUs pequeñas. Los usuarios que necesitan enviar o recibir varias SDUs diferentes y potencialmente grandes, o que necesitan intercambios estructurados, con frecuencia prefieren el `servicio orientado a conexión`.

.. index:: connection establishment, establecimiento de conexión

.. An invocation of the `connection-oriented service` is divided into three phases. The first phase is the establishment of a `connection`. A `connection` is a temporary association between two users through a service provider. Several connections may exist at the same time between any pair of users. Once established, the connection is used to transfer SDUs. `Connections` usually provide one bidirectional stream supporting the exchange of SDUs between the two users that are associated through the `connection`. This stream is used to transfer data during the second phase of the connection called the `data transfer` phase. The third phase is the termination of the connection. Once the users have finished exchanging SDUs, they request to the service provider to terminate the connection. As we will see later, there are also some cases where the service provider may need to terminate a connection itself.

Una invocación del `servicio orientado a conexión` se divide en tres fases. La primera fase es el establecimiento de una `conexión`, la cual es una asociación termporaria entre dos usuarios a través de un proveedor de servicio. Pueden existir varias conexiones simultáneas entre dos usuarios cualesquiera. Una vez establecida, la conexión se usa para transferir SDUs. Las `conexiones` usualmente proveen un flujo bidireccional soportando el intercambio de SDUs entre los dos usuarios que están asociados a través de la `conexión`. Este flujo se usa para transferir datos durante la segunda fase de la conexión, llamada `transferencia de datos`. La tercera fase es la terminación de la conexión. Una vez que los usuarios han terminado de intercambiar SDUs, solicitan al proveedor de servicio que termine la conexión. Como veremos más tarde, también hay algunos casos donde el proveedor puede necesitar terminar la conexión por su cuenta.

.. comment:: perhaps in the following paragraph it would provide more clarity to specify which host considers the connection to be open at which stage (first destination, then sender from my understanding). There are two sentences in this paragraph that begin with the phrase: "At this point, the connection is considered to be open". This might be confusing to somebody...somewhere....


.. The establishment of a connection can be modelled by using four primitives : `Connect.request`, `Connect.indication`, `Connect.response` and `Connect.confirm`. The `Connect.request` primitive is used to request the establishment of a connection. The main parameter of this primitive is the `address` of the destination user. The service provider delivers a `Connect.indication` primitive to inform the destination user of the connection attempt. If it accepts to establish a connection, it responds with a `Connect.response` primitive. At this point, the connection is considered to be open and the destination user can start sending SDUs over the connection. The service provider processes the `Connect.response` and will deliver a `Connect.confirm` to the user who initiated the connection. The delivery of this primitive terminates the connection establishment phase. At this point, the connection is considered to be open and both users can send SDUs. A successful connection establishment is illustrated below.

El establecimiento de una conexión puede ser modelada usando cuatro primitivas: `Connect.request`, `Connect.indication`, `Connect.response` y `Connect.confirm`. La primitiva `Connect.request` se usa para requerir el establecimiento de una conexión. El principal parámetro de esta primitiva es la `dirección` del usuario destinatario. El proveedor envía una primitiva `Connect.indication` para informar al destinatario del intento de conexión. En este punto, la conexión se considera abierta para el destinatario, quien puede comenzar a enviar SDUs sobre la conexión. El proveedor procesa la respuesta `Connect.response`, y entregará `Connect.confirm` al usuario que inició la conexión. La entrega de esta primitiva termina la fase de establecimiento de conexión. En este punto la conexión se considera abierta para el emisor, y ambos usuarios pueden enviar sus SDUs. A continuación se ilustra un establecimiento de conexión exitoso.

.. figure:: svg/intro-figures-019-c.*
   :align: center
   :scale: 80 

   Establecimiento de conexión
..   Connection establishment


.. The example above shows a successful connection establishment. However, in practice not all connections are successfully established. One reason is that the destination user may not agree, for policy or performance reasons, to establish a connection with the initiating user at this time. In this case, the destination user responds to the `Connect.indication` primitive by a `Disconnect.request` primitive that contains a parameter to indicate why the connection has been refused. The service provider will then deliver a `Disconnect.indication` primitive to inform the initiating user. A second reason is when the service provider is unable to reach the destination user. This might happen because the destination user is not currently attached to the network or due to congestion. In these cases, the service provider responds to the `Connect.request` with a `Disconnect.indication` primitive whose `reason` parameter contains additional information about the failure of the connection.

El ejemplo anterior muestra un establecimiento de conexión exitoso. Sin embargo, en la práctica no todas las conexiones se establecen exitosamente. Una razón es que el usuario destinatario puede no estar de acuerdo, por razones de política o de prestaciones, en establecer una conexión con el usuario que la inicia, en ese preciso momento. En este caso, el usuario destinatario responde a la primitiva `Connect.indication` con una primitiva `Disconnect.request`, conteniendo un parámetro que indica por qué la conexión ha sido rehusada. El proveedor de servicio entonces entregará una primitiva `Disconnect.indication` para informar al usuario que inició la conexión. Una segunda razón aparece cuando el proveedor de servicio no es capaz de llegar al usuario destinatario.  Esto podría ocurrir porque el destinatario no está momentáneamente conectado a la red, o debido a congestión. En esos casos, el provedor de servicio responde a la solicitud `Connect.request` con una indicación `Disconnect.indication` cuyo parámetro `motivo` contiene información adicional sobre la falla de la conexión.

.. figure:: svg/intro-figures-020-c.*
   :align: center
   :scale: 80 

   Dos tipos de rechazo de un intento de establecimiento de conexión
..   Two types of rejection for a connection establishment attempt


.. index:: message-mode data transfer

.. Once the connection has been established, the service provider supplies two data streams to the communicating users. The first data stream can be used by the initiating user to send SDUs. The second data stream allows the responding user to send SDUs to the initiating user. The data streams can be organised in different ways. A first organisation is the `message-mode` transfer. With the `message-mode` transfer, the service provider guarantees that one and only one `Data.indication` will be delivered to the endpoint of the data stream for each `Data.request` primitive issued by the other endpoint. The `message-mode` transfer is illustrated in the figure below. The main advantage of the `message-transfer` mode is that the recipient receives exactly the SDUs that were sent by the other user. If each SDU contains a command, the receiving user can process each command as soon as it receives a SDU.

Una vez que la conexión ha sido establecida, el proveedor de servicio ofrece dos flujos de datos a los usuarios que se comunican. El primer flujo de datos puede ser usado por el usuario que inició la conexión para enviar SDUs. El segundo flujo permite, al usuario que responde, enviar SDUs hacia el primero. Los flujos de datos pueden ser organizados en diferentes formas. Una primera organización es la transferencia `modo mensaje`. En el `modo mensaje`, el proveedor de servicio garantiza que una, y sólo una, indicación `Data.indication` será enviada a un terminal del flujo de datos por cada primitiva `Data.request` que haya sido emitida por el otro terminal. La transferencia en `modo mensaje` se ilustra en la figura siguiente. La principal ventaja del modo es que el receptor recibe exactamente las SDUs que fueron enviadas por el otro usuario. Si cada SDU contiene un comando, el usuario receptor puede procesar cada comando apenas lo recibe en forma de SDU.

.. figure:: svg/intro-figures-021-c.*
   :align: center
   :scale: 80 

   Transferencia en modo de mensajes en un servicio orientado a conexión
..   Message-mode transfer in a connection oriented service

.. index:: stream-mode data transfer

.. Unfortunately, the `message-mode` transfer is not widely used on the Internet. On the Internet, the most popular connection-oriented service transfers SDUs in `stream-mode`. With the `stream-mode`, the service provider supplies a byte stream that links the two communicating users. The sending user sends bytes by using `Data.request` primitives that contain sequences of bytes as SDUs. The service provider delivers SDUs containing consecutive bytes to the receiving user by using `Data.indication` primitives. The service provider ensures that all the bytes sent at one end of the stream are delivered correctly in the same order at the other endpoint. However, the service provider does not attempt to preserve the boundaries of the SDUs. There is no relation enforced by the service provider between the number of `Data.request` and the number of `Data.indication` primitives. The `stream-mode` is illustrated in the figure below. In practice, a consequence of the utilisation of the `stream-mode` is that if the users want to exchange structured SDUs, they will need to provide the mechanisms that allow the receiving user to separate successive SDUs in the byte stream that it receives. As we will see in the next chapter, application layer protocols often use specific delimiters such as the end of line character to delineate SDUs in a bytestream.

Desafortunadamente, la transferencia en `modo mensaje` no es ampliamente usada en Internet. En Internet, el servicio orientado a conexión más popular transfiere SDUs en `modo flujo`. Con `modo flujo`, el proveedor de servicio ofrece un flujo de bytes que vincula a los dos usuarios que se comunican. El usuario emisor envía bytes usando primitivas `Data.request` que contienen secuencias de bytes como SDUs. El proveedor de servicio entrega SDUs conteniendo bytes consecutivos al usuario receptor, usando primitivas `Data.indication`. El proveedor asegura que todos los bytes enviados en un extremo del flujo sean entregados correctamente y en orden en el otro extremo. Sin embargo, no intenta preservar los límites de las SDUs. No hay ninguna relación impuesta por el proveedor, entre la cantidad de `Data.request` y la cantidad de primitivas `Data.indication`. El `modo flujo` se ilustra en la figura siguiente. En la práctica, una consecuencia de la utilización del `modo flujo` es que si los usuarios quieren intercambiar SDUs estructuradas, necesitarán proveer los mecanismos que permitan, al usuario receptor, separar las sucesivas SDUs en el flujo de bytes que recibe. Como veremos en el próximo carácter, los protocolos de Capa de Aplicación con frecuencia usan delimitadores específicos como el carácter de fin de línea para delimitar SDUs en un flujo de bytes.

.. figure:: svg/intro-figures-022-c.*
   :align: center
   :scale: 80 

   Transferencia en modo de flujo en un servicio orientado a conexión
..   Stream-mode transfer in a connection oriented service

.. index:: abrupt connection release, liberación abrupta de conexión

.. The third phase of a connection is when it needs to be released. As a connection involves three parties (two users and one service provider), any of them can request the termination of the connection. Usually, connections are terminated upon request of one user once the data transfer is finished. However, sometimes the service provider may be forced to terminate a connection. This can be due to lack of resources inside the service provider or because one of the users is not reachable anymore through the network. In this case, the service provider will issue `Disconnect.indication` primitives to both users. These primitives will contain, as parameter, some information about the reason for the termination of the connection. Unfortunately, as illustrated in the figure below, when a service provider is forced to terminate a connection it cannot guarantee that all SDUs sent by each user have been delivered to the other user. This connection release is said to be abrupt as it can cause losses of data.

La tercera fase de una conexión es cuando necesita ser liberada. Como una conexión involucra tres partes (dos usuarios y un proveedor de servicio), cualquiera de ellos puede requerir la terminación de la conexión. Normalmente, las conexiones son terminadas a solicitud de un usuario, una vez que ha terminado la transferencia de datos. Sin embargo, a veces el proveedor del servicio puede verse forzado a terminar una conexión. Esto puede deberse a falta de recursos dentro del proveedor o a que uno de los usuarios ya no es alcanzable a través de la red. En este caso, el proveedor emitirá primitivas `Disconnect.indication` a ambos usuarios. Estas primitivas contendrán, como parámetro, alguna información acerca del motivo de la terminación de la conexión. Desafortunadamente, como se ilustra en la figura siguiente, cuando un proveedor de servicio es forzado a terminar una conexión, no puede garantizar que todas las SDUs enviadas por cada usuario hayan sido entregadas al otro. Esta liberación de conexión se llama `abrupta`, y puede causar pérdidas de datos.

.. figure:: svg/intro-figures-038-c.*
   :align: center
   :scale: 80 

   Liberación abrupta de conexión iniciada por el proveedor del servicio
..   Abrupt connection release initiated by the service provider


.. An abrupt connection release can also be triggered by one of the users. If a user needs, for any reason, to terminate a connection quickly, it can issue a `Disconnect.request` primitive and to request an abrupt release. The service provider will process the request, stop the two data streams and deliver the `Disconnect.indication` primitive to the remote user as soon as possible. As illustrated in the figure below, this abrupt connection release may cause losses of SDUs.

Una liberación abrupta de conexión también puede ser disparada por uno de los usuarios. Si un usuario necesita, por cualquier razón, terminar rápidamente una conexión, puede emitir una primitiva `Disconnect.request` para requerir una liberación abrupta. El proveedor del servicio procesará la solicitud, detendrá los dos flujos de datos y entregará la primitiva `Disconnect.indication` al usuario remoto tan pronto como sea posible. Como se ilustra en la figura siguiente, esta liberación abrupta de conexión puede causar pérdidas de SDUs.



.. figure:: svg/intro-figures-023-c.*
   :align: center
   :scale: 80 

   Liberación abrupta de conexión iniciada por un usuario
..   Abrupt connection release initiated by a user

.. index:: graceful connection release, liberación correcta de conexión 

.. To ensure a reliable delivery of the SDUs sent by each user over a connection, we need to consider the two streams that compose a connection as independent. A user should be able to release the stream that it uses to send SDUs once it has sent all the SDUs that it planned to send over this connection, but still continue to receive SDUs over the opposite stream. This `graceful` connection release is usually performed as shown in the figure below. One user issues a `Disconnect.request` primitive to its provider once it has issued all its `Data.request` primitives. The service provider will wait until all `Data.indication` primitives have been delivered to the receiving user before issuing the `Disconnnect.indication` primitive. This primitive informs the receiving user that it will no longer receive SDUs over this connection, but it is still able to issue `Data.request` primitives on the stream in the opposite direction. Once the user has issued all of its `Data.request` primitives, it issues a `Disconnnect.request` primitive to request the termination of the remaining stream. The service provider will process the request and deliver the corresponding `Disconnect.indication` to the other user once it has delivered all the pending `Data.indication` primitives. At this point, all data has been delivered and the two streams have been released successfully and the connection is completely closed.

Para asegurar una entrega confiable de las SDUs enviadas por cada usuario sobre una conexión, necesitamos considerar los dos flujos que componen una conexión como independientes. Un usuario debe ser capaz de liberar el flujo que usa para enviar SDUs, una vez que haya enviado todas las que planeaba enviar sobre esta conexión; pero debería continuar recibiendo SDUs sobre el flujo opuesto. Esta liberación `correcta` ("`graceful`") de conexión se ejecuta normalmente como se muestra en la figura siguiente. Un usuario emite una primitiva `Disconnect.request` a su proveedor una vez que ha emitido todas sus primitivas `Data.request`. El proveedor de servicio esperará hasta que todas las primitivas `Data.indication` hayan sido entregadas al usuario receptor antes de entregar la primitiva `Disconnnect.indication`. Esta primitiva informa al usuario receptor que ya no recibirá más SDUs por esta conexión; pero que aún puede emitir primitivas `Data.request` sobre el flujo que corre en dirección opuesta. Una vez que el usuario haya emitido todas las primitivas `Data.request`, emite una `Disconnnect.request` para solicitar la terminación del flujo restante. El proveedor de servicio procesará la solicitud y entregará la correspondiente `Disconnect.indication` al otro usuario, una vez que haya entregado todas las primitivas `Data.indication`  pendientes. Llegados a este punto, todos los datos han sido entregados y los dos flujos han sido liberados exitosamente; la conexión está completamente cerrada.

.. figure:: svg/intro-figures-024-c.*
   :align: center
   :scale: 80 

   Liberación correcta de conexión 
..   Graceful connection release


.. .. note:: Reliability of the connection-oriented service

.. An important point to note about the connection-oriented service is its reliability. A `connection-oriented` service can only guarantee the correct delivery of all SDUs provided that the connection has been released gracefully. This implies that while the connection is active, there is no guarantee for the actual delivery of the SDUs exchanged as the connection may need to be released abruptly at any time. 

.. note:: Confiabilidad del servicio orientado a conexión

 Un punto importante a notar sobre el servicio orientado a conexión es su confiabilidad. Un servicio `orientado a conexión` sólo puede garantizar la entrega correcta de todas las SDUs si la conexión ha sido liberada correctamente. Esto implica que mientras la conexión esté activa, no habrá garantías sobre la entrega real de las SDUs intercambiadas, ya que la conexión puede ser liberada abruptamente en cualquier momento. 

.. rubric:: Footnotes

.. .. [#fconnectionless] This service is called the connectionless service because there is no need to create a connection before transmitting any data in contrast with the connection-oriented service.

.. [#fconnectionless] Este servicio se llama `sin conexión` porque no hay necesidad de crear una conexión antes de transmitir datos, en contraste con el `servicio orientado a conexión`.

.. include:: ../links.rst
