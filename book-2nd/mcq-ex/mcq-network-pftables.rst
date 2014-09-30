.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


Port forwarding tables
----------------------

:task_id: networkpftable

Port forwarding tables are used in tree-shaped networks to automatically build the forwarding tables that allow the network nodes to forward packets towards their destinations.


 .. question:: portforwarding0 
   :nb_prop: 3 
   :nb_pos: 2 

   1. Consider the tree-shaped network shown in the figure below. Assume that the port-forwarding tables are as shown in the figure.

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[router, right=of A] (R1) { R1 };
      \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
      Dest. & OutPort  \\
      \hline 
      A & W \\
      \end{tabular}};
      \node[router,right=of R1] (R2) {R2};
      \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l} 
      Dest. & OutPort \\
      \hline 
      A & W \\
      \end{tabular}\\};
      \node[router,below=of R1] (R3) {R3};
      \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l} 
      Dest. & OutPort \\
      \hline 
      A & N  \\
      \end{tabular}\\};
      \node[host, right=of R3] (B) {B};
      \node[host, left=of R3] (C) {C};

      \path[draw,thick]
      (A) edge (R1) 
      (R1) edge (R2) 
      (R1) edge (R3) 
      (R3) edge (B)
      (C) edge (R3); 

      \draw[arrow, dashed] (FR1) -- (R1); 
      \draw[arrow, dashed] (FR2) -- (R2); 
      \draw[arrow, dashed] (FR3) -- (R3); 


   Which of the following affirmations are true ?

   .. positive:: If `C` sends a packet towards `A`, `R3` will immediately forward it on its `North` interface

   .. positive:: If `B` sends a packet towards `C`, `R3` will immediately forward it on its `West` interface

   .. positive:: If `A` sends a packet towards `C`, `R1` will send it to both its `East` and `South` interfaces. 

   .. positive:: If `A` sends a packet towards `B`, `R1` will send it to both its `East` and `South` interfaces. 
         
   .. negative:: If `A` sends a packet towards `B`, `R1` will send it only to its `East` interface. 
                 
      .. comment:: Since `R1` does not know how to reach destination `B`, it must send the packets on all interfaces except the one from which it has been received.           


   .. negative:: If `A` sends a packet towards `C`, `R1` will send it only to its `South` interface. 

      .. comment:: Since `R1` does not know how to reach destination `C`, it must send the packets on all interfaces except the one from which it has been received.           

   .. negative:: If `R1` receives from `R3` a packet whose destination is `A`, it sends it on both its `West` and `East` interfaces. 


 .. question:: portforwarding1
   :nb_prop: 3
   :nb_pos: 2

   2. Consider the tree-shaped network shown in the figure below. Assume that `A` has sent a packet towards `B` but `B` has not yet replied.

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[router, right=of A] (R1) { R1 };
      \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
      Dest. & OutPort  \\
      \hline
      A & W \\
      \end{tabular}};
      \node[router,right=of R1] (R2) {R2};
      \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l} 
      Dest. & OutPort \\
      \hline 
      A & W \\
      \end{tabular}\\};
      \node[router,below=of R1] (R3) {R3};
      \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l} 
      Dest. & OutPort \\
      \hline
      A & N  \\
      \end{tabular}\\};
      \node[host, below=of R2] (B) {B};


      \path[draw,thick]
      (A) edge (R1) 
      (R1) edge (R2) 
      (R2) edge (R3) 
      (R2) edge (B); 

      \draw[arrow, dashed] (FR1) -- (R1); 
      \draw[arrow, dashed] (FR2) -- (R2); 
      \draw[arrow, dashed] (FR3) -- (R3); 


      `B` sends a reply to `A`. Which of the following affirmations are true ?

   .. positive::    

      Upon reception of this packet, the port forwarding table of `R3` will be updated as :

      ======  ========
      Dest.   OutPort 
      ======  ========
      A       N 
      B       E 
      ======  ========


   .. positive::    

      Upon reception of this packet, the port forwarding table of `R1` will be updated as :

      ======  ========
      Dest.   OutPort 
      ======  ========
      A       W 
      B       S 
      ======  ========

   .. negative::    

      Upon reception of this packet, the port forwarding table of `R2` will be updated as :

      ======  ========
      Dest.   OutPort 
      ======  ========
      A       W 
      B       W 
      ======  ========

      .. comment:: When `R1` receives the packet sent by `B` towards `A`, it forwards it directly to `A`. This implies that `R2` will not receive this packet and thus cannot update its port forwarding table. 

   .. positive::    

      The port forwarding table of `R2` will never be updated with information about destination `B`. 

   .. negative::    

      Upon reception of this packet, the port forwarding table of `R3` will be updated as :

      ======  ========
      Dest.   OutPort 
      ======  ========
      A       N 
      B       N 
      ======  ========
