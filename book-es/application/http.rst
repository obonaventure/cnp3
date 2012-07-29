.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. _HTTP:

.. The HyperText Transfer Protocol
El protocolo HTTP (HyperText Transfer Protocol)
===============================================

.. In the early days of the Internet was mainly used for remote terminal access with telnet_, email and file transfer. The default file transfer protocol, `FTP`, defined in :rfc:`959` was widely used and `FTP` clients and servers are still included in most operating systems.

En los primeros días de Internet, la red se usaba principalmente para acceso de terminal remoto con telnet_, para email, y para transferencias de archivos. El protocolo de transferencia de archivos por defecto, `FTP`, definido en :rfc:`959`, era ampliamente usado. Aún hoy los clientes y servidores de `FTP` se incluyen en la mayoría de los sistemas operativos.

.. Many `FTP` clients offer a user interface similar to a Unix shell and allow the client to browse the file system on the server and to send and retrieve files. `FTP` servers can be configured in two modes :

..  - authenticated : in this mode, the ftp server only accepts users with a valid user name and password. Once authenticated, they can access the files and directories according to their permissions
..  - anonymous : in this mode, clients supply the `anonymous` userid and their email address as password. These clients are granted access to a special zone of the file system that only contains public files. 

Muchos clientes `FTP` ofrecen una interfaz de usuario similar a la de un shell de Unix, y permiten al cliente navegar el sistema de archivos del servidor, para enviar y recuperar archivos. Los servidores `FTP` pueden ser configurados en dos modos:

 - Autenticado: en este modo, el servidor FTP sólo acepta usuarios con un nombre de usuario y password válidos. Una vez autenticados, pueden acceder a los archivos y directorios de acuerdo a sus permisos.
 - Anónimo: en este modo, los clientes se presentan con la identidad de usuario `anonymous` y su dirección de email como password. Estos clientes reciben acceso a una zona especial del sistema de archivos que sólo contiene archivos públicos. 

.. ftp was very popular in the 1990s and early 2000s, but today it has mostly been superseded by more recent protocols. Authenticated access to files is mainly done by using the Secure Shell (ssh_) protocol defined in :rfc:`4251` and supported by clients such as scp_ or sftp_. Nowadays, anonymous access is mainly provided by web protocols.

FTP fue muy popular en los años 90 y principios del nuevo siglo; pero hoy mayormente ha sido desplazado por protocolos más recientes. El acceso autenticado a archivos se hace principalmente usando el protocolo SSH (Secure Shell, ssh_) definido en :rfc:`4251` y soportado por clientes como scp_ y sftp_. Hoy en día, el acceso anónimo es provisto principalmente por protocolos de Web.

.. In the late 1980s, high energy physicists working at CERN_ had to efficiently exchange documents about their ongoing and planned experiments. `Tim Berners-Lee`_ evaluated several of the documents sharing techniques that were available at that time [B1989]_. As none of the existing solutions met CERN's requirements, they choose to develop a completely new document sharing system. This system was initially called the `mesh`, but was quickly renamed the `world wide web`. The starting point for the `world wide web` are hypertext documents. An hypertext document is a document that contains references (hyperlinks) to other documents that the reader can immediately access. Hypertext was not invented for the world wide web. The idea of hypertext documents was proposed in 1945 [Bush1945]_ and the first experiments were done during the 1960s [Nelson1965]_ [Myers1998]_ . Compared to the hypertext documents that were used in the late 1980s, the main innovation introduced by the `world wide web` was to allow hyperlinks to reference documents stored on remote machines. 

A fines de los años 80, físicos de altas energías que trabajaban en CERN_ necesitaban intercambiar eficientemente sus documentos acerca de experimentos planificados o en marcha. `Tim Berners-Lee`_ evaluó varias de las formas de compartir documentos que existían al momento [B1989]_. Como ninguna de las soluciones disponibles satisfacían los requerimientos de CERN, eligieron desarrollar un sistema de documentación compartida completamente nuevo. Este sistema se llamó primero la `trama` (`mesh`), pero pronto fue renombrado como la `telaraña mundial` (`World Wide Web` o `WWW`; o simplemente, `la Web`). El punto de partida para la `World Wide Web` son los documentos de hipertexto. Un documento de hipertexto es un documento que contiene referencias (hiperenlaces o `hyperlinks`) a otros documentos, que el lector puede acceder inmediatamente. El hipertexto no fue inventado para la Web. La idea de los documentos hipertextuales fue propuesta ya en 1945 [Bush1945]_ y los primeros experimentos fueron hechos durante los años 60 [Nelson1965]_ [Myers1998]_. Comparando con los documentos de hipertexto que se usaban a fines de los años 80, la principal innovación que introdujo la Web fue permitir que los hiperenlaces referenciaran documentos almacenados en máquinas remotas.

.. figure:: svg/www-basics.png
   :align: center
   :scale: 60 

   Clientes y servidores Web
..   World-wide web clients and servers 


.. A document sharing system such as the `world wide web` is composed of three important parts.

.. 1. A standardised addressing scheme that allows unambiguous identification of documents 
.. 2. A standard document format : the `HyperText Markup Language <http://www.w3.org/MarkUp>`_
.. 3. A standardised protocol that facilitates efficient retrieval of documents stored on a server

Un sistema de documentos compartidos como `World Wide Web` se compone de tres importantes partes.

 1. Un esquema de direccionamiento estandarizado que permite la idenificación de documentos sin ambigüedades.
 2. Un formato estándar de documentos: el lenguaje de marcado de hipertexto o `HyperText Markup Language <http://www.w3.org/MarkUp>`_, HTML.
 3. Un protocolo estandarizado que facilita la recuperación eficiente de documentos alojados en un servidor.

.. .. note:: Open standards and open implementations

..  Open standards have, and are still playing a key role in the success of the `world wide web` as we know it today. Without open standards, the world wide web would never have reached its current size. In addition to open standards, another important factor for the success of the web was the availability of open and efficient implementations of these standards. When CERN started to work on the `web`, their objective was to build a running system that could be used by physicists. They developed open-source implementations of the `first web servers <http://www.w3.org/Daemon/>`_ and `web clients <http://www.w3.org/Library/Activity.html>`_. These open-source implementations were powerful and could be used as is, by institutions willing to share information on the web. They were also extended by other developers who contributed to new features. For example, NCSA_ added support for images in their `Mosaic browser <http://en.wikipedia.org/wiki/Mosaic_(web_browser)>`_ that was eventually used to create `Netscape Communications <http://en.wikipedia.org/wiki/Netscape>`_. 

.. note:: Estándares abiertos e implementaciones abiertas

  Los estándares abiertos han jugado, y siguen jugando, un rol clave en el éxito de la `World Wide Web` como la conocemos hoy. Sin estándares abiertos, la WWW jamás habría alcanzado el tamaño que hoy tiene. Además de los estándares abiertos, otro factor importante para el éxito de la Web fue la disponibilidad de implementaciones abiertas y eficientes de estos estándares. Cuando CERN comenzó a trabajar en la Web, su objetivo era construir un sistema activo que pudiera ser utilizado por los físicos. Desarrollaron implementaciones de código abierto de los `primeros servidores Web <http://www.w3.org/Daemon/>`_ y `clientes Web <http://www.w3.org/Library/Activity.html>`_. Estas implementaciones de código abierto eran poderosas y podían ser usadas tal como estaban, por instituciones que quisieran compartir información sobre la Web. También fueron extendidos por otros desarrolladores que contribuyeron con nuevas características. Por ejemplo, NCSA_ agregó soporte para imágenes en su navegador `Mosaic <http://en.wikipedia.org/wiki/Mosaic_(web_browser)>`_ que eventualmente fue usado para crear `Netscape Communications <http://en.wikipedia.org/wiki/Netscape>`_. 


.. The first components of the `world wide web` are the Uniform Resource Identifiers (URI), defined in :rfc:`3986`. A URI is a character string that unambiguously identifies a resource on the world wide web. Here is a subset of the BNF for URIs ::

Los primeros componentes de la `World Wide Web` son los los identificadores uniformes de recursos (`Uniform Resource Identifiers`, URI), definidos en :rfc:`3986`. Un URI es una cadena de caracteres que identifica sin ambigüedad un recurso en la WWW. He aquí un subconjunto de la forma BNF para los URIs::

   URI         = scheme ":" "//" authority path [ "?" query ] [ "#" fragment ]
   scheme      = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
   authority   = [ userinfo "@" ] host [ ":" port ]
   query       = *( pchar / "/" / "?" )
   fragment    = *( pchar / "/" / "?" )
   pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
   query         = *( pchar / "/" / "?" )
   fragment      = *( pchar / "/" / "?" )
   pct-encoded   = "%" HEXDIG HEXDIG
   unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
   reserved      = gen-delims / sub-delims
   gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
   sub-delims    = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+" / "," / ";" / "="


.. The first component of a URI is its `scheme`. A `scheme` can be seen as a selector, indicating the meaning of the fields after it. In practice, the scheme often identifies the application-layer protocol that must be used by the client to retrieve the document, but it is not always the case. Some schemes do not imply a protocol at all and some do not indicate a retrievable document [#furiretrieve]_. The most frequent scheme is `http that will be described later. A URI scheme can be defined for almost any application layer protocol [#furilist]_. The characters `:` and `//` follow the `scheme` of any URI.

El primer componente de un URI es su `esquema` (`scheme`). Un `esquema` puede ser visto como un selector, indicando el significado de los campos que vienen detrás. En la práctica, el esquema suele identificar al protocolo de capa de aplicación que debe ser usado por el cliente para recuperar el documento, pero no siempre es éste el caso. Algunos esquemas no implican protocolo alguno, y algunos no indican un documento recuperable [#furiretrieve]_. El esquema más frecuente es  `http` que será descrito más adelante. Puede definirse un esquema de URI para casi cualquier protocolo de capa de aplicación [#furilist]_. Los caracteres `:` y `//` siguen al `esquema` de todo URI.

.. The second part of the URI is the `authority`. With retrievable URI, this includes the DNS name or the IP address of the server where the document can be retrieved using the protocol specified via the `scheme`. This name can be preceded by some information about the user (e.g. a user name) who is requesting the information. Earlier definitions of the URI allowed the specification of a user name and a password before the `@` character (:rfc:`1738`), but this is now deprecated as placing a password inside a URI is insecure. The host name can be followed by the semicolon character and a port number. A default port number is defined for some protocols and the port number should only be included in the URI if a non-default port number is used (for other protocols, techniques like service DNS records are used).

La segunda parte del URI es la `autoridad` (`authority`). Con URI recuperables, esto incluye el nombre DNS o la dirección IP del servidor de donde se puede obtener el documento usando el protocolo especificado mediante el `esquema`. Este nombre puede estar precedido por algo de información acerca del usuario (como un nombre de usuario) que está requiriendo la información. Las definiciones anteriores del URI permitían la especificación de un nombre de usuario y un password antes del carácter `@` (:rfc:`1738`), pero esto está hoy desaconsejado, ya que colocar una password dentro de un URI es inseguro. El nombre de host puede estar seguido por punto y coma, y un número de puerto. Hay número de puerto por defecto definido para ciertos protocolos; y el número de puerto sólo debe incluirse en el URI si se utiliza uno distinto (para otros protocolos se utilizan técnicas como registros del servicio DNS).

.. The third part of the URI is the path to the document. This path is structured as filenames on a Unix host (but it does not imply that the files are indeed stored this way on the server). If the path is not specified, the server will return a default document. The last two optional parts of the URI are used to provide a query and indicate a specific part (e.g. a section in an article) of the requested document. Sample URIs are shown below.

La tercera parte del URI es el camino al documento. Este camino se estructura como los nombres de archivos en un host Unix (pero no implica que los archivos se almacenen efectivamente de esta forma en el servidor). Si el camino no está especificado, el servidor devolverá un documento por defecto. Las dos últimas partes, opcionales, del URI, se usan para proveer una consulta e indicar una parte específica de un documento (como, por ejemplo, una sección de un artículo). Véanse a continuación algunas muestras de URIs.

.. code-block:: text

   http://tools.ietf.org/html/rfc3986.html
   mailto:infobot@example.com?subject=current-issue   
   http://docs.python.org/library/basehttpserver.html?highlight=http#BaseHTTPServer.BaseHTTPRequestHandler
   telnet://[2001:6a8:3080:3::2]:80/
   ftp://cnn.example.com&story=breaking_news@10.0.0.1/top_story.htm

.. COMMENTED OUT IN ORIGINAL
.. The first URI corresponds to a document named `rfc3986.html` that is stored on the server named `tools.ietf.org` and can be accessed by using the `http` protocol on its default port. The second URI corresponds to an email message, with subject `current-issue`, that will be sent to user `infobot` in domain `example.com`. The `mailto:` URI scheme is defined in :rfc:`2368`. The third URI references the portion `BaseHTTPServer.BaseHTTPRequestHandler` of the document `basehttpserver.html` that is stored in the `library` directory on server `docs.python.org`. This document can be retrieved by using the `http` protocol. The query `highlight=http` is associated to this URI. The fourth example is a server that operates the telnet_ protocol, uses IPv6 address `2001:6a8:3080:3::2` and is reachable on port 80. The last URI is somewhat special. Most users will assume that it corresponds to a document stored on the `cnn.example.com` server. However, to parse this URI, it is important to remember that the `@` character is used to separate the user name from the host name in the authorisation part of a URI. This implies that the URI points to a document named `top_story.htm` on host having IPv4 address `10.0.0.1`. The document will be retrieved by using the `ftp` protocol with the user name set to `cnn.example.com&story=breaking_news`. 

.. The first URI corresponds to a document named `rfc3986.html` that is stored on the server named `tools.ietf.org` and can be accessed by using the `http` protocol on its default port. The second URI corresponds to an email message, with subject `current-issue`, that will be sent to user `infobot` in domain `example.com`. The `mailto:` URI scheme is defined in :rfc:`6068`. The third URI references the portion `BaseHTTPServer.BaseHTTPRequestHandler` of the document `basehttpserver.html` that is stored in the `library` directory on server `docs.python.org`. This document can be retrieved by using the `http` protocol. The query `highlight=http` is associated to this URI. The fourth example is a server that operates the telnet_ protocol, uses IPv6 address `2001:6a8:3080:3::2` and is reachable on port 80. The last URI is somewhat special. Most users will assume that it corresponds to a document stored on the `cnn.example.com` server. However, to parse this URI, it is important to remember that the `@` character is used to separate the user name from the host name in the authorisation part of a URI. This implies that the URI points to a document named `top_story.htm` on host having IPv4 address `10.0.0.1`. The document will be retrieved by using the `ftp` protocol with the user name set to `cnn.example.com&story=breaking_news`.


 - El primer URI corresponde a un documento llamado `rfc3986.html` que está almacenado en el servidor `tools.ietf.org` y puede ser accedido usando el protocolo `http` por su puerto por defecto. 
 - El segundo URI corresponde a un mensaje de correo electrónico, con asunto `current-issue`, que será enviado al usuario `infobot` en el dominio `example.com`. El esquema de URI `mailto:` se define en :rfc:`6068`. 
 - El tercer URI referencia la porción `BaseHTTPServer.BaseHTTPRequestHandler` del documento `basehttpserver.html` almacenado en el directorio `library` del servidor `docs.python.org`. Este documento puede ser recuperado usando el protocolo `http`. A este URI se le asocia la consulta `highlight=http`. 
 - El cuarto ejemplo es un servidor que opera el protocolo telnet_, usa dirección IPv6 `2001:6a8:3080:3::2` y es alcanzable sobre el puerto 80. 
 - El último URI es algo especial. La mayoría de los usuarios asumirán que corresponde a un documento almacenado en el servidor `cnn.example.com`. Sin embargo, para analizar este URI es importante recordar que el carácter `@` se usa para separar el nombre de usuario del nombre de host en la parte de autorización de un URI. Esto implica que el URI apunta a un documento llamado `top_story.htm` en el host que tiene dirección `10.0.0.1`. El documento será recuperado usando el protocolo `ftp` con el nombre de usuario establecido como `cnn.example.com&story=breaking_news`.  

.. The second component of the `word wide web` is the HyperText Markup Language (HTML). HTML defines the format of the documents that are exchanged on the `web`. The `first version of HTML <http://www.w3.org/History/19921103-hypertext/hypertext/WWW/MarkUp/Tags.html>`_ was derived from the Standard Generalized Markup Language (SGML) that was standardised in 1986 by :term:`ISO`. SGML_ was designed to allow large project documents in industries such as government, law or aerospace to be shared efficiently in a machine-readable manner. These industries require documents to remain readable and editable for tens of years and insisted on a standardised format supported by multiple vendors. Today, SGML_ is no longer widely used beyond specific applications, but its descendants including :term:`HTML` and :term:`XML` are now widespread.

El segundo componente de la WWW es el Lenguaje de Marcado de Hipertexto o `HyperText Markup Language` (HTML). HTML define el formato de los documentos que se intercambian en la Web. La  `primera versión de HTML <http://www.w3.org/History/19921103-hypertext/hypertext/WWW/MarkUp/Tags.html>`_ fue derivada del Lenguaje de Marcado Estándar Generalizado (`Standard Generalized Markup Language`, SGML) que fue estandarizado en 1986 por :term:`ISO`. SGML_ fue diseñado para permitir a grandes proyectos en los campos del gobierno, la ley o el aeroespacio, compartir eficientemente documentos en forma legible por la máquina. Estas actividades requieren que los documentos permanezcan legibles y editables por decenas de años, e insistían en un formato estandarizado soportado por múltiples vendedores de software. Hoy, SGML_ ya no se usa ampliamente más allá de aplicaciones específicas, pero sus descendientes, incluyendo :term:`HTML` y :term:`XML` están sumamente difundidos.

.. A markup language is a structured way of adding annotations about the formatting of the document within the document itself. Example markup languages include troff_, which is used to write the Unix man pages or Latex_. HTML uses markers to annotate text and a document is composed of `HTML elements`. Each element is usually composed of three items: a start tag that potentially includes some specific attributes, some text (often including other elements), and an end tag. A HTML tag is a keyword enclosed in angle brackets. The generic form of a HTML element is ::

Un lenguaje de marcado (`markup language`) es una forma estructurada de agregar anotaciones sobre el formato del documento, dentro del documento mismo. Entre los lenguajes de markup hay ejemplos como troff_, que es usado para escribir las páginas de manual (`man`) de Unix, o Latex_. HTML usa marcas para anotar el texto, y un documento se compone de elementos HTML. Cada elemento está compuesto generalmente de tres items: un rótulo inicial (o `tag`), que potencialmente incluye algunos atributos específicos, algún texto (a veces incluyendo otros elementos), y un rótulo o `tag` final. Un rótulo o `tag` HTML es una palabra reservada encerrada en ángulos. La forma genérica de un elemento HTML es::

 <rótulo>Texto a presentar</rótulo>
.. <tag>Some text to be displayed</tag>

.. More complex HTML elements can also include optional attributes in the start tag ::
Algunos elementos HTML más complejos pueden incluir atributos opcionales en el rótulo inicial::
 
 <rótulo atributo1="valor1" atributo2="valor2">Otro texto a presentar</rótulo>
.. <tag attribute1="value1" attribute2="value2">some text to be displayed</tag>

.. The HTML document shown below is composed of two parts : a header, delineated by the `<head>` and `</head>` markers, and a body (between the `<body>` and `</body>` markers). In the example below, the header only contains a title, but other types of information can be included in the header. The body contains an image, some text and a list with three hyperlinks. The image is included in the web page by indicating its URI between brackets inside the `<img src="...">` marker. The image can, of course, reside on any server and the client will automatically download it when rendering the web page. The `<h1>...</h1>` marker is used to specify the first level of headings. The `<ul>` marker indicates an unnumbered list while the `<li>` marker indicates a list item. The `<a href="URI">text</a>` indicates a hyperlink. The `text` will be underlined in the rendered web page and the client will fetch the specified URI when the user clicks on the link.

El documento HTML mostrado a continuación se compone de dos partes: una cabecera, delimitada por los marcadores  `<head>` y `</head>`, y un cuerpo (entre los marcadores `<body>` y `</body>`). En el ejemplo más abajo, la cabecera sólo contiene un título, pero en ella pueden incluirse otros tipos de información. El cuerpo contiene una imagen, una cantidad de texto y una lista con tres hiperenlaces. La imagen se incluye en la página Web indicando su URI entre ángulos, dentro del marcador `<img src="...">`. La imagen puede, por supuesto, residir en cualquier servidor, y el cliente la descargará automáticamente al dibujar la página. El marcador `<h1>...</h1>` se usa para especificar el primer nivel de encabezados. El marcador `<ul>` indica una lista sin numeración, mientras que el marcador `<li>` indica un elemento de lista. El `<a href="URI">texto</a>` indica un hiperenlace. El `texto` se verá subrayado en la página Web dibujada, y el cliente recuperará el URI especificado cuando el usuario haga click sobre el enlace.

.. figure:: png/app-fig-015-c.png
   :align: center
   :scale: 80 

   Una página HTML sencilla
..   A simple HTML page 

.. Additional details about the various extensions to HTML may be found in the `official specifications <http://www.w3.org/MarkUp/>`_ maintained by W3C_.
Pueden consultarse detalles sobre las varias extensiones al HTML en las `especificaciones oficiales  <http://www.w3.org/MarkUp/>`_ mantenidas por W3C_.

.. The third component of the `world wide web` is the HyperText Transport Protocol (HTTP). HTTP is a text-based protocol, in which the client sends a request and the server returns a response. HTTP runs above the bytestream service and HTTP servers listen by default on port `80`. The design of HTTP has largely been inspired by the Internet email protocols. Each HTTP request contains three parts :

.. - a `method` , that indicates the type of request, a URI, and the version of the HTTP protocol used by the client 
.. - a `header` , that is used by the client to specify optional parameters for the request. An empty line is used to mark the end of the header
.. - an optional MIME document attached to the request

El tercer componente de la Web es el protocolo HTTP (`HyperText Transport Protocol`). HTTP es un protocolo basado en texto, en el cual el cliente envía un requerimiento y el servidor devuelve una respuesta. HTTP corre sobre el servicio de flujo de bytes, y los servidores HTTP escuchan por el puerto `80` por defecto. El diseño de HTTP ha sido inspirado fuertemente por los protocolos de email de Internet. Cada requerimiento HTTP contiene tres partes:

 - Un `método`, que indica el tipo de requerimiento, un URI, y la versión del protocolo HTTP usada por el cliente.
 - Una `cabecera`, que es usada por el cliente para especificar parámetros opcionales para el requerimiento. Para marcar el final de la cabecera se inserta una línea vacía.
 - Un documento MIME opcional, adjunto (`attached`) al requerimiento.

.. The response sent by the server also contains three parts :

.. - a `status line` , that indicates whether the request was successful or not
.. - a `header` , that contains additional information about the response. The response header ends with an empty line.
.. - a MIME document 

La respuesta enviada por el servidor también contiene tres partes:

 - Una `línea de status`, que indica si el requerimiento fue o no exitoso.
 - Una `cabecera`, que contiene información adicional sobre la respuesta. La cabecera de la respuesta termina con una línea vacía.
 - Un documento MIME. 

.. figure:: svg/http-requests-responses.png
   :align: center
   :scale: 60 

   Requerimientos y respuestas HTTP
.. HTTP requests and responses


.. Several types of method can be used in HTTP requests. The three most important ones are :
..
 - the `GET` method is the most popular one. It is used to retrieve a document from a server. The `GET` method is encoded as `GET` followed by the path of the URI of the requested document and the version of HTTP used by the client. For example, to retrieve the http://www.w3.org/MarkUp/ URI, a client must open a TCP on port `80` with host `www.w3.org` and send a HTTP request containing the following line ::

   GET /MarkUp/ HTTP/1.0

 - the `HEAD` method is a variant of the `GET` method that allows the retrieval of the header lines for a given URI without retrieving the entire document. It can be used by a client to verify if a document exists, for instance. 
 - the `POST` method can be used by a client to send a document to a server. The sent document is attached to the HTTP request as a MIME document.

Pueden usarse varios tipos de métodos en las respuestas HTTP. Las tres más importantes son:

 - El método `GET`, que es el más popular. Se usa para recuperar un documento de un servidor. El método `GET` se codifica con la cadena `GET` seguida por el camino del URI del documento solicitado y la versión de HTTP usada por el cliente. Por ejemplo, para recuperar el URI `http://www.w3.org/MarkUp/`, un cliente debe abrir una conexión TCP por en puerto `80` con el host `www.w3.org` y enviar un requerimiento HTTP conteniendo la siguiente línea::

   GET /MarkUp/ HTTP/1.0

 - El método `HEAD`, que es una variante del método `GET`. Permite la recuperación de las líneas de cabecera para un URI dado, sin recuperar el documento completo.  Puede ser usado por un cliente para, por ejemplo, verificar si un documento existe. 
 - El método `POST`, que puede ser usado por un cliente para enviar un documento a un servidor. El documento enviado es adjuntado al requerimiento HTTP como documento MIME.

.. HTTP clients and servers can include many different HTTP headers in HTTP requests and responses. Each HTTP header is encoded as a single ASCII-line terminated by `CR` and `LF`. Several of these headers are briefly described below. A detailed discussion of all standard headers may be found in :rfc:`1945`. The MIME headers can appear in both HTTP requests and HTTP responses.

 - the `Content-Length:` header is the :term:`MIME` header that indicates the length of the MIME document in bytes.
 - the `Content-Type:` header is the :term:`MIME` header that indicates the type of the attached MIME document. HTML pages use the `text/html` type.
 - the `Content-Encoding:` header indicates how the :term:`MIME document` has been encoded. For example, this header would be set to `x-gzip` for a document compressed using the gzip_ software. 

Los clientes y servidores HTTP pueden incluir muchas diferentes cabeceras HTTP en requerimientos y respuestas. Cada cabecera HTTP se codifica como una única línea ASCII terminada en `CR` y `LF`. Más abajo se describen brevemente varias de estas cabeceras. Puede verse una discusión detallada de todas las cabeceras estándar en :rfc:`1945`. Las cabeceras MIME pueden aparecer tanto en requerimientos como en respuestas HTTP.

 - `Content-Length:` es la cabecera :term:`MIME` que indica la longitud del documento MIME en bytes.
 - `Content-Type:` es la cabecera :term:`MIME` que indica el tipo del documento MIME adjunto. Las páginas HTML usan el tipo `text/html`.
 - La cabecera `Content-Encoding:` indica cómo ha sido codificado el documento MIME. Por ejemplo, esta cabecera se fijaría al valor `x-gzip` para un documento comprimido usando el software gzip_. 


.. rfc:`1945` and :rfc:`2616` define headers that are specific to HTTP responses. These server headers include :

 - the `Server:` header indicates the version of the web server that has generated the HTTP response. Some servers provide information about their software release and optional modules that they use. For security reasons, some system administrators disable these headers to avoid revealing too much information about their server to potential attackers.
 - the `Date:` header indicates when the HTTP response has been produced by the server.
 - the `Last-Modified:` header indicates the date and time of the last modification of the document attached to the HTTP response. 

Los documentos :rfc:`1945` y :rfc:`2616` definen cabeceras que son específicas de respuestas HTTP. Estas cabeceras de servidor incluyen:

 - La cabecera `Server:` que indica la versión del servidor Web que ha generado la respuesta HTTP. Algunos servidores proveen información sobre la versión de software y módulos opcionales que usan. Por razones de seguridad, algunos administradores de sistemas deshabilitan estas cabeceras, para evitar revelar demasiada información acerca de su servidor a potenciales atacantes.
 - La cabecera `Date:` indica cuándo ha sido producida la respuesta HTTP por el servidor.
 - La cabecera `Last-Modified:` indica la fecha y hora de la última modificación del documento adjuntado a la respuesta HTTP. 
 
 
.. Similarly, the following header lines can only appear inside HTTP requests sent by a client :

 - the `User-Agent:` header provides information about the client that has generated the HTTP request. Some servers analyse this header line and return different headers and sometimes different documents for different user agents.
 - the `If-Modified-Since:` header is followed by a date. It enables clients to cache in memory or on disk the recent or most frequently used documents. When a client needs to request a URI from a server, it first checks whether the document is already in its cache. If it is, the client sends a HTTP request with the `If-Modified-Since:` header indicating the date of the cached document. The server will only return the document attached to the HTTP response if it is newer than the version stored in the client's cache. 
 - the `Referrer:` header is followed by a URI. It indicates the URI of the document that the client visited before sending this HTTP request. Thanks to this header, the server can know the URI of the document containing the hyperlink followed by the client, if any. This information is very useful to measure the impact of advertisements containing hyperlinks placed on websites. 
 - the `Host:` header contains the fully qualified domain name of the URI being requested. 

Similarmente, las siguientes líneas de cabecera sólo pueden aparecer dentro de requerimientos HTTP enviados por un cliente:

 - `User-Agent:` provee información sobre el cliente que ha generado el requerimiento HTTP. Algunos servidores analizan esta línea de cabecera y devuelven diferentes cabeceras, y a veces diferentes documentos, para diferentes agentes de usuario.
 - `If-Modified-Since:` es seguida por una fecha. Permite a los clietes almacenar en memoria cache o en disco los documentos más recientes o más frecuentemente usados. Cuando un cliente necesita requerir un URI de un servidor, primero verifica si el documento ya existe en su cache. Si existe, el cliente envía un requerimiento HTTP con la cabecera `If-Modified-Since:` indicando la fecha del documento en cache. El servidor sólo devolverá el documento adjunto a la respuesta HTTP si es más reciente que la versión almacenada en la cache del cliente.
 - La cabecera `Referrer:` es seguida por un URI. Indica el URI del documento que el cliente visitó antes de enviar este requerimiento HTTP. Gracias a esta cabecera, el servidor puede conocer el URI del documento conteniendo el hiperenlace seguido por el cliente, en caso de que exista. Esta información es muy útil para medir el impacto de avisos conteniendo hiperenlaces alojados en sitios Web.
 - La cabecera `Host:` contiene el nombre completamente calificado del URI que se solicita. 


.. .. note:: The importance of the `Host:` header line

 The first version of HTTP did not include the `Host:` header line. This was a severe limitation for web hosting companies. For example consider a web hosting company that wants to serve both `web.example.com` and `www.example.net` on the same physical server. Both web sites contain a `/index.html` document. When a client sends a request for either `http://web.example.com/index.html` or `http://www.example.net/index.html`, the HTTP 1.0 request contains the following line :
..
 .. code-block:: text

   GET /index.html HTTP/1.0

.. By parsing this line, a server cannot determine which `index.html` file is requested. Thanks to the `Host:` header line, the server knows whether the request is for `http://web.example.com/index.html` or `http://www.dummy.net/index.html`. Without the `Host:` header, this is impossible. The `Host:` header line allowed web hosting companies to develop their business by supporting a large number of independent web servers on the same physical server. 

.. note:: La importancia de la línea de cabecera `Host:`

 La primera versión de HTTP no incluía la línea de cabecera `Host:`. Ésta era una severa limitación para las empresas de alojamiento de páginas, o `Web hosting`. Por ejemplo, consideremos una empresa de alojamiento de páginas que quiere servir los dominios `web.example.com` y `www.example.net` en el mismo servidor físico. Ambos sitios Web contienen un documento `/index.html`. Cuando un cliente envía una solicitud para los URIs `http://web.example.com/index.html` o `http://www.example.net/index.html`, el requerimiento HTTP 1.0 contiene la siguiente línea:


 .. code-block:: text

   GET /index.html HTTP/1.0

 Al analizar esta línea, el servidor no sabe determinar cuál de los archivos `index.html` se le está solicitando. Gracias a la línea de cabecera `Host:`, el servidor sabe si el requerimiento es para `http://web.example.com/index.html` o para `http://www.dummy.net/index.html`. Sin la cabecera `Host:`, esto no es posible. La línea de cabecera `Host:` permitió a las empresas de alojamiento de páginas desarrollar sus negocios soportando una gran cantidad de servidores Web independientes en el mismo servidor físico. 

.. The status line of the HTTP response begins with the version of HTTP used by the server (usually `HTTP/1.0` defined in :rfc:`1945` or `HTTP/1.1` defined in :rfc:`2616`) followed by a three digit status code and additional information in English. HTTP status codes have a similar structure as the reply codes used by SMTP. 

 - All status codes starting with digit `2` indicate a valid response. `200 Ok` indicates that the HTTP request was successfully processed by the server and that the response is valid.
 - All status codes starting with digit `3` indicate that the requested document is no longer available on the server. `301 Moved Permanently` indicates that the requested document is no longer available on this server. A `Location:` header containing the new URI of the requested document is inserted in the HTTP response. `304 Not Modified` is used in response to an HTTP request containing the `If-Modified-Since:` header. This status line is used by the server if the document stored on the server is not more recent than the date indicated in the `If-Modified-Since:` header.
 - All status codes starting with digit `4` indicate that the server has detected an error in the HTTP request sent by the client. `400 Bad Request` indicates a syntax error in the HTTP request. `404 Not Found` indicates that the requested document does not exist on the server.
 - All status codes starting with digit `5` indicate an error on the server. `500 Internal Server Error` indicates that the server could not process the request due to an error on the server itself.

La línea de status de la respuesta HTTP comienza con la versión de HTTP usada por el servidor (normalmente `HTTP/1.0` definido en :rfc:`1945` o `HTTP/1.1` definido en :rfc:`2616`), seguido por un código de status de tres dígitos e información adicional en inglés. Los códigos de status HTTP tienen una estructura similar que los códigos de respuestas usados por SMTP. 

 - Todos los códigos de status que comienzan con el dígito `2` indican una respuesta válida. `200 Ok` indica que el requerimiento HTTP fue exitosamente procesado por el servidor y que la respuesta es válida.
 - Todos los códigos de status que comienzan con `3` indican que el documento solicitado ya no está disponible en el servidor (como `301 Moved Permanently`). En la respuesta HTTP vendrá insertada una cabecera `Location:` conteniendo el nuevo URI del documento solicitado. En respuesta a un requerimiento HTTP conteniendo la cabecera `If-Modified-Since:` se utiliza la cabecera `304 Not Modified`. Esta línea de status es usada por el servidor si el documento almacenado no es más reciente que la fecha indicada en la cabecera `If-Modified-Since:`.
 - Todos los códigos de status que comienzan con el dígito `4` indican que el servidor ha detectado un error en el requerimiento HTTP enviado por el cliente. `400 Bad Request` indica un error de sintaxis en el requerimiento HTTP. `404 Not Found` indica que el documento requerido no existe en el servidor.
 - Todos los códigos de status que comienzan con `5` indican un error en el servidor. `500 Internal Server Error` indica que el servidor no logró procesar el requerimiento debido a un error en el servidor mismo.

.. In both the HTTP request and the HTTP response, the MIME document refers to a representation of the document with the MIME headers indicating the type of document and its size.

Tanto en la cabecera como en la respuesta HTTP, el documento MIME se refiere a una representación del documento, con las cabeceras MIME indicando el tipo del documento y su tamaño.

.. As an illustration of HTTP/1.0, the transcript below shows a HTTP request for `http://www.ietf.org <http://www.ietf.org>`_ and the corresponding HTTP response. The HTTP request was sent using the curl_ command line tool. The `User-Agent:` header line contains more information about this client software. There is no MIME document attached to this HTTP request, and it ends with a blank line.

Como ilustración de HTTP/1.0, la siguiente transcripción muestra un requerimiento HTTP para el URI `http://www.ietf.org <http://www.ietf.org>`_ y la correspondiente respuesta HTTP. El requerimiento HTTP fue enviado usando la herramienta de línea de comandos curl_. La línea de cabecera `User-Agent:` contiene más información sobre este software cliente. No existe documento MIME adjunto a este requerimiento HTTP, que termina con una línea en blanco.

.. code-block:: text
 
   GET / HTTP/1.0
   User-Agent: curl/7.19.4 (universal-apple-darwin10.0) libcurl/7.19.4 OpenSSL/0.9.8l zlib/1.2.3
   Host: www.ietf.org
  

.. The HTTP response indicates the version of the server software used with the modules included. The `Last-Modified:` header indicates that the requested document was modified about one week before the request. A HTML document (not shown) is attached to the response. Note the blank line between the header of the HTTP response and the attached MIME document. The `Server:` header line has been truncated in this output.

La cabecera HTTP indica la versión del software servidor que se ha usado, con los módulos incluidos. La cabecera `Last-Modified:` indica que el documento solicitado fue modificado alrededor de una semana antes del requerimiento. Ha sido adjuntado a la respuesta un documento HTML (que no se muestra). Nótese la línea en blanco entre la cabecera de la respuesta HTTP y el documento MIME adjuntado. En esta salida, la línea de cabecera `Server:` ha sido truncada.

.. code-block:: text
 
  HTTP/1.1 200 OK
  Date: Mon, 15 Mar 2010 13:40:38 GMT
  Server: Apache/2.2.4 (Linux/SUSE) mod_ssl/2.2.4 OpenSSL/0.9.8e (truncated)
  Last-Modified: Tue, 09 Mar 2010 21:26:53 GMT
  Content-Length: 17019
  Content-Type: text/html
  
  <!DOCTYPE HTML PUBLIC .../HTML>

.. HTTP was initially designed to share self-contained text documents. For this reason, and to ease the implementation of clients and servers, the designers of HTTP chose to open a TCP connection for each HTTP request. This implies that a client must open one TCP connection for each URI that it wants to retrieve from a server as illustrated on the figure below. For a web page containing only text documents this was a reasonable design choice as the client usually remains idle while the (human) user is reading the retrieved document.

HTTP fue inicialmente diseñado para compartir documentos de texto autocontenidos. Por esta razón, y para facilitar la implementación de clientes y servidores, los diseñadores de HTTP decidieron abrir una conexión TCP por cada requerimiento HTTP. Esto implica que un cliente debe abrir una conexión TCP por cada URI que desea recuperar de un servidor, tal como se ilustra en la figura a continuación. Para una página Web que contiene sólo documentos de texto, éste era un diseño razonable, ya que el cliente normalmente permanece ocioso mientras el usuario (humano) lee el documento recuperado.

.. figure:: png/app-fig-016-c.png
   :align: center
   :scale: 60

   Protocolo HTTP 1.0 y la conexión TCP subyacente
..   HTTP 1.0 and the underlying TCP connection

.. However, as the web evolved to support richer documents containing images, opening a TCP connection for each URI became a performance problem [Mogul1995]_. Indeed, besides its HTML part, a web page may include dozens of images or more. Forcing the client to open a TCP connection for each component of a web page has two important drawbacks. First, the client and the server must exchange packets to open and close a TCP connection as we will see later. This increases the network overhead and the total delay of completely retrieving all the components of a web page. Second, a large number of established TCP connections may be a performance bottleneck on servers.

Sin embargo, según la Web evolucionaba para soportar formatos de documentos más ricos, conteniendo imágenes, abrir una conexión TCP por cada URI se volvió un problema de performance [Mogul1995]_. En realidad, además de su porción HTML, una página Web puede incluir docenas de imágenes, o más. Obligar al cliente a abrir una conexión TCP por cada componente de una página Web tiene dos importantes desventajas. Primero, cliente y servidor deben intercambiar paquetes para abrir y cerrar una conexión TCP, como veremos más adelante. Esto incrementa la sobrecarga de la red y el tiempo total de recuperación de todos los componentes de la página Web. Segundo, mantener un número mayor de conexiones TCP establecidas puede constituir un cuello de botella de performance en el servidor.

.. This problem was solved by extending HTTP to support persistent TCP connections :rfc:`2616`. A persistent connection is a TCP connection over which a client may send several HTTP requests. This is illustrated in the figure below.

Este problema fue resuelto extendiendo HTTP para soportar conexiones persistentes :rfc:`2616`. Una conexión persistente es una conexión TCP sobre la cual un cliente puede enviar múltiples requerimientos HTTP. Esto se ilustra en la figura siguiente.

.. figure:: svg/http-persistent.png
   :align: center
   :scale: 60

   Conexiones persistentes HTTP 1.1
..   HTTP 1.1 persistent connections

.. 
 To allow the clients and servers to control the utilisation of these persistent TCP connections, HTTP 1.1 :rfc:`2616` defines several new HTTP headers :

 - The `Connection:` header is used with the `Keep-Alive` argument by the client to indicate that it expects the underlying TCP connection to be persistent. When this header is used with the `Close` argument, it indicates that the entity that sent it will close the underlying TCP connection at the end of the HTTP response.
 - The `Keep-Alive:` header is used by the server to inform the client about how it agrees to use the persistent connection. A typical `Keep-Alive:` contains two parameters : the maximum number of requests that the server agrees to serve on the underlying TCP connection and the timeout (in seconds) after which the server will close an idle connection

Para permitir a clientes y servidores controlar la utilización de estas conexiones TCP persistentes, el protocolo HTTP 1.1 :rfc:`2616` define varias nuevas líneas de cabecera HTTP:

 - La cabecera `Connection:` es usada por el cliente con el argumento `Keep-Alive` para indicar que espera que la conexión TCP subyacente sea persistente. Cuando esta cabecera se usa con el argumento `Close` argument, indica que la entidad que la envió cerrará la conexión TCP al finalizar la respuesta HTTP.
 - La cabecera `Keep-Alive:` es usada por el servidor para informar al cliente su punto de vista sobre el uso de la conexión persistente. Una cabecera `Keep-Alive:` típica contiene dos parámetros: el número máximo de requerimientos que el servidor está de acuerdo en servir sobre la conexión TCP subyacente, y el timeout (en segundos) luego del cual el servidor cerrará una conexión ociosa.

.. The example below shows the operation of HTTP/1.1 over a persistent TCP connection to retrieve three URIs stored on the same server. Once the connection has been established, the client sends its first request with the `Connection: keep-alive` header to request a persistent connection.

El ejemplo siguiente muestra la operación de HTTP/1.1 sobre una conexión TCP persistente para recuperar tres URIs almacenados en el mismo servidor. Una vez que la conexión ha sido establecida, el cliente envía su primer requerimiento con la cabecera `Connection: keep-alive` para solicitar una conexión persistente. 

.. code-block:: text
 
  GET / HTTP/1.1
  Host: www.kame.net
  User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) 
  Connection: keep-alive


.. The server replies with the `Connection: Keep-Alive` header and indicates that it accepts a maximum of 100 HTTP requests over this connection and that it will close the connection if it remains idle for 15 seconds.
El servidor replica con la cabecera `Connection: Keep-Alive` e indica que aceptará un máximo de cien requerimientos HTTP sobre esta conexión, y que cerrará la conexión si permanece ociosa por quince segundos.

.. code-block:: text

  HTTP/1.1 200 OK
  Date: Fri, 19 Mar 2010 09:23:37 GMT
  Server: Apache/2.0.63 (FreeBSD) PHP/5.2.12 with Suhosin-Patch
  Keep-Alive: timeout=15, max=100
  Connection: Keep-Alive
  Content-Length: 3462
  Content-Type: text/html

  <html>...   </html>


.. The client sends a second request for the style sheet of the retrieved web page.
El cliente envía un segundo requerimiento para la hoja de estilos de la página Web recuperada.

.. code-block:: text
 
 GET /style.css HTTP/1.1
 Host: www.kame.net
 Referer: http://www.kame.net/
 User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) 
 Connection: keep-alive


.. The server replies with the requested style sheet and maintains the persistent connection. Note that the server only accepts 99 remaining HTTP requests over this persistent connection.
El servidor contesta con la hoja de estilos requerida y mantiene la conexión persistente. Nótese que el servidor sólo aceptará 99 requerimientos HTTP restantes sobre esta conexión persistente.

.. code-block:: text

 HTTP/1.1 200 OK
 Date: Fri, 19 Mar 2010 09:23:37 GMT
 Server: Apache/2.0.63 (FreeBSD) PHP/5.2.12 with Suhosin-Patch
 Last-Modified: Mon, 10 Apr 2006 05:06:39 GMT
 Content-Length: 2235
 Keep-Alive: timeout=15, max=99
 Connection: Keep-Alive
 Content-Type: text/css

 ...

.. Then the client automatically requests the web server's icon [#ffavicon]_ , that could be displayed by the browser. This server does not contain such URI and thus replies with a `404` HTTP status. However, the underlying TCP connection is not closed immediately.
Luego el cliente automáticamente solicita el ícono del servidor web [#ffavicon]_ , que podría ser exhibido por el navegador. Este servidor no contiene ese URI, por lo cual responde con un status HTTP `404`. Sin embargo, la conexión TCP subayacente no se cierra inmediatamente.

.. code-block:: text

 GET /favicon.ico HTTP/1.1
 Host: www.kame.net
 Referer: http://www.kame.net/
 User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) 
 Connection: keep-alive

 HTTP/1.1 404 Not Found
 Date: Fri, 19 Mar 2010 09:23:40 GMT
 Server: Apache/2.0.63 (FreeBSD) PHP/5.2.12 with Suhosin-Patch
 Content-Length: 318
 Keep-Alive: timeout=15, max=98
 Connection: Keep-Alive
 Content-Type: text/html; charset=iso-8859-1

 <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"> ...


.. As illustrated above, a client can send several HTTP requests over the same persistent TCP connection. However, it is important to note that all of these HTTP requests are considered to be independent by the server. Each HTTP request must be self-contained. This implies that each request must include all the header lines that are required by the server to understand the request. The independence of these requests is one of the important design choices of HTTP. As a consequence of this design choice, when a server processes a HTTP request, it doesn't' use any other information than what is contained in the request itself. This explains why the client adds its `User-Agent:` header in all of the HTTP requests it sends over the persistent TCP connection.

Como se ilustra más abajo, un cliente puede enviar varios requerimientos HTTP sobre la misma conexión TCP persistente. Sin embargo, es importante notar que todos estos requerimientos HTTP son considerados independientes por el servidor. Cada requerimiento HTTP debe ser autocontenido. Esto implica que cada uno debe incluir todas las líneas de cabecera que requiera el servidor para comprender la solicitud. La independencia de estos requerimientos es una de las decisiones de diseño importantes de HTTP. Como consecuencia de esta decisión de diseño, cuando un servidor procesa un requerimiento HTTP, no usa ninguna otra información que la contenida en el requerimiento mismo. Esto explica por qué el cliente agrega su cabecera `User-Agent:` en todos los requerimientos HTTP que envía sobre la conexión TCP persistente.

.. However, in practice, some servers want to provide content tuned for each user. For example, some servers can provide information in several languages or other servers want to provide advertisements that are targeted to different types of users. To do this, servers need to maintain some information about the preferences of each user and use this information to produce content matching the user's preferences. HTTP contains several mechanisms that enable to solve this problem. We discuss three of them below.

Sin embargo, en la práctica, algunos servidores quieren ofrecer contenido adaptado a cada usuario. Por ejemplo, pueden proveer información en varios idiomas, o incluir avisos destinados a diferentes tipos de usuarios. Para lograrlo, los servidores necesitan mantener alguna información sobre las preferencias de cada usuario, y usar esta información para producir contenido que corresponda a dichas preferencias. HTTP contiene varios mecanismos que posibilitan resolver este problema. A continuación discutimos tres de ellos.

.. A first solution is to force the users to be authenticated. This was the solution used by `FTP` to control the files that each user could access. Initially, user names and passwords could be included inside URIs :rfc:`1738`. However, placing passwords in the clear in a potentially publicly visible URI is completely insecure and this usage has now been deprecated :rfc:`3986`. HTTP supports several extension headers :rfc:`2617` that can be used by a server to request the authentication of the client by providing his/her credentials. However, user names and passwords have not been popular on web servers as they force human users to remember one user name and one password per server. Remembering a password is acceptable when a user needs to access protected content, but users will not accept the need for a user name and password only to receive targeted advertisements from the web sites that they visit.

Una primera solución es obligar a los usuarios a autenticarse. Ésta fue la solución usada por `FTP` para controlar los archivos que cada usuario podía acceder. Inicialmente, los nombres de usuario y passwords podían ser incluidos dentro de URIs :rfc:`1738`. Sin embargo, dejar passwords en texto claro en un URI, potencialmente visible en forma pública, es completamente inseguro, y este uso ha sido desaconsejado :rfc:`3986`. HTTP soporta varias cabeceras de extensión :rfc:`2617` que pueden ser usadas por un servidor para solicitar la autenticación del cliente proveyendo sus credenciales. Sin embargo, los nombres de usuario y passwords no han sido populares en los servidores Web, ya que obligan a los usuarios humanos a recordar nombre de usuario y password por cada servidor. Tener que recordar un password es aceptable cuando el usuario necesita acceder contenido protegido, pero nadie aceptará la necesidad de nombre de usuario y password sólo para recibir avisos personalizados de los sitios Web que visitan.

.. A second solution to allow servers to tune that content to the needs and capabilities of the user is to rely on the different types of `Accept-*` HTTP headers. For example, the `Accept-Language:` can be used by the client to indicate its preferred languages. Unfortunately, in practice this header is usually set based on the default language of the browser and it is not possible for a user to indicate the language it prefers to use by selecting options on each visited web server.

Una segunda solución para permitir a los servidores ajustar el contenido a las necesidades y capacidades del usuario es apoyarse en los diferentes tipos de cabecera HTTP `Accept-*` existentes. Por ejemplo, la cabecera `Accept-Language:` puede ser usada por el cliente para indicar sus lenguajes preferidos. Desafortunadamente, en la práctica esta cabecera se fija típicamente por el idioma por defecto del navegador, y no es posible, para un usuario, indicar el idioma que prefiere usar seleccionando opciones en cada servidor Web que visita.

.. The third, and widely adopted, solution are HTTP cookies. HTTP cookies were initially developed as a private extension by Netscape_. They are now part of the standard :rfc:`6265`. In a nutshell, a cookie is a short string that is chosen by a server to represent a given client. Two HTTP headers are used : `Cookie:` and `Set-Cookie:`. When a server receives an HTTP request from a new client (i.e. an HTTP request that does not contain the `Cookie:` header), it generates a cookie for the client and includes it in the `Set-Cookie:` header of the returned HTTP response. The `Set-Cookie:` header contains several additional parameters including the domain names for which the cookie is valid. The client stores all received cookies on disk and every time it sends a HTTP request, it verifies whether it already knows a cookie for this domain. If so, it attaches the `Cookie:` header to the HTTP request. This is illustrated in the figure below with HTTP 1.1, but cookies also work with HTTP 1.0.

La tercera solución, ampliamente adoptada, son las `cookies` HTTP. Fueron inicialmente desarrolladas como una extensión privada por Netscape_. Ahora son parte del estándar :rfc:`6265`. En pocas palabras, una `cookie` es una cadena corta, elegida por un servidor para representar a un cliente dado. Las dos cabeceras relacionadas son `Cookie:` y `Set-Cookie:`. Cuando un servidor recibe un requerimiento HTTP de un nuevo cliente (es decir, un requerimiento HTTP que no contiene la cabecera `Cookie:`), genera una cookie para el cliente y la incluye en la cabecera `Set-Cookie:` de la respuesta HTTP que devuelve. La cabecera `Set-Cookie:` contiene varios parámetros adicionales, incluyendo los nombres de dominio para los cuales es válida la cookie. El cliente almacena todas las cookies recibidas en disco, y cada vez que envía un requerimiento HTTP, verifica si ya tiene una cookie conocida para ese dominio. Si es así, adjunta la cabecera `Cookie:` al requerimiento HTTP. Esto se ilustra en la figura más abajo, con HTTP 1.1, aunque las cookies también funcionan con HTTP 1.0.

.. figure:: svg/http-cookies.png
   :align: center
   :scale: 60 

   Cookies HTTP 

.. .. note:: Privacy issues with HTTP cookies

 The HTTP cookies introduced by Netscape_ are key for large e-commerce websites. However, they have also raised many discussions concerning their `potential misuses <http://www.nytimes.com/2001/09/04/technology/04COOK.html>`_. Consider `ad.com`, a company that delivers lots of advertisements on web sites. A web site that wishes to include `ad.com`'s advertisements next to its content will add links to `ad.com` inside its HTML pages. If `ad.com` is used by many web sites, `ad.com` could be able to track the interests of all the users that visit its client websites and use this information to provide targeted advertisements. Privacy advocates have even `sued <http://epic.org/privacy/internet/cookies/>`_ online advertisement companies to force them to comply with the privacy regulations. More recent related technologies also raise `privacy concerns <http://www.eff.org/deeplinks/2009/09/new-cookie-technologies-harder-see-and-remove-wide>`_ 
 
.. note:: Aspectos de privacidad con cookies HTTP

 Las `cookies` HTTP introducidas por Netscape_ resultan clave para los sitios Web de comercio electrónico. Sin embargo, también han originado discusiones acerca de su `potencial mal uso <http://www.nytimes.com/2001/09/04/technology/04COOK.html>`_. Consideremos `ad.com`, una empresa imaginaria que distribuye grandes cantidades de avisos en sitios Web. Un sitio Web que desea incluir los avisos de `ad.com` junto a sus contenidos, agregará enlaces a `ad.com` dentro de sus páginas HTML. Si hay muchos sitios Web que usan los servicios de `ad.com`, esta empresa podría ser capaz de seguir la pista de los intereses de cada usuario que visite a sus sitios cliente, y usar esta información para ofrecer anuncios focalizados. Los defensores de la privacidad han llegado a promover `juicio  <http://epic.org/privacy/internet/cookies/>`_ a empresas de publicidad en línea para obligarlas a satisfacer las regulaciones de privacidad. Hay otras tecnologías relacionadas, más recientes, que también suscitan `preocupaciones de privacidad <http://www.eff.org/deeplinks/2009/09/new-cookie-technologies-harder-see-and-remove-wide>`_.

.. rubric:: Footnotes

.. .. [#furiretrieve] An example of a non-retrievable URI is `urn:isbn:0-380-81593-1` which is an unique identifier for a book, through the urn scheme (see :rfc:`3187`). Of course, any URI can be make retrievable via a dedicated server or a new protocol but this one has no explicit protocol. Same thing for the scheme tag (see :rfc:`4151`), often used in Web syndication (see :rfc:`4287` about the Atom syndication format). Even when the scheme is retrievable (for instance with http`), it is often used only as an identifier, not as a way to get a resource. See  http://norman.walsh.name/2006/07/25/namesAndAddresses for a good explanation.

.. [#furiretrieve] Un ejemplo de URI no recuperable es `urn:isbn:0-380-81593-1`, que es un identificador único para un libro, a través del esquema `urn` (ver :rfc:`3187`). Por supuesto que cualquier URI puede hacerse recuperable mediante un servidor dedicado o un nuevo protocolo, pero éste no tiene un protocolo explícito. Lo mismo para el esquema `tag` (ver :rfc:`4151`), con frecuencia usado en `redifusión` Web (o `Web syndication`; ver :rfc:`4287` acerca del formato de redifusión Atom). Aun cuando el esquema es recuperable (por ejemplo, con `http`), a menudo se usa sólo como un identificador, no como una forma de obtener un recurso. Véase una buena explicación en http://norman.walsh.name/2006/07/25/namesAndAddresses.

.. .. [#furilist] The list of standard URI schemes is maintained by IANA_ at http://www.iana.org/assignments/uri-schemes.html
.. [#furilist] La lista de esquemas URI estándar es mantenida por IANA_ en http://www.iana.org/assignments/uri-schemes.html.

.. .. [#ffavicon] Favorite icons are small icons that are used to represent web servers in the toolbar of Internet browsers. Microsoft added this feature in their browsers without taking into account the W3C standards. See http://www.w3.org/2005/10/howto-favicon for a discussion on how to cleanly support such favorite icons.

.. [#ffavicon] Los íconos favoritos (`favicons`) son pequeños íconos usados para representar servidores Web en la barra de herramientas de los navegadores de Internet. Microsoft agregó esta peculiaridad en sus navegadores sin tener en cuenta los estándares de W3C. Véase en http://www.w3.org/2005/10/howto-favicon una discusión sobre cómo soportar de manera limpia estos íconos favoritos.

.. include:: /links.rst
