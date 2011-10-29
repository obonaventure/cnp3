.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

.. _chapter-application:

=====================
The application Layer
=====================

The Application Layer is the most important and most visible layer in computer networks. Applications reside in this layer and human users interact via those applications through the network. 

In this chapter, we first briefly describe the main principles of the application layer and focus on the two most important application models :  the client-server and the peer-to-peer models. Then, we review in detail two families of protocols that have proved to be very useful in the Internet : electronic mail and the protocols that allow access to information on the world wide web. We also describe the Domain Name System that allows humans to use user-friendly names while the hosts use 32 bits or 128 bits long IP addresses. 

.. include:: principles.rst

.. include:: transport-service.rst


Application-level protocols
###########################


Many protocols have been defined for networked applications. In this section, we describe some of the important applications that are used on the Internet. We first explain the Domain Name System (DNS) that enables hosts to be identified by human-friendly names instead of the IPv4 or IPv6 addresses that are used by the network. Then, we describe the operation of electronic mail, one of the first killer applications on the global Internet, and the protocols used on world wide web. 

.. In the last section, we show how simple networked clients and servers can be written in python_ .

.. include:: dns.rst

.. include:: email.rst

.. include:: http.rst



.. include:: socket.rst


Summary
#######

In this chapter, we began by describing the client-server and peer-to-peer models. We then described, in detail, three important families of protocols in the application layer.
The Internet identifies hosts by using 32 bits IPv4 or 128 bits IPv6. However, using these addresses directly inside applications would be difficult for the humans that use them. We have explained how the Domain Name System allows the mapping of names to corresponding addresses. We have described both the DNS protocol that runs above UDP and the naming hierarchy. We have then discussed one of the oldest applications on the Internet : electronic mail. We have described the format of email messages and described the SMTP protocol that is used to send email messages as well as the POP protocol that is used by email recipients to retrieve their email messages from their server. Finally, we have explained the protocols that are used in the world wide web and the HyperText Transfer Protocol in particular. 


.. for DNS mention security as well and extensions for DNSSEC
.. for POP, the need for much stronger authentication
.. for SMTP the problems caused by spam and so on
.. for HTTP lots of information to be added, mention apache, mention a simple httpd server
.. time http://tf.nist.gov/service/its.htm




.. Today, Napster does not work anymore as explained due to copyright violations reasons.

.. One of the most efficient file transfer protocol used today is Bittorrent. Bittorrent also divides files into blocks and allows files to be downloaded from several nodes at the same time. This provides good redundancy in case of node/link failures, but also allows an efficient utilisation of the available link bandwidth by using uncongested paths (the node with the highest bandwidth will automatically serve blocks faster than a congested node). A Bittorrent node will not necessarily receive blocks in sequence. Furthermore, to ensure that all Bittorrent users contribute to the system, Bittorrent implementations apply the tit-for-tat principle which implies that once a node has received a block, it must serve this block to other nodes before being allowed to download new blocks.

.. Additional information about the Bittorrent protocol may be found i


.. include:: exercises/ex-application.rst

.. include:: ../links.rst


