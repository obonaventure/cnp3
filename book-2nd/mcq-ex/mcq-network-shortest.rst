.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



Shortest paths
--------------

:task_id: networkshortest 


1. Consider the network below.

   .. tikz::
      :libs: positioning, matrix, arrows

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[router] (R1) { R1 };
      \node[router,right=of R1] (R2) {R2};
      \node[router,below=of R1] (R3) {R3};
      \node[router,below=of R2] (R4) {R4};
      \path[draw,thick]
      (R1) edge node [midway,fill=white] {\em{3}} (R2)
      (R3) edge node [midway,fill=white] {\em{3}} (R2)
      (R1) edge node [midway, fill=white] {\em{2}} (R3)
      (R4) edge (R3)
      (R2) edge (R4);

.. question:: shortest1
   :nb_prop: 3
   :nb_pos: 2

   Given the link weights shown in the figure above, which of the following affirmations about the shortest paths in this network are correct ? 

   .. positive:: The shortest path from `R4` to `R1` is via `R3`. 

   .. positive:: The shortest path from `R2` to `R3` is via `R4`. 

   .. negative:: The shortest path from `R1` to `R2` is via `R3`. 

   .. negative:: The shortest path from `R3` to `R2` is the direct link. 

   .. positive:: The shortest path from `R3` to `R2` is via `R4`. 

   .. negative:: The shortest path from `R1` to `R4` is via `R3`. 

.. question:: shortest2
   :nb_prop: 3
   :nb_pos: 2

   2. Consider the network shown in the figure below.  

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[router] (R1) { R1 };
      \node[router,right=of R1] (R2) {R2};
      \node[router,below=of R1] (R3) {R3};
      \node[router,below=of R2] (R4) {R4};
      \path[draw,thick]
      (R1) edge node [midway,fill=white] {\em{3}} (R2) 
      (R3) edge node [midway,fill=white] {\em{3}} (R2) 
      (R1) edge node [midway, fill=white] {\em{2}} (R3) 
      (R4) edge (R3) 
      (R2) edge (R4); 


   Given the link weights shown in the figure above, which of the following affirmations about the shortest paths in this network are correct ? 

   .. positive:: The shortest path from `R4` to `R1` is via `R3`. 

   .. positive:: The shortest path from `R2` to `R3` is via `R4`. 

   .. negative:: The shortest path from `R1` to `R2` is via `R3`. 

   .. negative:: The shortest path from `R3` to `R2` is the direct link. 

   .. positive:: The shortest path from `R3` to `R2` is via `R4`. 

   .. negative:: The shortest path from `R1` to `R4` is via `R3`. 

