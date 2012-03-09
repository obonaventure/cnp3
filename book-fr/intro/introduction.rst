.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

============
Introduction
============

.. comment:: Second paragraph, first sentence: "Recent estimations...". Suggestion:"Recent estimations have shown continuing growth for over 20 years of the number of hosts connected to the internet". 
.. comment:: First paragraph, third sentence: "In the early 1960s...", is it meant to be "Donald Davies AND Joseph Licklider" or keep the "or"?

.. comment:: Translation by vvandens

Lorsque les premiers ordinateurs furent construits durant la seconde guerre mondiale, ils étaient extrêmement coûteux, et isolés.  Cependant, après vingt ans, suite à la baisse des prix, de premières expériences furent imaginées pour connecter les ordinateurs ensemble.  Au début des années 60, des chercheurs tels que `Paul Baran`_, `Donald Davies`_ ou `Joseph Licklider`_ publièrent chacun de leur côté les premiers articles décrivant l'idée d'un réseau informatique [Baran]_ [Licklider1963]_ . Etant donné le coût des ordinateurs, les partager à travers une grande distance était une idée intéressante.  Aux Etats-Unis, l':term:`ARPANET` débuta en 1969, et vécu jusqu'au milieu des années 80 [LCCD09]_. En France, `Louis Pouzin`_ développa le réseau Cyclades [Pouzin1975]_. D'autres réseaux de recherche ont été construits durant les années 70 [Moore]_. A ce moment, les industries informatique et des télécommunications commencèrent à s'intéresser aux réseaux informatiques.  L'industrie des télécoms paria sur X25_.  L'industrie informatique prit une approche complètement différente en concevant des réseaux locaux (LAN, Local Area Network).  Beaucoup de technologies LAN telles que Ethernet ou Token Ring furent conçues à cette époque.  Durant les années 80, le besoin d'interconnecter de plus en plus d'ordinateurs poussa les vendeurs d'ordinateurs à développer leur propre suite de protocoles réseaux.  Xerox développa [XNS]_ , DEC choisit DECNet [Malamud1991]_ , IBM dévelopa SNA [McFadyen1976]_ , Microsoft introduisit NetBIOS [Winston2003]_ , Apple paria sur Appletalk [SAO1990]_, etc. Dans la communauté de la recherche, ARPANET fut remplaçé par TCP/IP [LCCD09]_ , et l'implémentation de référence fut développé dans BSD Unix [McKusick1999]_. Les université qui utilisaient déjà Unix pouvaient donc adopter facilement TCP/IP, et les vendeurs de stations Unix tels que Sun ou Silicon Graphics inclurent TCP/IP dans leur variante de Unix.  En parallèle, l':term:`ISO`, avec le soutien des gouvernements, travailla sur une suite de protocoles réseaux ouverte.  Finalement, TCP/IP devint le standard de facto, et fut utilisé au delà de la communauté de la recherche.  Durant les années 90 et au début des années 2000, la croissance de l'utilisation de TCP/IP continua, et les protocoles propriétaires sont aujourd'hui rarement utilisés.  Comme le montre la figure ci-dessous, qui fournit une estimation du nombre d'hôtes attachés à l'Internet, ce dernier a subit une énorme croissance durant les vingt dernières années.  

.. figure:: png/intro-figures-006-c.png
   :align: center
   :scale: 50 

    Estimation du nombre d'hôtes sur l'Internet


Les estimations récentes du nombre d'hôtes attachés à l'Internet montre une croissance continue depuis plus de vingt ans.  Cependant, bien que le nombre d'hôtes attachés à l'Internet est élevé, il doit être comparé au nombre de téléphones mobiles utilisé aujourd'hui.  De plus en plus de ces téléphones mobiles seront connectés à l'Internet à l'avenir. De plus, grâce à la disponibilité d'implémentations de TCP/IP requérant des ressources limitées, telles que uIP_ [Dunkels2003]_, nous pouvons nous attendre à voir un accroissement des appareils embarqués supportant TCP/IP. 

.. figure:: png/intro-figures-007-c.png
   :align: center
   :scale: 50 

   Estimation du nombre de téléphones mobiles

Avant de regarder de plus près les services fournis par les réseaux informatiques, il est utile de s'accorder sur la terminologie utilisée dans la littérature des réseaux.  Ainsi, les réseaux informatiques sont souvent classés en fonction de la zone géographique qu'ils couvrent : 

- :term:`LAN` : Local Area Network, réseau local qui interconnecte typiquement des hôtes qui sont séparés de maximum quelques dizaines de kilomètres. 
- :term:`MAN` : Metropolitan Area Network, réseau local qui interconnecte typiquement des hôtes qui sont séparés de maximum quelques centaines de kilomètres.
- :term:`WAN` : Wide Area Network, réseau qui interconnecte des hôtes situés n'importe où sur la Terre. [#finterplanetary]_

.. comment:: Google Translate

Une autre classification des réseaux informatiques est basée sur leur topologie physique. Dans les figures suivantes, les liens physiques sont représentés par des lignes tandis que les boîtes montrent des ordinateurs ou d'autres types d'équipement réseau.

Les réseaux informatiques sont utilisés pour permettre à plusieurs hôtes d'échanger des informations entre eux. Pour permettre à n'importe quel hôte d'envoyer des messages à un autre hôte dans le réseau, la solution la plus simple est de les organiser en `full-mesh`, avec un lien direct dédié entre chaque paire d'hôtes. Une telle topologie physique est parfois utilisée, en particulier lorsque des performances élevées sont attendue et que de la redondance est nécessaire dans un réseau contenant un petit nombre d'hôtes. Cependant, il présente deux inconvénients majeurs:

- Pour un réseau contenant `n` hôtes, chaque hôte doit avoir `n-1` interfaces physiques. Dans la pratique, le nombre d'interfaces physiques sur un nœud limitera donc la taille des réseau `full-mesh` possibles.  
- Pour un réseau contenant `n` hôtes,:math: `\frac {n \times (n-1)} {2}` liens sont nécessaires. Cela est possible quand certains noeuds sont situés dans une même pièce, mais rarement quand ils sont situés à plusieurs kilomètres les uns des autres. 

.. figure:: svg/fullmesh.*
   :align: center
   :scale: 50

	Un réseau `full-mesh`

La deuxième organisation physique possible est le `bus`, qui est également utilisée dans les ordinateurs pour connecter différentes cartes d'extensions. Dans un réseau en bus, tous les hôtes sont attachés à un même support, généralement un câble, à travers une seule interface. Lorsque un hôte envoie un signal électrique sur le bus, le signal est reçu par tous les hôtes connectés au bus. Un inconvénient de ce type de réseau est qu'en cas de coupure du bus, le réseau est partitionné en deux sous-réseaux isolés.  Pour cette raison, les réseaux de bus sont parfois considérés comme difficiles à exploiter et à entretenir, surtout lorsque le câble est long et il y a beaucoup d'endroits où il peut se briser. Les premiers réseaux Ethernet utilisaient une topologie en bus. 


.. figure:: svg/bus.*
   :align: center
   :scale: 50 

 Un réseau organisé en bus

La troisième organisation de réseau informatique est la topologie en étoile. Dans une telle topologie, les hôtes disposent d'une interface physique unique et il y a un lien physique entre chaque hôte et le centre de l'étoile. Le nœud au centre de l'étoile peut être soit un équipement qui amplifie le signal électrique, ou un dispositif actif, comprenant le format des messages échangés sur réseau. Bien sûr, une panne du nœud central implique la défaillance de l'entièreté du réseau. Toutefois, si un lien physique tombe en panne (par exemple parce que le câble a été coupé), seul ce noeud est déconnecté du réseau. Dans la pratique, les réseaux en étoile sont plus faciles à exploiter et à entretenir que les réseaux en bus. De nombreux administrateurs réseau apprécient également le fait qu'ils peuvent contrôler le réseau à partir d'un point central. Administré à partir d'une interface Web, ou à travers une connexion type console, le centre de l'étoile est un bon point de contrôle (pour l'activation ou la désactivation des dispositifs) et un excellent point d'observation (pour les statistiques d'utilisation).

.. figure:: svg/star.*
   :align: center
   :scale: 50 

   Un réseau en étoile



La quatrième organisation physique de réseau est la topologie en anneau. Comme l'organisation en bus, chaque hôte dispose d'une interface physique unique le connectant à l'anneau. Tout signal envoyé par un hôte sur l'anneau sera reçu par tous les hôtes connectés à l'anneau. Du point de vue de la redondance, un anneau unique n'est pas la meilleure solution, puisque le signal se déplace dans une seule direction; donc si l'un des liens qui composent l'anneau est coupé, l'ensemble du réseau est en panne. Dans la pratique, ces anneaux ont été utilisés dans les réseaux locaux, mais ils sont maintenant souvent remplacées par des réseaux en forme d'étoile. Dans les réseaux métropolitains, les anneaux sont souvent utilisés pour interconnecter de multiples endroits. Dans ce cas, deux liens parallèles, composées de câbles différents, sont souvent utilisés pour la redondance. Avec un tel double anneau, quand un anneau échoue tout le trafic peut être rapidement passé à l'autre anneau.


.. figure:: svg/ring.*
   :align: center
   :scale: 50 

   Un réseau organisé en anneau

Une cinquième organisation physique d'un réseau est l'arbre. Ces réseaux sont généralement utilisés lorsque un grand nombre de clients doivent être connectés efficacement en optimisant les coûts. Les réseaux de télévision câblés sont souvent organisées en arbres.

.. figure:: svg/tree.*
   :align: center
   :scale: 50 

   Un réseau en arbre
   
Dans la pratique, la plupart des réseaux réels combinent plusieurs de ces topologies. Par exemple, un réseau de campus peut être organisé en anneau entre les bâtiments principaux, tandis que les petits bâtiments sont connectés en arbre ou en étoile aux bâtiments importants. Ou encore, un réseau de fournisseur d'accès internet peut avoir un `full-mesh` dans le coeur de son réseau, et des arbres connecter les utilisateurs distants.


.. comment:: It feels like there is something missing in the following sentence.. necessary for the network to what? function? operate? for the network to be created?

Tout au long de ce livre, notre objectif sera de comprendre les protocoles et les mécanismes qui sont nécessaires pour un réseau tel que celui illustré ci-dessous.


.. figure:: svg/internetwork.*
   :align: center
   :scale: 75

   A simple internetwork

La figure ci-dessus illustre un inter-réseau, à savoir un réseau qui connecte d'autres réseaux ensemble. Chaque réseau est illustré par une ellipse contenant plusieurs appareils. Tout au long du livre, nous allons détailler les différents dispositifs et leurs rôles respectifs dans l'échange d'informations entre hôtes. Nous analyserons également comment les topologies en bus, anneau et en `full-mesh` sont utilisées pour construire les réseaux réels.  

Le dernier point de terminologie à discuter concerne les modes de transmission.  Lors de l'échange d'informations à travers un réseau, nous ferons la distinction entre trois modes de transmission. Dans les transmissions TV et radio, le :terme: `broadcast` est souvent utilisé pour indiquer une technologie qui envoie un signal vidéo ou radio à tous les récepteurs dans une zone géographique donnée. Le broadcast est parfois utilisé dans les réseaux informatiques, mais uniquement dans les réseaux locaux où le nombre de destinataires est limité.

Le premier mode de transmission, et le plus répandu, est appelé :term:`unicast`. Dans ce mode de transmission, les informations sont envoyées par un expéditeur à un destinataire. La plupart des applications Internet d'aujourd'hui reposent sur le mode de transmission unicast. L'exemple ci-dessous montre un réseau avec deux types de dispositifs: des hôtes (représentée par des ordinateurs) et des nœuds intermédiaires (représenté par des cubes). Les hôtes échangent des informations via les noeuds intermédiaires. Dans l'exemple ci-dessous, lorsque l'hôte `S` utilise le mode unicast pour envoyer des informations, il l'envoie via trois nœuds intermédiaires. Chacun de ces nœuds reçoit les informations de son noeud en amont ou de l'hôte émetteur, puis les traite et les transmet au nœud en aval ou à l'hôte de destination. C'est ce qu'on appelle `store and forward` et nous verrons plus tard que ce concept est un élément clé dans les réseaux informatiques.

.. figure:: svg/unicast.*
   :align: center
   :scale: 50

   La transmission unicast

Le deuxième mode de transmission est le :term:`mode de transmission multicast`. Ce mode est utilisé lorsque la même information doit être envoyée à un ensemble de destinataires. Il a d'abord été utilisés dans les LAN, mais a été mis en place par après dans des réseaux plus étendus. Quand un expéditeur utilise le multicast pour envoyer des informations à `n` récepteurs, il envoie un exemplaire unique de l'information et les nœuds du réseau dupliquent ces informations chaque fois que nécessaire, afin que le message puisse atteindre tous les bénéficiaires appartenant au groupe de destination.
   

.. figure:: svg/multicast.*
   :align: center
   :scale: 50 

   La transmission multicast

Pour comprendre l'importance de la transmission multicast, considérons une source `S` qui envoie la même information à destination de `A`, `C` et `E`. Avec le mode unicast, la même information passe trois fois sur les nœuds intermédiaires `1` et `2` et deux fois sur le nœud `4`. Il s'agit d'un gaspillage de ressources sur les nœuds intermédiaires et sur les liens qui les relient. Avec la transmission multicast, l'hôte `S` envoie les informations vers le noeud '1', qui le transmet en aval vers le noeud `2`. Ce nœud crée une copie de l'information reçue et envoie une copie directement à l'hôte `E` et l'autre en aval au nœud `4`. Lors de la réception de l'information, le noeud `4` produit à son tour une copie, et transmet l'information aux noeud `A` et `C`. Grâce au mode multicast, la même information peut atteindre un grand nombre de récepteurs, tout en étant envoyée une seule fois sur chaque lien.

Le dernier mode de transmission est le mode :term:`anycast`. Il a été initialement défini dans le :rfc:`1542`. Dans ce mode de transmission, un ensemble de récepteurs est identifié. Quand une source envoie des informations vers l'ensemble de ces récepteurs, le réseau veille à ce que l'information soit livrée à `un` récepteur qui appartienne à cet ensemble. Habituellement, le récepteur le plus proche de la source est celui qui reçoit les informations que cette dernière envoie. Le mode de transmission anycast est utile pour assurer la redondance. Ainsi, lorsqu'un des récepteurs tombe en panne, le réseau veille à ce que l'information soit remise à un autre récepteur du même groupe. Cependant, dans la pratique faire fonctionner le mode de transmission anycast peut se révéler difficile.

.. figure:: svg/anycast.*
   :align: center
   :scale: 50 

   Transmission anycast

Dans l'exemple ci-dessus, les trois hôtes marqués par `*` font partie du même groupe anycast. Lorsque l'hôte `S` envoie des informations à ce groupe anycast, le réseau assure qu'il atteigne l'un des ses membres. Les lignes pointillées indiquent une transmission possible via les noeuds '1 ', '2 `et` 4 `. Une transmission anycast ultérieure de l'hôte `S` au même groupe anycast  pourrait atteindre l'hôte attaché au noeud intermédiaire `3` comme le montre la ligne continue. Une transmission anycast atteint n'importe quel membre du groupe anycast, choisi par le réseau en fonction des conditions du réseau à ce moment.
.. rubric:: Footnotes


.. [# fopen] Un protocole ouvert selon les termes de l'ISO s'opposait à l'époque aux suites de protocoles propriétaires dont les spécifications n'étaient pas toujours accessibles au public. Le gouvernement des États-Unis a même mandaté l'utilisation des protocoles OSI (voir: rfc:`1169`), mais ce ne fut pas suffisant pour encourager tous les utilisateurs d'adopter la suite de protocoles OSI, considéré par beaucoup comme trop complexe par rapport à d'autres suites de protocole .

.. [# finterplanetary] Dans ce livre, nous nous concentrons sur les réseaux qui sont utilisés sur Terre. Ces réseaux incluent parfois des liaisons par satellite. Outre les technologies de réseau utilisés sur Terre, les chercheurs développent des techniques de mise en réseau qui pourraient être utilisés entre des nœuds situés sur des planètes différentes. Une tel Internet inter-planétaire nécessite des techniques différentes de celles présentées dans ce livre. Voir: rfc:`4838` et les références qui s'y trouvent pour des informations sur ce sujet.
.. .. include:: services-protocols.rst
.. .. include:: referencemodels.rst
.. .. include:: organisation.rst


.. include:: ../links.rst


