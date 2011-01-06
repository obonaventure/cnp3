.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

.. index:: RIP, Routing Information Protocol

RIP
---

The Routing Information Protocol (RIP) is the simplest routing protocol that was standardised for the TCP/IP protocol suite. RIP is defined in :rfc:`2453`. Additional information about RIP may be found in [Malkin1999]_

RIP routers periodically exchange RIP messages. The format of these messages is show below. A RIP message is sent inside a UDP segment whose destination port is set to `521`. A RIP message contains several fields. The `Cmd` field indicates whether the RIP message is a request or a response. Routers send one of more RIP response messages every 30 seconds. These messages contain the distance vectors that summarize the router's routing table. The RIP requests messages can be used by routers or hosts to query other routers about the content of their routing table. A typical usage is when a router boots and wants to receive quickly the RIP responses from its neighbours to compute its own routing table. The current version of RIP is version 2 defined in :rfc:`2453` for IPv4 and :rfc:`2080` for IPv6. 

::

    0                   1                   2                   3 
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   | Command (1)   | Version (1)   |            unused             |
   +---------------+---------------+-------------------------------+
   |             0xFFFF            |    Authentication Type (2)    |
   +-------------------------------+-------------------------------+
   ~                       Authentication (16)                     ~
   +---------------------------------------------------------------+
   ~                     Up to 20 Route Entries                    ~
   +---------------------------------------------------------------+

   RIP message format


The RIP header contains an authentication field. This authentication can be used by network administrators to ensure that only the RIP messages sent by the routers that they manage are used to build the routing tables. :rfc:`2453` only supports a basic authentication scheme where all routers are configured with the same password and include this password in all RIP messages. This is not very secure since an attacker can know the password by capturing a single RIP message. However, this password can protect against configuration errors. Stronger authentication schemes are described in :rfc:`2082` and :rfc:`4822`, but the details of these mechanisms are outside the scope of this section.

Each RIP message contains a set of route entries. Each route entry is encoded as a 20 bytes field whose format is shown below. RIP was designed initially to be suitable for different network layer protocols. Some implementations of RIP were used in XNS or IPX networks. The first field of the RIP route entry is the `Address Family Identifier` (`AFI`). This identifier indicates the type of address found in the route entry [#fafi]_. IPv4 uses `AFI=1`. The other important fields of the route entry are the IPv4 prefix, the netmask that indicates the length of the subnet identifier and is encoded as a 32 bits netmask and the metric. Although the metric is encoded as a 32 bits field, the maximum RIP metric is `15` (for RIP, :math:`16=\infty`)

::

    0                   1                   2                   3 3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   | Address Family Identifier (2) |        Route Tag (2)          |
   +-------------------------------+-------------------------------+
   |                         IP Address (4)                        |
   +---------------------------------------------------------------+
   |                         Subnet Mask (4)                       |
   +---------------------------------------------------------------+
   |                         Next Hop (4)                          |
   +---------------------------------------------------------------+
   |                         Metric (4)                            |
   +---------------------------------------------------------------+

   Format of the RIP IPv4 route entries (:rfc:`2453`)

With a 20 bytes route entry, it was difficult to use the same format as above to support IPv6. Instead of defining a variable length route entry format, the designers of :rfc:`2080` defined a new format that does not include an `AFI` field. The format of the route entries used by :rfc:`2080` is shown below. `Plen` is the length of the subnet identifier in bits and the metric is encoded as one byte. The maximum metric is still `15`.

::

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                                                               |
      ~                        IPv6 prefix (16)                       ~
      |                                                               |
      +---------------------------------------------------------------+
      |         route tag (2)         | prefix len (1)|  metric (1)   |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   
      Format of the RIP IPv6 route entries

.. note:: A note on timers

 The first RIP implementations sent their distance vector exactly every 30 seconds. This worked well in most networks, but some researchers noticed that routers were sometimes overloaded because they were processing too many distance vectors at the same time [FJ1994]_. They collected packet traces in these networks and found that after some time the routers' timers became synchronised, i.e. almost all routers were sending their distance vectors at almost the same time. This synchronisation of the transmission times of the distance vectors caused an overload on the routers' CPU but also increased the convergence time of the protocol in some cases. This was mainly due to the fact that all routers set their timers to the same expiration time after having processed the received distance vectors. `Sally Floyd`_ and `Van Jacobson`_ proposed in [FJ1994]_ a simple solution to solve this synchronisation problem. Instead of advertising their distance vector exactly after 30 seconds, a router should send its next distance vector after a delay chosen randomly in the [15,45] interval :rfc:`2080`. This randomisation of the delays prevents the synchronisations that occur with a fixed delay and is today a recommended practice for protocol designers. 


.. rubric:: Footnotes


.. [#fafi] The Address Family Identifiers are maintained by IANA at http://www.iana.org/assignments/address-family-numbers/
