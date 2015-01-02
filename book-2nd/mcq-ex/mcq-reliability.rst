.. Copyright |copy| 2013, 2014 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. _mcq-reliable:

*****************
Reliable transfer
*****************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 


:task_id: reliable

Framing techniques
------------------

.. question:: bitstuffing
   :nb_prop: 3 
   :nb_pos: 1 


   1. *Bit stuffing*. Consider a simple protocol that uses 16 bits frames. Bit stuffing can be used to recover the frames from a string of bits. The table below shows an original frame (before bit stuffing) and a transmitted frame (after having applied bit stuffing). Only one of the lines below corresponds to a valid utilisation of bit stuffing (the frame boundary marker is 01111110). Which one ? 

   .. positive::
     
     ================  ================================
     Before stuffing   After stuffing
     ================  ================================
     0001001010000110  01111110000100101000011001111110
     ================  ================================

   .. positive::

     ===============================  ========================================================
     Before stuffing                  After stuffing
     ===============================  ========================================================
     1111110110111100110101101110101  01111110111110101101111000111111011010110111010101111110
     ===============================  ========================================================

   .. negative::

     ================ ================================
     Before stuffing  After stuffing
     ================ ================================
     0111111000101010 01111110011111100010101001111110
     ================ ================================

   .. negative::

     ================ ================
     Before stuffing   After stuffing
     ================ ================
     0111111001111110 0111111001111110
     ================ ================

   .. negative::

     ================================================ =========================================================================
     Before stuffing                                  After stuffing
     ================================================ =========================================================================
     011111100010101001111001010101011011011101010110 0111111001111101000101010011111100111100101010101011111101011011101010110
     ================================================ =========================================================================







.. question:: charstuffing
   :nb_prop: 3 
   :nb_pos: 1 


   2. *Character stuffing* is another framing technique. It uses the `DLE`, `STX` and `ETX` characters. The table below shows original (before stuffing) and transmitted frames (after stuffing). Only one of the proposed answers is valid. Which one ? 


   .. positive::

     =========================    =====================================================
     Before stuffing              After stuffing
     =========================    =====================================================
     DLE STX 1 2 3 DLE DLE ETX    DLE STX DLE DLE STX 1 2 3 DLE DLE DLE DLE ETX DLE ETX
     =========================    =====================================================

   .. positive::

     ================  ================================================
     Before stuffing   After stuffing
     ================  ================================================
     DLE DLE DLE DLE   DLE STX DLE DLE DLE DLE DLE DLE DLE DLE DLE ETX 
     ================  ================================================

   .. negative::

     =================== ===================================
     Before stuffing     After stuffing
     =================== ===================================
     1 2 3 4 DLE DLE 7 8 STX 1 2 3 4 DLE DLE DLE DLE 7 8 ETX
     =================== ===================================

   .. negative::

     ================ =======================
     Before stuffing  After stuffing
     ================ =======================
     DLE STX DLE ETX  DLE STX DLE DLE ETX
     ================ =======================

   .. negative::

     =========================================== =========================================================================
     Before stuffing                             After stuffing
     =========================================== =========================================================================
     DLE A Z R STX DLE ETX ETX DLE 1 1 1 1 0 0 4 DLE STX DLE DLE A Z R DLE STX DLE DLE ETX ETX DLE 1 1 1 1 0 0 4 DLE ETX
     =========================================== =========================================================================


Error detection and correction
------------------------------

.. question:: errodetection
   :nb_prop: 3 
   :nb_pos: 1 

   1. For this question, we assume 16-bits blocks. For each sequence of 3 blocks, we compute a parity block where each parity bit of this block refers to the bits occupying the same position in the 3 previous blocks. The parity block can then be used as an error detection scheme. 

   Among the examples below, only one corresponds to a valid even parity block. Which one ?

   .. positive::
        
    .. code-block:: text
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101010100001 => parity block
        
   .. negative::

    .. code-block:: text
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        0100010101011110 => parity block
      
      .. comment:: This is an odd parity block

   .. negative::

    .. code-block:: text

        1010101011111001
        0101110110011011
        1010111011111010
        1111111111111111 => parity block


   .. negative::

    .. code-block:: text
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101001011110 => parity block
  
   .. negative::
 
    .. code-block:: text

        1011101111&10111
        1001011101010101
        1010000011111111
        1010000011111111 => parity block


   .. negative::

    .. code-block:: text
        
        1011101001100111
        1010101010010101
        1001010111111111
        1011101001100111 => parity block


.. question:: errorcorrection
   :nb_prop: 3 
   :nb_pos: 1 

   2. Parity blocks can also be used to recover from transmission errors. For this question, we assume that one parity block has been computed for 4 blocks and one of the block was discarded due to transmission errors. 
  
   .. code-block:: text
        
        1001011010100101
        0001000111001000
        0101001011101001
        ................ =>missing block
        1001100110011010 =>parity block


   Only one of the blocks below is a recovered block. Which one ?

   .. positive::

      .. code-block:: text
     
        0100110000011110

   .. positive::
 
      .. code-block:: text

        1011001111100001


   .. negative::

      .. code-block:: text
     
        1011001100011110

   .. negative::
     
      .. code-block:: text
        
        0100110001100001

   .. negative::     
          
      .. code-block:: text
        
        1001011010100101

   .. negative::     

      .. code-block:: text
        
        0100111000011110


Alternating Bit Protocol
------------------------
.. question:: abp0 
   :nb_prop: 3           
   :nb_pos: 2 


   1. After having correctly transmitted several frames, a host sends a data frame that is correctly acknowledged. This corresponds to the situation shown in the figure below :

     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(x)\nstart timer" ] ,
        b>>c [ label = "D(1,x)", arcskip="1"];
        c=>d [ label = "DATA.ind(x)" ];
        c>>b [label= "C(OK1)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];


   At this stage, which of the following affirmations are correct (select all of them) ?


   .. positive::  If the right host receives `D(1,y)`, it will ignore the frame and reply with `C(OK1)`.  

   .. positive::  If the left host receives `C(OK,0)`, it will retransmit the frame `D(1,y)`. 

   .. negative::  If the right host receives `D(1,y)`, it will ignore the frame and reply with `C(OK0)`. 

   .. negative::  If the right host receives `D(0,y)`, it will ignore the frame and reply with `C(OK1)`. 

   .. positive::  If the right host receives `D(0,y)`, it will accept the frame and reply with `C(OK0)`. 


.. question:: abp1
   :nb_prop: 3           
   :nb_pos: 1


   2. Consider a host on the left that needs to transmit 2 bytes of data to the host on right. Among the following time sequence diagrams, which is the one that corresponds to a successful transmission of these two bytes ?

   .. positive::

     .. comment::
        
        This example is correct. It could correspond to a scenario where the host on the left sent some data until it reached sequence number 0 and then become idle before sending data `y`.
 
     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(x)\nstart timer" ] ,
        b>>c [ label = "D(1,x)", arcskip="1"];
        c=>d [ label = "DATA.ind(x)" ];
        c>>b [label= "C(OK1)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(y)\nstart timer" ] ,
        b>>c [ label = "D(0,y)", arcskip="1"];
        c=>d [ label = "DATA.ind(y)" ];
        c>>b [label= "C(OK0)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];


   .. negative::

     .. comment::
        
        This scenario is incorrect. The same sequence number is used incorrectly to send `x` and `y`.

     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(x)\nstart timer" ] ,
        b>>c [ label = "D(1,x)", arcskip="1"];
        c=>d [ label = "DATA.ind(x)" ];
        c>>b [label= "C(OK1)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(y)\nstart timer" ] ,
        b>>c [ label = "D(1,y)", arcskip="1"];
        c>>b [label= "C(OK1)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];

   .. negative::

     .. comment::

        This scenario is incorrect. The host on the right should not send `C(OK1)` after having received `D(0,x)`

     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(x)\nstart timer" ] ,
        b>>c [ label = "D(0,x)", arcskip="1"];
        c=>d [ label = "DATA.ind(x)" ];
        c>>b [label= "C(OK1)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(y)\nstart timer" ] ,
        b>>c [ label = "D(1,y)", arcskip="1"];
        c=>d [ label = "DATA.ind(y)" ];
        c>>b [label= "C(OK0)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];


.. question:: abp2
   :nb_prop: 3
   :nb_pos: 1


   3. Sometimes, a host needs to send the same information twice. Consider a host that sends `d` followed by `d`. What is the correct time sequence diagram for this scenario ? 


   .. positive::

     .. comment::
        
        This example is correct. 
 
     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(0,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK0)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(1,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK1)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];

   .. positive::

     .. comment::
        
        This example is correct. 
 
     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(1,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK1)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(0,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK0)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];


   .. negative::

     .. comment::
        
        This example is incorrect. The second frame is a retransmission for the host on the right since it carries the same sequence number. It should never delivery the data to its user.
 
     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(1,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK1)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(1,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK1)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];

   .. negative::

     .. comment::
        
        This example is incorrect. The second frame is a retransmission for the host on the right since it carries the same sequence number. It should never delivery the data to its user.
 
     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(0,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK0)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(0,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK0)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];

   .. negative::

     .. comment::
        
        This example is incorrect. The acknowledgements sent by the host on the right are incorrect. When receiving `D(1,d)` and accepting it since it issues a `Data.ind(d)`, it should not send `C(OK0)` but instead `C(OK1)`.
 
     .. msc::

        a [label="", linecolour=white],
        b [label="Host A", linecolour=black],
        z [label="", linecolour=white],
        c [label="Host B", linecolour=black],
        d [label="", linecolour=white];
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(1,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK0)", arcskip="1"];
        b->a [linecolour=white, label="cancel timer"];
        |||;
        a=>b [ label = "DATA.req(d)\nstart timer" ] ,
        b>>c [ label = "D(0,d)", arcskip="1"];
        c=>d [ label = "DATA.ind(d)" ];
        c>>b [label= "C(OK1)", arcskip="1"]; 
        b->a [linecolour=white, label="cancel timer"];





Go-back-N
---------


.. question:: gbn0
                 

   1. The diagram below shows the operation of a go-back-n protocol.      

      .. tikz:: 

                % vertical lines 
                \draw (4,0) -- (4,-8);
                \draw (7,0) -- (7,-8);
                %window of 3 
                % data request 
                \draw [->] (1,0) --  node [above] {Data.req(abcd)} (3.9,0);
                %
                % data indication 
                \draw [->] (7,-2) --  node [above] {Data.ind(a)} (10,-2);
                \draw [->, thick] (7,-2) -- (4.1,-4);
                \node at (3,-4) (cok0) [color=red] {C(OK,0)};
                \draw [->] (7,-3) --  node [above] {Data.ind(b)} (10,-3);
                %
                \draw [->, thick] (7,-3) -- (4.1,-5) ;
                \node at (3,-5) (cok1) [color=red] {C(OK,1)};
                %
                \draw [->] (7,-4) --  node [above] {Data.ind(c)} (10,-4);
                %
                \draw [->, thick] (7,-4) -- (4.1,-6);
                \node at (3,-6) (cok2) [color=red] {C(OK,2)};
                %
                \draw [->] (7,-6) --  node [above] {Data.ind(d)} (10,-6);
                \draw [->, thick] (7,-6) -- (4.1,-8);
                \node at (3,-8) (cok2) [color=red] {C(OK,3)};
                %data at the end
                \draw [->, thick] (4.1,0) -- (6.9,-2) node [midway, sloped, fill=white] {D(0,a)};
                \draw [->, thick] (4.1,-1) -- (6.9,-3) node [midway, sloped, fill=white] {D(1,b)};
                \draw [->, thick] (4.1,-2) -- (6.9,-4) node [midway, sloped, fill=white] {D(2,c)};
                \draw [->, thick] (4.1,-4) -- (6.9,-6) node [midway, sloped, fill=white] {D(3,d)};        
                
   What is the size of the window (measured in frames) ?

   .. positive:: 3

      .. comment:: Correct

   .. negative:: 2

      .. comment:: With a window of two frames, the sending host would have to wait for the acknowledgements after having sent the second frame.  This is not the case in the diagram.

   .. negative:: 1

      .. comment:: With a window of one frame, the sending host would have to wait for the acknowledgements after having sent the first frame. This is not the case in the diagram.

   .. negative:: We cannot know from this diagram.
             



.. question:: gbn2 

   2. You implement a Go-back-n sender and observe the following frames that you send/receive. Assume that you use a window of three frames. 


      .. tikz:: 

                % vertical lines 
                \draw (4,0) -- (4,-8);
                %window of 3 
                % data request 
                \draw [->] (1,0) --  node [above] {Data.req(abc)} (3.9,0);
                %
                \draw [->, thick] (7,-2) -- (4.1,-4);
                \node at (3,-4) (cok0) [color=red] {C(OK,0)};
                \draw [->, thick] (7,-4) -- (4.1,-6);
                \node at (3,-6) (cok2) [color=red] {C(OK,1)};
                %data at the end 
                \draw [->, thick] (4.1,0) -- (6.9,-2) node [midway, sloped, fill=white] {D(0,a)};
                \draw [->, thick] (4.1,-1) -- (6.9,-3) node [midway, sloped, fill=white] {D(1,b)};
                \draw [->, thick] (4.1,-2) -- (6.9,-4) node [midway, sloped, fill=white] {D(2,c)};


   Which affirmation is correct among the ones below :

   .. negative:: The receiver has correctly received the three frames that you have sent, but one acknowledgement has been lost. 

      .. comment:: If this was the case, then you would have received `C(OK,2)` as the last acknowledgement. 

   .. negative:: The receiver has only received the first frame that you have sent. It has neither received the second nor the third frame. 

      .. comment:: In this case, then the receiver should have never sent a second acknowledgement since it only sends acknowledgements when receiving data frames. 

   .. negative:: The receiver has correctly received the first and the third frame that your have sent. The second frame has been lost and should be retransmitted. 

   .. positive:: 

      The receiver has correctly received the first two frames. The third frame and the second acknowledgements have been lost. 


.. question:: gbn3 
   :nb_prop: 3 
   :nb_pos: 1 


   3. You implement a Go-back-n sender and observe the following sequence of frames. Assuming that you have a window of three segments. 
     
      .. tikz:: 

                % vertical lines 
                \draw (4,0) -- (4,-8);
                %window of 3 
                % data request 
                \draw [->] (1,0) --  node [above] {Data.req(abcd)} (3.9,0);
                \draw [->, thick] (7,-3) -- (4.1,-5) ;
                \node at (3,-5) (cok1) [color=red] {C(OK,1)};
                %data at the end 
                \draw [->, thick] (4.1,0) -- (6.9,-2) node [midway, sloped, fill=white] {D(0,a)};
                \draw [->, thick] (4.1,-1) -- (6.9,-3) node [midway, sloped, fill=white] {D(1,b)};
                \draw [->, thick] (4.1,-2) -- (6.9,-4) node [midway, sloped, fill=white] {D(2,c)};


   Among the following affirmations, only one is correct. Which one ?

   .. positive:: After having received `C(OK,1)`, you know that the first two frames have been received correctly. Since you never received an acknowledgement for the third frame, you will retransmit it after the expiration of the associated retransmission timer. 

   .. negative:: The first three frames have been received correctly. Upon reception of `C(OK,1)`, you can immediately transmit the next data frame, i.e. `D(3,d)`. 

      .. comment:: If the first three frames would have been received correctly, you would have received `C(OK,2)`. When you receive `C(OK,2)`, you only know that the first two frames have been received correctly. 

   .. negative:: After having received `C(OK,1)`, you know that the first two frames have been received correctly. You retransmit immediately the frame `D(2,c)` that has not been received correctly. 

      .. comment:: You cannot immediately infer than the third frame (or the corresponding acknowledgement) has been lost. You will retransmit `D(2,c)` only after the expiration of the retransmission timer.         

   .. negative:: Since you never received `C(OK,0)`, there was something wrong in the transmission of the first frame. You retransmit all frames upon expiration of your retransmission timer. 

      .. comment:: Since you received `C(OK,1)`, you *know* that the first two frames have been received correctly. 

   .. negative:: Since you never received `C(OK,0)`, there was something wrong in the transmission of the first frame. You retransmit this frame immediately after having received `C(OK,1)`. 

      .. comment:: Since you received `C(OK,1)`, you *know* that the first two frames have been received correctly. 


.. question:: gbn4 

   4. You implement a go-back-n receiver and receive the following frames. 


      .. tikz:: 

                % vertical lines 
                \draw (7,0) -- (7,-8);
                % data indication 
                \draw [->] (7,-2) --  node [above] {Data.ind(a)} (10,-2);
                \draw [->, thick] (7,-2) -- (4.1,-4);
                \node at (3,-4) (cok0) [color=red] {C(OK,0)};
                %data at the end 
                \draw [->, thick] (4.1,0) -- (6.9,-2) node [midway, sloped, fill=white] {D(0,a)};
                \draw [->, thick] (4.1,-2) -- (6.9,-4) node [midway, sloped, fill=white] {D(2,b)};

   How do you respond to the reception of the frame `D(2,b)` ?

   .. positive:: You ignore the out-of-sequence frame and respond with `C(OK,0)`. 

   .. negative:: You place the frame in your buffer and respond with `C(OK,2)`. 

      .. comment:: Since the frame is out-of-sequence, a go-back-n receiver would ignore it. Furthermore, sending `C(OK,2)` indicates that all frames, up to and including sequence number `2` have been received in sequence.           

   .. negative:: You issue a `Data.ind(b)` to deliver the information to your user and respond with `C(OK,2)`. 

      .. comment:: The frame is out of sequence. It cannot be delivered to the user. Furthermore, sending `C(OK,2)` indicates that all frames, up to and including sequence number `2` have been received in sequence.                     

   .. negative:: You ignore the out-of-sequence frame and do not respond. 

      .. comment:: As a go-back-n receiver, you should respond with an acknowledgement to each received frame. 

   .. negative:: You ignore the out-of-sequence frame and respond with `C(OK,1)`. 

      .. comment:: By sending `C(OK,1)`, you indicate that the second frame has been received correctly, which is not the case. 

                         


Selective repeat
----------------



.. question:: sr2 

   1. You implement a Selective-repeat sender and observe the following frames that you send/receive. Assume that you use a window of three frames. 


      .. tikz:: 

                % vertical lines 
                \draw (4,0) -- (4,-8);
                %window of 3 
                % data request 
                \draw [->] (1,0) --  node [above] {Data.req(abc)} (3.9,0);
                %
                \draw [->, thick] (7,-2) -- (4.1,-4);
                \node at (3,-4) (cok0) [color=red] {C(OK,1)};
                \draw [->, thick] (7,-4) -- (4.1,-6);
                \node at (3,-6) (cok2) [color=red] {C(OK,2)};
                %data at the end 
                \draw [->, thick] (4.1,0) -- (6.9,-2) node [midway, sloped, fill=white] {D(1,a)};
                \draw [->, thick] (4.1,-1) -- (6.9,-3) node [midway, sloped, fill=white] {D(2,b)};
                \draw [->, thick] (4.1,-2) -- (6.9,-4) node [midway, sloped, fill=white] {D(3,c)};


   Which affirmation is correct among the ones below :

   .. negative::

       The receiver has correctly received the three frames that you have sent, but one acknowledgement has been lost. No retransmission is needed.

       .. comment:: If this was the case, then you would have received `C(OK,3)` as the last acknowledgement. 

   .. negative::

       The receiver has only received the first frame that you have sent. It has neither received the second nor the third frame. You plan to retransmit only the second frame.

       .. comment:: In this case, then the receiver should have never sent a second acknowledgement since it only sends acknowledgements when receiving data frames. 

   .. negative::

       The frames containing `a` and `c` have been received correctly. The second frame (containing `b`) has not been received. 

   .. positive:: 

       The frames containing `a` and `b` have been received correctly. The third frame (containing `c`) has not been received.



.. question:: sr4

   2. You implement a selective repeat receiver and receive the following frames. 


      .. tikz:: 

                % vertical lines 
                \draw (7,0) -- (7,-8);
                % data indication 
                \draw [->] (7,-2) --  node [above] {Data.ind(a)} (10,-2);
                \draw [->, thick] (7,-2) -- (4.1,-4);
                \node at (3,-4) (cok0) [color=red] {C(OK,1)};
                %data at the end 
                \draw [->, thick] (4.1,0) -- (6.9,-2) node [midway, sloped, fill=white] {D(1,a)};
                \draw [->, thick] (4.1,-2) -- (6.9,-4) node [midway, sloped, fill=white] {D(3,b)};

   How do you respond to the reception of the frame `D(3,b)` ?

   .. negative:: You ignore the out-of-sequence frame and respond with `C(OK,1)`. 

      .. comment:: A selective repeat receiver should store the out-of-sequence frames inside its receive buffer.

   .. negative:: You place the frame in your buffer and respond with `C(OK,3)`. 

      .. comment:: Placing the out-of-sequence frame inside the buffer is correct. Unfortunately, sending `C(OK,3)` indicates that all frames, up to and including sequence number `3` have been received in sequence.           

   .. positive:: You place the frame in your buffer and respond with `C(OK,1)`. 

      .. comment:: Placing the out-of-sequence frame inside the buffer is correct. 

   .. negative:: You issue a `Data.ind(b)` to deliver the information to your user and respond with `C(OK,2)`. 

      .. comment:: The frame is out of sequence. It cannot be delivered to the user. Furthermore, sending `C(OK,2)` indicates that all frames, up to and including sequence number `2` have been received in sequence.                     

   .. negative:: You ignore the out-of-sequence frame and do not respond. 

      .. comment:: As a selective repeat receiver, you should respond with an acknowledgement to each received frame and store the out-of-sequence frames that you receive.

   .. negative:: You ignore the out-of-sequence frame and respond with `C(OK,2)`. 

      .. comment:: By sending `C(OK,1)`, you indicate that the second frame has been received correctly, which is not the case. As a selective repeat receiver, you should respond with an acknowledgement to each received frame and store the out-of-sequence frames that you receive.

                




.. include:: /links.rst
