.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. index:: Modèles de référence

.. comment:: translation by vvandens

Les modèles de référence
########################

Etant donné la complexité croissante des réseaux informatiques, les chercheurs du domaine ont proposé, au cours des années 70, des modèles de référence permettant de décrire les protocoles et services réseau.  Le modèle OSI (Open Systems Interconnection) [Zimmermann80]_ fut probablement le plus influent.  Il a servit de base au travail de standardisation effectué par l':term:`ISO` visant à développer des standards globaux pour les réseaux informatiques.  Le modèle de référence utilisé dans ce livre peut être considéré comme une version simplifiée du modèle de référence OSI . [#fiso-tcp]_.

.. index:: Modèle de référence en cinq couches

Le modèle de référence en cinq couches
--------------------------------------

Notre modèle de référence est divisé en cinq couches, comme montré ci-dessous. 

.. figure:: png/intro-figures-026-c_.png
   :align: center
   :scale: 50 

   Les cinq couches du modèle de référence


.. index:: câble électrique, fibre optique, fibre optique multimode, fibre optique monomode

La première couche en commençant par le bas est la couche Physique.  Deux appareils communiquant entre eux sont reliés par un médium physique.  Le médium physique est utilisé pour transférer un signal électrique ou optique entre deux appareils directement connectés.  En pratique, plusieurs types de mediums sont utilisables : 

 - `Le câble électrique`.  L'information peut être transmise sur différents types de câbles électriques.  Les plus communs sont les paires torsadées utilisées dans le réseau téléphonique, mais également dans les réseaux d'entreprise, et les câbles coaxiaux.  Les câbles coaxiaux sont toujours utilisés dans les réseaux de télévision câblés, mais plus dans les réseaux d'entreprise.  Certaines technologies réseaux fonctionnent par dessus le câble électrique classique. 
 - `La fibre optique`.  Les fibres optique sont fréquemment utilisées dans les réseaux publiques et d'entreprise, quand la distance entre les appareils de communication est supérieure à un kilomètre.  Il y a deux types principals de fibres optiques : multimode et monomode.  La fibre multimode est beaucoup plus cher que la monomode parce qu'une LED peut être utilisée pour envoyer un signal au dessus d'une fibre multimode tandis qu'une fibre monomode ne fonctionne qu'avec un laser.  A cause des mode de propagation de la lumière différents, les fibres monomodes sont limité à des distances de quelques kilomètres tandis que les fibres multimodes peuvent être utilisées sur des distances supérieures à plusieurs dizaines de kilomètres.  Dans les deux cas, des répétiteurs peuvent être utilisés pour regénérer le signal optique en fin de fibre, avant de l'envoyer sur une autre fibre.  
 - `wireless`. Dans ce cas, un signal radio est utilisé pour encoder l'information échangée entre les appareils communiquant.  Plusieurs techniques de modulation sont utilisées pour envoyer l'information sur un canal sans fil, et il y a beaucoup d'innovation dans ce domaine, puisque de nouvelles techniques apparaissent chaque année.  Alors que la plupart des réseaux sans fil se base sur des signaux radio, certains utilisent un laser qui envoie des impulsions lumineuses à un détecteur distant.  Ces techniques optiques permettent de créer des liens point-à-point, alors que les techniques basées sur les signaux radios peuvent être utiliser pour créer des réseaux contenant plusieurs appareils répartis dans une petite zone géographique (en fonction de la directionnalité des antennes utilisées).  



Un point important à noter au sujet de la couche Physique est le service qu'elle fournit.  Ce service est généralement un service orienté-connexion non fiable, qui permet aux utilisateurs de la couche Physique d'échanger des bits.  L'unité de transfert d'information de la couche Physique est le bit.  Cette couche est non fiable parce que : 

 - La couche Physique peut changer. Par exemple, la valeur d'un bit peut changer en cours de transmission à cause d'interférences électromagnétiques
 - La couche Physique peut transmettre plus de bits au receveur que le nombre de bits envoyés par l'émetteur
 - La couche Physique peut transmettre moins de bits au receveur que le nombre de bits envoyés par l'émetteur

Les deux derniers points peuvent sembler surprenant à première vue.  Lorsque deux appareils sont reliés par un câble, comment est-ce possible que des bits puissent apparaître ou disparaître sur ce câble?  Cela est principalement du au fait que les appareils utilisent leur propre horloge pour transmettre des bits à un débit donné.  Considérons un émetteur avec une horloge générant des ticks un million de fois par seconde, et envoie un bit à chaque tick.  Chaque microseconde, l'émetteur envoie un signal électrique ou optique encodant un bit.  La bande passante de l'émetteur est donc de 1Mbps.  Si l'horloge du receveur émet des ticks chaque micro seconde très exactement, il pourra également délivrer un Mbps à ses utilisateurs.  Néanmoins, si l'horloge du receveur est légèrement plus rapide (ou plus lente), il délivrera alors légèrement plus (ou moins) qu'un million de bits par seconde.  Cela explique pourquoi la couche Physique peut perdre ou créer des bits.  

.. note:: Bande passante

Dans les réseaux informatiques, la bande passante de la couche physique est toujours exprimée en bits par seconde.  Un Mbps correspond à un million de bits par seconde, et un Gbps à un milliard de bits par seconde.  Cela contraste avec les spécifications des mémoires qui sont généralement exprimées en octets (8 bits), KiloOctets (1024 octets) ou MegaOctets (1048576 octets).  Donc, pour transférer un MegaOctet à travers un lien d'un Mbps prendra 1.049 secondes.  

 ==============       ===============
 Bande passante       Bits per second
 ==============       ===============
 1 Kbps	       :math:`10^3`
 1 Mbps	       :math:`10^6`
 1 Gbps	       :math:`10^9`
 1 Tbps	       :math:`10^{12}`
 ==============       ===============
  

.. index:: Couche Physique


.. figure:: svg/intro-figures-027-c.*
   :align: center
   :scale: 80

   La couche Physique

La couche Physique permet donc à deux ou plusieurs entités directement attachées au même médium de transmission d'échanger des bits.  Pouvoir échanger des bits est important, puisque toute information peut virtuellement être encodée comme une suite de bits.  Les ingénieurs électriciens ont l'habitude de traiter des flux de bits, mais les informaticiens préfèrent généralement utiliser des concepts de plus haut niveau.  Un problème similaire se pose au niveau du stockage de fichiers.  Le matériel de stockage tel que les disques durs stockent également des flux de bits.  Il existe des appareils hardware qui traitent le flux de bits produit par un disque dur, mais les informaticiens ont conçu des systèmes de fichiers pour permettre aux applications d'accéder facilement à ce matériel de stockage.  Ces systèmes de fichiers sont typiquement divisés en plusieurs couches.  Les disques durs stockent des secteurs de 512 octets ou plus.  Les systèmes de fichiers Unix regroupent les secteurs en blocs plus larges qui contient des données ou des i-nodes qui représentent la structure du système de fichiers.  Finalement, les applications manipulent les fichiers et les répertoires, qui sont traduits en blocs, secteurs et éventuellement bits par le système d'exploitation.  

.. index:: Couche Liaison de données, trame

Les réseaux informatiques utilisent une approche similaire, et chaque couche fournit un service qui est construit au dessus de la couche inférieure, et est plus proche des besoins des applications.  

La couche `Liaison de données` repose au dessus du service fournit par la couche physique.  Cette couche permet à deux hôtes directement connectés à travers la couche physique d'échanger de l'information.  L'unité d'information échangée entre les deux entités de la couche `Liaison de données` est la trame.  Une trame est une suite de bits finie.  Certaines couches `Liaison de données` utilisent des trames de longueur variable, tandis que d'autres utilisent des trames de longueur fixe.  Certaines couches `Liaison de données` fournissent un service orienté-connexion, tandis que d'autres fournissent un service sans connexion.  certaines couches `Liaison de données ` fournissent un service fiable, tandis que d'autres ne garantissent pas la transmission correcte de l'information.  

Un point important à noter au sujet de la couche `Liaison de données` est que, bien que la figure ci-dessous indique que deux entités de la couches `Liaison de données` échangent des trames directement, en réalité, cela peut être légèrement différent.  Lorsque l'entité `Liaison de données` à gauche a besoin de transmettre une trame, elle envoie chacun des bits de la trame à la couche Physique sous-jacente.  La couche Physique va alors traduire cette séquence de bits en signal électromagnétique ou optique, et l'enverra à travers le médium physique.  La couche Physique de l'entité de droite va décoder le signal reçu, le re-traduire en bits et va transmettre la séquence de bits obtenue à la couche `Liaison de données`.  S'il n'y a pas d'erreur de transmission, l'entité `Liaison de données` va donc recevoir la trame émise par l'entité de gauche.  



.. figure:: svg/intro-figures-028-c.*
   :align: center
   :scale: 80 

   La couche Liaison de Données


.. index:: Couche Réseau, paquet

La couche `Liaison de Données` permet à des hôtes directement connectés d'échanger de l'information, mais il est aussi souvent nécessaire d'échanger de l'information entre des hôtes qui ne sont pas attachés au même médium physique.  Ce rôle échoit à la couche `Réseau`.  La couche `Réseau` est construite au dessus de la couche `Liaison de Données`.  Les entités de cette couches échangent des `paquets`.  Un `paquet` est défini comme une suite finie d'octets qui est transmise par la couche `Liaison de Données` à l'intérieur d'une ou de plusieurs trames.  Un paquet contient généralement de l'information à propos de son origine et de sa destination.  Il passe généralement par plusieurs appareils intermédiaires appelés routeurs avant de rejoindre sa destination.  

.. figure:: svg/intro-figures-029-c.*
   :align: center
   :scale: 80 

   La couche Réseau

.. index:: Couche Transport, segment

La plupart des réalisations de la couche Réseau, incluant l'Internet, ne fournissent pas un service fiable.  Cependant, de nombreuses applications ont besoin d'échanger de l'information de manière fiable, et utiliser la couche `Réseau` directement n'est donc pas une bonne solution.  Assurer une transmission fiable des données produites par une application est le rôle de la couche `Transport`.  Les entités de la couche `Transport` échangent des `segments`.  Un segment est une suite finie d'octets qui sont transportés à l'intérieur d'un ou de plusieurs paquets.  Une entité de la couche Transport transmet des segments (ou parfois des morceaux de segments) à la couche `Réseau` sous-jacente.  

Il y a différents types de couches transport.  Les plus utilisés sur Internet sont :term:`TCP`, qui fournit un service de transport de flux d'octets fiable orienté connexion, et :term:`UDP`, qui fournit un service de transport sans connexion non fiable.

.. figure:: svg/intro-figures-030-c.*
   :align: center
   :scale: 80 

   La couche Transport

.. index:: Couche Application

La couche supérieure de notre architecture est la couche `Application`.  Elle inclut tous les mécanismes et les structures de données nécessaires pour les applications.  Nous utiliserons le terme ADU (Application Data Unit) pour indiquer les données échangées entre deux entités de la couche Application.  

.. figure:: svg/intro-figures-031-c.*
   :align: center
   :scale: 50 

   La couche Application

.. index:: Modèle de référence TCP/IP


Le modèle de référence TCP/IP
-----------------------------

 Contrairement à OSI, la communauté TCP/IP n'a pas produit beaucoup d'efforts pour définir un modèle de référence détaillé.  En fait, les buts de l'architecture Internet ne furent documentés qu'après que TCP/IP soit déployé [Clark88]_.   :rfc:`1122` qui définit les spécifications des hôtes Internet mentionne quatre couches différentes.  Il s'agit, en commençant par le haut, de : 


- Une couche Application
- Une couche Transport
- Une couche Internet, qui est l'équivalent de la couche `Réseau` dans le modèle en cinq couches
- Une couche Lien, qui combine les fonctionnalités de la couche physique et de la couche Liaison de Données du modèle en cinq couches. 

Outre ces différences dans les couches les plus basses, le modèle de référence TCP/IP est très proche du modèle en cinq couches présenté dans ce document.  


.. index:: Modèle de référence OSI

Le modèle de référence OSI
--------------------------

 Comparé au modèle de référence en cinq couche expliqué ci-dessus, le modèle de référence :term:`OSI` est divisé en sept couches.  Les quatre couches inférieures sont similaires à celles du modèle en cinq couches.  Par contre, le modèle de référence `OSI` détaille la couche Application en trois couches : 
 - La couche Session.  Cette couche contient les protocoles et mécanismes nécessaires pour organiser et synchroniser le dialogue et gérer les échanges de données des entités de la couche Présentation.  Alors qu'une des fonctions principales de la couche Transport est de gérer la non-fiabilité de la couche Réseau, l'objectif de la couche Session est de cacher les pannes éventuelles des connexions de la couche Transport aux couches supérieures.  Pour cela, la couche Session fournit des services permettant d'établir des sessions, de supporter l'échange ordonné de données, et de terminer les sessions proprement.  
 - La couche Présentation a été créée pour gérer les différents modes de représentation de l'information sur les ordinateurs.  Il y a plusieurs différences dans la manière dont les ordinateurs stockent l'information.  Certains stockent les entiers sur 32 bits, d'autres sur 64, et le même problème se présente avec les nombres en virgule flottante.  Pour les informations textuelles, c'est encore plus complexe, à cause des différents codes de caractères utilisés.  Enfin, la situation se complique encore lorsqu'il s'agit d'échanger des informations structurées, telles que les enregistrements de base de données.  Pour résoudre ce problème, la couche Présentation fournit une représentation commune pour les données transférées.  La notation :term:`ASN.1` a été créée pour la couche Présentation, et est toujours utilisée de nos jours par certains protocoles.  
 - La couche Application, qui contient les mécanismes qui ne rentrent ni dans la couche Présentation, ni dans la couche Session.  La couche Application OSI a été elle-même divisée en plusieurs éléments génériques de service.  


.. note:: Où sont les couches manquantes du modèle TCP/IP? 

 Le modèle de référence TCP/IP place implicitement les couches Session et Présentation dans la couche Application.  Les motivations principales sur lesquelles se base le modèle TCP/IP pour simplifier les couches supérieures est d'ordre pragmatique : La plupart des applications Internet furent lancés en tant que prototypes, qui ont évolués et furent ensuite standardisés.  Beaucoup de ces applications supposaient qu'elles seraient utilisées pour échanger de l'information écrite en anglais américain, et que le code US-ASCII sur 7 bits serait suffisant.  Ce fut le cas pour l'email, comme nous le verrons dans le chapitre suivant.  L'email a été capable d'évoluer pour supporter différents encodages de caractères.  Certaines applications ont considéré les différentes représentations de données de manière explicite.  Par exemple, :term:`ftp` contient des mécanismes pour convertir un fichier d'un format en un autre, et le langage HTML a été défini pour représenter des pages web.  D'un autre côté, beaucoup de spécification sISO ont été développées par des comités composés de personnes ne participant pas aux implémentations.  L'ISO a dépensé beaucoup d'efforts pour analyser les spécifications et pour définir une solution qui rencontre ces dernières.  Malheureusement, certaines de ces spécifications étaient si complexe qu'il était difficile de les implémenter complètement.  
.. comment:: Que signifie la dernière phrase : the standardisation bodies defined recommended profiles that contained the implemented sets of options...  ? 


.. The work within ISO and ITU on protocols and services was 

.. figure:: png/intro-figures-032-c.png
   :align: center
   :scale: 80 

   Les sept couches du modèle de référence OSI

.. rubric:: Footnotes


.. [#funicode] Il y a à présent un consensus global sur l'usage du format de caractère Unicode_.  Unicode peut représenter plus de 100,000 caractères différents des langages écrits sur Terre.  Il est possible qu'un jour, les ordinateurs n'utiliseront plus qu'Unicode pour représenter tous les caractères, et que ce dernier devienne le format standard pour l'échange de caractères, mais nous y sommes pas encore.


.. [#fiso-tcp] Une discussion historique intéressante sur le débat OSI-TCP/IP peut être trouvée dans [Russel06]_

.. [#fsynchro] Arriver à synchroniser parfaitemetn des horloges à haute fréquence est en pratique extrêmement difficile.  Néanmoins, certaines couches physiques introduisent une boucle de feedback qui permet à l'horloge du receveur de se synchroniser automatiquement à celle de l'émetteur.  Cependant, toutes les couches physiques ne permettent pas ce type de synchronisation. 

.. include:: ../links.rst
