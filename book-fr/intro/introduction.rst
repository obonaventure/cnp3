.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

============
Introduction
============

.. comment:: Second paragraph, first sentence: "Recent estimations...". Suggestion:"Recent estimations have shown continuing growth for over 20 years of the number of hosts connected to the internet". 
.. comment:: First paragraph, third sentence: "In the early 1960s...", is it meant to be "Donald Davies AND Joseph Licklider" or keep the "or"?

.. comment:: Translation by vvandens

Lorsque les premiers ordinateurs furent construits durant la seconde guerre mondiale, ils étaient extrêmement coûteux, et isolés.  Cependant, après vingt ans, suite à la baisse des prix, de premières expériences furent imaginées pour connecter les ordinateurs ensemble.  Au début des années 60, des chercheurs tels que `Paul Baran`_, `Donald Davies`_ ou `Joseph Licklider`_ publièrent chacun de leur côté les premiers articles décrivant l'idée d'un réseau informatique [Baran]_ [Licklider1963]_ . Etant donné le coût des ordinateurs, les partager à travers une grande distance était une idée intéressante.  Aux Etats-Unis, l':term:`ARPANET` débuta en 1969, et vécu jusqu'au milieu des années 80 [LCCD09]_. En France, `Louis Pouzin`_ développa le réseau Cyclades [Pouzin1975]_. D'autres réseaux de recherche ont été construits durant les années 70 [Moore]_. A ce moment, les industries informatique et des télécommunications commencèrent à s'intéresser aux réseaux informatiques.  L'industrie des télécoms paria sur X25_.  L'industrie informatique prit une approche complètement différente en concevant des réseaux locaux (LAN, Local Area Network.  Beaucoup de technologies LAN telles que Ethernet ou Token Ring furent conçues à cette époque.  Durant les années 80, le besoin d'interconnecter de plus en plus d'ordinateurs poussa les vendeurs d'ordinateurs à développer leur propre suite de protocoles réseaux.  Xerox développa [XNS]_ , DEC choisit DECNet [Malamud1991]_ , IBM dévelopa SNA [McFadyen1976]_ , Microsoft introduisit NetBIOS [Winston2003]_ , Apple paria sur Appletalk [SAO1990]_, etc. Dans la communauté de la recherche, ARPANET fut remplaçé par TCP/IP [LCCD09]_ , et l'implémentation de référence fut développé dans BSD Unix [McKusick1999]_. Les université qui utilisaient déjà Unix pouvaient donc adopter facilement TCP/IP, et les vendeurs de stations Unix tels que Sun ou Silicon Graphics inclurent TCP/IP dans leur variante de Unix.  En parallèle, l':term:`ISO`, avec le soutien des gouvernements, travailla sur une suite de protocoles réseaux ouverte.  Finalement, TCP/IP devint le standard de facto, et fut utilisé au delà de la communauté de la recherche.  Durant les années 90 et au début des années 2000, la croissance de l'utilisation de TCP/IP continua, et les protocoles propriétaires sont aujourd'hui rarement utilisés.  Comme le montre la figure ci-dessous, qui fournit une estimation du nombre d'hôtes attachés à l'Internet, ce dernier a subit une énorme croissance durant les vingt dernières années.  

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

Une autre classification des réseaux informatiques est basée sur leur topologie physique. Dans les figures suivantes, les liens physiques sont représentés par des lignes tout en boîtes montrent ordinateurs ou d'autres types d'équipement de réseau.

Les réseaux informatiques sont utilisés pour permettre à plusieurs hôtes d'échanger des informations entre eux. Pour permettre à n'importe quel hôte d'envoyer des messages à un autre hôte dans le réseau, la solution la plus simple est de les organiser comme un plein filet, avec un lien direct et spécifique entre chaque paire d'hôtes. Une telle topologie physique est parfois utilisé, en particulier lorsque des performances élevées et une redondance élevée est nécessaire pour un petit nombre d'hôtes. Cependant, il présente deux inconvénients majeurs:

- Pour un réseau contenant `n` hôtes, chaque hôte doit avoir `n-1` interfaces physiques. Dans la pratique, le nombre d'interfaces physiques sur un nœud de limiter la taille d'un réseau complet à mailles qui peut être construit
- Pour un réseau contenant `n` hôtes,:math: `\frac {n \times (n-1)} {2}` liens sont nécessaires. Cela est possible quand il y a quelques noeuds dans la même chambre, mais rarement quand ils sont situés à plusieurs kilomètres en dehors

.. figure:: svg/fullmesh.*
   :align: center
   :scale: 50

	Un réseau maillé complet

La deuxième organisation physique possible, qui est également utilisé dans les ordinateurs à connecter des cartes d'extension différents, est le bus. Dans un réseau de bus, tous les hôtes sont attachés à un support partagé, généralement un câble à travers une seule interface. Lorsque un hôte envoie un signal électrique sur le bus, le signal est reçu par tous les hôtes connectés au bus. Un inconvénient de bus réseaux est que, si le bus est physiquement coupé, puis le réseau est divisé en deux réseaux isolés. Pour cette raison, les réseaux de bus sont parfois considérés comme difficiles à exploiter et à entretenir, surtout lorsque le câble est long et il y a beaucoup d'endroits où il peut se briser. Une telle topologie de bus en ligne a été utilisé dans les réseaux Ethernet début.


.. figure:: svg/bus.*
   :align: center
   :scale: 50 

 Un réseau organisé comme un bus

Une troisième organisation d'un réseau informatique est une topologie en étoile. Dans un tel topologies, les hôtes disposent d'une interface physique unique et il y a un lien physique entre chaque hôte et le centre de l'étoile. Le nœud au centre de l'étoile peut être soit une pièce d'équipement qui amplifie un signal électrique, ou un dispositif actif, comme une pièce d'équipement qui comprend le format des messages échangés par l'intermédiaire du réseau. Bien sûr, l'échec du nœud central implique la défaillance du réseau. Toutefois, si un lien physique échoue (par exemple parce que le câble a été coupé), puis un seul nœud est déconnecté du réseau. Dans la pratique, en forme d'étoile réseaux sont plus faciles à exploiter et à entretenir que le bus en forme de réseaux. De nombreux administrateurs réseau apprécieront également le fait qu'ils peuvent contrôler le réseau à partir d'un point central. Administré à partir d'une interface Web, ou à travers une connexion à la console-like, le centre de l'étoile est un bon point de contrôle (activation ou la désactivation des dispositifs) et un point d'observation excellente (les statistiques d'utilisation).

.. figure:: svg/star.*
   :align: center
   :scale: 50 

   Un réseau organisé comme une étoile



Une quatrième organisation physique d'un réseau est la topologie en anneau. Comme l'organisation de bus, chaque hôte dispose d'une interface physique unique de le connecter à l'anneau. Tout signal envoyé par un hôte sur l'anneau sera reçu par tous les hôtes connectés à l'anneau. D'un point de vue de redondance, un seul anneau n'est pas la meilleure solution, que le signal se déplace dans une seule direction sur l'anneau; donc si l'un des liens qui composent l'anneau est coupé, l'ensemble du réseau échoue. Dans la pratique, ces anneaux ont été utilisés dans les réseaux locaux, mais ils sont maintenant souvent remplacées par des réseaux en forme d'étoile. Dans les réseaux métropolitains, les anneaux sont souvent utilisés pour interconnecter de multiples endroits. Dans ce cas, deux liens parallèles, composées de câbles différents, sont souvent utilisés pour la redondance. Avec un tel double anneau, quand un anneau échoue tout le trafic peut être rapidement passé à l'autre bague.


.. figure:: svg/ring.*
   :align: center
   :scale: 50 

   Un réseau organisé comme une bague

Une cinquième organisation physique d'un réseau est l'arbre. Ces réseaux sont généralement utilisés lorsque un grand nombre de clients doit être connecté d'une manière très rentable. Les réseaux câblés sont souvent organisées comme des arbres.

.. figure:: svg/tree.*
   :align: center
   :scale: 50 

   A network organised as a Tree
   
Dans la pratique, la plupart des réseaux réels combiner une partie de ces topologies. Par exemple, un réseau de campus peut être organisé comme un anneau entre les bâtiments principaux, tandis que les petits bâtiments sont attachés comme un arbre ou une étoile aux bâtiments importants. Ou un réseau ISP peut avoir un maillage complet de dispositifs dans le coeur de son réseau, et des arbres pour se connecter les utilisateurs distants.


.. comment:: It feels like there is something missing in the following sentence.. necessary for the network to what? function? operate? for the network to be created?

Tout au long de ce livre, notre objectif sera de comprendre les protocoles et les mécanismes qui sont nécessaires pour un réseau tel que celui illustré ci-dessous.


.. figure:: svg/internetwork.*
   :align: center
   :scale: 75

   A simple internetwork

La figure ci-dessus illustre un réseau d'interconnexion, à savoir un réseau qui interconnecte les réseaux d'autres. Chaque réseau est illustré comme une ellipse contenant quelques appareils. Nous allons vous expliquer tout au long du livre, les différents types de dispositifs et de leurs rôles respectifs permettant à tous les hôtes d'échanger des informations. Ainsi que cela, nous allons discuter de la façon dont les réseaux sont interconnectés, et les règles qui guident ces interconnexions. Nous allons également analyser la façon dont le bus, anneau et maillage topologies sont utilisées pour construire des réseaux réels.



Le dernier point de la terminologie dont nous devons discuter est les modes de transmission. Lors de l'échange d'informations à travers un réseau, nous avons souvent la distinction entre trois modes de transmission. Dans la transmission TV et radio,: terme: `émission` est souvent utilisé pour indiquer une technologie qui envoie un signal vidéo ou la radio à tous les récepteurs dans une zone géographique donnée. Diffusion est parfois utilisé dans les réseaux informatiques, mais uniquement dans les réseaux locaux où le nombre de bénéficiaires est limité.

Le premier mode de transmission et la plus répandue est appelée :term: `unicast. Dans le mode de transmission point à point, les informations sont envoyées par un expéditeur à un récepteur. La plupart des applications Internet d'aujourd'hui reposent sur le mode de transmission unicast. L'exemple ci-dessous montre un réseau avec deux types de dispositifs: les machines (dessiné comme les ordinateurs) et les nœuds intermédiaires (établi en cubes). L'échange d'informations par l'intermédiaire d'Hôtes des noeuds intermédiaires. Dans l'exemple ci-dessous, lorsque l'hôte `S` utilise unicast pour envoyer des informations, il l'envoie par l'intermédiaire de trois nœuds intermédiaires. Chacun de ces nœuds reçoit les informations de son noeud en amont ou de l'hôte, puis les processus et la transmet à son nœud en aval ou de l'hôte. C'est ce qu'on appelle `store and forward` et nous verrons plus tard que ce concept est un élément clé dans les réseaux informatiques.

.. figure:: svg/unicast.*
   :align: center
   :scale: 50

   La transmission unicast

Un deuxième mode de transmission est la suivante: durée: `mode multicast de transmission`. Ce mode est utilisé lorsque la même information doit être envoyée à un ensemble de destinataires. Il a d'abord été utilisés dans les LAN, mais est devenu plus tard pris en charge dans les réseaux étendus. Quand un expéditeur utilise la multidiffusion d'envoyer des informations à `n` récepteurs, l'expéditeur envoie un seul exemplaire de l'information et les nœuds du réseau dupliquer ces informations chaque fois que nécessaire, afin qu'il puisse atteindre tous les bénéficiaires appartenant au groupe de destination.
   

.. figure:: svg/multicast.*
   :align: center
   :scale: 50 

   La transmission multicast

Pour comprendre l'importance de la transmission multicast, pensez à la source `S` qui envoie la même information à destinations `A`, `C` et `e`. Avec unicast, la même information passe trois fois sur les nœuds intermédiaires `1` et `2` et deux fois sur le nœud `4`. Il s'agit d'un gaspillage de ressources sur les nœuds intermédiaires et sur les liens entre eux. Avec la transmission multicast, l'hôte `S` envoie les informations vers le noeud '1 'que transmet en aval vers le noeud `2`. Ce nœud crée une copie de l'information reçue et envoie une copie directement à l'hôte `E` et l'autre en aval de nœud `4`. Lors de la réception de l'information, noeud `4` produit une copie et transmet un à noeud `A` et une autre vers le noeud `C`. Merci à la multidiffusion, la même information peut atteindre un grand nombre de récepteurs, tout en étant envoyé une seule fois sur chaque lien.

Le mode de transmission est la dernière :term: le mode `anycast de transmission`. Il a été initialement défini dans :rfc:`1542`. Dans ce mode de transmission, un ensemble de récepteurs est identifié. Quand une source envoie des informations vers l'ensemble de ces récepteurs, le réseau veille à ce que l'information est livrée à `un` récepteur qui appartient à cet ensemble. Habituellement, le récepteur le plus proche de la source est celle qui reçoit les informations envoyées par cette source particulière. Le mode de transmission anycast est utile pour assurer la redondance, comme lorsque l'un des récepteurs échoue, le réseau veillera à ce que l'information sera remis à un autre récepteur appartenant au même groupe. Cependant, dans la pratique soutenir le mode de transmission anycast peut être difficile.

.. figure:: svg/anycast.*
   :align: center
   :scale: 50 

   Transmission anycast

Dans l'exemple ci-dessus, les trois hôtes marqués `*` font partie du groupe anycast même. Lorsque l'hôte `S` envoie des informations à ce groupe anycast, le réseau assure qu'il atteigne l'un des membres du groupe anycast. Les lignes pointillées indiquent une livraison possible via des noeuds de '1 ', '2 `et` 4 `. Une transmission anycast ultérieure de l'hôte `S` au groupe anycast même pourrait atteindre l'hôte attaché au noeud intermédiaire `3` comme le montre la ligne de plaine. Une transmission anycast atteint un membre du groupe anycast qui est choisi par le réseau en fonction des conditions actuelles du réseau.
.. rubric:: Footnotes


.. [# fopen] Ouvrir en termes ISO était en contraste avec les suites de protocoles propriétaires dont les spécifications ne fut pas toujours accessibles au public. Le gouvernement des États-Unis, même mandaté l'utilisation des protocoles OSI (voir: rfc:`1169`), mais ce n'était pas suffisant pour encourager tous les utilisateurs de passer à la suite du protocole OSI qui a été considéré par beaucoup comme trop complexe par rapport à d'autres suites de protocole .

.. [# finterplanetary] Dans ce livre, nous nous concentrons sur les réseaux qui sont utilisés sur Terre. Ces réseaux incluent parfois des liaisons par satellite. Outre les technologies de réseau qui sont utilisés sur Terre, les chercheurs développent des techniques de mise en réseau qui pourraient être utilisés entre les nœuds situés sur des planètes différentes. Une telle Internet Inter planétaire nécessite des techniques différentes de celles présentées dans ce livre. Voir: rfc:`4838` et les références qui s'y trouvent pour des informations sur ces techniques.
.. .. include:: services-protocols.rst
.. .. include:: referencemodels.rst
.. .. include:: organisation.rst


.. include:: ../links.rst


