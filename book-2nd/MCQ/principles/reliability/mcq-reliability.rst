.. Copyright |copy| 2013 by Olivier Bonaventure, Florentin Rochet, Justin Vellemans
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. raw:: html

  <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript" src="js/jquery-shuffle.js"></script>
  <script type="text/javascript" src="js/rst-form.js"></script>
  <script type="text/javascript">$nmbr_prop = 4</script>


Reliable data transfer
=======================


1. Framing problem - Bit stuffing.
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



2. Character stuffing
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


3. Error detection code
-----------------------

For this question, we assume 16-bits blocks. For each sequence of 3 blocks, we compute a parity block where each parity bit of this block refer to the bits occupying the same position in the 3 previous blocks. The parity block can be used as an error detection scheme. 

Among the examples below, only one corresponds to a valid parity block. Which one (assuming that the parity block has been computed by using XOR of the corresponding bits) ?

.. class:: positive
        
- 
  .. code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101010100001 => parity block
        

-
  .. code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        0100010101011110 => parity block
      
.. class:: negative

- 
  .. code-block::

        1010101011111001
        0101110110011011
        1010111011111010
        1111111111111111 => parity block

-
  .. code-block::
        
        1010111011110101
        1110101010101011 
        1111111011111111  
        1011101001011110 => parity block
  
- 
  .. code-block::

        1011101111&10111
        1001011101010101
        1010000011111111
        1010000011111111 => parity block


-
  .. code-block::
        
        1011101001100111
        1010101010010101
        1001010111111111
        1011101001100111 => parity block



4. Error correction codes
-------------------------

Parity blocks can also be used to recover from transmission errors. For this question, we assume that one parity block has been computed for 4 blocks and one of the block was discarded due to transmission errors. 
  
  .. code-block:: text
        
        1001011010100101
        0001000111001000
        0101001011101001
        ................ =>missing block
        1001100110011010 =>parity block


Only one of the blocks below is a recovered block. Which one ?

.. class:: positive

-
  .. code-block::

        0100110000011110

-
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


5. Alternating Bit Protocol
---------------------------

One timing diagram is displaying a correct transfert of 3 frames with the one bit protocol. Wich one?

.. class:: positive

-
  .. figure:: images/qcm1-1-solution1.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-1-solution2.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-1-solution3.png
     :align: center
     :scale: 100

.. class:: negative

-
  .. figure:: images/qcm1-1-wrong1.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-1-wrong2.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-1-wrong3.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-1-wrong4.png
     :align: center
     :scale: 100


6. Alternating Bit Protocol
---------------------------
Observe the following time diagram. What's the next frame send by the sender?

  .. figure:: images/qcm1-7-nextstep.png
     :align: center
     :scale: 100

.. class:: positive

-
  .. figure:: images/qcm1-7-solution.png
     :align: center
     :scale: 100

.. class:: negative

- 
  .. figure:: images/qcm1-7-wrong1.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-7-wrong2.png
     :align: center
     :scale: 100

-
  .. figure:: images/qcm1-7-wrong3.png
     :align: center
     :scale: 100
 
