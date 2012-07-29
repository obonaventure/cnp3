.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. Writing simple networked applications
Escribiendo aplicaciones de red sencillas
#########################################


.. Networked applications were usually implemented by using the :term:`socket` :term:`API`. This API was designed when TCP/IP was first implemented in the `Unix BSD`_ operating system [Sechrest]_ [LFJLMT]_, and has served as the model for many APIs between applications and the networking stack in an operating system. Although the socket API is very popular, other APIs have also been developed. For example, the STREAMS API has been added to several Unix System V variants [Rago1993]_. The socket API is supported by most programming languages and several textbooks have been devoted to it. Users of the C language can consult [DC2009]_, [Stevens1998]_, [SFR2004]_ or [Kerrisk2010]_. The Java implementation of the socket API is described in [CD2008]_ and in the `Java tutorial <http://java.sun.com/docs/books/tutorial/networking/sockets/index.html>`_. In this section, we will use the python_ implementation of the socket_ API to illustrate the key concepts. Additional information about this API may be found in the `socket section <http://docs.python.org/library/socket.html>`_ of the `python documentation <http://docs.python.org/>`_ .

Las aplicaciones de red han sido comúnmente implementadas usando la :term:`API` de :term:`socket`. Esta API fue diseñada cuando se implementó por primera vez TCP/IP en el sistema operativo `Unix BSD`_ [Sechrest]_ [LFJLMT]_, y ha servido como modelo para muchas APIs entre las aplicaciones y el stack de red en los sistemas operativos. Aunque la API de sockets es muy popular, otras también han sido desarrolladas. Por ejemplo, la API de STREAMS ha sido añadida a varias variantes de Unix System V [Rago1993]_. La API de sockets está soportada por la mayor parte de los lenguajes de programación, y  le han sido dedicados varios libros de texto. Los usuarios del lenguaje C pueden consultar [DC2009]_, [Stevens1998]_, [SFR2004]_ o [Kerrisk2010]_. La implementación Java de la API de socket se describe en [CD2008]_ y en el `tutorial Java  <http://java.sun.com/docs/books/tutorial/networking/sockets/index.html>`_. En esta sección usaremos la implementación python_ de la API de socket_ para ilustrar los conceptos clave. Se puede encontrar más información sobre esta API en la `sección de sockets <http://docs.python.org/library/socket.html>`_ de la `documentación de python <http://docs.python.org/>`_.

.. The socket API is quite low-level and should be used only when you need a complete control of the network access. If your application simply needs, for instance, to retrieve data with HTTP, there are much simpler and higher-level APIs.

La API de socket es de muy bajo nivel, y debería usarse sólo cuando se necesita un control completo del acceso a la red. Si su aplicación necesita simplemente, por ejemplo, recuperar datos a través de HTTP, entonces hay APIs disponibles mucho más simples y de más alto nivel.

.. A detailed discussion of the socket API is outside the scope of this section and the references cited above provide a detailed discussion of all the  details of the socket API. As a starting point, it is interesting to compare the socket API with the service primitives that we have discussed in the previous chapter. Let us first consider the connectionless service that consists of the following two primitives : 

.. - `DATA.request(destination,message)` is used to send a message to a specified destination. In this socket API, this corresponds to the ``send`` method.
.. - `DATA.indication(message)` is issued by the transport service to deliver a message to the application. In the socket API, this corresponds to the return of the ``recv`` method that is called by the application. 

Una discusión detallada de la API de socket excede el propósito de esta sección, pero las referencias citadas más abajo ofrecen un análisis en profundidad de la API. Como punto de partida, es interesante comparar la API de socket con las primitivas de servicio que hemos discutido en el capítulo anterior. Consideremos primero el servicio sin conexión que consiste en las siguientes dos primitivas:

 - `DATA.request(destino,mensaje)` se usa para enviar un mensaje a un destino especificado. En esta API de socket, esto corresponde al método ``send``.
 - `DATA.indication(mensaje)` es emitida por el servicio de transporte para entregar un mensaje a la aplicación. En la API de sockets, esto corresponde a la información devuelta por el método ``recv`` que es invocado por la aplicación.

.. The `DATA` primitives are exchanged through a service access point. In the socket API, the equivalent to the service access point is the `socket`. A `socket` is a data structure which is maintained by the networking stack and is used by the application every time it needs to send or receive data through the networking stack. The `socket` method in the python_ API takes two main arguments :

.. - an `address family` that specifies the type of address family and thus the underlying networking stack that will be used with the socket. This parameter can be either ``socket.AF_INET`` or ``socket.AF_INET6``. ``socket.AF_INET``, which corresponds to the TCP/IPv4 protocol stack is the default. ``socket.AF_INET6`` corresponds to the TCP/IPv6 protocol stack.
.. - a `type` indicates the type of service which is expected from the networking stack. ``socket.STREAM`` (the default) corresponds to the reliable bytestream connection-oriented service. ``socket.DGRAM`` corresponds to the connectionless service.
 
Las primitivas `DATA` se intercambian a través de un punto de acceso al servicio. En la API de socket, el equivalente al punto de acceso al servicio es el `socket`. Un `socket` es una estructura de datos que es mantenida por el stack de red, y es usada por la aplicación cada vez que necesita enviar o recibir datos a través del stack de red. El método `socket` en la API de python_ lleva dos argumentos principales:

 - Una `familia de direcciones` que especifica el tipo de familia de direcciones y por lo tanto el stack de red subyacente que será usado con el socket. Este parámetro puede ser, o bien ``socket.AF_INET``, o ``socket.AF_INET6``. El valor por defecto es ``socket.AF_INET``, que corresponde a la pila de protocolos TCP/IPv4. ``socket.AF_INET6`` corresponde a la pila TCP/IPv6.
 - un `tipo` que indica el tipo de servicio que se espera de la pila de red. El valor por defecto, ``socket.STREAM``, corresponde al servicio confiable de flujo de bytes, orientado a conexión.  ``socket.DGRAM`` corresponde al servicio sin conexión.

.. COMENTADO EN EL ORIGINAL?
.. However, it is important to understand the basics and the limitations of this API. We use the `python socket API <http://docs.python.org/library/socket.html>` to describe these issues. The socket API allows applications to interact with the transport services offered by the networking stack. The simplest transport service is the connectionless service. The simplest client application that uses this service will issue a `DATA.request` with its request and wait for a `DATA.indication` that contains the response.

.. index:: socket, sendto, AF_INET, AF_INET6, SOCK_DGRAM, SOCK_STREAM

.. A simple client that sends a request to a server is often written as follows in descriptions of the socket API.
Un cliente sencillo, que envía un requerimiento a un servidor, frecuentemente se escribe de la forma que sigue, en las descripciones de la API de sockets.

.. literalinclude:: python/simpleclientip.py
  :language: python

.. A typical usage of this application would be 
Un uso típico de esta aplicación podría ser la siguiente.

.. code-block:: text

   python client.py 127.0.0.1 12345

.. where ``127.0.0.1`` is the IPv4 address of the host (in this case the localhost) where the server is running and ``12345`` the port of the server.
Donde ``127.0.0.1`` es la dirección IPv4 del host donde está corriendo el servidor (en este caso, el `localhost`); y ``12345`` es el puerto del servidor.

.. The first operation is the creation of the ``socket``. Two parameters must be specified while creating a ``socket``. The first parameter indicates the address family and the second the socket type. The second operation is the transmission of the message by using ``sendto`` to the server. It should be noted that ``sendto`` takes as arguments the message to be transmitted and a tuple that contains the IPv4 address of the server and its port number.

La primera operación es la creación del ``socket``. Durante la creación de un socket deben especificarse dos parámetros. El primero indica la familia de direcciones, y el segundo, el tipo del socket. La segunda operación es la transmisión del mensaje usando la primitiva ``sendto`` hacia el servidor. Debe notarse que ``sendto`` toma como argumento el mensaje a ser transmitido y una tupla que contiene la dirección IPv4 del servidor y su número de puerto.  

.. The code shown above supports only the TCP/IPv4 protocol stack. To use the TCP/IPv6 protocol stack the ``socket`` must be created by using the ``socket.AF_INET6`` address family. Forcing the application developer to select TCP/IPv4 or TCP/IPv6 when creating a ``socket`` is a major hurdle for the deployment and usage of TCP/IPv6 in the global Internet [Cheshire2010]_. While most operating systems support both TCP/IPv4 and TCP/IPv6, many applications still only use TCP/IPv4 by default. In the long term, the ``socket`` API should be able to handle TCP/IPv4 and TCP/IPv6 transparently and should not force the application developer to always specify whether it uses TCP/IPv4 or TCP/IPv6.

El código que se muestra anteriormente soporta sólo la pila de protocolos TCP/IPv4. Para usar la pila TCP/IPv6, el ``socket`` debe ser creado usando la familia de direcciones ``socket.AF_INET6``. Obligar al desarrollador de aplicaciones a seleccionar  TCP/IPv4 o TCP/IPv6 al crear un socket es un obstáculo importante para la implantación y uso de TCP/IPv6 en la Internet global [Cheshire2010]_. Mientras que la mayor parte de los sistemas operativos soportan a la vez TCP/IPv4 y TCP/IPv6, muchas aplicaciones aún usan únicamente TCP/IPv4 por defecto. A largo plazo, la API de ``socket`` deberá ser capaz de manejar TCP/IPv4 y TCP/IPv6 transparentemente y no deberá forzar al desarrollador a especificar siempre si usará TCP/IPv4 o TCP/IPv6.  

.. index:: getaddrinfo, AF_UNSPEC

.. Another important issue with the socket API as supported by python_ is that it forces the application to deal with IP addresses instead of dealing directly with domain names. This limitation dates from the early days of the ``socket`` API in Unix 4.2BSD. At that time, the DNS was not widely available and only IP addresses could be used. Most applications rely on DNS names to interact with servers and this utilisation of the DNS plays a very important role to scale web servers and content distribution networks. To use domain names, the application needs to perform the DNS resolution by using the ``getaddrinfo`` method. This method queries the DNS and builds the ``sockaddr`` data structure which is used by other methods of the socket API. In python_, ``getaddrinfo`` takes several arguments :

.. - a `name` that is the domain name for which the DNS will be queried
.. - an optional `port number` which is the port number of the remote server
.. - an optional `address family` which indicates the address family used for the DNS request. ``socket.AF_INET`` (resp. ``socket.AF_INET6``) indicates that an IPv4 (IPv6) address is expected. Furthermore, the python_ socket API allows an application to use ``socket.AF_UNSPEC`` to indicate that it is able to use either IPv4 or IPv6 addresses.
.. - an optional `socket type` which can be either ``socket.SOCK_DGRAM`` or ``socket.SOCK_STREAM``

Otro aspecto importante con la API de sockets tal como la soporta python_ es que obliga a la aplicación a tratar con direcciones IP en lugar de trabajar directamente con nombres de dominio. Esta limitación data de los primeros días de la API de ``socket`` en Unix 4.2BSD. En ese momento, el servicio DNS no estaba ampliamente disponible, y sólo podían usarse direcciones IP. La mayoría de las aplicaciones dependen de nombres DNS Para interactuar con servidores, y esta utilización del DNS juega un rol muy importante para la escalabilidad de los servidores web y las redes de distribución de contenidos. Para usar nombres de dominio, la aplicación necesita ejecutar la resolución DNS usando el método ``getaddrinfo``. Este método consulta al DNS y construye una estructura de datos ``sockaddr`` que es usada por otros métodos de la API. En python_, ``getaddrinfo`` lleva varios argumentos:

 - Un nombre (`name`) que es el nombre de dominio por el cual se consultará al DNS.
 - Un número de puerto opcional, que es el número de puerto del servidor remoto.
 - Una familia de direcciones, opcional, que indica la familia usada para el requerimiento DNS. El argumento ``socket.AF_INET`` (resp. ``socket.AF_INET6``) indica que se desea obtener una dirección IPv4 (resp. IPv6). La API de socket python_ permite a una aplicación el uso de ``socket.AF_UNSPEC`` para indicar que es capaz de usar tanto direcciones IPv4 como IPv6.
 - Un tipo de socket opciones que puede ser, o bien ``socket.SOCK_DGRAM`` o ``socket.SOCK_STREAM``.

.. In today's Internet hosts that are capable of supporting both IPv4 and IPv6, all applications should be able to handle both IPv4 and IPv6 addresses. When used with the ``socket.AF_UNSPEC`` parameter, the ``socket.getaddrinfo`` method returns a list of tuples containing all the information to create a ``socket``.

En los hosts de Internet de hoy, que son capaces de soportar a la vez IPv4 y IPv6, todas las aplicaciones deberían ser capaces de manejar tanto direcciones IPv4 como IPv6. Al ser usado con el parámetro ``socket.AF_UNSPEC``, el método ``socket.getaddrinfo`` devuelve una lista de tuplas que contienen toda la información para crear un ``socket``.

.. code-block:: python

  import socket
  socket.getaddrinfo('www.example.net',80,socket.AF_UNSPEC,socket.SOCK_STREAM)
  [ (30, 1, 6, '', ('2001:db8:3080:3::2', 80, 0, 0)), 
    (2, 1, 6, '', ('203.0.113.225', 80))]

.. In the example above, ``socket.getaddrinfo`` returns two tuples. The first one corresponds to the ``sockaddr`` containing the IPv6 address of the remote server and the second corresponds to the IPv4 information. Due to some peculiarities of IPv6 and IPv4, the format of the two tuples is not exactly the same, but the key information in both cases are the network layer address (``2001:db8:3080:3::2`` and ``203.0.113.225``) and the port number (``80``). The other parameters are seldom used.

En el ejemplo anterior, ``socket.getaddrinfo`` devuelve dos tuplas. La primera corresponde a la estructura ``sockaddr`` que contiene la dirección IPv6 del servidor remoto, y la segunda corresponde a la información de IPv4.
Debido a algunas peculiaridades de IPv6 e IPv4, el formato de ambas tuplas no es exactamente el mismo, pero las piezas de información importante son en ambos casos las direcciones de capa de red  (``2001:db8:3080:3::2`` y ``203.0.113.225``) y los números de puerto (``80``). Los restantes parámetros se usan muy ocasionalmente.

.. ``socket.getaddrinfo`` can be used to build a simple client that queries the DNS and contact the server by using either IPv4 or IPv6 depending on the addresses returned by the ``socket.getaddrinfo`` method. The client below iterates over the list of addresses returned by the DNS and sends its request to the first destination address for which it can create a ``socket``. Other strategies are of course possible. For example, a host running in an IPv6 network might prefer to always use IPv6 when IPv6 is available [#fipv6pref]_. Another example is the happy eyeballs approach which is being discussed within the IETF_ [WY2011]_. For example, [WY2011]_ mentions that some web browsers try to use the first address returned by ``socket.getaddrinfo``. If there is no answer within some small delay (e.g. 300 milliseconds), the second address is tried.

Puede usarse la primitiva ``socket.getaddrinfo`` para construir un cliente sencillo, que consulta el DNS y contacta al servidor usando ya sea IPv4 o IPv6, dependiendo de las direcciones devueltas por el método ``socket.getaddrinfo``. El cliente que se muestra más abajo itera sobre la lista de direcciones devueltas por el DNS y envía sus requerimientos a la primera dirección destino para la cual pueda crear un socket. Otras estrategias son posibles, por supuesto. Por ejemplo, un host que corre en una red IPv6 podría preferir usar siempre IPv6 si está disponible [#fipv6pref]_. Otro ejemplo es la aproximación de "vista feliz" que se discute en IETF_ [WY2011]_. Por ejemplo, [WY2011]_ menciona que algunos navegadores de web tratan de usar la primera dirección devuelta por ``socket.getaddrinfo``. Si no hay respuesta dentro de algún pequeño delay (por ejemplo, 300 milisegundos), se intenta con la segunda dirección.


.. literalinclude:: python/simpleclientname.py
   :language: python

.. index:: socket.connect, socket.send, socket.recv, socket.close, socket.shutdown

.. Now that we have described the utilisation of the socket API to write a simple client using the connectionless transport service, let us have a closer look at the reliable byte stream transport service. As explained above, this service is invoked by creating a ``socket`` of type ``socket.SOCK_STREAM``. Once a socket has been created, a client will typically connect to the remote server, send some data, wait for an answer and eventually close the connection. These operations are performed by calling the following methods :

.. - ``socket.connect`` : this method takes a ``sockaddr`` data structure, typically returned by ``socket.getaddrinfo``, as argument. It may fail and raise an exception if the remote server cannot be reached.
.. - ``socket.send`` : this method takes a string as argument and returns the number of bytes that were actually sent. The string will be transmitted as a sequence of consecutive bytes to the remote server. Applications are expected to check the value returned by this method and should resend the bytes that were not send.
.. - ``socket.recv`` : this method takes an integer as argument that indicates the size of the buffer that has been allocated to receive the data. An important point to note about the utilisation of the ``socket.recv`` method is that as it runs above a bytestream service, it may return any amount of bytes (up to the size of the buffer provided by the application). The application needs to collect all the received data and there is no guarantee that some data sent by the remote host by using a single call to the ``socket.send`` method will be received by the destination with a single call to the ``socket.recv`` method. 
.. - ``socket.shutdown`` : this method is used to release the underlying connection. On some platforms, it is possible to specify the direction of transfer to be released (e.g. ``socket.SHUT_WR`` to release the outgoing direction or ``socket.SHUT_RDWR`` to release both directions).
.. - ``socket.close``: this method is used to close the socket. It calls ``socket.shutdown`` if the underlying connection is still open.


Ahora que hemos descrito la utilización de la API de sockets para escribir un cliente sencillo usando el servicio de transporte sin conexión, demos una mirada más de cerca al servicio de transporte confiable. Como se explicó anteriormente, este servicio se invoca creando un ``socket`` de tipo ``socket.SOCK_STREAM``. Una vez que un socket ha sido creado, un cliente típicamente se conectará al servidor remoto, enviará algunos datos, esperará una respuesta y eventualmente cerrará la conexión. Estas operaciones se ejecutan llamando a los siguientes métodos:

 - ``socket.connect``: este método toma una estructura de datos ``sockaddr``, típicamente devuelta por  ``socket.getaddrinfo``, como argumento. Puede fallar y levantar una excepción si el servidor remoto no puede ser alcanzado.
 - ``socket.send``: este método toma una cadena como argumento, y devuelve la cantidad de bytes que fueron efectivamente enviados. La cadena será transmitida como una secuencia de bytes consecutivos al servidor remoto. Las aplicaciones deben verificar el valor devuelto por este método y deben reenviar los bytes que no fueron emitidos.
 - ``socket.recv``: este método toma un entero como argumento un entero que indica el tamaño del buffer que ha sido asignado para recibir los datos. Un punto importante a notar sobre la utilización del método ``socket.recv`` es que, como corre sobre un servicio de flujo de bytes, puede devolver cualquier cantidad de bytes (hasta el tamaño del buffer provisto por la aplicación). La aplicación necesita recoger todos los datos recibidos, y no hay garantías de que un conjunto de datos enviado por el host remoto usando una única llamada al método ``socket.send`` vaya a ser recibido por el destinatario con una única llamada al método ``socket.recv``. 
 - ``socket.shutdown``: usado para liberar la conexión subyacente. En algunas plataformas, es posible especificar la dirección de transferencia a ser liberada (por ejemplo, ``socket.SHUT_WR`` para liberar la dirección de salida, o  ``socket.SHUT_RDWR`` para liberar ambas).
 - ``socket.close``: usado para cerrar el socket. Llama a ``socket.shutdown`` si la conexión subyacente aún está abierta.


.. With these methods, it is now possible to write a simple HTTP client. This client operates over both IPv6 and IPv4 and writes the homepage of the remote server on the standard output. It also reports the number of ``socket.recv`` calls that were used to retrieve the homepage [#fnumrecv]_ . 

Con estos métodos, ahora es posible escribir un cliente HTTP sencillo. Este cliente opera tanto sobre IPv6 como sobre IPv4, y escribe la página inicial o `homepage` del servidor remoto sobre la salida estándar. También informa la cantidad de llamadas a  ``socket.recv`` que fueron usadas para recuperar la página inicial [#fnumrecv]_ . 

.. literalinclude:: python/httpclient.py
   :language: python


.. As mentioned above, the socket API is very low-level. This is the interface to the transport service. For a common and simple task, like retrieving a document from the Web, there are much simpler solutions. For example, the python_ `standard library <http://docs.python.org/library/>`_ includes several high-level APIs to implementations of various application layer protocols including HTTP. For example, the `httplib <http://docs.python.org/library/httplib.html>`_ module can be used to easily access documents via HTTP. 

Como ya se mencionó, la API de sockets es de muy bajo nivel. Ésta es la interfaz al servicio de transporte. Para una tarea común y sencilla, como recuperar un documento de la Web, hay soluciones mucho más simples. Por ejemplo, la `biblioteca estándar <http://docs.python.org/library/>`_ de python_ incluye varias APIs de alto nivel para implementaciones de varios protocolos de capa de aplicación, entre ellos HTTP. Por ejemplo, el módulo `httplib <http://docs.python.org/library/httplib.html>`_ puede ser usado para acceder a documentos a través de HTTP con facilidad. 

.. literalinclude:: python/http-client-httplib.py
 :language: python

.. Another module, `urllib2 <http://docs.python.org/library/urllib2.html>`_ allows the programmer to directly use URLs. This is much more simpler than directly using sockets. 

Otro módulo, `urllib2 <http://docs.python.org/library/urllib2.html>`_, permite al programador usar URLs directamente. Esto es mucho más simple que el uso directo de sockets.

.. literalinclude:: python/http-cclient-urllib2.py
 :language: python

.. But simplicity is not the only advantage of using high-level libraries. They allow the programmer to manipulate higher-level concepts ( e.g. `I want the content pointed by this URL`) but also include many features such as transparent support for the utilisation of :term:`TLS` or IPv6.

Pero la simplicidad no es la única ventaja de usar bibliotecas de alto nivel. Permiten al programador manipular conceptos de alto nivel (como, por ejemplo, "quiero el contenido apuntado por este URL"); pero además traen mecanismos como el soporte transparente para la utilización de :term:`TLS` o de IPv6.

.. The second type of applications that can be written by using the socket API are the servers. A server is typically runs forever waiting to process requests coming from remote clients. A server using the connectionless will typically start with the creation of a `socket` with the ``socket.socket``. This socket can be created above the TCP/IPv4 networking stack (``socket.AF_INET``) or the TCP/IPv6 networking stack (``socket.AF_INET6``), but not both by default. If a server is willing to use the two networking stacks, it must create two threads, one to handle the TCP/IPv4 socket and the other to handle the TCP/IPv6 socket. It is unfortunately impossible to define a socket that can receive data from both networking stacks at the same time with the python_ socket API.

El segundo tipo de aplicaciones que pueden ser escritas usando la API de sockets son los servidores. Un servidor típicamente corre en forma perpetua, esperando procesar requerimientos que vienen de clientes remotos. Un servidor que usa el transporte sin conexión comenzará usualmente con la creación de un `socket` con la primitiva ``socket.socket``. Este socket puede ser creado sobre la pila de red TCP/IPv4 (``socket.AF_INET``) o sobre la pila TCP/IPv6 (``socket.AF_INET6``), pero no ambos por defecto. Si un servidor desea usar las dos pilas de red, debe crear dos threads, uno para manejar el socket TCP/IPv4 y el otro para manejar el socket TCP/IPv6. Desafortunadamente, es imposible definir un socket que pueda recibir datos de ambas pilas al mismo tiempo con la API de sockets de python_.

.. index:: socket.bind, socket.recvfrom

.. A server using the connectionless service will typically use two methods from the socket API in addition to those that we have already discussed.

.. - ``socket.bind`` is used to bind a socket to a port number and optionally an IP address. Most servers will bind their socket to all available interfaces on the servers, but there are some situations where the server may prefer to be bound only to specific IP addresses. For example, a server running on a smartphone might want to be bound to the IP address of the WiFi interface but not on the 3G interface that is more expensive.
.. - ``socket.recvfrom`` is used to receive data from the underlying networking stack. This method returns both the sender's address and the received data.

Un servidor que use el servicio sin conexión típicamente usará dos métodos de la API de sockets además de los que ya hemos discutido.

 - ``socket.bind`` se usa para ligar un socket a un número de puerto y opcionalmente una dirección IP. La mayoría de los servidores ligan su socket a todas las interfaces disponibles de los hosts servidores, pero hay algunas situaciones donde el servidor puede preferir ligarse sólo a direcciones IP específicas.  Por ejemplo, un servidor que corre en un `smartphone` puede querer ligarse a la dirección IP de la interfaz WiFi, pero no a la interfaz 3G, que es más costosa.
 - ``socket.recvfrom`` se usa para recibir datos desde la pila de red subyacente. Este método devuelve tanto la dirección del emisor como los datos recibidos.


.. The code below illustrates a very simple server running above the connectionless transport service that simply prints on the standard output all the received messages. This server uses the TCP/IPv6 networking stack.
El código siguiente ilustra un servidor muy simple corriendo sobre el servicio  de transporte sin conexión, que simplemente imprime todos los mensajes que recibe sobre salida estándar. Este servidor usa la pila de red TPC/IPv6.

.. literalinclude:: python/simpleserverudp.py
   :language: python

.. A server that uses the reliable byte stream service can also be built above the socket API. Such a server starts by creating a socket that is bound to the port that has been chosen for the server. Then the server calls the ``socket.listen`` method. This informs the underlying networking stack of the number of transport connection attempts that can be queued in the underlying networking stack waiting to be accepted and processed by the server. The server typically has a thread waiting on the ``socket.accept`` method. This method returns as soon as a connection attempt is received by the underlying stack. It returns a socket that is bound to the established connection and the address of the remote host. With these methods, it is possible to write a very simple web server that always returns a `404` error to all `GET` requests and a `501` errors to all other requests. 

Sobre la API de sockets también puede construirse un servidor que use el servicio de flujo de bytes confiable. Dicho servidor comienza creando un socket que se liga al puerto que ha sido elegido para el servidor. Luego llama al método ``socket.listen``. Éste informa a la pila de red subyacente cuál es la cantidad de intentos de conexión de transporte que pueden ser encoladas en dicha pila de red, esperando ser aceptados y procesados por el servidor. El servidor, típicamente,  tiene un thread esperando sobre el método ``socket.accept``. Este método regresa tan pronto como se reciba un intento de conexión en la pila subyacente. Devuelve un socket que está ligado a la conexión establecida y a la dirección del host remoto. Con estos métodos, es posible escribir un web server muy sencillo que siempre devuelve un error `404` a todos los requerimientos `GET`, y errores `501` a todos los demás requerimientos. 

.. literalinclude:: python/simplehttpserver.py
   :language: python

.. This server is far from a production-quality web server. A real web server would use multiple threads and/or non-blocking IO to process a large number of concurrent requests [#fapache]_ . Furthermore, it would also need to handle all the errors that could happen while receiving data over a transport connection. These are outside the scope of this section and additional information on more complex networked applications may be found elsewhere. For example, [RG2010]_ provides an in-depth discussion of the utilisation of the socket API with python while [SFR2004]_ remains an excellent source of information on the socket API in C.

Este servidor web está muy lejos de tener calidad de producción. Un servidor web real usaría múltiples threads, y/o entrada/salida no bloqueante, para procesar una gran cantidad de requerimientos concurrentes [#fapache]_. Además, también necesitaría manejar todos los errores que pudieran ocurrir mientras recibiera datos sobre una conexión de transporte. Esto queda fuera del alcance de esta sección; y puede hallarse más información sobre aplicaciones de red más complejas en otros lugares. Por ejemplo, [RG2010]_ ofrece una discusión en profundidad sobre la utilización de la API de sockets con python_, mientras que [SFR2004]_ es siempre una excelente fuente de información sobre la API de sockets en C.


..  To be written : connect by name API is key !  http://www.stuartcheshire.org/IETF72/


.. [Cheshire2010]_



.. rubric:: Footnotes

.. .. [#fipv6pref] Most operating systems today by default prefer to use IPv6 when the DNS returns both an IPv4 and an IPv6 address for a name. See http://ipv6int.net/systems/ for more detailed information.
.. [#fipv6pref] La mayoría de los sistemas operativos de hoy, por defecto, prefieren usar IPv6 cuando el DNS devuelve a la vez direcciones IPv4 e IPv6 para un mismo nombre consultado. Véase http://ipv6int.net/systems/ para más detalles.  

.. .. [#fnumrecv] Experiments with the client indicate that the number of `socket.recv` calls can vary at each run. There are various factors that influence the number of such calls that are required to retrieve some information from a server. We'll discuss some of them after having explained the operation of the underlying transport protocol.
.. [#fnumrecv] Los experimentos con el cliente indican que la cantidad de llamadas a `socket.recv` puede variar con cada corrida. Existen varios factores que tienen influencia sobre la cantidad de llamadas que se requieren para recuperar una información dada de un servidor. Discutiremos algunos de ellos luego de haber explicado la operación del protocolo de transporte subyacente.

.. .. [#fapache] There are many `production quality web servers software <http://en.wikipedia.org/wiki/Comparison_of_web_server_software>`_ available. apache_ is a very complex but widely used one. `thttpd <http://www.acme.com/software/thttpd/>`_ and `lighttpd <http://www.lighttpd.net/>`_ are less complex and their source code is probably easier to understand.
.. [#fapache] Existe mucho software de `web servers de calidad de producción <http://en.wikipedia.org/wiki/Comparison_of_web_server_software>`_ disponible. apache_ es uno de tales sistemas, complejo pero ampliamente usado. `thttpd <http://www.acme.com/software/thttpd/>`_ y `lighttpd <http://www.lighttpd.net/>`_ son menos complejos, y su código fuente es probablemente más fácil de entender.

.. include:: /links.rst
