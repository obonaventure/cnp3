.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_




.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 

.. _mcq-ipv6:



Multiple choice questions
=========================
:task_id: mcqipv6bis

1. The IPv6 packet header includes several fields that are shown in the figure below.

   .. figure:: /../../book/network/pkt/ipv6.png
      :align: center
      :scale: 100

.. question:: ipv6packet
   :nb_prop: 3
   :nb_pos: 1

   Among the following affirmations about the role of these different fields, only one is *incorrect*. Select the incorrect affirmation.

   .. positive:: A router never changes any field of an IPv6 packet that it forwards.

      .. comment:: This affirmation is incorrect. A router changes the Hop-Limit of the packets that it forwards. It may also change other fields such as the TClass, but this is outside the scope of this ebook.

   .. positive:: When a host sends an IPv6 packet, its HopLimit is always set to zero. Routers increment the value of this field for each packet that they forward.

      .. comment:: This affirmation is incorrect. A host sends packets with a positive HopLimit and routers decrement this field. 

   .. negative:: A router always decrements the HopLimit of all forwarded IPv6 packets.
   
      .. comment:: This affirmation is correct. 
 
   .. negative:: To forward a packet, a router always looksup the destination address inside its forwarding table.

      .. comment:: This affirmation is correct. 

   .. negative:: The NextHeader field of the IPv6 packet identifies the type of transport segment contained in the packet.
                  

2. The IPv6 addresses are 128 bits wide and can be represented by using the hexadecimal representation defined in :rfc:`5952`.

.. question:: ip6addre
   :nb_prop: 5
   :nb_pos: 3


   Among the following textual representations, select all the ones that correspond to a valid IPv6 address.

   .. positive:: ``2001:db8:0:0:1::1``

   .. positive:: ``2001:db8:a:bb:cc:ddd::1``

   .. negative:: ``2001:db8:a:bb:cc:ddd:eeee::1``
   
      .. comment:: This address is invalid. The textual representation of an IPv6 address cannot contain more than 7 individual fields if we two semi columns ``::``

   .. negative:: ``2001:db8:a:bb:cc:ddddd::1``

      .. comment:: This address is invalid. The textual representation of an IPv6 address cannot contain more than 4 hexadecimal characters between two semi columns ``:``

   .. negative:: ``2001:db8:a:bb::cc:ddd::1``

      ..comment:: This address is invalid. An IPv6 address cannot contain twice two consecutive semicolumns ``::``

   .. positive:: ``2001:db8:1234:1234:1234:5678::1``

   .. positive:: ``2001:db8:1234::1234:5678:abc:1``

   .. positive:: ``2001:db8:1234:5678::abc:1``

   .. negative:: ``2001:dg8:1234:abcd::cafe``

      .. comment:: This address is invalid. An IPv6 address can only contain digits and letters ``a-f``.

   .. negative:: ``2001:dead:beef:bad:cafe:1234:abcd:cafe:1``

      .. comment:: This address is invalid. An IPv6 address is 128 bits long. This representation is 144 bits long.

.. question:: ipv6addrb
   :nb_prop: 4
   :nb_pos: 2

   3. Among the textual representation for IPv6 addresses below, select all the ones that correspond to IPv6 address ``2001:db8:0:0:a::cafe``.

   .. positive::  ``2001:db8:0:0:a:0:0:cafe``

   .. positive::  ``2001:db8:0:0:a::cafe``

   .. positive::  ``2001:0db8:0:0:a::cafe``

   .. positive::  ``2001:0db8:0000:0000:000a::cafe``

   .. positive::  ``2001:0db8::a:0:0:cafe``

   .. negative::  ``2001:0db8::a::cafe``

      .. comment:: This IPv6 address is ambiguous. An IPv6 address cannot contain twice two successive semi-columns ``::``.

   .. negative:: ``2001:db8:0:0:a000::cafe``

      .. comment:: This IPv6 address does not correspond to ``2001:db8:0:0:a::cafe``. In this address, the ``a`` 16 bits block corresponds to the following binary representation ``0000 0000 0000 1010`` while the binary representation for ``a000`` is ``1010 0000 0000 0000``.

   .. negative:: ``2001:db80:0:0:a::cafe``

      .. comment:: This IPv6 address does not correspond to ``2001:db8:0:0:a::cafe``. In this address, the ``db8`` 16 bits block corresponds to the following binary representation ``0000 1101 1011 1000`` while the binary representation for ``db80`` is ``1101 1011 1000 0000``.


4. The forwarding tables used in an IPv6 network define the forwarding paths that are used for the packets. Consider the simple network depicted in the figure below. In this network, the hosts have the following addresses :

 - host ``A`` : ``2001:db8:1341:1::A`` and its default route points to ``2001:db8:1341:1::1``
 - host ``B`` : ``2001:db8:1341:3::B`` and its default route points to ``2001:db8:1341:3::3``

The routers have one address inside each network :

 - router ``R1`` uses address ``2001:db8:1341:1::1`` on its West interface, address ``2001:db8:1341:12::1`` on its East interface and address ``2001:db8:1341:13::1`` on its South interface
 - router ``R2`` uses address ``2001:db8:1341:12::2`` on its West interface and address ``2001:db8:1341:23::2`` on its South-West interface 
 - router ``R3`` uses address ``2001:db8:1341:3::3`` on its East interface, address ``2001:db8:1341:23::3`` on its North-East interface and address ``2001:db8:1341:13::3`` on its North interface

The forwarding tables of these three routers, ignoring the routes to the local interfaces, are shown in the figure below.

    .. tikz::
       :libs: positioning, matrix, arrows 

       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \node[host] (A) {A};
       \node[router, right=of A] (R1) { R1 };
       \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
       Dest. & Nexthop \\
       \hline
       2001:db8:1341:3/64 & 2001:db8:1341:12::2 \\
       2001:db8:1341:23/64 & 2001:db8:1341:13::3 \\
       \end{tabular}};
       \node[router,right=of R1] (R2) {R2};
       \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l} 
       Dest. & Nexthop \\
       \hline 
       2001:db8:1341:3/64 & 2001:db8:1341:23::3 \\
       2001:db8:1341:1/64 & 2001:db8:1341:12::1 \\
       2001:db8:1341:13/64 & 2001:db8:1341:23::3 \\
       \end{tabular}\\};
       \node[router,below=of R1] (R3) {R3};
       \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l} 
       Dest. & Nexthop \\
       \hline
       2001:db8:1341:1/64 & 2001:db8:1341:13::1 \\
       2001:db8:1341:12/64 & 2001:db8:1341:23::2 \\
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
 

.. question:: ip6path1
   :nb_prop: 3
   :nb_pos: 2

   In the list below, select all the graphs below that represent the correct path followed by packets from ``A`` to ``B`` or from ``B`` to ``A``. 

   .. positive::

      .. tikz::
         :libs: positioning, matrix, arrows 

         \tikzstyle{arrow} = [thick,->,>=stealth]
         \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
         \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
         \tikzset{ftable/.style={rectangle, dashed, draw} }
         \node[host] (A) {A};
         \node[router, right=of A] (R1) { R1 };
         \node[router,right=of R1] (R2) {R2};
         \node[router,below=of R1] (R3) {R3};
         \node[host, right=of R3] (B) {B};

         \draw[arrow, color=red] (A) -- (R1); 
         \draw[arrow, color=red] (R1) -- (R2); 
         \draw[arrow, color=red] (R2) -- (R3);
         \draw[arrow, color=red] (R3) -- (B);


   .. negative::

      .. tikz::
         :libs: positioning, matrix, arrows 

         \tikzstyle{arrow} = [thick,->,>=stealth]
         \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
         \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
         \tikzset{ftable/.style={rectangle, dashed, draw} }
         \node[host] (A) {A};
         \node[router, right=of A] (R1) { R1 };
         \node[router,right=of R1] (R2) {R2};
         \node[router,below=of R1] (R3) {R3};
         \node[host, right=of R3] (B) {B};

         \draw[arrow, color=red] (B) -- (R3); 
         \draw[arrow, color=red] (R3) -- (R2); 
         \draw[arrow, color=red] (R2) -- (R1);
         \draw[arrow, color=red] (R1) -- (A);

      .. comment:: Check the nethop for the route towards ``2001:db8:1341:1/64`` on router ``R3``

   .. negative::

      .. tikz::
         :libs: positioning, matrix, arrows 

         \tikzstyle{arrow} = [thick,->,>=stealth]
         \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
         \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
         \tikzset{ftable/.style={rectangle, dashed, draw} }
         \node[host] (A) {A};
         \node[router, right=of A] (R1) { R1 };
         \node[router,right=of R1] (R2) {R2};
         \node[router,below=of R1] (R3) {R3};
         \node[host, right=of R3] (B) {B};

         \draw[arrow, color=red] (A) -- (R1); 
         \draw[arrow, color=red] (R1) -- (R3); 
         \draw[arrow, color=red] (R3) -- (B);


      .. comment:: Check the nethop for the route towards ``2001:db8:1341:3/64`` on router ``R1``

   .. positive::

      .. tikz::
         :libs: positioning, matrix, arrows 

         \tikzstyle{arrow} = [thick,->,>=stealth]
         \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
         \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
         \tikzset{ftable/.style={rectangle, dashed, draw} }
         \node[host] (A) {A};
         \node[router, right=of A] (R1) { R1 };
         \node[router,right=of R1] (R2) {R2};
         \node[router,below=of R1] (R3) {R3};
         \node[host, right=of R3] (B) {B};

         \draw[arrow, color=red] (B) -- (R3); 
         \draw[arrow, color=red] (R3) -- (R1); 
         \draw[arrow, color=red] (R1) -- (A);

5. Consider the network shown in the figure below. In this network, the following addresses are used.

  - host ``A`` : ``2001:db8:1341:1::A`` and its default route points to ``2001:db8:1341:1::1``
  - host ``B`` : ``2001:db8:1341:4::B`` and its default route points to ``2001:db8:1341:4::4``

The routers have one address inside each network :

 - router ``R1`` uses address ``2001:db8:1341:1::1`` on its West interface, address ``2001:db8:1341:12::1`` on its East interface and address ``2001:db8:1341:13::1`` on its South interface
 - router ``R2`` uses address ``2001:db8:1341:12::2`` on its West interface, address ``2001:db8:1341:23::2`` on its South-West interface and address ``2001:db8:1341:24::2`` on its South interface.
 - router ``R3`` uses address ``2001:db8:1341:34::3`` on its East interface, address ``2001:db8:1341:23::3`` on its North-East interface and address ``2001:db8:1341:13::3`` on its North interface
 - router ``R4`` uses address ``2001:db8:1341:34::4`` on its West interface, address ``2001:db8:1341:24::4`` on its North interface and address ``2001:db8:1341:4::4`` on its East interface

The forwarding paths used in a network depend on the forwarding tables installed in the network nodes. Sometimes, these forwarding tables must be configured manually. 

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
        Dest. & Nexthop \\
        \hline 
        2001:db8:1341:4/64  & 2001:db8:1341:12::2 \\
        2001:db8:1341:23/64 & 2001:db8:1341:13::3 \\        
        2001:db8:1341:34/64 & 2001:db8:1341:13::3 \\        
        2001:db8:1341:24/64 & 2001:db8:1341:12::2 \\        
        \end{tabular}};
        \node[router,right=of R1] (R2) {R2};

        \node[router,below=of R1] (R3) {R3};

        \node[router,below=of R2] (R4) {R4};
        \node[ftable,below=of R4] (FR4) { \begin{tabular}{l|l} 
        Dest. & Nexthop \\
        \hline 
        2001:db8:1341:1/64  & 2001:db8:1341:34::3 \\
        2001:db8:1341:23/64 & 2001:db8:1341:24::2 \\        
        2001:db8:1341:13/64 & 2001:db8:1341:34::3 \\        
        2001:db8:1341:12/64 & 2001:db8:1341:24::2 \\        
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

.. question:: 4routers
   :nb_prop: 4 
   :nb_pos: 2 

   In this network, select `all` the forwarding tables below that ensure that hosts ``A`` and ``B`` can exchange packets in both directions.


   .. positive:: New forwarding table for ``R3``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:23::2 
       2001:db8:1341:4/64    2001:db8:1341:34::4 
       2001:db8:1341:12/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:23::2         
       ====================  ===================      
 

      New forwarding table for ``R2``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:12::1 
       2001:db8:1341:4/64    2001:db8:1341:24::4 
       2001:db8:1341:13/64   2001:db8:1341:12::1         
       2001:db8:1341:34/64   2001:db8:1341:23::3         
       ====================  ===================      


   .. positive:: New forwarding table for ``R3``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:13::1 
       2001:db8:1341:4/64    2001:db8:1341:34::4 
       2001:db8:1341:12/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:23::2         
       ====================  ===================      
 

      New forwarding table for ``R2``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:12::1 
       2001:db8:1341:4/64    2001:db8:1341:24::4 
       2001:db8:1341:13/64   2001:db8:1341:12::1         
       2001:db8:1341:34/64   2001:db8:1341:23::3         
       ====================  ===================      

   .. positive:: New forwarding table for ``R3``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:13::1 
       2001:db8:1341:4/64    2001:db8:1341:34::4 
       2001:db8:1341:12/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:23::2         
       ====================  ===================      
 

      New forwarding table for ``R2``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:12::1 
       2001:db8:1341:4/64    2001:db8:1341:23::3 
       2001:db8:1341:13/64   2001:db8:1341:12::1         
       2001:db8:1341:34/64   2001:db8:1341:23::3         
       ====================  ===================      


   .. negative:: New forwarding table for ``R3``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:34::4 
       2001:db8:1341:4/64    2001:db8:1341:34::4 
       2001:db8:1341:12/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:23::2         
       ====================  ===================      
 

      New forwarding table for ``R2``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:12::1 
       2001:db8:1341:4/64    2001:db8:1341:24::4 
       2001:db8:1341:13/64   2001:db8:1341:12::1         
       2001:db8:1341:34/64   2001:db8:1341:23::3         
       ====================  ===================      

      .. comment:: The forwarding table of ``R3`` is incorrect, check the nexthop to reach ``2001:db8:1341:4/64``.

   .. negative:: New forwarding table for ``R3``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:23::2 
       2001:db8:1341:4/64    2001:db8:1341:34::4 
       2001:db8:1341:12/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:23::2         
       ====================  ===================      
 

      New forwarding table for ``R2``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:23::3 
       2001:db8:1341:4/64    2001:db8:1341:24::4 
       2001:db8:1341:13/64   2001:db8:1341:12::1         
       2001:db8:1341:34/64   2001:db8:1341:23::3         
       ====================  =================== 

      .. comment:: These forwarding tables are incorrect. Check what happens when ``R2`` receives a packet towards ``2001:db8:1341::1/64``     

   .. negative:: New forwarding table for ``R3``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:13::1 
       2001:db8:1341:4/64    2001:db8:1341:23::2 
       2001:db8:1341:12/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:23::2         
       ====================  ===================      
 

      New forwarding table for ``R2``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:12::1 
       2001:db8:1341:4/64    2001:db8:1341:23::3 
       2001:db8:1341:13/64   2001:db8:1341:12::1         
       2001:db8:1341:34/64   2001:db8:1341:23::3         
       ====================  ===================      

      .. comment:: These forwarding tables are incorrect. Check what happens when ``R2`` receives a packet towards ``2001:db8:1341::4/64``


6. Consider the same network as in the previous question, but now the forwarding tables of ``R2`` and ``R3`` are configured as shown below :

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[router,right=of R1] (R2) {R2};
        \node[ftable, above=of R2] (FR2) { \begin{tabular}{l|l} 
        Dest. & Nexthop \\
        \hline 
        2001:db8:1341:1/64  & 2001:db8:1341:12::1 \\
        2001:db8:1341:4/64  & 2001:db8:1341:23::3 \\
        2001:db8:1341:13/64 & 2001:db8:1341:23::3 \\        
        2001:db8:1341:34/64 & 2001:db8:1341:23::3 \\        
        \end{tabular}};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[ftable,below=of R3] (FR3) { \begin{tabular}{l|l} 
        Dest. & Nexthop \\
        \hline 
        2001:db8:1341:1/64  & 2001:db8:1341:23::2 \\
        2001:db8:1341:4/64  & 2001:db8:1341:34::4 \\
        2001:db8:1341:12/64 & 2001:db8:1341:23::2 \\        
        2001:db8:1341:24/64 & 2001:db8:1341:23::2 \\          
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

        \draw[arrow, dashed] (FR2) -- (R2); 
        \draw[arrow, dashed] (FR3) -- (R3); 


.. question:: 4routersb
   :nb_prop: 3 
   :nb_pos: 1 

   In this network, select `all` the forwarding tables below that ensure that the packets sent from ``A`` to ``B`` follow the reverse path of the packets sent by ``B`` to ``A``.


   .. positive:: New forwarding table for ``R1``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:4/64    2001:db8:1341:12::2 
       2001:db8:1341:23/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:12::2   
       2001:db8:1341:34/64   2001:db8:1341:13::3   
       ====================  ===================      

      New forwarding table for ``R4``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:34::3 
       2001:db8:1341:13/64   2001:db8:1341:34::3         
       2001:db8:1341:12/64   2001:db8:1341:24::2    
       2001:db8:1341:23/64   2001:db8:1341:24::2    
       ====================  ===================      


   .. negative:: New forwarding table for ``R1``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:4/64    2001:db8:1341:13::3 
       2001:db8:1341:23/64   2001:db8:1341:12::2         
       2001:db8:1341:24/64   2001:db8:1341:12::2   
       2001:db8:1341:34/64   2001:db8:1341:13::3   
       ====================  ===================      

      New forwarding table for ``R4``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:24::2 
       2001:db8:1341:13/64   2001:db8:1341:34::3         
       2001:db8:1341:12/64   2001:db8:1341:24::2    
       2001:db8:1341:23/64   2001:db8:1341:24::2    
       ====================  ===================      

      .. comment:: The two paths ``A->B`` and ``B->A`` do not pass through the same routers.

   .. negative:: New forwarding table for ``R1``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:4/64    2001:db8:1341:12::2 
       2001:db8:1341:23/64   2001:db8:1341:13::3         
       2001:db8:1341:24/64   2001:db8:1341:12::2   
       2001:db8:1341:34/64   2001:db8:1341:13::3   
       ====================  ===================      

      New forwarding table for ``R4``:

       ====================  ===================
       Dest.                 Nexthop 
       ====================  ===================
       2001:db8:1341:1/64    2001:db8:1341:24::2 
       2001:db8:1341:13/64   2001:db8:1341:34::3         
       2001:db8:1341:12/64   2001:db8:1341:24::2    
       2001:db8:1341:23/64   2001:db8:1341:24::2    
       ====================  ===================      

      .. comment:: The two paths ``A->B`` and ``B->A`` do not pass through the same routers.


7. Consider again the same network with three routers as discussed earlier. Let us know explore how :manpage:`traceroute6(8)` operates in such a network. A key point to remember about :manpage:`traceroute6(8)` is that when it returns an ICMP message, this message is sent inside a packet whose source is one of the addresses of the router and whose destination is the source address of the packet that triggered the generation of this ICMP message. In this network, the hosts have the following addresses :

 - host ``A`` : ``2001:db8:1341:1::A`` and its default route points to ``2001:db8:1341:1::1``
 - host ``B`` : ``2001:db8:1341:3::B`` and its default route points to ``2001:db8:1341:3::3``

The routers have one address inside each network :

 - router ``R1`` uses address ``2001:db8:1341:1::1`` on its West interface, address ``2001:db8:1341:12::1`` on its East interface and address ``2001:db8:1341:13::1`` on its South interface
 - router ``R2`` uses address ``2001:db8:1341:12::2`` on its West interface and address ``2001:db8:1341:23::2`` on its South-West interface 
 - router ``R3`` uses address ``2001:db8:1341:3::3`` on its East interface, address ``2001:db8:1341:23::3`` on its North-East interface and address ``2001:db8:1341:13::3`` on its North interface

The forwarding tables of these three routers, ignoring the routes to the local interfaces, are shown in the figure below.

    .. tikz::
       :libs: positioning, matrix, arrows 

       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \node[host] (A) {A};
       \node[router, right=of A] (R1) { R1 };
       \node[ftable, above=of R1] (FR1) { \begin{tabular}{l|l} 
       Dest. & Nexthop \\
       \hline
       2001:db8:1341:3/64 & 2001:db8:1341:12::2 \\
       2001:db8:1341:23/64 & 2001:db8:1341:13::3 \\
       \end{tabular}};
       \node[router,right=of R1] (R2) {R2};
       \node[ftable, right=of R2] (FR2) { \begin{tabular}{l|l} 
       Dest. & Nexthop \\
       \hline 
       2001:db8:1341:3/64 & 2001:db8:1341:23::3 \\
       2001:db8:1341:1/64 & 2001:db8:1341:12::1 \\
       2001:db8:1341:13/64 & 2001:db8:1341:23::3 \\
       \end{tabular}\\};
       \node[router,below=of R1] (R3) {R3};
       \node[ftable, below=of R3] (FR3) { \begin{tabular}{l|l} 
       Dest. & Nexthop \\
       \hline
       2001:db8:1341:1/64 & 2001:db8:1341:13::1 \\
       2001:db8:1341:12/64 & 2001:db8:1341:23::2 \\
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
 

.. question:: traceroute6 
   :nb_prop: 3 
   :nb_pos: 2          

   In this network, select the all traceroute outputs that are correct according to the forwarding tables shown above.

   .. positive::

      .. code-block:: console 

         traceroute6 to 2001:db8:1341:1::A from 2001:db8:1341:3::B 
         1  2001:db8:1341:3::3 
         2  2001:db8:1341:13::1 
         3  2001:db8:1341:1::A 

      .. comment:: This traceroute is correct but note that it's likely possible that the penultimate address will be an other IPv6 address of `R1`: ``2001:db8:1341:12::1`` instead of ``2001:db8:1341:13::1``, it depends if the ICMP package takes the path to the previous router or to the source (the reversed path is different according to the forwarding tables).

   .. negative::

      .. code-block:: console 

         traceroute6 to 2001:db8:1341:1::A from 2001:db8:1341:3::B 
         1  2001:db8:1341:3::3 
         2  2001:db8:1341:23::2
         3  2001:db8:1341:12::1
         4  2001:db8:1341:1::A 

      .. comment:: This traceroute is incorrect. Check the forwarding table of ``R3`` towards ``2001:db8:1341:1/64``

   .. negative::

      .. code-block:: console 

         traceroute6 to 2001:db8:1341:3::B from 2001:db8:1341:1::A 
         1  2001:db8:1341:1::1 
         2  2001:db8:1341:13::3 
         3  2001:db8:1341:3::B 

      .. comment:: This traceroute is incorrect. Check the forwarding table of ``R1`` towards ``2001:db8:1341:3/64``

   .. positive::

      .. code-block:: console 

         traceroute6 to 2001:db8:1341:3::B from 2001:db8:1341:1::A 
         1  2001:db8:1341:1::1 
         2  2001:db8:1341:12::2 
         3  2001:db8:1341:23::3
         4  2001:db8:1341:3::B 

      .. comment:: This traceroute is correct but note that it's likely possible that the penultimate address will be an other IPv6 address of `R3`: ``2001:db8:1341:13::3`` instead of ``2001:db8:1341:23::3``, it depends if the ICMP package takes the path to the previous router or to the source (the reversed path is different according to the forwarding tables).



8. When manipulating IPv6 address, it is sometimes necessary to convert an IPv6 address in its binary representation. 

.. question:: ipv6addr 
   :nb_prop: 3 
   :nb_pos: 1

   Among the following binary representations, which is the one that corresponds to address ``2001:DB8:1341:FC81::1``  (the first line shows the higher order 64 bits starting from the highest order bits, the second the low order 64 bits) ?


   .. positive::

      .. code-block:: console 

         00100000 00000001 00001101 10111000 00010011 01000001 11111100 10000001 
         00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000001 


   .. negative::
   
      .. code-block:: console 

         00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000001 
         00100000 00000001 00001101 10111000 00010011 01000001 11111100 10000001 

      .. comment:: This is the binary representation for IPv6 address ``0000:0000:0000:0001:2001:DB8:1341:FC81`` 

   .. negative::

      .. code-block:: console 

         00000001 00100000 10111000 00001101 010000000010011 1 10000001 11111100 
         00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000001

      .. comment:: This is the binary representation for IPv6 address ``0120:80DB:4113:81FC::1``

   .. negative::

      .. code-block:: console 

         00100000 00000001 11011011 10000000 00010011 01000001 11111100 10000001 
         00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000001 

      .. comment:: This is the binary representation for IPv6 address ``2001:DB80:1341:FC81::1``



9. When an IPv6 router receives a packet to be forwarded, it finds the most specific match for the destination address of this packet in its forwarding table. Consider the following forwarding table from an hypothetical IPv6 router.

 .. code-block:: console

     2001:DB8:1341::/48, via nexthop1
     2001:DB8:1341:2000/51, via nexthop5
     2001:DB8:1341:2000/64, interface1
     2001:DB8:1341:4000/50, via nexthop2
     2001:DB8:1341:5000/52, nexthop3
     2001:DB8:1341:7000/64, interface2
     2001:DB8:1341:5555/64, interface3
     2001:DB8::/16 via nexthop4
     ::/0 via nexthop0

.. question:: ipv6morespecific
   :nb_prop: 5
   :nb_pos: 3

   Among the following affirmations about the matching of destination addresses in the forwarding tables, select all the *correct* ones.

   .. positive:: A packet whose destination address is ``2001:DB8:1342:5555::1`` will be forwarded via ``nexthop4``

      .. comment:: This destination address matches ``2001:DB8::/16``


   .. negative:: A packet whose destination address is ``2001:DB8:1342:5555::1`` will be forwarded via ``interface3``

       .. comment:: No, this destination address matches route ``2001:DB8::/16``


   .. positive:: A packet whose destination address is ``2001:DB8:1341:3000::1`` will be forwarded via ``nexthop5``

       .. comment:: This destination address matches ``2001:DB8:1341:2000/51``


   .. negative:: A packet whose destination address is ``2001:DB8:1341:3000::1`` will be forwarded via ``nexthop0``

       .. comment:: No, this destination address matches route ``2001:DB8:1341:2000/51``

   .. negative:: A packet whose destination address is ``2001:DB8:1341:3000::1`` will be forwarded via ``nexthop1``

       .. comment:: No, this destination address matches route ``2001:DB8:1341:2000/51``


   .. positive:: A packet whose destination address is ``2001:DB8:1341:6000::1`` will be forwarded via ``nexthop2``

       .. comment:: This destination address matches ``2001:DB8:1341:4000/50``


   .. negative:: A packet whose destination address is ``2001:DB8:1341:6000::1`` will be forwarded via ``nexthop0``

       .. comment:: No, this destination address matches route ``2001:DB8:1341:4000/50``

   .. negative:: A packet whose destination address is ``2001:DB8:1341:6000::1`` will be forwarded via ``nexthop1``

       .. comment:: No, this destination address matches route ``2001:DB8:1341:4000/50``


   .. positive:: A packet whose destination address is ``2001:DB8:1341:5000::1`` will be forwarded via ``nexthop3``

       .. comment:: This destination address matches ``2001:DB8:1341:5000/52``


   .. negative:: A packet whose destination address is ``2001:DB8:1341:5000::1`` will be forwarded via ``nexthop2``

       .. comment:: No, this destination address matches route ``2001:DB8:1341:5000/52``

   .. negative:: A packet whose destination address is ``2001:DB8:1341:5000::1`` will be forwarded via ``nexthop1``

       .. comment:: No, this destination address matches route ``2001:DB8:1341:5000/52``


Design questions
----------------


1. Consider the network shown in the figure below. In this network, the following addresses are used.

  - host ``A`` : ``2001:db8:1341:1::A`` and its default route points to ``2001:db8:1341:1::1``
  - host ``B`` : ``2001:db8:1341:4::B`` and its default route points to ``2001:db8:1341:4::4``

The routers have one address inside each network :

 - router ``R1`` uses address ``2001:db8:1341:1::1`` on its West interface, address ``2001:db8:1341:12::1`` on its East interface and address ``2001:db8:1341:13::1`` on its South interface
 - router ``R2`` uses address ``2001:db8:1341:12::2`` on its West interface, and address ``2001:db8:1341:24::2`` on its South interface
 - router ``R3`` uses address ``2001:db8:1341:34::3`` on its East interface and address ``2001:db8:1341:13::3`` on its North interface
 - router ``R4`` uses address ``2001:db8:1341:34::4`` on its West interface, address ``2001:db8:1341:24::4`` on its North interface and address ``2001:db8:1341:4::4`` on its East interface

Routers ``R2`` and ``R3`` are buggy in this network. Besides the routes for their local interfaces (not shown in the figure), they only have a default route which is shown in the figure below.

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[ftable, above=of R1] (FR2) { \begin{tabular}{l|l} 
        Dest. & Nexthop \\
        \hline 
        ::/0  & 2001:db8:1341:12::1 \\
        \end{tabular}};
        \node[router,right=of R1] (R2) {R2};

        \node[router,below=of R1] (R3) {R3};

        \node[router,below=of R2] (R4) {R4};
        \node[ftable,below=of R4] (FR3) { \begin{tabular}{l|l} 
        Dest. & Nexthop \\
        \hline 
        ::/0  & 2001:db8:1341:34::4 \\
        \end{tabular}\\};
        \node[host, right=of R4] (B) {B};

        \path[draw,thick]
        (A) edge (R1) 
        (R1) edge (R2) 
        (R1) edge (R3) 
        (R4) edge (R3) 
        (R2) edge (R4) 
        (R4) edge (B); 

        \draw[arrow, dashed] (FR2) -- (R2); 
        \draw[arrow, dashed] (FR3) -- (R3); 

How do you configure the forwarding tables on ``R1`` and ``R4`` so that ``A`` can reach ``B`` and the reverse ?

2. Consider a slightly different network than in the previous question. 

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[router,right=of R1] (R2) {R2};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[host, right=of R4] (B) {B};

        \path[draw,thick]
        (A) edge (R1)
        (R1) edge (R2)
        (R1) edge (R3)
        (R1) edge (R4)
        (R4) edge (R3)
        (R2) edge (R4)
        (R4) edge (B);

 Assuming that the following IPv6 addresses are used :

  - host ``A`` : ``2001:db8:1341:1::A`` and its default route points to ``2001:db8:1341:1::1``
  - host ``B`` : ``2001:db8:1341:4::B`` and its default route points to ``2001:db8:1341:4::4``

The routers have one address inside each network :

 - router ``R1`` uses address ``2001:db8:1341:1::1`` on its West interface, address ``2001:db8:1341:12::1`` on its East interface, address ``2001:db8:1341:14::1`` on its South-East interface and address ``2001:db8:1341:13::1`` on its South interface
 - router ``R2`` uses address ``2001:db8:1341:12::2`` on its West interface, and address ``2001:db8:1341:24::2`` on its South interface
 - router ``R3`` uses address ``2001:db8:1341:34::3`` on its East interface and address ``2001:db8:1341:13::3`` on its North interface
 - router ``R4`` uses address ``2001:db8:1341:34::4`` on its West interface, address ``2001:db8:1341:24::4`` on its North interface, address ``2001:db8:1341:14::4`` on its North-West interface and address ``2001:db8:1341:4::4`` on its East interface

 Can you configure the forwarding tables so that the following paths are used by packets sent by host ``A`` to reach one of the four addresses of router ``R4``?

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[router,right=of R1] (R2) {R2};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[host, right=of R4] (B) {B};

        \path[draw,arrow, color=red, thick]
        (A) edge (R1) 
        (R1) edge (R2) 
        (R2) edge (R4);

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[router,right=of R1] (R2) {R2};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[host, right=of R4] (B) {B};

        \path[draw,arrow, color=blue, thick]
        (A) edge (R1) 
        (R1) edge (R4);

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A) {A};
        \node[router, right=of A] (R1) { R1 };
        \node[router,right=of R1] (R2) {R2};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[host, right=of R4] (B) {B};

        \path[draw,arrow, color=green, thick]
        (A) edge (R1) 
        (R1) edge (R3)
        (R3) edge (R4);

 Do your forwarding tables impose the path used to reach host ``B`` which is attached to router ``R4`` or do you need to configure an additional entry in these tables ?

3. Consider the network below that contains only routers. This network has been configured by a group of students and you must verify whether the configuration is correct. All the IPv6 addresses are part of the same ``/48`` prefix that we name ``p``. The following subnets are defined in this ``/48`` prefix.

 - ``p:12/64`` for the link between ``R1`` and ``R2``. On this subnet, ``R1`` uses address ``p:12::1`` while router ``R2`` uses address ``p:12::2``
 - ``p:13/64`` for the link between ``R1`` and ``R3``. On this subnet, ``R1`` uses address ``p:13::1`` while router ``R3`` uses address ``p:13::3``
 - ``p:24/64`` for the link between ``R2`` and ``R4``. On this subnet, ``R2`` uses address ``p:24::2`` while router ``R4`` uses address ``p:24::4``
 - ...

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[router] (R1) {R1};
        \node[router,right=of R1] (R2) {R2};
        \node[router,right=of R2] (R5) {R5};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[router,below=of R5] (R6) {R6};

        \path[draw,thick]
        (R1) edge (R2)
        (R1) edge (R3)
        (R4) edge (R3)
        (R2) edge (R4)
        (R2) edge (R5)
        (R4) edge (R6)
        (R5) edge (R6);

.. note 12 via R2 
.. note 13 via R3 mais boucle R2 R4 R5 R6 
.. note 34 via R4 mais blackhole en R2 et R5 pas de route
.. note 24 via R2 ou R4 pas de probleme
.. note 25 via le plus proche sauf boucle R4-R6
.. note 46 pas de route sauf defaut
.. note 56 tout vers R4 mais pas de route en R4

The students have configured the following forwarding tables on these six routers.

 - on router ``R1``

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[ftable] (FR1) { \begin{tabular}{l|l} 
        Dest. & Nexthop/Interface \\
        \hline 
        ::/0  & p:12::2 \\
        p:12::/64  & East \\
        p:13::/64  & South\\
        p:25::/64  & p:12::2\\
        p:34::/64 & p:12::2\\
        \end{tabular}};



 - on router ``R2``

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[ftable] (FR2) { \begin{tabular}{l|l} 
        Dest. & Nexthop/Interface \\
        \hline 
        ::/0  & p:12::1 \\
        p:12::/64  & West \\
        p:13::/64 & p:24::4\\
        p:24::/64  & South\\
        p:25::/64  & East\\
        p:56::/64 & p:24::4\\
        \end{tabular}};


 - on router ``R3``

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[ftable] (FR3) { \begin{tabular}{l|l} 
        Dest. & Nexthop/Interface \\
        \hline 
        ::/0 & p:13::1\\
        p:13::/64  & North \\
        p:34::/64  & East\\
        p:56::/64 & p:34::4\\
        \end{tabular}};


 - on router ``R5``

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[ftable] (FR5) { \begin{tabular}{l|l} 
        Dest. & Nexthop/Interface \\
        \hline 
        ::/0 & p:56::6 \\
        p:12::/64 & p:25::2\\
        p:25::/64  & West \\
        p:56::/64  & South\\
        \end{tabular}};

 - on router ``R4``

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzset{ftable/.style={rectangle, dashed, draw} }

        \node[ftable] (FR4) { \begin{tabular}{l|l} 
        Dest. & Nexthop/Interface \\
        \hline 
        p:12::/63 & p:24::2\\
        p:24::/64  & North\\
        p:25::/64  & p:46::6\\
        p:34::/64  & West\\
        p:46::/64  & East\\
        \end{tabular}};

 - on router ``R6``

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[ftable] (FR6) { \begin{tabular}{l|l} 
        Dest. & Nexthop/Interface \\
        \hline 
        ::/0 & p:56::5 \\
        p:13::/64 & p:46::4\\
        p:24::/63 & p:46::4\\
        p:34::/64 & p:46::4\\
        p:46::/64  & West\\
        p:56::/64  & North\\
        \end{tabular}};



4. Sometimes, static routes must be configured on networks to enforce certain paths. Consider the six routers network shown in the figure below.

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A1) {A1};
        \node[router, right=of A1] (R1) {R1};
        \node[host, below=of A1] (A2) {A2};
        \node[router,right=of R1] (R2) {R2};
        \node[router,right=of R2] (R5) {R5};
        \node[router,below=of R1] (R3) {R3};
        \node[router,below=of R2] (R4) {R4};
        \node[router,below=of R5] (R6) {R6};
        \node[host, right=of R5] (B1) {B1};
        \node[host, right=of R6] (B2) {B2};


        \path[draw,thick]
        (A1) edge (R1)
        (A2) edge (R3)
        (R1) edge (R2)
        (R1) edge (R3)
        (R4) edge (R3)
        (R2) edge (R4)
        (R2) edge (R5)
        (R4) edge (R6)
        (R5) edge (R6)
        (R5) edge (B1)
        (R6) edge (B2);


   In this network, we will focus on four IPv6 prefixes :

     - ``p:0000::/64`` used on the link ``A1-R1``. ``A1`` uses address ``p:0000::A1/64``
     - ``p:0001::/64`` used on the link ``A2-R3``. ``A2`` uses address ``p:0001::A2/64``
     - ``p:0002::/64`` used on the link ``B1-R5``. ``B1`` uses address ``p:0002::B1/64``
     - ``p:0003::/64`` used on the link ``B2-R6``. ``B2`` uses address ``p:0003::B2/64``

   Can you configure the forwarding tables of the six routers to achieve the following network objectives :

    a. All packets sent by ``B1`` and ``B2`` to ``A1`` and ``A2`` are always forwarded via ``R2`` while all packets from ``A1`` and ``A2`` are always forwarded via ``R4``
    b. The packets whose destinations are ``A1``,  ``A2``, ``B1`` or ``B2`` are never forwarded via router ``R4``
    c. The packets sent by ``A1`` or ``A2`` towards ``B1`` are always forwarded via ``R2`` while the packets towards ``B2`` are always forwarded via ``R4``.
 
   When creating these forwarding tables, try to minimise the number of entries that you install on each router.

5. When a network is designed, an important element of the design is the IP address allocation plan. A good allocation plan can provide flexibility and help to reduce the size of the forwarding tables. 

     .. tikz::
        :libs: positioning, matrix, arrows 

        \tikzstyle{arrow} = [thick,->,>=stealth]
        \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
        \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
        \tikzset{ftable/.style={rectangle, dashed, draw} }
        \node[host] (A1) {A1};
        \node[router, right=of A1] (R1) {R1};
        \node[host, below=of A1] (A2) {A2};
        \node[router,right=of R1] (R2) {R2};
        \node[router,right=of R2] (R5) {R5};
        \node[router,below=of R1] (R3) {R3};
         \node[router,below=of R5] (R6) {R6};
        \node[host, right=of R5] (B1) {B1};
        \node[host, right=of R6] (B2) {B2};


        \path[draw,thick]
        (A1) edge (R1)
        (A2) edge (R3)
        (R1) edge (R3)
        (R2) edge (R3)
        (R2) edge (R5)
        (R2) edge (R6)
        (R5) edge (R6)
        (R5) edge (B1)
        (R6) edge (B2);

  Assign IP subnets to all links in this network so that you can reduce the number of entries in the forwarding tables of all routers. Assume that you have received a ``/56`` prefix that you can use as you want. Each subnet containing a host must be allocated a ``/64`` subnet. 

