=====================
The Application Layer
=====================

The Application Layer is the most important and most visible layer in computer. Applications reside in this layer and human users interact via those applications through the network. 

In this chapter, we first briefly describe the main principles of the application layer and focus on the two most important models :  the client-server model and the peer-to-peer models. Then, we review in details two families of protocols that have proved to be very useful in networks such as the Internet : electronic mail and the protocols that allow to access information on the world wide web. We also describe the Domain Name System that allows humans to use user-friendly names while the hosts use IP addresses. Finally, we mention some of the practical problems that arise with these protocols in today's Internet.

Principles
##########

The are two important models to organise a networked application. The first and oldest model is the client-server model. In this model, a server provides services to clients that exchange information with it. This model is highly assymetrical : clients send requests and servers perform actions and provide responses. It is illsutrated in the figure below.


.. figure:: fig/app-fig-001-c.png
   :align: center
   :scale: 50 

   The client-server model


The second model is the peer-to-peer model. It appaered recently as another way to organise Internet applications. In the peer-to-peer model, all

The client-server model
=======================

The client-server model was the first model to be used to develop networked applications. This model comes naturally from the mainframes and minicomputers that were the only networked computers used until the 1980s. A minicomputer_ is a multi-user system that was used by tens or more users at the same time. Each user was interacting via the minicomputer by using a terminal. Those terminals, were mainly a screen, a keyboard and a cable connected to the minicomputer.


The peer-to-peer model
======================


Protocols
#########


.. DNS

The Domain Name System
======================


Electronic mail
===============


describe architecture

The Simple Mail Transfert Protocol
----------------------------------

smtp :rfc:`821`

describe protocol

MIME :rfc:`2045` :rfc:`2046`

The Post Office Protocol
------------------------

The Post Office Protocol is defined in :rfc:`1939`

The IMAP :rfc:`2060`

webmail (mainly implementations, no standard)


The HyperText Transfert Protocol
================================

In the early days of the Internet, the network was mainly used for remote terminal access with telnet_, email and file transfert. The default file transfert protocol, ftp, defined in :rfc:`959` was widely used and ftp clients and servers were included in most operating systems.

An ftp client offers a user interface similar to a Unix shell and allows the client to browse the file system on the server and send and retrieve files. ftp servers can be configured in two modes :

 - authenticated : in this mode, the ftp server only accepts users with a valid userid and password. Once authenticated, they can access the files and directories according to their permissions
 - anonymous : in this mode, clients supply the anonymous` anonymous` a special zone of the file system is 

urls : :rfc:`1738` see also http://www.w3.org/Addressing

html http://www.w3.org/MarkUp

http 1.0 : :rfc:`1945`

http 1.1 :rfc:`2616`

Practice
########


discuss briefly various implementations and mention the evolution of the protocols


for DNS mention security as well and extensions for DNSSEC
for POP, the need for much stronger authentication
for SMTP the problems caused by spam and so on
for HTTP lots of information to be added, mention apache, mention a simple httpd server



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
.. include:: ../links.rst