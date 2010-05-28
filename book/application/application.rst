=====================
The Application Layer
=====================

The Application Layer is the most important and most visible layer in computer networks. Applications reside in this layer and human users interact via those applications through the network. 

In this chapter, we first briefly describe the main principles of the application layer and focus on the two most important models :  the client-server model and the peer-to-peer models. Then, we review in details two families of protocols that have proved to be very useful in networks such as the Internet : electronic mail and the protocols that allow to access information on the world wide web. We also describe the Domain Name System that allows humans to use user-friendly names while the hosts use IP addresses. 

.. include:: principles.rst

.. include:: transport-service.rst


Application-level protocols
###########################


Many protocols have been defined for networked applications. In this section, we describe some of the important applications that are used on the Internet. We first explain the domain name systems that enables hosts to be identified by human-friendly names instead of the IPv4 or IPv6 addresses that are used by the network. Then we describe the operation of electronic mail, one of the first killer applications on the global Internet and the main protocol used on world wide web. In the last section, we show how simple networked clients and servers can be written in python_ .

.. include:: dns.rst

.. include:: email.rst

.. include:: http.rst


Writing simple networked applications
#####################################


.. include:: socket.rst


Summary
#######

.. for DNS mention security as well and extensions for DNSSEC
.. for POP, the need for much stronger authentication
.. for SMTP the problems caused by spam and so on
.. for HTTP lots of information to be added, mention apache, mention a simple httpd server
.. time http://tf.nist.gov/service/its.htm




.. Today, Napster does not work anymore as explained due to copyright violations reasons.

.. One of the most efficient file transfer protocol used today is Bittorrent. Bittorrent also divides files in blocks and allows files to be downloaded from several nodes at the same time. This provides good redundancy in case of node/link failures, but also allows an efficient utilisation of the available link bandwidth by using uncongested paths (the node with the highest bandwidth will automatically serve blocks faster than a congested node). A Bittorrent node will not necessarily receive blocks in sequence. Furthermore, to ensure that all Bittorrent users contribute to the system, Bittorrent implementations apply the tit-for-tat principle which implies that once a node has received a block, it must serve this block to other nodes before being allowed to download new blocks.

.. Additional information about the Bittorrent protocol may be found i

.. include:: ../links.rst


.. include:: exercises/ex-application.rst


.. rubric:: Footnotes

.. [#fhtonl] For example, the :manpage:`htonl(3)` (resp. :manpage:`ntohl(3)`) function the standard C library converts a 32-bits unsigned integer from the byte order used by the CPU to the network byte order (resp. from the network byte order to the CPU byte order). Similar functions exist in other programming languages.

.. [#fhosts] The :term:`hosts.txt` file is not maintained anymore. The snapshot retrieved on April 15th, 1984 is available from http://ftp.univie.ac.at/netinfo/netinfo/hosts.txt



.. [#fdnstimeline] See http://www.donelan.com/dnstimeline.html for a time line of DNS related developments. 

.. [#fidn] This specification evolved later to support domain names written by using other character sets than us-ASCII :rfc:`3490`. This extension is important to support other languages than English, but a detailed discussion is outside the scope of this document.

.. [#ftld] The official list of top-level domain names is maintained by IANA_ at http://data.iana.org/TLD/tlds-alpha-by-domain.txt Additional information about these domains may be found at http://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

.. [#froot] A copy of the information maintained by each root nameserver is available at http://www.internic.net/zones/root.zone

.. [#frootv6] Until February 2008, the root DNS servers only had IPv4 addresses. IPv6 addresses were added to the root DNS servers slowly to avoid creating problems as discussed in http://www.icann.org/en/committees/security/sac018.pdf In 2010, several DNS root servers are still not reachable by using IPv6. 

.. [#fnamed.root] The current list of the IP addresses of the root nameservers is maintained at http://www.internic.net/zones/named.root . These IP addresses are stable and root nameservers seldom change their IP addresses. DNS resolvers must however maintain an up-to-date copy of this file. 

.. [#fdozen] There are currently 13 root servers. In practice, some of these root servers are themselves implemented as a set of distinct physical servers. See http://www.root-servers.org/ for more information about the physical location of these servers. 

.. [#f8888] Some DNS resolvers allow any host to send queries. OpenDNS_ and GoogleDNS_ are example of open resolvers.

.. [#femailheaders] The list of all standard email header lines may be found at http://www.iana.org/assignments/message-headers/message-header-index.html

.. [#fsmtpauth] During the last years, many Internet Service Providers, campus and enterprise networks have deployed SMTP extensions :rfc:`4954` on their MSAs. These extensions for the MUAs to be authenticated before the MSA accepts an email message from the MUA. 

.. [#fdot] This implies that a valid email message cannot contain a line with one dot followed by `CR` and `LF`. If a user types such a line in an email, his email client will automatically add a space character before or after the dot when sending the message over SMTP.

.. [#fapop] :rfc:`1939` defines another authentication scheme that is not vulnerable to such attackers.

.. [#furilist] The list of standard URI schemes is maintained by IANA_ at http://www.iana.org/assignments/uri-schemes.html

.. [#ffavicon] Favorite icons are small icons that are used to represent web servers in the toolbar of Internet browsers. Microsoft added this feature in their browsers without taking into account the W3C standards. See http://www.w3.org/2005/10/howto-favicon for a discussion on how to cleanly support such favorite icons.

