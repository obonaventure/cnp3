.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

*****************
Sharing resources
*****************

Multiple choice questions
=========================

:task_id: sharing

.. question:: ALOHA1
   :nb_prop: 3
   :nb_pos: 2

   1. Which of the following affirmations are valid for the ALOHA Medium Access Control scheme ? Select all the valid ones.

   .. positive:: The retransmission timer has a random part to prevent synchronisation among the communicating hosts.

   .. positive:: ALOHA uses acknowledgements to confirm the correct reception of frames.

   .. positive:: In ALOHA, a collision can occur when several hosts transmit almost at the same time.

   .. negative:: With ALOHA, a host always listens before transmitting its frame.

   .. negative:: When using ALOHA, a host always listens to the communication channel while transmitting to detect collisions.

   .. negative:: ALOHA only supports fixed-length frames.


.. question:: CSMA
   :nb_prop: 3
   :nb_pos: 2

   2. Which of the following affirmations are valid for the CSMA Medium Access Control scheme ? Select all the valid ones.

   .. positive:: With persistent CSMA, a host sends its frame as soon as the communication channel becomes free.

   .. positive:: With non-persistent CSMA, a host checks at random times whether the communication channel when it needs to transmit.

   .. positive:: With CSMA, collisions are detected thanks to the expiration of a retransmission timer.

   .. negative:: When using CSMA, a host always listens to the communication channel while transmitting to detect collisions

   .. negative:: With CSMA, acknowledgements are not needed since each host senses whether the communication channel is free before transmitting.


.. question:: CSMACD
   :nb_prop: 3
   :nb_pos: 2

   3. Which of the following affirmations are valid for CSMA/CD ? Select the correct ones.

   .. positive:: With CSMA/CD, there is no need to use acknowledgements to detect collisions.

   .. negative:: CSMA/CD relies on explicit acknowledgements to detect collisions.

      .. comment:: When using CSMA/CD, the absence of any detected collision is equivalent to an implicit acknowledgement.

   .. positive:: When using CSMA/CD, a host must check that the communication channel is free before transmitting data.

      .. comment:: This is the Carrier Sense part of the CSMA/CD algorithm.

   .. positive:: To be able to detect all collisions, CSMA/CD must enforce a minimum size for all transmitted frames.

   .. negative:: To be able to detect all collisions, CSMA/CD must enforce a maximum size for all transmitted frames.

      .. comment:: Most CSMA/CD deployments use a maximum frame size, but this is not required to detect collisions. This maximum frame size is usually defined to ensure fairness and prevent communicating hosts from using the communication channel forever.


.. question:: MAC
   :nb_prop: 4
   :nb_pos: 3

   4. Which of these Medium Access Control algorithms rely on explicit acknowledgements to detect collisions ? Select all the valid answers.

   .. positive:: ALOHA

   .. positive:: slotted ALOHA

   .. negative:: CSMA/CD

   .. positive:: CSMA

   .. positive:: CSMA/CA


.. question:: MinFrame
   :nb_prop: 3
   :nb_pos: 1 

   5. Consider a network that is using CSMA/CD. An important parameter in such networks is the minimum frame size. Which of the following affirmations is true ?
   .. positive:: If the shared medium has a bandwidth of 100 Mbps and a length of 10 kilometers, then the minimum frame size is 10000 bits.

   .. positive:: If the shared medium has a bandwidth of 10 Mbps and a length of 2 kilometers, then the minimum frame size is 200 bits.

   .. negative:: If the shared medium has a bandwidth of 100 Mbps and a length of 1 kilometer, then the minimum frame size is 10000 bits.


   .. negative:: The minimum frame size is always set to 512 bits or 64 bytes. 

      .. comment:: This is the minimum frame size for Ethernet networks using CSMA/CD at 10 Mbps, but this is only valid for this specific deployment.

   .. negative:: If the shared medium has a bandwidth of 100 Mbps and a length of 1 kilometer, then the minimum frame size is 500 bits.


.. question:: CSMACA
   :nb_prop: 3
   :nb_pos: 2

   6. CSMA/CA is a Medium Access Control scheme used in wireless networks. Only a few of the affirmations below concerning CSMA/CA are correct. Which ones ?

   .. positive:: CSMA/CA uses explicit acknowledgements to ensure that the frames are correctly received by their destination.

   .. positive:: CSMA/CA hosts must listen to the communication channel before transmitting.

   .. negative:: The CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) enables the hosts to prevent all collisions.

      .. comment:: Unfortunately not. It tries to prevent collisions, but cannot prevent all of them.

   .. negative:: A host using CSMA/CA can transmit its frame as soon as it detects that the communication channel is free.

      .. comment:: The backoff time introduces some randomness in the transmission of the frames to prevent synchronisation effects.

   .. positive:: When using RTS/CTS, four frames in total are required to exchange a single data frame.
 
 
