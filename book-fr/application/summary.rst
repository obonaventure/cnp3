.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



Summary
#######

Dans ce chapitre, nous avons d'abord décrit les modèles client-serveur et pair-à-pair.  Ensuite, nous avons décrit en détails trois importantes familles de protocoles de la couche Application.  L'Internet identifie les hôtes par des adresses 32 ou 128 bits.  Cependant, l'utilisation de ces adresses directement depuis les applications les rendraient difficiles à utiliser par les utilisateurs humains.  Nous avons expliqué comment le DNS permet de faire correspondre des noms à ces adresses.  Nous avons également décrit à la fois le protocole DNS, fonctionnant au dessus d'UDP, et la hiérarchie de nommage.  Nous avons ensuite décrit l'une des plus anciennes applications de l'Internet : le courrier électronique.  Nous avons décrit le format des messages, et expliqué comment le protocole SMTP envoie les messages, et comment les protocoles POP et IMAP permettent aux destinataires de les retrouver depuis leur serveur.  Enfin, nous avons détaillé les protocoles utilisés dans le World Wide Web, en particulier le protocole HTTP (HyperText Transfert Protocol).  



.. for DNS mention security as well and extensions for DNSSEC
.. for POP, the need for much stronger authentication
.. for SMTP the problems caused by spam and so on
.. for HTTP lots of information to be added, mention apache, mention a simple httpd server
.. time http://tf.nist.gov/service/its.htm




.. Today, Napster does not work anymore as explained due to copyright violations reasons.

.. One of the most efficient file transfer protocol used today is Bittorrent. Bittorrent also divides files into blocks and allows files to be downloaded from several nodes at the same time. This provides good redundancy in case of node/link failures, but also allows an efficient utilisation of the available link bandwidth by using uncongested paths (the node with the highest bandwidth will automatically serve blocks faster than a congested node). A Bittorrent node will not necessarily receive blocks in sequence. Furthermore, to ensure that all Bittorrent users contribute to the system, Bittorrent implementations apply the tit-for-tat principle which implies that once a node has received a block, it must serve this block to other nodes before being allowed to download new blocks.

.. Additional information about the Bittorrent protocol may be found i


.. include:: ../links.rst


