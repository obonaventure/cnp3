.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. comment:: Translation by vvandens

Services et protocoles
######################

Un point important à comprendre avant d'étudier les réseaux informatique est la différence entre un *service* et un *protocole*. 

Pour saisir la différence entre les deux, il est utile de partir du monde réel.  La Poste traditionnelle utilise un service dans lequel un facteur délivre des lettres à leurs destinataires.  La Poste définit précisément quels types de lettres (taille, poids, ...) peuvent être transmises par les service postaux.  De plus, le format de l'enveloppe est spécifié (position de l'adresse de l'expéditeur et du destinataire, position du timbre).  Quelqu'un souhaitant envoyer une lettre doit doit déposer la lettre à la Poste, ou bien dans une boîte aux lettres dédiée.  La lettre sera alors collectée et délivrée à son destinataire final.  Notez que le service traditionnel de la Poste ne garantit généralement pas la transmission de chaque lettre en particulier.  Certaines lettres peuvent être perdues, et d'autres sont transmises au mauvais destinataire.  Si une lettre est importante, alors l'expéditeur peut utiliser le service des Recommandés pour s'assurer que la lettre sera correctement transmise.  Certains services postaux fournissent également un service avec accusé de réception, ou un service Express plus rapide que le service normal.  

Dans les réseaux informatique, la notion de service peut être comprise en considérant un réseau informatique, quelle que soit sa taille ou sa complexité, comme une boîte noire qui fournit un service à des `utilisateurs`, comme montré dans la figure ci-dessous.  Les utilisateurs peuvent être des humains, ou bien des processus fonctionnant sur un système informatique.

.. _fig-users:

.. figure:: svg/intro-figures-014-c.*
   :align: center
   :scale: 80 
	
   Utilisateurs et fournisseurs de service

.. index:: adresse

Il existe différent modèles de services dans les réseaux.  Le plus simple est appelé `Service sans connexion`.  Dans un tel service, l'utilisateur spécifie l'adresse source, l'adresse destination, et le message, et les transmet au fournisseur de service.  Ce dernier transmettra ces informations au destinataire.  

.. index:: point d'accès au service

Tout au long de ce livre, nous définirons un service comme un ensemble de fonctionnalités fournies par le système (et ses éléments sous-jacent) à l'utilisateur.  Un utilisateur interagit avec un service à travers un `point d'accès au service`.  Notez que selon la figure ci-dessus, les utilisateurs n'interagissent qu'avec un seul fournisseur de service.  En pratique, le fournisseurs est distribué sur plusieurs hôtes, mais ces détails d'implémentation ne sont pas important pour le moment.  Ces interactions entre un utilisateur et un fournisseur de service sont détaillés dans [X200]_ en utilisant des primitives telles que montrées dans la figure ci-dessous.  Ces primitives sont une représentation abstraite des interactions entre un utilisateur et un fournisseur de services;  En pratique, ces interactions pourraient être implémentées par des appels système par exemple.  

.. figure:: svg/intro-figures-016-c.*
   :align: center
   :scale: 80 

   Les quatre types de primitives

.. index:: primitives de service

Quatre types de primitives sont définies : 

 - `X.request`. Cette primitive corresponds à une requête générée par un utilisateur à un fournisseur de service. 
 - `X.indication`. Cette primitive est générée par le fournisseur réseau et délivrée à l'utilisateur (souvent en relation avec une primitive `X.request` antérieure et distante)
 - `X.response`. Cette primitive est générée par un utilisateur en réponse à une primitive `X.indication` antérieure.
 - `X.confirm`. Cette primitive est délivrée par le service pour confirmer à un utilisateur qu'une primitive `X.request` a été traitée avec succès.  

.. index:: service sans connexion
.. index:: Service Data Unit, SDU

Les primitives peuvent être combinées pour modéliser différents types de services.  Le service le plus simple dans les réseaux informatique est appelé le service `sans connexion` [#fconnectionless]_. Ce service peut être modélisé en utilisant deux primitives : 

 - `Data.request(source,destination,SDU)`. Cette primitive est générée par un utilisateur qui spécifie, comme paramètres, son adresse (source), l'adresse du destinataire du message, et le message lui-même.  Nous utiliserons l'acronyme SDU, pour `Service Data Unit`, pour désigner le message qui est échanger de manière transparente entre deux utilisateurs d'un service.  
 - `Data.indication(source,destination,SDU)`. Cette primitive est délivrée par le fournisseur de service à un utilisateur.  Elle contient comme paramètres un `SDU`, ainsi que les adresses des utilisateurs destinataire et destinateur.   

.. index:: diagramme time-sequence

Lorsqu'il est question d'un service fourni dans un réseau informatique, il est souvent utile de pouvoir décrire les interactions entre les utilisateurs et le fournisseur de manière graphique.  Une représentation fréquemment utilisée est le diagramme `time-sequence`.  Dans ce chapitre et tout au long de ce livre, nous utiliserons souvent des diagrammes tel que celui de la figure ci-dessous.  Un diagramme time-sequence décrit les interactions entre deux utilisateurs et un fournisseur de service.  Par convention, les utilisateurs sont représentés dans les parties gauche et droite du diagramme, tandis que le fournisseur de service occupe le milieu.  Le temps s'écoule du haut vers le bas du diagramme.  Chaque primitive est représentée par une flèche horizontale à laquelle le nom de la primitive est attachée.  Les lignes pointillées sont utilisées pour représenter les relations possible entre deux ou plusieurs primitives.  Un tel diagramme fournit de l'information à propos de l'ordre des différentes primitives, mais la distance entre deux primitives ne représente pas une durée temporelle précise.   



.. index:: service sans connexion

La figure ci-dessous fournit une représentation en diagramme `time-sequence` du service sans-connexion. L'utilisateur à gauche, avec l'adresse `S`, génère une primitive `Data.request` contenant le SDU `M` qui doit être délivrée par le fournisseur de service à la destination `D`.  La ligne pointillée entre les deux primitives indique que la primitive `Data.indication` qui est transmise à l'utilisateur de droite correspond à la primitive `Data.request` envoyée par l'utilisateur de gauche.  

.. figure:: svg/intro-figures-017-c.*
   :align: center
   :scale: 80 

   Un service sans-connexion simple

.. index:: service sans connexion fiable, service sans connexion non-fiable

Il existe différentes implémentation du service sans connexion, et nous en discuterons plus loin.  En attendant, il est utile de discuter des caractéristiques de ce service.  Ainsi, un service `sans connexion fiable` est un service où le fournisseur de service garantit que tous les messages envoyés par un utilisateur seront transmis à leur destinataire.  Un tel service est certes pratique, mais il est difficile de garantir une transmission parfaite.  Pour cette raison, les réseaux informatiques supportent en général un service `sans connexion non fiable`.  


Un service `sans connexion non fiable` peut souffrir de nombreux problèmes, comparé au service `sans connexion fiable`.  Tout d'abord, il ne garantit pas la délivrance de tous les SDUs.  Cela peut être exprimé graphiquement par le diagramme ci-dessous.  

.. figure:: svg/intro-figures-034-c.*
   :align: center
   :scale: 80 

   Un service sans connexion non fiable peut perdre des SDUs

En pratique, un service `sans connexion non fiable` transmettra généralement la majeure partie des SDUs.  Cependant, puisque la délivrance n'est pas garantie, l'utilisateur doit être capable de faire face à la perte de n'importe quel SDU. 


.. comment:: I have already altered it here below, but suggestion: "Some unreliable connectionless service providers may deliver a SDU, sent by a user, multiple times to the same recipient."

Une seconde imperfection qui peut affecter un service `sans connexion non fiable` est qu'il peut dupliquer des SDUs.  Certains fournisseurs de service sans connexion non fiable peuvent transmettre plusieurs fois un SDU envoyé par un utilisateur.  Cela est illustré dans le diagramme ci-dessous. 

.. figure:: svg/intro-figures-033-c.*
   :align: center
   :scale: 80 

   Un service sans connexion non fiable peut dupliquer les SDUs

Enfin, certains services sans connexion non fiables peuvent transmettre au destinataire un SDU différent de celui qui lui a été transmit par l'émetteur dans le `Data.request`. Cela est illustré ci-dessous. 

Finally, some unreliable connectionless service providers may deliver to a destination a different SDU than the one that was supplied in the `Data.request`. This is illustrated in the figure below. 

.. figure:: svg/intro-figures-035-c.*
   :align: center
   :scale: 80 

	Un service non fiable sans connexion peut transmettre des SDUs erronés


Lorsqu'un utilisateur interagit avec un fournisseur de service, il doit connaître précisément les limitations du service sous-jacent, afin de pouvoir réagir aux problèmes qui peuvent se produire.  Chaque service doit donc disposer d'une définition précise de ses caractéristiques.

.. index:: ordre des SDUs

Une autre caractéristique importante du service sans connexion est s'il garde l'ordre dans lequel les SDUs ont été envoyés par l'émetteur. 
Cela est illustré dans la figure ci-dessous.   

.. figure:: png/intro-figures-036-c.png
   :align: center
   :scale: 80 

   Un service sans connexion préservant l'ordre des SDUs envoyé par un utilisateur

C'est une caractéristique souvent souhaitée par les utilisateurs, mais hélas, beaucoup de services sans connexions ne garantissent pas la préservation de l'ordre des SDUs envoyés. Cela est illustré ci-dessous.

.. figure:: svg/intro-figures-037-c.*
   :align: center
   :scale: 80 

   Un service sans connexion qui ne préserve pas l'ordre des SDUs envoyé par un utilisateur


.. index:: service sans connexion avec confirmation

Le service `sans connexion` est largement utilisé dans les réseaux informatiques, comme nous le verrons plus loin.  Plusieurs variantes de ce service de base ont été proposées.  Une d'entre elles est le service `sans connexion avec confirmation`.  Ce service utilise une primitive `Data.confirm` en plus des primitives habituelles `Data.request` et `Data.indication`.  Cette primitive est générée par le fournisseur de service poru confirmer à l'utilisateur qu'un SDU précédemment envoyé a bien été transmis à son destinataire.  Notez que, comme le service postal correspondant, le `Data.confirm` indique seulement que le SDU a été transmis à la destination.  Elle n'indique pas que le SDU a été traité par l'utilisateur auquel il est destiné.  Ce service `sans connexion avec confirmation` est illustré dans la figure ci-dessous. 

.. figure:: svg/intro-figures-018-c.*
   :align: center
   :scale: 80 

   Un service sans connexion avec confirmation

.. index:: service orienté-connexion

Le service `sans connexion` que nous avons décrit plus haut est fréquemment utilisé par des utilisateurs souhaitant échanger de petits SDUs.  Les utilisateurs qui doivent soit envoyer soit recevoir des SDUs potentiellement longs, ou bien qui ont besoin d'échanges structurés préfèrent souvent le service `orienté-connexion`.

.. index:: établissement de connexion

L'utilisation d'un service `orienté-connexion` comporte trois phases.  La première est l'établissement de la `connexion`.  Une `connexion` est une association temporaire entre deux utilisateurs à travers un fournisseur de service.  Plusieurs connexions peuvent exister en même temps à travers n'importe quelle paire d'utilisateurs.  Lorsqu'elle a pu être établie, la connexion est utilisée pour transférer des SDUs.  Les connexions fournissent généralement un flux bi-directionnel qui permet l'échange de données entre deux utilisateurs.  Ce flux est utilisé pour transférer les données pendant la seconde phase de la connexion, également appelée `transfert de données`.  La troisième phase est la fermeture de la connexion.  Une fois que les utilisateurs ont fini d'échanger leurs SDUs, ils demandent au fournisseur de service de terminer la connexion. Comme nous le verrons plus tard, le fournisseur de service lui-même peut mettre fin à une connexion dans certains cas.  

.. comment:: perhaps in the following paragraph it would provide more clarity to specify which host considers the connection to be open at which stage (first destination, then sender from my understanding). There are two sentences in this paragraph that begin with the phrase: "At this point, the connection is considered to be open". This might be confusing to somebody...somewhere....

L'établissement de la connexion peut être modélisé avec quatre primitives : `Connect.request`, `Connect.indication`, `Connect.response` and `Connect.confirm`. La primitive `Connect.request` est utilisée pour demander l'établissement d'une connexion.  Le paramètre principal de cette primitive est l'`adresse` de la destination.  Le fournisseur de service délivre une primitive `Connect.indication` pour informer l'utilisateur à la destination de la demande de connexion.  Si ce dernier accepte l'établissement de la connexion, il répond avec une primitive `Connect.response`. A ce moment, la connexion est considérée comme établie, et la destination peut commencer à envoyer des SDUs.  Le fournisseur de service traite le `Connect.response` et délivrera un `Connect.confirm` à l'initiateur de la connexion.  La transmission de cette primitive termine la phase d'établissement de la connexion.  A ce moment, les deux directions de la connexion sont considérées comme ouvertes, et les deux utilisateurs peuvent transmettrent des SDUs.  Un établissement de connexion est illustré ci-dessous.  


.. figure:: svg/intro-figures-019-c.*
   :align: center
   :scale: 80 

   Etablissement de connexion.  

L'exemple ci-dessus montre un établissement de connexion réussi.  Cependant, en pratique, toutes les tentatives de connexion ne sont pas couronnées de succès.  Une raison est que la destination peut ne pas accepter, pour des raisons de politique ou de performance, d'établir la connexion avec l'initiateur à cet instant précis.  Dans ce cas, la destination répond à la primitive `Connect.indication` par une primitive `Disconnect.request` contenant un paramètre indiquant que la connexion a été refusée.  Le fournisseur de service délivrera alors une primitive `Disconnect.indication` pour informer l'initiateur de la connexion.  Une seconde raison est que le fournisseur de service pourrait ne pas être en mesure de joindre la destination, par exemple parce que cette dernière n'est pas attachée au réseau à cet instant précis, ou parce que le réseau est congestionné.  Dans ces cas, le fournisseur de service répond à la primitive `Connect.request` par un `Disconnect.indication` dont le paramètre `raison` contient des informations additionnelles au sujet de l'échec de la connexion. 


.. figure:: svg/intro-figures-020-c.*
   :align: center
   :scale: 80 

  Deux types d'échec de tentative de connexion


.. index:: transfert de données en mode message

Une fois la connexion établie, le fournisseur de service fournit deux flux de données aux utilisateurs.  Le premier flux de données peut être utilisé par le premier utilisateur pour envoyer des SDUs.  Le second permet au second d'envoyer des SDUs à l'initiateur.  Les flux de données peuvent être organisés de différentes manières.  Une première organisation possible est le transfert en `mode message`.  Avec le transfert en `mode message`, le fournisseur de service garantit que la destination recevra une et une seule primitive `Data.indication` pour chaque `Data.request` générée par l'autre extrémité de la communication.  Le transfert en `mode message` est illustré ci-dessous. L'avantage principal du transfert en mode message est que la destination reçoit les SDUs tels qu'envoyés par l'autre utilisateur.  Si chaque SDU contient une commande, l'utilisateur à la destination peut traiter chaque commande dès la réception du SDU correspondant. 


.. figure:: svg/intro-figures-021-c.*
   :align: center
   :scale: 80 

   Transfert en mode message, dans un service orienté connexion

.. index:: transfert de données en mode flux d'octets

Malheureusement, le transfert en `mode message` n'est pas beaucoup utilisé sur Internet.  Le plus populaire des services orienté-connexion est le mode `flux d'octets`.  Avec ce mode, le fournisseur de service fournit un flux d'octets qui fait la liaison entre les deux utilisateurs.  Le fournisseur de service garantit que les octets envoyés à une extrémité du flux via des primitives `Data.request` contenant des séquences d'octets comme SDUs seront délivrés correctement au receveur à l'autre extrémité en utilisant des primitives `Data.indication`.  Le fournisseur de service garantit que tous les octets envoyés à une extrémité du flux sont délivrées correctement et dans le même ordre à l'autre extrémité.  Cependant, le fournisseur de service ne garantit pas que les limites des SDUs soient préservées.  Il n'y a pas de relation entre le nombre de primitives `Data.request` et le nombres de primitives `Data.indication`.  Ce mode `flux d'octets` est illustré dans la figure ci-dessous.  Les conséquences pratiques de ceci sont que si l'utilisateur souhaite échanger des SDUs structurés, il va devoir fournir un mécanisme permettant au receveur de délimiter les SDUs successifs dans le flux d'octets qu'il reçoit.  Comme nous verrons dans le chapitre suivant, les protocoles de la couche Application utilisent souvent des délimiteurs tels que le caractère de fin de ligne, pour séparer les SDUs dans le flux d'octets.    


.. figure:: svg/intro-figures-022-c.*
   :align: center
   :scale: 80 

   Transfert en mode flux d'octets dans un service orienté-connexion

.. index:: fermeture de connexion abrupte


La troisième phase de la connexion est sa fermeture.  Puisqu'une connexion implique trois parties (deux utilisateurs et un fournisseur de service), n'importe lequel d'entre eux peut demander la fermeture de la connexion.  Généralement, les connexions sont fermées à la demande d'un utilisateur lorsque le transfert de données est terminé.  Cependant, parfois, le fournisseur de service peut être forcé de terminer la connexion, par exemple par manque de ressources, ou parce qu'un utilisateur n'est plus joignable.  Dans ce cas, le fournisseur de service générera des primitives `Disconnect.indication` aux utilisateurs.  Ces primitives contiendront en paramètres des informations expliquant la fermetture de la connexion.  Malheureusement, comme illustré dans la figure ci-dessous, quand un fournisseur de service est forcé de terminer une connexion, il ne peut garantir que tous les SDUs envoyés par les utilisateurs ont été transmis à leur destinataire.  Cette fermeture de connexion est dite `abrupte`, car elle peut causer des pertes de données. 



.. figure:: svg/intro-figures-038-c.*
   :align: center
   :scale: 80 

   Fermeture de connexion abrupte initiée par le fournisseur de service

Une fermeture de connexion abrupte peut également être causée par l'un des utilisateur.  Si un utilisateur a besoin, pour quelque raison que ce soit, de terminer une connexion rapidement, il peut générer une primitive `Disconnect.request` pour demander une terminaison abrupte.  Le fournisseur de service traitera la requête, arrêtera les deux flux de données et transmettra une primitive `Disconnect.indication` à l'utilisateur distant dès que possible.  Comme illustré dans la figure ci-dessous, cette fermeture abrupte peut causer des pertes de SDUs. 




.. figure:: svg/intro-figures-023-c.*
   :align: center
   :scale: 80 

   Fermeture de connexion abrupte initiée par un utilisateur

.. index:: Fermeture de connexion gracieuse

Pour assurer la transmission fiable des messages à travers une connexion, il faut considérer les deux flux qui la compose indépendamment.  Un utilisateur pourrait avoir terminé d'envoyer ses SDUs, et donc être prêt à terminer la connexion, mais toujours recevoir des SDUs sur le flux en sens inverse.  Une telle fermeture de connexion est représentée dans la figure ci-dessous.  Un utilisateur génère une primitive `Disconnect.request` à son fournisseur une fois qu'il a généré tous ses `Data.request`.  Le fournisseur de service attend que toutes les primitives `Data.indication` ait été transmises à la destination avant de générer la primitive `Disconnect.indication`.  Cette primitive informe le receveur qu'il ne recevra plus de SDUs sur cette connexion, mais il est toujours capable de générer lui-même des primitives `Data.request` sur le flux dans la direction opposée.  Une fois que ce second utilisateur a terminé ses transferts de SDUs, il génère à son tour une primitive `Disconnect.request` pour demander la terminaison de la direction de flux restant.  Le fournisseur de service traite la requête et délivre le `Disconnect.indication` correspondant à l'autre extrémité du flux une fois que toutes les primitives `Data.indication` en attente ont été transmises. Cette fermeture de connexion, dite 'gracieuse', implique donc que chaque direction de transfert soit fermée indépendamment de l'autre, et la fermeture est effective lorsque les deux flux sont terminés.  A ce moment, toutes les données ont été délivrées.  




.. figure:: svg/intro-figures-024-c.*
   :align: center
   :scale: 80 

   Fermeture de connexion gracieuse


.. note:: Fiabilité du service orienté-connexion

 Un point important à prendre en compte au sujet du service orienté-connexion est sa fiabilité.  Un service `orienté-connexion` peut uniquement garantir la délivrance correcte de tous les messages dans le cas où la connexion s'est terminée correctement.  Cela implique que, tant que la connexion est active, il n'y a aucune garantie sur la bonne délivrance des messages échangés puisqu'il est toujours possible que la connexion se termine abruptement.  

.. rubric:: Footnotes

.. [#fconnectionless] Ce service est appelé service sans connexion parce qu'il n'y a pas besoin de créer une connexion avant de transmettre les données, contrairement au service orienté-connexion. 


.. include:: ../links.rst
