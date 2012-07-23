.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. Exercises

Ejercicios
##########

.. 1. The host H0 pings its peer H1 in the network depicted in the figure below. Explain precisely what happened in the network since it has started.

1. El nodo H0 hace ping a su `peer` H1 en la red que se muestra en la figura siguiente. Explique con precisión qué ocurre en la red desde el momento en que H0 inicia su acción.

.. figure:: svg/ex-switches_w_simple_STP.png
   :align: center
   :scale: 70

.. 2. Consider the switched network shown in the figure below. What is the spanning tree that will be computed by 802.1d in this network assuming that all links have a unit cost ? Indicate the state of each port.

2. Considere la red conmutada que se muestra en la figura siguiente. ¿Cuál es el estado del árbol de expansión que será computado por 802.1d en esta red, suponiendo que todos los enlaces tienen un costo unitario? Indique el estado de cada puerto.

.. figure:: svg/ex-switches.png
   :align: center
   :scale: 70

   Una pequeña red compuesta de switches Ethernet
..   A small network composed of Ethernet switches

.. 3. Consider the switched network shown in the figure above. In this network, assume that the LAN between switches `3` and `12` fails. How should the switches update their port/address tables after the link failure ?

Considere la red conmutada de la figura anterior. En esta red, suponga que la LAN ubicada entre switches `3` y `12` falla. ¿Cómo actualizarían los switches sus tablas de puerto/dirección MAC luego de la falla del enlace?

.. 4. In the network depicted in the figure below, the host H0 performs a traceroute toward its peer H1 (designated by its name) through a network composed of switches and routers. Explain precisely the frames, packets, and segments exchanged since the network was turned on. You may assign addesses if you need to.

En la red que se muestra más abajo, el nodo H0 ejecuta un `traceroute` hacia su `peer` H1 (designándolo por su nombre) a través de una red compuesta de switches y routers. Explique con precisión las tramas, paquetes y segmentos intercambiados desde que la red entró en actividad. Puede asignar direcciones si es necesario.

.. figure:: svg/ex-switches_vs_routers.png
   :align: center
   :scale: 100

   El nodo H0 ejecuta traceroute hacia su peer H1 a través de una red con switches y routers.
.. The host H0 performs a traceroute toward its peer H1 through a network composed of switches and routers.

.. 5. Many enterprise networks are organized with a set of backbone devices interconnected by using a full mesh of links as shown in the figure below. In this network, what are the benefits and drawbacks of using Ethernet switches and IP routers running OSPF ?

5. Muchas redes corporativas están organizadas con un conjunto de dispositivos de backbone interconectados usando una trama completa de enlaces, como se muestra en la figura siguiente. En esta red, ¿cuáles son los beneficios y desventajas de usar switches Ethernet y routers IP corriendo OSPF?

.. figure:: svg/ex-backbone.png
   :align: center
   :scale: 70

   Un típico backbone de red corporativa
..   A typical enterprise backbone network 

.. 6. In the network represented on the figure below, can the host H0 communicate with H1 and vice-versa? Explain. Add whatever you need in the network to allow them to communicate.

6. En la red representada en la figura siguiente, ¿puede el nodo H0 comunicarse con H1 y viceversa? Explique. Agregue lo que necesite en la red para permitirles comunicarse.

.. figure:: svg/ex-routing_across_VLANs.png
   :align: center
   :scale: 70

   ¿Pueden comunicarse H0 y H1?
..   Can H0 and H1 communicate?

.. 7. Consider the network depicted in the figure below. Both of the hosts H0 and H1 have two interfaces: one connected to the switch S0 and the other one to the switch S1. Will the link between S0 and S1 ever be used? If so, under which assumptions? Provide a comprehensive answer.

7. Considere la red mostrada en la siguiente figura. Ambos nodos H0 y H1 tienen dos interfaces: una conectada al switch S0 y la otra conectada al switch S1. El enlace entre S0 y S1, ¿será usado alguna vez? En caso afirmativo, ¿bajo qué suposiciones? Dé una respuesta completa.

.. figure:: svg/ex-switches_wo_STP.png
   :align: center
   :scale: 70

   ¿Se usará alguna vez el enlace entre los switches S0 y S1?
..   Will the link between the switches S0 and S1 ever be used?

.. 8. Most commercial Ethernet switches are able to run the Spanning tree protocol independently on each VLAN. What are the benefits of using per-VLAN spanning trees ?

8. La mayoría de los switches Ethernet comerciales son capaces de correr el protocolo de Árbol de Expansión independientemente en cada VLAN. ¿Cuáles son los beneficios de usar un árbol de expansión por cada VLAN?


