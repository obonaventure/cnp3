.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Ejercicios
##########

.. This section contains several exercises and small challenges about the application layer protocols.
Esta sección contiene varios ejercicios y pequeños desafíos sobre los protocolos de capa de Aplicación.

El Sistema de Nombres de Dominio
================================

.. The Domain Name System (DNS) plays a key role in the Internet today as it allows applications to use fully qualified domain names (FQDN) instead of IPv4 or IPv6 addresses. Many tools enable queries through DNS servers. For this exercise, we will use dig_ which is installed on most Unix systems. 

El Sistema de Nombres de Dominio (`Domain Name System`, DNS) juega un rol crucial hoy en Internet, ya que permite a las aplicaciones usar nombres de dominio completamente calificados (FQDN) en vez de direcciones IPv4 o IPv6. Existen muchas herramientas que ofrecen la posibilidad de hacer consultas a través de los servidores DNS. Para este ejercicio, usaremos dig_, que viene instalado en la mayoría de los sistemas Unix. 

.. A typical usage of dig is as follows 
Un uso típico de dig es el siguiente:

.. code-block:: text

  dig @server -t type fqdn 

donde

.. - `server` is the IP address or the name of a DNS server or resolver
.. - `type` is the type of DNS record that is requested by the query such as `NS` for a nameserver, `A` for an IPv4 address, `AAAA` for an IPv6 address, `MX` for a mail relay, ...
.. - `fqdn` is the fully qualified domain name being queried

 - `server` es la dirección IP o el nombre de un servidor o resolver DNS
 - `type` es el tipo de registro DNS que se requiere con la consulta, como por ejemplo `NS` para nameserver, `A` para dirección IPv4, `AAAA` para dirección IPv6, `MX` para mail exchanger, ...
 - `fqdn` es el nombre de dominio copletamente calificado

.. 1. What are the IP addresses of the resolvers that the `dig` implementation you are using relies on [#fdig]_ ?
1. ¿Cuáles son las direcciones IP de los resolvers utilizados por la implementación de `dig` que usted está usando? [#fdig]_

.. 2. What is the IP address that corresponds to `inl.info.ucl.ac.be` ? Which type of DNS query does `dig` send to obtain this information ?
2. ¿Cuál es la dirección IP correspondiente a `inl.info.ucl.ac.be`? ¿Qué tipo de consulta DNS emite `dig` para obtener esta información?

.. 3. Which type of DNS request do you need to send to obtain the nameservers that are responsible for a given domain ?
3. ¿Qué tipo de consulta DNS se necesita enviar para obtener los nameservers que son responsables para un cierto dominio?

.. 4. What are the nameservers that are responsible for the `be` top-level domain ? Where are they located ? Is it possible to use IPv6 to query them ?
4. ¿Cuáles son los nameservers que son responsables por el dominio `be`? ¿Dónde están ubicados? ¿Es posible usar IPv6 para consultarlos?

.. 5. When run without any parameter, `dig` queries one of the root DNS servers and retrieves the list of the names of all root DNS servers. For technical reasons, there are only 13 different root DNS servers. This information is also available as a text file from http://www.internic.net/zones/named.root What are the IP addresses of all these servers. Do they all support IPv6 [#rs]_ ? 

5. Al ser ejecutado sin ningún parámetro, `dig` consulta uno de los servers DNS raíz y recupera la lista de los nombres de todos los servidores raíz. Por razones técnicas, existen sólo 13 diferentes servidores DNS raíz. Esta información también está disponible como archivo de texto en http://www.internic.net/zones/named.root. ¿Cuáles son las direcciones IP de todos estos servidores? ¿Todos ellos soportan IPv6? [#rs]_ 

.. 6. Assume now that you are residing in a network where there is no DNS resolver and that you need to start your query from the DNS root.

..   - Use `dig` to send a query to one of these root servers to find the IP address of the DNS server(s) (NS record) responsible for the `org` top-level domain
..   - Use `dig` to send a query to one of these DNS servers to find the IP address of the DNS server(s) (NS record) responsible for root-servers.org`
..   - Continue until you find the server responsible for `www.root-servers.org`
..   - What is the lifetime associated to this IP address ?

6. Supongamos que usted reside en una red donde no existe resolver DNS y que usted necesita comenzar su consulta desde la raíz del DNS. 

   - Usando `dig`, envíe una consulta a uno de estos servidores raíz para encontrar la dirección IP de los servidores DNS (registro NS) responsables por el dominio top-level `org`.
   - Usando `dig` envíe una consulta a uno de estos servidores DNS para hallar la dirección IP del servidor DNS (registro NS) responsable por el dominio `root-servers.org`.
   - Continúe hasta hallar el servidor responsable por `www.root-servers.org`
   - ¿Cuál es el tiempo de vida asociado a esta dirección IP?

.. 7. Perform the same analysis for a popular website such as `www.google.com`. What is the lifetime associated to this IP address ? If you perform the same request several times, do you always receive the same answer ? Can you explain why a lifetime is associated to the DNS replies ?
7. Ejecute el mismo análisis para un sitio web popular tal como `www.google.com`. ¿Cuál es el tiempo de vida asociado a esta dirección IP? Si ejecuta la misma consulta varias veces, ¿recibe siempre la misma respuesta? ¿Puede explicar por qué se asocia un tiempo de vida a las respuestas DNS?

.. 8. Use `dig` to find the mail relays used by the `uclouvain.be` and `gmail.com` domains. What is the `TTL` of these records ? Can you explain the preferences used by the `MX` records. You can find more information about the MX records in :rfc:`5321`
8. Use `dig` para hallar los mail exchangers usados por los dominios `uclouvain.be` y `gmail.com`. ¿Cuál es el `TTL` de estos registros? ¿Puede explicar las preferencias usadas por los registros `MX`? Puede encontrar más información sobre los registros MX en :rfc:`5321`.

.. 9. Use `dig` to query the IPv6 address (DNS record AAAA) of the following hosts

..   - `www.sixxs.net`
..   - `www.ietf.org`
..   - `ipv6.google.com`

9. Use `dig` para encontrar la dirección IPv6 (registro DNS tipo AAAA) de los siguientes hosts:

   - `www.sixxs.net`
   - `www.ietf.org`
   - `ipv6.google.com`

.. 10. When `dig` is run, the header section in its output indicates the `id` the DNS identifier used to send the query. Does your implementation of `dig` generates random identifiers ?

10. Al ejecutar `dig`, la sección de cabecera en la salida del programa indica el `id o identificador DNS (`DNS identifier`) usado para enviar la consulta. Su implementación de `dig` ¿genera identificadores aleatorios?  

.. code-block:: text

	dig -t MX gmail.com

	; <<>> DiG 9.4.3-P3 <<>> -t MX gmail.com
	;; global options:  printcmd   
	;; Got answer:
	;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25718

.. 11. A DNS implementation such as `dig` and more importantly a name resolver such as bind_ or unbound_, always checks that the received DNS reply contains the same identifier as the DNS request that it sent. Why is this so important ?

..   - Imagine an attacker who is able to send forged DNS replies to, for example, associate `www.bigbank.com` to his own IP address. How could he attack a DNS implementation that

..     - sends DNS requests containing always the same identifier
..     - sends DNS requests containing identifiers that are incremented by one after each request
..     - sends DNS requests containing random identifiers


11. Una implementación DNS como `dig`, y con mayor importancia, un name resolver, como bind_ o unbound_, siempre verifican que las respuestas DNS contengan el mismo identificador que la consulta DNS que enviaron. ¿Por qué es esto tan importante?

   - Imaginemos un atacante que pueda enviar respuestas DNS falsas para asociar, por ejemplo, `www.bigbank.com` con su propia dirección IP. ¿De qué manera podría él atacar a una implementación DNS que:

     - envíe consultas DNS conteniendo siempre el mismo identificador
     - envíe consultas DNS conteniendo identificadores que se incrementan en uno luego de cada consulta
     - envíe consultas DNS conteniendo siempre identificadores aleatorios

.. 12. The DNS protocol can run over UDP and over TCP. Most DNS servers prefer to use UDP because it consumes fewer resources on the server. However, TCP is useful when a large answer is expected or when a large answer is expected. Use `time dig +tcp` to query a root DNS server. Is it faster to receive an answer via TCP or via UDP ?

12. El protocolo DNS puede correr sobre UDP y sobre TCP. La mayoría de los servidores prefieren usar UDP porque consume menos recursos del servidor. Sin embargo, TCP es útil cuando se espera una respuesta voluminosa. Use `time dig +tcp` para consultar un servidor DNS raíz. ¿Es más rápido recibir una respuesta a través de TCP o de UDP?

Protocolos de correo electrónico de Internet
============================================

.. Many Internet protocols are ASCII_-based protocols where the client sends requests as one line of ASCII_ text terminated by `CRLF` and the server replies with one of more lines of ASCII_ text. Using such ASCII_ messages has several advantages compared to protocols that rely on binary encoded messages

..   - the messages exchanged by the client and the server can be easily understood by a developer or network engineer by simply reading the messages
..   - it is often easy to write a small prototype that implements a part of the protocol
..   - it is possible to test a server manually by using telnet Telnet is a protocol that allows to obtain a terminal on a remote server. For this, telnet opens a TCP connection with the remote server on port 23. However, most `telnet` implementations allow the user to specify an alternate port as `telnet hosts port` When used with a port number as parameter, `telnet` opens a TCP connection to the remote host on the specified port. `telnet` can thus be used to test any server using an ASCII-based protocol on top of TCP. Note that if you need to stop a running `telnet` session, ``Ctrl-C`` will not work as it will be sent by `telnet` to the remote host over the TCP connection. On many `telnet` implementations you can type ``Ctrl-]`` to freeze the TCP connection and return to the telnet interface.

En muchos protocolos de Internet, basados en ASCII_, el cliente envía consultas en forma de una línea de texto ASCII_ terminada por `CRLF`, y el servidor responde con una o más líneas de texto ASCII_. Usar estos mensajes ASCII_ tiene varias ventajas sobre protocolos que descansan en mensajes con codificación binaria.

   - Los mensajes intercambiados por cliente y servidor pueden ser fácilmente comprendidos por un desarrollador o ingeniero de redes simplemente leyendo los mensajes.
   - Suele ser fácil escribir un pequeño prototipo que implemente parte de un protocolo.
   - Es posible verificar manualmente un servidor usando telnet. Telnet es un protocolo que permite obtener una terminal sobre un servidor remoto. Para esto, telnet abre una conexión TCP con el servidor remoto sobre el puerto 23. Sin embargo, la mayoría de las implementaciones de telnet permiten al usuario especificar un puerto alternativo, en la forma `telnet <host> <puerto>`. Cuando se usa con un número de puerto como parámetro, `telnet` abre una conexión TCP al host remoto, sobre el puerto especificado. Así `telnet` puede ser usado para probar un servidor usando un protocolo basado en ASCII, encima de TCP. Nótese que si necesitamos detener una sesión `telnet` que esté en marcha, la combinación de teclas ``Ctrl-C`` no funcionará, ya que será enviada por `telnet` al host remoto sobre la conexión TCP. En muchas implementaciones de `telnet`, podemos teclear ``Ctrl-]`` para congelar la conexión TCP y volver a la interfaz de telnet.



.. 1. Assume that your are sending an email from your `@student.uclouvain.be` inside the university to another student's `@student.uclouvain.be` address. Which protocols are involved in the transmission of this email ?
1. Supongamos que usted envía un email desde su cuenta `alfa@student.uclouvain.be` dentro de la universidad, a otro estudiante con dirección `beta@student.uclouvain.be`. ¿Qué protocolos están involucrados en la transmisión de este email?

.. 2. Same question when you are sending an email from  your `@student.uclouvain.be` inside the university to another student's `@gmail.com` address
2. La misma pregunta, para el caso en que usted envía un email desde su cuenta  `alfa@student.uclouvain.be` dentro de la universidad a la dirección de otro estudiante, `beta@gmail.com`.

.. 3. Before the advent of webmail and feature rich mailers, email was written and read by using command line tools on servers. Using your account on `sirius.info.ucl.ac.be` use the `/bin/mail` command line tool to send an email to yourself *on this host*. This server stores local emails in the `/var/mail` directory with one file per user. Check with `/bin/more` the content of your mail file and try to understand which lines have been added by the server in the header of your email.
3. Antes de la llegada del webmail y los programas de correo ricos en características, el email se escribía y se leía usando herramientas de línea de comandos disponibles en servidores. Usando su cuenta en `sirius.info.ucl.ac.be`, use la herramienta de línea de comandos `/bin/mail` para enviarse un email a sí mismo en este host.  Este servidor almacena emails locales en el directorio `/var/mail`, con un archivo por usuario. Verifique el contenido de su mail con `/bin/more`y trate de comprender qué líneas de cabecera han sido añadidas por el servidor.

.. 4. Use your preferred email tool to send an email message to yourself containing a single line of text. Most email tools have the ability to show the `source` of the message, use this function to look at the message that you sent and the message that you received. Can you find an explanation for all the lines that have been added to your single line email [#fsmtpevol]_ ?
4. Use su herramienta de email preferida para enviarse un mensaje de email a sí mismo, conteniendo una sola línea de texto. La mayoría de las herramientas de mail tienen la capacidad de mostrar el `fuente` del mensaje; use esta función para ver el mensaje que ha enviado y el que ha recibido. ¿Puede hallar una explicación para todas las líneas que han sido agregadas a su email de una sola línea [#fsmtpevol]_?

.. 5. The first version of the SMTP protocol was defined in :rfc:`821`. The current draft standard for SMTP is defined in :rfc:`5321` Considering only :rfc:`821` what are the main commands of the `SMTP` protocol [#fsmtp]_ ? 
5. La primera versión del protocolo SMTP fue definida en :rfc:`821`. El estándar borrador actual para SMTP se define en :rfc:`5321`. Considerando únicamente :rfc:`821`, ¿cuál es son los principales comandos del protocolo SMTP [#fsmtp]_? 

.. 6. When using SMTP, how do you recognise a positive reply from a negative one ?
6. Al usar SMTP, ¿cómo diferenciar una respuesta positiva de una negativa?

.. 7. A SMTP server is a daemon process that can fail due to a bug or lack of resources (e.g. memory). Network administrators often install tools [#fmonitoring]_ that regularly connect to their servers to check that they are operating correctly. A simple solution is to open a TCP connection on port 25 to the SMTP server's host [#fblock]_ . If the connection is established, this implies that there is a process listening. What is the reply sent by the SMTP server when you type the following command ? 

7. Un servidor SMTP es un proceso `daemon` que puede fallar debido a un error o a falta de recursos (como, por ejemplo, memoria). Los administradores de red a veces instalan herramientas [#fmonitoring]_ que se conectan periódicamente a sus servidores para verificar que están operando correctamente. Una solución simple es abrir una conexión TCP sobre el puerto 25 al host donde reside el servidor SMTP [#fblock]_. Si se establece la conexión, esto implica que hay un proceso escuchando. ¿Cuál es la respuesta enviada por el servidor SMTP cuando se tipea el siguiente comando?

 .. code-block:: text

   telnet cnp3.info.ucl.ac.be 25
 
.. *Warning* : Do *not* try this on a random SMTP server. The exercises proposed in this section should only be run on the SMTP server dedicated for these exercises : `cnp3.info.ucl.ac.be`. If you try them on a production SMTP server, the administrator of this server may become angry.

 *Aviso* : *No trate* de hacer esto sobre un servidor SMTP arbitrario. Los ejercicios que se proponen en esta sección sólo deben ser ejecutados sobre el servidor dedicado para estos ejercicios. Si los prueba sobre un servidor SMTP en producción, el administrador de este server puede montar en cólera.

.. 8. Continue the SMTP session that you started above by sending the greetings command (`HELO` followed by the fully qualified domain name of your host) and end the session by sending the `QUIT` command.
8. Continúe la sesión SMTP que comenzó anteriormente enviando los comandos de saludo (`HELO`, seguido por el nombre de dominio completamente calificado para su host) y termine la sesión enviando el comando `QUIT`.

9. The minimum SMTP session above allows to verify that the SMTP is running. However, this does not always imply that mail can be delivered. For example, large SMTP servers often use a database to store all the email addresses that they serve. To verify the correct operation of such a server, one possibility is to use the `VRFY` command. Open a SMTP session on the lab's SMTP server (`cnp3.info.ucl.ac.be`) and use this command to verify that your account is active. 

10. Now that you know the basics of opening and closing an SMTP session, you can now send email manually by using the `MAIL FROM:`, `RCPT TO:` and `DATA` commands. Use these commands to *manually* send an email to `INGI2141@cnp3.info.ucl.ac.be` . Do not forget to include the `From:`, `To:` and `Subject:` lines in your header.

.. look at the emails sent by the students
 
11. By using SMTP, is it possible to send an email that contains exactly the following ASCII art ? 

.. figure:: pkt/ascii-art.png
   :align: center
   :scale: 100

12. Most email agents allow you to send email in carbon-copy (`cc:`) and also in blind-carbon-copy (`bcc:`) to a recipient. How does a SMTP server supports these two types of recipients ?

13. In the early days, email was read by using tools such as `/bin/mail` or more advanced text-based mail readers such as pine_ or elm_ . Today, emails are stored on dedicated servers and retrieved by using protocols such as POP_ or IMAP_ From the user's viewpoint, can you list the advantages and drawbacks of these two protocols ?

14. The TCP protocol supports 65536 different ports numbers. Many of these port numbers have been reserved for some applications. The official repository of the reserved port numbers is maintained by the Internet Assigned Numbers Authority (IANA_) on http://www.iana.org/assignments/port-numbers [#fservices]_ Using this information, what is the default port number for the POP3 protocol ? Does it run on top of UDP or TCP ?

15. The Post Office Protocol (POP) is a rather simple protocol described in :rfc:`1939`. POP operates in three phases. The first phase is the authorization phase where the client provides a username and a password. The second phase is the transaction phase where the client can retrieve emails. The last phase is the update phase where the client finalises the transaction. What are the main POP commands and their parameters ? When a POP server returns an answer, how can you easily determine whether the answer is positive or negative ? 

16. On smartphones, users often want to avoid downloading large emails over a slow wireless connection. How could a POP client only download emails that are smaller than 5 KBytes ?

17. Open a POP session with the lab's POP server (`cnp3.info.ucl.ac.be`) by using the username and password that you received. Verify that your username and password are accepted by the server.

18. The lab's POP server contains a script that runs every minute and sends two email messages to your account if your email folder is empty. Use POP to retrieve these two emails and provide the secret message to your teaching assistant. 

.. the magic words are squeamish ossifrage from RSA129

The HyperText Transfer Protocol
===============================


1. What are the main methods supported by the first version of the HyperText Transfer Protocol (HTTP) defined in :rfc:`1945` [#fhttp1]_ ? What are the main types of replies sent by a http server [#fhttp2]_ ?

2.  System administrators who are responsible for web servers often want to monitor these servers and check that they are running correctly. As a HTTP server uses TCP on port 80, the simplest solution is to open a TCP connection on port 80 and check that the TCP connection is accepted by the remote host. However, as HTTP is an ASCII-based protocol, it is also very easy to write a small script that downloads a web page on the server and compares its content with the expected one. Use `telnet` to verify that a web server is running on host `rembrandt.info.ucl.ac.be` [#fhttp]_


3. Instead of using `telnet` on port 80, it is also possible to use a command-line tool such as curl_ Use curl_ with the `--trace-ascii tracefile` option to store in `tracefile` all the information exchanged by curl when accessing the server.

   - what is the version of HTTP used by curl ?
   - can you explain the different headers placed by curl in the request ?
   - can you explain the different headers found in the response ?

4. HTTP 1.1, specified in :rfc:`2616` forces the client to use the `Host:` in all its requests. HTTP 1.0 does not define the `Host:` header, by most implementations support it. By using `telnet` and `curl` retrieve the first page of the http://totem.info.ucl.ac.be webserver by sending http requests with and without the `Host:` header. Explain the difference between the two [#ftotem]_ . 

5. By using dig_ and curl_ , determine on which physical host the http://www.info.ucl.ac.be, http://inl.info.ucl.ac.be and http://totem.info.ucl.ac.be are hosted

6. Use curl_ with the `--trace-ascii filename` to retrieve http://www.google.com . Explain what a browser such as firefox would do when retrieving this URL.

7. The headers sent in a HTTP request allow the client to provide additional information to the server. One of these headers is the `Accept-Language` header that allows to indicate the preferred language of the client [#lang]_. For example, `curl -HAccept-Language:en http://www.google.be' will send to `http://www.google.be` a HTTP request indicating English (en) as the preferred language. Does google provide a different page in French (fr) and Walloon (wa) ? Same question for `http://www.uclouvain.be` (given the size of the homepage, use ``diff`` to compare the different pages retrieved from `www.uclouvain.be`)

8. Compare the size of the http://www.yahoo.com and http://www.google.com web pages by downloading them with curl_

9. What is a http cookie ? List some advantages and drawbacks of using cookies on web servers.

10. You are now responsible for the `http://www.belgium.be`. The government has built two datacenters_ containing 1000 servers each in Antwerp and Namur. This website contains static information and your objective is to balance the load between the different servers and ensures that the service remains up even if one of the datacenters is disconnected from the Internet due to flooding or other natural disasters. What are the techniques that you can use to achieve this goal ?

.. rubric:: Footnotes

.. [#fdig] On a Linux machine, the *Description* section of the `dig` manpage tells you where `dig` finds the list of nameservers to query.

.. [#rs] You may obtain additional information about the root DNS servers from http://www.root-servers.org

.. [#fblock] Note that using `telnet` to connect to a remote host on port 25 may not work in all networks. Due to the spam_ problem, many :term:`ISP` networks do not allow their customers to use port TCP 25 directly and force them to use the ISP's mail relay to forward their email. Thanks to this, if a software sending spam has been installed on the PC of one of the ISP's customers, this software will not be able to send a huge amount of spam. If you connect to `cnp3.info.ucl.ac.be` from the fixed stations in INGI's lab, you should not be blocked.

.. [#fmonitoring] There are many `monitoring tools <http://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems>`_ available. nagios_ is a very popular open source monitoring system. 

.. [#fsmtp] A shorter description of the SMTP protocol may be found on wikipedia at http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol

.. [#fsmtpevol] Since :rfc:`821`, SMTP has evolved a lot due notably to the growing usage of email and the need to protect the email system against spammers. It is unlikely that you will be able to explain all the additional lines that you will find in email headers, but we'll discuss them together.

.. [#fservices] On Unix hosts, a subset of the port assignments is often placed in `/etc/services`

.. [#fhttp] The minimum command sent to a HTTP server is `GET / HTTP/1.0` followed by CRLF and a blank line

.. [#fhttp1] See section 5 of :rfc:`1945`

.. [#fhttp2] See section 6.1 of :rfc:`1945`

.. [#ftotem] Use dig_ to find the IP address used by `totem.info.ucl.ac.be`

.. [#lang] The list of available language tags can be found at http://www.iana.org/assignments/language-subtag-registry Versions in other formats are available at http://www.langtag.net/registries.html Additional information about the support of multiple languages in Internet protocols may be found in rfc5646_




