.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


=======
Preface
=======

This is the current draft of the second edition of the `Computer Networking : Principles, Protocols and Practice`. 

.. This textbook came from a frustration of its main author. Many authors chose to write a textbook because there are no textbooks in their field or because they are not satisfied with the existing textbooks. This frustration has produced several excellent textbooks in the networking community. At a time when networking textbooks were mainly theoretical, `Douglas Comer`_ chose to write a textbook entirely focused on the TCP/IP protocol suite [Comer1988]_, a difficult choice at that time. He later extended his textbook by describing a complete TCP/IP implementation, adding practical considerations to the theoretical descriptions in [Comer1988]_. `Richard Stevens`_ approached the Internet like an explorer and explained the operation of protocols by looking at all the packets that were exchanged on the wire [Stevens1994]_. `Jim Kurose`_ and `Keith Ross`_ reinvented the networking textbooks by starting from the applications that the students use and later explained the Internet protocols by removing one layer after the other [KuroseRoss09]_. 

.. The frustrations that motivated this book are different. When I started to teach networking in the late 1990s, students were already Internet users, but their usage was limited. Students were still using reference textbooks and spent time in the library. Today's students are completely different. They are avid and experimented web users who find lots of information on the web. This is a positive attitude since they are probably more curious than their predecessors. Thanks to the information that is available on the Internet, they can check or obtain additional information about the topics explained by their teachers. This abundant information creates several challenges for a teacher. Until the end of the nineteenth century, a teacher was by definition more knowledgeable than his students and it was very difficult for the students to verify the lessons given by their teachers. Today, given the amount of information available at the fingertips of each student through the Internet, verifying a lesson or getting more information about a given topic is sometimes only a few clicks away. Websites such as `wikipedia <https://wikipedia.org/>`_ provide lots of information on various topics and students often consult them. Unfortunately, the organisation of the information on these websites is not well suited to allow students to learn from them. Furthermore, there are huge differences in the quality and depth of the information that is available for different topics. 

.. The second reason is that the computer networking community is a strong participant in the open-source movement. Today, there are high-quality and widely used open-source implementations for most networking protocols. This includes the TCP/IP implementations that are part of linux_, freebsd_ or the uIP_ stack running on 8bits controllers, but also servers such as bind_, unbound_, apache_ or sendmail_ and implementations of routing protocols such as xorp_ or quagga_ . Furthermore, the documents that define almost all of the Internet protocols have been developed within the Internet Engineering Task Force (IETF_) using an open process. The IETF publishes its protocol specifications in the publicly available RFC_ and new proposals are described in `Internet drafts`_.  

.. This open textbook aims to fill the gap between the open-source implementations and the open-source network specifications by providing a detailed but pedagogical description of the key principles that guide the operation of the Internet. The book is released under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_. Such an open-source license is motivated by two reasons. The first is that we hope that this will allow many students to use the book to learn computer networks. The second is that I hope that other teachers will reuse, adapt and improve it. Time will tell if it is possible to build a community of contributors to improve and develop the book further. As a starting point, the first release contains all the material for a one-semester first upper undergraduate or a graduate networking course.

The first edition of this ebook has been written by `Olivier Bonaventure`_. `Laurent Vanbever`_, `Virginie Van den Schriek`_, `Damien Saucez`_ and `Mickael Hoerdt`_ have contributed to exercises. Pierre Reinbold designed the icons used to represent switches and Nipaul Long has redrawn many figures in the SVG format. Stephane Bortzmeyer sent many suggestions and corrections to the text. Additional information about the textbook is available at https://inl.info.ucl.ac.be/CNP3

.. The overall objective of the book is to explain the principles and the protocols used in computer networks such as the Internet and also provide the students with some intuition about the important practical problems that often arise. The textbook was developed for the 
.. The course follows a hybrid problem-based learning (:term:`PBL`) approach. During each week, the students follow a 2 hours theoretical course that describes the principles and some of the protocols. They also receive a set of small problems that they need to solve in groups. These problems are designed to reinforce the student's knowledge but also to explore the practical problems that arise in real networks by allowing the students to perform experiments by writing prototype networking code. 


.. note::

 `Computer Networking : Principles, Protocols and Practice`, (c) 2011, `Olivier Bonaventure <https://inl.info.ucl.ac.be/obo>`_, `Universite catholique de Louvain <https://uclouvain.be/>`_ (Belgium) and the collaborators listed above, used under a Creative Commons Attribution (CC BY) license made possible by funding from The Saylor Foundation's Open Textbook Challenge in order to be incorporated into Saylor.org' collection of open courses available at `https://www.saylor.org <https://www.saylor.org>`_. Full license terms may be viewed at : `http://creativecommons.org/licenses/by/3.0/ <http://creativecommons.org/licenses/by/3.0/>`_


About the author
################

`Olivier Bonaventure <https://inl.info.ucl.ac.be/obo>`_ is currently professor at `Universite catholique de Louvain <https://uclouvain.be/>`_ (Belgium) where he leads the `IP Networking Lab <https://inl.info.ucl.ac.be/>`_ . His research has been focused on Internet protocols for more than twenty years. Together with his Ph.D. students, he has developed traffic engineering techniques, performed various types of Internet measurements, improved the performance of routing protocols such as BGP and IS-IS and participated to the development of new Internet protocols including shim6, LISP and Multipath TCP. He frequently contributes to standardisation within the `IETF <https://www.ietf.org>`_. 

.. He was on the editorial board of IEEE/ACM Transactions on Networking and is Education Director of `ACM SIGCOMM <https://www.sigcomm.org>`_.





.. include:: links.rst

