.. Copyright |copy| 2013 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


*****************
Sharing resources
*****************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=4


Medium Access Control
=====================

To understand the operation of Medium Access Control algorithms, it is often interesting to use a geometric representation of the transmission of frames on a shared medium. This representation is suitable if the communicating devices are attached to a single cable. Consider a simple scenario with a host connected at one end of a cable. For simplicity, let us consider a cable that has a length of one kilometer. Let us also consider that the propagation delay of the electrical signal is five microseconds per kilometer. The figure below shows the transmission of a 2000 bits frame at 100 Mbps by host A on the cable.

 .. tikz::
     :libs: positioning, matrix, arrows

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A} -- (1,9);
     \draw[thick, red, fill=red, -] (1,9) -- (1,5) -- (9,4) -- (9,8);



If the transmitting host is located at another position on the shared medium than one of the edges, then the geometrical pattern that represents the transmission of a frame is slightly different. If the transmitting host is placed in the middle of the cable, then the signal is transmitted in both directions on the cable. The figure below shows the transmission of one 100 bits frame at 100 Mbps by host C on the same cable.

 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, green, ->] (5,10) node [anchor=north, fill=white] {C} -- (5,9);
     \draw[thick, green, fill=green, -] (5,9) -- (5,7) -- (9,6.5) -- (9,8.5);
     \draw[thick, green, fill=green, -] (5,9) -- (5,7) -- (1,6.5) -- (1,8.5);

In a shared medium, a collision may happen if two hosts transmit at almost the same time as shown in the example below.


 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A} -- (1,9);
     \draw[very thick, blue, ->] (10,8) node [anchor=north, fill=white] {B} -- (9,7) ;
     \draw[thick, red, fill=red, -] (1,9) -- (1,5) -- (9,2) -- (9,6);
     \draw[thick, blue, fill=blue, -] (9,7) -- (9,5) -- (1,2) -- (1,4);

1. Consider the following scenario for the ALOHA medium access control algorithm. Three hosts are attached to a one-kilometer long cable and transmit 1000 bits frames at 1 Mbps. Each arrow represents a request to transmit a frame on the corresponding host. Each square represents 250 microseconds in the figure. Represent all the transmitted frames and list the frames that collide.

 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$250 \mu sec$};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A} -- (1,9);
     \draw[very thick, blue, ->] (10,8) node [anchor=north, fill=white] {B} -- (9,7);
     \draw[very thick, green, ->] (4,7) node [anchor=north, fill=white] {C} -- (5,6);
     \draw[very thick, blue, ->] (10,3) node [anchor=north, fill=white] {B} -- (9,2);


2. Same question as above, but now consider that the hosts transmit 1000 bits frames at 100 Mbps. The cable has a length of 2 kilometers. C is in the middle of the cable. Each square in the figure below corresponds to 10 microseconds.

 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
    \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
    \tikzset{ftable/.style={rectangle, dashed, draw} }
    \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
    \node [red, fill=white] at (1,10.5) {A};
    \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
    \node [blue, fill=white] at (9,10.5) {B};
    \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
    \node [green, fill=white] at (5,10.5) {C};
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
    \node [black, fill=white] (0,1) {time};
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$10 \mu sec$};
    \draw[very thick, -] (1,9) -- (9,9);
    \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A} -- (1,9);
    \draw[very thick, blue, ->] (10,9) node [anchor=north, fill=white] {B} -- (9,8);
    \draw[very thick, green, ->] (4,7) node [anchor=north, fill=white] {C} -- (5,6);
    \draw[very thick, blue, ->] (10,7) node [anchor=north, fill=white] {B} -- (9,6);

  .. no collision between A and B
  .. no collision B and C
  .. collision C and last B


3. In ALOHA, the hosts rely on acknowledgements to detect whether their frame has been received correctly by the destination. Consider a network running at 100 Mbps where the host exchange 1000 bits frames and acknowledgements of 100 bits. Draw the frames sent by hosts A and B in the figure below. Assume that a square corresponds to 10 microseconds and that the cable has a length of 2 kilometers. 

 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$10 \mu sec$};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A$\rightarrow$B [1000 bits]} -- (1,9);
     \draw[very thick, blue, ->] (10,9) node [anchor=north, fill=white] {B$\rightarrow$A [1000 bits]} -- (9,8);
     \draw[very thick, blue, ->] (10,7) node [anchor=north, fill=white] {B$\rightarrow$A [1000 bits]} -- (9,6);

4. Same question as above, but now assume that the retransmission timer of each host is set to 50 microseconds.


 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
    \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
    \tikzset{ftable/.style={rectangle, dashed, draw} }
    \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
    \node [red, fill=white] at (1,10.5) {A};
    \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
    \node [blue, fill=white] at (9,10.5) {B};
    \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
    \node [green, fill=white] at (5,10.5) {C};
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
    \node [black, fill=white] (0,1) {time};
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$10 \mu sec$};
    \draw[very thick, -] (1,9) -- (9,9);
    \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A$\rightarrow$B [1000 bits]} -- (1,9);
    \draw[very thick, green, ->] (4,9) node [anchor=north, fill=white] {C$\rightarrow$A [1000 bits]} -- (5,8);
    \draw[very thick, blue, ->] (10,7) node [anchor=north, fill=white] {B$\rightarrow$A [1000 bits]} -- (9,6);

  .. collision between the ack of A->B and C->A

5. In practice, hosts transmit variable length frames. Consider a cable having a bandwidth of 100 Mbps and a length of 2 kilometers. 


 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$10 \mu sec$};
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A$\rightarrow$B [2000 bits]} -- (1,9);
     \draw[very thick, green, ->] (4,8) node [anchor=north, fill=white] {C$\rightarrow$A [1000 bits]} -- (5,7);
     \draw[very thick, blue, ->] (10,6) node [anchor=north, fill=white] {B$\rightarrow$A [2000 bits]} -- (9,5);



6. With CSMA, hosts need to listen to the communication channel before starting their transmission. Consider again a 2 kilometers long cable where hosts send frames at 100 Mbps. Show in the figure below the correct transmission of frames with CSMA. 


 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$10 \mu sec$};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A$\rightarrow$B [2000 bits]} -- (1,9);
     \draw[very thick, green, ->] (4,9) node [anchor=north, fill=white] {C$\rightarrow$A [1000 bits]} -- (5,8);
     \draw[very thick, blue, ->] (10,7) node [anchor=north, fill=white] {B$\rightarrow$A [1000 bits]} -- (9,6);

     .. C->A needs to be delayed
  

7. CSMA/CD does not use acknowledgements but instead assumes that each host can detect collisions by listening while transmitting. Consider a 2 kilometers long cable running at 10 Mbps. Show in the figure below the utilisation of the communication channel and the collisions that would occur. For this exercise, do not attempt to retransmit the frames that have collided.

 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$10 \mu sec$};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A$\rightarrow$B [200 bits]} -- (1,9);
     \draw[very thick, green, ->] (4,10) node [anchor=north, fill=white] {C$\rightarrow$A [100 bits]} -- (5,9);
     \draw[very thick, blue, ->] (10,7) node [anchor=north, fill=white] {B$\rightarrow$A [100 bits]} -- (9,6);


     .. collision for A->B and C->A no collision for B



8. Consider again a network that uses CSMA/CD. This time, the bandwidth is set to 1 Gbps and the cable has a length of two kilometers. When a collision occurs, consider that the hosts B and C retransmit immediately while host A waits for the next slot.

 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$5 \mu sec$};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,10) node [anchor=north, fill=white] {A$\rightarrow$B [10000 bits]} -- (1,9);
     \draw[very thick, green, ->] (4,9) node [anchor=north, fill=white] {C$\rightarrow$A [10000 bits]} -- (5,8);
     \draw[very thick, blue, ->] (10,6) node [anchor=north, fill=white] {B$\rightarrow$A [10000 bits]} -- (9,5);
     \draw[very thick, red, ->] (0,5.5) node [anchor=north, fill=white] {A$\rightarrow$B [10000 bits]} -- (1,4.5);

9. An important part of the CSMA/CD algorithm is the exponential backoff. To illustrate the operation of this algorithm, let us consider a cable that has a length of one kilometer. The bandwidth of the network is set to 10 Mbps. Assume that when a collision occurs, host A always selects the highest possible random delay according to the exponential backoff algorithm while host B always selects the shortest one. In this network, the slot time is equal to the time required to transmit 100 bits. We further assume that a host can detect collision immediately (i.e. as soon as the other frame arrives).

 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \tikzstyle{arrow} = [thick,->,>=stealth]
     \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
     \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
     \tikzset{ftable/.style={rectangle, dashed, draw} }
     \draw[very thick, -, fill=red, red] (0.9,10) -- (1.1,10) -- ( 1.1, 10.1) -- (0.9,10.1);
     \node [red, fill=white] at (1,10.5) {A};
     \draw[very thick, -, fill=blue, blue] (8.9,10) -- (9.1,10) -- ( 9.1, 10.1) -- (8.9,10.1);
     \node [blue, fill=white] at (9,10.5) {B};
     \draw[very thick, -, fill=green, green] (4.9,10) -- (5.1,10) -- ( 5.1, 10.1) -- (4.9,10.1);
     \node [green, fill=white] at (5,10.5) {C};
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] (0,1) {time};
     \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$5 \mu sec$};
     \draw[very thick, -] (1,9) -- (9,9);
     \draw[very thick, red, ->] (0,8) node [anchor=north, fill=white] {A$\rightarrow$C [100 bits]} -- (1,7);
     \draw[very thick, blue, ->] (10,9) node [anchor=north, fill=white] {B$\rightarrow$C [100 bits]} -- (9,8);
     \draw[very thick, blue, ->] (10,7.5) node [anchor=north, fill=white] {B$\rightarrow$C [100 bits]} -- (9,6.5);


Fairness and congestion control
===============================

1. Consider the network below. Compute the max-min fair allocation for the hosts in this network assuming that nodes `Sx` always send traffic towards node `Dx`. Furthermore, link `R1-R2` has a bandwidth of 10 Mpbs while link `R2-R3` has a bandwidth of 20 Mbps.


   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (S1) {S1};
      \node[host, below=of S1] (S2) {S2};
      \node[host, below=of S2] (S3) {S3};
      \node[host, below=of S3] (S4) {S4};
      \node[host, below=of S4] (S5) {S5};
      \node[router, right=of S1] (R1) { R1 };
      \node[router,right=of R1] (R2) {R2};
      \node[router,below=of R1] (R3) {R3};
      \node[host, right=of R3] (D1) {D1};
      \node[host, right=of R2] (D2) {D2};
      \node[host, below=of D1] (D3) {D3};
      \node[host, above=of R1] (D4) {D4};
      \node[host, above=of R2] (D5) {D5};
      \draw[-] (R1) -- (R2); 
      \draw[-] (R2) -- (R3); 
      \draw[-] (S1)--(R1);
      \draw[-] (S2)--(R1);
      \draw[-] (S3)--(R1);
      \draw[-] (S4)--(R3);
      \draw[-] (S5)--(R3);
      \draw[-] (D1)--(R3);
      \draw[-] (D3)--(R3);
      \draw[-] (D4)--(R1);
      \draw[-] (D5)--(R2);
      \draw[-] (D2)--(R2);


To understand congestion control algorithms, it can also be useful to represent the exchange of packets by using a graphical representation. As a first example, let us consider a very simple network composed of two hosts interconnected through a switch.


   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[host, right=3 cm of A] (R) {R};
      \node[host, right=3 cm of R] (B) {B};
      \draw[-] (A) -- node [midway, above] { 3 Mbps} (R); 
      \draw[-] (R) -- node [midway, above] { 1 Mbps} (B); 


Suppose now that host A uses a window of three segments and sends these three segments immediately. The segments will be queued in the router before being transmitted on the output link and delivered to their destination. The destination will reply with a short acknowledgement segment. A possible visualisation of this exchange of packets is represented in the figure below. We assume for this figure that the router marks the packets to indicate congestion as soon as its buffer is non-empty when its receives a packet on its input link. In the figure, a `(c)` sign is added to each packet to indicate that it has been explicitly marked.


 .. tikz::
     :libs: positioning, matrix, arrows 

     \colorlet{lightgray}{black!20}
     \colorlet{ligthred}{red!25}
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] at (0,1) {time};
     \draw[thick, red, -] (2,9) -- (2,1);
     \node [red, fill=white] at (1.5,9) {Input};
     \draw[thick, black, -] (4,9) -- (4,1);
     \node [black, fill=white] at (5,9) {Output};
     \draw[black, fill=red!25] (1,8) -- (1,8.5) -- (2, 8.5) -- (2,8) -- (1,8);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,8.2) {P1};
     \draw[black, fill=red!25] (1,7.5) -- (1,8) -- (2, 8) -- (2,7.5) -- (1,7.5);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,7.7) {P2};
     \draw[black, fill=red!25] (1,7) -- (1,7.5) -- (2, 7.5) -- (2,7) -- (1,7);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,7.2) {P3};

     \draw[black, fill=red!25] (4,8) -- (4,6.5) -- (7,6.5) -- (7,8) -- (4,8);
     \node[black, fill=red!25, font=\scriptsize] at (5,7.2) {P1};
     \draw[black, fill=red!25] (4,6.5) -- (4,5) -- (7,5) -- (7,6.5) -- (4,6.5);
     \node[black, fill=red!25, font=\scriptsize] at (5,5.7) {P2(c)};
     \draw[black, fill=red!25] (4,5) -- (4,3.5) -- (7,3.5) -- (7,5) -- (4,5);
     \node[black, fill=red!25, font=\scriptsize] at (5,4.2) {P3(c)};

     \draw[very thick, red, ->] (7,6.5) -- (1,6.5);
     \draw[very thick, red, ->] (7,5) -- (1,5);
     \draw[very thick, red, ->] (7,3.5) -- (1,3.5);

In practice, a router is connected to multiple input links. The figure below shows an example with two hosts. 
     

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host, red] (A) {A};
      \node[host, right=3 cm of A] (R) {R};
      \node[host, right=3 cm of R] (C) {C};
      \node[host, below=of A, blue] (B) {B};
      \draw[-] (A) -- node [midway, above] { 2 Mbps} (R); 
      \draw[-] (B) -- node [midway, fill=white, below] { 2 Mbps} (R); 
      \draw[-] (R) -- node [midway, above] { 1 Mbps} (C); 


 .. tikz::
     :libs: positioning, arrows 

     \colorlet{lightgray}{black!20}
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] at (0,1) {time};
     \draw[thick, red, -] (2,9) -- (2,1);
     \node [red, fill=white] at (1.5,9) {InputA};
     \draw[thick, blue, -] (3.5,9) -- (3.5,1);
     \node [blue, fill=white] at (3.4,9) {InputB};
     \draw[thick, black, -] (4.5,9) -- (4.55,1);
     \node [black, fill=white] at (5.2,9) {Output};
     \draw[black, fill=red!25] (1,8) -- (1,8.5) -- (2, 8.5) -- (2,8) -- (1,8);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,8.2) {P1};
     \draw[black, fill=red!25] (1,7.5) -- (1,8) -- (2, 8) -- (2,7.5) -- (1,7.5);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,7.7) {P2};

     \draw[black, fill=blue!25] (2.5,8) -- (2.5,8.5) -- (3.5, 8.5) -- (3.5,8) -- (2.5,8);
     \node[black, fill=blue!25, font=\scriptsize] at (3,8.2) {P1};
     \draw[black, fill=blue!25] (2.5,7.5) -- (2.5,8) -- (3.5, 8) -- (3.5,7.5) -- (2.5,7.5);
     \node[black, fill=blue!25, font=\scriptsize] at (3,7.7) {P2};

     \draw[black, fill=red!25] (4.5,8) -- (4.5,7) -- (7,7) -- (7,8) -- (4.5,8);
     \draw[very thick, red, ->] (7,7) -- (1,7);
     \node[black, fill=red!25, font=\scriptsize] at (5,7.5) {P1};

     \draw[black, fill=blue!25] (4.5,7) -- (4.5,6) -- (7,6) -- (7,7) -- (4.5,7);
     \draw[very thick, blue, ->] (7,6) -- (2.5,6);
     \node[black, fill=blue!25, font=\scriptsize] at (5,6.5) {P1(c)};

     \draw[black, fill=red!25] (4.5,6) -- (4.5,5) -- (7,5) -- (7,6) -- (4.5,6);
     \draw[very thick, red, ->] (7,5) -- (1,5);
     \node[black, fill=red!25, font=\scriptsize] at (5,5.5) {P2(c)};

     \draw[black, fill=blue!25] (4.5,5) -- (4.5,4) -- (7,4) -- (7,5) -- (4.5,5);
     \draw[very thick, blue, ->] (7,4) -- (2.5,4);
     \node[black, fill=blue!25, font=\scriptsize] at (5,4.5) {P2(c)};

 
In general, the links have a non-zero delay. This is illustrated in the figure below where a delay has been added on the link between `R` and `C`.

 .. tikz::
     :libs: positioning, arrows, backgrounds 

     \colorlet{lightgray}{black!20}
     \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
     \draw[very thick,->] (0.5,9.5) -- (0.5,0.5);
     \node [black, fill=white] at (0,1) {time};
     \draw[thick, red, -] (2,9) -- (2,1);
     \node [red, fill=white] at (1.5,9) {InputA};
     \draw[thick, blue, -] (3.5,9) -- (3.5,1);
     \node [blue, fill=white] at (3.4,9) {InputB};
     \draw[thick, black, -] (4.5,9) -- (4.55,1);
     \node [black, fill=white] at (5.2,9) {Output};
     \draw[black, fill=red!25] (1,8) -- (1,8.5) -- (2, 8.5) -- (2,8) -- (1,8);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,8.2) {P1};
     \draw[black, fill=red!25] (1,7.5) -- (1,8) -- (2, 8) -- (2,7.5) -- (1,7.5);
     \node[black, fill=red!25, font=\scriptsize] at (1.5,7.7) {P2};

     \draw[black, fill=blue!25] (2.5,8) -- (2.5,8.5) -- (3.5, 8.5) -- (3.5,8) -- (2.5,8);
     \node[black, fill=blue!25, font=\scriptsize] at (3,8.2) {P1};
     \draw[black, fill=blue!25] (2.5,7.5) -- (2.5,8) -- (3.5, 8) -- (3.5,7.5) -- (2.5,7.5);
     \node[black, fill=blue!25, font=\scriptsize] at (3,7.7) {P2};

     \begin{pgfonlayer}{background}

     \draw[black, fill=red!25] (4.5,8) -- (4.5,7) -- (7,6) -- (7,7) -- (4.5,8);
     \node[black, fill=red!25, font=\scriptsize] at (5,7.5) {P1};

     \draw[black, fill=blue!25] (4.5,7) -- (4.5,6) -- (7,5) -- (7,6) -- (4.5,7);
 
     \node[black, fill=blue!25, font=\scriptsize] at (5,6.5) {P1(c)};

     \draw[black, fill=red!25] (4.5,6) -- (4.5,5) -- (7,4) -- (7,5) -- (4.5,6);
 
     \node[black, fill=red!25, font=\scriptsize] at (5,5.5) {P2(c)};

     \draw[black, fill=blue!25] (4.5,5) -- (4.5,4) -- (7,3) -- (7,4) -- (4.5,5);

     \node[black, fill=blue!25, font=\scriptsize] at (5,4.5) {P2(c)};
     \end{pgfonlayer}
     \draw[very thick, red, ->] (7,6) -- (1,5);
     \draw[very thick, blue, ->] (7,5) -- (2.5,4);
     \draw[very thick, red, ->] (7,4) -- (1,3);
     \draw[very thick, blue, ->] (7,3) -- (2.5,2);

2. Consider the network depicted in the figure below.

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[host, right=3 cm of A] (R1) {R1};
      \node[host, right=3 cm of R1] (R2) {R2};
      \node[host, below=of A] (B) {B};
      \node[host, right=3 cm of R2] (D) {D};
      \draw[-] (A) -- node [midway, above, fill=white, align=center] { 1 Mbps \\ 0 msec} (R1); 
      \draw[-] (B) -- node [midway, below, align=center] { 10 Mbps \\ 10 msec} (R1); 
      \draw[-] (R1) -- node [midway, fill=white, below, align=center] { 1 Mbps\\10 msec} (R2); 
      \draw[-] (R2) -- node [midway, below, align=center] { 100 Mbps \\ 0 msec} (D); 


 a. In this network, compute the minimum round-trip-time between `A` (resp. `B`) and `D`. Perform the computation if the hosts send segments containing 1000 bits. 
 b. How is the maximum round-trip-time influenced if the buffers of router `R1` store 10 packets ?  
 c. If hosts `A` and `B` send to `D` 1000 bits segments and use a sending window of four segments, what is the maximum throughput that they can achieve ?
 d. Assume now that `R1` is using round-robin scheduling instead of a FIFO buffer. One queue is used to store the packets sent by `A` and another for the packets sent by `B`. `A` sends one 1000 bits packet every second while `B` sends packets at 10 Mbps. What is the round-trip-time measured by each of these two hosts if each of the two queues of `R1` can store 5 packets ? 


3. When analyzing the reaction of a network using round-robin schedulers, it is sometimes useful to consider that the packets sent by each source are equivalent to a fluid and that each scheduler acts as a tap. Using this analogy, consider the network below. In this network, all the links are 100 Mbps and host `B` is sending packets at 100 Mbps. If A sends at 1, 5, 10, 20, 30, 40, 50, 60, 80 and 100 Mbps, what is the throughput that destination `D` will receive from `A`. Use this data to plot a graph that shows the portion of the traffic sent by host `A` which is received by host `D`. 


   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[host, right=3 cm of A] (R1) {R1};
      \node[host, below=of A] (B) {B};
      \node[host, right=3 cm of R1] (D) {D};
      \draw[-] (A) -- (R1); 
      \draw[-] (B) -- (R1); 
      \draw[-] (R1)  (D); 

4. Compute the max-min fair bandwidth allocation in the network below.

 .. figure:: ../principles/figures/png/ex-fairness.png
    :align: center


    Simple network topology


5. Consider the simple network depicted in the figure below.   

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[host, right=3 cm of A] (R1) {R1};
      \node[host, right=3 cm of R1] (R2) {R2};
      \node[host, right=3 cm of R2] (D) {D};
      \draw[-] (A) -- node [midway, above, fill=white, align=center] { 1 Mbps} (R1); 
      \draw[-] (R1) -- node [midway, fill=white, below, align=center] { 250 kbps} (R2); 
      \draw[-] (R2) -- node [midway, below, align=center] { 100 Mbps} (D); 


 a. In this network, a 250 Kbps link is used between the routers. The propagation delays in the network are negligible. Host `A` sends 1000 bits long segments so that it takes one msec to transmit one segment on the `A-R1` link. Neglecting the transmission delays for the acknowledgements, what is the minimum round-trip time measured on host `A` with such segments ?
 b. If host `A` uses a window of two segments and needs to transmit five segments of data. How long does the entire transfer lasts ?
 c. Same question as above, but now host `A` uses the simple DECBIT congestion control mechanism and a maximum window size of four segments.

6. Consider the network depicted in the figure below.

   .. tikz::
      :libs: positioning, matrix, arrows 

      \tikzstyle{arrow} = [thick,->,>=stealth]
      \tikzset{router/.style = {rectangle, draw, text centered, minimum height=2em}, }
      \tikzset{host/.style = {circle, draw, text centered, minimum height=2em}, }
      \tikzset{ftable/.style={rectangle, dashed, draw} }
      \node[host] (A) {A};
      \node[host, right=3 cm of A] (R1) {R1};
      \node[host, below=of A] (B) {B};
      \node[host, right=3 cm of R1] (D) {D};
      \draw[-] (A) -- node [midway, above, fill=white, align=center] { 1 Mbps\\ 10 msec} (R1);
      \draw[-] (B) -- node [midway, above, fill=white, align=center] { 1 Mbps\\ 0 msec} (R1);
      \draw[-] (R1) -- node [midway, fill=white, below, align=center] { 500 kbps \\ 0 msec} (D); 

 Hosts `A` and `B` use the simple congestion control scheme described in the book and router `R1` uses the DECBIT mechanism to mark packets as soon as its buffers contain one packet. Hosts `A` and `B` need to send five segments and start exactly at the same time. How long does each hosts needs to wait to receive the acknowledgement for its fifth segment ?

Discussion questions
====================

1. In a deployed CSMA/CD network, would it be possible to increase or decrease the duration of the slottime ? Justify your answer

2. Consider a CSMA/CD network that contains hosts that generate frames at a regular rate. When the transmission rate increases, the amount of collisions increases. For a given network load, measured in bits/sec, would the number of collisions be smaller, equal or larger with short frames than with long frames ?

3. Slotted ALOHA improves the performance of ALOHA by dividing the time in slots. However, this basic idea raises two interested questions. First how would you enforce the duration of these slots ? Second, should a slot include the time to transmit a data frame or the time to transmit a data frame and the corresponding acknowledgement ?

4. Like ALOHA, CSMA relies on acknowledgements to detect where a frame has been correctly received. When a host senses an idle channel, if should transmit its frame immediately. How should it react if it detects that another host is already transmitting ? Consider two options :

 - the host continues to listen until the communication channel becomes free. It transmits as soon as the communication channel becomes free.
 - the host stops to listen and waits for a random time before sensing again the communication channel to check whether it is free.

.. include:: /links.rst
