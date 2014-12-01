.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



The Border Gateway Protocol
===========================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 

.. _mcq-bgp:


Multiple choice questions
-------------------------

:task_id: mcqbgp


1. The BGP decision process is the process that is used by a BGP router to select the best path among all the paths learned towards a given destination prefix. The table below represents all the BGP routes learned by a BGP router and their corresponding attributes. For simplicity, the nexthops are indicated as router names instead of IP addresses.

   ================  ===========    ==========    =======
   prefix            AS Path        local-pref    nexthop
   ----------------  -----------    ----------    -------
   2001:db8:1/48     AS1:AS4        100           R1 
   2001:db8:1/48     AS1:AS3:AS4    200           R2 
   2001:db8:1/48     AS1:AS4        100           R3 
   2001:db8:1/48     AS4            150           R4
   2001:db8:2/48     AS1:AS4        100           R1 
   2001:db8:2/48     AS1:AS3:AS4    100           R2 
   2001:db8:2/48     AS1:AS4        100           R3 
   2001:db8:2/48     AS4            150           R4
   2001:db8:0/47     AS1:AS4        200           R1 
   2001:db8:0/47     AS1:AS3:AS4    200           R2 
   2001:db8:0/47     AS1:AS4        100           R3 
   2001:db8:0/47     AS4            150           R4
   2001:db8:0/48     AS1:AS4        100           R1 
   2001:db8:0/48     AS1:AS3:AS4    100           R2 
   2001:db8:0/48     AS1:AS4        150           R3 
   2001:db8:0/48     AS4            150           R4
   ================  ===========    ==========    =======

.. question:: bgpdc 
   :nb_prop: 4 
   :nb_pos: 3  

   Assuming that the router above belongs to ``AS5``, select all the routes that it will advertise to an hypothetical router that belongs to ``AS9``.

   .. positive:: The router will advertise a route towards ``2001:db8:1/48`` with the ``AS5:AS1:AS3:AS4`` AS Path.

   .. positive:: The router will advertise a route towards ``2001:db8:2/48`` with the ``AS5:AS4`` AS Path.

   .. positive:: The router will advertise a route towards ``2001:db8:0/47`` with the ``AS5:AS1:AS4`` AS Path.

   .. positive:: The router will advertise a route towards ``2001:db8:0/48`` with the ``AS5:AS4`` AS Path.


   .. negative:: The router will advertise a route towards ``2001:db8:1/48`` with the ``AS5:AS4`` AS Path.

      .. comment:: In the BGP Decision process, a route with a higher local preference is always preferred over a route with a lower preference.

   .. negative:: The router will advertise a route towards ``2001:db8:0/47`` with the ``AS5:AS4`` AS Path.

      .. comment:: In the BGP Decision process, a route with a higher local preference is always preferred over a route with a lower preference.

   .. negative:: The router will advertise a route towards ``2001:db8:0/48`` with the ``AS5:AS1:AS4`` AS Path.
      .. comment:: In the BGP Decision process, a route with a shorter AS Path is always preferred over a route with a longer AS Path.



2. Consider the BGP routing table shown in the previous question and consider the forwarding of IP packets.

.. question:: bgpdc2
   :nb_prop: 5 
   :nb_pos: 2  

    Among all the affirmations below, select all the correct ones.

   .. positive:: The router will forward a packet whose destination is ``2001:db8:1::1`` via ``R2``

   .. positive:: The router will forward a packet whose destination is ``2001:db8:0::1`` via ``R4``

   .. positive:: The router will forward a packet whose destination is ``2001:db8:2::1`` via ``R4``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:1::1`` via ``R1``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:0::1`` via ``R1``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:2::1`` via ``R1``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:1::1`` via ``R3``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:0::1`` via ``R3``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:2::1`` via ``R3``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:1::1`` via ``R4``

   .. negative:: The router will forward a packet whose destination is ``2001:db8:0::1`` via ``R2``

3. Consider a router that belongs to ``AS8`` and is connected to ``AS9``. The BGP routes that it has received are the following ones. This router is connected to four different ASes : ``AS1`` (on router ``R1``), ``AS5`` (on router ``R2``), ``AS6`` (on router ``R3``)  and ``AS4`` (on router ``R4``). We assume that the same local-pref is used for all routes received from a given peer.

   ================  ===========    ==========    ========
   prefix            AS Path        local-pref    nexthop
   ----------------  -----------    ----------    --------
   2001:db8:2/48     AS1:AS4        50            R1 (AS1)
   2001:db8:2/48     AS5:AS3:AS4    100           R2 (AS5)
   2001:db8:2/48     AS6:AS4        100           R3 (AS6)
   2001:db8:2/48     AS4            100           R4 (AS4)
   ================  ===========    ==========    ========

.. question:: bgpdc4 
   :nb_prop: 3
   :nb_pos: 2 

   Select in the list below all the correct affirmations about the reaction of this router to the reception of a BGP message from one of its peers. We assume that ``AS9`` is a client of ``AS8`` and thus it receives all the routes learned by ``AS9``.

   .. positive:: If a Withdraw message for prefix ``2001:db8:2/48`` is received from ``AS1``, then no message is sent to ``AS8``.

   .. positive:: If a Withdraw message for prefix ``2001:db8:2/48`` is received from ``AS5``, then no message is sent to ``AS8``.

   .. positive:: If a Withdraw message for prefix ``2001:db8:2/48`` is received from ``AS6``, then no message is sent to ``AS8``.

   .. negative:: If a Withdraw message for prefix ``2001:db8:2/48`` is received from ``AS1``, then a Withdraw message is sent for this prefix to ``AS8``.

      .. comment:: The best route towards ``2001:db8:2/48`` does not change upon reception of the Withdraw message for this prefix from ``AS1``. ``AS8`` still has a route towards ``2001:db8:2/48``.

   .. positive:: If a Withdraw message for prefix ``2001:db8:2/48`` is received from ``AS4``, then the router will send an Update message for prefix ``2001:db8:2/48`` with ``AS8:AS6:AS4`` as AS Path.


4. Consider now a router that belongs to ``AS8`` and is connected to ``AS9``. The BGP routes that it has received are the following ones. This router is connected to four different ASes : ``AS1`` (on router ``R1``), ``AS5`` (on router ``R2``), ``AS6`` (on router ``R3``)  and ``AS4`` (on router ``R4``). We assume that the same local-pref is used for all routes received from a given peer.

   ================  ===========    ==========    =======
   prefix            AS Path        local-pref    nexthop
   ----------------  -----------    ----------    -------
   2001:db8:1/48     AS1:AS1:AS4    100           R1 (AS1)
   2001:db8:1/48     AS5:AS3:AS4    200           R2 (AS5)
   2001:db8:1/48     AS6:AS4        100           R3 (AS6)
   2001:db8:1/48     AS4            150           R4 (AS4)
   ================  ===========    ==========    =======


.. question:: bgpdc3 
   :nb_prop: 4
   :nb_pos: 2

   Consider the routes that this router advertises to ``AS9``. Assuming that there are no routing policies (i.e. the router advertises all its best routes), select all the correct affirmations about the reaction of the router to the reception of BGP messages from one of its peers.

   .. positive:: If the router receives a Withdraw for prefix ``2001:db8:1/48`` from ``R1``, it does not send any BGP message to ``AS9``.

   .. positive:: If the router receives a Withdraw for prefix ``2001:db8:1/48`` from ``R3``, it does not send any BGP message to ``AS9``.

   .. positive:: If the router receives a Withdraw for prefix ``2001:db8:1/48`` from ``R4``, it does not send any BGP message to ``AS9``.

   .. positive:: If the router receives a Withdraw for prefix ``2001:db8:1/48`` from ``R2``, it sends an Update to ``AS9`` that advertises this prefix via the ``AS6:AS4`` path.

   .. positive:: If the router receives an Update for prefix ``2001:db8:1/48`` from ``R2`` with AS Path ``AS5:AS7:AS8:AS4``, it sends an Update for this prefix with AS Path ``AS8:AS5:AS7:AS8:AS4``.

   .. negative:: If the router receives an Update for prefix ``2001:db8:1/48`` from ``R2`` with AS Path ``AS5:AS7:AS8:AS4``, it sends a Withdraw for this prefix to ``AS9``.

      .. comment:: The best path towards prefix ``2001:db8:1/48`` on this router is the path learned from ``AS5`` since it has the highest local-pref. If this path changes, the updated path must be advertised to ``AS9``.

   .. negative:: If the router receives an Update for prefix ``2001:db8:1/48`` from ``R1`` with AS Path ``AS1:AS4``, it sends an Update for this prefix with AS Path ``AS5:AS1:AS4`` to ``AS9``.

      .. comment:: The best path towards prefix ``2001:db8:1/48`` on this router is the path learned from ``AS5`` since it has the highest local-pref. This best path does not change and thus the router does not send any message to ``AS9``.

   .. negative:: If the router receives an Update for prefix ``2001:db8:1/48`` from ``R3`` with AS Path ``AS6:AS4``, it sends an Update for this prefix with AS Path ``AS5:AS6:AS4`` to ``AS9``.

      .. comment:: The best path towards prefix ``2001:db8:1/48`` on this router is the path learned from ``AS5`` since it has the highest local-pref. This best path does not change and thus the router does not send any message to ``AS9``.



5. In the small Internet shown below, ``AS4`` announces one prefix : ``2001:db8:4/48``.

 .. tikz::
       :libs: positioning, matrix, arrows, shapes 

       [align=center,node distance=3cm] 
       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \tikzset{as/.style={cloud, draw,cloud puffs=10,cloud puff arc=120, aspect=2, minimum height=2em, minimum width=2em} }
       \node[as] (AS1) {AS1};
       \node[as, right of=AS1] (AS2) {AS2};
       \node[as, right of=AS2] (AS5) {AS5};
       \node[as, below of=AS1] (AS3) {AS3};
       \node[as, right of=AS3] (AS4) {AS4}; 
        \path[draw,thick]
        (AS1) edge (AS2) 
        (AS1) edge (AS3) 
        (AS3) edge (AS2) 
        (AS3) edge (AS4) 
        (AS2) edge (AS5);

 
.. question:: bgp1 
   :nb_prop: 4 
   :nb_pos: 2          

   Assuming that all the links are up and the network has converged, select all the correct affirmations about the state of the BGP routing tables. Assume that there are no routing policies in this Internet. 

   .. positive:: The BGP routing table of ``AS3`` contains only one path towards prefix ``2001:db8:4/48``. It's AS-Path is ``AS4``. 

   .. positive:: The BGP routing table of ``AS5`` contains only one path towards prefix ``2001:db8:4/48``. It's AS-Path is ``AS2:AS3:AS4``. 

   .. negative:: The BGP routing table of ``AS5`` contains only one path towards prefix ``2001:db8:4/48``. It's AS-Path is ``AS2:AS1:AS3:AS4``. 

      .. comment:: A BGP router always prefers the path with the shortest AS-Path. ``AS2`` has learned two paths for prefix ``2001:db8:4/48`` : ``AS3:AS4`` and ``AS1:AS3:AS4``. ``AS2`` will use the path ``AS3:AS4`` and advertise it to ``AS5``. 

   .. negative:: The BGP routing table of ``AS5`` contains two paths towards prefix ``2001:db8:4/48`` :  ``AS2:AS1:AS3:AS4`` and ``AS2:AS3:AS4``. ``AS5`` prefers and uses the path ``AS2:AS3:AS4``. 

      .. comment:: ``AS5`` only learns one path from ``AS2`` : ``AS2:AS3:AS4``. It never learns the path ``AS2:AS1:AS3:AS4``

   .. positive:: The BGP routing table of ``AS2`` contains two paths towards prefix ``2001:db8:4/48`` :  ``AS1:AS3:AS4`` and ``AS3:AS4``. ``AS2`` prefers and uses the path ``AS3:AS4``. 

   .. negative:: The BGP routing table of ``AS2`` contains only one path towards prefix ``2001:db8:4/48`` :  ``AS1:AS3:AS4``. 

      .. comment:: ``AS2`` learns two paths for this prefix, one from ``AS1`` and the other from ``AS3``. 

   .. negative:: The BGP routing table of ``AS2`` contains only one path towards prefix ``2001:db8:4/48`` :  ``AS3:AS4``. 

      .. comment:: ``AS2`` learns two paths for this prefix, one from ``AS1`` and the other from ``AS3``. 


6. Consider the same Internet as above, but now assume that ``AS2`` has configured its import filters to attach a higher local-preference to the routes received from ``AS1``. ``AS4`` announces one prefix : ``2001:db8:4/48``.

    .. tikz::
       :libs: positioning, matrix, arrows, shapes 

       [align=center,node distance=3cm] 
       \tikzstyle{arrow} = [thick,->,>=stealth]
       \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
       \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
       \tikzset{ftable/.style={rectangle, dashed, draw} }
       \tikzset{as/.style={cloud, draw,cloud puffs=10,cloud puff arc=120, aspect=2, minimum height=2em, minimum width=2em} }
       \node[as] (AS1) {AS1};
       \node[as, right of=AS1] (AS2) {AS2};
       \node[as, right of=AS2] (AS5) {AS5};
       \node[as, below of=AS1] (AS3) {AS3};
       \node[as, right of=AS3] (AS4) {AS4}; 
        \path[draw,thick]
        (AS1) edge (AS2) 
        (AS1) edge (AS3) 
        (AS3) edge (AS2) 
        (AS3) edge (AS4) 
        (AS2) edge (AS5);

 
.. question:: bgp2 
   :nb_prop: 4 
   :nb_pos: 2          

   Assuming that all the links are up and the network has converged, select all the correct affirmations about the state of the BGP routing tables. Assume that there are no routing policies in this Internet. 

   .. positive:: The BGP routing table of ``AS3`` contains only one path towards prefix ``2001:db8:4/48``. It's AS-Path is ``AS4``. 
 
   .. positive:: The BGP routing table of ``AS5`` contains only one path towards prefix ``2001:db8:4/48``. It's AS-Path is ``AS2:AS1:AS3:AS4``. 

   .. negative:: The BGP routing table of ``AS5`` contains only one path towards prefix ``2001:db8:4/48``. It's AS-Path is ``AS2:AS3:AS4``. 

      .. comment:: ``AS2`` has learned two paths for prefix ``2001:db8:4/48`` : ``AS3:AS4`` and ``AS1:AS3:AS4``. The second path is longer but has a highest local-preference. ``AS2`` will use it and advertise it to ``AS5``. 

   .. negative:: The BGP routing table of ``AS5`` contains two paths towards prefix ``2001:db8:4/48`` :  ``AS2:AS1:AS3:AS4`` and ``AS2:AS3:AS4``. ``AS5`` prefers and uses the path ``AS2:AS3:AS4``. 

      .. comment:: ``AS5`` only learns one path from ``AS2`` : ``AS2:AS1:AS3:AS4``. It never learns the path ``AS2:AS3:AS4``

   .. positive:: The BGP routing table of ``AS2`` contains two paths towards prefix ``2001:db8:4/48`` :  ``AS1:AS3:AS4`` and ``AS3:AS4``. ``AS2`` prefers and uses the path ``AS1:AS3:AS4``. 

   .. negative:: The BGP routing table of ``AS2`` contains only one path towards prefix ``2001:db8:4/48`` :  ``AS1:AS3:AS4``. 

      .. comment:: ``AS2`` learns two paths for this prefix, one from ``AS1`` and the other from ``AS3``. 

   .. negative:: The BGP routing table of ``AS2`` contains only one path towards prefix ``2001:db8:4/48`` :  ``AS3:AS4``. 

      .. comment:: ``AS2`` learns two paths for this prefix, one from ``AS1`` and the other from ``AS3``. 




7. A router belongs to ``AS5`` and is connected to three different ASes :
 
   - ``AS1`` is its main provider
   - ``AS2`` is a shared cost peer
   - ``AS3`` is a customer


 
.. question:: bgp2 
   :nb_prop: 3 
   :nb_pos: 1

   Which of the configurations below is a correct setting for the local-preference ?

   .. positive:: 

         - All routes received from ``AS1`` are tagged with a local-preference of 100 
         - All routes received from ``AS2`` are tagged with a local-preference of 150 
         - All routes received from ``AS3`` are tagged with a local-preference of 200

   .. negative::

         - All routes received from ``AS1`` are tagged with a local-preference of 100 
         - All routes received from ``AS2`` are tagged with a local-preference of 100 
         - All routes received from ``AS3`` are tagged with a local-preference of 100 

      .. comment:: On a BGP router, the routes received from a customer should be preferred over the routes received from a shared-cost peer and a provider. Similarly, the routes received from a shared-cost peer should be preferred over the routes received from a provider. 


   .. negative::

         - All routes received from ``AS1`` are tagged with a local-preference of 200 
         - All routes received from ``AS2`` are tagged with a local-preference of 150 
         - All routes received from ``AS3`` are tagged with a local-preference of 100 

      .. comment:: On a BGP router, the routes received from a customer should be preferred over the routes received from a shared-cost peer and a provider. Similarly, the routes received from a shared-cost peer should be preferred over the routes received from a provider. 



   .. negative::

         - All routes received from ``AS1`` are tagged with a local-preference of 150 
         - All routes received from ``AS2`` are tagged with a local-preference of 200 
         - All routes received from ``AS3`` are tagged with a local-preference of 100 

      .. comment:: On a BGP router, the routes received from a customer should be preferred over the routes received from a shared-cost peer and a provider. Similarly, the routes received from a shared-cost peer should be preferred over the routes received from a provider. 



