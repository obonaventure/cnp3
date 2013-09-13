.. Copyright |copy| 2013 by Olivier Bonaventure, Florentin Rochet, Justin Vellemans
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. raw:: html

  <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript" src="js/jquery-shuffle.js"></script>
  <script type="text/javascript" src="js/rst-form.js"></script>
  <script type="text/javascript">$nmbr_prop = 4</script>


Reliable data transfer
=======================


#. Framing problem - Bit stuffing.
----------------------------------

Consider a simple protocol that uses 16 bits frames. Bit stuffing can be used to recover the frames from a string of bits. The table below shows an original frame (before bit stuffing) and a transmitted frame (after having applied bit stuffing). Only one of the lines below corresponds to a valid utilisation of bit stuffing ((The frame boundary marker is 01111110). Which one ? 

   ===========================   =============================================
   Original frame                 Transmitted frame
   ===========================   =============================================

.. class:: positive


-  ================  ================================
   0001001010000110  01111110000100101000011001111110
   ================  ================================

-  ===============================  ========================================================
   1111110110111100110101101110101  01111110111110101101111000111111011010110111010101111110
   ===============================  ========================================================

.. class:: negative

-  ================ ================================
   0111111000101010 01111110011111100010101001111110
   ================ ================================
-  ================ ================
   0111111001111110 0111111001111110
   ================ ================
-  ================================================ =========================================================================
   011111100010101001111001010101011011011101010110 0111111001111101000101010011111100111100101010101011111101011011101010110
   ================================================ =========================================================================



#. Character stuffing
---------------------

Character stuffing is another framing technique. It uses the `DLE`, `STX` and `ETX` characters. The table blow shows original (before stuffing) and transmitted frames (after stuffing). Only one of the proposed answers is valid. Which one ? 

  ===========================   =============================================
   Original frame                 Transmitted frame
  ===========================   =============================================


.. class:: positive


-  =========================    =====================================================
   DLE STX 1 2 3 DLE DLE ETX    DLE STX DLE DLE STX 1 2 3 DLE DLE DLE DLE ETX DLE ETX
   =========================    =====================================================

-  ================  ================================================
   DLE DLE DLE DLE   DLE STX DLE DLE DLE DLE DLE DLE DLE DLE DLE ETX 
   ================  ================================================
.. class:: negative

-  =================== ===================================
   1 2 3 4 DLE DLE 7 8 STX 1 2 3 4 DLE DLE DLE DLE 7 8 ETX
   =================== ===================================
-  ================ =======================
   DLE STX DLE ETX  DLE STX DLE DLE ETX
   ================ =======================
-  =========================================== =========================================================================
   DLE A Z R STX DLE ETX ETX DLE 1 1 1 1 0 0 4 DLE STX DLE DLE A Z R DLE STX DLE DLE ETX ETX DLE 1 1 1 1 0 0 4 DLE ETX
   =========================================== =========================================================================


#. Error detection code
-----------------------

We considere here 16-bits blocs. For each sequence of 3 blocs, we compute parity bloc
where each parity bits of this bloc refer to the bits occupying the same position in the 3 previous blocs.
The parity bloc is therefore used to verify the integrity of the 3 previous
blocs, using XOR on the parity bloc received with the parity bloc rebuilded.

Which one of these parity blocs is correct ?

.. class:: positive
        
- 
  .. code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101010100001 => parity bloc
        

-
  .. code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        0100010101011110 => parity bloc
      
.. class:: negative

- 
  .. code-block::

        1010101011111001
        0101110110011011
        1010111011111010
        1111111111111111 => parity bloc

-
  .. code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101001011110 => parity bloc
  
- 
  .. code-block::

        1011101111&10111
        1001011101010101
        1010000011111111
        1010000011111111 => parity bloc


-
  .. code-block::
        
        1011101001100111
        1010101010010101
        1001010111111111
        1011101001100111 => parity bloc



Question 5. Error detection code (suite)
----------------------------------------
We consider here 16-bits blocs. For each sequence of 4 blocs, we compute parity
bloc where each parity bits of this bloc refer to the bits occupying the same
position in the previous blocs. The parity bloc is therefore used to verify the
integrity of the 4 previous block.
One of the 4 blocs has been lost. Can you find wich one using the three other
blocs and the parity bloc?
  
  .. code-block::
        
        1001011010100101
        0001000111001000
        0101001011101001
        ................ =>missing bloc
        1001100110011010 =>parity bloc

.. class:: positive

-
  .. code-block::

        0100110000011110

  .. code-block::

        1011001111100001

.. class:: negative

-
  .. code-block::

        1011001100011110

-
  .. code-block::
        
        0100110001100001
           
-
  .. code-block::
        
        1001011010100101

-
  .. code-block::
        
        0100111000011110

Question 6. The One Bit Protocol
--------------------------------------------
One timing diagram is displaying a correct transfert of 3 frames with the one bit protocol. Wich one?

.. class:: positive

-
  .. figure:: ../../png/lan/qcm1-1-solution1.png
     :align: center
     :scale: 100

-
  .. figure:: ../../png/lan/qcm1-1-solution2.png
     :align: center
     :scale: 100

-
  .. figure:: ../../png/lan/qcm1-1-solution3.png
     :align: center
     :scale: 100

.. class:: negative

-
  .. figure:: ../../png/lan/qcm1-1-wrong1.png
     :align: center
     :scale: 100

-
  .. figure:: ../../png/lan/qcm1-1-wrong2.png
     :align: center
     :scale: 100

-
  .. figure:: ../../png/lan/qcm1-1-wrong3.png
     :align: center
     :scale: 100

-
  .. figure:: ../../png/lan/qcm1-1-wrong4.png
     :align: center
     :scale: 100

Question 7. The One Bit Protocol (suite)
----------------------------------------
Observe the following time diagram. What's the next frame send by the sender?

  .. figure:: ../../png/lan/qcm1-7-nextstep.png
     :align: center
     :scale: 100
.. class:: positive

  .. figure:: ../../png/lan/qcm1-7-solution.png
     :align: center
     :scale: 100

.. class:: negative

  .. figure:: ../../png/lan/qcm1-7-wrong1.png
     :align: center
     :scale: 100

  .. figure:: ../../png/lan/qcm1-7-wrong2.png
     :align: center
     :scale: 100

  .. figure:: ../../png/lan/qcm1-7-wrong3.png
     :align: center
     :scale: 100
 
