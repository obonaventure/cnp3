.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Principios
##########

.. The datalink layer uses the service provided by the physical layer. Although there are many different implementations of the physical layer from a technological perspective, they all provide a service that enables the datalink layer to send and receive bits between directly connected devices. The datalink layer receives packets from the network layer. Two datalink layer entities exchange `frames`. As explained in the previous chapter, most datalink layer technologies impose limitations on the size of the frames. Some technologies only impose a maximum frame size, others enforce both minimum and maximum frames sizes and finally some technologies only support a single frame size. In the latter case, the datalink layer will usually include an adaptation sublayer to allow the network layer to send and receive variable-length packets. This adaptation layer may include fragmentation and reassembly mechanisms.
La capa de Enlace de Datos usa el servicio provisto por la capa Física. Aunque hay muchas diferentes implementaciones de la capa Física desde un punto de vista tecnológico, todas ellas proveen un servicio que habilita a la capa de Enlace de Datos a enviar y recibir bits entre dispositivos directamente conectados. La capa de Enlace de Datos recibe paquetes de la capa de red. Dos entidades de capa de Enlace de Datos intercambian `tramas` (`frames`). Como se explicó en el capítulo anterior, la mayoría de las tecnologías de enlace de datos imponen limitaciones sobre el tamaño de las tramas. Algunas tecnologías sólo imponen un tamaño máximo de trama; otras imponen tamaños máximos y mínimos, y finalmente, algunas sólo soportan un único tamaño de trama. En este último caso, la capa de Enlace de Datos generalmente incluirá una subcapa de adaptación para permitir que la capa de red pueda enviar y recibir paquetes de tamaño variable. Esta capa de adaptación puede incluir mecanismos de fragmentación y reensamblado.


.. figure:: png/lan-fig-003-c.png
   :align: center
   :scale: 70
   
   La capa de Enlace de Datos y el modelo de referencia 
..   The datalink layer and the reference model


.. The physical layer service facilitates the sending and receiving of bits. Furthermore, it is usually far from perfect as explained in the introduction :
El servicio de la capa Física facilita el envío y recepción de bits. Pero, por otro lado, normalmente está lejos de la perfección, como se explicó en la Introducción:

 - La capa Física puede alterar (debido, por ejemplo, a interferencias electromagnéticas) el valor de un bit que está siendo transmitido. 
 - La capa Física puede entregar `más` bits al receptor que los bits enviados por el emisor.
 - La capa Física puede entregar `menos` bits al receptor que los bits enviados por el emisor.

.. - the Physical layer may change, e.g. due to electromagnetic interferences, the value of a bit being transmitted
.. - the Physical layer may deliver `more` bits to the receiver than the bits sent by the sender
.. - the Physical layer may deliver `fewer` bits to the receiver than the bits sent by the sender

.. The datalink layer must allow endsystems to exchange frames containing packets despite all of these limitations. On point-to-point links and Local Area Networks, the first problem to be solved is how to encode a frame as a sequence of bits, so that the receiver can easily recover the received frame despite the limitations of the physical layer.
La capa de Enlace de Datos debe permitir que los sistemas finales intercambien tramas conteniendo paquetes, a pesar de todas estas limitaciones. En enlaces punto a punto, y en LANs, el primer problema a resolver es cómo codificar una trama como una secuencia de bits, de modo que el receptor pueda fácilmente recuperar la trama recibida a pesar de las limitaciones de la capa Física.




.. index:: framing

.. If the physical layer were perfect, the problem would be very simple. The datalink layer would simply need to define how to encode each frame as a sequence of consecutive bits. The receiver would then easily be able to extract the frames from the received bits. Unfortunately, the imperfections of the physical layer make this framing problem slightly more complex. Several solutions have been proposed and are used in practice in different datalink layer technologies.
Si la capa Física fuera perfecta, el problema sería muy simple. La capa de Enlace de Datos simplemente necesitaría definir cómo codificar cada trama como secuencia de bits consecutivos. El receptor entonces fácilmente podría extraer las tramas de los bits recibidos. Desafortunadamente, las imperfecciones de la capa Física hacen que este problema del `framing` resulte algo más complejo. Se han propuesto y usado en la práctica varias soluciones en diferentes tecnologías de enlace de datos.

Framing
=======

.. This is the `framing` problem. It can be defined as : "`How does a sender encode frames so that the receiver can efficiently extract them from the stream of bits that it receives from the physical layer`". 

En esto consiste el problema del `framing`, que puede definirse de la siguiente manera: "`Cómo debe un emisor codificar las tramas de manera que el receptor pueda extraerlas eficientemente del tren de bits que recibe de la capa Física`".

.. A first solution to solve the framing problem is to require the physical layer to remain idle for some time after the transmission of each frame. These idle periods can be detected by the receiver and serve as a marker to delineate frame boundaries. Unfortunately, this solution is not sufficient for two reasons. First, some physical layers cannot remain idle and always need to transmit bits. Second, inserting an idle period between frames decreases the maximum bandwidth that can be achieved by the datalink layer.
Una primera solución al problema del framing es requerir que la capa Física permanezca ociosa durante algún tiempo después de la transmisión de cada trama. Estos períodos ociosos pueden ser detectados por el receptor y servir como demarcación de los límites de tramas. Lamentablemente, esta solución no es suficiente por dos razones. Primero, algunas implementaciones de la capa Física no pueden permanecer ociosas y necesitan estar siempre transmitiendo bits. Segundo, insertar un período ocioso entre tramas disminuye el ancho de banda máximo que puede lograrse en la capa de Enlace de Datos.

.. .. index:: Manchester encoding
.. index:: Codificación Manchester

.. Some physical layers provide an alternative to this idle period. All physical layers are able to send and receive physical symbols that represent values `0` and `1`. However, for various reasons that are outside the scope of this chapter, several physical layers are able to exchange other physical symbols as well. For example, the Manchester encoding used in several physical layers can send four different symbols. The Manchester encoding is a differential encoding scheme in which time is divided into fixed-length periods. Each period is divided in two halves and two different voltage levels can  be applied. To send a symbol, the sender must set one of these two voltage levels during each half period. To send a `1` (resp. `0`), the sender must set a high (resp. low) voltage during the first half of the period and a low (resp. high) voltage during the second half. This encoding ensures that there will be a transition at the middle of each period and allows the receiver to synchronise its clock to the sender's clock. Apart from the encodings for `0` and `1`, the Manchester encoding also supports two additional symbols : `InvH` and `InvB`  where the same voltage level is used for the two half periods. By definition, these two symbols cannot appear inside a frame which is only composed of `0` and `1`. Some technologies use these special symbols as markers for the beginning or end of frames.

Algunas entidades de la capa Física proveen una alternativa a este período ocioso. Todas las entidades de la capa Física son capaces de enviar y recibir símbolos físicos que representan valores `0` y `1`. Sin embargo, por varios motivos que escapan al alcance de este capítulo, varias de ellas son capaces de intercambiar otros símbolos físicos también. Por ejemplo, la codificación Manchester usada en varias implementaciones de capa Física puede enviar cuatro símbolos diferentes. La codificación Manchester es un esquema de codificación diferencial en el cual el tiempo se divide en períodos de longitud fija. Cada período se divide en dos mitades, y se pueden aplicar dos diferentes niveles de voltaje. Para enviar un símbolo, el emisor debe fijar uno de estos niveles de voltaje durante cada semiperíodo. Para enviar un `1` (resp. un `0`) el emisor debe fijar un voltaje alto (resp. bajo) durante la primera mitad del período, y un voltaje bajo (resp. alto) durante la segunda mitad. Esta codificación asegura que siempre habrá una transición en el medio de cada período, y permite que el receptor sincronice su reloj al del emisor. Aparte de las codificaciones para el `0` y el `1`, la codificación Manchester también soporta dos símbolos adicionales: `InvH` e `InvB`, donde se usa el mismo nivel de voltaje para los dos semiperíodos. Por definición, estos dos símbolos no pueden aparecer dentro de una trama que sólo se componga de `0` y `1`. Algunas tecnologías hacen uso de estos símbolos especiales como delimitadores para el principio o fin de las tramas.

.. figure:: png/lan-fig-006-c.png
   :align: center
   :scale: 70
   
   Codificación Manchester
..   Manchester encoding

.. .. index:: bit stuffing, stuffing (bit)
.. index:: bit stuffing, stuffing (bit) rellenado de bits, bit de relleno

.. Unfortunately, multi-symbol encodings cannot be used by all physical layers and a generic solution which can be used with any physical layer that is able to transmit and receive only `0` and `1` is required. This generic solution is called `stuffing` and two variants exist : `bit stuffing` and `character stuffing`. To enable a receiver to easily delineate the frame boundaries, these two techniques reserve special bit strings as frame boundary markers and encode the frames so that these special bit strings do not appear inside the frames.
Lamentablemente, las codificaciones multi-símbolo no pueden ser usadas en todas las entidades físicas, y se requiere una solución genérica que se pueda usar con cualquier implementación de la capa Física que sea capaz de transmitir y recibir sólo símbolos `0` y `1`.

.. `Bit stuffing` reserves the `01111110` bit string as the frame boundary marker and ensures that there will never be six consecutive `1` symbols transmitted by the physical layer inside a frame. With bit stuffing, a frame is sent as follows. First, the sender transmits the marker, i.e. `01111110`. Then, it sends all the bits of the frame and inserts an additional bit set to `0` after each sequence of five consecutive `1` bits. This ensures that the sent frame never contains a sequence of six consecutive bits set to `1`. As a consequence, the marker pattern cannot appear inside the frame sent. The marker is also sent to mark the end of the frame. The receiver performs the opposite to decode a received frame. It first detects the beginning of the frame thanks to the `01111110` marker. Then, it processes the received bits and counts the number of consecutive bits set to `1`. If a `0` follows five consecutive bits set to `1`, this bit is removed since it was inserted by the sender. If a `1` follows five consecutive bits sets to `1`, it indicates a marker if it is followed by a bit set to `0`. The table below illustrates the application of bit stuffing to some frames.

La técnica del `rellenado de bit` ("`bit stuffing`") reserva la cadena de bits `01111110` como  marca de límite de tramas, y asegura que la capa Física nunca transmitirá seis símbolos `1` consecutivos dentro de una trama. Con rellenado de bit, una trama se envía del siguiente modo. Primero, el emisor transmite la marca, es decir, `01111110`. Luego, envía todos los bits de la trama, insertando un bit `0` adicional luego de cada secuencia de cinco bits `1` consecutivos. Esto asegura que nunca la trama enviada contenga una secuencia de seis bits `1` consecutivos. Como consecuencia, la marca nunca puede aparecer dentro de la trama enviada. La marca se utiliza entonces para marcar el final de cada trama. El receptor ejecuta la operación inversa para recuperar la trama recibida. Primero, detecta el principio de cada trama gracias a la marca `01111110`. Luego, procesa los bits recibidos y cuenta el número de bits consecutivos puestos a `1`. Si un  grupo de cinco bits `1` consecutivos es seguido por un `0`, este bit se elimina, ya que fue insertado por el emisor. Si un grupo de cinco bits consecutivos `1` es seguido por un `1`, entonces indica una marca sólo si a su vez está seguido por un bit `0`. La tabla más abajo ilustra la aplicación del rellenado de bit a algunas tramas.

 ===========================   =============================================
 Trama original	      	       Trama transmitida
 ===========================   =============================================
 0001001001001001001000011     01111110000100100100100100100001101111110
 0110111111111111111110010     01111110011011111011111011111011001001111110
 01111110		       0111111001111101001111110
 ===========================   =============================================
 

.. For example, consider the transmission of `0110111111111111111110010`. The sender will first send the `01111110` marker followed by `011011111`. After these five consecutive bits set to `1`, it inserts a bit set to `0` followed by `11111`. A new `0` is inserted, followed by `11111`. A new `0` is inserted followed by the end of the frame `110010` and the `01111110` marker.
Por ejemplo, consideremos la transmisión de `0110111111111111111110010`. El emisor primero envía la marca `01111110` seguida por `011011111`. Luego de estos cinco bits consecutivos a `1`, inserta un bit puesto a `0` seguido por  `11111`. Luego inserta un nuevo `0`, seguido por `11111`. Luego inserta un nuevo `0` seguido por el final de la trama `110010`, y finalmente la marca `01111110`.


.. `Bit stuffing` increases the number of bits required to transmit each frame. The worst case for bit stuffing is of course a long sequence of bits set to `1` inside the frame. If transmission errors occur, stuffed bits or markers can be in error. In these cases, the frame affected by the error and possibly the next frame will not be correctly decoded by the receiver, but it will be able to resynchronise itself at the next valid marker. 
El `bit stuffing` incrementa el número de bits necesarios para transmitir cada trama. El peor caso es, por supuesto, una larga secuencia de bits, todos puestos a `1`, dentro de la trama. Si ocurren errores de transmisión, los bits relleno o las marcas pueden ser recibidas con errores. En estos casos, la trama afectada por el error, y posiblemente también la próxima trama, no serán correctamente decodificadas por el receptor; pero éste será capaz de resincronizarse al recibir la siguiente marca válida.

.. index:: character stuffing, stuffing (character), rellenado de carácter, carácter de relleno

.. `Bit stuffing` can be easily implemented in hardware. However, implementing it in software is difficult given the higher overhead of bit manipulations in software. Software implementations prefer to process characters than bits, software-based datalink layers usually use `character stuffing`. This technique operates on frames that contain an integer number of 8-bit characters. Some characters are used as markers to delineate the frame boundaries. Many `character stuffing` techniques use the `DLE`, `STX` and `ETX` characters of the ASCII character set. `DLE STX` (resp. `DLE ETX`) is used to mark the beginning (end) of a frame. When transmitting a frame, the sender adds a `DLE` character after each transmitted `DLE` character. This ensures that none of the markers can appear inside the transmitted frame. The receiver detects the frame boundaries and removes the second `DLE` when it receives two consecutive `DLE` characters. For example, to transmit frame `1 2 3 DLE STX 4`, a sender will first send `DLE STX` as a marker, followed by `1 2 3 DLE`. Then, the sender transmits an additional `DLE` character followed by `STX 4` and the `DLE ETX` marker.

El `bit stuffing` puede implementarse con facilidad en hardware. Sin embargo, implementarlo en software es difícil debido a la alta sobrecarga que presenta la manipulación de bits en software. Las implementaciones de software prefieren procesar caracteres antes que bits, por lo cual las entidades de enlace de datos implementadas en software generalmente usan `relleno de carácter` (`character stuffing`). Esta técnica opera sobre tramas que contienen un número entero de caracteres de ocho bits. Algunos caracteres se usan como marcas para demarcar los límites de las tramas.  Muchas técnicas de `character stuffing` usan los caracteres `DLE`, `STX` y `ETX` del conjunto de caracteres ASCII. `DLE STX` (resp. `DLE ETX`) se usa para señalar el comienzo (resp. final) de una trama. Al transmitir una trama, el emisor agrega un carácter `DLE` luego de cada carácter `DLE` transmitido. Esto asegura que ninguna de las marcas pueda aparecer dentro de la trama transmitida. El receptor detecta los límites de la trama y elimina el segundo `DLE` cada vez que reciba dos `DLE` consecutivos. Por ejemplo, para transmitir la trama `1 2 3 DLE STX 4`, un emisor enviará primero `DLE STX` como marca, seguido de `1 2 3 DLE`. Luego transmitirá un carácter `DLE` adicional seguido por `STX 4` y finalmente la marca `DLE ETX`.

 ===========================   =============================================
 Trama original	      	       Trama transmitida
 ===========================   =============================================
 `1 2 3 4`		       `DLE STX 1 2 3 4 DLE ETX`
 `1 2 3 DLE STX 4`	       `DLE STX 1 2 3 DLE DLE STX 4 DLE ETX`
 `DLE STX DLE ETX`	       `DLE STX DLE DLE STX DLE DLE ETX DLE ETX`
 ===========================   =============================================

.. `Character stuffing` , like bit stuffing, increases the length of the transmitted frames. For `character stuffing`, the worst frame is a frame containing many `DLE` characters. When transmission errors occur, the receiver may incorrectly decode one or two frames (e.g. if the errors occur in the markers). However, it will be able to resynchronise itself with the next correctly received markers.
Como el relleno de bits, el relleno de caracteres incrementa la longitud de las tramas transmitidas. Para el relleno de caracteres, la peor trama es aquella que contiene muchos caracteres `DLE`. Cuando ocurran errores de transmisión, el receptor podrá decodificar incorrectamente una o dos tramas (por ejemplo, si los errores ocurren sobre las marcas). Sin embargo, podrá resincronizarse con la siguiente marca correctamente recibida.

Detección de errores
====================

.. Besides framing, datalink layers also include mechanisms to detect and sometimes even recover from transmission error. To allow a receiver to detect transmission errors, a sender must add some redundant information as an `error detection` code to the frame sent. This `error detection` code is computed by the sender on the frame that it transmits. When the receiver receives a frame with an error detection code, it recomputes it and verifies whether the received `error detection code` matches the computer `error detection code`. If they match, the frame is considered to be valid. Many error detection schemes exist and entire books have been written on the subject. A detailed discussion of these techniques is outside the scope of this book, and we will only discuss some examples to illustrate the key principles.

Además del `framing`, la capa de enlace también incluye mecanismos para detectar errores de transmisión, y a veces recuperarse de ellos. Para que un receptor pueda detectar errores de transmisión, un emisor debe agregar alguna información redundante a la trama que está enviando, a manera de código de `detección de errores`. Este código de `detección de errores` es un dato computado por el emisor para cada trama que envía. Cuando el receptor recibe una trama con código de detección de errores, lo recomputa y verifica si el código recibido coincide con el código computado. Si coinciden, la trama se considera válida. Existen muchos esquemas de detección de errores, y hay libros completos dedicados al tema. Una discusión detallada de estas técnicas está fuera del alcance de este libro, y sólo analizaremos algunos ejemplos para ilustrar los principios clave.

.. To understand `error detection codes`, let us consider two devices that exchange bit strings containing `N` bits. To allow the receiver to detect a transmission error, the sender converts each string of `N` bits into a string of `N+r` bits. Usually, the `r` redundant bits are added at the beginning or the end of the transmitted bit string, but some techniques interleave redundant bits with the original bits. An `error detection code` can be defined as a function that computes the `r` redundant bits corresponding to each string of `N` bits. The simplest error detection code is the parity bit. There are two types of parity schemes : even and odd parity. With the `even` (resp. `odd`) parity scheme, the redundant bit is chosen so that an even (resp. odd) number of bits are set to `1` in the transmitted bit string of `N+r` bits. The receiver can easily recompute the parity of each received bit string and discard the strings with an invalid parity. The parity scheme is often used when 7-bit characters are exchanged. In this case, the eighth bit is often a parity bit. The table below shows the parity bits that are computed for bit strings containing three bits. 


Para comprender los `códigos de detección de errores`, consideremos dos dispositivos que intercambian cadenas de bits conteniendo `N` bits. Para permitir al receptor detectar un error de transmisión, el emisor convierte cada cadena de `N` bits en una cadena de `N+r` bits. Generalmente, los `r` bits redundantes se agregan al principio o al final de la cadena transmitida, pero algunas técnicas entremezclan los bits redundantes con los originales. Un código de detección de errores puede definirse com una función que computa los `r` bits redundantes correspondientes a cada cadena de `N` bits. El código de detección de errores más simple es el bit de paridad. Hay dos tipos de esquemas de paridad: paridad par y paridad impar. Con el esquema de paridad impar (resp. par), el bit de redundancia se elige de manera que haya una cantidad impar (resp. par) de bits a `1` en la cadena transmitida de `N+r` bits. El receptor puede fácilmente recomputar la paridad de cada cadena de bits recibida y descartar las cadenas con paridad inválida. El esquema de paridad suele usarse cuando se intercambian caracteres de 7 bits. En este caso, el octavo bit es frecuentemente un bit de paridad. La tabla más abajo muestra los bits de paridad que son computados a partir de cadenas de bits de tamaño 3.

  ================	=============	===========
  Cadena de 3 bits	Paridad impar	Paridad par
  ================	=============	===========
  000	     		  1		   0
  001			  0		   1
  010			  0		   1
  100			  0		   1
  111			  0		   1
  110			  1		   0
  101			  1		   0
  011			  1		   0
  ================	=============	===========


.. The parity bit allows a receiver to detect transmission errors that have affected a single bit among the transmitted `N+r` bits. If there are two or more bits in error, the receiver may not necessarily be able to detect the transmission error. More powerful error detection schemes have been defined. The Cyclical Redundancy Checks (CRC) are widely used in datalink layer protocols. An N-bits CRC can detect all transmission errors affecting a burst of less than N bits in the transmitted frame and all transmission errors that affect an odd number of bits. Additional details about CRCs may be found in [Williams1993]_.


El bit de paridad permite que un receptor detecte errores de transmisión que hayan afectado a un único bit entre los `N+r` bits transmitidos. Si hay dos o más bits en error, el receptor no necesariamente será capaz de detectar el error de transmisión. Se han definido esquemas de detección de errores más poderosos. Los `Códigos de Redundancia Cíclicos` (`Cyclical Redundancy Checks`, CRC) se usan ampliamente en los protocolos de la capa de Enlace de Datos. Un CRC de N bits puede detectar todos los errores de transmisión que afecten una ráfaga de menos de N bits en la trama transmitida, y todos los errores de transmisión que afecten a un número impar de bits. Pueden encontrarse más detalles sobre CRCs en [Williams1993]_.

.. It is also possible to design a code that allows the receiver to correct transmission errors. The simplest `error correction code` is the triple modular redundancy (TMR). To transmit a bit set to `1` (resp. `0`), the sender transmits `111` (resp. `000`). When there are no transmission errors, the receiver can decode `111` as `1`. If transmission errors have affected a single bit, the receiver performs majority voting as shown in the table below. This scheme allows the receiver to correct all transmission errors that affect a single bit. 

También es posible diseñar un código que permita al receptor `corregir` errores de transmisión. El `código de corrección de errores` más simple posible es la triple redundancia modular (TMR). Para transmitir un bit en `1` (resp. `0`), el emisor transmite `111` (resp. `000`). Cuando no haya errores de transmisión, el receptor podrá decodificar `111` como `1`. Si los errores de transmisión han afectado a un único bit, el receptor decide por el voto de la mayoría, como se muestra en la tabla más abajo. Este esquema permite que el receptor corrija todos los errores de transmisión que afecten a un único bit.

  ==============    ================
  Bits recibidos    Bit decodificado
  ==============    ================
	 000	 	0
	 001		0
	 010		0
	 100		0
	 111		1
	 110		1
	 101		1
	 011		1
  ==============    ================

.. Other more powerful error correction codes have been proposed and are used in some applications. The `Hamming Code <http://en.wikipedia.org/wiki/Hamming_code>`_ is a clever combination of parity bits that provides error detection and correction capabilities. 

Se han propuesto códigos de corrección de errores más poderosos, y se usan en algunas aplicaciones. El `Código de Hamming <http://en.wikipedia.org/wiki/Hamming_code>`_ es una astuta combinación de bits de paridad que ofrece capacidades de detección y corrección de errores.

.. In practice, datalink layer protocols combine bit stuffing or character stuffing with a length indication in the frame header and a checksum or CRC. The checksum/CRC is computed by the sender and placed in the frame before applying bit/character stuffing.

En la práctica, los protocolos de capa de Enlace de Datos combinan rellenado de bits o de caracteres con una indicación de longitud en la cabecera de la trama y una suma de control o un CRC. La suma de control o CRC son computados por el emisor y colocados en la trama antes de aplicar rellenado de bits o caracteres.

Control de Acceso al Medio
##########################

.. Point-to-point datalink layers need to select one of the framing techniques described above and optionally add retransmission algorithms such as those explained for the transport layer to provide a reliable service. Datalink layers for Local Area Networks face two additional problems. A LAN is composed of several hosts that are attached to the same shared physical medium. From a physical layer perspective, a LAN can be organised in four different ways :

Para ofrecer un servicio confiable, las entidades de capa de Enlace de Datos punto a punto necesitan seleccionar una de las técnicas de framing descritas anteriormente, y opcionalmente agregar algoritmos de retransmisión como los explicados para la capa de transporte. La capa de enlace para LANs enfrenta dos problemas adicionales. Una LAN se compone de varios hosts que están conectados al mismo medio físico compartido. Desde el punto de vista físico, una LAN puede organizarse en cuatro formas diferentes:

 - Red en forma de bus donde todos los nodos están conectados al mismo medio físico
 - Red en forma de anillo donde todos los nodos están conectados a un nodo anterior y uno posterior según el sentido de recorrido del anillo
 - Red en forma de estrella, donde todos los nodos están conectados a un mismo dispositivo
 - Red inalámbrica, donde todos los nodos pueden enviar y recibir tramas usando señales de radio

.. - a bus-shaped network where all hosts are attached to the same physical cable
.. - a ring-shaped where all hosts are attached to an upstream and a downstream node so that the entire network forms a ring
.. - a star-shaped network where all hosts are attached to the same device
.. - a wireless network where all hosts can send and receive frames using radio signals

.. These four basic physical organisations of Local Area Networks are shown graphically in the figure below. We will first focus on one physical organisation at a time.

Estas cuatro formas básicas de organización física de las Redes de Área Local se muestran gráficamente en la figura más abajo. Nos ocuparemos de una forma de organización física por vez.

.. figure:: svg/bus-ring-star.png
   :align: center
   :scale: 90
  
   Redes de Área Local en forma de bus, anillo y estrella 
..   Bus, ring and star-shaped Local Area Network 


.. .. index:: collision
.. index:: colisiones

.. The common problem among all of these network organisations is how to efficiently share the access to the Local Area Network. If two devices send a frame at the same time, the two electrical, optical or radio signals that correspond to these frames will appear at the same time on the transmission medium and a receiver will not be able to decode either frame. Such simultaneous transmissions are called `collisions`. A `collision` may involve frames transmitted by two or more devices attached to the Local Area Network. Collisions are the main cause of errors in wired Local Area Networks.

El problema común de todas estas organizaciones de red es cómo compartir eficientemente el acceso a la LAN. Si dos dispositivos envían una trama al mismo tiempo, las dos señales eléctricas, ópticas o de radio, que correspondan a estas tramas, aparecerán al mismo tiempo sobre el medio de transmisión, y un receptor no podrá decodificar ninguna de las dos tramas. Estas transmisiones simultáneas se llaman `colisiones`. En una `colisión` pueden estar implicadas tramas transmitidas por dos o más dispositivos conectados a la LAN. Las colisiones son la principal causa de errores en las Redes de Área Local cableadas. 

.. All Local Area Network technologies rely on a `Medium Access Control` algorithm to regulate the transmissions to either minimise or avoid collisions. There are two broad families of `Medium Access Control` algorithms :

Todas las tecnologías de LAN descansan sobre un algoritmo de `Control de Acceso al Medio` (`Medium Access Control`, MAC) para regular las transmisiones de modo de minimizar o evitar las colisiones. Hay dos amplias familias de algoritmos MAC, o de Control de Acceso al Medio:

 #. Algoritmos MAC `determinísticos`, o `pesimistas`. Estos algoritmos asumen que las colisiones son un problema muy severo y que debe ser completamente evitado. Estos algoritmos aseguran que en cualquier momento, a lo sumo un dispositivo esté habilitado para enviar una trama a la LAN. Esto generalmente se logra usando un protocolo distribuido que elige un único dispositivo para transmitir en cada momento. Un algoritmo MAC determinístico asegura que no haya colisiones, pero la regulación de la transmisión de todos los dispositivos de la LAN provocará una cierta sobrecarga.
 #. Algoritmos MAC `estocásticos`, u `optimistas`. Estos algoritmos asumen que las colisiones son parte de la operación normal de una LAN. Apuntan a minimizar el número de colisiones, pero no intentan evitarlas a todas. Los algoritmos estocásticos generalmente son más fáciles de implementar que los determinísticos.

..  #. `Deterministic` or `pessimistic` MAC algorithms. These algorithms assume that collisions are a very severe problem and that they must be completely avoided. These algorithms ensure that at any time, at most one device is allowed to send a frame on the LAN. This is usually achieved by using a distributed protocol which elects one device that is allowed to transmit at each time. A deterministic MAC algorithm ensures that no collision will happen, but there is some overhead in regulating the transmission of all the devices attached to the LAN.
.. #. `Stochastic` or `optimistic` MAC algorithms. These algorithms assume that collisions are part of the normal operation of a Local Area Network. They aim to minimise the number of collisions, but they do not try to avoid all collisions. Stochastic algorithms are usually easier to implement than deterministic ones.


.. We first discuss a simple deterministic MAC algorithm and then we describe several important optimistic algorithms, before coming back to a distributed and deterministic MAC algorithm.

Primero veremos un algoritmo MAC determinístico simple, y luego describiremos varios algoritmos optimistas importantes, antes de volver a un algoritmo MAC distribuido y determinístico.

Métodos de asignación estática
==============================

.. A first solution to share the available resources among all the devices attached to one Local Area Network is to define, `a priori`, the distribution of the transmission resources among the different devices. If `N` devices need to share the transmission capacities of a LAN operating at `b` Mbps, each device could be allocated a bandwidth of :math:`\frac{b}{N}` Mbps. 

Una primera solución para compartir los recursos disponibles entre todos los dispositivos conectados a una Red de Área Local es definir, `a priori`, la distribución de los recursos de transmisión entre los diferentes dispositivos. Si `N` dispositivos necesitan compartir las capacidades de transmisión de una LAN que opera a `b` Mbps, cada dispositivo deberá recibir un ancho de banda de :math:`\frac{b}{N}` Mbps. 

.. index:: Frequency Division Multiplexing, FDM, Multiplexado por División de Frecuencia

.. Limited resources need to be shared in other environments than Local Area Networks. Since the first radio transmissions by `Marconi <http://en.wikipedia.org/wiki/Guglielmo_Marconi>`_ more than one century ago, many applications that exchange information through radio signals have been developed. Each radio signal is an electromagnetic wave whose power is centered around a given frequency. The radio spectrum corresponds to frequencies ranging between roughly 3 KHz and 300 GHz. Frequency allocation plans negotiated among governments reserve most frequency ranges for specific applications such as broadcast radio, broadcast television, mobile communications, aeronautical radio navigation, amateur radio, satellite, etc. Each frequency range is then subdivided into channels and each channel can be reserved for a given application, e.g. a radio broadcaster in a given region.

Los recursos limitados necesitan ser compartidos, en otros ambientes que las Redes de Área Local. Desde las primeras transmisiones de radio realizadas por `Marconi <http://en.wikipedia.org/wiki/Guglielmo_Marconi>`_, hace más de un siglo, se han desarrollado muchas aplicaciones que intercambian información a través de señales de radio. Cada señal de radio es una onda electromagnética cuya potencia se centra alrededor de una frecuencia dada. El espectro de radio corresponde a frecuencias que van aproximadamente desde los 3 KHz hasta los 300 GHz. Los planes de asignación de frecuencias negociados entre los gobiernos reservan la mayor parte de los rangos de frecuencias para aplicaciones específicas, como radiodifusión, teledifusión, comunicaciones móviles, radionavegación aeronáutica, radio amateur, satélite, etc. Cada rango de frecuencia se subdivide en canales y cada canal puede ser reservado para una cierta aplicación; por ejemplo, para una estación de radio en una región dada.

.. index:: Wavelength Division Multiplexing, WDM, Multiplexado por División de Frecuencia de Onda

.. `Frequency Division Multiplexing` (FDM) is a static allocation scheme in which a frequency is allocated to each device attached to the shared medium. As each device uses a different transmission frequency, collisions cannot occur. In optical networks, a variant of FDM called `Wavelength Division Multiplexing` (WDM) can be used. An optical fiber can transport light at different wavelengths without interference. With WDM, a different wavelength is allocated to each of the devices that share the same optical fiber.

La `Multiplexión por División de Frecuencia` (`Frequency Division Multiplexing`, FDM) es un esquema de asignación estática en el cual se asigna una frecuencia a cada dispositivo conectado al medio compartido. Como cada dispositivo usa una frecuencia de transmisión diferente, las colisiones no pueden ocurrir. En las redes ópticas puede usarse una variante de FDM, llamada `Multiplexado por División en Frecuencia de Onda` (`Wavelength Division Multiplexing`, WDM). Con WDM, se asigna una longitud de onda diferente a cada uno de los dispositivos que comparten la misma fibra óptica.


.. index:: Time Division Multiplexing, Multiplexado por División en Tiempo

.. `Time Division Multiplexing` (TDM) is a static bandwidth allocation method that was initially defined for the telephone network. In the fixed telephone network, a voice conversation is usually transmitted as a 64 Kbps signal. Thus, a telephone conservation generates 8 KBytes per second or one byte every 125 microseconds. Telephone conversations often need to be multiplexed together on a single line. For example, in Europe, thirty 64 Kbps voice signals are multiplexed over a single 2 Mbps (E1) line. This is done by using  `Time Division Multiplexing` (TDM). TDM divides the transmission opportunities into slots. In the telephone network, a slot corresponds to 125 microseconds. A position inside each slot is reserved for each voice signal. The figure below illustrates TDM on a link that is used to carry four voice conversations. The vertical lines represent the slot boundaries and the letters the different voice conversations. One byte from each voice conversation is sent during each 125 microseconds slot. The byte corresponding to a given conversation is always sent at the same position in each slot.

El `Multiplexado por División en Tiempo` (`Time Division Multiplexing`, TDM) es un método de asignación estática que inicialmente fue definido para la red telefónica. En la red de telefonía fija, una conversación de voz normalmente se transmite como una señal de 64 Kbps. Así, una conversación telefónica genera 8 KBytes de datos por segundo, o sea un byte cada 125 microsegundos. Las conversaciones telefónicas frecuentemente necesitan ser multiplexadas sobre una sola línea. Por ejemplo, en Europa, treinta señales de voz de 64 Kbps se multiplexan sobre una única línea de 2 Mbps (llamada E1). Esto se hace usando `Multiplexado por División en Tiempo` (TDM). Esta técnica divide las oportunidades de transmisión en ranuras (`slots`). En la red telefónica, una ranura corresponde a 125 microsegundos. Para cada señal de voz se reserva una posición dentro de cada ranura. La figura siguiente ilustra TDM sobre un enlace que es usado para transportar cuatro conversaciones de voz. Las líneas verticales representan los límites de la ranura, y las letras, las diferentes conversaciones. De cada conversación de voz se envía un byte durante cada ranura de 125 microsegundos. El byte que corresponde a una conversación dada siempre se envía en la misma posición en cada ranura.


.. figure:: png/lan-fig-012-c.png
   :align: center
   :scale: 70

   Multiplexado por División en Tiempo

..   Time-division multiplexing 


.. TDM as shown above can be completely static, i.e. the same conversations always share the link, or dynamic. In the latter case, the two endpoints of the link must exchange messages specifying which conversation uses which byte inside each slot. Thanks to these signalling messages, it is possible to dynamically add and remove voice conversations from a given link. 

Tal como se lo ha mostrado anteriormente, TDM puede ser completamente estático, es decir, siempre las mismas conversaciones compartiendo el enlace, o dinámico. En el último caso, los dos puntos extremos del enlace deben intercambiar mensajes especificando qué conversación usa cuál byte dentro de cada ranura. Gracias a estos mensajes de señalización, es posible dinámicamente agregar y eliminar conversaciones de voz de un enlace dado.

.. TDM and FDM are widely used in telephone networks to support fixed bandwidth conversations. Using them in Local Area Networks that support computers would probably be inefficient. Computers usually do not send information at a fixed rate. Instead, they often have an on-off behaviour. During the on period, the computer tries to send at the highest possible rate, e.g. to transfer a file. During the off period, which is often much longer than the on period, the computer does not transmit any packet. Using a static allocation scheme for computers attached to a LAN would lead to huge inefficiencies, as they would only be able to transmit at :math:`\frac{1}{N}` of the total bandwidth during their on period, despite the fact that the other computers are in their off period and thus do not need to transmit any information. The dynamic MAC algorithms discussed in the remainder of this chapter aim solve this problem.

TDM y FDM son ampliamente usados en redes telefónicas para soportar conversaciones de ancho de banda fijo. Usarlos en LANs que soportan computadoras probablemente sería ineficiente. Las computadoras generalmente no envían información a tasa fija. En su lugar, frecuentemente tienen comportamiento irregular. Durante el período de actividad, la computadora trata de enviar a la velocidad más alta posible; por ejemplo, para enviar un archivo. Durante el período de inactividad, que con frecuencia es mucho más largo que el de actividad, la computadora no transmite paquete alguno. Usar un esquema de asignación estático para computadoras conectadas a una LAN llevaría a enormes ineficiencias, ya que sólo podrían transmitir a :math:`\frac{1}{N}` del ancho de banda total durante su período de actividad, a pesar del hecho de que las demás computadoras estarían en su período sin actividad y así no necesitarían transmitir información alguna. Los algoritmos MAC dinámicos discutidos en el resto de este capítulo intentan resolver este problema.

ALOHA
=====

.. index:: packet radio

.. In the 1960s, computers were mainly mainframes with a few dozen terminals attached to them. These terminals were usually in the same building as the mainframe and were directly connected to it. In some cases, the terminals were installed in remote locations and connected through a :term:`modem` attached to a :term:`dial-up  line`. The university of Hawaii chose a different organisation. Instead of using telephone lines to connect the distant terminals, they developed the first `packet radio` technology [Abramson1970]_. Until then, computer networks were built on top of either the telephone network or physical cables. ALOHANet showed that it was possible to use radio signals to interconnect computers.

En los años 60, las computadoras eran principalmente `mainframes` con docenas de terminales conectados a ellos. Estos terminales generalmente estaban en el mismo edificio que el mainframe y estaban directamente conectados a él. En algunos casos, los terminales estaban instalados en ubicaciones remotas y conectados a través de un :term:`modem` conectado a una :term:`línea discada` (:term:`dial-up line`). La Universidad de Hawaii eligió una organización diferente. En lugar de usar líneas telefónicas para conectar los terminales distantes, desarrollaron la primera tecnología de `packet radio` [Abramson1970]_. Hasta ese momento, las redes de computadoras se construían, o bien encima de la red telefónica, o bien sobre cableado físico. La red ALOHANet mostró que era posible usar señales de radio para interconectar computadoras. 

.. index:: ALOHA

.. The first version of ALOHANet, described in [Abramson1970]_, operated as follows: First, the terminals and the mainframe exchanged fixed-length frames composed of 704 bits. Each frame contained 80 8-bit characters, some control bits and parity information to detect transmission errors. Two channels in the 400 MHz range were reserved for the operation of ALOHANet. The first channel was used by the mainframe to send frames to all terminals. The second channel was shared among all terminals to send frames to the mainframe. As all terminals share the same transmission channel, there is a risk of collision. To deal with this problem as well as transmission errors, the mainframe verified the parity bits of the received frame and sent an acknowledgement on its channel for each correctly received frame. The terminals on the other hand had to retransmit the unacknowledged frames. As for TCP, retransmitting these frames immediately upon expiration of a fixed timeout is not a good approach as several terminals may retransmit their frames at the same time leading to a network collapse. A better approach, but still far from perfect, is for each terminal to wait a random amount of time after the expiration of its retransmission timeout. This avoids synchronisation among multiple retransmitting terminals. 

La primera versión de ALOHANet, descrita en [Abramson1970]_, operaba como sigue. Los terminales y el mainframe intercambiaban tramas de tamaño fijo compuestas de 704 bits. Cada trama contenía 80 caracteres de 8 bits, algunos bits de control e información de paridad para detectar errores de transmisión. Se reservaban dos canales en el rango de 400 MHz para la operación de ALOHANet. El primer canal era usado por el mainframe para enviar tramas a todos los terminales. El segundo canal era compartido entre todos los terminales para enviar tramas al mainframe. Como todos los terminales compartían el mismo canal de transmisión, existía riesgo de colisión. Para tratar este problema, a la vez que los errores de transmisión, el mainframe verificaba los bits de paridad de la trama recibida, y enviaba un reconocimiento sobre su canal por cada trama recibida correctamente. Los terminales, por su parte, debían retransmitir las tramas que no recibían reconocimiento. En cuanto a TCP, retransmitir estas tramas inmediatamente, al expirar un tiempo de vencimiento fijo o `timeout`, no es buena estrategia, ya que muchos terminales pueden retransmitir sus tramas simultáneamente llevando la red a un colapso. Una mejor idea, aunque aún lejos de ser perfecta, es que cada terminal espere una cantidad aleatoria de tiempo luego de la expiración de su tiempo de retransmisión. Esto evita la sincronización entre múltiples terminales que retransmiten. 

.. The pseudo-code below shows the operation of an ALOHANet terminal. We use this python syntax for all Medium Access Control algorithms described in this chapter. The algorithm is applied to each new frame that needs to be transmitted. It attempts to transmit a frame at most `max` times (`while loop`). Each transmission attempt is performed as follows: First, the frame is sent. Each frame is protected by a timeout. Then, the terminal waits for either a valid acknowledgement frame or the expiration of its timeout. If the terminal receives an acknowledgement, the frame has been delivered correctly and the algorithm terminates. Otherwise, the terminal waits for a random time and attempts to retransmit the frame. 

El pseudocódigo que aparece más abajo muestra la operación de un terminal ALOHANet. Usamos esta sintaxis de Python para todos los algoritmos de Control de Acceso al Medio descritos en este capítulo. El algoritmo se aplica a cada nueva trama que se necesita transmitir. Se intenta transmitir una trama a lo sumo `max` veces (en el lazo `while`). Cada intento de transmisión se ejecuta como sigue: primero se envía la trama; cada trama es protegida por un `timeout`. Luego, el terminal espera, o bien un reconocimiento válido de la trama, o bien la expiración del `timeout`. Si el terminal recibe un reconocimiento, la trama ha sido entregada corrrectamente, y el algoritmo termina. De otro modo, el terminal espera un tiempo aleatorio y luego reintenta la transmisión de la trama.

.. code-block:: python

 # ALOHA
 N=1
 while N<= max :
    send(trama)
    wait(ack_sobre_canal_de_regreso or timeout)
    if (ack_sobre_canal_de_regreso):
       	break  # la transmisión fue exitosa
    else:
	# timeout 
	wait(tiempo_aleatorio)
	N=N+1
  else:		
    # Demasiados intentos de transmisión

.. 
  # ALOHA
  N=1
  while N<= max :
    send(frame)
    wait(ack_on_return_channel or timeout)
    if (ack_on_return_channel):
       	break  # transmission was successful
    else:
	# timeout 
	wait(random_time)
	N=N+1
   else:		
    # Too many transmission attempts

.. [Abramson1970]_ analysed the performance of ALOHANet under particular assumptions and found that ALOHANet worked well when the channel was lightly loaded. In this case, the frames are rarely retransmitted and the `channel traffic`, i.e. the total number of (correct and retransmitted) frames transmitted per unit of time is close to the `channel utilization`, i.e. the number of correctly transmitted frames per unit of time. Unfortunately, the analysis also reveals that the `channel utilization` reaches its maximum at :math:`\frac{1}{2 \times e}=0.186` times the channel bandwidth. At higher utilization, ALOHANet becomes unstable and the network collapses due to collided retransmissions.

Abramson [Abramson1970]_ analizó el rendimiento de ALOHANet bajo suposiciones generales, y halló que ALOHANet funcionaba bien cuando la carga del canal era liviana. En este caso, las tramas rara vez son retransmitidas, y el `tráfico del canal`, es decir, la cantidad total de tramas (correctas y retransmitidas) transmitidas por unidad de tiempo se acerca a la `utilización del canal`, es decir, a la cantidad de tramas correctamente transmitidas por unidad de tiempo. Desafortunadamente, el análisis también revela que la `utilización del canal` alcanza su máximo a :math:`\frac{1}{2 \times e}=0.186` veces el ancho de banda del canal. A utilizaciones mayores, ALOHANet se vuelve inestable y la red colapsa debido a retransmisiones con colisiones.

.. .. note:: Amateur packet radio

.. Packet radio technologies have evolved in various directions since the first experiments performed at the University of Hawaii. The Amateur packet radio service developed by amateur radio operators is one of the descendants ALOHANet. Many amateur radio operators are very interested in new technologies and they often spend countless hours developing new antennas or transceivers. When the first personal computers appeared, several amateur radio operators designed radio modems and their own datalink layer protocols [KPD1985]_ [BNT1997]_. This network grew and it was possible to connect to servers in several European countries by only using packet radio relays. Some amateur radio operators also developed TCP/IP protocol stacks that were used over the packet radio service. Some parts of the `amateur packet radio network <http://www.ampr.org/>`_ are connected to the global Internet and use the `44.0.0.0/8` prefix. 

.. note:: Packet radio amateur 

 Las tecnologías de `packet radio` han evolucionado en varias direcciones desde los primeros experimentos llevados a cabo en la Universidad de Hawaii. El servicio `packet radio amateur` desarrollado por radiooperadores aficionados es uno de los descendientes de ALOHANet. Muchos radioaficionados se interesan en nuevas tecnologías y pasan incontables horas desarrollando nuevas antenas o transmisores. Cuando aparecieron las primeras computadoras personales, varios radioaficionados diseñaron modems de radio y sus propios protocolos de capa de enlace de datos [KPD1985]_ [BNT1997]_. Esta red creció, y fue posible conectarse a servidores en varios países europeos usando sólo `relays` de packet radio. Algunos radioaficionados también desarrollaron pilas de protocolos TCP/IP que fueron usadas sobre el servicio de packet radio. Algunas porciones de la `red amateur de packet radio <http://www.ampr.org/>`_ están conectadas a la Internet global y usan el prefijo `44.0.0.0/8`.

.. index:: slotted ALOHA, ALOHA ranurado

.. Many improvements to ALOHANet have been proposed since the publication of [Abramson1970]_, and this technique, or some of its variants, are still found in wireless networks today. The slotted technique proposed in [Roberts1975]_ is important because it shows that a simple modification can significantly improve channel utilization. Instead of allowing all terminals to transmit at any time, [Roberts1975]_ proposed to divide time into slots and allow terminals to transmit only at the beginning of each slot. Each slot corresponds to the time required to transmit one fixed size frame. In practice, these slots can be imposed by a single clock that is received by all terminals. In ALOHANet, it could have been located on the central mainframe. The analysis in [Roberts1975]_ reveals that this simple modification improves the channel utilization by a factor of two. 

Se han propuesto múltiples mejoras a ALOHANet desde la publicación de [Abramson1970]_, y esta técnica, o algunas de sus variantes, aún se encuentran en las redes inalámbricas de hoy. La técnica ranurada propuesta en [Roberts1975]_ es importante porque muestra que una modificación simple puede mejorar significativamente la utilización del canal. En lugar de permitir que todos los terminales transmitieran en cualquier momento, [Roberts1975]_ propuso dividir el tiempo en ranuras, y permitir a los terminales transmitir únicamente al principio de cada ranura. Cada ranura corresponde al tiempo requerido para transmitir una trama de tamaño fijo. En la prácica, estas ranuras pueden ser impuestas por un reloj único, cuya señal sea recibida por todos los terminales. En ALOHANet, este reloj podría haber sido ubicado en el mainframe central. El análisis en [Roberts1975]_ revela que esta sencilla modificación mejora la utilización del canal por un factor de 2.

.. index:: CSMA, Carrier Sense Multiple Access


Acceso Múltiple por Sensado de Portadora (CSMA)
===============================================


.. ALOHA and slotted ALOHA can easily be implemented, but unfortunately, they can only be used in networks that are very lightly loaded. Designing a network for a very low utilisation is possible, but it clearly increases the cost of the network. To overcome the problems of ALOHA, many Medium Access Control mechanisms have been proposed which improve channel utilization. Carrier Sense Multiple Access (CSMA) is a significant improvement compared to ALOHA. CSMA requires all nodes to listen to the transmission channel to verify that it is free before transmitting a frame [KT1975]_. When a node senses the channel to be busy, it defers its transmission until the channel becomes free again. The pseudo-code below provides a more detailed description of the operation of CSMA. 

ALOHA y ALOHA ranurado pueden ser fácilmente implementados, pero, desafortunadamente, sólo pueden ser usados en redes con carga sumamente liviana. Diseñar una red para una utilización muy baja es posible, pero claramente incrementa el costo de la red. Para superar los problemas de ALOHA, se han propuesto muchos mecanismos de control de acceso al medio que mejoran la utilización del canal. El método de `Acceso Múltiple por Sensado de Portadora` (`Carrier Sense Multiple Access`, CSMA) es una mejora significativa comparada con ALOHA. CSMA requiere que todos los nodos escuchen el canal de transmisión para verificar que esté libre antes de transmitir una trama [KT1975]_. Cuando un nodo detecta que el canal está ocupado, difiere su transmisión hasta que el canal quede libre nuevamente. El pseudocódigo más abajo ofrece una descripción más detallada de la operación de CSMA.

.. index:: persistent CSMA, CSMA (persistent), CSMA persistente

.. code-block:: text

  # CSMA persistente
  N=1
  while N<= max :
    wait(canal_libre)
    send(trama)
    wait(reconocimiento or timeout)
    if reconocimiento :
       	break  # la transmisión fue exitosa
    else :
	# timeout 
	N=N+1
  # fin del lazo while
    # Demasiados intentos de transmisión

.. 
  # persistent CSMA
  N=1
  while N<= max :
    wait(channel_becomes_free)
    send(frame)
    wait(ack or timeout)
    if ack :
       	break  # transmission was successful
    else :
	# timeout 
	N=N+1
  # end of while loop 
    # Too many transmission attempts

.. The above pseudo-code is often called `persistent CSMA` [KT1975]_ as the terminal will continuously listen to the channel and transmit its frame as soon as the channel becomes free. Another important variant of CSMA is the `non-persistent CSMA` [KT1975]_. The main difference between persistent and non-persistent CSMA described in the pseudo-code below is that a non-persistent CSMA node does not continuously listen to the channel to determine when it becomes free. When a non-persistent CSMA terminal senses the transmission channel to be busy, it waits for a random time before sensing the channel again. This improves channel utilization compared to persistent CSMA. With persistent CSMA, when two terminals sense the channel to be busy, they will both transmit (and thus cause a collision) as soon as the channel becomes free. With non-persistent CSMA, this synchronisation does not occur, as the terminals wait a random time after having sensed the transmission channel. However, the higher channel utilization achieved by non-persistent CSMA comes at the expense of a slightly higher waiting time in the terminals when the network is lightly loaded. 

El pseudocódigo mostrado anteriormente se llama a veces `CSMA persistente` [KT1975]_, porque el terminal escuchará continuamente el canal, y transmitirá su trama tan pronto como el canal quede libre. Otra variante importante de CSMA es el `CSMA no persistente` [KT1975]_. La principal diferencia entre ambas variantes es que un nodo CSMA no persistente `no` escucha continuamente el canal para determinar cuándo queda libre; sino que, cuando el canal está ocupado, espera un intervalo de tiempo aleatorio para volver a sensar. Esto mejora la utilización del canal en comparación al CSMA persistente. Con CSMA persistente, cuando dos terminales perciben canal ocupado, apenas el canal queda libre, ambos comienzan a transmitir (causando así una colisión). Con CSMA no persistente, esta sincronización no ocurre, ya que los terminales esperan un tiempo aleatorio luego de haber sensado el canal de transmisión. Sin embargo, la utilización más alta alcanzada por el CSMA no persistente viene al costo de un tiempo de espera algo mayor en los terminales cuando la red está ligeramente cargada.

.. index:: non-persistent CSMA, CSMA (non-persistent), CSMA no persistente

.. code-block:: text

 # CSMA no persistente
 N=1
 while N <= max :
    listen(canal)
    if free(canal):
       send(trama)	
       wait(reconocimiento or timeout)
       if reconocimiento :
       	  break  # la transmisión fue exitosa
       else :
	  # timeout 
	  N=N+1
    else:
       wait(tiempo_aleatorio)
  # fin del lazo while
    # Demasiados intentos de transmisión
.. 
 # Non persistent CSMA
 N=1
 while N<= max :
    listen(channel)
    if free(channel):
       send(frame)	
       wait(ack or timeout)
       if received(ack) :
       	  break  # transmission was successful
       else :
	  # timeout 
	  N=N+1
    else:
       wait(random_time)
  # end of while loop		
    # Too many transmission attempts

.. [KT1975]_ analyzes in detail the performance of several CSMA variants. Under some assumptions about the transmission channel and the traffic, the analysis compares ALOHA, slotted ALOHA, persistent and non-persistent CSMA. Under these assumptions, ALOHA achieves a channel utilization of only 18.4% of the channel capacity. Slotted ALOHA is able to use 36.6% of this capacity. Persistent CSMA improves the utilization by reaching 52.9% of the capacity while non-persistent CSMA achieves 81.5% of the channel capacity. 

[KT1975]_ analiza en detalle el rendimiento de varias variantes CSMA. Bajo algunas suposiciones sobre el canal de transmisión y sobre el tráfico, el análisis compara ALOHA, ALOHA ranurado, CSMA persistente y CSMA no persistente. Bajo estas suposiciones, ALOHA alcanza una utilización del canal de sólo 18.4% de la capacidad. ALOHA ranurado es capaz de usar 36.6% de esta capacidad. CSMA persistente mejora la utilización alcanzando 52.9% de la capacidad del canal, mientras que CSMA no persistente logra utilizar 81.5% de la capacidad. 

.. index:: Carrier Sense Multiple Access with Collision Detection, CSMA/CD

Acceso Múltiple por Sensado de Portadora con Detección de Colisiones (CSMA/CD)
==============================================================================


.. .. index:: speed of light
.. index:: velocidad de la luz

.. CSMA improves channel utilization compared to ALOHA. However, the performance can still be improved, especially in wired networks. Consider the situation of two terminals that are connected to the same cable. This cable could, for example, be a coaxial cable as in the early days of Ethernet [Metcalfe1976]_. It could also be built with twisted pairs. Before extending CSMA, it is useful to understand more intuitively, how frames are transmitted in such a network and how collisions can occur. The figure below illustrates the physical transmission of a frame on such a cable. To transmit its frame, host A must send an electrical signal on the shared medium. The first step is thus to begin the transmission of the electrical signal. This is point `(1)` in the figure below. This electrical signal will travel along the cable. Although electrical signals travel fast, we know that information cannot travel faster than the speed of light (i.e. 300.000 kilometers/second). On a coaxial cable, an electrical signal is slightly slower than the speed of light and 200.000 kilometers per second is a reasonable estimation. This implies that if the cable has a length of one kilometer, the electrical signal will need 5 microseconds to travel from one end of the cable to the other. The ends of coaxial cables are equipped with termination points that ensure that the electrical signal is not reflected back to its source. This is illustrated at point `(3)` in the figure, where the electrical signal has reached the left endpoint and host B. At this point, B starts to receive the frame being transmitted by A. Notice that there is a delay between the transmission of a bit on host A and its reception by host B. If there were other hosts attached to the cable, they would receive the first bit of the frame at slightly different times. As we will see later, this timing difference is a key problem for MAC algorithms. At point `(4)`, the electrical signal has reached both ends of the cable and occupies it completely. Host A continues to transmit the electrical signal until the end of the frame. As shown at point `(5)`, when the sending host stops its transmission, the electrical signal corresponding to the end of the frame leaves the coaxial cable. The channel becomes empty again once the entire electrical signal has been removed from the cable.

CSMA mejora la utilización del canal respecto de ALOHA. Sin embargo, el rendimiento aún puede mejorarse, especialmente en redes cableadas. Consideremos la situación de dos terminales que se conectan al mismo cable. Este medio podría ser, por ejemplo, un cable coaxil como en los primeros días de Ethernet [Metcalfe1976]_; también podría estar realizado con par trenzado. Antes de extender CSMA, es útil comprender más intuitivamente cómo se transmiten las tramas en una red así, y cómo pueden ocurrir las colisiones. La figura más abajo ilustra la transmisión física de una trama en dicho cable. Para transmitir su trama, el nodo A debe enviar una señal eléctrica sobre el medio compartido. El primer paso es entonces comenzar la transmisión de la señal eléctrica. Éste es el punto `(1)` en la figura. Esta señal eléctrica viajará por el cable. Aunque las señales eléctricas se desplazan rápidamente, sabemos que la información no puede viajar más rápido que la luz (o sea, 300.000 Km/s). Sobre un cable coaxil, una señal eléctrica es ligeramente más lenta, y una estimación razonable será de unos 200.000 Km/s. Esto implica que si el cable tiene una longitud de un kilómetro, la señal eléctrica necesitará 5 microsegundos para viajar de un extremo del cable al opuesto. Las puntas del cable coaxil está equipadas con terminadores, que aseguran que la señal no se refleje de vuelta hacia el origen. Esto se ilustra en el punto `(3)` de la figura, donde la señal eléctrica ha alcanzado al extremo izquierdo y al nodo B. En este punto, B comienza a recibir la trama que A está transmitiendo. Nótese que hay una demora entre la transmisión de un bit por el nodo A y su recepción en el nodo B. Si hubiera otros nodos conectados al cable, recibirían el primer bit de la trama en momentos levemente diferentes. Como veremos más tarde, esta diferencia en tiempos es un problema clave para los algoritmos MAC. En el punto `(4)`, la señal eléctrica ha alcanzado ambos extremos del cable y lo ocupa completamente. El nodo A continúa transmitiendo la señal eléctrica hasta el final de la trama. Como se muestra en el punto `(5)`, cuando el nodo emisor detiene su transmisión, la señal eléctrica correspondiente al fin de la trama abandona el cable coaxil. El canal queda vacío nuevamente, una vez que la señal eléctrica completa ha sido retirada del cable.

.. figure:: png/lan-fig-024-c.png
   :align: center
   :scale: 70

   Transmisión de una trama sobre un medio compartido 

..   Frame transmission on a shared bus 

.. Now that we have looked at how a frame is actually transmitted as an electrical signal on a shared bus, it is interesting to look in more detail at what happens when two hosts transmit a frame at almost the same time. This is illustrated in the figure below, where hosts A and B start their transmission at the same time (point `(1)`). At this time, if host C senses the channel, it will consider it to be free. This will not last a long time and at point `(2)` the electrical signals from both host A and host B reach host C. The combined electrical signal (shown graphically as the superposition of the two curves in the figure) cannot be decoded by host C. Host C detects a collision, as it receives a signal that it cannot decode. Since host C cannot decode the frames, it cannot determine which hosts are sending the colliding frames. Note that host A (and host B) will detect the collision after host C (point `(3)` in the figure below).

Ahora que hemos visto de qué manera se transmite una trama como una señal eléctrica sobre un bus compartido, es interesante ver en mayor detalle qué ocurre cuando dos nodos transmiten una trama casi al mismo tiempo. Esto se ilustra en la figura más abajo, donde los nodos A y B comienzan su transmisión en el mismo momento (punto `(1)`). En este momento, si el nodo C sensa el canal, lo considerará libre. Esto no durará mucho tiempo, y en el punto `(2)` las señales eléctricas de los nodos A y B alcanzarán a C. La señal eléctrica combinada (mostrada gráficamente como la superposición de las dos curvas en la figura) no puede ser decodificada por el nodo C. El nodo C detecta una colisión, ya que recibe una señal que no puede decodificar. Como el nodo C no puede decodificar las tramas, no puede determinar qué nodos están enviando las tramas que han colisionado. Nótese que el nodo A (y el nodo B) detectarán la colisión luego del nodo C (punto `(3)` en la figura abajo).

.. figure:: png/lan-fig-025-c.png
   :align: center
   :scale: 70
  
   Colisión de tramas en un medio compartido 
..   Frame collision on a shared bus 



.. index:: collision detection, jamming, detección de colisiones

.. As shown above, hosts detect collisions when they receive an electrical signal that they cannot decode. In a wired network, a host is able to detect such a collision both while it is listening (e.g. like host C in the figure above) and also while it is sending its own frame. When a host transmits a frame, it can compare the electrical signal that it transmits with the electrical signal that it senses on the wire. At points `(1)` and `(2)` in the figure above, host A senses only its own signal. At point `(3)`, it senses an electrical signal that differs from its own signal and can thus detects the collision. At this point, its frame is corrupted and it can stop its transmission. The ability to detect collisions while transmitting is the starting point for the `Carrier Sense Multiple Access with Collision Detection (CSMA/CD)` Medium Access Control algorithm, which is used in Ethernet networks [Metcalfe1976]_ [802.3]_ . When an Ethernet host detects a collision while it is transmitting, it immediately stops its transmission. Compared with pure CSMA, CSMA/CD is an important improvement since when collisions occur, they only last until colliding hosts have detected it and stopped their transmission. In practice, when a host detects a collision, it sends a special jamming signal on the cable to ensure that all hosts have detected the collision.

Como se vio más arriba, los nodos detectan colisiones cuando reciben una señal eléctrica que no pueden decodificar. En una red cableada, un nodo es capaz de detectar una tal colisión en dos ocasiones: mientras está escuchando (como, por ejemplo, el nodo C en la figura anterior) y mientras está enviando su propia trama. Mientras un nodo transmite una trama, puede comparar la señal eléctrica que transmite con la señal que sensa sobre el cable. En los puntos `(1)` y `(2)` en la figura anterior, el nodo A sensa únicamente su señal. En el punto `(3)`, sensa una señal eléctrica que difiere de su propia señal, y puede así detectar la colisión. En este punto, su trama está corrupta y puede detener su transmisión. La capacidad de detectar colisiones mientras se transmite es el punto de partida para el algoritmo de control de acceso al medio CSMA/CD, que es el usado en las redes Ethernet [Metcalfe1976]_ [802.3]_. Cuando un nodo detecta una colisión mientras está transmitiendo, inmediatamente detiene su transmisión. Comparado con CSMA puro, CSMA/CD es una mejora importante, ya que cuando ocurran colisiones, éstas durarán sólo hasta que los nodos que colisionan la hayan detectado y hayan detenido su transmisión. En la práctica, cuando un nodo detecta una colisión, envía una señal especial de `jamming` sobre el cable para asegurar que todos los nodos sepan de la colisión.

.. To better understand these collisions, it is useful to analyse what would be the worst collision on a shared bus network. Let us consider a wire with two hosts attached at both ends, as shown in the figure below. Host A starts to transmit its frame and its electrical signal is propagated on the cable. Its propagation time depends on the physical length of the cable and the speed of the electrical signal. Let us use :math:`\tau` to represent this propagation delay in seconds. Slightly less than :math:`\tau` seconds after the beginning of the transmission of A's frame, B decides to start transmitting its own frame. After :math:`\epsilon` seconds, B senses A's frame, detects the collision and stops transmitting. The beginning of B's frame travels on the cable until it reaches host A. Host A can thus detect the collision at time :math:`\tau-\epsilon+\tau \approx 2\times\tau`. An important point to note is that a collision can only occur during the first :math:`2\times\tau` seconds of its transmission. If a collision did not occur during this period, it cannot occur afterwards since the transmission channel is busy after :math:`\tau` seconds and CSMA/CD hosts sense the transmission channel before transmitting their frame. 

Para comprender mejor estas colisiones, es útil analizar lo que sería la peor colisión sobre una red de bus compartido. Consideremos un cable con dos nodos conectados en ambos extremos, como se muestra en la figura siguiente. El nodo A comienza a transmitir su trama, y su señal eléctrica se propaga por el cable. Su tiempo de propagación depende de la longitud física del cable y de la velocidad de la señal eléctrica. Usemos la notación :math:`\tau` para representar este retardo de propagación en segundos. Poco menos de  :math:`\tau` segundos luego del comienzo de la transmisión de la trama de A, B decide comenzar a transmitir su propia trama. Luego de :math:`\epsilon` segundos, B sensa la trama de A, detecta la colisión y detiene su transmisión. El comienzo de la trama de B viaja por el cable hasta que alcanza al nodo A. El nodo A entonces puede detectar la colisión en el momento :math:`\tau-\epsilon+\tau \approx 2\times\tau`. Un punto importante a notar es que una colisión sólo puede ocurrir durante los primeros  :math:`2\times\tau` segundos de la transmisión. Si la colisión no ocurriera durante este período, no podrá ocurrir más tarde, ya que el canal de transmisión está ocupado luego de :math:`\tau` segundos, y los nodos CSMA/CD sensan el canal de transmisión antes de transmitir su trama.

.. figure:: png/lan-fig-027-c.png
   :align: center
   :scale: 70
   
   La peor colisión en un bus compartido
..   The worst collision on a shared bus


.. Furthermore, on the wired networks where CSMA/CD is used, collisions are almost the only cause of transmission errors that affect frames. Transmission errors that only affect a few bits inside a frame seldom occur in these wired networks. For this reason, the designers of CSMA/CD chose to completely remove the acknowledgement frames in the datalink layer. When a host transmits a frame, it verifies whether its transmission has been affected by a collision. If not, given the negligible Bit Error Ratio of the underlying network, it assumes that the frame was received correctly by its destination. Otherwise the frame is retransmitted after some delay.

En las redes cableadas donde se usa CSMA/CD, las colisiones son casi la única causa de errores de transmisión que afectan a las tramas. Los errores de transmisión que sólo afectan a unos pocos bits dentro de una trama ocurren raramente en estas redes cableadas. Por esta razón, los diseñadores de CSMA/CD eligieron eliminar completamente las tramas de reconocimiento en la capa de Enlace de Datos. Cuando un nodo transmite una trama, verifica si su transmisión ha sido afectada por una colisión. Si no ha sido así, dada la despreciable tasa de error de bits (`Bit Error Ratio`, BER) de la red subyacente, asume que la trama fue correctamente recibida por su destinatario. De otro modo, la trama será retransmitida luego de una cierta demora.

.. Removing acknowledgements is an interesting optimisation as it reduces the number of frames that are exchanged on the network and the number of frames that need to be processed by the hosts. However, to use this optimisation, we must ensure that all hosts will be able to detect all the collisions that affect their frames. The problem is important for short frames. Let us consider two hosts, A and B, that are sending a small frame to host C as illustrated in the figure below. If the frames sent by A and B are very short, the situation illustrated below may occur. Hosts A and B send their frame and stop transmitting (point `(1)`). When the two short frames arrive at the location of host C, they collide and host C cannot decode them (point `(2)`). The two frames are absorbed by the ends of the wire. Neither host A nor host B have detected the collision. They both consider their frame to have been received correctly by its destination.

Eliminar los reconocimientos es una optimización interesante, ya que reduce el número de tramas que se intercambian sobre la red, y el número de tramas que los nodos necesitan procesar. Sin embargo, para usar esta optimización, debemos asegurar que todos los nodos sean capaces de detectar todas las colisiones que afecten a sus tramas. El problema es importante para las tramas cortas. Consideremos dos nodos, A y B, que están enviando una trama pequeña al nodo C, como se ilustra en la figura más abajo. Si las tramas enviadas por A y B son muy cortas, puede darse la situación ilustrada. Los nodos A y B envían su trama y detienen su transmisión (punto `(1)`). Cuando las dos tramas cortas llegan al nodo C, colisionan, y el nodo C no puede decodificarlas (punto `(2)`). Las dos tramas son absorbidas por los extremos del cable. Ni el nodo A ni el nodo B han detectado la colisión. Ambos consideran que su trama ha sido correctamente recibida por el destinatario.

.. figure:: png/lan-fig-026-c.png
   :align: center
   :scale: 70

   El problema de la colisión de tramas cortas 
..   The short-frame collision problem



.. index:: slot time (Ethernet)


.. To solve this problem, networks using CSMA/CD require hosts to transmit for at least :math:`2\times\tau` seconds. Since the network transmission speed is fixed for a given network technology, this implies that a technology that uses CSMA/CD enforces a minimum frame size. In the most popular CSMA/CD technology, Ethernet, :math:`2\times\tau` is called the `slot time` [#fslottime]_. 

Para resolver este problema, las redes que usan CSMA/CD requieren que los nodos transmitan durante al menos :math:`2\times\tau` segundos. Como la velocidad de transmisión de la red para una tecnología de red dada es fija, esto implica que una tecnología que use CSMA/CD impondrá un tamaño de trama mínimo. En la tecnología CSMA/CD más popular, Ethernet, :math:`2\times\tau` es llamado el `tiempo de ranura` (`slot time`) [#fslottime]_. 



.. index:: binary exponential back-off (CSMA/CD), back-off exponencial

.. The last innovation introduced by CSMA/CD is the computation of the retransmission timeout. As for ALOHA, this timeout cannot be fixed, otherwise hosts could become synchronised and always retransmit at the same time. Setting such a timeout is always a compromise between the network access delay and the amount of collisions. A short timeout would lead to a low network access delay but with a higher risk of collisions. On the other hand, a long timeout would cause a long network access delay but a lower risk of collisions. The `binary exponential back-off` algorithm was introduced in CSMA/CD networks to solve this problem.

La innovación final introducida por CSMA/CD es el cómputo del `timeout` de retransmisión. Como ocurre en ALOHA, este tiempo no puede ser fijo, ya que los nodos quedarían sincronizados y retransmitirían siempre al mismo tiempo. Establecer cuál será el tiempo de timeout es siempre un compromiso entre el retardo de acceso a la red y la cantidad de colisiones. Un timeout corto llevaría a un bajo retardo de acceso a la red, pero con un riesgo más alto de colisiones. Por el otro lado, un timeout largo causaría un retardo de acceso a la red alto, pero un riesgo menor de colisiones. El algoritmo de `back-off exponencial binario` fue introducido en las redes CSMA/CD para resolver este problema.

.. To understand `binary exponential back-off`, let us consider a collision caused by exactly two hosts. Once it has detected the collision, a host can either retransmit its frame immediately or defer its transmission for some time. If each colliding host flips a coin to decide whether to retransmit immediately or to defer its retransmission, four cases are possible :

Para comprender el `back-off exponencial binario` consideremos una colisión causada por exactamente dos nodos. Una vez que ha detectado la colisión, un nodo puede, o bien retransmitir su trama inmediatamente, o diferir su transmisión por algún tiempo. Si cada nodo que colisiona arroja una moneda para decidir si retransmitir inmediatamente o diferir su transmisión, caben cuatro casos posibles:

 1. Ambos nodos retransmiten inmediatamente y ocurre una nueva colisión.
 2. El primer nodo retransmite inmediatamente y el segundo difiere su transmisión.
 3. El primer nodo difiere su transmisión y el segundo retransmite inmediatamente.
 4. Ambos nodos difieren su transmisión y ocurre una nueva colisión.

.. 
 1. Both hosts retransmit immediately and a new collision occurs
 2. The first host retransmits immediately and the second defers its retransmission
 3. The second host retransmits immediately and the first defers its retransmission
 4. Both hosts defer their retransmission and a new collision occurs

.. In the second and third cases, both hosts have flipped different coins. The delay chosen by the host that defers its retransmission should be long enough to ensure that its retransmission will not collide with the immediate retransmission of the other host. However the delay should not be longer than the time necessary to avoid the collision, because if both hosts decide to defer their transmission, the network will be idle during this delay. The `slot time` is the optimal delay since it is the shortest delay that ensures that the first host will be able to retransmit its frame completely without any collision. 

En el segundo y tercer casos, ambos nodos han arrojado diferentes monedas. El retardo elegido por el nodo que difiere su retransmisión debería ser lo bastante largo como para asegurar que su retransmisión no colisionará con la retransmisión inmediata del otro nodo. Sin embargo, el retardo no deberá ser más largo que el tiempo necesario para evitar la colisión, porque si ambos nodos deciden diferir su transmisión, la red quedará ociosa durante ese tiempo. El `tiempo de ranura` es el retardo óptimo, ya que es el retardo más corto que asegura que el primer nodo será capaz de retransmitir su trama completamente sin ninguna colisión.


.. If two hosts are competing, the algorithm above will avoid a second collision 50% of the time. However, if the network is heavily loaded, several hosts may be competing at the same time. In this case, the hosts should be able to automatically adapt their retransmission delay. The `binary exponential back-off` performs this adaptation based on the number of collisions that have affected a frame. After the first collision, the host flips a coin and waits 0 or 1 `slot time`. After the second collision, it generates a random number and waits 0, 1, 2 or 3 `slot times`, etc. The duration of the waiting time is doubled after each collision. The complete pseudo-code for the CSMA/CD algorithm is shown in the figure below. 

Si compiten dos nodos, el algoritmo descrito más arriba evitará una segunda colisión en el 50% de las veces. Sin embargo, si la red está muy cargada, varios nodos podrán estar compitiendo al mismo tiempo. En este caso, los nodos deberán ser capaces de adaptar automáticamente su retardo de retransmisión. El `back-off exponencial binario` ejecuta esta adaptación basándose en la cantidad de colisiones que han afectado a una trama. Luego de la primera colisión, el nodo arroja una moneda y espera 0 o 1 `tiempos de ranura`. Luego de la segunda colisión, genera un número aleatorio entre 0 y 3, y espera 0, 1, 2 o 3 `tiempos de ranura`, etc. La duración del tiempo de espera se duplica luego de cada colisión. El pseudocódigo completo para el algoritmo CSMA/CD se muestra en la figura siguiente. 

.. code-block:: text

 # Pseudocódigo de CSMA/CD
 N=1
 while N<= max :
    wait(canal_libre)
    send(trama)   
    wait_until (fin_de_trama) or (colisión)	
    if colisión:
	detener transmisión
	send(señal_de_jamming)
	k = min (10, N)
	r = random(0, 2k - 1) * tiempo_de_ranura
	wait(r*tiempo_de_ranura)
	N=N+1
    else :	
        wait(retardo_entre_tramas)
	break
  # fin del lazo while
    # Demasiados intentos de transmisión

.. 	
 # CSMA/CD pseudo-code
 N=1
 while N<= max :
    wait(channel_becomes_free)
    send(frame)   
    wait_until (end_of_frame) or (collision)	
    if collision detected:
	stop transmitting
	send(jamming)
	k = min (10, N)
	r = random(0, 2k - 1) * slotTime
	wait(r*slotTime)
	N=N+1
    else :	
        wait(inter-frame_delay)
	break
  # end of while loop	
    # Too many transmission attempts

.. The inter-frame delay used in this pseudo-code is a short delay corresponding to the time required by a network adapter to switch from transmit to receive mode. It is also used to prevent a host from sending a continuous stream of frames without leaving any transmission opportunities for other hosts on the network. This contributes to the fairness of CSMA/CD. Despite this delay, there are still conditions where CSMA/CD is not completely fair [RY1994]_. Consider for example a network with two hosts : a server sending long frames and a client sending acknowledgments. Measurements reported in [RY1994]_ have shown that there are situations where the client could suffer from repeated collisions that lead it to wait for long periods of time due to the exponential back-off algorithm. 

El `retardo entre tramas` (`ìnter-frame delay`) usado en este pseudocódigo es un breve retardo correspondiente al tiempo que requiere un adaptador de red para cambiar de modo transmitir a modo recibir. También se usa para evitar que un nodo envíe un flujo continuo de tramas sin dar oportunidad de transmitir a los demás nodos de la red. A pesar de este retardo, aún hay condiciones donde CSMA/CD no es completamente justo [RY1994]_. Consideremos, por ejemplo, una red con dos nodos: un servidor enviando tramas largas, y un cliente enviando reconocimientos. Las mediciones reportadas en [RY1994]_ han mostrado que hay situaciones donde el cliente podría sufrir colisiones repetidas que lo llevarían a esperar largos períodos de tiempo debido al algoritmo de `back-off exponencial binario`. 

.. .. [#fslottime] This name should not be confused with the duration of a transmission slot in slotted ALOHA. In CSMA/CD networks, the slot time is the time during which a collision can occur at the beginning of the transmission of a frame. In slotted ALOHA, the duration of a slot is the transmission time of an entire fixed-size frame.

.. [#fslottime] Este término no debe ser confundido con la duración de una ranura de transmisión en ALOHA ranurado. En redes CSMA/CD, el tiempo de ranura es el tiempo, al principio de la transmisión de una trama, durante el cual puede ocurrir una colisión. En ALOHA ranurado, la duración de una ranura es el tiempo de transmisión de una trama completa, de tamaño fijo.

.. index:: Carrier Sense Multiple Access with Collision Avoidance, CSMA/CA

Acceso Múltiple por Sensado de Portadora con Exclusión de Colisiones (CSMA/CA)
==============================================================================

.. The `Carrier Sense Multiple Access with Collision Avoidance` (CSMA/CA) Medium Access Control algorithm was designed for the popular WiFi wireless network technology [802.11]_. CSMA/CA also senses the transmission channel before transmitting a frame. Furthermore, CSMA/CA tries to avoid collisions by carefully tuning the timers used by CSMA/CA devices.

El algoritmo de control de acceso al medio `Acceso Múltiple por Sensado de Portadora con Exclusión de Colisiones` (`Carrier Sense Multiple Access with Collision Avoidance`, CSMA/CA) fue diseñado para la popular tecnología de redes inalámbricas WiFi [802.11]_. CSMA/CA también sensa el canal de transmisión antes de transmitir una trama; pero además trata de `evitar` las colisiones ajustando cuidadosamente los timers usados por los dispositivos CSMA/CA.

.. index:: Short Inter Frame Spacing, SIFS

.. CSMA/CA uses acknowledgements like CSMA. Each frame contains a sequence number and a CRC. The CRC is used to detect transmission errors while the sequence number is used to avoid frame duplication. When a device receives a correct frame, it returns a special acknowledgement frame to the sender. CSMA/CA introduces a small delay, named `Short Inter Frame Spacing`  (SIFS), between the reception of a frame and the transmission of the acknowledgement frame. This delay corresponds to the time that is required to switch the radio of a device between the reception and transmission modes.

CSMA/CA, como CSMA, usa reconocimientos. Cada trama contiene un número de secuencia y un CRC. El CRC se usa para detectar errores de transmisión, mientras que el número de secuencia se usa para evitar duplicación de tramas. Cuando un dispositivo recibe una trama correcta, devuelve una trama especial de reconocimiento al emisor. CSMA/CA introduce un pequeño retardo, llamado `Short Inter Frame Spacing`  (SIFS) entre la recepción de una trama y la transmisión de la trama de reconocimiento. Este retardo corresponde al tiempo que se requiere para cambiar de modo recepción a transmisión la radio de un dispositivo.

.. index:: Distributed Coordination Function Inter Frame Space, DIFS, Extended Inter Frame Space, EIFS

.. Compared to CSMA, CSMA/CA defines more precisely when a device is allowed to send a frame. First, CSMA/CA defines two delays : `DIFS` and `EIFS`. To send a frame, a device must first wait until the channel has been idle for at least the `Distributed Coordination Function Inter Frame Space` (DIFS) if the previous frame was received correctly. However, if the previously received frame was corrupted, this indicates that there are collisions and the device must sense the channel idle for at least the `Extended Inter Frame Space` (EIFS), with :math:`SIFS<DIFS<EIFS`. The exact values for SIFS, DIFS and EIFS depend on the underlying physical layer [802.11]_. 

Comparado con CSMA, CSMA/CA define con mayor precisión cuándo un dispositivo puede enviar una trama. CSMA/CA define dos retardos, `DIFS` y `EIFS`. Para enviar una trama, un dispositivo debe primero esperar, si la trama anterior ha sido recibida correctamente, hasta que el canal haya estado ocioso por al menos un período DIFS, `Distributed Coordination Function Inter Frame Space`. Sin embargo, si la trama anterior estaba corrupta, esto indica que hay colisiones, y el dispositivo debe percibir que el canal está ocioso por al menos un período EIFS, `Extended Inter Frame Space`, con :math:`SIFS<DIFS<EIFS`. Los valores exactos de SIFS, DIFS y EIFS dependen de la capa Física subyacente [802.11]_. 

.. The figure below shows the basic operation of CSMA/CA devices. Before transmitting, host `A` verifies that the channel is empty for a long enough period. Then, its sends its data frame. After checking the validity of the received frame, the recipient sends an acknowledgement frame after a short SIFS delay. Host `C`, which does not participate in the frame exchange, senses the channel to be busy at the beginning of the data frame. Host `C` can use this information to determine how long the channel will be busy for. Note that as :math:`SIFS<DIFS<EIFS`, even a device that would start to sense the channel immediately after the last bit of the data frame could not decide to transmit its own frame during the transmission of the acknowledgement frame.

La figura más abajo ilustra la operación básica de los dispositivos CSMA/CA. Antes de transmitir, el nodo A verifica que el canal esté vacío por un período suficientemente largo. Luego envía su trama de datos. Después de verificar la validez de la trama recibida, el receptor envía una trama de reconocimiento luego de un corto retardo SIFS. El nodo C, que no participa en el intercambio de tramas, percibe que el canal está ocupado al principio de la trama de datos. Dicho nodo puede usar esta información para determinar por cuánto tiempo estará ocupado el canal. Nótese que, como :math:`SIFS<DIFS<EIFS`, aun un dispositivo que comenzara a sensar el canal inmediatamente después del último bit de la trama, no podría decidir la transmisión de su propia trama durante la transmisión de la trama de reconocimiento.


.. figure:: svg/datalink-fig-006-c.png
   :align: center
   :scale: 70
   
   Operación de un dispositivo CSMA/CA
..   Operation of a CSMA/CA device



.. index:: slotTime (CSMA/CA)

.. The main difficulty with CSMA/CA is when two or more devices transmit at the same time and cause collisions. This is illustrated in the figure below, assuming a fixed timeout after the transmission of a data frame. With CSMA/CA, the timeout after the transmission of a data frame is very small, since it corresponds to the SIFS plus the time required to transmit the acknowledgement frame.

La principal dificultad con CSMA/CA se presenta cuando dos o más dispositivos transmiten al mismo tiempo y provocan una colisión. Esto se muestra en la figura siguiente, suponiendo un timeout fijo después de la transmisión de una trama. Con CSMA/CA, el timeout luego de la transmisión de una trama es muy pequeño, ya que corresponde al SIFS más el tiempo requerido para transmitir la trama de reconocimiento.

.. figure:: svg/datalink-fig-007-c.png
   :align: center
   :scale: 70
   
   Colisiones con CSMA/CA
..   Collisions with CSMA/CA 

.. To deal with this problem, CSMA/CA relies on a backoff timer. This backoff timer is a random delay that is chosen by each device in a range that depends on the number of retransmissions for the current frame. The range grows exponentially with the retransmissions as in CSMA/CD. The minimum range for the backoff timer is :math:`[0,7*slotTime]` where the `slotTime` is a parameter that depends on the underlying physical layer. Compared to CSMA/CD's exponential backoff, there are two important differences to notice. First, the initial range for the backoff timer is seven times larger. This is because it is impossible in CSMA/CA to detect collisions as they happen. With CSMA/CA, a collision may affect the entire frame while with CSMA/CD it can only affect the beginning of the frame. Second, a CSMA/CA device must regularly sense the transmission channel during its back off timer. If the channel becomes busy (i.e. because another device is transmitting), then the back off timer must be frozen until the channel becomes free again. Once the channel becomes free, the back off timer is restarted. This is in contrast with CSMA/CD where the back off is recomputed after each collision. This is illustrated in the figure below. Host `A` chooses a smaller backoff than host `C`. When `C` senses the channel to be busy, it freezes its backoff timer and only restarts it once the channel is free again.

Para tratar este problema, CSMA/CA descansa en un `backoff timer` o temporizador de retirada. Este temporizador es una demora aleatoria elegida por cada dispositivo dentro de un rango que depende del número de retransmisiones de la trama actual. El rango crece exponencialmente con las retransmisiones, como en CSMA/CD. El rango mínimo para el backoff timer es :math:`[0,7*slotTime]`, donde `slotTime` es un parámetro que depende de la capa física subyacente. Comparado con el `backoff exponencial` de CSMA/CD, hay que notar dos importantes diferencias. Primero, el rango inicial para el `backoff timer` es siete veces mayor. Esto se debe a que es imposible en CSMA/CA detectar las colisiones mientras ocurren. Con CSMA/CA, una colisión puede afectar la trama completa, mientras que con CSMA/CD sólo puede afectar el comienzo de la trama. Segundo, un dispositivo CSMA/CA debe sensar regularmente el canal de transmisión durante su temporizador. Si el canal es ocupado (porque otro dispositivo comienza a transmitir), entonces el temporizador debe congelarse hasta que el canal quede libre nuevamente. Una vez libre el canal, el temporizador sigue corriendo de nuevo. Esto contrasta con CSMA/CD, donde el backoff se recomputa luego de cada colisión. Esto se ilustra en la figura más abajo. El nodo A elige un tiempo de backoff más pequeño que el nodo C. Cuando C sensa que el canal está ocupado, congela su temporizador y sólo lo reanuda una vez que el canal quede libre nuevamente.

.. figure:: svg/datalink-fig-008-c.png
   :align: center
   :scale: 70

   Ejemplo detallado con CSMA/CA   
..   Detailed example with CSMA/CA


.. The pseudo-code below summarises the operation of a CSMA/CA device. The values of the SIFS, DIFS, EIFS and slotTime depend on the underlying physical layer technology [802.11]_

El pseudocódigo siguiente resume la operación de un dispositivo CSMA/CA. Los valores de SIFS, DIFS, EIFS y slotTime dependen de la tecnología de la capa física subyacente [802.11]_]. 

.. code-block:: text

 # Pseudocódigo simplificado CSMA/CA
 N=1
 while N <= max :
    waitUntil(canal_libre) 
    if correcta(última_trama) :
       wait(canal_libre_durante_t >= DIFS)
    else:
       wait(canal_libre_durante_t >= EIFS)
       	
    tiempo_back-off = int(random[0,min(255,7*(2^(N-1)))])*slotTime
    wait(canal_libre_durante_tiempo_back-off)
    # backoff timer congelado mientras el canal esté ocupado
    send(trama) 
    wait(reconocimiento or timeout)
    if reconocimiento
       # trama recibida correctamente
       break
    else:
       # se necesita retransmisión
       N=N+1

.. 
 # CSMA/CA simplified pseudo-code
 N=1
 while N<= max :
    waitUntil(free(channel)) 
    if correct(last_frame) :
       wait(channel_free_during_t >=DIFS)
    else:
       wait(channel_free_during_t >=EIFS)
       	
    back-off_time = int(random[0,min(255,7*(2^(N-1)))])*slotTime
    wait(channel free during backoff_time)
    # backoff timer is frozen while channel is sensed to be busy
    send(frame) 
    wait(ack or timeout)
    if received(ack)
       # frame received correctly
       break
    else:
       # retransmission required
       N=N+1

.. index:: hidden station problem, problema de la estación oculta

.. Another problem faced by wireless networks is often called the `hidden station problem`. In a wireless network, radio signals are not always propagated same way in all directions. For example, two devices separated by a wall may not be able to receive each other's signal while they could both be receiving the signal produced by a third host. This is illustrated in the figure below, but it can happen in other environments. For example, two devices that are on different sides of a hill may not be able to receive each other's signal while they are both able to receive the signal sent by a station at the top of the hill. Furthermore, the radio propagation conditions may change with time. For example, a truck may temporarily block the communication between two nearby devices. 

Otro problema que se encuentra en redes inalámbricas suele llamarse `problema de la estación oculta`. En una red inalámbrica, las señales de radio no siempre se propagan de la misma forma en todas direcciones. Por ejemplo, dos dispositivos separados por un muro quizás no puedan recibir las señales del otro, aunque ambos podrían estar recibiendo la señal de un tercero. Esto se ilustra en la figura más abajo, pero puede ocurrir en otros escenarios. Por ejemplo, dos dispositivos que están sobre diferentes lados de una colina quizás no puedan recibir las señales del otro, y sin embargo sean capaces de recibir la señal enviada por una estación en la cima de la colina. Además, las condiciones de propagación de radio pueden variar con el tiempo. Por ejemplo, la comunicación entre dos dispositivos cercanos puede verse temporariamente bloqueada por un vehículo.

.. figure:: svg/datalink-fig-009-c.png
   :align: center
   :scale: 70
   
   Problema de la estación oculta
..   The hidden station problem 



.. index:: Request To Send, RTS, Clear To Send, CTS

.. To avoid collisions in these situations, CSMA/CA allows devices to reserve the transmission channel for some time. This is done by using two control frames : `Request To Send` (RTS) and `Clear To Send` (CTS). Both are very short frames to minimize the risk of collisions. To reserve the transmission channel, a device sends a RTS frame to the intended recipient of the data frame. The RTS frame contains the duration of the requested reservation. The recipient replies, after a SIFS delay, with a CTS frame which also contains the duration of the reservation. As the duration of the reservation has been sent in both RTS and CTS, all hosts that could collide with either the sender or the reception of the data frame are informed of the reservation. They can compute the total duration of the transmission and defer their access to the transmission channel until then. This is illustrated in the figure below where host `A` reserves the transmission channel to send a data frame to host `B`. Host `C` notices the reservation and defers its transmission.

Para evitar colisiones en estas situaciones, CSMA/CA permite a los dispositivos reservar el canal de transmisión por un tiempo dado. Esto se hace usando dos tramas de control: `Request to Send` (RTS) y `Clear to Send` (CTS). Ambas tramas son muy cortas, para minimizar el riesgo de colisión. Para reservar el canal de transmisión, un dispositivo envía una trama RTS al destinatario de la trama. La trama RTS contiene la duración de la reservación requerida. El receptor responde, luego de un retardo SIFS, con una trama CTS que también contiene la duración de la reservación. Como la duración de la reservación ha sido enviada en ambos RTS y CTS, todos los nodos que podrían colisionar con el emisor o el receptor de la trama estań informados de la reserva. Pueden computar la duración total de la transmisión y diferir su acceso al canal de transmisión hasta entonces. Esto se ilustra en la figura más abajo, donde el nodo A reserva el canal de transmisión para enviar una trama al nodo B. El host C advierte esta reservación y difiere su transmisión.

.. figure:: svg/datalink-fig-010-c.png
   :align: center
   :scale: 70
   
   Reservaciones con CSMA/CA
..   Reservations with CSMA/CA

.. The utilization of the reservations with CSMA/CA is an optimisation that is useful when collisions are frequent. If there are few collisions, the time required to transmit the RTS and CTS frames can become significant and in particular when short frames are exchanged. Some devices only turn on RTS/CTS after transmission errors.

La utilización de reservaciones con CSMA/CA es una optimización útil cuando las colisiones son frecuentes. Si hay pocas colisiones, el tiempo requerido para transmitir las tramas RTS y CTS puede volverse significativo, y en particular cuando se intercambian tramas cortas. Algunos dispositivos sólo activan el mecanismo de RTS/CTS luego de que ocurren errores de transmisión.
	
.. Deterministic Medium Access Control algorithms
.. ==============================================

 Algoritmos de Control de Acceso al Medio Determinísticos
 ========================================================

.. During the 1970s and 1980s, there were huge debates in the networking community about the best suited Medium Access Control algorithms for Local Area Networks. The optimistic algorithms that we have described until now were relatively easy to implement when they were designed. From a performance perspective, mathematical models and simulations showed the ability of these optimistic techniques to sustain load. However, none of the optimistic techniques are able to guarantee that a frame will be delivered within a given delay bound and some applications require predictable transmission delays. The deterministic MAC algorithms were considered by a fraction of the networking community as the best solution to fulfill the needs of Local Area Networks. 

Durante los años 70 y 80 se dio un intenso debate en la comunidad de Redes sobre cuáles serían los algoritmos de Control de Acceso al Medio más adecuados para las Redes de Área Local (LANs). Los algoritmos optimistas que hemos descrito hasta ahora eran relativamente fáciles de implementar cuando fueron diseñados. Desde el punto de vista del rendimiento, los modelos matemáticos y las simulaciones mostraban la capacidad de estas técnicas optimistas para soportar una carga sostenida. Sin embargo, ninguna de las técnicas optimistas es capaz de garantizar que una trama será entregada dentro de una cota de retardo dada, y algunas aplicaciones requieren retardos de transmisión predecibles. Los algoritmos MAC determinísticos fueron considerados por una parte de la comunidad de Redes como la mejor solución para satisfacer las necesidades de las LANs.

.. Both the proponents of the deterministic and the opportunistic techniques lobbied to develop standards for Local Area networks that would incorporate their solution. Instead of trying to find an impossible compromise between these diverging views, the IEEE 802 committee that was chartered to develop Local Area Network standards chose to work in parallel on three different LAN technologies and created three working groups. The `IEEE 802.3 working group <http://www.ieee802.org/3/>`_ became responsible for CSMA/CD. The proponents of deterministic MAC algorithms agreed on the basic principle of exchanging special frames called tokens between devices to regulate the access to the transmission medium. However, they did not agree on the most suitable physical layout for the network. IBM argued in favor of Ring-shaped networks while the manufacturing industry, led by General Motors, argued in favor of a bus-shaped network. This led to the creation of the `IEEE 802.4 working group` to standardise Token Bus networks and the `IEEE 802.5 working group <http://www.ieee802.org/5/>`_ to standardise Token Ring networks. Although these techniques are not widely used anymore today, the principles behind a token-based protocol are still important.

Tanto quienes proponían las técnicas determinísticas, como las oportunísticas, abogaron por el desarrollo de estándares para LANs que incorporaran su solución favorita. El comité IEEE 802, que estaba encargado de desarrollar los estándares LAN, en lugar de buscar un imposible compromiso entre estas dos visiones divergentes, decidió trabajar en paralelo sobre tres diferentes tecnologías LAN y crear tres grupos de trabajo. El `grupo de trabajo IEEE 802.3 <http://www.ieee802.org/3/>`_ se hizo responsable por CSMA/CD. Quienes proponían los algoritmos MAC determinísticos se pusieron de acuerdo en el principio básico de intercambiar, entre los dispositivos, tramas especiales llamadas `tokens` (o `fichas`), para regular el acceso al medio de transmisión. Sin embargo, no hubo acuerdo sobre cuál era el arreglo físico más conveniente para la red. La empresa de computación IBM estaba a favor de redes en forma de anillo, mientras que la industria de manufacturas, liderada por General Motors, apoyaba un modelo de red en forma de bus. Esto llevó a la creación del `grupo de trabajo IEEE 802.4` para estandarizar las redes `Token Bus` y el `grupo de trabajo IEEE 802.5 <http://www.ieee802.org/5/>`_ para estandarizar las redes `Token Ring` (o `Anillo con Ficha`). Aunque estas técnicas ya no son muy ampliamente usadas, los principios detrás de los protocolos basados en `ficha` o `token` siguen siendo importantes.

.. The IEEE 802.5 Token Ring technology is defined in [802.5]_. We use Token Ring as an example to explain the principles of the token-based MAC algorithms in ring-shaped networks. Other ring-shaped networks include the almost defunct FDDI [Ross1989]_ or the more recent Resilient Pack Ring [DYGU2004]_ . A good survey of the token ring networks may be found in [Bux1989]_ .

La tecnología IEEE 802.5, `Token Ring`, se define en [802.5]_. Usamos Token Ring como un ejemplo para explicar los principios de los algoritmos MAC en las redes con topología de anillo con ficha. Otras redes con topología de anillo incluyen el casi extinto FDDI [Ross1989]_ o el más reciente Resilient Pack Ring (Anillo Redundante) [DYGU2004]_. Se puede consultar un buen panorama de las redes de la familia de anillo con ficha en [Bux1989]_ .


.. A Token Ring network is composed of a set of stations that are attached to a unidirectional ring. The basic principle of the Token Ring MAC algorithm is that two types of frames travel on the ring : tokens and data frames. When the Token Ring starts, one of the stations sends the token. The token is a small frame that represents the authorization to transmit data frames on the ring. To transmit a data frame on the ring, a station must first capture the token by removing it from the ring. As only one station can capture the token at a time, the station that owns the token can safely transmit a data frame on the ring without risking collisions. After having transmitted its frame, the station must remove it from the ring and resend the token so that other stations can transmit their own frames.

Una red Token Ring se compone de un conjunto de estaciones conectadas a un anillo unidireccional. Los principios básicos del algoritmo MAC de anillo con ficha es que hay dos tipos de tramas viajando por el anillo: fichas y tramas de datos. Cuando arranca la red, una de las estaciones envía la ficha. La ficha es una trama pequeña, que representa la autorización para transmitir tramas de datos sobre el anillo. Una estación, para transmitir una trama de datos, primero debe capturar la ficha, retirándola del anillo. Como sólo una estación por vez puede capturar la ficha, aquella que la posea puede transmitir con seguridad su trama de datos sin arriesgarse a generar colisiones. Luego de haber transmitido su trama, la estación debe retirarla del anillo y volver a emitir la ficha, para que otras estaciones puedan transmitir sus propias tramas.


.. _fig-tokenring:
.. figure:: svg/datalink-fig-011-c.png
   :align: center
   :scale: 70
  
   Una red Token Ring 
..   A Token Ring network



.. While the basic principles of the Token Ring are simple, there are several subtle implementation details that add complexity to Token Ring networks. To understand these details let us analyse the operation of a Token Ring interface on a station. A Token Ring interface serves three different purposes. Like other LAN interfaces, it must be able to send and receive frames. In addition, a Token Ring interface is part of the ring, and as such, it must be able to forward the electrical signal that passes on the ring even when its station is powered off.

Aunque los principios básicos de Token Ring son simples, hay varios sutiles detalles de implementación que agregan complejidad a las redes Token Ring. Para comprender estos detalles analicemos la operación de una interfaz Token Ring en una estación. Una interfaz Token Ring sirve a tres propósitos diferentes. Como las demás interfaces LAN, debe ser capaz de enviar y transmitir tramas. Además, como es parte del anillo, debe ser capaz de reexpedir las señales eléctricas que pasan por el anillo aun cuando la estación esté apagada.

.. When powered-on, Token Ring interfaces operate in two different modes : `listen` and `transmit`. When operating in `listen` mode, a Token Ring interface receives an electrical signal from its upstream neighbour on the ring, introduces a delay equal to the transmission time of one bit on the ring and regenerates the signal before sending it to its downstream neighbour on the ring.

Encendidas, las interfaces Token Ring operan en dos modos diferentes: escuchar y transmitir. Cuando opera en modo escuchar, la interfaz recibe una señal eléctrica de su vecino anterior en el anillo, introduce un retardo igual al tiempo de transmisión de un bit en el anillo y regenera la señal, antes de enviarla a su vecino siguiente. 

.. The first problem faced by a Token Ring network is that as the token represents the authorization to transmit, it must continuously travel on the ring when no data frame is being transmitted. Let us assume that a token has been produced and sent on the ring by one station. In Token Ring networks, the token is a 24 bits frame whose structure is shown below.

El primer problema enfrentado por una red Token Ring es que, como la ficha representa la autorización para transmitir, debe circular continuamente por el anillo aun cuando no haya tramas de datos siendo transmitidas. Supongamos que una estación ha generado y emitido una ficha al anillo. En las redes Token Ring, la ficha es una trama de 24 bits cuya estructura se muestra a continuación.


.. index:: Token Ring token frame, 802.5 token frame

.. figure:: pkt/token.png
   :align: center
   :scale: 100

   Formato de ficha 802.5
..   802.5 token format


.. index:: Starting Delimiter (Token Ring), Ending Delimiter (Token Ring)

.. The token is composed of three fields. First, the `Starting Delimiter` is the marker that indicates the beginning of a frame. The first Token Ring networks used Manchester coding and the `Starting Delimiter` contained both symbols representing `0` and symbols that do not represent bits. The last field is the `Ending Delimiter` which marks the end of the token. The `Access Control` field is present in all frames, and contains several flags. The most important is the `Token` bit that is set in token frames and reset in other frames.

La ficha se compone de tres campos. Primero, el delimitador de comienzo (`Starting Delimiter`) es la marca que indica el comienzo de una ficha. Las primeras redes Token Ring usaban codificación Manchester, y el delimitador de comienzo contenía símbolos representando `0`, y símbolos que no representan bits. El último campo es el delimitador de final (`Ending Delimiter`) que marca el final de la ficha. El campo `Control de Acceso` (`Access Control`) está presente en todas las tramas, y contiene varias señales. La más importante es el bit `Token`, que está activo en las tramas ficha e inactivo en las demás tramas.

.. index:: Token Ring Monitor

.. Let us consider the five station network depicted in figure :ref:`fig-tokenring` above and assume that station `S1` sends a token. If we neglect the propagation delay on the inter-station links, as each station introduces a one bit delay, the first bit of the frame would return to `S1` while it sends the fifth bit of the token. If station `S1` is powered off at that time, only the first five bits of the token will travel on the ring. To avoid this problem, there is a special station called the `Monitor` on each Token Ring. To ensure that the token can travel forever on the ring, this `Monitor` inserts a delay that is equal to at least 24 bit transmission times. If station `S3` was the `Monitor` in figure :ref:`fig-tokenring`, `S1` would have been able to transmit the entire token before receiving the first bit of the token from its upstream neighbour.

Consideremos la red de cinco estaciones representada en la figura :ref:`fig-tokenring` arriba y supongamos que la estación S1 emite la ficha. Si despreciamos el retardo de propagación en los enlaces entre estaciones, como cada estación introduce un retardo de un bit, el primer bit de la trama volvería a S1 mientras está enviando el quinto bit de la ficha. Si S1 fuera apagada en ese instante, sólo los primeros cinco bits de la ficha lograrían circular por el anillo. Para evitar este problema, existe una estación especial llamada el `Monitor` en cada Token Ring. Para asegurar que la ficha siempre pueda atravesar el anillo, este `Monitor` inserta un retardo que es igual al menos a 24 tiempos de transmisión de un bit. Si la estación S3 fuera el `Monitor` en la figura :ref:`fig-tokenring`, S1 habría sido capaz de transmitir la ficha completa antes de recibir el primer bit de la ficha desde su vecino anterior.

.. Now that we have explained how the token can be forwarded on the ring, let us analyse how a station can capture a token to transmit a data frame. For this, we need some information about the format of the data frames. An 802.5 data frame begins with the `Starting Delimiter` followed by the `Access Control` field whose `Token` bit is reset, a `Frame Control` field that allows for the definition of several types of frames, destination and source address, a payload, a CRC, the `Ending Delimiter` and a `Frame Status` field. The format of the Token Ring data frames is illustrated below.

Ahora que hemos explicado cómo la ficha puede ser impulsada por el anillo, analicemos cómo una estación puede capturar una ficha para transmitir una trama de datos. Para esto, necesitamos información sobre el formato de las tramas de datos. Una trama de datos 802.5 comienza con el delimitador de comienzo, seguido por el campo `Control de Acceso`, que permite la definición de varios tipos de tramas; direcciones destino y origen; una carga útil; un CRC; el delimitador de final, y un campo `Estado de trama` (`Frame Status`). El formato de la trama de datos Token Ring está ilustrado más abajo.

.. index:: Token Ring data frame, 802.5 data frame

.. figure:: pkt/8025.png
   :align: center
   :scale: 100

   Trama de datos 802.5
..   802.5 data frame format


.. To capture a token, a station must operate in `Listen` mode. In this mode, the station receives bits from its upstream neighbour. If the bits correspond to a data frame, they must be forwarded to the downstream neighbour. If they correspond to a token, the station can capture it and transmit its data frame. Both the data frame and the token are encoded as a bit string beginning with the `Starting Delimiter` followed by the `Access Control` field. When the station receives the first bit of a `Starting Delimiter`, it cannot know whether this is a data frame or a token and must forward the entire delimiter to its downstream neighbour. It is only when it receives the fourth bit of the `Access Control` field (i.e. the `Token` bit) that the station knows whether the frame is a data frame or a token. If the `Token` bit is reset, it indicates a data frame and the remaining bits of the data frame must be forwarded to the downstream station. Otherwise (`Token` bit is set), this is a token and the station can capture it by resetting the bit that is currently in its buffer. Thanks to this modification, the beginning of the token is now the beginning of a data frame and the station can switch to `Transmit` mode and send its data frame starting at the fifth bit of the `Access Control` field. Thus, the one-bit delay introduced by each Token Ring station plays a key role in enabling the stations to efficiently capture the token. 

Para capturar una ficha, una estación debe operar en modo escucha. En este modo, la estación recibe bits de su vecino anterior. Si los bits corresponden a una trama de datos, deben ser reexpedidos al vecino siguiente. Si corresponden a una ficha, la estación puede capturarla y emitir su trama de datos. Tanto la ficha como la trama de datos se codifican como trenes de bits, comenzando con el delimitador de comienzo, seguido del campo `Control de Acceso`. Cuando la estación recibe el primer bit de un delimitador de comienzo, no puede saber si se trata de una trama de datos o de una ficha, y debe reexpedir el delimitador completo a su vecino siguiente. Sólo cuando recibe el cuarto bit del campo `Control de Acceso` (es decir, el bit de `Ficha`), es que la estación sabe si la trama es de datos o es una ficha. Si el bit de `Ficha` está inactivo, indica una trama de datos, y los restantes bits de la trama de datos deben ser reexpedidos a la estación siguiente. De otro modo, si el bit de `Ficha` está activo, ésta es una ficha, y la estación puede capturarla desactivando el bit que en este momento está en su buffer. Gracias a esta modificación, el principio de la ficha ahora es el comienzo de una trama de datos, y la estación puede cambiar a modo transmitir y enviar su trama de datos comenzando en el quinto bit del campo `Control de Acceso`. Así, el retardo de un bit introducido por cada estación Token Ring juega un rol vital en habilitar a las estaciones a capturar eficientemente la ficha.


.. After having transmitted its data frame, the station must remain in `Transmit` mode until it has received the last bit of its own data frame. This ensures that the bits sent by a station do not remain in the network forever. A data frame sent by a station in a Token Ring network passes in front of all stations attached to the network. Each station can detect the data frame and analyse the destination address to possibly capture the frame. 

Luego de haber transmitido su trama de datos, la estación debe quedar en modo transmitir hasta que haya recibido el último bit de su propia trama de datos. Esto asegura que los bits enviados por una estación no permanezcan en la red. Una trama de datos enviada por una estación en una red Token Ring, pasa frente a todas las estaciones conectadas a la red. Cada estación puede detectar la trama de datos y analizar la dirección destino, para, posiblemente, capturar la trama.

.. The `Frame Status` field that appears after the `Ending Delimiter` is used to provide acknowledgements without requiring special frames. The `Frame Status` contains two flags : `A` and `C`. Both flags are reset when a station sends a data frame. These flags can be modified by their recipients. When a station senses its address as the destination address of a frame, it can capture the frame, check its CRC and place it in its own buffers. The destination of a frame must set the `A` bit (resp. `C` bit) of the `Frame Status` field once it has seen (resp. copied) a data frame. By inspecting the `Frame Status` of the returning frame, the sender can verify whether its frame has been received correctly by its destination.

El campo de `Estado de Trama` que aparece luego del delimitador de final se usa para proveer reconocimientos sin requerir tramas especiales. El `Estado de Trama` contiene dos señales: A y C. Ambas señales se desactivan cuando una estación envía una trama de datos. Estas señales pueden ser modificadas por sus destinatarios. Cuando una estación detecta que su propia dirección es la dirección destino de una trama, puede capturar la trama, verificar su CRC y ubicarla en sus buffers. El destinatario de una trama debe activar el bit A (resp. el bit C) del campo `Estado de Trama` una vez que ha visto (resp. copiado) una trama de datos. Inspeccionando el `Estado de Trama` de la trama que vuelve, el emisor puede verificar si su trama ha sido recibida correctamente por su destinatario. 

.. index:: Monitor station, Token Holding Time

.. The text above describes the basic operation of a Token Ring network when all stations work correctly. Unfortunately, a real Token Ring network must be able to handle various types of anomalies and this increases the complexity of Token Ring stations. We briefly list the problems and outline their solutions below. A detailed description of the operation of Token Ring stations may be found in [802.5]_. The first problem is when all the stations attached to the network start. One of them must bootstrap the network by sending the first token. For this, all stations implement a distributed election mechanism that is used to select the `Monitor`. Any station can become a `Monitor`. The `Monitor` manages the Token Ring network and ensures that it operates correctly. Its first role is to introduce a delay of 24 bit transmission times to ensure that the token can travel smoothly on the ring. Second, the `Monitor` sends the first token on the ring. It must also verify that the token passes regularly. According to the Token Ring standard [802.5]_, a station cannot retain the token to transmit data frames for a duration longer than the `Token Holding Time` (THT) (slightly less than 10 milliseconds). On a network containing `N` stations, the `Monitor` must receive the token at least every :math:`N \times THT` seconds. If the `Monitor` does not receive a token during such a period, it cuts the ring for some time and then reinitialises the ring and sends a token.

El texto anterior describe la operación básica de una red Token Ring cuando todas las estaciones funcionan correctamente. Desafortunadamente, una red Token Ring en la realidad debe ser capaz de manejar varios tipos de anomalías, y esto incrementa la complejidad de las estaciones. Enumeraremos brevemente los problemas y bosquejaremos sus soluciones. Una descripción detallada de la operación de las estaciones Token Ring puede encontrarse en [802.5]_. El primer problema es cuando todas las estaciones conectadas a la red arrancan. Una de ellas debe levantar la red enviando la primera ficha. Para esto, todas las estaciones implementan un mecanismo de elección distribuida que se usa para seleccionar el `Monitor`. Cualquiera de las estaciones puede convertirse en el `Monitor`. Éste maneja la red Token Ring y asegura que opere correctamente. Su primer rol es introducir un retardo de 24 bits para asegurar que la ficha pueda circular libremente por el anillo. Segundo, el Monitor envía la primera ficha en el anillo. También debe verificar que la ficha pase con regularidad. De acuerdo al estándar Token Ring [802.5]_, una estación no puede retener la ficha para transmitir tramas de datos por un plazo mayor que el `tiempo de retención de ficha` (`Token Holding Time`, THT), de duración ligeramente mayor que 10 milisegundos. En una red que contiene N estaciones, el Monitor debe recibir la ficha al menos cada :math:`N \times THT` segundos. Si el Monitor no recibe una ficha durante este período, corta el anillo por algún tiempo y luego lo reinicializa enviando una ficha.

.. Several other anomalies may occur in a Token Ring network. For example, a station could capture a token and be powered off before having resent the token. Another station could have captured the token, sent its data frame and be powered off before receiving all of its data frame. In this case, the bit string corresponding to the end of a frame would remain in the ring without being removed by its sender. Several techniques are defined in [802.5]_ to allow the `Monitor` to handle all these problems. If unfortunately, the `Monitor` fails, another station will be elected to become the new `Monitor`.

En una red Token Ring pueden ocurrir varias otras anomalías. Por ejemplo, una estación podría capturar una ficha y ser apagada antes de haberla reenviado. Otra estación podría haber capturado la ficha, enviado su trama de datos y ser apagada antes de recibir toda la trama de datos. En este caso, el tren de bits correspondiente al final de una trama permanecería en el anillo sin ser retirado por su emisor. Varias técnicas se definen en [802.5]_ para permitir al Monitor manejar todos estos problemas. Si, desafortunadamente, el Monitor falla, otra estación será elegida para convertirse en el nuevo `Monitor`.

