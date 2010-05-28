==============================================
The datalink layer and the Local Area Networks
==============================================


The datalink layer is the lowest layer of the reference model that we discuss in details. As mentioned previously, there are two type of datalink layers. The first datalink layers that appeared are the ones that are used on point-to-point links between endsystems that are directly connected by a physical link. We will briefly discuss one of these datalink layers in this chapter. The second type of datalink layers are the ones used in Local Area Networks. The main difference between the point-to-point and the LAN datalink layers is that the latter need to regulate the access to the Local Area Network which is usually a shared medium. 
This chapter is organised as follows. We first discuss the principles and of datalink layer and the service that it uses from the physical layer. Then we describe in more details several Medium Access Control algorithms that are used by Local Area Networks to regulate the access to the shared medium. Finally we discuss in details several important datalink layer technologies with an emphasis on Ethernet.

.. include:: principles.rst

.. include:: technologies.rst




Summary
#######

In this chapter, we have first explained the principles of the datalink layer. We have considered two types of datalink layers : those used over point-to-point links and those used over Local Area Networks. On point-to-point links, the datalink layer must at least provide a framing technique, but some datalink layer protocols also include reliability mechanisms such as those used in the transport layer. We have described the Point-to-Point Protocol that is often used over point-to-point links in the Internet.

Local Area Networks pose a different problem since several devices share the same transmission channel. In this case, a Medium Access Control algorithm is necessary to regulate the access to the transmission channel since when two devices transmit at the same time a collision occur and none of their frames can be decoded by its recipient. There are two families of MAC algorithms. The statistical or optimistic MAC algorithms reduce the probability of collisions but do not prevent them. With such algorithms, when a collision occurs, the collided frames must be retransmitted. We have described the operation of the ALOHA, CSMA, CSMA/CD and CSMA/CA MAC algorithms. Deterministic or pessimistic MAC algorithms avoid all collisions. We have described the Token Ring MAC where stations exchange a token to regulate the access to the transmission channel.

Finally, we have described in more details two successful Local Area Network technologies : Ethernet and WiFi. Ethernet is now the de facto LAN technology. We have analysed the evolution of Ethernet including the operation of hubs and switches. We have also described the Spanning Tree Protocol that must be used when switches are interconnected. During the last years, WiFi became the de facto wireless technology at home and inside enterprises. We have explained the operation of WiFi networks and described the main 802.11 frames.


.. include:: ../links.rst


.. include:: exercises/ex-lan.rst



