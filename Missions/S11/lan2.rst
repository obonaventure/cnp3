Ethernet networks
=================

The deadline for this exercise is Tuesday December 15th, 13.00.

Exercices
---------


#. Consider the switched network shown in the figure below. What is the spanning tree that will be computed by 802.1d in this network assuming that all links have a unit cost ? Indicate the state of each port.


.. figure:: switchesok.pdf
   :align: center
   :scale: 70 

   A small network composed of Ethernet switches

.# Consider the switched network shown in the figure above.  In this network, assume that the LAN between switches $3$ and $12$ fails. How should the switches update their port/address tables after the link failure ?


#. Many enterprise networks are organized with a set of backbone devices interconnected by using a full mesh of links as shown in the figure below. In this network, what are the benefits and drawbacks of using Ethernet switches and IP routers running OSPF ?

.. figure:: switchesok.pdf
   :align: center
   :scale: 70 

   A typical enterprise backbone network 

\begin{figure}[htbp]
\begin{center}
\includegraphics[scale=0.25]{backbone.pdf}
\label{figure:backbone}\caption{A typical backbone enterprise network}
\end{center}
\end{figure}

\item Most Ethernet switches are able to run the Spanning tree protocol independently on each VLAN. What are the benefits of using per-VLAN spanning trees ?
