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

We will discuss serveral examples of application-level protocols in this chapter.

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

To retrieve the mapping for host `h2.dom`, a client sends its query to the name server that is reponsible for domain `.dom`. The name server directly answers the query. To retrieve a mapping for `h3.a.sdom1.dom` a DNS client first sends a query to the name server that is responsible for the `.dom` domain. This nameserver returns the nameserver that is responsible for the `sdom1.dom` domain. This nameserver can now be contacted to obtain the nameserver that is responsible for the `a.sdom1.dom` domain. This nameserver can be contacted to retrieve the mapping for the `h3.a.sdom1.dom` name. Thanks to this organisation of the nameservers, it is possible for a DNS client to obtain the mapping of any host inside the `.dom` domain or any of its subdomains. To ensure that any DNS client will be able to resolve any fully qualified domain name, there are special nameservers that are responsible for the root of the domain name hierarchy. These nameservers are called :term:`root nameserver`. There are currently about a dozen of root nameservers [#fdozen]_.   

Each root nameserver maintains the list [#froot]_ of all the nameservers that are responsible for each of the top-level domain names and their IP addresses. Allroot nameservers are synchronised and provide the same answers. By querying any of the root nameservers, a DNS client can obtain the nameserver that is responsible for any top-level-domain name. From this nameserver, it is possible to resolve any domain, ... 

To be able to contact the root nameservers, each DNS client must know their IP addresses. This implies, that DNS clients must maintain an up-to-date list of the IP addresses of the root nameservers [#fnamed.root]_. Without this list, it is impossible to contact the root nameservers. Forcing all Internet hosts to maintain the most recent version of this list would be difficult from an operational viewpoint. To solve this problem, the designers of the DNS introduced a special type of DNS server : the DNS resolvers. A :term:`resolver` is a server that provides name resolution service for a set of clients. A network usually contains a few resolvers. Each host in these networks is configured to send all its DNS queries via one of its local resolvers. These queries are called `recursive queries as the :term:`resolver` must recurse through the hierarchy of nameservers to find the `answer. 

DNS resolvers have several advantages over letting each Internet host query directly nameservers. First, regular Internet hosts do not need to maintain the up-to-date list of the IP addresses of the root servers. Second, regular implements the DNS protocol and sends queries to nameservers

  Furthermore, to traverse the tree of all domain names, DNS clients must send and receive DNS messages.  However. This list  use stable IP addresses that do not change frequently

In practice, regular Internet hosts do not usually query the nameservers directly. Most networks contain :term:`resolvers`

 
Any DNS client can contact a root nameserver 




In practice, regular hosts 

The last component of the Domain Name System is the DNS protocol. This 


DNS protocol runs both above the datagram service and the bytestream service. In practice, the datagram service is used when short queries and responses are exchanged.

.. sidebar:: Network byte order

 Both the datagram and the byte-stream services used on the Internet have been designed to allow applications to exchange groups of bytes. Many applications exchange character strings encoded by using the ascii character set :rfc:`20` or one of its derivatives. Besides characters, some applications also need to exchange 16 bits and 32 bits fields such as IPv4 addresses. A naive solution would have been to send the 16- or 32-bits field as it was encoded in memory. Unfortunately, there are different methods to store 16- or 32-bits fields in memory. Some CPUs store the most significant byte of a 16-bits field in the first address of the field while others store the least significant byte at this location. When networked applications running on different CPUs exchange 16 bits fields, there are two possibilies to transfer them over the transport service :

  - send the most significant byte followed by the least significant byte
  - send the least significant byte followed by the most significant byte

 The first possibility was named  `big-endian` in a note written by Cohen [Cohen1980]_ while the second was named `little-endian`. Vendors of CPUs that used `big-endian` in memory insisted on using `big-endian` encoding in networked applications while vendors of CPUs that used `little-endian` recommended the opposite. Several studies were written on the relative merits of each type of encoding, but the discussion became almost a religious issue [Cohen1980]_. Eventually, the Internet chose the `big-endian` encoding, i.e. multi-byte fields are always transmitted by sending the most significant byte first :rfc:`791` and refer to this encoding as the :term:`network-byte order`. Most librairies [#fhtonl]_ used to write networked applications contain functions to convert multibyte fields from memory to the network byte order and vice versa. 





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


The second model is the peer-to-peer model. It appaered recently as another way to organise Internet applications. In the peer-to-peer model, all


.. _DNS:

introduce the address


.. _Email:

Electronic mail
===============



ascii : :rfc:`20`
abnf crocker : :rfc:`5234`

.. figure:: fig/app-fig-010-c.png
   :align: center
   :scale: 50 

   Structure of email messages


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


 
.. figure:: fig/app-fig-012-c.png
   :align: center
   :scale: 50 

   Email delivery protocols


describe architecture

.. _SMTP:

The Simple Mail Transfert Protocol
----------------------------------

smtp :rfc:`821`

describe protocol

MIME :rfc:`2045` :rfc:`2046`

.. _POP:

The Post Office Protocol
------------------------

The Post Office Protocol is defined in :rfc:`1939`

The IMAP :rfc:`2060`

webmail (mainly implementations, no standard)

.. _HTTP:

The HyperText Transfert Protocol
================================

In the early days of the Internet, the network was mainly used for remote terminal access with telnet_, email and file transfert. The default file transfert protocol, ftp, defined in :rfc:`959` was widely used and ftp clients and servers were included in most operating systems.

An ftp client offers a user interface similar to a Unix shell and allows the client to browse the file system on the server and send and retrieve files. ftp servers can be configured in two modes :

 - authenticated : in this mode, the ftp server only accepts users with a valid userid and password. Once authenticated, they can access the files and directories according to their permissions
 - anonymous : in this mode, clients supply the anonymous` anonymous` a special zone of the file system is 


.. figure:: fig/app-fig-013-c.png
   :align: center
   :scale: 50 

   File transfer protocol 


urls : :rfc:`1738` see also http://www.w3.org/Addressing

html http://www.w3.org/MarkUp

http 1.0 : :rfc:`1945`

http 1.1 :rfc:`2616`

Structure of email messages



.. figure:: fig/app-fig-014-c.png
   :align: center
   :scale: 50 

   World-wide web clients and servers 


.. figure:: fig/app-fig-015-c.png
   :align: center
   :scale: 50 

   A simple HTML page 

.. figure:: fig/app-fig-017-c.png
   :align: center
   :scale: 50 

   HTTP requests and responses


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

.. [#fnamed.root] The current list of the IP addresses of the root nameservers is maintained at http://www.internic.net/zones/named.root . These IP addresses are stable and root nameservers seldom change their IP addresses. DNS resolvers must however maintain an up-to-date copy of this file. 

.. [#fdozen] There are currently 13 root servers. In practice, some of these root servers are themselves implemented as a set of distinct physical servers. See http://www.root-servers.org/ for more information about the physical location of these servers. 

.. include:: ../links.rst
