=====================
The Application Layer
=====================

The Application Layer is the most important and most visible layer in computer networks. Applications reside in this layer and human users interact via those applications through the network. 

In this chapter, we first briefly describe the main principles of the application layer and focus on the two most important models :  the client-server model and the peer-to-peer models. Then, we review in details two families of protocols that have proved to be very useful in networks such as the Internet : electronic mail and the protocols that allow to access information on the world wide web. We also describe the Domain Name System that allows humans to use user-friendly names while the hosts use IP addresses. 

Principles
##########

The are two important models to organise a networked application. The first and oldest model is the client-server model. In this model, a server provides services to clients that exchange information with it. This model is highly assymetrical : clients send requests and servers perform actions and provide responses. It is illsutrated in the figure below.


.. figure:: fig/app-fig-001-c.png
   :align: center
   :scale: 50 

   The client-server model

The client-server model was the first model to be used to develop networked applications. This model comes naturally from the mainframes and minicomputers that were the only networked computers used until the 1980s. A minicomputer_ is a multi-user system that was used by tens or more users at the same time. Each user was interacting via the minicomputer by using a terminal. Those terminals, were mainly a screen, a keyboard and a cable connected to the minicomputer.

There are various types of servers and various types of clients. A web server provides information in response to the query sent by the client. A print server prints documents sent as queries by the client. An email server will forward towards their recipient the email messages sent as queries while a music server will deliver the music requested by the client. From the viewpoint of the application developper, the client and the server applications directly exchange messages (the horizontal arrows in the above figure), but in practice these messages are exchanged thanks to the underlying protocols (the vertical arrows in the above figure). In this chapter, we focus on these horizontal exchanges of messages. 

Networked applications do not exchange random messages. To ensure that the server is able to understand the queries sent by the client and that the client is able to understand the responses sent by the server, they must agree on a set of syntactical and semantical rules that define the format of the messages that they exchange and their ordering. This set of rules is called an application-level `protocol`.

An `application-level protocol` is similar to a structured conversation between humans. Assume that Alice wants to know the current time but does not have a watch. If Bob passes closeby, the following conversation could take place :

 - Alice : `Hello`
 - Bob : `Hello`
 - Alice : `What time is it ?`
 - Bob : `11:55`
 - Alice : `Thank you`
 - Bob : `You're welcome`  

This conversation can succeed provided that both Alice and Bob speak the same language. If Alice meets Tchang who only speaks Chinese, she won't be able to ask him the current time. A conversation between humans can be more complex. For example, assume that Bob is a security guard who's duty is to only allow trusted secret agents to enter a meeting room. If all agents know a secret password, the conversation between Bob and Trudy could be as follows :

 - Bob : `What is the secret password ?`
 - Trudy : `1234`
 - Bob : `This is the correct password, you're welcome`
 
If Alice wants to enter the meeting room but does not know the password, her conversation could be as follows :

 - Bob : `What is the secret password ?`
 - Alice : `3.1415`
 - Bob : `This is not the correct password.`

Application-layer protocols can exchange two types of messages. Some protocols such as those used to support electronic mail exchange messages that are expressed as strings or lines of characters. As the transport layer allows hosts to exchange bytes, they need to agree on a common representation of the characters. The first and simplest method to encode characters is to use the :term:`ASCII` table. :rfc:`20` provides the ASCII table that is used by many protocols on the Internet. For example, the table defines the following binary representations :

 - `A` : `1000011b` 
 - `0` : `0110000b`
 - `z` : `1111010b`
 - `@` : `1000000b`
 - `space` : `0100000b`

In addition, the :term:`ASCII` table also defines several non-printable or control characters. These characters were designed to allow an application to control a printer or a terminal. The most common ones are `CR` and `LF` that are used to terminate a line or the `Bell` character that causes the terminal to emit a sound.

 - `carriage return` (`CR`) : `0001101b`
 - `line feed` (`LF`) : `0001010b`
 - `Bell`: `0000111b`

The :term:`ASCII` characters are encoded as a seven bits field, but transmitted as an eight-bits byte whose high order bit is set to `0`. Bytes are always transmitted starting from the high order or most significant bit.

Besides characters, some applications also need to exchange 16 bits and 32 bits fields such as IPv4 addresses. A naive solution would have been to send the 16- or 32-bits field as it was encoded in memory. Unfortunately, there are different methods to store 16- or 32-bits fields in memory. Some CPUs store the most significant byte of a 16-bits field in the first address of the field while others store the least significant byte at this location. When networked applications running on different CPUs exchange 16 bits fields, there are two possibilies to transfer them over the transport service :

  - send the most significant byte followed by the least significant byte
  - send the least significant byte followed by the most significant byte

The first possibility was named  `big-endian` in a note written by Cohen [Cohen1980]_ while the second was named `little-endian`. Vendors of CPUs that used `big-endian` in memory insisted on using `big-endian` encoding in networked applications while vendors of CPUs that used `little-endian` recommended the opposite. Several studies were written on the relative merits of each type of encoding, but the discussion became almost a religious issue [Cohen1980]_. Eventually, the Internet chose the `big-endian` encoding, i.e. multi-byte fields are always transmitted by sending the most significant byte first :rfc:`791` and refer to this encoding as the :term:`network-byte order`. Most librairies [#fhtonl]_ used to write networked applications contain functions to convert multibyte fields from memory to the network byte order and vice versa. 

Besides 16 and 32 bits words, some applications need to exchange that contain bit fields of various lengths. For example, a message may be composed of a 16 bits field followed by eight one bit flags, a 24 bits field and two 8 bits bytes. Internet protocol specifications will define such as message by using a representation such as the one below. In this representation, each line corresponds to 32 bits and the vertical lines are used to delineate fields. The numbers above the lines indicate the bit positions in the 32-bits word, with the high order bit at position `0`. 

::

    0                   1                   2                   3   
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |       First field  (16 bits)  |A|B|C|D|E|F|G|H|   Second      | 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |       field (24 bits)         |  First Byte   | Second Byte   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


The message mentionned above will be transmitted starting from the upper 32-bits word in network byte order. The first field is encoded in 16 bits. It is followed by eight one bit flags (`A-H`), a 24 bits field whose high order byte is shown in the first line and the two low order bytes appear in the second line and two one byte fields. This ascii representation is frequently used when defining binary protocols. We will use it for all the binary protocols that are discussed in this book.

We will discuss several examples of application-level protocols in this chapter.

.. introduce ipv4 and ipv6 addresses
.. mention names very early, they are important

The peer-to-peer model
======================

The peer-to-peer model 


The transport services
======================

Networked applications are built on top of the transport service. As explained in the previous chapter, there are two main types of transport services :

 - the `connectionless` or `datagram` service
 - the `connection-oriented` or `byte-stream` service

The connectionless service allows applications to easily exchange messages or Service Data Units. On the Internet, this service is provided by the UDP protocol  that will be explained in the next chapter. The connectionless transport service on the Internet is unreliable but is able to detect transmission errors. This implies that an application will not receive an SDU that has been modified by transmission errors. 

The connectionless transport service allows networked application to exchange messages. Several networked applications may be running at the same time on a given host. Each of these applications must be able to exchange SDUs with remote applications. To enable these exchanges of SDUs, each networked application running on a host is identified by the following information :

 - the `host` on which the application is running
 - the `port number` on which the application `listens` for SDUs

On the Internet, the `port number` is an integer and the `host` is identified by its network address. As we will explain in chapter `xx` there are two types of Internet Addresses :

 - `IP version 4` addresses that are 32 bits wide
 - `IP version 6` addresses that are 128 bits wide

IPv4 addresses are usually represented by using a dotted decimal representation where each decimal number corresponds to one byte of the address, e.g. 130.104.32.107. IPv6 addresses are usually represented as a set of hexadecimal numbers separated by by semicolons, e.g. 2001:6a8:3080:2:217:f2ff:fed6:65c0. Today, most Internet hosts have an IPv4 address. A small fraction of them also have an IPv6 address. In the future, we can expect that more and more hosts will have IPv6 addresses and that some of them will not have an IPv4 address anymore. A host that only has an IPv4 address cannot communicate with a host having only an IPv6 address. Another possibility to identify an Internet host is by using its `fully qualified domain name` (usually summarised as `name`). The figure below illustrates two that are using the datagram service provided by UDP on hosts with IPv4 addresses.


.. figure:: fig/app-fig-002-c.png
   :align: center
   :scale: 50 

   The connectionless or datagram service 

The second transport service is the connection-oriented service. On the Internet, this service is often called the `byte-stream service` as it creates a reliable byte stream between the two applications that are linked by a transport connection. As for the datagram service, the networked applications that are using the byte-stream service are identified by the host where they run and a port number. The hosts can be identified by an IPv4 address, an IPv6 address or a name. The figure below illustrates two applications that are using the byte-stream service provided by the TCP protocol on IPv6 hosts. The byte stream service provided by TCP is reliable and bidirectional. Some applications use SCTP instead of TCP for the byte-stream service.


.. figure:: fig/app-fig-003-c.png
   :align: center
   :scale: 50 

   The connection-oriented or byte-stream service 


Application-level protocols
###########################


Many protocols have been defined for networked applications. In this section, we describe some of the important applications that are used on the Internet. We first explain the domain name systems that enables hosts to be identified by human-friendly names instead of the IPv4 or IPv6 addresses that are used by the network. Then we describe the operation of electronic mail, one of the first killer applications on the global Internet and the main protocol used on world wide web. In the last section, we show how simple networked clients and servers can be written in python_ .


.. _DNS:

The Domain Name System
======================

In the early days of the Internet, there were only few hosts (mainly minicomputers) connected to the network. The most popular applications were remote login and file transfer. In 1983, there were already five hundred hosts attached to the network. Each of these hosts was identified by a unique IPv4 address. Forcing human users to remember the IPv4 addresses of the remote hosts that they want to use was not user-friendly. Human users prefer to remember names and us them when needed. Programming languages use named variables that allow programmers to ignore their exact location in memory. Networked applications must also be able to use names instead of IP addresses. 

A first solution to allow applications to use names was the :term:`hosts.txt` file. This file contained the mapping between the name of each Internet host and its associated IPv4 addresse(s) [#fhosts]_. It was maintained by SRI_ International that coordinated the Network Information Center. When a new host was connected to the network, the system administrator had to register the name of the host and its IP address at the NIC. The NIC updated the :term:`hosts.txt` file on its server. All Internet hosts retrieved regularly the updated :term:`hosts.txt` from the server maintained by SRI_. This file was stored at a well-known location on each Internet host :rfc:`952` and networked applications could use it to find the IP address corresponding to a name. 

The :term:`hosts.txt` file can be used when there a up to a few hundred hosts on the network. However, it is clearly not suitable for a network containing thousands or millions of hosts. A key issue in a large network is to define a suitable naming scheme. The ARPANet initially used a flat naming space, i.e. each host was assigned a unique name that usually contained the name of the institution and a suffix to identify the host inside the institution. On the ARPANet few institutions had several hosts connected to the network. 

However, the limitations of a flat naming scheme became clear before the end of the ARPANet and :rfc:`819` proposed a hierarchical naming scheme. While :rfc:`819` discussed the possibility of organising the names as a directed graph, the Internet opted eventually for a tree containing all names. In this tree, the top-level domains are those that are directly attached to the root. The first top-level domain was `.arpa` [#fdnstimeline]_. In 1984, the `.gov`, `.edu`, `.com`, `.mil` and `.org` generic top-level domain names were added and :rfc:`1032` proposed the utilisation of the two letters ISO-3166_ country codes as top-level domain names. Since ISO-3166_ defines a two letters code for each country recognised by the United Nations, this allowed all countries to automatically have a top-level domain. These domains include `.be` for Belgium, `.fr` for France, `.us` for the USA or `.tv` for Tuvalu, a group of small islands in the Pacific and `.tm` for Turkmenistan. Recently, :term:`ICANN` added a dozen of generic top-level domains that are not related to a country and the `.cat` top-level domain has been registered for the Catalonia region in Spain. There are ongoing discussions within :term:`ICANN` to increase the number of top-level domains.

Each top-level domain is managed by an organisation that decides how subdomain names can be registered. Most top-level domain names use first-come first served, an allow anyone to register domain names, but there are some exceptions. For example, `.gov` is reserved for the US government. 

.. figure:: fig/app-fig-007-c.png
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

This grammar speficies that a domain name is an ordered list of labels separated by the dot (`.`) character. Each label can contain letters, numbers and the hyphen character (`-`) but must start with a letter [#fidn]_. Fully qualified domain names are read from left to right. The first label is a hostname or a domain name followed by the hierarchy of domains and ending with the root implicitely at the right. The top-level domain name must be one of the registered TLDs [#ftld]_. For example, in the above figure, `www.whitehouse.gov` corresponds to a host named `www` inside the `whitehouse` domain that belongs to the `gov` top-level domain. `info.ucl.ac.be` corresponds to the `info` domain inside the `ucl` domain that is included in the `ac` subdomain of the `be` top-level domain.

This hierarchical naming scheme is a key component of the Domain Name System (DNS). The DNS is a distributed database that contains mappings between fully qualified domain names and IP addresses. The DNS uses the client-server model. The clients are hosts that need to retrieve the mapping for a given name. Each :term:`nameserver` stores part of the distributed database and answer to the queries sent by the client. There is at least one :term:`nameserver` that is responsible for each domain. In the figure below, domains are represented by circles and there are three hosts inside domain `dom` and three hosts inside domain `a.sdom1.dom`. 

.. figure:: fig/app-fig-006-c.png
   :align: center
   :scale: 50 

   A simple tree of domain names

A :term:`nameserver` that is reponsible for domain `dom` can directly answer the following queries :
 
 - the IP address of any host residing directly inside domain `dom` (e.g. `h2.dom` in the figure above)
 - the DNS server(s) that are responsible for any direct subdomain of domain `dom` (i.e. `sdom1.dom` and `sdom2.dom` in the figure above, but not `z.sdom1.dom`)

To retrieve the mapping for host `h2.dom`, a client sends its query to the name server that is reponsible for domain `.dom`. The name server directly answers the query. To retrieve a mapping for `h3.a.sdom1.dom` a DNS client first sends a query to the name server that is responsible for the `.dom` domain. This nameserver returns the nameserver that is responsible for the `sdom1.dom` domain. This nameserver can now be contacted to obtain the nameserver that is responsible for the `a.sdom1.dom` domain. This nameserver can be contacted to retrieve the mapping for the `h3.a.sdom1.dom` name. Thanks to this organisation of the nameservers, it is possible for a DNS client to obtain the mapping of any host inside the `.dom` domain or any of its subdomains. To ensure that any DNS client will be able to resolve any fully qualified domain name, there are special nameservers that are responsible for the root of the domain name hierarchy. These nameservers are called :term:`root nameserver`. There are currently about a dozen root nameservers [#fdozen]_.   

Each root nameserver maintains the list [#froot]_ of all the nameservers that are responsible for each of the top-level domain names and their IP addresses [#frootv6]_. All root nameservers are synchronised and provide the same answers. By querying any of the root nameservers, a DNS client can obtain the nameserver that is responsible for any top-level-domain name. From this nameserver, it is possible to resolve any domain, ... 

To be able to contact the root nameservers, each DNS client must know their IP addresses. This implies, that DNS clients must maintain an up-to-date list of the IP addresses of the root nameservers [#fnamed.root]_. Without this list, it is impossible to contact the root nameservers. Forcing all Internet hosts to maintain the most recent version of this list would be difficult from an operational viewpoint. To solve this problem, the designers of the DNS introduced a special type of DNS server : the DNS resolvers. A :term:`resolver` is a server that provides name resolution service for a set of clients. A network usually contains a few resolvers. Each host in these networks is configured to send all its DNS queries via one of its local resolvers. These queries are called `recursive queries` as the :term:`resolver` must recurse through the hierarchy of nameservers to find the `answer`. 

DNS resolvers have several advantages over letting each Internet host query directly nameservers. First, regular Internet hosts do not need to maintain the up-to-date list of the IP addresses of the root servers. Second, regular Internet hosts do not need to send queries to nameservers all over the Internet. Furthermore, as a DNS resolver serves a large number of hosts, it can cache the received answers. This allows the resolver to quickly return answers for popular DNS queries and reduces the load on all DNS servers.  

The last component of the Domain Name System is the DNS protocol. The DNS protocol runs both above the datagram service and the bytestream service. In practice, the datagram service is used when short queries and responses are exchanged and the bytestream is used when longer responses are expected. In this section, we will only discuss the utilisation of the DNS protocol above the datagram service.

DNS messages are composed of five parts that are named sections in :rfc:`1035`. The first three sections are mandatory and the last two are optionnal. The first section of a DNS message is its `Header`. It contains information about the type of message and the content of the other sections. The second section contains the `Question` sent to the name server or resolver. The third section contains the `Answer` to the `Question`. When a client sends a DNS query, the `Answer` section is empty. The fourth section, named `Authority`, contains information the servers that can provide authoritative answers if required. The last section contains addition information that was not requested in the question.

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

The `AA` bit is set when the server that sent the response is an `authority` for the domain name found in the question section. In the orginal DNS deployments, two types of servers were considered : `authoritative` servers and `non-authoritative` servers. The `authoritative` servers are managed by the system administrators that are responsible for a given domain. They always store the most recent information about a domain. `Non-authoritative` servers on the other are not directly managed by the owners of a domain. They may thus provide answers that are out of date. From a security viewpoint, the `authoritative` bit is not an indication about the validity of an answer. Securing the Domain Name Systems is a complex problem that was only addressed satisfactorily recently by the utilisation of cryptographic signatures in the DNSSEC extensions to DNS described in :rfc:`4033`. These extensions are outside the scope of this chapter and will be discussed later. 

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

.. _Email:

Electronic mail
===============

Electronic mail or email is a very popular application in computer networks such as the Internet. Email `appeared <http://openmap.bbn.com/~tomlinso/ray/firstemailframe.html>`_ in the early 1970s. It allows users to exchange messages. Initially, Email was mainly used to exchange short messages, but over the years its usage has grown. Email is now used to exchange very long messages but also messages composed of several parts as we will see later. 

Before looking at the details of Internet email, let us consider a simple scenario illustrated in the figure below where Alice sends an email to Bob. Alice prepares her email by using one of the available `email clients <http://en.wikipedia.org/wiki/Comparison_of_email_clients>`_ and sends it to her email server. Alice's `email server <http://en.wikipedia.org/wiki/Comparison_of_mail_servers>`_ extracts Bob's address from the email and delivers the message to Bob's server. Bob retrieves Alice's message on his server and reads it by using his favourite email client or through a webmail. 

.. figure:: fig/app-fig-009-c.png
   :align: center
   :scale: 50 

   Architecture of the Internet email 

In practice, an email system is composed of four components :

 - a precise format to encode email messages
 - protocols that allow to exchange email messages
 - client software that allows users to easily create and read email messages
 - software that allows servers to efficiently exchange email messages

We first discuss the format of email messages and then the protocols that are used on today's Internet to exchange and retrieve emails. Other email systems have been developed in the past, but today most email solutions have migrated to the Internet email. Information about the software that is used to compose and deliver emails may be found on wikipedia_ for both `email clients <http://en.wikipedia.org/wiki/Comparison_of_email_clients>`_ and `email servers <http://en.wikipedia.org/wiki/Comparison_of_mail_servers>`_.

Email messages, like postal mail, are composed of two parts :

 - the `header` that contains control information that is used by the email servers to deliver the email message to its recipient
 - the `body` that contains the message itself.  

Email messages are entirely composed of lines of ASCII characters. Each line can contain up to 998 characters and is terminated by the `CR` and `LF` control characters. The lines that compose the `header` appear before the message `body`. An empty line, containing only the `CR` and `LF` characters, marks the end of the `header`. This is illustrated in the figure below.

.. abnf crocker : :rfc:`5234`

.. figure:: fig/app-fig-010-c.png
   :align: center
   :scale: 50 

   The structure of email messages

The email header contains several lines that all begin by a keyword followed by colon and additional information. The format of email messages and the different types of header lines are defined in :rfc:`5322`. Two of these header lines are mandatory and must appear in all email messages :

 - The sender address. This header line starts with `From:`. It contains the (optional) name of the sender followed by its address between `<` and `>`. Email addresses are always composed of a username followed by the `@` sign and a domain name.
 - The date. This header line starts with `Date:`. :rfc:`5322` precisely defines the format used to encode a date.


The `Subject:` header line allows the sender to indicate the topic discussed in the email. Three types of header lines can be used to indicate the recipients of a message :

 - the `To:` header line contains the list of the email addresses of the primary recipients of the message. Several addresses are separated by using commas.
 - the `cc:` header line is used by the sender to provide a list of email addresses that must receive a carbon copy of the message. Several addresses can be listed in this header line, separated by commas. All recipients of the email message receive the `To:` and `cc:` header lines. 
 - the `bcc:` header line is used by the sender to provide a list of comma separated email addresses that must receive a blind carbon copy of the message. The `bcc:` header line is not delivered to the recipients of the email message. 

A simple email message containing the `From:`, `To:`, `Subject:` and `Date:` header lines and two lines of body is shown below.

::

 From: Bob Smith <Bob@machine.example>
 To: Alice Doe <alice@example.net>, Alice Smith <Alice@machine.example>
 Subject: Hello
 Date: Mon, 8 Mar 2010 19:55:06 -0600
 
 This is the "Hello world" of email messages.
 This is the second line of the body


Note the empty line after the `Date:` header line. This empty line marks the boundary between the header and the body of the message.

Several other header lines are defined in :rfc:`5322` and other optional header lines have been defined elsewhere [#femailheaders]_. Furthermore, many email software define their own header lines starting from `X-`. Several of these header lines are worth being discussed here :

 - the `Message-Id:` header line is used to associate a "unique" identifier to each email. Email identiefiers are usually structured as `string@domain` where `string` is a unique character string or sequence number chosen by the sender of the email and `domain` the domain name of the sender. 
 - the `In-reply-to:` is used when a message was created in reply to a previous message. In this case, the end of the `In-reply-to:` line contains the identifier of the original message.
 - the `Received:` header line is used when an email message is processed by several servers before reaching its destination. Each intermediate email server adds a `Received:` header line. These header lines are useful to debug problems in delivering email messages.

The figure below shows the header lines of one email message. The message was orginitated at a host named `wira.firstpr.com.au` and was received by `smtp3.sgsi.ucl.ac.be`. The `Received:` lines have been wrapped for readability.

::

 Received: from smtp3.sgsi.ucl.ac.be (Unknown [10.1.5.3])
     by mmp.sipr-dc.ucl.ac.be
     (Sun Java(tm) System Messaging Server 7u3-15.01 64bit (built Feb 12 2010))
     with ESMTP id <0KYY00L85LI5JLE0@mmp.sipr-dc.ucl.ac.be>; Mon,
     08 Mar 2010 11:37:17 +0100 (CET)
 Received: from mail.ietf.org (mail.ietf.org [64.170.98.32])
     by smtp3.sgsi.ucl.ac.be (Postfix) with ESMTP id B92351C60D7; Mon,
     08 Mar 2010 11:36:51 +0100 (CET)
 Received: from [127.0.0.1] (localhost [127.0.0.1])	by core3.amsl.com (Postfix)
     with ESMTP id F066A3A68B9; Mon, 08 Mar 2010 02:36:38 -0800 (PST)
 Received: from localhost (localhost [127.0.0.1])	by core3.amsl.com (Postfix)
     with ESMTP id A1E6C3A681B	for <rrg@core3.amsl.com>; Mon,
     08 Mar 2010 02:36:37 -0800 (PST)
 Received: from mail.ietf.org ([64.170.98.32])
     by localhost (core3.amsl.com [127.0.0.1]) (amavisd-new, port 10024)
     with ESMTP id erw8ih2v8VQa for <rrg@core3.amsl.com>; Mon,
     08 Mar 2010 02:36:36 -0800 (PST)
 Received: from gair.firstpr.com.au (gair.firstpr.com.au [150.101.162.123])
     by core3.amsl.com (Postfix) with ESMTP id 03E893A67ED	for <rrg@irtf.org>; Mon,
     08 Mar 2010 02:36:35 -0800 (PST)
 Received: from [10.0.0.6] (wira.firstpr.com.au [10.0.0.6])
     by gair.firstpr.com.au (Postfix) with ESMTP id D0A49175B63; Mon,
     08 Mar 2010 21:36:37 +1100 (EST)
 Date: Mon, 08 Mar 2010 21:36:38 +1100
 From: Robin Whittle <rw@firstpr.com.au>
 Subject: Re: [rrg] Recommendation and what happens next
 In-reply-to: <C7B9C21A.4FAB%tony.li@tony.li>
 To: RRG <rrg@irtf.org>
 Message-id: <4B94D336.7030504@firstpr.com.au>
 
 Message content removed

Initially, email was used to exchange small messages of ASCII text between computer scientists. However, with the growth of the Internet, this became a severe limitation for two reasons. First, non-English speakers wanted to write emails in their mother language that often requires more characters than those of the ASCII character table. Second, many users wanted to send other content than ASCII text by email such as binary files, images or sound. 

To solve this problem, the IETF_ developed the Multipurpose Internet Mail Extensions (:term:`MIME`). These extensions where carefully designed to allow Internet email to carry non-ASCII characters and binary files without breaking the email servers that were deployed at that time. This requirement for backward compatibility forced the MIME designers to develop extensions to the existing email message format :rfc:`822` instead of defining a completely new format that would have been better suited to support the new types of emails. 

.. sidebar:: Backward compatibility and the evolution of the Internet
 
 The Internet protocols such as eBackward compatibility Although backward compatibility increases 



:rfc:`2045` defines three new types of header lines that can appear inside the headers of email messages.

 - The `MIME-Version:` header indicates the version of the MIME specification that was used to encode the email message. The current version of MIME is 1.0. Other versions of MIME might be defined in the future. Thanks to this header line, software that process email messages will be able to adapt to the MIME version used to encode the message. Messages that do not contain this header are supposed to be formatted according to the rfc:`822` specification.
 - The `Content-Type:` header line indicates that type of data that is carried inside the message.
 - The `Content-Transfer-Encoding:` Header line is used to specify how the message has been encoded. When MIME was designed, some email servers were only able to process messages containing characters encoded using the 7 bits ASCII character set. Some servers were unable to process 8 bits ASCII characters and dropped such characters if they appeared. To solve this problem, several techniques were designed to map 

The `Content-Type:` header line is used for two different purposes. When used inside the email header, it indicates how the MIME email message is structured. :rfc:`2046` defines the utilisation of this header line. The two most common structures for MIME messages are :

 - `Content-Type: multipart/mixed`. This header line indicates that the MIME message contains several independant parts. For example, such a message may contain a part in plain text and a binary file.
 - `Content-Type: multipart/alternative`. This header line indicates that the MIME message contains several representations of the same information. For example, a `multipart/alternative` message may contain both a plain text and an HTML version of the same text. 

To support these two types of MIME messages, the recipient of a message must be able to extract the different parts from the message. In :rfc:`822`, an empty line was used to separate the header lines from the body. Using an empty line to separate the different parts of an email body would be difficult as an email message can naturally contain an empty line. Another possible option would be to define a special line, e.g. `*-*-*-*-*-*-*-*-*-*` to mark the boundary between two parts of a MIME message. Unfortunately, this is not possible as some emails may contain this string in their body (e.g. emails sent to students to explain them the format of MIME messages). To solve this problem, the `Content-Type:` header line contains a second parameter that specifies the string that has been used by the sender of the MIME message to delineate the different parts. In practice, this string is often chosen randomly by the mail client.

The email message below, copied from :rfc:`2046` shows a MIME message that contains two parts that are both in plain text and encoded by using the ASCII character set. Note that the string `simple boundary` is defined in the `Content-Type:` header as the string that marks the boundary between the header and the first part and also between the first and the second part and at the end of the message. Other example of MIME messages may be found in :rfc:`2046`.

::

 Date: Mon, 20 Sep 1999 16:33:16 +0200
 From: Nathaniel Borenstein <nsb@bellcore.com>
 To: Ned Freed <ned@innosoft.com>
 Subject: Test
 MIME-Version: 1.0
 Content-Type: multipart/mixed; boundary="simple boundary"

 preamble, to be ignored

 --simple boundary
 Content-Type: text/plain; charset=us-ascii

 First part

 --simple boundary
 Content-Type: text/plain; charset=us-ascii

 Second part
 --simple boundary

The `Content-Type:` header can also be used inside a MIME part. In this case, it indicates the type of data that may be found in this part. Each data type is specified as a type followed by a subtype. A detailed description may be found in :rfc:`2046`. Some of the most popular `Content-Type:` are :

 - `text`. The message part contains information in textual format. There are several subtypes : `text/plain` for regular ASCII text, `text/html` defined in :rfc:`2854` for documents in HTML_ format or the `text/enriched` format defined in :rfc:`1896`. The `Content-Type:` header line may contain a second parameter that specifies the character set used to encode the text. `charset=us-ascii` is the standard ASCII character.  Other frequent character sets include `charset=UTF8` or `charset=iso-8859-1`. The `list of standard character sets <http://www.iana.org/assignments/character-sets>`_ is maintained by IANA_
 - `image`. The message part contains a binary representation of an image. The subtype indicates the format of the image. 
 - `audio`. The message part contains an audio clip. The subtype indicates the format of the audio clip.
 - `video`. The message part contains a video clip. The subtype indicates the format of the video clip.
 - `application`. The message part contains binary information that was produced by a particular application that is listed as the subtype. Email clients may use the subtype to launch the application that is able to decode the received binary information. 


.. sidebar:: From ASCII to Unicode

 The first computers used different techniques to represent characters in memory and on disk. During the 1950s, most computers were isolated. During the 1960s, computers became less and less isolated and started to exchange information via tape or telephone lines. Unfortunately, each vendor had its own proprietary character set and exchanging data between computers from different vendors was sometimes difficult. The 7 bits ASCII character :rfc:`20` set was adopted by several vendors and by many Internet protocols. However, ASCII became a problem with the internationalisation of the Internet and the desire of more and more users to use character sets that support their own written language. A first move was the definition of ISO-8859_ by ISO_ This family of standards specified various character sets that allow to represent many European written languages by using 8 bits characters. Unfortunately, ISO-8859 was not able to support some widely used languages such as those used in Asian countries. Fortunately, at the end of the 1980s, several computer scientists proposed to develop a standard that allows to support all written languages that are used on Earth today. The Unicode standard [Unicode]_ has now been adopted by most computer and software vendors. It defines the standard way to encode characters. It can be expected that all applications, notably on the Internet, will support Unicode.

 
The last MIME header line is `Content-Transfer-Encoding:`. This header line is used after the `Content-Type:` header line in a message part. It specifies how the message part has been encoded. The default encoding is to use 7 bits ASCII. The most frequence encodings are `quoted-printable` and `Base64`. They both allow to encode a sequence of bytes in a set of ASCII lines that can be safely transmitted by email servers. `quoted-printable` is defined in :rfc:`2045`. We briefly describe `base64` which is defined in :rfc:`2045` and :rfc:`4648`. 

`Base64` divides the sequence of bytes to be encoded in groups of three bytes (with the last group being possibly partially filled). Each group of three bytes is divided in four six-bits fields and each six bits field is encoded as a character from the table below. 

+-------+----------+-------+----------+-------+----------+-------+----------+
| Value | Encoding | Value | Encoding | Value | Encoding | Value | Encoding |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   0   |    A     |  17   |    R     |  34   |    i     |  51   |     z    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   1   |    B     |  18   |    S     |  35   |    j     |  52   |     0    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   2   |    C     |  19   |    T     |  36   |    k     |  53   |     1    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   3   |    D     |  20   |    U     |  37   |    l     |  54   |     2    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   4   |    E     |  21   |    V     |  38   |    m     |  55   |     3    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   5   |    F     |  22   |    W     |  39   |    n     |  56   |     4    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   6   |    G     |  23   |    X     |  40   |    o     |  57   |     5    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   7   |    H     |  24   |    Y     |  41   |    p     |  58   |     6    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   8   |    I     |  25   |    Z     |  42   |    q     |  59   |     7    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|   9   |    J     |  26   |    a     |  43   |    r     |  60   |     8    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  10   |    K     |  27   |    b     |  44   |    s     |  61   |     9    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  11   |    L     |  28   |    c     |  45   |    t     |  62   |     \+   |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  12   |    M     |  29   |    d     |  46   |    u     |  63   |     /    |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  13   |    N     |  30   |    e     |  47   |    v     |       |          |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  14   |    O     |  31   |    f     |  48   |    w     |       |          |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  15   |    P     |  32   |    g     |  49   |    x     |       |          |
+-------+----------+-------+----------+-------+----------+-------+----------+
|  16   |    Q     |  33   |    h     |  50   |    y     |       |          |
+-------+----------+-------+----------+-------+----------+-------+----------+

The example below, from :rfc:`4648` illustrates the `base64` encoding.

 +----------------+----------------------------------------------------------+
 |  Input data    | 0x14fb9c03d97e                                           |
 +----------------+----------------------------------------------------------+
 |  8-bit         | 00010100 11111011 10011100   00000011 11011001 01111110  |
 +----------------+----------------------------------------------------------+
 |  6-bit         | 000101 001111 101110 011100  000000 111101 100101 111110 |
 +----------------+----------------------------------------------------------+
 |  Decimal       |    5      15     46     28      0     61     37     62   |
 +----------------+----------------------------------------------------------+
 |  Encoding      |    F      P      u      c       A      9      l      \+  |
 +----------------+----------------------------------------------------------+
   
The last point to be discussed about `base64` is what happens when the sequence of bytes to be encoded are not a multiple of three. In this case, the last group of bytes may contain one or two bytes instead of three. `Base64` reserves the `=` as a padding character. This character is used twice when the last group contains two bytes and once when the last group of bytes contains one byte as illustrated by the two examples below. 

 +----------------+-----------------------+
 |  Input data    | 0x14                  |
 +----------------+-----------------------+
 |  8-bit         | 00010100              |
 +----------------+-----------------------+
 |  6-bit         | 000101 000000         |
 +----------------+-----------------------+
 |  Decimal       |    5     0            |
 +----------------+-----------------------+
 |  Encoding      |    F     A    \=  \=  |
 +----------------+-----------------------+



 +----------------+-----------------------------+
 |  Input data    | 0x14b9                      |
 +----------------+-----------------------------+
 |  8-bit         | 00010100  11111011          |
 +----------------+-----------------------------+
 |  6-bit         | 000101 001111 101100        |
 +----------------+-----------------------------+
 |  Decimal       |    5    15      44          |
 +----------------+-----------------------------+
 |  Encoding      |    F     P       s     \=   |
 +----------------+-----------------------------+



Now that we have explained the format of the email messages, we can discuss how these messages can be exchanged through the Internet. The figure below illustrates the protocols that are used when `Alice` sends an email message to `Bob`. `Alice` prepares her email with an email client or on a webmail interface. To send her email to `Bob`, `Alice`'s client will use the Simple Mail Transfert Protocol (:term:`SMTP`) to deliver her message to her SMTP server. `Alice`'s email client is configured with the name of the default SMTP server for her domain. There is usually at least one SMTP server per domain. Do deliver the message, `Alice`'s SMTP server must find the SMTP server that contains `Bob`'s mailbox. This can be done by using the Mail eXchange (MX) records of the DNS. A set of MX records can be associated to each domain. Each MX record contains a numerical preference and the fully qualified domain name of a SMTP server that is responsible for the domain. The DNS can return several MX records for a given domain. In this case, the server with the lowest preference is used first. If this server is not reachable, the second most preferred server is used ... `Bob`'s SMTP server will store the email sent by `Alice` until `Bob` retrieves the message by using a webmail interface or protocols such as the Post Office Protocol (:term:`POP`) or the Internet Message Access Protocol (:term:`IMAP`). 
 
.. figure:: fig/app-fig-012-c.png
   :align: center
   :scale: 50 

   Email delivery protocols


.. _SMTP:

The Simple Mail Transfert Protocol
----------------------------------

The Simple Mail Transfert Protocol (:term:`SMTP`) defined in :rfc:`5321` is a client-server protocol. The SMTP specification distinguishes five types of hosts that are involved in the delivery of email messages. Email messages are composed on a Mail User Agent (MUA). In practice, the MUA is either an email client or a webmail. The MUA sends the email message to a Mail Submission Agent (MSA). The MSA processes the received email and forwards it to the Mail Transmission Agent (MTA). The MTA is responsible for the transmission of the email, directly or via intermediate MTAs to the MTA of the destination domain. This destination MTA will then forward the message to the Mail Delivery Agent (MDA) where it will be accessed by the recipient's MUA. SMTP is used for the interactions between MUA and MSA [#fsmtpauth]_, MSA-MTA and MTA-MTA.

SMTP is a text-based protocol like many other application-layer protocols on the Internet. SMTP use the byte-stream service and servers listen on port `21`. SMTP clients sends commands that are each composed of one line of ASCII text terminated by `CR+LF`. SMTP servers reply by sending ASCII lines that contain a three digits numerical error/success code and additional comments.

The SMTP protocol, like most text-based protocols, is specified as a :term:`BNF`. The full BNF is defined in :rfc:`5321`. The main SMTP commands are defined by the following BNF rules.::

 helo = "HELO" SP Domain CRLF
 mail = "MAIL FROM:" Path CRLF
 rcpt = "RCPT TO:" ( "<Postmaster@" Domain ">" / "<Postmaster>" / Path ) CRLF
 data = "DATA" CRLF
 quit = "QUIT" CRLF
 Path           = "<" Mailbox ">"
 Domain         = sub-domain *("." sub-domain)
 sub-domain     = Let-dig [Ldh-str]
 Let-dig        = ALPHA / DIGIT
 Ldh-str        = *( ALPHA / DIGIT / "-" ) Let-dig
 Mailbox        = Local-part "@" Domain 
 Local-part     = Dot-string 
 Dot-string     = Atom *("."  Atom)
 Atom           = 1*atext


In this BNF, `atext` corresponds to the printable ASCII characters. This BNF rule is defined in :rfc:`5322`. The five main commands are `HELO`, `MAIL FROM:`, `RCPT TO:`, `DATA` and `QUIT`. `Postmaster` is the alias of the system administrator who is responsible for a given domain or SMTP server. All domains must have a `Postmaster` alias.

The SMTP responses returned by the SMTP server are defined by the following BNF rules ::

   Greeting       = "220 " Domain [ SP textstring ] CRLF
   textstring     = 1*(%d09 / %d32-126) 
   Reply-line     = *( Reply-code "-" [ textstring ] CRLF )
                    Reply-code [ SP textstring ] CRLF
   Reply-code     = %x32-35 %x30-35 %x30-39

SMTP servers use structured reply codes. The first digit of the reply code indicates whether the command was successful or not. A reply code of `2xy` indicates that the command has been accepted. A reply code of `3xy` indicates that the command has been accepted, but additional information from the client is expected. A reply code of `4xy` indicates a transient negative reply. For some reasons, indicated by the other digits or the comment, the command cannot be processed immediately, but there is some hope that the problem will be transient. This is a hint to the client that it should try again the same command later. In contrast, a reply code of `5xy` indicates a permanent failure or error. In this case, it is useless for the client to retry the same command later. Other application later protocols such as FTP :rfc:`959`  or HTTP :rfc:`2616` use a similar structure for their reply codes. Additional details about the other reply codes may be found in :rfc:`5321`.

Example of SMTP reply codes include the following : ::

   500  Syntax error, command unrecognized 
   501  Syntax error in parameters or arguments
   502  Command not implemented 
   503  Bad sequence of commands
   220  <domain> Service ready
   221  <domain> Service closing transmission channel
   421  <domain> Service not available, closing transmission channel
   250  Requested mail action okay, completed
   450  Requested mail action not taken: mailbox unavailable 
   452  Requested action not taken: insufficient system storage
   550  Requested action not taken: mailbox unavailable 
   354  Start mail input; end with <CRLF>.<CRLF>

The first four reply codes correspond to errors the commands sent by the client. The fourth reply code would be sent by the server when the client sends command in an incorrect order (e.g. the client tries to send an email before providing the destination of the message). Reply code `220` is used by the server as the first message when it agrees to interact with the client. Reply code `221` is sent by the server before closing the underlying TCP connection. Reply code `421` is returned when there is a problem (e.g. lack of memory/disk resources) that prevents the server from acception the TCP connection. Reply code `250` is the standard positive reply that indicates the sucess of the previous command. Reply codes `450` and `452` indicate that the destination mailbox is temporarily unavailable, for different reasons while reply code `550` indicates that the mailbox does no exist or cannot be used for policy reasons. Reply code `354` is sent to allow the client to transmit its email message.

The transfert of an email message is performed in three phases. During the first phase, the client opens a TCP connection with the server. Then the client and the server exchange greetings messages. Most servers insist on receiving valid greeting messages and some of them drop the underlying TCP connection if they do not receive valid greetings. Once the greetings have been exchanged, the email transfert phase can start. During this phase, the client transfers one or more email messages by indicating the email address of the sender, the email address of the recipient followed by the headers of the body of the email message. Once the client has sent all the email messages to the SMTP server, it terminates the SMTP association.

A successful transfert of an email message is shown below ::

 S: 220 smtp.example.com ESMTP MTA information
 C: HELO mta.example.org
 S: 250 Hello mta.example.org, glad to meet you
 C: MAIL FROM:<alice@example.org>
 S: 250 Ok
 C: RCPT TO:<bob@example.com>
 S: 250 Ok
 C: DATA
 S: 354 End data with <CR><LF>.<CR><LF>
 C: From: "Alice Doe" <alice@example.org>
 C: To: Bob Smith <bob@example.com>
 C: Date: Mon, 9 Mar 2010 18:22:32 +0100
 C: Subject: Hello
 C:
 C: Hello Bob
 C: This is a small message containing 4 lines of text. 
 C: Best regards,
 C: Alice
 C: .
 S: 250 Ok: queued as 12345
 C: QUIT
 S: 221 Bye


In this example, the MTA running on `mta.example.org` opens a TCP connection to the SMTP server on host `smtp.example.com`. The lines prefixed with `S:` (resp. `C:`) are the responses sent by the server (resp. the commands sent by the client). The server sends its greetings as soon as the TCP connection has been established. The client then sends the `HELO` command with its fully qualified domain name. The server replies with reply-code `250` and sends its greetings. To send an email, the client must issue three commands : `RCPT TO:` that provides the address of the recipient of the email, `MAIL FROM:` that indicates the address of the sender of the email and `DATA` that starts the actual transfer of the email message. The `MAIL FROM:` and `RCPT TO:` must be issued before the `DATA` command, but the former does not need to be sent before the former. After having received the `354` reply code, the client sends the headers and the body of its email message. The client indicates the end of the message by sending a line containing only the `.` (dot) character [#fdot]_. The server confirms that the email message has been queued for delivery or transmission with a reply code of `250`. The client issues the `QUIT` command to close the session and the server confirms with reply-code `221` before closing the TCP connection.


.. sidebar:: Open SMTP relays and spam 

 Since its creation in 1971, email was a very useful tool that was used my many users to exchange lots of information. Unfortunately, over the years, some unscrupulous users found ways to use email to 

A `study <http://www.enisa.europa.eu/act/res/other-areas/anti-spam-measures>`_ carried out by ENISA_ in 2009 reveals that 95% of email was spam.

http://www.templetons.com/brad/spamreact.html#msg
allowed to quickly exchange infoUntil a few years ago, most SMTP servers agreed to relay messages sent by any user. This default configuration allowed 

were configured to relay messages 
 smtp auth : rfc:`4954`
 configuration of relays :rfc:`5068`
 first spam Http://www.templetons.com/brad/spamreact.html#msg
 Unsollicited Commercial Email (UCE)


.. _POP:

The Post Office Protocol
------------------------

When the first versions of SMTP were designed, the Internet was composed of minicomputers_ that were used by an entire university departement or research lab. These minicomputers_ were used by many users at the same time. Email was mainly used to send messages from a user on a given host to another user on a remote host. At that time, SMTP was the only protocol involved in the delivery of the emails as all hosts attached to the network were running a SMTP server. On such hosts, email destined to local users was delivered by placing the email in a directory owned by the user. However, the introduction of the personnal computers in the 1980s, changed the environment. Initially, users of these personnal computers used applications such as telnet_ to open a remote session on the local minicomputer to read their email. This was not user-friendly. A better solution appeared with the development of email client applications running on personnal computers. Several protocols were designed to allow these client applications to retrieve the email messages destined to a user from his/her server. Two of these protocols became popular and are still used today. The Post Office Protocol (POP), defined in :rfc:`1939`, is the simplest one. It allows a client to download all the messages destined to a given user from his/ser email server. We describe POP briefly in this section. The second protocol is the Internet Message Access Protocol (IMAP), defined in :rfc:`3501`. IMAP is more powerful, but also more complex than POP. While POP is mainly used to download email messages, IMAP was designed to allow client applications to efficiently access in real-time to messages stored in various folders on servers. IMAP assumes that all the messages of a given user are stored on a server and provides the functions that are necessary to search, download, delete or filter messages. 


POP is another example of a simple line-based protocol. POP runs above the bytestream service. A POP server usually listens to port 110. A POP session is composed of three parts : an `authorisation` phase during which the server verifies the client's credential, a `transaction` phase during which the client downloads messages and an `update` phase that concludes the session. The client sends commands and the server replies are prefixed by `+OK` to indicate a successful command and by `-ERR` to indicate errors.

When a client opens a connection with the server, the latter sends as banner and ASCII-line starting with `+OK`. The POP session is at that time in the `authorisation` phase. In this phase, the client can send its username (resp. password) with the `USER` (resp. `PASS`) command. The server returns `+OK` if the username (resp. password) is valid and `-ERR` otherwise. 

Once the username and passward have been validated, the POP session enters in the `transaction` phase. In this phase, the client can issue several commands. The `STAT` command is used to retrieve the status of the server. Upon reception of this command, the server replies with a line that contains `+OK` followed by the number of messages in the mailbox and the total size of the mailbox in bytes. The `RETR` command, followed by a space and an integer, is used to retrieve the nth message of the mailbox. The `DELE` command is used to mark for deletion the nth message of the mailbox.

Once the client has retrieved and possibly deleted the emails contained in the mailbox, it must issue the `QUIT` command. This command terminates the POP session and indicates that the server can delete all messages that have been marked for deletion by using the `DELE` command. 

The figure below provides a simple POP session. All lines prefixed with `C:` (resp. `S:`) are sent by the client (resp. server). ::

      S:    +OK POP3 server ready 
      C:    USER alice
      S:    +OK
      C	    PASS 12345pass
      S:    +OK alice's maildrop has 2 messages (620 octets)
      C:    STAT
      S:    +OK 2 620
      C:    LIST
      S:    +OK 2 messages (620 octets)
      S:    1 120
      S:    2 500
      S:    .
      C:    RETR 1
      S:    +OK 120 octets
      S:    <the POP3 server sends message 1>
      S:    .
      C:    DELE 1
      S:    +OK message 1 deleted
      C:    QUIT
      S:    +OK POP3 server signing off (1 message left)


In this example, a POP client contacts a POP server on behalf of the user named `alice`. Note that in this example, Alice's password is sent in clear by the client. This implies that if someone is able to capture the packets sent by Alice, he will know Alice's password [#fapop]_. Then Alice's client issues the `STAT` command to know the number of messages that are stored in her mailbox. It then retrieves and deletes the first message of the mailbox.

.. sidebar:: SMTP versus POP

 Both SMTP and POP are involved in the delivery of email messages. They are thus complimentary protocols. However, there are two important differences between these two protocols. First, POP forces the client to be authenticated, usually by providing a username and a password. SMTP was designed without any authentication. Second, the POP client downloads email messages from the server, while the SMTP client sends email messages. 


.. .. sidebar:: Names and passwords
.. The simplest authentication
.. APOP mrose c4c9334bac560ecc979e58001b3e22fb


.. _HTTP:

The HyperText Transfert Protocol
================================

In the early days of the Internet, the network was mainly used for remote terminal access with telnet_, email and file transfert. The default file transfert protocol, ftp, defined in :rfc:`959` was widely used and ftp clients and servers are still included in most operating systems.

Many ftp client offer a user interface similar to a Unix shell and allows the client to browse the file system on the server and send and retrieve files. ftp servers can be configured in two modes :

 - authenticated : in this mode, the ftp server only accepts users with a valid userid and password. Once authenticated, they can access the files and directories according to their permissions
 - anonymous : in this mode, clients supply the `anonymous` userid and their email address as password. These clients are granted access to a special zone of the file system that only contains public files. 

ftp was very popular in the 1990s and early 2000s, but today it has mostly been pserseded by more recent protocols. Authenticated access to files is mainly done by using the Secure Shell (ssh) protocol defined in :rfc:`4251` and supported by clients such as scp_ or sftp_. Anonymous access is nowadays mainly provided by web protocols.

In the late 1980s, high energy physicists working at CERN_ had to efficiently exchange documents about their ongoing and planned experiments. `Tim Berners-Lee`_ evaluated several of the documents sharing that were available then [B1989]_. As none of the existing solutions met CERN's requirements, they choose to develop a completely new document sharing system. This system was initially called the `mesh`, but was quickly renamed the `world wide web`. The starting point for the `world wide web` is the hypertext. An hypertext is a text that contains references (hyperlinks) to other text that the reader can immediately access. Compared to the hypertexts that were used in the late 1980s, the main innovation introduced by the `world wide web` was to allow hyperlinks to reference documents stored on remote machines. 


.. figure:: fig/app-fig-014-c.png
   :align: center
   :scale: 50 

   World-wide web clients and servers 


A document sharing system such as the `world wide web` is composed of three important parts.

 1. A standardised addressing scheme that allows to unambiguously identify documents 
 2. A standard document format. html http://www.w3.org/MarkUp
 3. A standardised protocol that allows to efficiently retrieve documents stored on a server


.. sidebar:: Open standards and open implementations

 Open standards have and are still playing a key role in the success of the `world wide web` as we know it today. However, open and efficient implementations of these standards have greatly contributed to the sucess of the `web`. When CERN started to work on the `web`, their objective was to build a running system that could be used by physicists. They developped open-source implementations of the `first web servers <http://www.w3.org/Daemon/>`_ and `web clients <http://www.w3.org/Library/Activity.html>`. These open-source implementations were powerful and could be used as is by institutions willing to share information on the web. They were also extended by other developpers who contributed to new features. For example, NCSA_ added support for images in their `Mosaic browser <http://en.wikipedia.org/wiki/Mosaic_(web_browser)>`_ that was eventually used to create `Netscape Communications <http://en.wikipedia.org/wiki/Netscape>`_. 


The first component of the `world wide web` are the Uniform Resource Identifiers (URI) defined in :rfc:`3986`. A URI is a character string that unambigously identifies a resource on the world wide web. Here is a subset of the BNF for the URIs ::

   URI         = scheme ":" "//" authority path [ "?" query ] [ "#" fragment ]
   scheme      = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
   authority   = [ userinfo "@" ] host [ ":" port ]
   query       = *( pchar / "/" / "?" )
   fragment    = *( pchar / "/" / "?" )

The first componet of a URI is its `scheme`. In practice, the `scheme` identifies the application-layer protocol that must used by the client to retrieve the document. The most frequent scheme is `http` that will be described later, but a URI scheme can be defined for almost any application layer protocol [#furilist]_. The characters `:` and `//` follow the `scheme` of any URI.

The second part of the URI  is the `authority`. It includes the DNS name or the IP address on which the document can be retrieved by using the protocol specified in the `scheme`. This name can be preceeded by some information about the user (e.g. a username) who is requesting the information. Earlier definitions of the URI allowed to specify a username and a password before the `@` character (:rfc:`1738`), but this is now deprecated as placing a password inside a URI is insecure. The host name can be followed by the semicolon character and a port number. A default port number is defined for each `scheme` and the port number should only be included in the URI is a non-default port number is used.

The third part of the URI is the path to the document. This path is structured as filenames on a Unix host. If the path is not specified, the server will provide a default document. The last two optional parts of the URI are used to provide a query and indicate a specific part (e.g. a section in an article) of the requested document. Sample URIs are shown below ::

   http://tools.ietf.org/html/rfc3986.html
   mailto:infobot@example.com?subject=current-issue   
   http://docs.python.org/library/basehttpserver.html?highlight=http#BaseHTTPServer.BaseHTTPRequestHandler
   ftp://cnn.example.com&story=breaking_news@10.0.0.1/top_story.htm

The first URI corresponds to a document named `rfc3986.html` that is stored on the server named `tools.ietf.org` and can be accessed by using the `http` protocol on its default port. The second URI corresponds to an email message with subject `current-issue` that will be sent to user `infobot` in domain `example.com`. The `mailto:` URI scheme i sdefined in :rfc:`2368`. The third URI references the portion `BaseHTTPServer.BaseHTTPRequestHandler` of the document `basehttpserver.html` that is stored in the `library` directory on server `docs.python.org` by using `http`. The query `highlight=http` is associated to this URI. The last URI is somewhat special. Most users will assume that it corresponds to a document stored on the `cnn.example.com` server. However, to parse this URI, it is important to remember that the `@` character is used to separate the usename from the host name in the authorisation part of a URI. This implies that the URI points to a document named `top_story.htm` on host having IPv4 address `10.0.0.1`. The document will be retrieved by using the `ftp` protocol with the username set `cnn.example.com&story=breaking_news`. 

The second component of the `word wide web` is the HyperText Markup Langage (HTML). HTML defines the format of the documents that are exchanged on the `web`. The `first version of HTML <http://www.w3.org/History/19921103-hypertext/hypertext/WWW/MarkUp/Tags.html>`_ was derived from the Standard Generalized Markup Language (SGML) that was standardised in 1986 by ISO_. SGML_ was designed to allow large project documents in industries such as government, law or aerospace to be shared efficiently in a machine-readable manner. These industries require documents that remain readable and editable for tens of years and insisted on a standardised format supported by multiple vendors. Today, SGML_ is not widely used anymore besides specific applications, but children like :term:`HTML` and :term:`XML` are now widespread.

HTML is a markup language that contains several markers. Most markers areA very simple HTML document such as the one shown in the figure below is delineated by the `<HTML>
The HTML document shown below is composed of two parts : a header delineated by the `<HEAD>` and `</HEAD>` markers and a body (between the `<BODY>` and `</BODY>` markers). In the example below, the header only contains a title, but other types of information can be included in the header. The body contains an image, some text and a list with three hyperlinks. The image is included in the web page by indicating its URI between brackets inside the `<IMG SRC="...">` marker. The image can, of course, reside on any server and the client will automatically download it when rendering the web page. The `<H1>...</H1>` marker is used to specify the first level of headings. The `<UL>` indicates an unnumbered list while thhe `<LI>` marker indicates a list item. The `<A HREF="URI">text</A>` indicates an hyperlink. The `text` will be rendered in the web page and client will fetch the URI if the user clicks on the link.

.. figure:: fig/app-fig-015-c.png
   :align: center
   :scale: 50 

   A simple HTML page 

Additional details about the various extensions to HTML may be found in the `official specifications <http://www.w3.org/MarkUp/>`_ maintained by W3C_.

The third component of the `world wide web` is the HyperText Transport Protocol (HTTP). HTTP is a text-based protocol in which the client sends a request and the server returns a response. HTTP runs above the bytestream service and HTTP servers listen by default on port `80`. Each HTTP request contains three parts :

 - a `method` that indicates the type of request, a URI and the version of the HTTP protocol used by the client 
 - a `header` that is used by the client to indicate optionnal parameters for each request. An empty line is used to mark the end of the header.
 - an optionnal MIME document attached to the request

The response sent by the server also contains three parts :
 - a `status line` that indicates whether the request was successful or not
 - a `header` that contains additional information about the response. The header ends with an empty line.
 - a MIME document 

.. figure:: fig/app-fig-017-c.png
   :align: center
   :scale: 50 

   HTTP requests and responses


There are three types of methods in HTTP requests :

 - the `GET` method is the most popular one. It is used to retrieve a document from a server. It should be noted that the client only provides the path of URI of the requested document after the `GET` keyword. For example, if a client requests the http://www.w3.org/MarkUp/ URI, it will open a TCP on port `80` with host `www.w3.org`. The first line of its HTTP request will contain ::
  GET /MarkUp/ HTTP/1.0
 - the `HEAD` method is a variant of the `GET` method that allows to retrieve the header lines for a given URI without retrieveing the entire document. It can be used by a client that wants to verify whether a document has changed compared to a previous version.
 - the `POST` method is less popular. It can be used by a client to send a document to a server. The document sent is attached to the HTTP request.


HTTP clients and servers can include many different HTTP headers in the HTTP requests and responses. Each header is encoded as a single ASCII-line terminated by `CR` and `LF`. Several of these headers are briefly described below. A detailed discussion of all standard headers may be found in :rfc:`1945`. The MIME headers can appear in both HTTP requests and HTTP responses.

 - the `Content-Length:` header is the MIME_ header that indicates the length of the MIME document in bytes`.
 - the `Content-Type:` header is the MIME_ header that indicates the type of the attached MIME document. HTML pages use the `text/html` type.
 - the `Content-Enconding:` header indicates how the MIME_ document has been encoded. This header would be set to `x-gzip` for a document compressed by using the gzip_ software. 

:rfc:`1945` and :rfc:`2616`also defines headers that are specific to HTTP responses. These server headers include :

 - the `Server:` header indicates the version of the web server that has generated the HTTP response. Some servers provide information about the software release and optionnal modules that is uses. For security reasons, some system administrators disable these headers to avoid revealing too much information about their server to potential attackers.
 - the `Date:` header indicates when the HTTP response has been produced by the server.
 - the `Last-Modified:` indicates the last modification date and time of the document attached to the HTTP respons. 
 
Similarly, the following header lines can only appear inside HTTP requests sent by a client :

 - the `User-Agent:` header provides information about the client that has generated the HTTP request. Some servers analyse this header line and return different headers and sometimes different documents for different user agents.
 - the `If-Modified-Since:` header is followed by a date. It enables the clients to cache in memory or on disk the recent or most frequently used documents. When a client needs to request a URI from a server, it first checks whether the document is already inside its cache. If yes, it sends an HTTP request with the `If-Modified-Since:` header indicating the date of the cached document. The server will only return the document attached to the HTTP response if it is newer than the version stored in the client's cache. 
 - the `Referer:` header is followed by a URI. It indicates the URI of the document that the client visited before sending this HTTP request. Thanks to this header, the server can know the URI of the document containing the hyperlink followed by the client, if any. This information is very useful to measurement the impact of advertisements containing hyperlinks placed on websites. 
 - the `Host:` header contains the fully qualified domain name of the URI being requested. 

.. sidebar:: The importance of the `Host:` header line

 The first version of HTTP did not include the `Host:` header line. This was a severe limitation for web hosting companies. For example consider a webhosting company that wants to server both `web.example.com` and `www.dummy.net` on the same physical server. Both web sites contain a `/index.html` document. When a client sends a request for either `http://web.example.com/index.html` or `http://www.dummy.net/index.html`, The HTTP request contains the following line : ::

  GET /index.html HTTP/1.0

 Thanks to the `Host:` header line, the server knows whether the request is for `http://web.example.com/index.html` or `http://www.dummy.net/index.html`. Without the `Host:` header, this is impossible. The `Host:` header line allowed web hosting companies to develop their business by supporting a large number of independant web servers on the same physical server. 


The status line of the HTTP response begins with the version of HTTP used by the server (usually `HTTP/1.0` defined in :rfc:`1945` or `HTTP/1.1` defined in :rfc:`2616`) followed by a three digits status code and additional information in English. The HTTP status codes have a similar structure as the reply codes used by STMP. 

 - All status codes starting with digit `2` indicate a valid response. `200 Ok` indicates that the HTTP request was successfully processed by the server and that the response is valid.
 - All status codes starting with digit `3` indicate that the requested document is not available anymore on the server. `301 Moved Permanently` indicates that the requested document is not anymore available on this server. A `Location:` header containing the new URI of the requested document is inserted in the HTTP response. `304 Not Modified` is used in response to an HTTP request containing the `If-Modified-Since:` header. This status line is used by the server if the document stored on the server is not more recent than the date indicated in the `If-Modified-Since:` header.
 - All status codes starting with digit `4` indicate that the server has detected an error in the HTTP request sent by the client. `400 Bad Request` indicates a syntax error in the HTTP request. `404 Not Found` indicates that the requested document does not exist on the server.
 - All status codes starting with digit `5` indicate an error on the server. `500 Internal Server Error` indicates that the server could not process the request due to an error on the server itself.


In both the HTTP request and the HTTP response, the MIME document refers to a representation of the document with the MIME headers that indicate the type of document and its size.

As an illustration of HTTP/1.0, here are an HTTP request for http://www.ietf.org and the corresponding HTTP respons. The HTTP request was sent by the curl_ command line tool. The `User-Agent:` header line contains more information about this client software. There is no MIME document attached to this HTTP request, it ends with a blank line. ::
  GET / HTTP/1.0
  User-Agent: curl/7.19.4 (universal-apple-darwin10.0) libcurl/7.19.4 OpenSSL/0.9.8l zlib/1.2.3
  Host: www.ietf.org
  


The HTTP response indicates the version of the server software used with the included modules. The `Last-Modified:` header indicates that the requested document was modified about one week before the request. An HTML document (not shown) is attached to the response. Note the blank line between the header of the HTTP response and the attached MIME document. ::

  HTTP/1.1 200 OK
  Date: Mon, 15 Mar 2010 13:40:38 GMT
  Server: Apache/2.2.4 (Linux/SUSE) mod_ssl/2.2.4 OpenSSL/0.9.8e PHP/5.2.6 with Suhosin-Patch mod_python/3.3.1 Python/2.5.1 mod_perl/2.0.3 Perl/v5.8.8
  Last-Modified: Tue, 09 Mar 2010 21:26:53 GMT
  Content-Length: 17019
  Content-Type: text/html
  
  <!DOCTYPE HTML PUBLIC .../HTML>


HTTP was initially designed to share text documents that were self-contained.



.. figure:: fig/app-fig-016-c.png
   :align: center
   :scale: 50 

   HTTP 1.0 and the underlying TCP connection

http 1.0 : :rfc:`1945`

http 1.1 :rfc:`2616`






.. figure:: fig/app-fig-019-c.png
   :align: center
   :scale: 50 

   HTTP 1.1 persistent connections


.. figure:: fig/app-fig-020-c.png
   :align: center
   :scale: 50 

   HTTP proxiesrequests and responses

Email delivery protocols


Writing simple networked applications
=====================================

connect by name API is key !
http://www.stuartcheshire.org/IETF72/

Practice
########


discuss briefly various implementations and mention the evolution of the protocols


for DNS mention security as well and extensions for DNSSEC
for POP, the need for much stronger authentication
for SMTP the problems caused by spam and so on
for HTTP lots of information to be added, mention apache, mention a simple httpd server
time http://tf.nist.gov/service/its.htm


Historical notes
################

email

Ray Tomlinson first email http://openmap.bbn.com/~tomlinso/ray/firstemailframe.html 
First spam, decnet
X400
Fidonet
uucp
bitnet
earn

DNS
/etc/hosts.txt
X.500

www
ottlet
xanadu project
ftp
gopher


Today, Napster does not work anymore as explained due to copyright violations reasons.

One of the most efficient file transfer protocol used today is Bittorrent. Bittorrent also divides files in blocks and allows files to be downloaded from several nodes at the same time. This provides good redundancy in case of node/link failures, but also allows an efficient utilisation of the available link bandwidth by using uncongested paths (the node with the highest bandwidth will automatically serve blocks faster than a congested node). A Bittorrent node will not necessarily receive blocks in sequence. Furthermore, to ensure that all Bittorrent users contribute to the system, Bittorrent implementations apply the tit-for-tat principle which implies that once a node has received a block, it must serve this block to other nodes before being allowed to download new blocks.

Additional information about the Bittorrent protocol may be found i

.. [#fhtonl] For example, the :manpage:`htonl(3)` (resp. :manpage:`ntohl(3)`) function the standard C library converts a 32-bits unsigned integer from the byte order used by the CPU to the network byte order (resp. from the network byte order to the CPU byte order). Similar functions exist in other programming langages.

.. [#fhosts] The :term:`hosts.txt` file is not maintained anymore. The snapshot retrieved on April 15th, 1984 is available from http://ftp.univie.ac.at/netinfo/netinfo/hosts.txt



.. [#fdnstimeline] See http://www.donelan.com/dnstimeline.html for a timeline of DNS related developments. 

.. [#fidn] This specification evolved later to support domain names written by using other character sets than us-ascii :rfc:`3490`. This extension is important to support other languages than English, but a detailed discussion is outside the scope of this document.

.. [#ftld] The official list of top-level domain names is maintained by IANA_ at http://data.iana.org/TLD/tlds-alpha-by-domain.txt Additional information about these domains may be found at http://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

.. [#froot] A copy of the information maintained by each root nameserver is available at http://www.internic.net/zones/root.zone

.. [#frootv6] Until February 2008, the root DNS servers only had IPv4 addresses. IPv6 addresses were added to the root DNS servers slowly to avoid creating problems as discussed in http://www.icann.org/en/committees/security/sac018.pdf In 2010, several DNS root servers are still not reachable by using IPv6. 

.. [#fnamed.root] The current list of the IP addresses of the root nameservers is maintained at http://www.internic.net/zones/named.root . These IP addresses are stable and root nameservers seldom change their IP addresses. DNS resolvers must however maintain an up-to-date copy of this file. 

.. [#fdozen] There are currently 13 root servers. In practice, some of these root servers are themselves implemented as a set of distinct physical servers. See http://www.root-servers.org/ for more information about the physical location of these servers. 

.. [#f8888] Some DNS resolvers allow any host to send queries. OpenDNS_ and GoogleDNS_ are example of open resolvers.

.. [#femailheaders] The list of all standard email header lines may be found at http://www.iana.org/assignments/message-headers/message-header-index.html

.. [#smtpauth] During the last years, many Internet Service Providers, campus and enterprise networks have deployed SMTP extensions :rfc:`4954` on their MSAs. These extensions for the MUAs to be authenticated before the MSA accepts an email message from the MUA. 

.. [#fdot] This implies that a valid email message cannot contain a line with one dot followed by `CR` and `LF`. If a user types such a line in an email, his email client will automatically add a space character before or after the dot when sending the message over SMTP.

.. [#fapop] :rfc:`1939` defines another authentication scheme that is not vulnerable to such attackers.

.. [#furilist] The list of standard URI schemes is maintained by IANA_ at http://www.iana.org/assignments/uri-schemes.html

.. include:: ../links.rst
