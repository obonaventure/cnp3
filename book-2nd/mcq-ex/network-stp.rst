.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 

.. _mcq-network-stp:


Ethernet networks
=================

:task_id: spanningtree

1. With the 802.1d protocol, Ethernet switches exchange BPDUs that contain four informations :

 - the `Root identifier` 
 - the `Cost` to reach the root
 - the `Transmitter identifier`

The third information contains two parts : the identifier of the switch that sent the BPDU and the identifier of the port where the BPDU has been sent. Each switch uses a unique identifier for each of its ports. 

.. question:: stp1
   :nb_prop: 4
   :nb_pos: 2          

   Select among the list below *all* the BPDUs that are better than ``[R=123,C=17,T=15.4]``

   .. positive:: ``[R=123,C=11,T=16.9]``

      .. comment:: The two BPDUs have the same Root, but this BPDU has a lower cost.

   .. positive:: ``[R=122,C=21,T=19]``

      .. comment:: This BPDU has a smaller root. 

   .. positive:: ``[R=123,C=17,T=15.1]``

      .. comment:: The two BPDUs have the same Root, the same cost but this BPDU has a lower Transmitter identifier.

   .. positive:: ``[R=123,C=17,T=12.19]``

      .. comment:: The two BPDUs have the same Root, the same cost but this BPDU has a lower Transmitter identifier.

   .. negative:: ``[R=126,C=11,T=6.9]``

      .. comment:: This BPDU has a smaller root identifier.

   .. negative:: ``[R=123,C=21,T=19]``

      .. comment:: This BPDU has the same root, but a higher cost.

   .. negative:: ``[R=123,C=17,T=25.1]``

      .. comment:: The two BPDUs have the same Root, the same cost but this BPDU has a  higher Transmitter identifier.

   .. negative:: ``[R=123,C=17,T=22.19]``

      .. comment:: The two BPDUs have the same Root, the same cost but this BPDU has a larger Transmitter identifier.

2. Consider a large Ethernet network that contains the switches shown in the figure below.

    .. tikz::
       :libs: positioning, matrix, arrows, shapes 

       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{switch/.style = {diamond, draw, text centered, minimum height=2em, node distance=2cm}, }
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       [node distance= 4cm and 4cm]
       \node[switch] (S32) {S32};
       \node[switch, left of=S32] (S22) {S22};
       \node[switch, right of=S32] (S19) {S19};
       \node[switch, above of=S32] (S42) {S42};
       \node[switch, below of=S32] (S25) {S25};
       \node[switch, right of=S25] (S46) {S46};

       \path[draw,thick]
       (S32) edge (S22) 
       (S32) edge (S19) 
       (S32) edge (S42) 
       (S32) edge (S25)
       (S32) edge (S46); 


 Switch ``32`` has received the following BPDUs from its neighbours :

  - ``[R=9,C=21,T=19.2]``
  - ``[R=9,C=12,T=42.1]``
  - ``[R=25,C=5,T=25.2]``
  - ``[R=9,C=5,T=46.3]``

.. question:: stp2
   :nb_prop: 3
   :nb_pos: 1          

   Which is the ``BPDU`` of switch ``32`` assuming that all links have a cost of ``1`` ?

   .. positive:: ``[R=9,C=6,T=32]``

   .. negative:: ``[R=25,C=6,T=25]``

      .. comment:: The root of this network cannot be switch ``25``.

   .. negative:: ``[R=9,C=6,T=25]``

      .. comment:: The BPDU of a switch has the switch has its transmitting identifier. 

   .. negative:: ``[R=9,C=6,T=19.32]``

      .. comment:: The BPDU of a switch has the switch has its transmitting identifier. 

   .. negative:: ``[R=9,C=5,T=32]``

      .. comment:: The cost towards the root must be incremented with the cost of the link over which the BPDU has been received.


3. Consider the same network as above. Assume now that switch ``32`` has received the following BPDUs from its neighbours :

  - ``[R=9,C=6,T=19.2]``
  - ``[R=9,C=12,T=42.1]``
  - ``[R=9,C=5,T=25.2]``
  - ``[R=9,C=5,T=46.3]``

   .. BPDU : ``[R=9,C=6,T=32]`` best is 25

.. question:: stp3
   :nb_prop: 3
   :nb_pos: 1          

   Which of the following affirmations about the state of the ports of switch ``32`` is correct ? 

   .. positive:: The port towards switch ``25`` is the `root port` of the switch and the ports towards switches ``42``, ``19`` and ``46`` are `blocked`. 

   .. negative:: The port towards switch ``25`` is the `root port` of the switch. The ports towards switch ``19`` is `blocked` and the ports towards switches ``42`` and ``46`` are `designated`. 

   .. negative:: The port towards switch ``19`` is the `root port` of the switch. The ports towards switch ``46`` is `blocked` and the ports towards switches ``42`` and ``25`` are `designated`. 

   .. negative:: The port towards switch ``25`` is the `root port` of the switch. The ports towards switches ``46``, ``42`` and ``25`` are `designated`. 


4. Consider the switched network shown in the figure below.

    .. tikz::
       :libs: positioning, matrix, arrows, shapes 

       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{switch/.style = {diamond, draw, text centered, minimum height=2em, node distance= 2cm}, }
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \node[switch] (S3) {S3};
       \node[switch, left of=S3] (S6) {S6};
       \node[switch, right of=S3] (S7) {S7};
       \node[switch, above of=S3] (S4) {S4};
       \node[switch, below of=S3] (S9) {S9};
 
       \path[draw,thick]
       (S3) edge (S6) 
       (S3) edge (S7) 
       (S6) edge (S4) 
       (S4) edge (S7)
       (S3) edge (S9)
       (S9) edge (S7)
       (S3) edge (S7); 


.. question:: stp4
   :nb_prop: 3
   :nb_pos: 1          

   Assuming that all the links have a cost of ``1``, which switch will become the root of the spanning tree ?

   .. positive:: Switch ``3`` becomes the root of the spanning tree. 

   .. negative:: Switch ``6`` becomes the root of the spanning tree. 

   .. negative:: Switch ``7`` becomes the root of the spanning tree. 

   .. negative:: Switch ``9`` becomes the root of the spanning tree. 

   .. negative:: Switch ``4`` becomes the root of the spanning tree. 


5. Consider the same network as in the above question. 

.. question:: stp5
   :nb_prop: 8
   :nb_pos: 5          

   Select *all* the valid affirmations about the state of the ports of the different switches.

   .. positive:: The port of ``S3`` that leads to ``S6`` is in the designated state.
      
      .. comment:: All the ports of the root switch are in the designated state.

   .. positive:: The port of ``S3`` that leads to ``S9`` is in the designated state.  

      .. comment:: All the ports of the root switch are in the designated state.  

   .. positive:: The port of ``S3`` that leads to ``S7`` is in the designated state. 

      .. comment:: All the ports of the root switch are in the designated state. 

   .. positive:: The port of ``S6`` that leads to ``S3`` is a root port.

   .. positive:: The port of ``S9`` that leads to ``S3`` is a root port.

   .. positive:: The port of ``S7`` that leads to ``S3`` is a root port.

   .. positive:: The port of ``S6`` that leads to ``S4`` is in the designated state. 

   .. positive:: The port of ``S7`` that leads to ``S4`` is in the designated state. 

   .. positive:: The port of ``S7`` that leads to ``S9`` is in the designated state. 

   .. negative:: The port of ``S4`` that leads to ``S6`` is in the blocked state. 

   .. positive:: The port of ``S4`` that leads to ``S7`` is in the blocked state. 

   .. positive:: The port of ``S9`` that leads to ``S7`` is in the blocked state.


   .. negative:: The port of ``S6`` that leads to ``S4`` is in the blocked state. 

      .. comment:: This port is a designated port. The BPDU of switch ``S6`` is better than the BPDU of switch ``S4``.

   .. negative:: The port of ``S7`` that leads to ``S4`` is in the blocked state. 

      .. comment:: This port is a designated port. The BPDU of switch ``S7`` is better than the BPDU of switch ``S4``.

   .. negative:: The port of ``S7`` that leads to ``S9`` is in the blocked state. 

      .. comment:: The BPDU of switch ``S7`` is better than the BPDU of switch ``S9``.

   .. negative:: The port of ``S4`` that leads to ``S6`` is in the designated state. 

      .. comment:: The BPDU of switch ``S4`` is worse than the BPDU of switch ``S6``.

   .. negative:: The port of ``S4`` that leads to ``S7`` is in the designated state. 

      .. comment:: The BPDU of switch ``S4`` is worse than the BPDU of switch ``S7``.

   .. negative:: The port of ``S9`` that leads to ``S7`` is in the designated state.

      .. comment:: The BPDU of switch ``S9`` is worse than the BPDU of switch ``S7``.


6. Ethernet switches can also be connected to a HUB. Consider the Ethernet network below.


    .. tikz::
       :libs: positioning, matrix, arrows, shapes 

       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{switch/.style = {diamond, draw, text centered, minimum height=2em, node distance= 2cm}, }
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{hub/.style = {circle, draw, text centered, minimum height=2em, node distance=2cm}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \node[switch] (S9) {S9};
       \node[switch, left of=S9] (S12) {S12};
       \node[switch, right of=S9] (S6) {S6};
       \node[switch, above of=S9] (S3) {S3};
       \node[hub, below of=S9] (HUB) {HUB};
 
       \path[draw,thick]
       (S3) edge (S12) 
       (S12) edge (HUB) 
       (S6) edge (S3) 
       (S6) edge (HUB)
       (S3) edge (S9)
       (S9) edge (HUB);

.. question:: stp6
   :nb_prop: 5
   :nb_pos: 3          

   Select all the affirmations that are correct about the states of the different switches attached to the Hub. 

   .. positive:: The port of switch ``6`` attached to the Hub is a designated port.

   .. positive:: The port of switch ``9`` attached to the Hub is a blocked port.

   .. positive:: The port of switch ``12`` attached to the Hub is a blocked port.

   .. negative:: The port of switch ``12`` attached to the Hub is a designated port. 

      .. comment:: The BPDU of this switch is worse than the BPDU of switch ``6``. 


   .. negative:: The port of switch ``9`` attached to the Hub is a designated port. 

      .. comment:: The BPDU of this switch is worse than the BPDU of switch ``6``. 

   .. positive:: The port of switch ``6`` attached to the Hub is a blocked  port.



