.. Copyright |copy| 2014 by Olivier Bonaventure
.. This file is licensed under a
   `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



Routing protocols
-----------------

:task_id: networkrouting

.. question:: dv1
   :nb_prop: 4
   :nb_pos: 2

   1. Consider the network represented in the figure below. Assume that the
      network is using a distance vector protocol as its routing protocol
      When the network boots, which of the following distance vectors
      correspond to the first vector
      that each router sends ? We assume that the link weights are configured on
      the routers as shown in the figure. We consider a basic version of
      distance routing without split horizon and without poisoning. What
      are all the correct distance vectors among the choices below ?

      .. tikz::
         :libs: positioning, matrix, arrows

         \tikzstyle{arrow} = [thick,->,>=stealth]
         \tikzset{router/.style = {rectangle, draw, text centered,minimum height=2em}, }
         \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
         \tikzset{ftable/.style={rectangle, dashed, draw} }
         \node[router] (R1) { R1 };
         \node[router,right=of R1] (R2) {R2};
         \node[router,below=of R1] (R3) {R3};
         \node[router,below=of R2] (R4) {R4};
         \path[draw,thick]
         (R3) edge node [midway,fill=white] {\em{3}} (R2)
         (R1) edge (R2)
         (R1) edge (R3)
         (R2) edge (R4);

   .. negative:: Router `R1` sends `[ R1=0, R2=1, R3=1]`

      .. comment:: When a distance vector router boots, it only knows itself at a distance of `0`.

   .. negative:: Router `R2` sends `[ R2=0, R1=1, R3=3, R4=1]`

      .. comment:: When a distance vector router boots, it only knows itself at a distance of `0`.

   .. negative:: Router `R3` sends `[ R3=0, R1=1, R2=3]`

      .. comment:: When a distance vector router boots, it only knows itself at a distance of `0`.

   .. negative:: Router `R4` sends `[ R4=0, R2=1, R3=3, R4=1]`

      .. comment:: When a distance vector router boots, it only knows itself at a distance of `0`.

   .. positive:: Router `R4` sends `[ R4=0 ]`

   .. positive:: Router `R3` sends `[ R3=0 ]`

   .. positive:: Router `R2` sends `[ R2=0 ]`

   .. positive:: Router `R1` sends `[ R1=0 ]`


.. question:: dv2
   :nb_prop: 4
   :nb_pos: 2

   2. Consider the same network as in the previous question. The network has been running for several hours. Among the following answers, what are the distance vectors that are produced by the routers at that time ?



   .. negative:: Router `R1` sends `[ R1=0, R2=1, R3=1]`

      .. comment:: A router always sends a summary of its routing table. After several hours, `R1` already knows how to reach `R4`.

   .. positive:: Router `R2` sends `[ R2=0, R1=1, R3=3, R4=1]`

   .. negative:: Router `R3` sends `[ R3=0, R1=1, R2=3]`

      .. comment:: A router always sends a summary of its routing table. After several hours, `R3` already knows how to reach `R4`.

   .. positive:: Router `R4` sends `[ R4=0, R2=1, R3=3, R4=1]`

   .. negative:: Router `R4` sends `[ R4=0 ]`

      .. comment:: A router always sends a summary of its entire routing table. This is not the case here.

   .. negative:: Router `R3` sends `[ R3=0 ]`

      .. comment:: A router always sends a summary of its entire routing table. This is not the case here.

   .. negative:: Router `R2` sends `[ R2=0 ]`

      .. comment:: A router always sends a summary of its entire routing table. This is not the case here.

   .. positive:: Router `R1` sends `[ R1=0 ]`

      .. comment:: A router always sends a summary of its entire routing table. This is not the case here.


.. question:: ls1
   :nb_prop: 4
   :nb_pos: 2

   3. Consider the network shown in the figure below.

       .. tikz::
          :libs: positioning, matrix, arrows

          \tikzstyle{arrow} = [thick,->,>=stealth]
          \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
          \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
          \tikzset{ftable/.style={rectangle, dashed, draw} }
          \node[router] (R1) { R1 };
          \node[router,right=of R1] (R2) {R2};
          \node[router,below=of R1] (R3) {R3};
          \node[router,above=of R2] (R4) {R4};
          \path[draw,thick]
          (R3) edge node [midway,fill=white] {\em{3}} (R2)
          (R1) edge (R2)
          (R1) edge (R3)
          (R2) edge (R4)
          (R4) edge (R1);

   Among the link state packets shown below, which corresponds to link state packets that could be transmitted by the nodes of this network ? Select all the valid answers.



   .. positive:: Router `R1` sends LSP : `R1-0 [R2:1] [R3:1] [R4:1]`

   .. positive:: Router `R2` sends LSP : `R2-0 [R2:1] [R3:3] [R4:1]`

   .. positive:: Router `R3` sends LSP : `R3-0 [R1:1] [R2:3]`

   .. positive:: Router `R4` sends LSP : `R4-0 [R1:1] [R2:1]`

   .. negative:: Router `R3` sends LSP : `R3-0 [R1:1] [R2:3] [R4:3]`

      .. comment:: The link state packet contains the information about the direct neighbours of a network node. `R3` is not directly attached to `R4`.

   .. negative:: Router `R4` sends LSP : `R4-0 [R1:1] [R2:1] [R3:3]`

      .. comment:: The link state packet contains the information about the direct neighbours of a network node. `R4` is not directly attached to `R3`.






.. include:: /links.rst
