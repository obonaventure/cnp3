.. Copyright |copy| 2013 by Olivier Bonaventure, Florentin Rochet, Justin Vellemans
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_



Building a network
==================

:task_id: network_principles

1. Shortest Path Tree
---------------------

.. question::
   :nb_pos: 1 
   :nb_prop: 3

 Consider the network shown in the figure below. The numbers attached to the links indicate the link weights. 

  .. figure:: images/qcm1-1-shortestPath.png
     :align: center
     :scale: 100


 Only one of the graphs below corresponds to the shortest path tree for the above network. Which one ?

 .. positive::

    .. figure:: images/qcm1-1-solution1.png 
       :align: center
       :scale: 100
  
 .. positive::

     .. figure:: images/qcm1-1-solution2.png 
        :align: center
        :scale: 100

 .. negative::


   .. figure:: images/qcm1-1-wrong1.png 
      :align: center
      :scale: 100

 .. negative::

    .. figure:: images/qcm1-1-wrong2.png 
       :align: center
       :scale: 100


2. Forwarding tables
--------------------

.. question::
   :nb_pos: 1 
   :nb_prop: 3

The network below is using link state routing or distance vector routing with the link weights shown in the graph. Each router computes its own forwarding table that indicates the nexthop to reach each destination address.

  .. figure:: images/qcm1-1-shortestPath.png
     :align: center
     :scale: 100

Only one of these forwarding tables is correct. Which one?


 .. positive::

  .. code-block:: console

        Router A: (A=0[local], B=4[South], C=3[South-East], D=6[South-East], E=8[South])

 .. positive::

  .. code-block:: console

        Router A: (A=0[local], B=4[South], C=3[South-East], D=6[South-East], E=8[South-East])
     
 .. positive::

  .. code-block:: console

        Router C: (C=0[local], A=3[North-West], B=7[North-West], D=3[Noth-East], E=5[South-East])
     
 .. positive::

  .. code-block:: console

        Router D: (D=0[local], A=6[South-West], C=3[South-West], B=10[South-West], E=8[South-West])
     

 .. negative::

  .. code-block:: console

        Router A: (B=4[South], C=3[South-East], D=6[South-East], E=8[South])

 .. negative::

  .. code-block:: console

        Router A: (A=0[local], B=4[South], C=3[South-East], D=10[West], E=8[South-East])
     
 .. negative::

  .. code-block:: console

        Router C: (C=0[local], A=3[North-West], B=7[East], D=3[Noth-East], E=5[South-East])
     

 .. negative::

  .. code-block:: console

        Router D: (D=0[West], A=6[South-West], C=3[South-West], B=8[South-West], E=8[South-West])
     


Question 3. Link state routing
-------------------------------

.. question::
   :nb_pos: 1 
   :nb_prop: 3

 The network shown in the figure below uses link state routing. 


  .. figure:: images/qcm1-1-shortestPath.png
     :align: center
     :scale: 100

 All routers have been up for some time. Among the different link stat packets listed below, only one corresponds to a link state packet that could have been captured in this network. Which one ?

 The format of the LSPs  is: `LSP : [Sender] [Age] [Sequence Number] [List of Adjacent Active Links]`.

 .. positive::

    `LSP : A 60 31 [C:3];[D:10];[B:4]`

 .. positive::

    `LSP : D 15 5 [C:3];[A:10];[E:10]`

 .. positive::

    `LSP : C 24 26 [D:3];[A:3];[E:5]`

 .. positive::

    `LSP : B 12 1 [A:4];[E:4]`

 .. positive::

    `LSP : E 10 18 [C:5];[D:10];[B:4]`

 .. negative::

    `LSP : A 15 24 [C:3];[D:6];[B:4];`

  .. comment::

	 	 A LSP from a router contains only the costs to the directly connected neighbors. It does not compute a shortest path. The cost from A to D is thus 10 not 6.

 .. negative:: 
    
    `LSP : A 60 19 [C:3];[D:6];[B:4];[E:8]`

    .. comment::

	A LSP from a router contains only the costs to the directly connected neighbors. It does not include information about addresses that are noted directly connected.

 .. negative:: 
    
    `LSP : D 21 60 [C:3];[A:6];[E:8]`

    .. comment::

	 	 A LSP from a router contains only the costs to the directly connected neighbors. It does not compute a shortest path. The cost from A to D is thus 10 not 6.


  .. negative:: 

     `LSP : D 15 63 [C:3];[A:6];[E:8];[B:10]`

     .. comment::

	A LSP from a router contains only the costs to the directly connected neighbors. It does not include information about addresses that are noted directly connected.


  .. negative:: 

     `LSP : C 32 1 [D:3];[A:3];[E:5];[B:7]`

     .. comment::

	A LSP from a router contains only the costs to the directly connected neighbors. It does not include information about addresses that are noted directly connected.
  
  .. negative:: 

     `LSP : B 47 62 [A:4];[E:4];[C:7];[D:10]`

      .. comment::

	A LSP from a router contains only the costs to the directly connected neighbors. It does not include information about addresses that are noted directly connected.

 .. negative:: 

    `LSP : E 25 25 [C:5];[D:8];[B:4]`

     .. comment::

 	 A LSP from a router contains only the costs to the directly connected neighbors. It does not compute a shortest path.  The cost from E to D is thus 10 not 8.

 .. negative::

    `LSP : E 14 18 [C:5];[D:8];[B:4];[A:8]`

    .. comment::

	A LSP from a router contains only the costs to the directly connected neighbors. It does not include information about addresses that are noted directly connected.



4. Distance vector routing
--------------------------

Consider again the same network shown in the figure below. This time, the network is using distance vector routing.

  .. figure:: images/qcm1-1-shortestPath.png
     :align: center
     :scale: 100


.. question::
   :nb_prop: 3
   :nb_pos: 1
	     
Among the sequences of distance vectors shown below, only one is a valid sequence for the above network. Which one ? 


 .. positive::


  .. code-block:: console

      - D: [D=0]
      - A: [A=0, D=10]
      - B: [B=0]
      - C: [C=0, A=3, D=3]
      - E: [E=0, A=8, B=4, C=5, D=8]
      - D: [D=0, A=6, B=14, C=3, E=10]
      - B: [B=0, A=4, C=9, E=4, D=14]
      - A: [A=0, B=4, C=3, D=6, E=8]


 .. positive::

  .. code-block:: console

      - C: [C=0]
      - A: [A=0, C=3]
      - D: [D=0, C=3, A=10]
      - E: [E=0, A=20, C=5, D=10]
      - B: [B=0, A=4, E=4, C=7, D=14]
      - C: [C=0, A=3, D=3, E=5]
      - E: [E=0, A=8, C=5, D=8, B=4]
      - A: [A=0, B=4, C=3, D=6, E=8]


 .. negative::

  .. code-block:: console

      - B: [B=0]
      - C: [C=0]
      - D: [D=0, C=3]
      - A: [A=0, B=4, C=3, D=10]
      - E: [E=0, C=5, B=4, D=10]
      - D: [D=0, A=6, B=14, C=3, E=10]
      - B: [B=0, A=4, C=7, E=4, D=14]
      - A: [A=0, B=4, C=3, D=6, E=8]
      - C: [C=0, A=3, D=3, E=5, B=7]

    .. comment::

      At line 6: Router `D` cannot know how to reach `A` with a cost of 6 until router `C` has sent its vector. 


  .. negative::

    .. code-block:: console

      - D: [D=0]
      - A: [A=0, D=10]
      - B: [B=0, A=4]
      - C: [C=0, A=3, D=3, B=7]
      - E: [E=0, A=8, B=4, C=5, D=10]
      - D: [D=0, A=6, B=10, C=3, E=10]
      - B: [B=0, A=4, C=7, E=4, D=14]
      - A: [A=0, B=4, C=3, D=6, E=8]

    .. comment::

	At line 4: Router C cannot know how to reach `B`. Indeed `B` has sent its vector to `A` and `E` only. `B` will be reachable by `C` only once `A` or `E` send their vector.

  .. negative::

   .. code-block:: console

      - C: [C=0]
      - A: [A=0, C=3]
      - D: [D=0, C=3, A=6]
      - E: [E=0, A=8, C=5, D=10]
      - B: [B=0, A=4, E=4, C=9, D=14]
      - C: [C=0, A=3, D=3, E=5]
      - E: [E=0, A=8, C=5, D=5, B=4]
      - A: [A=0, B=4, C=3, D=6, E=8]

   .. comment::

      At line 3: Router `D` only knows a route of cost `10` to reach À`. It will learn later the best route with cost `6`. 




    

