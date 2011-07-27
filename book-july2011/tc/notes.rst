.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_



Traffic Control



La façon utilisée cette année pour présenter le cours s'est bien passée, avec des discussions à la fin sur les mécanismes de scheduling et leur intéreêt.

L'exercise où l'on regarde ce qui se trouve en sortie en fonction de l'entrée d'un scheduler wfq est particulièrement intéressant et devrait se trouver dans le cours comme exercice de base

on pourrait également faire des exercices du même style sur le token bucket en regardant les différents patterns de trafic et voir comment ils sont acceptés/rejetés par un token bucket pour donner une idée aux étudiants


le chapitre pourrait être organisé sous la forme des slides de cette année, avec les schedulers à la fin


- classification
- shaping/policing, avec focus sur token bucket et les autres en illustration
- buffer acceptance, avec red et ecn
- scheduling en commençant par le best effort et en mettant des compléments dans les exercices pour que les étudiants comprennent bien les différentces entre les types de schedulers

pour wrr, il serait intéressant d'avoir un exercice qui compare le pattern de traffic en fonction de la façon dont le schedule est organisé. idem pour un exercice qui indique les limitations dues à un gros/petit schedule (style, quel est le débit minimum que l'on peut associer à un flux si on a un schedule avec x positions)

pour virtual clock et scfq, on peut également faire une petite discussion sur la difficulté d'implémenter et l'impact du wrap et du nombre de bits pour représenter les timestamps

pour drr, une petite analyse de l'impact du quantum pourrait être un exercice intéressant

le projet fait par Virginie cette année pourrait être un excellent projet de programmation à inclure au bouquin

la discussion sur l'utilisation d'intserv et de diffserv est nettement moins itnéressante et va probablement sauter

