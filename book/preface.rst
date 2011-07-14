.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_


=======
Preface
=======

As most textbooks, this textbook came from a frustation of its main author. Many authors chose to write a textbook because there are no textbooks in their field or because they are not satistified with the existing textbooks. This frustration has produced several excellent textbooks in the networking community. At a time when networking textbooks were mainly theoretical, `Douglas Comer`_ chose to wrote a textbook entirely focused on the TCP/IP protocol suite [Comer1988]_, a difficult choice at that time. He later extended his textbook by describing a complete TCP/IP implementation, adding practical considerations to the theoretical descriptions in [Comer1988]_. `Richard Stevens`_ approached the Internet like an explorator and explained the operation of protocols by looking at all the packets that were exchanged on the wire [Stevens1994]_. `Jim Kurose`_ and `Keith Ross`_ reinvented the networking textbooks by starting from the applications that the students use and later explained the Internet protocols by removing one layer after the other [KuroseRoss09]_. 

The frustations that motivated this book are different. When I started to teach networking in the late 1990s, students were already Internet users, but they usage was limited. They were still using reference textbooks and spent time in the library. Today's students are completely different. They are avide and experimented web users who find lots of information on the web. This is a positive attitude since they are probably more curious thant their predecessors. Thanks to the information that is available on the Internet, they can check or obtain additional information about the topics explained by their teachers. This abudant information creates several challenges for a teacher. Until the end of the nineteenth century, a teacher was by defintion more knowledgeable than his students and it was very difficult for the students to verify the lessons given by their teachers. Today, given the amount of information that is available at the fingertips of each student through the Internet, verifying a lesson or getting more information about a given topic is sometimes only a few clicks away. Websites such as http://wikipedia.org provide lots of information on various topics and students often consult them. Unfortunately, the organisation of the information on these websites is not well suited to allow a students to learn from them. Furthermore, there are huge differences in the quality and the depth of the information that is available for different topics. 

The second reason is that that the computer networking community is a strong participant in the open-source mouvement. Today, there are high-quality and widely used open-source implementations for most of networking protocols. This includes the TCP/IP implementations that are part of linux_, freebsd_ or the uIP_ stack running on 8bits controllers, but also servers such as bind_, unbound_, apache_ or sendmail_ and implementations of routing protocols such as xorp_ or quagga_ . Furthermore, the documents that define almost all of the Internet protocols have been developed within the Internet Engineering Task Force (IETF_) using an open process. The IETF publishes its protocols specifications in the publicly available RFC_ and new proposals are described in `Internet drafts`_.  

This open textbook aims at filling the gap between the open-source implementations and the open-source network specifications by providing a detailed but pedagogical description of the key principles that guide the operation of the Internet.  The book is released under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_. Such an open-source license is motivated by two reasons. The first is that we hope that this will allow many students to use the book to learn computer networks. The second is that I hope that other teachers will reuse, adapt and improve it. Time will tell if it is possible to build a community of contributors to improve and develop the book further. As a starting point, the first release contains all the material for a one-semester first upper undergraduate or a graduate networking course.

.. note:: How to contribute ?

 Like any open-source project, the future of `Computer Networking Principles, Protocols and Practice` will depend on its contributors. Most of the text has been written by `Olivier Bonaventure`_. `Laurent Vanbever`_, `Virginie Van den Schriek`_, `Damien Saucez`_ and `Mickael Hoerdt`_.
 
 The development of the textbook is managed through a trac platform at https://scm.info.ucl.ac.be/trac/cnp3 . You can contribute to the project by : 

  - sending comments, suggestions or bug reports  by filing `tickets <https://scm.info.ucl.ac.be/trac/cnp3/newticket>`_ or via the CNP3 mailing list at https://listes-2.sipr.ucl.ac.be/sympa/subscribe/cnp3
  - proposing new exercices on the `CNP3 mailing list <https://listes-2.sipr.ucl.ac.be/sympa/subscribe/cnp3>`_
  - proposing new sections or chapters on the `CNP3 mailing list <https://listes-2.sipr.ucl.ac.be/sympa/subscribe/cnp3>`_
  - follow the developmen on the book's 'facebook page <http://www.facebook.com/pages/Computer-Networking-Principles-Protocols-and-Practice/129951043755620>'
  
 A stable release of the textbook will be issued at least once per year on http://inl.info.ucl.ac.be/CNP3 and the development version will always be available from https://scm.info.ucl.ac.be/trac/cnp3 . You can download the sources via subversion by using `svn co https://scm.info.ucl.ac.be/svn/cnp3/book`. The book was compiled on MacOS/X Snow Leopard using sphinx_. inkscape_ is required to convert some of the images in png format. Most of the images will be converted to the SVG format to improve the portability of the textbook.

.. The overall objective of the book is to explain the principles and the protocols used in computer networks and also provide the students with some intuition about the important practical issues that arise often. The course follows a hybrid problem-based learning (:term:`PBL`) approach. During each week, the students follow a 2 hours theoretical course that describes the principles and some of the protocols. They also receive a set of small problems that they need to solve in groups. These problems are designed to reinforce the student's knowledge but also to explore the practical problems that arise in real networks by allowing the students to perform experiments by writing prototype networking code. 



.. include:: links.rst

