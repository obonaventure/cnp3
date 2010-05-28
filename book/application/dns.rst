.. _DNS:

The Domain Name System
======================

In the early days of the Internet, there were only few hosts (mainly minicomputers) connected to the network. The most popular applications were remote login and file transfer. In 1983, there were already five hundred hosts attached to the network. Each of these hosts was identified by a unique IPv4 address. Forcing human users to remember the IPv4 addresses of the remote hosts that they want to use was not user-friendly. Human users prefer to remember names and us them when needed. Programming languages use named variables that allow programmers to ignore their exact location in memory. Networked applications must also be able to use names instead of IP addresses. 

A first solution to allow applications to use names was the :term:`hosts.txt` file. This file contained the mapping between the name of each Internet host and its associated IPv4 address(s) [#fhosts]_. It was maintained by SRI_ International that coordinated the Network Information Center. When a new host was connected to the network, the system administrator had to register the name of the host and its IP address at the NIC. The NIC updated the :term:`hosts.txt` file on its server. All Internet hosts retrieved regularly the updated :term:`hosts.txt` from the server maintained by SRI_. This file was stored at a well-known location on each Internet host :rfc:`952` and networked applications could use it to find the IP address corresponding to a name. 

The :term:`hosts.txt` file can be used when there a up to a few hundred hosts on the network. However, it is clearly not suitable for a network containing thousands or millions of hosts. A key issue in a large network is to define a suitable naming scheme. The ARPANet initially used a flat naming space, i.e. each host was assigned a unique name that usually contained the name of the institution and a suffix to identify the host inside the institution. On the ARPANet few institutions had several hosts connected to the network. 

However, the limitations of a flat naming scheme became clear before the end of the ARPANet and :rfc:`819` proposed a hierarchical naming scheme. While :rfc:`819` discussed the possibility of organising the names as a directed graph, the Internet opted eventually for a tree containing all names. In this tree, the top-level domains are those that are directly attached to the root. The first top-level domain was `.arpa` [#fdnstimeline]_. In 1984, the `.gov`, `.edu`, `.com`, `.mil` and `.org` generic top-level domain names were added and :rfc:`1032` proposed the utilisation of the two letters ISO-3166_ country codes as top-level domain names. Since ISO-3166_ defines a two letters code for each country recognised by the United Nations, this allowed all countries to automatically have a top-level domain. These domains include `.be` for Belgium, `.fr` for France, `.us` for the USA or `.tv` for Tuvalu, a group of small islands in the Pacific and `.tm` for Turkmenistan. Recently, :term:`ICANN` added a dozen of generic top-level domains that are not related to a country and the `.cat` top-level domain has been registered for the Catalonia region in Spain. There are ongoing discussions within :term:`ICANN` to increase the number of top-level domains.

Each top-level domain is managed by an organisation that decides how sub-domain names can be registered. Most top-level domain names use first-come first served, an allow anyone to register domain names, but there are some exceptions. For example, `.gov` is reserved for the US government. 

.. figure:: png/app-fig-007-c.png
   :align: center
   :scale: 50 

   The tree of domain names

:rfc:`1035` clarified the definition of the fully qualified domain names by using the following :term:`BNF` :: 

 <domain> ::= <subdomain> | " "
 <subdomain> ::= <label> | <subdomain> "." <label>
 <label> ::= <letter> [ [ <ldh-str> ] <let-dig> ]
 <ldh-str> ::= <let-dig-hyp> | <let-dig-hyp> <ldh-str>
 <let-dig-hyp> ::= <let-dig> | "-"
 <let-dig> ::= <letter> | <digit>
 <letter> ::= any one of the 52 alphabetic characters A through Z in upper case and a through z in lower case
 <digit> ::= any one of the ten digits 0 through 9

This grammar speficies that a domain name is an ordered list of labels separated by the dot (`.`) character. Each label can contain letters, numbers and the hyphen character (`-`) but must start with a letter [#fidn]_. Fully qualified domain names are read from left to right. The first label is a hostname or a domain name followed by the hierarchy of domains and ending with the root implicitly at the right. The top-level domain name must be one of the registered TLDs [#ftld]_. For example, in the above figure, `www.whitehouse.gov` corresponds to a host named `www` inside the `whitehouse` domain that belongs to the `gov` top-level domain. `info.ucl.ac.be` corresponds to the `info` domain inside the `ucl` domain that is included in the `ac` sub-domain of the `be` top-level domain.

This hierarchical naming scheme is a key component of the Domain Name System (DNS). The DNS is a distributed database that contains mappings between fully qualified domain names and IP addresses. The DNS uses the client-server model. The clients are hosts that need to retrieve the mapping for a given name. Each :term:`nameserver` stores part of the distributed database and answer to the queries sent by the client. There is at least one :term:`nameserver` that is responsible for each domain. In the figure below, domains are represented by circles and there are three hosts inside domain `dom` and three hosts inside domain `a.sdom1.dom`. 

.. figure:: png/app-fig-006-c.png
   :align: center
   :scale: 50 

   A simple tree of domain names

A :term:`nameserver` that is responsible for domain `dom` can directly answer the following queries :
 
 - the IP address of any host residing directly inside domain `dom` (e.g. `h2.dom` in the figure above)
 - the DNS server(s) that are responsible for any direct sub-domain of domain `dom` (i.e. `sdom1.dom` and `sdom2.dom` in the figure above, but not `z.sdom1.dom`)

To retrieve the mapping for host `h2.dom`, a client sends its query to the name server that is responsible for domain `.dom`. The name server directly answers the query. To retrieve a mapping for `h3.a.sdom1.dom` a DNS client first sends a query to the name server that is responsible for the `.dom` domain. This nameserver returns the nameserver that is responsible for the `sdom1.dom` domain. This nameserver can now be contacted to obtain the nameserver that is responsible for the `a.sdom1.dom` domain. This nameserver can be contacted to retrieve the mapping for the `h3.a.sdom1.dom` name. Thanks to this organisation of the nameservers, it is possible for a DNS client to obtain the mapping of any host inside the `.dom` domain or any of its subdomains. To ensure that any DNS client will be able to resolve any fully qualified domain name, there are special nameservers that are responsible for the root of the domain name hierarchy. These nameservers are called :term:`root nameserver`. There are currently about a dozen root nameservers [#fdozen]_.   

Each root nameserver maintains the list [#froot]_ of all the nameservers that are responsible for each of the top-level domain names and their IP addresses [#frootv6]_. All root nameservers are synchronised and provide the same answers. By querying any of the root nameservers, a DNS client can obtain the nameserver that is responsible for any top-level-domain name. From this nameserver, it is possible to resolve any domain, ... 

To be able to contact the root nameservers, each DNS client must know their IP addresses. This implies, that DNS clients must maintain an up-to-date list of the IP addresses of the root nameservers [#fnamed.root]_. Without this list, it is impossible to contact the root nameservers. Forcing all Internet hosts to maintain the most recent version of this list would be difficult from an operational viewpoint. To solve this problem, the designers of the DNS introduced a special type of DNS server : the DNS resolvers. A :term:`resolver` is a server that provides name resolution service for a set of clients. A network usually contains a few resolvers. Each host in these networks is configured to send all its DNS queries via one of its local resolvers. These queries are called `recursive queries` as the :term:`resolver` must recurse through the hierarchy of nameservers to find the `answer`. 

DNS resolvers have several advantages over letting each Internet host query directly nameservers. First, regular Internet hosts do not need to maintain the up-to-date list of the IP addresses of the root servers. Second, regular Internet hosts do not need to send queries to nameservers all over the Internet. Furthermore, as a DNS resolver serves a large number of hosts, it can cache the received answers. This allows the resolver to quickly return answers for popular DNS queries and reduces the load on all DNS servers.  

The last component of the Domain Name System is the DNS protocol. The DNS protocol runs both above the datagram service and the bytestream service. In practice, the datagram service is used when short queries and responses are exchanged and the bytestream is used when longer responses are expected. In this section, we will only discuss the utilisation of the DNS protocol above the datagram service.

DNS messages are composed of five parts that are named sections in :rfc:`1035`. The first three sections are mandatory and the last two are optional. The first section of a DNS message is its `Header`. It contains information about the type of message and the content of the other sections. The second section contains the `Question` sent to the name server or resolver. The third section contains the `Answer` to the `Question`. When a client sends a DNS query, the `Answer` section is empty. The fourth section, named `Authority`, contains information the servers that can provide authoritative answers if required. The last section contains addition information that was not requested in the question.

The header of DNS messages is composed of 12 bytes and its structure is shown in the figure below.

::

                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

The `ID` (identifier) is a 16-bits value chosen by the client. When a client sends a question to a DNS server, it remembers the question and its identifier. When a server returns an answer, it returns in the `ID` field the identifier chosen by the client. Thanks to this identifier, the client can match the received answer with the question that it sent. 

.. dns attacks http://www.cs.columbia.edu/~smb/papers/dnshack.ps
.. http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html
.. http://www.secureworks.com/research/articles/dns-cache-poisoning

The `QR` flag is set to `0` in DNS queries and `1` in DNS answers. The `Opcode` is used to specify the type of query. One utilisation of this field is to distinguish between a :term:`standard query` in which a client sends a `name` and the server returns the corresponding `address` and an :term:`inverse query` in which the client sends an `address` and the server returns the corresponding `name`. 

The `AA` bit is set when the server that sent the response is an `authority` for the domain name found in the question section. In the original DNS deployments, two types of servers were considered : `authoritative` servers and `non-authoritative` servers. The `authoritative` servers are managed by the system administrators that are responsible for a given domain. They always store the most recent information about a domain. `Non-authoritative` servers on the other are not directly managed by the owners of a domain. They may thus provide answers that are out of date. From a security viewpoint, the `authoritative` bit is not an indication about the validity of an answer. Securing the Domain Name Systems is a complex problem that was only addressed satisfactorily recently by the utilisation of cryptographic signatures in the DNSSEC extensions to DNS described in :rfc:`4033`. These extensions are outside the scope of this chapter and will be discussed later. 

The `RD` (recursion desired) bit is set by a client when it sends a query to a resolver. Such a query is said to be `recursive`. In the past, all resolvers were configured to perform recursive queries on behalf of any Internet host. However, this exposes the resolvers to several security risks. The simplest one is that the resolver could become overloaded by having too many recursive queries to process. As of this writing, most resolvers [#f8888]_ only allow recursive queries from clients belonging to their company or network and discard all other recursive queries. The `RA` bit indicates whether the server supports recursion. The `RCODE` is used to distinguish between different types of errors. See :rfc:`1035`
for addition details. The last four field indicate the size of the `Question`, `Answer`, `Authority` and `Additional` sections of the DNS message.


The last four sections of the DNS message contain `Resource Records`. 


All RRs have the same top level format shown below :

::

                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                                               /
    /                      NAME                     /
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     CLASS                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TTL                      |
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                   RDLENGTH                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--|
    /                     RDATA                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

In a `Resource Record` (`RR`), the `Name` indicates the name of the node to which this resource record pertains. The two bytes `Type` field indicate the type of resource record. The `Class` field was used to support the utilisation of the DNS in other environment than the Internet. 

The `TTL` field indicates the lifetime of the `Resource Record` in seconds. This field is set by the server that returns an answer and indicates for how long a client or a resolver can store the `Resource Record` inside its cache. A long `TTL` indicates a stable `RR`. Some companies use short `TTL` values for mobile hosts and also when load must be spread among several servers.

The `RDLength` field is the size of the `RData` field that contains the information of the type specified in the `Type` field.

Several types of DNS RR are used in practice. The `A` type is used to encode the IPv4 address that corresponds to the specified name. The `AAAA` type is used to encode the IPv6 address that corresponds to the specified name. A `NS` record contains the name of the DNS server that is responsible for a given domain. `CNAME` (or canonical names) are used to define aliases. For example `www.example.com` Could be a `CNAME` for `pc12.example.com` that is the actual name of the server on which the web server for `www.example.com` runs. 

.. sidebar:: Reverse DNS and in-addr.arpa

 The DNS is mainly used to find the IP address that corresponds to a given name. However, it is sometimes useful to obtain the name that corresponds to an IP address. This done by using the `PTR` (`pointer`) `RR`. The `RData` part of a `PTR` `RR` contains the name while the `Name` part of the `RR` contains the IP address encoded in the `in-addr.arpa` domain. IPv4 addresses are encoded in the `in-addr.arpa` by reversing the four digits that compose the dotted decimal representation of the address. For example, consider IPv4 address `192.0.2.11`. The hostname associated to this address can be found by requesting the `PTR` `RR` that corresponds to `11.2.0.192.in-addr.arpa`. A similar solution is used to support IPv6 addresses, see :rfc:`3596`.

