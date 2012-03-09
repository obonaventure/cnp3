.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Principles
##########

Il y a deux modèles important d'organisation d'applications distribuées : Le modèle Client-Serveur, et le modèle Pair-à-Pair.  Le premier, et le plus ancien, est le modèle client-serveur.  Dans ce modèle, un serveur fournit des services aux clients qui échangent de l'information avec lui.  Ce modèle est donc asymétrique : les clients envoient des requêtes et les serveurs exécutent des actions et renvoient des réponses.  Ceci est illustré dans la figure ci-dessous. 


.. figure:: png/app-fig-001-c.png
   :align: center
   :scale: 50 

   Le modèle client-serveur

Le modèle client-serveur fut le premier à être utilisé pour développer des applications réseaux.  Ce modèle dérive naturellement des mainframes et des mini-ordinateurs qui furent les seuls machines utilisées en réseaux jusque dans les années 80.  Un mini-ordinateur est un système multi-utilisateur utilisé par des dizaines, voire plus, d'utilisateurs en même temps.  Chaque utilisateur interagit avec le mini-ordinateur en utilisant un terminal.  Ces terminaux étaient essentiellement un clavier, un écran et un câble directement connectés au mini-ordinateur.  

Il y a de nombreux types de serveurs, et de nombreux types de clients.  Ainsi, un serveur Web fournit de l'information en réponse aux requêtes envoyées par ses clients.  Un serveur d'impression imprime les documents envoyés par les clients.  Un serveur mail transmettra les messages emails à leur destinataire, tandis qu'un serveur de musique délivrera la musique requise par le client.  
Du point de vue du développeur de l'application, les applications clients et serveurs échangent des messages directement, mais en pratique, ces messages sont échangés en passant par les couches réseau inférieures (les flèches verticales dans la figure ci-dessus).  Dans ce chapitre, nous nous concentrerons sur ces échanges horizontaux de messages. 

Les applications réseau n'échangent pas leurs messages n'importe comment.  Pour s'assurer que le serveur soit capable de comprendre les requêtes d'un client, et que le client est à même de comprendre les réponses du serveur, ils doivent se mettre d'accord sur un ensemble de règles syntaxiques et sémantiques.  Ces règles définissent le format des messages qu'ils échangent, ainsi que l'ordre dans lequel ils sont échangés.  Un tel ensemble de règles est appelé un `protocole`.  

Un `protocole de niveau applicatif` est similaire à une conversation structurée entre humains.  Supposons qu'Alice désire connaître l'heure, mais n'a pas de montre.  Si Bob passe à proximité, la conversation suivante pourrait se produire : 


 - Alice : `Bonjour`
 - Bob : `Bonjour`
 - Alice : `Quelle heure est-il ?`
 - Bob : `11:55`
 - Alice : `Merci
 - Bob : `De rien`  

Une telle conversation est possible pour peu qu'Alice et Bob parlent le même langage.  Si Alice rencontre Tchang qui ne parle que le chinois, elle ne sera pas en mesure de lui demander l'heure.  Une conversation entre humains peut être encore plus complexe.  Par exemple, supposons que Bob est un garde de sécurité dont le job est de ne permettre qu'à des agents secrets fiables d'entrer dans une salle de réunion.  Si tous les agents connaissent un mot de passe secret, la conversation entre Bob et Trudy pourrait être comme suit : 

 - Bob : `Quel est le mot de passe ?`
 - Trudy : `1234`
 - Bob : `C'est correct, vous pouvez entrer`
Si Alice désire entrer dans la salle de réunion, mais ne connaît pas le mot de passe, la conversation donnera : 

 - Bob : `Quel est le mot de passe ?`
 - Alice : `3.1415`
 - Bob : `Ce n'est pas correct.`

Les conversations humaines peuvent être très formelles, comme par exemple lorsque des soldats communiquent avec leur hiérarchie, ou informelles, lors de discussion entre amis.  Les ordinateurs qui communiquent s'apparentent plus aux soldats, et requièrent des règles bien-définies pour assurer un échange d'information correct.  Il y a deux types de règles qui définissent comment l'information peut être échangée entre ordinateurs : 

- Les règles syntaxiques, qui définissent précisément le format des messages échangés.  Puisque les ordinateurs ne manipulent que des bits, les règles syntaxiques spécifient comment l'information est encodé sous forme de suite de bits.  
- L'organisation du flux d'information.  Pour beaucoup d'applications, le flux d'informations doit être structuré, et il doit y avoir des relations de priorité entre les différents types d'informations.  Dans l'exemple de l'heure ci-dessus, Alice doit saluer Bob avant de lui poser une question.  Alice ne commencerait pas par lui demander l'heure avant de le saluer.  De telles relations d'ordre existent également dans les applications réseau.  Par exemple, un serveur doit recevoir un nom d'utilisateur et un mot de passe valide avant d'accepter des commandes plus complexes de la part de ses clients.

Commençons par discuter des règles syntaxiques.  Nous verrons plus tard comment le flux d'information peut être organisé en analysant des applications réseaux réelles.  


Les protocoles de la couche Application échangent deux types de messages.  Certains protocoles tels que ceux utilisés pour le courrier électroniques échangent des messages exprimés comme des chaînes ou des lignes de caractères.  Comme la couche Transport permet aux hôtes d'échanger des octets, ces protocoles doivent convenir d'une représentation commune des caractères.  La méthode la plus simple pour encoder des caractères consiste à utiliser la table :term:`ASCII` table. Le :rfc:`20` fournit la table ASCII utilisée par de nombreux protocoles sur l'Internet.  Par exemple, cette table définit les représentations binaires suivantes : 

 - `A` : `1000011b` 
 - `0` : `0110000b`
 - `z` : `1111010b`
 - `@` : `1000000b`
 - `espace` : `0100000b`

De plus, la table :term:`ASCII` définit également plusieurs caractères non imprimables ou de contrôle.  Ces caractères ont été conçus pour permettre à une application de contrôler une imprimante ou un terminal.  Ces caractères de contrôles incluent notamment `CR` et `LF`, utilisés pour terminer une ligne, et le caractère `Bell`, qui fait en sorte que le terminal produise un son. 

 - `carriage return` (`CR`) : `0001101b`
 - `line feed` (`LF`) : `0001010b`
 - `Bell`: `0000111b`

The :term:`ASCII` characters are encoded as a seven bits field, but transmitted as an eight-bits byte whose high order bit is usually set to `0`. Bytes are always transmitted starting from the high order or most significant bit.

Most applications exchange strings that are composed of fixed or variable numbers of characters. A common solution to define the character strings that are acceptable is to define them as a grammar using a Backus-Naur Form (:term:`BNF`) such as the Augmented BNF defined in :rfc:`5234`. A BNF is a set of production rules that generate all valid character strings. For example, consider a networked application that uses two commands, where the user can supply a username and a password. The BNF for this application could be defined as shown in the figure below.

.. figure:: pkt/bnf.png
   :align: center
   :scale: 100 

   A simple BNF specification

The example above defines several terminals and two commands : `usercommand` and `passwordcommand`. The `ALPHA` terminal contains all letters in upper and lower case. In the `ALPHA` rule, `%x41` corresponds to ASCII character code 41 in hexadecimal, i.e. capital `A`.  The `CR` and `LF` terminals correspond to the carriage return and linefeed control characters. The `CRLF` rule concatenates these two terminals to match the standard end of line termination. The `DIGIT` terminal contains all digits. The `SP` terminal corresponds to the white space characters. The `usercommand` is composed of two strings separated by white space. In the ABNF rules that define the messages used by Internet applications, the commands are case-insensitive. The rule `"user"` corresponds to all possible cases of the letters that compose the word between brackets, e.g. `user`, `uSeR`, `USER`, `usER`, ... A `username` contains at least one letter and up to 8 letters. User names are case-sensitive as they are not defined as a string between brackets. The `password` rule indicates that a password starts with a letter and can contain any number of letters or digits. The white space and the control characters cannot appear in a `password` defined by the above rule.

Besides character strings, some applications also need to exchange 16 bits and 32 bits fields such as integers. A naive solution would have been to send the 16- or 32-bits field as it is encoded in the host's memory. Unfortunately, there are different methods to store 16- or 32-bits fields in memory. Some CPUs store the most significant byte of a 16-bits field in the first address of the field while others store the least significant byte at this location. When networked applications running on different CPUs exchange 16 bits fields, there are two possibilities to transfer them over the transport service :

  - send the most significant byte followed by the least significant byte
  - send the least significant byte followed by the most significant byte

The first possibility was named  `big-endian` in a note written by Cohen [Cohen1980]_ while the second was named `little-endian`. Vendors of CPUs that used `big-endian` in memory insisted on using `big-endian` encoding in networked applications while vendors of CPUs that used `little-endian` recommended the opposite. Several studies were written on the relative merits of each type of encoding, but the discussion became almost a religious issue [Cohen1980]_. Eventually, the Internet chose the `big-endian` encoding, i.e. multi-byte fields are always transmitted by sending the most significant byte first, :rfc:`791` refers to this encoding as the :term:`network-byte order`. Most libraries [#fhtonl]_ used to write networked applications contain functions to convert multi-byte fields from memory to the network byte order and vice versa. 

Besides 16 and 32 bit words, some applications need to exchange data structures containing bit fields of various lengths. For example, a message may be composed of a 16 bits field followed by eight, one bit flags, a 24 bits field and two 8 bits bytes. Internet protocol specifications will define such a message by using a representation such as the one below. In this representation, each line corresponds to 32 bits and the vertical lines are used to delineate fields. The numbers above the lines indicate the bit positions in the 32-bits word, with the high order bit at position `0`. 

.. figure:: pkt/message.png
   :align: center
   :scale: 100 

   Message format

The message mentioned above will be transmitted starting from the upper 32-bits word in network byte order. The first field is encoded in 16 bits. It is followed by eight one bit flags (`A-H`), a 24 bits field whose high order byte is shown in the first line and the two low order bytes appear in the second line followed by two one byte fields. This ASCII representation is frequently used when defining binary protocols. We will use it for all the binary protocols that are discussed in this book.

We will discuss several examples of application-level protocols in this chapter.

.. introduce ipv4 and ipv6 addresses
.. mention names very early, they are important

.. index:: peer-to-peer

The peer-to-peer model
======================

The peer-to-peer model emerged during the last ten years as another possible architecture for networked applications. In the traditional client-server model, hosts act either as servers or as clients and a server serves a large number of clients. In the peer-to-peer model, all hosts act as both servers and clients and they play both roles. The peer-to-peer model has been used to develop various networked applications, ranging from Internet telephony to file sharing or Internet-wide filesystems. A detailed description of peer-to-peer applications may be found in [BYL2008]_. Surveys of peer-to-peer protocols and applications may be found in [AS2004]_ and [LCP2005]_.

.. principle distinction between server and client does not exist anymore
.. focus will be on file distribution, but there are various other usages
.. centralised p2p, like napster
.. unstructured p2P like gnutella or freenet
.. structured like chord as example

.. Surveys : 

.. Chord : [SMKKB2001]_


.. The peer-to-peer model 


.. rubric:: Footnotes

.. [#fhtonl] For example, the :manpage:`htonl(3)` (resp. :manpage:`ntohl(3)`) function the standard C library converts a 32-bits unsigned integer from the byte order used by the CPU to the network byte order (resp. from the network byte order to the CPU byte order). Similar functions exist in other programming languages.

.. include:: /links.rst
