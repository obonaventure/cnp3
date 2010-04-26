
============
Introduction
============

When the first computers were built during the second world war, they were expensive and isolated. However, after about twenty years, as their prices were decreasing and the first experiments were started to connect computers together. In 1964, `Paul Baran`_ and `Donald Davies`_ published independently the first papers describing the idea of building computer networks. Given the cost of computers, sharing them over a long distance was an interesting idea. In the US, the :term:`ARPANET` started in 1969 and continued until the mid 1980s. In France, `Louis Pouzin`_ developed the Cyclades network. During the 1970s, the telecommunication and the computer industry became interested in computer networks. The telecommunication industry bet on the X25_. Many local area networks such as Ethernet or Token Ring were designed at that time. During the 1980s, the need to interconnect more and more computers lead most computer vendors to develop their own suite of networking protocols. Xerox developed XNS, DEC chose DECNet, IBM developed SNA, Microsoft introduced NetBIOS, Apple bet on Appletalk, ... In the research community, ARPANET was decommissioned and replaced by TCP/IP and the reference implementation was developed inside BSD Unix. Universities who were already running Unix could thus adopt TCP/IP easily and vendors of Unix workstations such as Sun or Silicon Graphics included TCP/IP in their variant of Unix. In parallel, the :term:`ISO`, with support from the governments, worked on developing an open [#open]_ suite of networking protocols. In the end, TCP/IP became the de facto standard that is used not only within the research community. During the 1990s and the early 2000s, the growth of the usage of TCP/IP continued and today proprietary protocols are seldom used. As shown by the figure below that provides the estimation of the number of hosts attached to the Internet, the Internet sustained a huge growth during the last 20+ years.


.. figure:: png/intro-figures-006-c.png
   :align: center
   :scale: 50 

   Estimation of the number of hosts on the Internet


Recent estimations of the number of hosts attached to the Internet show a continuing growth since 20+ years. However, although the number of hosts attached to the Internet is high, it should be compared to the number of mobile phones that are in use today. More and more of these mobile phones will be connected to the Internet. Furthermore, thanks to the availability of TCP/IP implementations requiring limited resources such as uIP_ , we can expect to see a growth of the TCP/IP enabled embedded devices.  

.. figure:: png/intro-figures-007-c.png
   :align: center
   :scale: 50 

   Estimation of the number of mobile phones

Before looking at the services that are provided by computer networks, it is useful to agree on some terminology that is widely used in the networking literature. First, computer networks are often classified as function of the geographical area that they cover

- :term:`LAN` : a local area network typically interconnects hosts that are up to a few or maybe a few tens of kilometers apart. 
- :term:`MAN` : a metropolitan area network typically interconnects devices that are up to a few hundred kilometers apart
- :term:`WAN` : a wide area network interconnect hosts that can be located anywhere on Earth

Another classification of computer networks is based on their physical topology. In the following figures, physical links are represented as lines while boxes show computers or other types of networking equipment.

Computer networks are used to allow several hosts to exchange information between themselves. In order to allow any host to send messages to any other host in the network, the easiest solution is to organise them as a full-mesh with a direct and dedicated link between each pair of hosts. Such a physical topology is sometimes used, especially when high performance and high redundancy is required for a small number of hosts. However, it has two major drawbacks :

- for a network containing `n` hosts, each host must have `n-1` physical interfaces. Thus, in practice the number of physical interfaces on a node will limit the size of a full-mesh network that can be built
- for a network containing `n` hosts, `n*(n-1)/2` links are required. This is possible when there are a few nodes in the same room, but rarely when they are located several kilometers apart

.. figure:: png/intro-figures-001-c.png
   :align: center
   :scale: 50 

   A Full mesh network

The second possible physical organisation, which is used inside computers to connect different extension cards, is the bus. In a bus network, all hosts are attached to a shared medium, usually a cable through a single interface. When one hosts sends a signal on the bus, the signal is received by all hosts attached to the bus. A drawback of bus-based networks is that if the bus is physically cut, then the network is split in two different networks.  For this reason, bus-based networks are sometimes considered to be difficult to manage especially when the cable is long and there are many places where it can break. Such as bus-based topology is used for example by Ethernet networks.

.. figure:: png/intro-figures-002-c.png
   :align: center
   :scale: 50 

   A network organised as a Bus

A third organisation of a computer network is a star topology. In such topologies, the hosts have a single physical interface and there is one physical link between each host and the center of the star. The node at the center of the star can be either a passive device such as an equipment that amplifies electrical signal or an active device such as an equipment that understands the format of the messages exchanged through the network. Of course, the failure of the central node implies the failure of the network. However, if one physical link fails (e.g. because the cable has been cut), then only one node is disconnected from the network. In practice, star-shaped networks are easier to manage than bus-shaped networks.

.. figure:: png/intro-figures-003-c.png
   :align: center
   :scale: 50 

   A network organised as a Star

A fourth physical organisation is the Ring. As with the bus, each host has a single physical interface that connects it to the ring. Any signal sent by a host on the ring will be received by all hosts attached to the ring. From a redundancy viewpoint, a single ring is not the best solution as the signal travels only in one direction on the ring. If one of the links that compose the ring is cut, then the entire network fails. This makes failure easier to detect than in bus-based networks. In practice, such rings have been used in local area networks, but nowadays they are often replaced by star-shaped networks. In metropolitan are networks, rings are often used to interconnect multiple locations. In this case, two parallel links composed of different cables are often used for redundancy. With such a dual ring, when one ring fails all the traffic can be switched quickly to the other ring.

.. figure:: png/intro-figures-005-c.png
   :align: center
   :scale: 50 

   A network organised as a Ring

A fifth physical organisation of a network is the tree. Such networks are typically used when a large number of customers must be connected in a very cost-effective manner. Cable TV networks are often organised as trees.

.. figure:: png/intro-figures-004-c.png
   :align: center
   :scale: 50 

   A network organised as a Tree
   
In practice, most real networks combine part of these topologies. For example, a campus network can be organised as a ring between the key buildings while smaller buildings are attached as a tree or a star to important buildings. Or an ISP network may have a full mesh of devices in the core of its network and trees to connect remote users.

Throughout this book, our objective will be to understand the protocols and mechanisms that are necessary for a network such as the one shown below.

.. figure:: png/intro-figures-013-c.png
   :align: center
   :scale: 50 

   A simple internetwork


The last point of terminology that we need to discuss are the transmission modes. When exchanging information through a network, we often distinguish three transmission modes. In TV and radio transmission, :term:`broadcast` is often used to indicate a technology that send a video or radio signal to all receivers in a given geographical area. Broadcast is sometimes used in computer networks, but only in local area networks where the number of recipients is limited.

The first and most widespread transmission mode is called :term:`unicast` . In the unicast transmission mode, information is sent by one sender to one receiver. Most of today's Internet applications rely on the unicast transmission mode.

.. figure:: png/intro-figures-008-c.png
   :align: center
   :scale: 50 

   Unicast transmission

A second mode of transmission is the :term:`multicast` transmission mode. This mode is used when the same information must be sent to a set of recipients. It was first used in LANs but became later supported in wide area networks. When a sender uses multicast to send information to `N`receivers, the sender sends a single copy of the information and the network nodes duplicate the information whenever necessary so that it can reach all the recipients that belong to the destination group.  

.. figure:: png/intro-figures-009-c.png
   :align: center
   :scale: 50 

   Multicast transmission

The last transmission mode is the :term:`anycast` transmission mode. It was initially defined in :rfc:`1542`. In this transmission mode, a set of receivers is identified. When a source sends information towards this set of receivers, the network ensures that the information is delivered to `one` receiver that belongs to this set. Usually the receiver that is closest to the source is the one that receives the information sent by this particular source. The anycast transmission mode is useful to ensure redundancy as when one of the receivers fails, the network will ensure that information will be delivered to another receiver belonging to the same group. However, in practice supporting the anycast transmission mode can be difficult.

.. figure:: png/intro-figures-010-c.png
   :align: center
   :scale: 50 

   Anycast transmission


Services and protocols
######################

An important point to understand before studying computer networks is the different between a *service* and a *protocol*. 

To understand the difference between the two, it is useful to start from the real world. The traditional Post provides a service which is to deliver letters to recipients. The service can be more precisely 

In computer networks, the notion of service is more formally defined in [X200]_ . It can be better understood by considering a computer networks, what ever its size or complexity as a black box that provides a service to ` users`  as shown in the figure below. These users could be human users or processes running on a computer system. 

.. _fig-users:

.. figure:: png/intro-figures-014-c.png
   :align: center
   :scale: 50 

   Users and service provider

.. index:: address

Many users can be attached to the same service provider. Through this provider, each user must be able to exchange messages with any other user. To be able to deliver these messages, the service provider must be able to unambiguously identify each user. In computer networks, each user is identified by a unique `address`. We will discuss later how these addresses are built and used. At this point, and when considering unicast transmission, the important characteristics of these `addresses` is that they are unique. Two different users attached to the network cannot have the same address. 

.. index:: service access point

Throughout this book, we will define a service as a set of capabilities provided by a system (and its underlying elements) to its user. A user interacts with a service through a `service access point`. Note that as shown in the figure above, the users interact with one service provider. In practice, the service provider is distributed over several hosts, but these are implementation details that are not important at this stage. These interactions between a user an a service provider are expressed in [X200]_ by using primitives as show in the figure below. These primitives are an abstract representation of the interactions between a user and a service provider. In practice, these interactions could be implemented as system calls for example.

.. figure:: png/intro-figures-016-c.png
   :align: center
   :scale: 50 

   The four types of primitives

.. index:: service primitives

Four types of primitives are defined :

 - `X.request`. This type of primitive corresponds to a request issued by a user to a service provider
 - `X.indication`. This type of primitive is generated by the network provider and delivered to a user (often related to an earlier and remote `X.request` primitive)
 - `X.response`. This type of primitive is generated by a user to answer to an earlier `X.indication` primitive 
 - `X.confirm`. This type of primitive is delivered by the service provide to confirm to a user that a previous `X.request` has been successfully processed.

.. index: Connectionless service
.. index: Service Data Unit, SDU

Primitives can be combined to model different types of services. The simplest service in computer networks is the connectionless service. This service can be modelled by using two primitives :

 - `Data.request(source,destination,SDU)`. This primitive is issued by a user that specifies as parameters its (source) address, the address of the recipient of the message and the message itself. We will use `Service Data Unit` (SDU) to name the message that is exchanged transparently between two users of a service.
 - `Data.indication(source,destination,SDU)`. This primitive is delivered by a service provider to a user. It contains as parameters a `Service Data Unit` as well as the addresses of the sender and the destination users. 

.. index:: time-sequence diagram

When discussing about the service provided in a computer network, it is often useful to be able to describe the interactions between the users and the provider graphically. A frequently used representation is the time-sequence diagram. In this chapter and later throughout the book, we will often use diagrams such as the figure below. A time-sequence diagram describes the interactions between two users and a service provider. By convention, the users are represented in the left and right parts of the diagram while the service provider occupies the middle of the diagram. In such a time-sequence diagram, time flows from the top of the bottom of the diagram. Each primitive is represented by a plain horizontal arrow to which the name of the primitive is attached. The dashed lines are used to represent the possible relationship between two (or more) primitives. Such a diagram provides information about the ordering of the different primitives, but the distance between two primitives does not represent a precise amount of time.

.. index:: connectionless service

The figure below provides a representation of the connectionless service. The user on the left, having address `S`, issues a `Data.request` primitive containing SDU `M` that must be delivered by the service provider to destination `D`. The dashed line between the two primitives indicates that the `Data.indication` primitive that is delivered to the user on the right corresponds to the `Data.request` primitive sent by the user on the left.

.. figure:: png/intro-figures-017-c.png
   :align: center
   :scale: 50 

   A simple connectionless service

.. index:: reliable connectionless service, unreliable connectionless service

There are several possible implementations of the connectionless service that we will discuss later in this book. Before studying these realisations, it is useful to discuss the possible characteristics of the connectionless service. A `reliable connectionless service` is a service where the service provider guarantees that all SDUs submitted in `Data.requests` by a user will be eventually delivered to their destination. Such a service would be very useful for users, but guaranteeing perfect delivery is difficult in practice. For this reason, computer networks usually support an `unreliable connectionless service`.

An `unreliable connectionless` service may suffer from various types of problems compared to a `reliable connectionless service`. First, an `unreliable connectionless service` does not guarantee the delivery of all SDUs. This can be expressed graphically by using the time-sequence diagram below.

.. figure:: png/intro-figures-034-c.png
   :align: center
   :scale: 50 

   An unreliable connectionless service may loose SDUs

In practice, an `unreliable connectionless service` will usually deliver a large fraction of the SDUs. However, since the delivery of SDUs is not guaranteed, the user must be able to recover from the loss of any SDU. A second imperfection that may affect an `unreliable connectionless service` is that it may duplicate SDUs. Some unreliable connectionless service providers may deliver twice or even more a SDU sent by a user. This is illustrated by the time-sequence diagram below.


.. figure:: png/intro-figures-033-c.png
   :align: center
   :scale: 50 

   An unreliable connectionless service may duplicate SDUs

Finally, some unreliable connectionless service providers may deliver to a destination a different SDU than the one that was provided in the `Data.request`. This is illustrated in the figure below. 

.. figure:: png/intro-figures-035-c.png
   :align: center
   :scale: 50 

   An unreliable connectionless service may deliver erroneous SDUs

When a user interacts with a service provider, it must know precisely the limitations of the underlying service to be able to overcome any problem that may arise. This requires a precise definition of the characteristics of the underlying service.

.. index:: ordering of SDUs

Another important characteristic of the connectionless service is whether it preserves the ordering of the SDUs sent by one user. From the user's viewpoint, this is often a desirable characteristic. This is illustrated in the figure below.

.. figure:: png/intro-figures-036-c.png
   :align: center
   :scale: 50 

   A connectionless service that preserves the ordering of SDUs sent by a given user

However, many connectionless services, and in particular the unreliable connection services do not guarantee that they will always preserve the ordering of the SDUs sent by each user. This is illustrated in the figure below.

.. figure:: png/intro-figures-037-c.png
   :align: center
   :scale: 50 

   An connectionless service that does not preserve the ordering of SDUs sent by a given user


.. index:: confirmed connectionless service

The `connectionless service` is widely used in computer networks as we will see in the next chapter. Several variations to this basic service have been proposed. One of these is the `confirmed connectionless service`. This service uses a `Data.confirm` primitive in addition to the classical `Data.request` and `Data.indication` primitives. This primitive is issued by the service provider to confirm to a user the delivery of a previously sent SDU to its recipient. Note that, like the registered service of the post office, the `Data.confirm` only indicates that the SDU has been delivered to the destination user. The `Data.confirm` primitive does not indicate whether the SDU has been processed by the destination user. This `confirmed connectionless service` is illustrated in the figure below.

.. figure:: png/intro-figures-018-c.png
   :align: center
   :scale: 50 

   A confirmed connectionless service

.. index:: connection-oriented service

The `connectionless service` that we have described earlier is frequently used by users who need to exchange small SDUs. Users who need to either send or receive several different and potentially large SDUs or who need structured exchanges often prefer the `connection-oriented service`. 

.. index:: connection establishment

An invocation of the `connection-oriented service` is divided in three phases. The first phase is the establishment of a `connection`. A `connection` is a temporary association between two users through a service provider. Several connections may exist at the same time between any pair of users. Once established, the connection is used to transfer SDUs. `Connections` usually provide one bidirectional stream that supports the exchange of SDUs between the two users that are associated through the `connection`. This `data transfer` phase is the second phase of a connection. The third phase is the termination of the connection. Once the users have finished to exchange SDUs, they request the service provider to terminate the connection. As we'll see later, there are also some cases where the service provider may need to terminate itself a connection.

The establishment of a connection can be modelled by using four primitives : `Connect.request`, `Connect.indication`, `Connect.response` and `Connect.confirm`. The `Connect.request` primitive is used to request the establishment of a connection. The main parameter of this primitive is the `address` of the destination user. The service provider delivers a `Connect.indication` primitive to inform the destination user of the connection attempt. If it accepts to establish a connection, it responds with a `Connect.response` primitive. At this point, the connection is considered to be open and the destination user can start to send SDUs over the connection. The service provider processes the `Connect.response` and will deliver a `Connect.confirm` to the user who initiated the connection. The delivery of this primitive terminates the connection establishment phase. At this point, the connection is considered to be open and both users can send SDUs. A successful connection establishment is illustrated below.

.. figure:: png/intro-figures-019-c.png
   :align: center
   :scale: 50 

   Connection establishment


The example above shows a successful connection establishment. However, in practice not all connections are successfully established. A first reason is that the destination user may not agree, for policy or performance reasons, to establish a connection with the initiating user at this time. In this case, the destination user responds to the `Connect.indication` primitive by a `Disconnect.request` primitive that contains a parameter to indicate why the connection has been refused. The service provider will then deliver a `Disconnect.indication` primitive to inform the initiating user. A second reason is when the service provider is unable to reach the destination user. This might happen because the destination user is not currently attached to the network or due to congestion. In these cases, the service provider responds to the `Connect.request` with a `Disconnect.indication` primitive whose `reason` parameter contains additional information about the failure of the connection.

.. figure:: png/intro-figures-020-c.png
   :align: center
   :scale: 50 

   Two types of rejection for a connection establishment attempt

.. index:: message-mode data transfer

Once the connection has been established, the service provider supplies two data streams to the communicating users. The first data stream can be used by the initiating user to send SDUs. The second data stream allows the responding user to send SDUs to the initiating user. The data streams can be organised in different ways. A first organisation is the `message-mode` transfer. With the `message-mode` transfer, the service provider guarantees that one and only one `Data.indication` will be delivered to the endpoint of the data stream for each `Data.request` primitive issued by the other endpoint. The `message-mode` transfer is illustrated in the figure below. The main advantage of the `message-transfer` mode is that the recipient receives exactly the SDUs that were sent by the other user. If each SDU contains a command, the receiving user can process each command as soon as it receives a SDU.

.. figure:: png/intro-figures-021-c.png
   :align: center
   :scale: 50 

   Message-mode transfer in a connection oriented service

.. index:: stream-mode data transfer

Unfortunately, the `message-mode` transfer is not widely used on the Internet. On the Internet, the most popular connection-oriented service transfers SDUs in `stream-mode`. With the `stream-mode`, the service provider supplies a byte stream that links the two communicating user. The sending user sends bytes by using `Data.request` primitives that contain groups of bytes as SDUs. The service provider delivers SDUs containing consecutive bytes to the receiving user by using `Data.indication` primitives. The service provider ensures that all the bytes sent at one end of the stream are delivered correctly in the same ordering at the other endpoint. However, the service provider does not attempt to preserve the boundaries of the SDUs. There is no relation enforced by the service provider between the number of `Data.request` and the number of `Data.indication` primitives. The `stream-mode` is illustrated in the figure below. In practice, a competence of the utilisation of the `stream-mode` is that if the users want to exchange structured SDUs, they will need to provide the mechanisms that allow the receiving user to delineate these SDUs in the byte stream that it receives.


.. figure:: png/intro-figures-022-c.png
   :align: center
   :scale: 50 

   Stream-mode transfer in a connection oriented service

.. index:: abrupt connection release


The third phase of a connection is when it needs to be released. As a connection involves three parties (two users and a service provider), any of them can request the termination of the connection. Usually, connections are terminated upon request of one user. However, sometimes the service provider may be forced to terminate a connection. This can be due to lack of resources inside the service provider or because one of the users is not reachable anymore through the network. In this case, the service provider will issue `Disconnect.indication` primitives to both users. These primitives will contain as parameter some information about the reason for the termination of the connection. As illustrated in the figure below, when a service provider is forced to terminate a connection it cannot guarantee that all SDUs sent by each user have been delivered to the other user. This connection release is said to be abrupt as it can cause losses of data.


.. figure:: png/intro-figures-038-c.png
   :align: center
   :scale: 50 

   Abrupt connection release initiated by the service provider


An abrupt connection release can also be triggered by one of the users. If a user needs, for any reason, to terminate a connection quickly, it issues a `Disconnect.request` primitive and requests an abrupt release. The service provider will process the request, stop the two data streams and deliver the `Disconnect.indication` to the remote user as soon as possible. As illustrated in the figure below, this abrupt connection release may cause losses of SDUs.


.. figure:: png/intro-figures-023-c.png
   :align: center
   :scale: 50 

   Abrupt connection release initiated by a user

.. index:: graceful connection release

To ensure a reliable delivery of the SDUs sent by each user over a connection, we need to consider the two streams that compose a connection as independent. A user should be able to release the stream that it uses to send SDUs once it has sent all the SDUs that it planned over this connection, but still continue to receive SDUs over the other stream. This `graceful` connection release is usually performed as shown in the figure below. One user issues a `Disconnect.request` primitives to its provider once it has issued all its `Data.request` primitives. The service provider will wait until all `Data.indication` have been delivered to the receiving user before issuing the `Disconnnect.indication` primitive. This primitive informs the receiving user that he will not receive anymore SDUs over this connection, but he is still able to issue `Data.request` primitives on the stream in the opposite direction. Once the user has issued all his `Data.request` primitives, it issues a `Disconnnect.request` primitive to request the termination of the remaining stream. The service provider will process the request and deliver the corresponding `Data.indication` to the other user once it has delivered all the pending `Data.indication` primitives. At this point, the two streams have been released successfully and the connection is completely closed.


.. figure:: png/intro-figures-024-c.png
   :align: center
   :scale: 50 

   Graceful connection release


.. sidebar:: Reliability of the connection-oriented service

 An important point to discuss about the connection-oriented service is its reliability. In practice, a `connection-oriented` can only guarantee the correct delivery of all SDUs if the connection has been released gracefully. This implies that while the connection is active, there is no guarantee for the actual delivery of the SDUs exchanged as the connection may need to be released abruptly at any time.


.. index:: Reference models

The reference models
####################

Given the growing complexity of computer networks, network researchers proposed during the 1970s reference models that allow to describe network protocols and services. The Open Systems Interconnection (OSI) model [Zimmermann80]_ was probably the most influential one. It was the basis for the standardisation work performed within the :term:`ISO` to develop global computer network standards. The reference model that we use in this book can be considered as a simplified version of the OSI reference model [#fiso-tcp]_.

.. index:: Five layers reference model

The five layers reference model
-------------------------------

Our reference model is divided in five layers as shown in the figure below.

.. figure:: png/intro-figures-026-c.png
   :align: center
   :scale: 50 

   The five layers of the reference model


Starting from the bottom, the first layer is the Physical layer. Two communicating devices are  linked through a physical medium. The physical medium is used to transfer and electrical or optical signal between the two devices. Different types of physical mediums are used in practice : 

 - `electrical cable`. Information can be transmitted over different types of electrical cables. The most common ones are twisted pairs that are used in the telephone network, but also in enterprise networks and coaxial cables. Coaxial cables are still used in cable TV networks, but not anymore in enterprise networks. 
 - `optical fiber`. Optical fibers are frequently used in public and enterprise networks with the distance is larger than one kilometer. 
 - `wireless`. In this case, a radio signal is used to encode the information being exchanged between the communicating devices. 

.. note:: Additional information about the physical layer will be added later.

An important point to note about the Physical layer is the service that it provides. This service is usually an unreliable connection-oriented service that allows the users of the Physical layer to exchange bits. The unit of information transfer in the Physical layer is the bit. The Physical layer service is unreliable because :

 - The Physical layer may change, e.g. due to electromagnetic interferences, the value of a bit being transmitted
 - the Physical layer may deliver `more` bits to the receiver than the bits sent by the sender
 - the Physical layer may deliver `fewer` bits to the receiver than the bits sent by the sender

The last two points may seem strange at first glance. When two devices are attached through a cable, how is it possible for bits to be created or lost on such a cable ? 

This is mainly due to the fact that the communicating devices use their own clock to transmit bits at a given bandwidth. Consider a sender having a clock that ticks one million times per second and sends one bit every tick. Every microsecond, the sender sends an electrical or optical signal that encodes one bit. The sender's bandwidth is thus 1 Mbps. If the receiver clock ticks exactly [#fsynchro]_ every microsecond, it will also deliver 1 Mbps to its user. However, if the receiver's clock is slightly faster (resp. slower), than it will deliver slightly more (resp. less) than one million bits every second.

.. sidebar:: Bandwidth

 In computer networks, the bandwidth achievable through the physical layer is always expressed in bits per second. A Mega bps is one million bits per second and a Giga bps is one billion bits per second. This is in contrast with memory specifications that are usually expressed in bytes (8 bits), KiloBytes ( 1024 bytes) or MegaBytes (1048576 bytes). Thus transferring one MByte through a 1 Mbps link lasts 1.048 seconds.


.. index:: Physical layer


.. figure:: png/intro-figures-027-c.png
   :align: center
   :scale: 50

   The Physical layer


The physical layer allows thus two or more entities that are directly attached to the same transmission medium to exchange bits. Being able to exchange bits is important because virtually any information can be encoded as a sequence of bits. Electrical engineers are used to process streams of bits, but computer scientists usually prefer to deal with higher level concepts. A similar issue arises with file storage. Storage devices such as hard-disks also store streams of bits. There are hardware devices that process the bit stream produced by a hard-disk, but computer scientists have designed filesystems to allow applications to easily access such storage devices. These filesystems are typically divided in several layers as well. Hard-disks store sectors of 512 bytes or more. Unix filesystems groups sectors in larger blocks that can contain data or inodes that represent the structure of the filesystem. Finally, applications manipulate files and directories that are translated in blocks, sectors and eventually bits by the operating system.

.. index:: Datalink layer
.. index:: frame


Computer networks use a similar approach and each layer provides a service that it built above the underlying layer and is closer to the needs of the applications. The `Datalink layer` builds on the service provided by the underlying physical layer. The `Datalink layer` allows two hosts that are directly connected through the physical layer to exchange information. The unit of information exchanged between two entities in the `Datalink layer` is a frame. A frame is a finite sequence of bits. Some `Datalink layers` user variable-length frames while others only use fixed-length frames. Some `Datalink layers` provide a connection-oriented service while others provide a connectionless service. Some `Datalink layers` provide a reliable delivery while others do not guarantee the correct delivery of the information.

An important point to note about the `Datalink layer` is that although the figure below indicates that two entities of the `Datalink layer` exchange frames directly, in reality this is slightly different. When the `Datalink layer` entity on the left needs to transmit a frame, it issues as many `Data.request` to the underlying `physical layer` as there are bits in the frame. The physical layer will then convert the sequence of bits in an electromagnetic physical that will be sent over the physical medium. The `physical layer` on the right side of the figure will decode the received signal, recover the bits and issue the corresponding `Data.indication` primitives to its `Datalink layer` entity. If there are not transmission errors, this entity will receive the frame sent earlier. 


.. figure:: png/intro-figures-028-c.png
   :align: center
   :scale: 50 

   The Datalink layer


.. index:: Network layer, packet

The `Datalink layer` allows directly connected hosts to exchange information, but it is often necessary to exchange information between hosts that are not attached to the same physical medium. This is the task of the `network layer`. The `network layer` is built above the `datalink layer`. The network layer entities exchange `packets`. A `packet` is a finite sequence of bytes. A packet usually contains information about its origin and its destination. A packet usually passes through several intermediate devices called routers on its way from its origin to its destination.

Different types of network layers can be implemented. The Internet uses an unreliable connectionless network layer service. Other networks have used reliable and unreliable connection-oriented network layer services.


.. figure:: png/intro-figures-029-c.png
   :align: center
   :scale: 50 

   The network layer

.. index:: Transport layer, segment

Most realisations, including the Internet, of the network layer do not provide a reliable service. However, many applications need to exchange information reliably and using the network layer service directly would be very difficult for them. Ensuring a reliable delivery of the data produced by applications is the task of the `transport layer`. `Transport layer` entities exchange `segments`. A segment is a finite sequence of bytes. A transport layer entity issues segments (or sometimes part of segments) as `Data.request` to the underlying network layer entity. 

There are different types of transport layers. The most widely used on the Internet are :term:`TCP` that provides a reliable connection-oriented bytestream transport service and :term:`UDP` that provides an unreliable connection-less transport service.


.. figure:: png/intro-figures-030-c.png
   :align: center
   :scale: 50 

   The transport layer

.. index:: Application layer

The upper layer of our architecture is the `Application layer`. It includes all the mechanisms and data structures that are necessary for the applications. We will use Application Data Unit (ADU) to indicate the data exchanged between two entities of the Application layer.

.. figure:: png/intro-figures-031-c.png
   :align: center
   :scale: 50 

   The Application layer

.. index:: TCP/IP reference model


The TCP/IP reference model
--------------------------

In contrast with OSI, the TCP/IP community did not spend a lot of effort at defining a detailed reference model and in fact the goals of the Internet architecture were only documented after TCP/IP had been deployed [Clark88]_. :rfc:`1122` that defines the requirements for Internet hosts mentions four different layers. Starting from the top, these are :

- the application layer
- the transport layer
- the internet layer which is equivalent to the network layer of our reference model
- the link layer which combines the functionalities of the physical and datalink layers.

Besides this difference in the lower layers, the TCP/IP reference model is very close to the five layers that we use throughout this document.

.. index:: OSI reference model

The OSI reference model
-----------------------

Compared to the five layers reference model explained above, the :term:`OSI` reference model defined in [X200]_ is divided in seven layers. The four lower layers are similar to the four lower layers described above. The OSI reference model refined the application layer by dividing it in three layers :

 - the Session layer. The Session layer contains the protocols and mechanisms that are necessary to organize and to synchronize the dialogue and manage the data exchange of presentation layer entities. While one of the main functions of the transport layer is to cope with the unreliability of the network layer, the session's layer objective is to hide the failure of transport-level connections to the upper layer higher. For this, the Session Layer provides services that allow to establish a session-connection, to support orderly data exchange (including mechanisms that allow to recover from the abrupt release of an underlying transport connection), and to release the connection in an orderly manner. 
 - the Presentation layer was designed to cope with the different ways of representing information on computers. There are many differences in the way computer store information. Some computers store integers as 32 bits field, others use 64 bits field and the same problem arises with floating point number. For textual information, this is even more complex with the many different character codes that have been used [#funicode]_. The situation is even more complex when considering the exchange of structured information such as records. To solve this problem, the Presentation layer contains provides for common representation of the data transferred. The :term:`ASN.1` notation was designed for the Presentation layer. 
 - the Application layers that contains the mechanisms that do not fit in neither the Presentation nor the Session layer. The OSI Application layer was itself further divided in several generic service elements. 

.. sidebar:: Where are the missing layers in TCP/IP reference model ?

 The TCP/IP reference places the Presentation and the Session layers implicitly in the Application layer. The main motivations for simplifying the upper layers in the TCP/IP reference model were pragmatic. Most Internet applications started as prototypes that evolved and were standardised later. Many of these applications assumed that they would be used to exchange information written in American English and for which the 7 bits US-ASCII character code was sufficient. This was the case for email, but as we'll see in the next chapter email was able to evolve to support different characters encodings. Some applications considered the different data representations explicitly. For example, :term:`ftp` contained mechanisms to convert a file from one format to another. On the other hand, many ISO specifications were developed by committees composed of people who did not all participate in actual implementations. ISO spent a lot of effort at analysing the requirements and defining a solution that meets all these requirements. Sometimes, the specification was so complex that it was difficult to implement it completely... 

.. The work within ISO and ITU on protocols and services was 

.. figure:: png/intro-figures-032-c.png
   :align: center
   :scale: 50 

   The seven layers of the OSI reference model


Organisation of the document
----------------------------

This document is organised according to the :term:`TCP/IP` reference model and follows a top-down approach. Most of the first networking textbooks chose a bottom-up approach, i.e. they first explained all the electrical and optical details of the physical layer then moved to the datalink layer, ... This approach worked well during the infancy of computer networks and until the late 1990s. At that time, most students were not users of computer networks and it was useful to explain computer networks by building the corresponding protocols from the simplest in the physical layer up to the application layer. Today, all students are active users of Internet applications and starting to learn computer networking by looking at bits is not very motivating. Starting from [KuroseRoss09]_, many textbooks and teachers have chosen a top-down approach. This approach starts from the applications such as email and web that students already know and explores the different layers starting from the application layer. This approach works pretty well with today's students.

.. sidebar:: Top-down versus bottom-up

   The traditional bottom-up approach could be in fact considered as an engineering approach since it starts from the simple network that allows to exchange bits and explains how to combine different protocols and mechanisms to build the most complex applications. The top-down approach could on the other hand be considered as a scientific approach. Like biologists, it starts from an existing (man-built) system and explores it layer by layer.

Besides the top-down versus bottom-up organisation, computer networking books can aim at having an in-depth coverage of a small number of topics or at having a limited coverage of a wide range of topics. Covering a wide range of topics is interesting for introductory courses or for students who do not need a detailed knowledge of computer networks. It allows the students to learn a `little about everything` and then start from this basic knowledge later if they need to understand computer networking in more details. This books chose to cover in details a smaller number of topics than other textbooks. This is motivated by the fact that computer networks are often pushed to their limits and understanding the details of the main networking protocols is important to be able to fully grasp how a network behaves or extend it to provide innovative services. As the popular quote says, `the devil is in the details` and this quote is even more important in computer networking where the change of a single bit may have huge consequences. In computer networks, understanding *all* the details is, unfortunately for some students, sometimes necessary.

The overall objective of the book is to explain the principles and the protocols used in computer networks and also provide the students with some intuition about the important practical issues that arise often. The course follows a hybrid problem-based learning (:term:`PBL`) approach. During each week, the students follow a 2 hours theoretical course that describes the principles and some of the protocols. They also receive a set of small problems that they need to solve in groups. These problems are designed to reinforce the student's knowledge but also to explore the practical problems that arise in real networks by allowing the students to perform experiments by writing prototype networking code. Most of the prototype code will be written in python_ by using the scapy_ packet injection/manipulation framework that will be described later.

.. sidebar:: Why open source ?

   This book is being developed as an open-source book under a creative commons licence. This choice an an open-source license is motivated by two reasons. The first is that we hope that this will allow many students to use the book to learn computer networks and maybe other teachers will reuse, adapt and improve it. The second reason is that that the computer networking community heavily relies on open source implementations. In fact, there are high-quality and widely used open-source implementations for most of the protocols described in this book. This includes the TCP/IP implementations that are part of linux_, freebsd_ or the uIP_ stack running on 8bits controllers, but also servers such as bind_, unbound_, apache_ or sendmail_ and implementations of routing protocols such as xorp_ or quagga_ . Furthermore, the official specifications of most of the protocols that are described in this book have been developed within the IETF_ in an almost open-source manner. The IETF publishes its protocols specifications in the publicly available RFC_ and new proposals are described in `Internet drafts`_.  

The book is organised as follows. We first describe the application layer. Given the large number of Internet-based applications, it is of course impossible to cover them all in details. Instead we focus on three types of Internet-based applications. We first study the Domain Name System (DNS) and then explain some of the protocols involved in the exchange of electronic mail. The discussion of the application layer ends with a description of the key protocols of the world wide web and a brief explanation of peer-to-peer applications. All these applications rely on the transport layer. This is a key layer in today's networks as it contains all the mechanisms that are necessary to provide a reliable delivery of data over an unreliable network. We cover the transport layer by first developing a simple reliable transport layer protocol and then explain the details of the TCP and UDP protocols used in TCP/IP networks. After the transport layer, we focus on the network layer. This is also a very important layer as it is responsible for the delivery of packets from any source to any destination through intermediate routers. In the network layer, we describe the two possible organisations of the network layer and the routing protocols based on link-state and distance vectors. Then we explain in details the IPv4, IPv6, RIP, OSPF and BGP protocols that are actually used in today's Internet. The last part of the course is devoted to the datalink layer. More precisely, our focus in this part is on the Local area networks. We first describe the Medium Access Control mechanisms that allow multiple hosts to share a given transmission medium. We consider both opportunistic and deterministic techniques. We explain in details two types of LANs that are important from a deployment viewpoint today : Ethernet and WiFi. 


.. rubric:: Footnotes


.. [#open] open in ISO terms was in contrast with the proprietary protocol suites whose specification was not always available. The US government even mandated the usage of the OSI protocols (see :rfc:`1169`), but this was not sufficient to encourage all users to switch to the OSI protocol suite that was considered by many as too complex compared to other protocol suites.


.. [#unicode] There is now a rough consensus on using more and more the Unicode_ character format. Unicode can represent more than 100,000 different characters from the known written languages on Earth. Maybe one day all computers will only use Unicode to represent all their stored characters and Unicode could become the standard format to exchange characters, but we are not yet at this stage today. Even then, it would be necessary to decide which version of Unicode to use.

.. [#fiso-tcp] An interesting historical discussion of the OSI-TCP/IP debate may be found in [Russel06]_

.. [#fsynchro] Having perfectly synchronised clocks running at a high frequency is very difficult in practice. However, some physical layers introduce a feedback loop that allows the receiver's clock to synchronise itself automatically to the sender's clock. However, not all physical layers include this kind of synchronisation. 

.. include:: ../links.rst


