The Application Layer
=====================

The Application Layer is the most important and most visible layer in computer. Applications reside in this layer and human users interact via those applications through the network. 

In this chapter, we first briefly describe the main principles of the application layer and focus on the two most important models :  the client-server model and the peer-to-peer models. Then, we review in details two families of protocols that have proved to be very useful in networks such as the Internet : electronic mail and the protocols that allow to access information on the world wide web. We also describe the Domain Name System that allows humans to use user-friendly names while the hosts use IP addresses. Finally, we mention some of the practical problems that arise with these protocols in today's Internet.

Principles
----------

The are two important models to organise a networked application. The first and oldest model is the client-server model. In this model, a server provides services to clients that exchange information with it. This model is highly assymetrical : clients send requests and servers perform actions and provide responses. It is illsutrated in the figure below.


.. figure:: png/intro-figures-007-c.png
   :align: center
   :scale: 50 

   Host count GSM

 The second model is the peer-to-peer model. It appaered recently as another way to organise Internet applications. 

The client-server model
.......................

The client-server model was the first model to be used to develop networked applications. This model comes naturally from the mainframes and minicomputers that were the only networked computers used until the 1980s. A minicomputer_ is a multi-user system that was used by tens or more users at the same time. Each user was interacting via the minicomputer by using a terminal. Those terminals, were mainly a screen, a keyboard and a cable connected to the minicomputer.


The peer-to-peer model
......................


Protocols
---------



The Domain Name System
.......................


Electronic mail
...............


describe architecture

The Simple Mail Transfert Protocol
..................................

smtp :rfc:`821

describe protocol

MIME :rfc:`2045` :rfc:`2046

The Post Office Protocol
........................

The Post Office Protocol is defined in :rfc:`1939`

The IMAP :rfc:`2060`

webmail (mainly implemantions, no standard)


The HyperText Transfert Protocol
................................


file transfert : ftp : :rfc:`959

urls : :rfc:`1738` see also http://www.w3.org/Addressing

html http://www.w3.org/MarkUp

http 1.0 : :rfc:`1945`

http 1.1 :rfc:`2616






Practice
--------


discuss briefly various implementations and mention the evolution of the protocols


for DNS mention security as well and extensions for DNSSEC
for POP, the need for much stronger authentication
for SMTP the problems caused by spam and so on
for HTTP lots of information to be added, mention apache, mention a simple httpd server



Historical notes
----------------

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


.. include:: ../links.rst