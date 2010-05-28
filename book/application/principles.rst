Principles
##########

The are two important models to organise a networked application. The first and oldest model is the client-server model. In this model, a server provides services to clients that exchange information with it. This model is highly asymmetrical : clients send requests and servers perform actions and provide responses. It is illustrated in the figure below.


.. figure:: png/app-fig-001-c.png
   :align: center
   :scale: 50 

   The client-server model

The client-server model was the first model to be used to develop networked applications. This model comes naturally from the mainframes and minicomputers that were the only networked computers used until the 1980s. A minicomputer_ is a multi-user system that was used by tens or more users at the same time. Each user was interacting via the minicomputer by using a terminal. Those terminals, were mainly a screen, a keyboard and a cable connected to the minicomputer.

There are various types of servers and various types of clients. A web server provides information in response to the query sent by the client. A print server prints documents sent as queries by the client. An email server will forward towards their recipient the email messages sent as queries while a music server will deliver the music requested by the client. From the viewpoint of the application developer, the client and the server applications directly exchange messages (the horizontal arrows in the above figure), but in practice these messages are exchanged thanks to the underlying protocols (the vertical arrows in the above figure). In this chapter, we focus on these horizontal exchanges of messages. 

Networked applications do not exchange random messages. To ensure that the server is able to understand the queries sent by the client and that the client is able to understand the responses sent by the server, they must agree on a set of syntactical and semantic rules that define the format of the messages that they exchange and their ordering. This set of rules is called an application-level `protocol`.

An `application-level protocol` is similar to a structured conversation between humans. Assume that Alice wants to know the current time but does not have a watch. If Bob passes close by, the following conversation could take place :

 - Alice : `Hello`
 - Bob : `Hello`
 - Alice : `What time is it ?`
 - Bob : `11:55`
 - Alice : `Thank you`
 - Bob : `You're welcome`  

This conversation can succeed provided that both Alice and Bob speak the same language. If Alice meets Tchang who only speaks Chinese, she won't be able to ask him the current time. A conversation between humans can be more complex. For example, assume that Bob is a security guard who's duty is to only allow trusted secret agents to enter a meeting room. If all agents know a secret password, the conversation between Bob and Trudy could be as follows :

 - Bob : `What is the secret password ?`
 - Trudy : `1234`
 - Bob : `This is the correct password, you're welcome`
 
If Alice wants to enter the meeting room but does not know the password, her conversation could be as follows :

 - Bob : `What is the secret password ?`
 - Alice : `3.1415`
 - Bob : `This is not the correct password.`

Application-layer protocols can exchange two types of messages. Some protocols such as those used to support electronic mail exchange messages that are expressed as strings or lines of characters. As the transport layer allows hosts to exchange bytes, they need to agree on a common representation of the characters. The first and simplest method to encode characters is to use the :term:`ASCII` table. :rfc:`20` provides the ASCII table that is used by many protocols on the Internet. For example, the table defines the following binary representations :

 - `A` : `1000011b` 
 - `0` : `0110000b`
 - `z` : `1111010b`
 - `@` : `1000000b`
 - `space` : `0100000b`

In addition, the :term:`ASCII` table also defines several non-printable or control characters. These characters were designed to allow an application to control a printer or a terminal. The most common ones are `CR` and `LF` that are used to terminate a line or the `Bell` character that causes the terminal to emit a sound.

 - `carriage return` (`CR`) : `0001101b`
 - `line feed` (`LF`) : `0001010b`
 - `Bell`: `0000111b`

The :term:`ASCII` characters are encoded as a seven bits field, but transmitted as an eight-bits byte whose high order bit is set to `0`. Bytes are always transmitted starting from the high order or most significant bit.

Besides characters, some applications also need to exchange 16 bits and 32 bits fields such as IPv4 addresses. A naive solution would have been to send the 16- or 32-bits field as it was encoded in memory. Unfortunately, there are different methods to store 16- or 32-bits fields in memory. Some CPUs store the most significant byte of a 16-bits field in the first address of the field while others store the least significant byte at this location. When networked applications running on different CPUs exchange 16 bits fields, there are two possibilities to transfer them over the transport service :

  - send the most significant byte followed by the least significant byte
  - send the least significant byte followed by the most significant byte

The first possibility was named  `big-endian` in a note written by Cohen [Cohen1980]_ while the second was named `little-endian`. Vendors of CPUs that used `big-endian` in memory insisted on using `big-endian` encoding in networked applications while vendors of CPUs that used `little-endian` recommended the opposite. Several studies were written on the relative merits of each type of encoding, but the discussion became almost a religious issue [Cohen1980]_. Eventually, the Internet chose the `big-endian` encoding, i.e. multi-byte fields are always transmitted by sending the most significant byte first :rfc:`791` and refer to this encoding as the :term:`network-byte order`. Most libraries [#fhtonl]_ used to write networked applications contain functions to convert multibyte fields from memory to the network byte order and vice versa. 

Besides 16 and 32 bits words, some applications need to exchange that contain bit fields of various lengths. For example, a message may be composed of a 16 bits field followed by eight one bit flags, a 24 bits field and two 8 bits bytes. Internet protocol specifications will define such as message by using a representation such as the one below. In this representation, each line corresponds to 32 bits and the vertical lines are used to delineate fields. The numbers above the lines indicate the bit positions in the 32-bits word, with the high order bit at position `0`. 

::

    0                   1                   2                   3   
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |       First field  (16 bits)  |A|B|C|D|E|F|G|H|   Second      | 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |       field (24 bits)         |  First Byte   | Second Byte   |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   Message format

The message mentioned above will be transmitted starting from the upper 32-bits word in network byte order. The first field is encoded in 16 bits. It is followed by eight one bit flags (`A-H`), a 24 bits field whose high order byte is shown in the first line and the two low order bytes appear in the second line and two one byte fields. This ASCII representation is frequently used when defining binary protocols. We will use it for all the binary protocols that are discussed in this book.

We will discuss several examples of application-level protocols in this chapter.

.. introduce ipv4 and ipv6 addresses
.. mention names very early, they are important

.. The peer-to-peer model
.. ======================

.. The peer-to-peer model 
