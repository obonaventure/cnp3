.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Principios
##########

.. The are two important models used to organise a networked application. The first and oldest model is the client-server model. In this model, a server provides services to clients that exchange information with it. This model is highly asymmetrical : clients send requests and servers perform actions and return responses. It is illustrated in the figure below.

Existen dos modelos importantes que se utilizan para organizar una aplicación de red. El primero y más antiguo es el `modelo cliente-servidor`. En este modelo, un servidor ofrece servicios a clientes que intercambian información con él. Este modelo es altamente asimétrico: los clientes envían requerimientos (`requests`) y los servidores ejecutan acciones y devuelven respuestas (`responses`). Se ilustra en la figura más abajo.


.. figure:: png/app-fig-001-c.png
   :align: center
   :scale: 50 

   El modelo cliente-servidor
..   The client-server model

.. The client-server model was the first model to be used to develop networked applications. This model comes naturally from the mainframes and minicomputers that were the only networked computers used until the 1980s. A minicomputer_ is a multi-user system that is used by tens or more users at the same time. Each user interacts with the minicomputer by using a terminal. Those terminals, were mainly a screen, a keyboard and a cable directly connected to the minicomputer.

El modelo cliente-servidor fue el primero en ser usado para desarrollar aplicaciones de red. Este modelo surge naturalmente de los mainframes o minicomputadoras, que fueron las únicas computadoras usadas en red hasta los años 80. Un minicomputador (minicomputer_) es un sistema multiusuario que es usado por decenas de usuarios al mismo tiempo. Cada usuario interactúa con el minicomputador usando un terminal. Estos terminales eran básicamente una pantalla, un teclado y un cable conectado directamente al minicomputador.

.. There are various types of servers as well as various types of clients. A web server provides information in response to the query sent by its clients. A print server prints documents sent as queries by the client. An email server will forward towards their recipient the email messages sent as queries while a music server will deliver the music requested by the client. From the viewpoint of the application developer, the client and the server applications directly exchange messages (the horizontal arrows labelled `Queries` and `Responses` in the above figure), but in practice these messages are exchanged thanks to the underlying layers (the vertical arrows in the above figure). In this chapter, we focus on these horizontal exchanges of messages. 

Existen varios tipos de servidores, así como varios tipos de clientes. Un servidor de web provee información en respuesta a la consulta enviada por sus clientes. Un servidor de impresión imprime documentos enviados como requerimiento por el cliente. Un servidor de correo electrónico reenvía a sus destinatarios los mensajes de email enviados como requerimientos, mientras que un servidor de música ofrecerá la música requerida por el cliente. Desde el punto de vista del desarrollador de aplicaciones, las aplicaciones cliente y servidor intercambian directamente mensajes (las flechas horizontales rotuladas `Requerimientos`, o `Queries`, y `respuestas`, o `Responses`, en la figura anterior). En este capítulo nos concentraremos en los intercambios horizontales de mensajes.

.. Networked applications do not exchange random messages. In order to ensure that the server is able to understand the queries sent by a client, and also that the client is able to understand the responses sent by the server, they must both agree on a set of syntactical and semantic rules. These rules define the format of the messages exchanged as well as their ordering. This set of rules is called an application-level `protocol`.

Las aplicaciones de redes no intercambian mensajes al azar. Para asegurar que el servidor sea capaz de comprender los requerimientos emitidos por un cliente, y a la vez, de que el cliente sea capaz de comprender las respuestas emitidas por el servidor, ambos deben estar de acuerdo en un conjunto de reglas sintácticas y semánticas. Estas reglas definen el formato de los mensajes intercambiados, así como su ordenamiento. A este conjunto de reglas se lo llama `protocolo de nivel de Aplicación`.

.. An `application-level protocol` is similar to a structured conversation between humans. Assume that Alice wants to know the current time but does not have a watch. If Bob passes close by, the following conversation could take place :

.. - Alice : `Hello`
.. - Bob : `Hello`
.. - Alice : `What time is it ?`
.. - Bob : `11:55`
.. - Alice : `Thank you`
.. - Bob : `You're welcome`  

Un `protocolo de nivel de Aplicación` es similar a una conversación estructurada entre humanos. Supongamos que Alice  [#faliceandbob]_ quiere saber qué hora es, pero no dispone de un reloj. Si se encuentra con Bob, podría darse la siguiente conversación:

 - Alice: `¡Hola!`
 - Bob: `¡Hola!`
 - Alice: `¿Qué hora es?`
 - Bob: `Las 11:55.`
 - Alice: `Gracias.`
 - Bob: `Por nada.`

.. Such a conversation succeeds if both Alice and Bob speak the same language. If Alice meets Tchang who only speaks Chinese, she won't be able to ask him the current time. A conversation between humans can be more complex. For example, assume that Bob is a security guard whose duty is to only allow trusted secret agents to enter a meeting room. If all agents know a secret password, the conversation between Bob and Trudy could be as follows :

.. - Bob : `What is the secret password ?`
.. - Trudy : `1234`
.. - Bob : `This is the correct password, you're welcome`
 
Esta conversación será exitosa sólo si Alice y Bob hablan el mismo idioma. Si Alice se encuentra con Chang, quien sólo habla chino, no podrá preguntarle la hora. Una conversación entre humanos puede ser más compleja. Por ejemplo, supongamos que Bob es un guardia de seguridad cuya obligación es permitir la entrada a una sala de reuniones sólo a los agentes secretos en quienes confíe. Si todos los agentes conocen una clave secreta o contraseña (`password`), la conversación entre Bob y Alice podría ser como sigue:

 - Bob: `¿Cuál es la contraseña?`
 - Alice: `"1234".`
 - Bob: `Es la contraseña correcta, adelante.`

.. If Alice wants to enter the meeting room but does not know the password, her conversation could be as follows :

.. - Bob : `What is the secret password ?`
.. - Alice : `3.1415`
.. - Bob : `This is not the correct password.`

Si Trudy quisiera entrar a la sala de reuniones pero no supiera la contraseña, su conversación podría haber sido como sigue:

 - Bob: `¿Cuál es la clave secreta?`
 - Trudy: `"3.1415".`
 - Bob: `No es la contraseña correcta.`

.. Human conversations can be very formal, e.g. when soldiers communicate with their hierarchy, or informal such as when friends discuss. Computers that communicate are more akin to soldiers and require well-defined rules to ensure an successful exchange of information.  There are two types of rules that define how information can be exchanged between computers :

..  - syntactical rules that precisely define the format of the messages that are exchanged. As computers only process bits, the syntactical rules specify how information is encoded as bit strings 
..  - organisation of the information flow. For many applications, the flow of information must be structured and there are precedence relationships between the different types of information. In the time example above, Alice must greet Bob before asking for the current time. Alice would not ask for the current time first and greet Bob afterwards. Such precedence relationships exist in networked applications as well. For example, a server must receive a username and a valid password before accepting more complex commands from its clients.

Las conversaciones humanas pueden ser muy formales, por ejemplo, cuando los soldados se comunican con sus superiores, o informal, como cuando dos amigos discuten de cualquier tema. Las computadoras que se comunican se parecen más a los soldados, y requieren reglas bien definidas para asegurar un intercambio de información exitoso. Hay dos tipos de reglas que definen cómo se intercambia la información entre computadoras:

 - Las reglas sintácticas, que definen con precisión el formato de los mensajes intercambiados. Como las computadoras únicamente procesan bits, las reglas sintácticas especifican cómo se codifica la información en forma de cadenas de bits.
 - La organización del flujo de la información. Para muchas aplicaciones, el flujo de la información debe estructurarse, y deben existir relaciones de precedencia entre los diferentes tipos de información. En el ejemplo de la hora, más arriba, Alice debe saludar a Bob `antes` de preguntarle la hora, y no al revés. Estas reglas de precedencia existen en las aplicaciones de red también. Por ejemplo, un servidor debe recibir un nombre de usuario y una contraseña válida antes de aceptar comandos más complejos de sus clientes.

.. Let us first discuss the syntactical rules. We will later explain how the information flow can be organised by analysing real networked applications.

Discutamos primero las reglas sintácticas. Más tarde explicaremos cómo el flujo de información puede organizarse analizando aplicaciones de red reales.

.. Application-layer protocols exchange two types of messages. Some protocols such as those used to support electronic mail exchange messages expressed as strings or lines of characters. As the transport layer allows hosts to exchange bytes, they need to agree on a common representation of the characters. The first and simplest method to encode characters is to use the :term:`ASCII` table. :rfc:`20` provides the ASCII table that is used by many protocols on the Internet. For example, the table defines the following binary representations :

Los protocolos de Capa de Aplicación intercambian dos tipos de mensajes. Algunos protocolos, como los usados para soportar el correo electrónico, intercambian mensajes expresados como cadenas o líneas de caracteres. Como la Capa de Transporte permite a los nodos intercambiar bytes, estos nodos necesitan quedar de acuerdo sobre una representación común de los caracteres. El primer método, y el más simple, para codificar caracteres, es usar la tabla :term:`ASCII`. El documento :rfc:`20` provee la tabla ASCII usada por muchos protocolos en Internet. Por ejemplo, la tabla define las siguientes representaciones binarias:

.. - `A` : `1000011b` 
.. - `0` : `0110000b`
.. - `z` : `1111010b`
.. - `@` : `1000000b`
.. - `space` : `0100000b`

 - `A` : `1000011b` 
 - `0` : `0110000b`
 - `z` : `1111010b`
 - `@` : `1000000b`
 - `espacio` : `0100000b`

.. In addition, the :term:`ASCII` table also defines several non-printable or control characters. These characters were designed to allow an application to control a printer or a terminal. These control characters include `CR` and `LF`, that are used to terminate a line, and the `Bell` character which causes the terminal to emit a sound.

.. - `carriage return` (`CR`) : `0001101b`
.. - `line feed` (`LF`) : `0001010b`
.. - `Bell`: `0000111b`

Además, la tabla ASCII también define varios caracteres no imprimibles o de control. Estos caracteres fueron diseñados para permitir que una aplicación controlara una impresora o un terminal. Estos caracteres de control incluyen `CR` y `LF`, que se usan para terminar una línea, y el carácter `Bell` (campana) que hace que el terminal emita un sonido.

 - Retorno de carro o `carriage return` (`CR`): `0001101b`
 - Nueva línea o `line feed` (`LF`): `0001010b`
 - Campana o `Bell`: `0000111b`

.. The :term:`ASCII` characters are encoded as a seven bits field, but transmitted as an eight-bits byte whose high order bit is usually set to `0`. Bytes are always transmitted starting from the high order or most significant bit.

Los caracteres ASCII se codifican como un campo de siete bits, pero se transmiten como un byte de ocho bits, cuyo bit de orden más alto es generalmente puesto a `0`. Los bytes siempre se transmiten comenzando por el bit más alto o más significativo.

.. Most applications exchange strings that are composed of fixed or variable numbers of characters. A common solution to define the character strings that are acceptable is to define them as a grammar using a Backus-Naur Form (:term:`BNF`) such as the Augmented BNF defined in :rfc:`5234`. A BNF is a set of production rules that generate all valid character strings. For example, consider a networked application that uses two commands, where the user can supply a username and a password. The BNF for this application could be defined as shown in the figure below.

La mayoría de las aplicaciones intercambian cadenas compuestas de un número fijo o variable de caracteres. Una solución común para definir las cadenas de caracteres que son aceptables es definirlas como una gramática, usando una Forma de Backus-Naur (:term:`BNF`) como la `BNF Aumentada` o `ABNF` definida en :rfc:`5234`. Una BNF es un conjunto de reglas de producción que generan todas las cadenas válidas de caracteres. Por ejemplo, consideremos una aplicación de red que usa dos comandos, donde el usuario puede proveer un nombre de usuario y una password. La BNF para esta aplicación podría definirse como sigue:

.. figure:: pkt/bnf.png
   :align: center
   :scale: 100 

   Una especificación BNF sencilla
..   A simple BNF specification

.. The example above defines several terminals and two commands : `usercommand` and `passwordcommand`. The `ALPHA` terminal contains all letters in upper and lower case. In the `ALPHA` rule, `%x41` corresponds to ASCII character code 41 in hexadecimal, i.e. capital `A`.  The `CR` and `LF` terminals correspond to the carriage return and linefeed control characters. The `CRLF` rule concatenates these two terminals to match the standard end of line termination. The `DIGIT` terminal contains all digits. The `SP` terminal corresponds to the white space characters. The `usercommand` is composed of two strings separated by white space. In the ABNF rules that define the messages used by Internet applications, the commands are case-insensitive. The rule `"user"` corresponds to all possible cases of the letters that compose the word between brackets, e.g. `user`, `uSeR`, `USER`, `usER`, ... A `username` contains at least one letter and up to 8 letters. User names are case-sensitive as they are not defined as a string between brackets. The `password` rule indicates that a password starts with a letter and can contain any number of letters or digits. The white space and the control characters cannot appear in a `password` defined by the above rule.

El ejemplo anterior define varios terminales y dos comandos: `usercommand` y `passwordcommand`. El terminal `ALPHA` contiene todas las letras en mayúsculas y minúsculas. En la regla `ALPHA`, `%x41` corresponde al carácter ASCII 41 en hexadecimal, es decir, `A` mayúscula.  Los terminales `CR` y `LF` corresponden a los caracteres de control retorno de carro y nueva línea. La regla `CRLF` concatena estos dos terminales coincidiendo con el fin de línea estándar. El terminal `DIGIT` contiene todos los dígitos. El terminal `SP` corresponde a los caracteres de espacio en blanco. El `usercommand` se compone de dos cadenas separadas por espacio en blanco. En las reglas ABNF que definen los mensajes usados por aplicaciones de Internet, no se diferencia mayúscula de minúsculas en los comandos. La regla `"user"` corresponde a todos los posibles casos de las letras que componen la palabra entre corchetes, es decir,  `user`, `uSeR`, `USER`, `usER`, ... Un nombre de usuario (`username`) contiene al menos una letra y hasta ocho letras. Los nombres de usuario son sensibles a la diferencia entre mayúsculas y minúsculas, porque no están definidos como cadena entre corchetes. La regla `password` indica que una contraseña comienza con una letra y puede contener cualquier cantidad de letras o números. El espacio en blanco y los caracteres de control no pueden aparecer en una `password` definida por la regla anterior.

.. Besides character strings, some applications also need to exchange 16 bits and 32 bits fields such as integers. A naive solution would have been to send the 16- or 32-bits field as it is encoded in the host's memory. Unfortunately, there are different methods to store 16- or 32-bits fields in memory. Some CPUs store the most significant byte of a 16-bits field in the first address of the field while others store the least significant byte at this location. When networked applications running on different CPUs exchange 16 bits fields, there are two possibilities to transfer them over the transport service :

..  - send the most significant byte followed by the least significant byte
..  - send the least significant byte followed by the most significant byte

Además de las cadenas de caracteres, algunas aplicaciones necesitan también intercambiar campos de 16 y 32 bits, como los  enteros. Una solución ingenua podría haber sido enviar los campos de 16 o 32 bits tal como están codificados en la memoria del host. Desafortunadamente, hay diferentes métodos para almacenar esos campos en memoria. Algunas CPUs almacenan el byte más significativo de un campo de 16 bits en la primera dirección del campo, mientras que otras almacenan allí el byte menos significativo. Cuando las aplicaciones de red que corren en diferentes CPUs intercambian esos campos, hay dos posibilidades para transferirlas sobre el servicio de transporte:

 - Enviar el byte más significativo, seguido por el menos significativo
 - Enviar el byte menos significativo, seguido por el más significativo


.. The first possibility was named  `big-endian` in a note written by Cohen [Cohen1980]_ while the second was named `little-endian`. Vendors of CPUs that used `big-endian` in memory insisted on using `big-endian` encoding in networked applications while vendors of CPUs that used `little-endian` recommended the opposite. Several studies were written on the relative merits of each type of encoding, but the discussion became almost a religious issue [Cohen1980]_. Eventually, the Internet chose the `big-endian` encoding, i.e. multi-byte fields are always transmitted by sending the most significant byte first, :rfc:`791` refers to this encoding as the :term:`network-byte order`. Most libraries [#fhtonl]_ used to write networked applications contain functions to convert multi-byte fields from memory to the network byte order and vice versa. 

La primera posibilidad fue llamada `big-endian` en una nota escrita por Cohen [Cohen1980]_ mientras que la segunda fue llamada `little-endian`. Los fabricantes de CPUs que usaban `big-endian` en memoria insistieron en usar codificación `big-endian` en las aplicaciones de redes, mientras que aquéllos que usaban `little-endian` recomendaban lo contrario. Se escribieron varios estudios sobre los méritos relativos de cada tipo de codificación, pero la discusión se tornó un asunto casi religioso [Cohen1980]_. Eventualmente, Internet escogió la codificación `big-endian`, es decir, los campos multi-byte se transmiten siempre enviando primero el byte más significativo. :rfc:`791` se refiere a esta codificación como `orden de red` :term:`network-byte order`. La mayoría de las bibliotecas [#fhtonl]_ usadas para escribir aplicaciones de redes contienen funciones para convertir campos multi-byte, de orden en memoria a orden de red y viceversa. 

.. Besides 16 and 32 bit words, some applications need to exchange data structures containing bit fields of various lengths. For example, a message may be composed of a 16 bits field followed by eight, one bit flags, a 24 bits field and two 8 bits bytes. Internet protocol specifications will define such a message by using a representation such as the one below. In this representation, each line corresponds to 32 bits and the vertical lines are used to delineate fields. The numbers above the lines indicate the bit positions in the 32-bits word, with the high order bit at position `0`. 

Además de las palabras de 16 y 32 bits, algunas aplicaciones necesitan intercambiar estructuras de datos conteniendo campos de bits de varias longitudes. Por ejemplo, un mensaje puede estar compuesto de un campo de 16 bits seguido de ocho flags de un bit, un campo de 24 bits y dos bytes de 8 bits. Las especificaciones de protocolos de Internet definirán dicho mensaje usando una representación como la siguiente. En esta representación, cada línea corresponde a 32 bits y las líneas verticales se usan para delimitar campos. Los números encima de las líneas indican las posiciones de bits en la palabra de 32 bits, con el bit de orden más alto en la posición `0`.

.. figure:: pkt/message.png
   :align: center
   :scale: 100 

   Formato de mensajes
..   Message format

.. The message mentioned above will be transmitted starting from the upper 32-bits word in network byte order. The first field is encoded in 16 bits. It is followed by eight one bit flags (`A-H`), a 24 bits field whose high order byte is shown in the first line and the two low order bytes appear in the second line followed by two one byte fields. This ASCII representation is frequently used when defining binary protocols. We will use it for all the binary protocols that are discussed in this book.

El mensaje mencionado anteriormente será transmitido comenzando por la palabra de 32 bits, situada al tope de la figura, en orden de red. El primer campo se codifica en 16 bits. Lo siguen ocho señales (`flags`) de un bit (`A-H`), un campo de 24 bits cuyo byte de orden más alto se muestra en la primera línea, y los dos bytes de orden bajo que aparecen en la segunda línea, seguidos por dos campos de un byte. Esta representación ASCII se usa con frecuencia al definir protocolos binarios. La usaremos para todos los protocolos binarios que se discutan en este libro.

.. We will discuss several examples of application-level protocols in this chapter.

En este capítulo hablaremos sobre varios ejemplos de protocolos de nivel de Aplicación.

.. introduce ipv4 and ipv6 addresses
.. mention names very early, they are important

.. index:: peer-to-peer

El modelo peer-to-peer
======================

.. The peer-to-peer model emerged during the last ten years as another possible architecture for networked applications. In the traditional client-server model, hosts act either as servers or as clients and a server serves a large number of clients. In the peer-to-peer model, all hosts act as both servers and clients and they play both roles. The peer-to-peer model has been used to develop various networked applications, ranging from Internet telephony to file sharing or Internet-wide filesystems. A detailed description of peer-to-peer applications may be found in [BYL2008]_. Surveys of peer-to-peer protocols and applications may be found in [AS2004]_ and [LCP2005]_.

El modelo peer-to-peer emergió durante los últimos diez años como otra posible arquitectura para aplicaciones de red. En el modelo cliente-servidor tradicional, los hosts actúan como servidores o como clientes, y un servidor da servicio a una gran cantidad de clientes. En el modelo peer-to-peer, todos los hosts actúan a la vez como servidores y como clientes, jugando ambos roles. El modelo peer-to-peer ha sido usado para desarrollar varias aplicaciones de red, desde telefonía IP hasta compartir archivos, o implantar sistemas de archivos que abarcan la Internet. Se puede consultar una descripción detallada de aplicaciones peer-to-peer en [BYL2008]_. Pueden hallarse estudios de protocolos y aplicaciones peer-to-peer en [AS2004]_ y [LCP2005]_.


.. principle distinction between server and client does not exist anymore
.. focus will be on file distribution, but there are various other usages
.. centralised p2p, like napster
.. unstructured p2P like gnutella or freenet
.. structured like chord as example

.. Surveys : 

.. Chord : [SMKKB2001]_


.. The peer-to-peer model 


.. rubric:: Footnotes

.. .. [#fhtonl] For example, the :manpage:`htonl(3)` (resp. :manpage:`ntohl(3)`) function the standard C library converts a 32-bits unsigned integer from the byte order used by the CPU to the network byte order (resp. from the network byte order to the CPU byte order). Similar functions exist in other programming languages.
.. [#fhtonl] Por ejemplo, la función :manpage:`htonl(3)` (resp. :manpage:`ntohl(3)`), de la biblioteca estándar de C, convierte un entero sin signo de 32 bits, del orden usado por la CPU al orden de red (resp. del orden de red al orden de la CPU). Existen funciones similares en otros lenguajes de programación.
.. [#faliceandbob] Alice y Bob (y ocasionalmente su enemiga común Trudy) son personajes típicos de la bibliografía de Seguridad Informática. En la situación habitual, Alice y Bob quieren comunicarse en forma segura, pero Trudy intenta ataques a la confidencialidad o a la integridad de sus mensajes.

.. include:: /links.rst
