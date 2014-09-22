.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Virtual circuits
----------------

:task_id: networkvc

.. question:: vc1
   :nb_prop: 3
   :nb_pos: 1

   1. In a network that uses virtual circuits, the forwarding paths depend on the label tables installed inside each network node. 

    .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[router, right=of A] (R1) { R1 };
      \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline
      1 & E & 2 \\
      2 & W & 1 \\
      3 & S & 3 \\
      \end{tabular}};
      \node[router,right=of R1] (R2) {R2};
      \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline 
      1 & S-W & 4 \\
      2 & W & 2 \\
      \end{tabular}\\};
      \node[router,below=of R1] (R3) {R3};
      \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline
      1 & N-E & 1 \\
      3 & N-E & 2 \\
      4 & E & 1 \\
      \end{tabular}\\};
      \node[host, right=of R3] (B) {B};
      \path[draw,thick]
      (A) edge (R1) 
      (R1) edge (R2) 
      (R2) edge (R3) 
      (R1) edge (R3)
      (R3) edge (B); 
      \draw[arrow, dashed] (FR1) -- (R1); 
      \draw[arrow, dashed] (FR2) -- (R2); 
      \draw[arrow, dashed] (FR3) -- (R3); 

   In this network, only one of the affirmations about the forwarding paths is correct. Which one ?

   .. positive:: To reach `B`, `A` must send packets with `label=2` and the path is `R1->R2->R3`

   .. positive:: To reach `A`, `B` must send packets with `label=3` and the path is `R3->R2->R1` 

   .. negative:: To reach `B`, `A` must send packets with `label=3` and the path is `R1->R3`

      .. comment:: This path is incorrect. If `A` sends a packet with `label=3`, the packet will follow the path `R1->R3->R2->R1` and return to `A`. 

   .. negative:: To reach `A`, `B` must send packets with `label=1` and the path is `R3->R2->R1` 

      .. comment:: This path is incorrect. If `B` sends a packet with `label=1`, the packet will follow the path `R3->R2` and will loop on link `R2-R3`


.. question:: vcSym
   :nb_prop: 3 
   :nb_pos: 1 

   2. The forwarding paths used in a virtual circuits network depend on the label forwarding tables installed in the network nodes. Sometimes, these tables must be configured manually. 

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[router, right=of A] (R1) { R1 };
      \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline 
      1 & W & 1 \\
      2 & S & 2 \\
      3 & E & 3 \\
      \end{tabular}};
      \node[router,right=of R1] (R2) {R2};

      \node[router,below=of R1] (R3) {R3};

      \node[router,below=of R2] (R4) {R4};
      \node[ftable, below right=of R4] (FR4) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline 
      1 & E & 4 \\
      2 & N & 5 \\
      3 & W & 6 \\
      \end{tabular}\\};
      \node[host, right=of R4] (B) {B};

      \path[draw,thick]
      (A) edge (R1) 
      (R1) edge (R2) 
      (R2) edge (R3) 
      (R1) edge (R3) 
      (R4) edge (R3) 
      (R2) edge (R4) 
      (R4) edge (B); 

      \draw[arrow, dashed] (FR1) -- (R1); 
      \draw[arrow, dashed] (FR4) -- (R4); 

   In this network, which of the label forwarding tables below ensures that : 

     - `A` and `B` can exchange packets in both directions.
     - the path from `A` to `B` is the reverse of the path from `B` to `A`

   .. positive:: To reach `B`, `A` sends packet with `label=2`. To reach `A`, `B` sends packets with `label=3`.  New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        E       1 
       6        N       1 
       ======== ======= ========


      New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       3        S-W     2 
       5        W       2 
       ======== ======= ========


   .. positive:: To reach `B`, `A` sends packet with `label=3`. To reach `A`, `B` sends packets with `label=2`. New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       5        W       1 
       6        S       1 
       ======== ======= ========


      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       3        N-W     2 
       5        N       2 
       ======== ======= ========

   .. negative:: To reach `B`, `A` sends packet with `label=2`. To reach `A`, `B` sends packets with `label=2`.  New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       5        W       1 
       6        S       1 
       ======== ======= ========


      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        E       1 
       5        N       2 
       ======== ======= ========

      .. comment:: With these label forwarding tables, the path from `A` to `B` is not the reverse of the path from `B` to `A`.

   .. negative:: To reach `B`, `A` sends packet with `label=3`. To reach `A`, `B` sends packets with `label=3`. New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       5        W       1 
       3        S       1 
       ======== ======= ========


      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       6        N-W     5 
       5        N       2 
       ======== ======= ========

      .. comment:: With these label forwarding tables, the path from `A` to `B` is not the reverse of the path from `B` to `A`.


   .. negative:: To reach `B`, `A` sends packet with `label=2`. To reach `A`, `B` sends packets with `label=3`. New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        S       1 
       1        W       1 
       ======== ======= ========

      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       6        N       1 
       1        E       1 
       ======== ======= ========

      .. comment:: The packets sent by `A` towards `B` reach `R3` which sends them to `R2` that returns them to `R1`.



3. The forwarding paths used in a virtual circuits network depend on the label forwarding tables installed in the network nodes. Sometimes, these tables must be configured manually. 

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[router, right=of A] (R1) { R1 };
      \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline 
      1 & W & 1 \\
      2 & S & 1 \\
      3 & E & 2 \\
      \end{tabular}};
      \node[router,right=of R1] (R2) {R2};

      \node[router,below=of R1] (R3) {R3};

      \node[router,below=of R2] (R4) {R4};
      \node[ftable, below right=of R4] (FR4) { \begin{tabular}{l|l|l} 
      InLabel & OutPort & OutLabel \\
      \hline 
      1 & E & 1 \\
      2 & N & 1 \\
      3 & W & 3 \\
      \end{tabular}\\};
      \node[host, right=of R4] (B) {B};

      \path[draw,thick]
      (A) edge (R1) 
      (R1) edge (R2) 
      (R2) edge (R3) 
      (R1) edge (R3) 
      (R4) edge (R3) 
      (R2) edge (R4) 
      (R4) edge (B); 

      \draw[arrow, dashed] (FR1) -- (R1); 
      \draw[arrow, dashed] (FR4) -- (R4); 

.. question:: vcAdd
   :nb_prop: 3
   :nb_pos: 1

   In this network, which of the label forwarding tables below ensures that- `A` and `B` can exchange packets in both directions.


   .. positive:: To reach `B`, `A` sends packet with `label=3`. To reach `A`, `B` sends packets with `label=2`. New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        S       1 
       1        W       1 
       ======== ======= ========

      The label forwarding table for `R3` remains empty. 


   .. positive:: To reach `B`, `A` sends packet with `label=3`. To reach `A`, `B` sends packets with `label=3`. New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        S-W     4 
       ======== ======= ========

      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       4        E       1 
       1        N       1 
       ======== ======= ========


   .. negative:: To reach `B`, `A` sends packet with `label=2`. To reach `A`, `B` sends packets with `label=1`. New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        S       1 
       1        W       1 
       ======== ======= ========

      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        E       1 
       1        N       1 
       ======== ======= ========

      .. comment:: The packets sent by `A` towards `B` reach `R3` which returns them to `R1`.

   .. negative:: To reach `B`, `A` sends packet with `label=3`. To reach `A`, `B` sends packets with `label=2`. 
 New label forwarding table for `R2`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       2        S-W     4 
       1        S-W     2 
       ======== ======= ========

      New label forwarding table for `R3`:

       ======== ======= ========
       InLabel  OutPort OutLabel 
       ======== ======= ========
       4        E       1 
       2        E       2 
       ======== ======= ========

      .. comment:: There is also a loop with these label forwarding tables. 
