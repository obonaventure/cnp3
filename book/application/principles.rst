.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

Principles
##########

The are two important models to organise a networked application. The first and oldest model is the client-server model. In this model, a server provides services to clients that exchange information with it. This model is highly asymmetrical : clients send requests and servers perform actions and return responses. It is illustrated in the figure below.


.. figure:: png/app-fig-001-c.png
   :align: center
   :scale: 50 

   The client-server model

The client-server model was the first model to be used to develop networked applications. This model comes naturally from the mainframes and minicomputers that were the only networked computers used until the 1980s. A minicomputer_ is a multi-user system that is used by tens or more users at the same time. Each user interacts with the minicomputer by using a terminal. Those terminals, were mainly a screen, a keyboard and a cable directly connected to the minicomputer.

There are various types of servers and various types of clients. A web server provides information in response to the query sent by its clients. A print server prints documents sent as queries by the client. An email server will forward towards their recipient the email messages sent as queries while a music server will deliver the music requested by the client. From the viewpoint of the application developer, the client and the server applications directly exchange messages (the horizontal arrows labelles `Queries` and `Responses` in the above figure), but in practice these messages are exchanged thanks to the underlying layers (the vertical arrows in the above figure). In this chapter, we focus on these horizontal exchanges of messages. 

Networked applications do not exchange random messages. To ensure that the server is able to understand the queries sent by a client and that the client is able to understand the responses sent by the server, they must agree on a set of syntactical and semantic rules. These rules define the format of the messages that they exchange and their ordering. This set of rules is called an application-level `protocol`.

An `application-level protocol` is similar to a structured conversation between humans. Assume that Alice wants to know the current time but does not have a watch. If Bob passes close by, the following conversation could take place :

 - Alice : `Hello`
 - Bob : `Hello`
 - Alice : `What time is it ?`
 - Bob : `11:55`
 - Alice : `Thank you`
 - Bob : `You're welcome`  

Such a conversation succeeds if both Alice and Bob speak the same language. If Alice meets Tchang who only speaks Chinese, she won't be able to ask him the current time. A conversation between humans can be more complex. For example, assume that Bob is a security guard whose duty is to only allow trusted secret agents to enter a meeting room. If all agents know a secret password, the conversation between Bob and Trudy could be as follows :

 - Bob : `What is the secret password ?`
 - Trudy : `1234`
 - Bob : `This is the correct password, you're welcome`
 
If Alice wants to enter the meeting room but does not know the password, her conversation could be as follows :

 - Bob : `What is the secret password ?`
 - Alice : `3.1415`
 - Bob : `This is not the correct password.`

Human conversations can be very formal, e.g. when soldiers communicate with their hierarchy, or informal such as when friends discuss. Computers that communicate are more akin to soldiers and require well-defined rules to ensure an successful exchange of information.  There are two types of rules that define how information can be exchanged between computers :

 - syntactical rules that precisely define the format of the messages that are exchanged. As computers only process bits, the syntactical rules specify how information is encoded as bit strings 
 - organisation of the information flow. For many applications, the flow of information must be structured and there are precedence relationships between the different types of information. In the time example above, Alice must greet Bob before asking for the current time. Alice would not ask for the current time first and greet Bob afterwards. Such precedence relationships exist in networked applications as well. For example, a server must receive a username and a valid password before accepting more complex commands from its clients.

Let us first discuss the syntactical rules. We will later explain how the information flow can be organised by analysing real networked applications.

Application-layer protocols exchange two types of messages. Some protocols such as those used to support electronic mail exchange messages that are expressed as strings or lines of characters. As the transport layer allows hosts to exchange bytes, they need to agree on a common representation of the characters. The first and simplest method to encode characters is to use the :term:`ASCII` table. :rfc:`20` provides the ASCII table that is used by many protocols on the Internet. For example, the table defines the following binary representations :

 - `A` : `1000011b` 
 - `0` : `0110000b`
 - `z` : `1111010b`
 - `@` : `1000000b`
 - `space` : `0100000b`

In addition, the :term:`ASCII` table also defines several non-printable or control characters. These characters were designed to allow an application to control a printer or a terminal. These control characters `CR` and `LF` that are used to terminate a line or the `Bell` character that causes the terminal to emit a sound.

 - `carriage return` (`CR`) : `0001101b`
 - `line feed` (`LF`) : `0001010b`
 - `Bell`: `0000111b`

The :term:`ASCII` characters are encoded as a seven bits field, but transmitted as an eight-bits byte whose high order bit is usually set to `0`. Bytes are always transmitted starting from the high order or most significant bit.

Most applications exchange strings that are composed of fixed or variable numbers of characters. A common solution to define the character strings that are acceptable is to define them as a grammar using a Backus-Naur Form (:term:`BNF`) such as the Augmented BNF defined in :rfc:`5234`. A BNF is a set of production rules that generate all valid character strings. For example, consider a networked application that uses two commands where the user can supply a username and a passwords. The BNF for this application could be defined them as follows ::

 command     	 = usercommand / passworcommand
 usercommand     = "user" SP username CRLF
 passwordcommand = "pass" SP password CRLF
 username	 = 1*8ALPHA
 password	 = (ALPHA) *(ALPHA/DIGIT)
 ALPHA           =  %x41-5A / %x61-7A   ; A-Z / a-z
 CR              =  %x0D  ; carriage return
 CRLF            =  CR LF ; Internet standard newline
 DIGIT    	 =  "0" / "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9"
 LF              =  %x0A  ; linefeed
 SP              =  %x20 / %x09 ; space or tabulation


The example above defines several terminals and two commands : `usercommand` and `passwordcommand`. The `ALPHA` terminal contains all letters in upper and lower case. The `CR` and `LF` terminals correspond to the carriage return and linefeed control characters. The `CRLF` rule concatenates these two terminals to match the standard end of line termination. The `DIGIT` terminal contains all digits. The `SP` terminal corresponds to the white space characters. The `usercommand` is composed of two strings separated a white space. In the ABNF rules that define the messages used by Internet applications, the commands are case-insentitive. The rule `"user"` corresponds to all possible cases of the letters that compose the word between brackets, e.g. `user`, `uSeR`, `USER`, `usER`, ... A `username` contains at least one letter and up to 8 letters. Usernames are case-sensitive  as they are not defined as a string between brackets. The `password` rule indicates that a password starts with a letter and can contain any number of letters or digits. The white space and the control characters cannot appear in a `password` defined by the above rule.

Besides character strings, some applications also need to exchange 16 bits and 32 bits fields such as integers. A naive solution would have been to send the 16- or 32-bits field as it is encoded in the host's memory. Unfortunately, there are different methods to store 16- or 32-bits fields in memory. Some CPUs store the most significant byte of a 16-bits field in the first address of the field while others store the least significant byte at this location. When networked applications running on different CPUs exchange 16 bits fields, there are two possibilities to transfer them over the transport service :

  - send the most significant byte followed by the least significant byte
  - send the least significant byte followed by the most significant byte

The first possibility was named  `big-endian` in a note written by Cohen [Cohen1980]_ while the second was named `little-endian`. Vendors of CPUs that used `big-endian` in memory insisted on using `big-endian` encoding in networked applications while vendors of CPUs that used `little-endian` recommended the opposite. Several studies were written on the relative merits of each type of encoding, but the discussion became almost a religious issue [Cohen1980]_. Eventually, the Internet chose the `big-endian` encoding, i.e. multi-byte fields are always transmitted by sending the most significant byte first :rfc:`791` and refers to this encoding as the :term:`network-byte order`. Most libraries [#fhtonl]_ used to write networked applications contain functions to convert multibyte fields from memory to the network byte order and vice versa. 

Besides 16 and 32 bits words, some applications need to exchange that contain bit fields of various lengths. For example, a message may be composed of a 16 bits field followed by eight one bit flags, a 24 bits field and two 8 bits bytes. Internet protocol specifications will define such as message by using a representation such as the one below. In this representation, each line corresponds to 32 bits and the vertical lines are used to delineate fields. The numbers above the lines indicate the bit positions in the 32-bits word, with the high order bit at position `0`. 

.. figure:: pkt/message.png
   :align: center
   :scale: 10 

   Message format

The message mentioned above will be transmitted starting from the upper 32-bits word in network byte order. The first field is encoded in 16 bits. It is followed by eight one bit flags (`A-H`), a 24 bits field whose high order byte is shown in the first line and the two low order bytes appear in the second line and two one byte fields. This ASCII representation is frequently used when defining binary protocols. We will use it for all the binary protocols that are discussed in this book.

We will discuss several examples of application-level protocols in this chapter.

.. introduce ipv4 and ipv6 addresses
.. mention names very early, they are important

.. index:: peer-to-peer

The peer-to-peer model
======================

The peer-to-peer model emerged during the last ten years as another possible architecture for networked applications. In the traditionnal client-server model, hosts act either as servers or as clients and a server serves a large number of clients. In the peer-to-peer model, all hosts act as both servers and clients and they play both roles. The peer-to-peer model has been used to develop various networked applications, ranging from Internet telephony to file sharing or Internet-wide filesystems. A detailed description of peer-to-peer applications may be found in [BYL2008]_. 


.. The peer-to-peer model 


.. rubric:: Footnotes

.. [#fhtonl] For example, the :manpage:`htonl(3)` (resp. :manpage:`ntohl(3)`) function the standard C library converts a 32-bits unsigned integer from the byte order used by the CPU to the network byte order (resp. from the network byte order to the CPU byte order). Similar functions exist in other programming languages.
