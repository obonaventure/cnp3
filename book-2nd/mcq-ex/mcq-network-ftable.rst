.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



******************
Building a network
******************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 

.. _mcq-network:


Multiple choice questions
=========================


Building forwarding tables
--------------------------

:task_id: networkftable

1. The forwarding paths used in a network depend on the forwarding tables installed in the network nodes. Consider the network shown below with the forwarding tables.

    .. tikz::
       :libs: positioning, matrix, arrows 

       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \node[host] (A) {A};
       \node[router, right=of A] (R1) { R1 };
       \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
       Dest. & Port \\
       \hline
       A & W \\
       B & E \\
       \end{tabular}};
       \node[router,right=of R1] (R2) {R2};
       \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l} 
       Dest. & Port \\
       \hline 
       A & W \\
       B & S-W \\
       \end{tabular}\\};
       \node[router,below=of R1] (R3) {R3};
       \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l} 
       Dest. & Port \\
       \hline
       A & N \\
       B & E \\
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
 
.. question:: ftable1
   :nb_prop: 3
   :nb_pos: 1          

   In this network, only one of the affirmations about the forwarding paths is correct. Which one ?

   .. positive:: The path from `A` to `B` is `R1->R2->R3`

   .. positive:: The path from `B` to `A` is `R3->R1`

   .. negative:: The path from `B` to `A` is `R3->R2->R1`

   .. negative:: The path from `A` to `B` is `R1->R3`




2. The forwarding paths used in a network depend on the forwarding tables installed in the network nodes. Sometimes, these forwarding tables must be configured manually. 

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
        Dest. & Port \\
        \hline 
        A & W \\
        B & S \\
        \end{tabular}};
        \node[router,right=of R1] (R2) {R2};

        \node[router,below=of R1] (R3) {R3};

        \node[router,below=of R2] (R4) {R4};
        \node[ftable, below right=of R4] (FR4) { \begin{tabular}{l|l} 
        Dest. & Port \\
        \hline 
        A & N \\
        B & E \\
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

.. question:: ftableAdd
   :nb_prop: 3 
   :nb_pos: 1 

   In this network, which of the forwarding tables below ensures that both :

     - `A` and `B` can exchange packets in both directions 
     - the path from `A` to `B` is the reverse of the path from `B` to `A` 

   .. positive:: New forwarding table for `R3`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      N 
       B      N-E 
       ====== =====

      New forwarding table for `R2`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      S-W 
       B      S 
       ====== =====

   .. negative:: New forwarding table for `R3`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      N-E 
       B      N-E 
       ====== =====

      New forwarding table for `R2`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      S-W 
       B      S 
       ====== =====

      .. comment:: There is a forwarding loop with this forwarding table. `B` cannot reach `A` because the packets that it sends loop on the `R2-R3` link. 


   .. negative:: New forwarding table for `R3`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      N 
       B      N-E 
       ====== =====

      New forwarding table for `R2`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      E 
       B      S-W 
       ====== =====

      .. comment:: There is a forwarding loop with this forwarding table. `A` cannot reach `B` because the packets that it sends loop on the `R2-R3` link. 


   .. negative:: New forwarding table for `R3`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      N 
       B      E 
       ====== =====

      New forwarding table for `R2`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      E 
       B      S 
       ====== =====

      .. comment:: The path from `A` to `B` is not the reverse of the path from `B` to `A` with these forwarding tables.



3. The forwarding paths used in a network depend on the forwarding tables installed in the network nodes. Sometimes, these forwarding tables are configured manually and an incorrect configuration may cause some paths to be impossible. 

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[router, right=of A] (R1) { R1 };
      \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
      Dest. & Port \\
      \hline 
      A & W \\
      B & E \\
      \end{tabular}};
      \node[router,right=of R1] (R2) {R2};
      \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l} 
      Dest. & Port \\
      \hline 
      A & S-W \\
      B & S-W \\
      \end{tabular}\\};
      \node[router,below=of R1] (R3) {R3};
      \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l} 
      Dest. & Port \\
      \hline 
      A & E \\
      B & E \\
      \end{tabular}\\};
      \node[router,below=of R2] (R4) {R4};
      \node[ftable, below right=of R4] (FR4) { \begin{tabular}{l|l} 
      Dest. & Port \\
      \hline 
      A & N \\
      B & E \\
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
      \draw[arrow, dashed] (FR2) -- (R2); 
      \draw[arrow, dashed] (FR3) -- (R3); 
      \draw[arrow, dashed] (FR4) -- (R4); 

.. question:: ftableErr 
   :nb_prop: 3 
   :nb_pos: 1          

   In this network, `A` can send packets to `B`, but when `B` sends a packet to `A`, this packet never reaches its destination. Among the following forwarding tables, which is the one that ensures that `A` can exchange packets with `B` ? 

   .. positive:: New forwarding table for `R3`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      N 
       B      E 
       ====== =====

   .. positive:: New forwarding table for `R2`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      W 
       B      S 
       ====== =====


   .. negative:: New forwarding table for `R4`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      W 
       B      E 
       ====== =====

   .. negative:: New forwarding table for `R2`:

       ====== =====
       Dest.  Port 
       ====== =====
       A      W 
       B      S-W 
       ====== =====

