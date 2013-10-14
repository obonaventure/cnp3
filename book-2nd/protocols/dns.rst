.. Copyright |copy| 2013 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. _DNS:

The Domain Name System
======================

We have already explained the main principles that underlie the utilisation of names on the Internet and their mapping to addresses.
The last component of the Domain Name System is the DNS protocol. The DNS protocol runs above both the datagram service and the bytestream services. In practice, the datagram service is used when short queries and responses are exchanged, and the bytestream service is used when longer responses are expected. In this section, we will only discuss the utilisation of the DNS protocol above the datagram service. This is the most frequent utilisation of the DNS.

.. index:: DNS message format

DNS messages are composed of five parts that are named sections in :rfc:`1035`. The first three sections are mandatory and the last two sections are optional. The first section of a DNS message is its `Header`. It contains information about the type of message and the content of the other sections. The second section contains the `Question` sent to the name server or resolver. The third section contains the `Answer` to the `Question`. When a client sends a DNS query, the `Answer` section is empty. The fourth section, named `Authority`, contains information about the servers that can provide an authoritative answer if required. The last section contains additional information that is supplied by the resolver or server but was not requested in the question.

The header of DNS messages is composed of 12 bytes and its structure is shown in the figure below.

.. figure:: /../book/application/pkt/dnsheader.png
   :align: center
   :scale: 100

   DNS header

The `ID` (identifier) is a 16-bits random value chosen by the client. When a client sends a question to a DNS server, it remembers the question and its identifier. When a server returns an answer, it returns in the `ID` field the identifier chosen by the client. Thanks to this identifier, the client can match the received answer with the question that it sent. 

.. dns attacks http://www.cs.columbia.edu/~smb/papers/dnshack.ps
.. http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html
.. http://www.secureworks.com/research/articles/dns-cache-poisoning

The `QR` flag is set to `0` in DNS queries and `1` in DNS answers. The
`Opcode` is used to specify the type of query. For instance, a :term:`standard query` is when a client sends a `name` and the server returns the corresponding `data` and an update request is when the client sends a `name` and new `data` and the server then updates its database.

The `AA` bit is set when the server that sent the response has `authority` for the domain name found in the question section. In the original DNS deployments, two types of servers were considered : `authoritative` servers and `non-authoritative` servers. The `authoritative` servers are managed by the system administrators responsible for a given domain. They always store the most recent information about a domain. `Non-authoritative` servers are servers or resolvers that store DNS information about external domains without being managed by the owners of a domain. They may thus provide answers that are out of date. From a security point of view, the `authoritative` bit is not an absolute indication about the validity of an answer. Securing the Domain Name System is a complex problem that was only addressed satisfactorily recently by the utilisation of cryptographic signatures in the DNSSEC extensions to DNS described in :rfc:`4033`. However, these extensions are outside the scope of this chapter. 

The `RD` (recursion desired) bit is set by a client when it sends a query to a resolver. Such a query is said to be `recursive` because the resolver will recurse through the DNS hierarchy to retrieve the answer on behalf of the client. In the past, all resolvers were configured to perform recursive queries on behalf of any Internet host. However, this exposes the resolvers to several security risks. The simplest one is that the resolver could become overloaded by having too many recursive queries to process. As of this writing, most resolvers [#f8888]_ only allow recursive queries from clients belonging to their company or network and discard all other recursive queries. The `RA` bit indicates whether the server supports recursion. The `RCODE` is used to distinguish between different types of errors. See :rfc:`1035`
for additional details. The last four fields indicate the size of the `Question`, `Answer`, `Authority` and `Additional` sections of the DNS message.

The last four sections of the DNS message contain `Resource Records` (RR).  All RRs have the same top level format shown in the figure below. 

.. figure:: /../book/application/pkt/dnsrr.png
   :align: center
   :scale: 100

   DNS Resource Records

In a `Resource Record` (`RR`), the `Name` indicates the name of the node to which this resource record pertains. The two bytes `Type` field indicate the type of resource record. The `Class` field was used to support the utilisation of the DNS in other environments than the Internet. 

The `TTL` field indicates the lifetime of the `Resource Record` in seconds. This field is set by the server that returns an answer and indicates for how long a client or a resolver can store the `Resource Record` inside its cache. A long `TTL` indicates a stable `RR`. Some companies use short `TTL` values for mobile hosts and also for popular servers. For example, a web hosting company that wants to spread the load over a pool of hundred servers can configure its nameservers to return different answers to different clients. If each answer has a small `TTL`, the clients will be forced to send DNS queries regularly. The nameserver will reply to these queries by supplying the address of the less loaded server.

The `RDLength` field is the length of the `RData` field that contains the information of the type specified in the `Type` field.

Several types of DNS RR are used in practice. The `A` type is used to encode the IPv4 address that corresponds to the specified name. The `AAAA` type is used to encode the IPv6 address that corresponds to the specified name. A `NS` record contains the name of the DNS server that is responsible for a given domain. For example, a query for the `AAAA` record associated to the `www.ietf.org` name returns the following answer.

.. figure:: /protocols/pkt/dns6-www-ietf-org.png
   :align: center

   Query for the `AAAA` record of `www.ietf.org` 

This answer contains several pieces of information. First, the name `www.ietf.org` is associated to IP address `2001:1890:123a::1:1e`. Second, the `ietf.org` domain is managed by six different nameservers. Five of these nameservers are reachable via IPv4 and IPv6. 

`CNAME` (or canonical names) are used to define aliases. For example `www.example.com` could be a `CNAME` for `pc12.example.com` that is the actual name of the server on which the web server for `www.example.com` runs. 

.. note:: Reverse DNS 

 The DNS is mainly used to find the address that correspond to a given name. However, it is sometimes useful to obtain the name that corresponds to an IP address. This done by using the `PTR` (`pointer`) `RR`. The `RData` part of a `PTR` `RR` contains the name while the `Name` part of the `RR` contains the IP address encoded in the `in-addr.arpa` domain. IPv4 addresses are encoded in the `in-addr.arpa` by reversing the four digits that compose the dotted decimal representation of the address. For example, consider IPv4 address `192.0.2.11`. The hostname associated to this address can be found by requesting the `PTR` `RR` that corresponds to `11.2.0.192.in-addr.arpa`.
 A similar solution is used to support IPv6 addresses :rfc:`3596`, but slightly more complex given the length of the IPv6 addresses. For example, consider IPv6 address `2001:1890:123a::1:1e`. To obtain the name that corresponds to this address, we need first to convert it in a reverse dotted decimal notation : `e.1.0.0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.a.3.2.1.0.9.8.1.1.0.0.2`. In this notation, each character between dots corresponds to one nibble, i.e. four bits. The low-order byte (`e`) appears first and the high order (`2`) last. To obtain the name that corresponds to this address, one needs to append the `ip6.arpa` domain name and query for `e.1.0.0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.a.3.2.1.0.9.8.1.1.0.0.2.ip6.arpa`. In practice, tools and libraries do the conversion automatically and the user does not need to worry about it.


An important point to note regarding the Domain Name System is its extensibility. Thanks to the `Type` and `RDLength` fields, the format of the Resource Records can easily be extended. Furthermore, a DNS implementation that receives a new Resource Record that it does not understand can ignore the record while still being able to process the other parts of the message. This allows, for example, a DNS server that only supports IPv6 to ignore the IPv4 addresses listed in the DNS reply for `www.ietf.org` while still being able to correctly parse the Resource Records that it understands. This extensibility allowed the Domain Name System to evolve over the years while still preserving the backward compatibility with already deployed DNS implementations.


.. rubric:: Footnotes


.. [#f8888] Some DNS resolvers allow any host to send queries. Google operates a `public DNS resolver <https://developers.google.com/speed/public-dns/docs/using>`_ at addresses `2001:4860:4860::8888` and `2001:4860:4860::8844` 


.. include:: /links.rst
