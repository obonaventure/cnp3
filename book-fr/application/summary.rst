.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



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


.. include:: ../links.rst


