.. Copyright |copy| 2013, 2014 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. _mcq-congestion:

**************************
TCP and congestion control
**************************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 


A complete TCP implementation includes several mechanisms that interact together : reliable transfert that uses acknowledgements, timers, retransmissions, flow control that relies on sliding windows and congestion control. To understand the interactions between these different mechanisms, we analyse how TCP reacts in various situations where some of these mechanisms are disabled. Then we progressively add new mechanisms to end the exercises with a fairly complete TCP implementation.

Unless otherwise noted, we assume for the exercices in this section that the following conditions hold.

 - the sender/receiver performs a single :manpage:`send(3)` of `x` bytes
 - the round-trip-time is fixed and does not change during the lifetime of the TCP connection. We assume a fixed value of 100 milliseconds for the rtt and a fixed value of 200 milliseconds for the retransmission timer.
 - the delay required to transmit a single TCP segment containing MSS bytes is small and set to 1 milliseconds, independently of the MSS size
 - the transmission delay for a TCP ack is negligible
 - the initial value of the congestion window is one MSS-sized segment
 - the value of the duplicate ack threshold is fixed and set to 3
 - TCP always acks each received segment
 
:task_id: icwnd

Congestion control
------------------

1. To understand the operation of the TCP congestion control, it is often useful to write time-sequence diagrams for different scenarios. The example below shows the operation of the TCP congestion control scheme in a very simple scenario. The initial congestion window (``cwnd``) is set to 1000 bytes and the receive window (``rwin``) advertised by the receiver (supposed constant for the entire connection) is set to 2000 bytes. The slow-start threshold (``ssthresh``) is set to 64000 bytes.

 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$25 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=2000 \\
      cwnd=1000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(3k)} -- (3,9);
    \draw[black,thick, ->] (3,9) -- (7,8) node [midway, fill=white] {0:1000};
    \draw[black,thick, ->] (7,8) -- (3,7) node [midway, fill=white] {ack 1000};
    \node [state] at (0,6) {\begin{small}\begin{tabular}{l}
      rwin=2000 \\
      cwnd=2000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    \draw[black,thick, ->] (3,7) -- (7,6) node [midway, fill=white] {1000:2000};
    \draw[black,thick, ->] (3,6.5) -- (7,5.5) node [midway, fill=white] {2000:3000};
    \draw[black,thick, ->] (7,6) -- (3,5) node [midway, fill=white] {ack 2000};
    \draw[black,thick, ->] (7,5.5) -- (3,4.5) node [midway, fill=white] {ack 3000};


 a. Can you explain why the sender only sends one segment first and then two successive segments (the delay between the two segments on the figure is due to graphical reasons) ?

 b. Can you explain why the congestion window is increased after the reception of the first ack ?

 c. How long does it take for the sender to deliver 3 KBytes to the receiver ?


2. Same question as above but now with a small variation. Recent TCP implementations use a large initial value for the congestion window. Draw the time-sequence diagram that corresponds to an initial value of 10000 bytes for this congestion window.


 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$25 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=2000 \\
      cwnd=10000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(3k)} -- (3,9);

3. Same question as the first one, but consider that the MSS on the sender is set to 500 bytes. How does this modification affect the entire delay ? 

 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$25 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=2000 \\
      cwnd=1000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(10k)} -- (3,9);
   
4. Assuming that there are no losses and that there is no congestion in the network. If the sender writes `x` bytes on a newly established TCP connection, derive a formula that computes the minimum time required to deliver all these `x` bytes to the receiver. For the derivation of this formula, assume that `x` is a multiple of the maximum segment size and that the receive window and the slow-start threshold are larger than `x`. 

5. In question 1, we assumed that the receiver acknowledged every segment received from the sender. In practice, many deployed TCP implementations use delayed acknowledgements. Assuming a delayed acknowledgement timer of 50 milliseconds, modify the time-sequence diagram below to reflect the impact of these delayed acknowledgement. Does their usage decreases or increased the transmission delay ?

 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$25 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=2000 \\
      cwnd=1000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(3k)} -- (3,9);
    \draw[black,thick, ->] (3,9) -- (7,8) node [midway, fill=white] {0:1000};
    \draw[black,thick, ->] (7,8) -- (3,7) node [midway, fill=white] {ack 1000};
    \node [state] at (0,6) {\begin{small}\begin{tabular}{l}
      rwin=2000 \\
      cwnd=2000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    \draw[black,thick, ->] (3,7) -- (7,6) node [midway, fill=white] {1000:2000};
    \draw[black,thick, ->] (3,6.5) -- (7,5.5) node [midway, fill=white] {2000:3000};
    \draw[black,thick, ->] (7,6) -- (3,5) node [midway, fill=white] {ack 2000};
    \draw[black,thick, ->] (7,5.5) -- (3,4.5) node [midway, fill=white] {ack 3000};


6. The congestion control scheme in a TCP implementation can operate in slow-start or in congestion avoidance mode. For this, the implementation compares the current value of the congestion window with the slow-start threshold. 

.. question:: ss-ca
   :nb_prop: 3 
   :nb_pos: 1 

   Among the TCP states shown below, which is the one that corresponds to a connection operating in congestion avoidance ? 

   .. positive:: cwnd=64000 and ssthresh=64000

   .. positive:: cwnd=4000 and  ssthresh=2000

   .. negative:: cwnd=4000 and  ssthresh=48000 

      .. comment:: A TCP connection operates in congestion avoidance when its congestion window is larger or equal than the slow-start threshold 

   .. negative:: cwnd=2000 and  ssthresh=4000 

      .. comment:: A TCP connection operates in congestion avoidance when its congestion window is larger or equal than the slow-start threshold 

   .. negative:: cwnd=4000 and  ssthresh=8000 

      .. comment:: A TCP connection operates in congestion avoidance when its congestion window is larger or equal than the slow-start threshold 
        

7. Let us now explore the impact of congestion on the slow-start and congestion avoidance mechanisms. Consider the scenario below. For graphical reasons, it is not possible anymore to show information about the segments on the graph, but you can easily infer them. 


 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=64000 \\
      cwnd=4000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(10k)} -- (3,9);
    \draw[black,thick, ->] (3,9) -- (7,7.75);
    \draw[black,thick, ->] (3,8.7) -- (7,7.45);
    \draw[black,thick, ->] (3,8.4) -- (7,7.15);
    \draw[black,thick, ->] (3,8.1) -- (7,6.85);
    \draw[black,thick, ->] (7,7.75) -- (3,6.5);
    \draw[black,thick, ->] (7,7.45) -- (3,6.2);
    \draw[black,thick, ->] (7,7.15) -- (3,5.9);
    \draw[black,thick, ->] (7,6.855) -- (3,5.6);

    \node [state] at (0,6) {\begin{small}\begin{tabular}{l}
      rwin=64000 \\
      cwnd=8000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    \draw[black,thick, ->] (3,6.5) -- (7,5.25);
    \draw[black,thick, ->] (3,6.25) -- (7,5);
    \draw[black,thick, ->] (3,6) -- (7,4.75);
    \draw[black,thick, ->] (3,5.75) -- (7,4.5);
    \draw[black,thick, ->] (3,5.5) -- (7,4.25);
    \draw[black,thick, ->] (3,5.25) -- (7,4);

    \draw[black,thick, ->] (7,5.25) -- (3,4);
    \draw[black,thick, ->] (7,5) -- (3,3.75);
    \draw[black,thick, ->] (7,4.75) -- (3,3.5);
    \draw[black,thick, ->] (7,4.5) -- (3,3.25);
    \draw[black,thick, ->] (7,4.25) -- (3,3);
    \draw[black,thick, ->] (7,4) -- (3,2.75);
    \node [state] at (0,2.5) {\begin{small}\begin{tabular}{l}
      rwin=64000 \\
      cwnd=16000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};


 a. Redraw the same figure assuming that the second segment that was delivered by the sender in the figure experienced congestion. In a network that uses Explicit Congestion Notification, this segment would be marked by routers and the receiver would return the congestion mark in the corresponding acknowledgement. 

 b. Same question, but assume now that the fourth segment delivered by the sender experienced congestion (but was not discarded).

8. A TCP has been active for some time and reached a congestion window of 8000 bytes (its initial value was 1000 bytes). At this point, there is no unacknowledged data and the application running on the sender tries to send 2000 bytes of data.

 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=64000 \\
      cwnd=8000 \\ 
      ssthresh=64000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(2k)} -- (3,9);
    \draw[black,thick, ->] (3,9) -- (7,7.75);
    \draw[black,thick, ->] (3,8.7) -- (7,7.45);


.. question:: tcpto 
   :nb_pos: 1 
   :nb_prop: 3

   None of these two segments reaches the receiver. Which of the graphs below corresponds to a correct reaction of the TCP stack running on the sender ?

   .. negative:: 

      .. tikz::
         :libs: positioning, matrix, arrows 

         \colorlet{lightgray}{black!20}
         \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
         \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
         \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
         \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
         \node [black, fill=white] at (3,10) {Sender};
         \node [black, fill=white] at (7,10) {Receiver};
         \draw[very thick,->] (3,9.5) -- (3,0.5);
         \draw[very thick,->] (7,9.5) -- (7,0.5);
         % initial state       
         \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=8000 \\ 
         ssthresh=64000\\
         \end{tabular}\end{small}};    
         \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(2k)} -- (3,9);
         \draw[black,thick, ->] (3,9) -- (7,7.75);
         \draw[black,thick, ->] (3,8.7) -- (7,7.45);
         
         %timeout 
         \draw[blue, <->] (2,9) -- (2,4) node [midway, fill=white] {timeout};
                  
         \node [state] at (0,3) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=2000 \\ 
         ssthresh=32000\\
         \end{tabular}\end{small}};
         \draw[black,thick, ->] (3,4) -- (7,2.75);
         \draw[black,thick, ->] (3,3.75) -- (7,2.5);
         \draw[black,thick, ->] (7,2.75) -- (3,1.5);
         \draw[black,thick, ->] (7,2.5) -- (3,1.25);

      .. comment:: When the retransmission timer expires, the congestion window is reset to its initial value (1000 bytes here) and the slow-start threshold is set to half the value reached by the congestion window. 


   .. negative:: 

      .. tikz::
         :libs: positioning, matrix, arrows 

         \colorlet{lightgray}{black!20}
         \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
         \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
         \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
         \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
         \node [black, fill=white] at (3,10) {Sender};
         \node [black, fill=white] at (7,10) {Receiver};
         \draw[very thick,->] (3,9.5) -- (3,0.5);
         \draw[very thick,->] (7,9.5) -- (7,0.5);
         % initial state       
         \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=8000 \\ 
         ssthresh=64000\\
         \end{tabular}\end{small}};    
         \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(2k)} -- (3,9);
         \draw[black,thick, ->] (3,9) -- (7,7.75);
         \draw[black,thick, ->] (3,8.7) -- (7,7.45);
         
         %timeout 
         \draw[blue, <->] (2,9) -- (2,4) node [midway, fill=white] {timeout};
                  
         \node [state] at (0,3) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=2000 \\ 
         ssthresh=4000\\
         \end{tabular}\end{small}};
         \draw[black,thick, ->] (3,4) -- (7,2.75);
         \draw[black,thick, ->] (3,3.75) -- (7,2.5);
         \draw[black,thick, ->] (7,2.75) -- (3,1.5);
         \draw[black,thick, ->] (7,2.5) -- (3,1.25);

      .. comment:: When the retransmission timer expires, the congestion window is reset to its initial value (1000 bytes here) and the slow-start threshold is set to half the value reached by the congestion window. 


   .. negative:: 

      .. tikz::
         :libs: positioning, matrix, arrows 

         \colorlet{lightgray}{black!20}
         \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
         \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
         \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
         \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
         \node [black, fill=white] at (3,10) {Sender};
         \node [black, fill=white] at (7,10) {Receiver};
         \draw[very thick,->] (3,9.5) -- (3,0.5);
         \draw[very thick,->] (7,9.5) -- (7,0.5);
         % initial state       
         \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=8000 \\ 
         ssthresh=64000\\
         \end{tabular}\end{small}};    
         \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(2k)} -- (3,9);
         \draw[black,thick, ->] (3,9) -- (7,7.75);
         \draw[black,thick, ->] (3,8.7) -- (7,7.45);
         
         %timeout 
         \draw[blue, <->] (2,9) -- (2,4) node [midway, fill=white] {timeout};
                  
         \node [state] at (0,3) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=2000 \\ 
         ssthresh=2000\\
         \end{tabular}\end{small}};
         \draw[black,thick, ->] (3,4) -- (7,2.75);
         \draw[black,thick, ->] (3,3.75) -- (7,2.5);
         \draw[black,thick, ->] (7,2.75) -- (3,1.5);
         \draw[black,thick, ->] (7,2.5) -- (3,1.25);

      .. comment:: When the retransmission timer expires, the congestion window is reset to its initial value (1000 bytes here) and the slow-start threshold is set to half the value reached by the congestion window. 


   .. positive::

      .. tikz::
         :libs: positioning, matrix, arrows 

         \colorlet{lightgray}{black!20}
         \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
         \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
         \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
         \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
         \node [black, fill=white] at (3,10) {Sender};
         \node [black, fill=white] at (7,10) {Receiver};
         \draw[very thick,->] (3,9.5) -- (3,0.5);
         \draw[very thick,->] (7,9.5) -- (7,0.5);
         % initial state       
         \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=8000 \\ 
         ssthresh=64000\\
         \end{tabular}\end{small}};    
         \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(2k)} -- (3,9);
         \draw[black,thick, ->] (3,9) -- (7,7.75);
         \draw[black,thick, ->] (3,8.7) -- (7,7.45);
         
         %timeout 
         \draw[blue, <->] (2,9) -- (2,4) node [midway, fill=white] {timeout};
                  
         \node [state] at (0,3) {\begin{small}\begin{tabular}{l}
         rwin=64000 \\
         cwnd=1000 \\ 
         ssthresh=4000\\
         \end{tabular}\end{small}};
         \draw[black,thick, ->] (3,4) -- (7,2.75);
         \draw[black,thick, ->] (7,2.75) -- (3,1.5);
         \draw[black,thick, ->] (3,1.5) -- (7,0.25);
  


9. A TCP connection has been active for some time and has reached a congestion window of 4000 bytes. Four segments are sent, but the second (shown in red in the figure) is corrupted. 

 .. tikz::
    :libs: positioning, matrix, arrows 

    \colorlet{lightgray}{black!20}
    \tikzstyle{arrow} = [thick,->,>=stealth,font=\tiny]
    \draw[step=0.5cm,lightgray,very thin] (0,0) grid (10,10);
    \draw[very thick, <->] (9.7,10) -- (9.7,9.5) node [anchor=west, fill=white] {$20 msec$};
    \tikzset{state/.style={rectangle, dashed, draw, fill=white} }
    \node [black, fill=white] at (3,10) {Sender};
    \node [black, fill=white] at (7,10) {Receiver};
    \draw[very thick,->] (3,9.5) -- (3,0.5);
    \draw[very thick,->] (7,9.5) -- (7,0.5);
    % initial state       
    \node [state] at (0,11) {\begin{small}\begin{tabular}{l}
      rwin=64000 \\
      cwnd=4000 \\ 
      ssthresh=4000\\
     \end{tabular}\end{small}};
    
    \draw[red, ->] (0,9) node [anchor=north, fill=white] {send(10k)} -- (3,9);
    \draw[black,thick, ->] (3,9) -- (7,7.75);
    \draw[red,thick, dashed, ->] (3,8.7) -- (7,7.45);
    \draw[black,thick, ->] (3,8.4) -- (7,7.15);
    \draw[black,thick, ->] (3,8.1) -- (7,6.85);
    \draw[black,thick, ->] (7,7.75) -- (3,6.5);

    \draw[black,thick, ->] (7,7.15) -- (3,5.9);
    \draw[black,thick, ->] (7,6.855) -- (3,5.6);

.. question:: tcpfrr 
   :nb_pos: 1 
   :nb_prop: 3
 
   What is the new state of the TCP connection upon reception of the acknowledgements for the first, third and fourth segments ?

   .. positive:: 

      - Upon reception of the first acknowledgement, ``cwnd`` is set to 4250 bytes and ``ssthresh`` is unchanged 
      - Upon reception of the third acknowledgement, ``cwnd`` and ``ssthresh`` are unchanged 
      - Upon reception of the fourth acknowledgement, ``cwnd`` and ``ssthresh`` are unchanged

   .. negative::

      - Upon reception of the first acknowledgement, ``cwnd`` is set to 4250 bytes and ``ssthresh`` is unchanged 
      - Upon reception of the third acknowledgement, ``cwnd`` is set to 2225 bytes and ``ssthresh`` is set to 2000 bytes  
      - Upon reception of the fourth acknowledgement, ``cwnd`` and ``ssthresh`` are unchanged
 
      .. comment:: Given the initial values for ``cwnd`` and ``ssthresh``, this connection operates in congestion avoidance mode. The first acknowledgement increases the congestion window since it acknowledges new data. The third acknowledgement does not acknowledged new data. The congestion window cannot increase due to the reception of this acknowledgement. Furthermore, a single duplicate acknowledgement is not sufficient to detect a loss segment and trigger a fast retransmit.

   .. negative::


      - Upon reception of the first acknowledgement, ``cwnd`` is set to 5000 bytes and ``ssthresh`` is unchanged 
      - Upon reception of the third acknowledgement, ``cwnd`` is set to 6000 bytes and ``ssthresh`` is unchanged 
      - Upon reception of the fourth acknowledgement, ``cwnd`` is set to 7000 bytes and ``ssthresh`` is unchanged 

      .. comment:: Given the initial values for ``cwnd`` and ``ssthresh``, this connection operates in congestion avoidance mode. The first acknowledgement increases the congestion window since it acknowledges new data, but not the two others. 

   .. negative::

      - Upon reception of the first acknowledgement, ``cwnd`` is set to 4250 bytes and ``ssthresh`` is unchanged 
      - Upon reception of the third acknowledgement, ``cwnd`` is set to 4485 bytes and ``ssthresh`` is unchanged 
      - Upon reception of the fourth acknowledgement, ``cwnd`` is set to 4707 bytes and ``ssthresh`` is unchanged 

      .. comment:: Given the initial values for ``cwnd`` and ``ssthresh``, this connection operates in congestion avoidance mode. The first acknowledgement increases the congestion window since it acknowledges new data, but not the two others. 


10. Draw the complete time-sequence diagram for the scenario used in question 9.

.. include:: /../links.rst
