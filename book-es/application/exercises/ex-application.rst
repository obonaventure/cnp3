.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Ejercicios
##########

El Sistema de Nombres de Dominio
================================

El Sistema de Nombres de Dominio (`Domain Name System`, DNS) juega un rol crucial hoy en Internet, ya que permite a las aplicaciones usar nombres de dominio completamente calificados (FQDN) en vez de direcciones IPv4 o IPv6. Existen muchas herramientas que ofrecen la posibilidad de hacer consultas a través de los servidores DNS. Para este ejercicio, usaremos `dig`_, que viene instalado en la mayoría de los sistemas Unix. 

Esta sección contiene varios ejercicios y pequeños desafíos sobre los protocolos de capa de Aplicación.

Un uso típico de `dig` es el siguiente:

.. code-block:: text

  dig @server -t type fqdn 

donde

 - `server` es la dirección IP o el nombre de un servidor o resolver DNS.
 - `type` es el tipo de registro DNS que se requiere con la consulta, como por ejemplo `NS` para nameserver, `A` para dirección IPv4, `AAAA` para dirección IPv6, `MX` para mail exchanger, ...
 - `fqdn` es el nombre de dominio completamente calificado.


#. ¿Cuáles son las direcciones IP de los resolvers utilizados por la implementación de `dig` que usted está usando? [#fdig]_

#. ¿Cuál es la dirección IP correspondiente a `inl.info.ucl.ac.be`? ¿Qué tipo de consulta DNS emite `dig` para obtener esta información?

#. ¿Qué tipo de consulta DNS se necesita enviar para obtener los nameservers que son responsables para un cierto dominio?

#. ¿Cuáles son los nameservers que son responsables por el dominio `be`? ¿Dónde están ubicados? ¿Es posible usar IPv6 para consultarlos?

#. Al ser ejecutado sin ningún parámetro, `dig` consulta uno de los servers DNS raíz y recupera la lista de los nombres de todos los servidores raíz. Por razones técnicas, existen sólo 13 diferentes servidores DNS raíz. Esta información también está disponible como archivo de texto en http://www.internic.net/zones/named.root. ¿Cuáles son las direcciones IP de todos estos servidores? ¿Puede hacérseles consultas a través de IPv6? [#rs]_ 


#. Supongamos que usted reside en una red donde no existe resolver DNS y que usted necesita comenzar su consulta desde la raíz del DNS. 

   - Usando `dig`, envíe una consulta a uno de estos servidores raíz para encontrar la dirección IP de los servidores DNS (registro NS) responsables por el dominio top-level `org`.
   - Usando `dig` envíe una consulta a uno de estos servidores DNS para hallar la dirección IP del servidor DNS (registro NS) responsable por el dominio `root-servers.org`.
   - Continúe hasta hallar el servidor responsable por `www.root-servers.org`
   - ¿Cuál es el tiempo de vida asociado a esta dirección IP?

#. Ejecute el mismo análisis para un sitio web popular tal como `www.google.com`. ¿Cuál es el tiempo de vida asociado a esta dirección IP? Si ejecuta la misma consulta varias veces, ¿recibe siempre la misma respuesta? ¿Puede explicar por qué se asocia un tiempo de vida a las respuestas DNS?

#. Use `dig` para hallar los mail exchangers usados por los dominios `uclouvain.be` y `gmail.com`. ¿Cuál es el `TTL` de estos registros? ¿Puede explicar las preferencias usadas por los registros `MX`? Puede encontrar más información sobre los registros MX en :rfc:`974`.

#. Use `dig` para encontrar la dirección IPv6 (registro DNS tipo AAAA) de los siguientes hosts:

   - `www.sixxs.net`
   - `www.ietf.org`
   - `ipv6.google.com`

#. Al ejecutar `dig`, la sección de cabecera en la salida del programa indica el `id` o identificador DNS (`DNS identifier`) usado para enviar la consulta. Su implementación de `dig` ¿genera identificadores aleatorios?

.. code-block:: text

	dig -t MX gmail.com

	; <<>> DiG 9.4.3-P3 <<>> -t MX gmail.com
	;; global options:  printcmd   
	;; Got answer:
	;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25718

#. Una implementación DNS como `dig`, y con mayor importancia, un name resolver, como bind_ o unbound_, siempre verifican que las respuestas DNS recibidas contengan el mismo identificador que la consulta DNS que enviaron. ¿Por qué es esto tan importante? Imaginemos un atacante que pueda enviar respuestas DNS falsas para asociar, por ejemplo, `www.bigbank.com` con su propia dirección IP. ¿De qué manera podría él atacar a una implementación DNS que envíe consultas DNS:

     - conteniendo siempre el mismo identificador?
     - conteniendo identificadores que se incrementan en uno luego de cada consulta?
     - conteniendo siempre identificadores aleatorios?

#. El protocolo DNS puede correr sobre UDP y sobre TCP. La mayoría de los servidores prefieren usar UDP porque consume menos recursos del servidor. Sin embargo, TCP es útil cuando se espera una respuesta voluminosa. Usando `dig +tcp` puede forzarse el uso de TCP. Utilice el comando ``time dig +tcp`` para consultar un servidor DNS raíz y registrar el tiempo insumido. Consulte un servidor DNS raíz usando TCP y UDP. ¿Es más rápido recibir una respuesta a través de TCP o de UDP?

Protocolos de correo electrónico de Internet
============================================


En muchos protocolos de Internet, basados en ASCII_, el cliente envía consultas en forma de una línea de texto ASCII_ terminada por `CRLF`, y el servidor responde con una o más líneas de texto ASCII_. Usar estos mensajes ASCII_ tiene varias ventajas sobre protocolos que descansan en mensajes con codificación binaria.

   - Los mensajes intercambiados por cliente y servidor pueden ser fácilmente comprendidos por un desarrollador o ingeniero de redes simplemente leyendo los mensajes.
   - Suele ser fácil escribir un pequeño prototipo que implemente parte de un protocolo.
   - Es posible verificar manualmente un servidor usando telnet. Telnet es un protocolo que permite obtener una terminal sobre un servidor remoto. Para esto, telnet abre una conexión TCP con el servidor remoto sobre el puerto 23. Sin embargo, la mayoría de las implementaciones de telnet permiten al usuario especificar un puerto alternativo, en la forma ``telnet <host> <puerto>``. Cuando se usa con un número de puerto como parámetro, `telnet` abre una conexión TCP al host remoto, sobre el puerto especificado. Así `telnet` puede ser usado para probar un servidor usando un protocolo basado en ASCII, encima de TCP. Nótese que si necesitamos detener una sesión `telnet` que esté en marcha, la combinación de teclas ``Ctrl-C`` no funcionará, ya que será enviada por `telnet` al host remoto sobre la conexión TCP. En muchas implementaciones de `telnet`, podemos teclear ``Ctrl-]`` para congelar la conexión TCP y volver a la interfaz de telnet.



#. Supongamos que Alice envía un email desde su cuenta `alice@yahoo.com`, a Bob, con dirección `bob@yahoo.com`. ¿Qué protocolos están involucrados en la transmisión de este email?

#. La misma pregunta, para el caso en que Alice envía un email a su amiga Trudy, `trudy@gmail.com`.

#. Antes de la llegada del webmail y los programas de correo ricos en características, el email se escribía y se leía usando herramientas de línea de comandos disponibles en servidores. Usando su cuenta en `sirius.info.ucl.ac.be`, use la herramienta de línea de comandos `/bin/mail` para enviarse un email a sí mismo en este host.  Este servidor almacena emails locales en el directorio `/var/mail`, con un archivo por usuario. Verifique el contenido de su mail con `/bin/more` y trate de comprender qué líneas de cabecera han sido añadidas por el servidor.

#. Use su herramienta de email preferida para enviarse un mensaje de email a sí mismo, conteniendo una sola línea de texto. La mayoría de las herramientas de mail tienen la capacidad de mostrar el `texto fuente` del mensaje; use esta función para ver el mensaje que ha enviado y el que ha recibido. ¿Puede hallar una explicación para todas las líneas que han sido agregadas a su email de una sola línea [#fsmtpevol]_?

#. La primera versión del protocolo SMTP fue definida en :rfc:`821`. El estándar borrador actual para SMTP se define en :rfc:`5321`. Considerando únicamente :rfc:`821`, ¿cuál es son los principales comandos del protocolo SMTP [#fsmtp]_? 

#. Al usar SMTP, ¿cómo diferenciar una respuesta positiva de una negativa?

#. Un servidor SMTP es un proceso `daemon` que puede fallar debido a un error o a falta de recursos (como, por ejemplo, memoria). Los administradores de red a veces instalan herramientas [#fmonitoring]_ que se conectan periódicamente a sus servidores para verificar que están operando correctamente. Una solución simple es abrir una conexión TCP sobre el puerto 25 al host donde reside el servidor SMTP [#fblock]_. Si se establece la conexión, esto implica que hay un proceso escuchando. ¿Cuál es la respuesta enviada por el servidor SMTP cuando se tipea el comando ``telnet cnp3.info.ucl.ac.be 25``?

.. warning:: 
 *No trate de hacer esto* sobre un servidor SMTP arbitrario. Los ejercicios que se proponen en esta sección sólo deben ser ejecutados sobre el servidor dedicado para estos ejercicios. Si los prueba sobre un servidor SMTP en producción, el administrador de este server puede enojarse peligrosamente.

#. Continúe la sesión SMTP que comenzó anteriormente enviando los comandos de saludo (`HELO`, seguido por el nombre de dominio completamente calificado para su host) y termine la sesión enviando el comando `QUIT`.

#. La sesión SMTP minimal desarrollada anteriormente permite verificar que SMTP está activo. Sin embargo, esto no siempre implica que pueda enviarse correo. Por ejemplo, los servidores SMTP grandes suelen usar una base de datos para almacenar todas direcciones de email que sirven. Para verificar la operación correcta de dicho servidor, una posibilidad es usar el comando `VRFY`. Abra una sesión SMTP en el servidor SMTP del laboratorio (`cnp3.info.ucl.ac.be`) y use este comando para verificar que su cuenta está activa.

#. Ahora que conocemos lo básico de abrir y cerrar sesiones SMTP, podemos enviar email manualmente usando los comandos `MAIL FROM:`, `RCPT TO:` y `DATA`. Use estos comandos para enviar *manualmente* un email a `INGI2141@cnp3.info.ucl.ac.be`. No olvide incluir las líneas `From:`, `To:` y `Subject:` en la cabecera.

.. look at the emails sent by the students 
#. Usando SMTP, ¿es posible enviar un email que contenga exactamente el siguiente diseño ASCII?  

.. code-block:: text

   .
   ..
   ...


#. La mayoría de los agentes de email le permiten enviar email en "copia carbónica" (`carbon-copy`, `cc:`) y también en "copia carbónica ciega" (`blind-carbon-copy`, `bcc:`) para un destinatario. ¿De qué manera soporta estos dos tipos de destinatarios un servidor SMTP?

#. Antiguamente, el email era leído usando herramientas como `/bin/mail` u otros lectores de email basados en texto, más avanzados, como pine_ o elm_. Hoy, los emails son almacenados en servidores dedicados, y recuperados usando protocolos como POP_ o IMAP_. Desde el punto de vista del usuario, ¿puede puntualizar las ventajas y desventajas de ambos protocolos?


#. El protocolo TCP soporta 65536 diferentes números de puerto. Muchos de estos números de puerto han sido reservados para algunas aplicaciones. El repositorio oficial de números reservados es mantenido por la autoridad de números asignados de Internet (`Internet Assigned Numbers Authority`, IANA_) en http://www.iana.org/assignments/port-numbers [#fservices]_. usando esta información, ¿cuál es el número de puerto por defecto del protocolo POP3? ¿Corre sobre UDP o TCP?

#. El protocolo de oficina de correos (`Post Office Protocol`, POP) es un protocolo bastante simple, descrito en :rfc:`1939`. POP opera en tres fases. La primera es la de autorización, donde el cliente provee un nombre de usuario y un password. La segunda fase es la de transacción, donde el cliente puede recuperar emails. La última es la de actualización, en la cual el cliente, finaliza la transacción. ¿Cuáles son los principales comandos POP y sus parámetros? Cuando un servidor POP devuelve una respuesta, ¿cómo se puede determinar fácilmente si se trata de una respuesta positiva o negativa?


#. En los `smartphones`, los usuarios suelen querer evitar la descarga de emails grandes debido a conexiones inalámbricas lentas. ¿Cómo podría un cliente POP descargar sólo los emails de tamaño menor que 5 KB?

#. Abra una sesión POP con el servidor POP del laboratorio (`nostromo.info.ucl.ac.be`) usando el nombre de usuario y password que usted ha recibido. Verifique que ambos son aceptados por el servidor.

#. El servidor POP del laboratorio contiene un script que corre a cada minuto y envía dos mensajes de mail a su cuenta si su carpeta de email está vacía. Use POP para recuperar estos dos emails y comunique el mensaje secreto al docente.

.. the magic words are squeamish ossifrage from RSA129

El Protocolo HTTP
=================


#. ¿Cuáles son los principales métodos soportados por la primera versión del Protocolo de Transferencia de Hipertexto (HTTP) definido en :rfc:`1945` [#fhttp1]_? ¿Cuáles son los principales tipos de respuestas enviadas por un servidor HTTP [#fhttp2]_ ?

#.  Los administradores de sistemas responsables de servidores Web suelen querer monitorizar estos servidores y verificar que estén corriendo correctamente. Como un servidor HTTP usa TCP sobre el puerto 80, la solución más simple es abrir una conexión TCP por el puerto 80 y ver que la conexión es aceptada por el host remoto. Sin embargo, como HTTP es un protocolo basado en ASCII, es también muy fácil escribir un pequeño script que descargue una página Web del servidor y compare su contenido con el esperado. Use `telnet` para verificar que un servidor Web en el host `rembrandt.info.ucl.ac.be` esté corriendo [#fhttp]_.


#. En lugar de usar `telnet` al puerto 80, también es posible usar una herramienta de línea de comandos como curl_. Use curl_ con la opción `--trace-ascii tracefile` para almacenar en el archivo `tracefile` toda la información intercambiada por curl al acceder al servidor. 

   - ¿Cuál es la versión de HTTP usada por curl?
   - ¿Puede explicar las diferentes cabeceras colocadas por curl en el requerimiento?
   - ¿Puede explicar las diferentes cabeceras que se encuentran en la respuesta?

#. HTTP 1.1, especificado en :rfc:`2616`, obliga al cliente a usar la cabecera `Host:` en todos sus requerimientos. HTTP 1.0 no define la cabecera `Host:`, pero la mayoría de las implementaciones la soportan. Usando `telnet` y `curl`, recupere la primera página del servidor Web http://totem.info.ucl.ac.be enviando requerimientos HTTP con y sin la cabecera `Host:`. Explique la diferencia entre las dos formas [#ftotem]_ .  

#. Usando dig_ y curl_, determine en qué host físico están alojadas las páginas http://www.info.ucl.ac.be, http://inl.info.ucl.ac.be y http://totem.info.ucl.ac.be.

#. Use curl_ con la opción ``--trace-ascii filename`` para recuperar http://www.google.com. Explique qué hace un navegador tal como Firefox cuando se recupera este URL.

#. Las cabeceras enviadas en un requerimiento HTTP permiten al cliente ofrecer información adicional al servidor. Una de estas cabeceras es `Language:`, que permite indicar el idioma preferido del cliente [#lang]_. Por ejemplo, ``curl -HAccept-Language:en http://www.google.be`` enviará a `http://www.google.be` un requerimiento HTTP indicando que el idioma preferido es inglés. ¿Ofrece Google una página diferente en francés (fr) que en walloon (wa)? Misma pregunta para http://www.uclovain.be (dado el tamaño de la página home, úsese ``diff`` para comparar las diferentes páginas recuperadas de www.uclovain.be).

#. Compare el tamaño de las páginas Web http://www.yahoo.com y http://www.google.com descargándolas con curl_.

#. ¿Qué es una `cookie` de HTTP? Enumere algunas ventajas y desventajas de usar cookies en servidores Web.

#. Supongamos que usted es el responsable del dominio `http://www.belgium.be`. El gobierno ha construido dos datacenters_ conteniendo 1000 servidores cada uno, en Amberes y en Namur. Este sitio Web contiene información estática, y su objetivo es balancear la carga entre los diferentes servidores y asegurar que el servicio se mantenga activo, aun si uno de los datacenters es desconectado de Internet debido a inundación, u otros desastres naturales. ¿Qué técnicas puede usar para lograr esta meta?

.. rubric:: Footnotes

.. .. [#fdig] On a Linux machine, the *Description* section of the `dig` manpage tells you where `dig` finds the list of nameservers to query.
.. [#fdig] En una máquina Linux, la sección *Description* de la página man de `dig` dice dónde busca `dig` la lista de nameservers a consultar.

.. .. [#rs] You may obtain additional information about the root DNS servers from http://www.root-servers.org
.. [#rs] Puede obtener más información sobre los servidores DNS raíz en http://www.root-servers.org.

.. .. [#fblock] Note that using `telnet` to connect to a remote host on port 25 may not work in all networks. Due to the spam_ problem, many ISP_ networks do not allow their customers to use port TCP 25 directly and force them to use the ISP's mail relay to forward their email. Thanks to this, if a software sending spam has been installed on the PC of one of the ISP's customers, this software will not be able to send a huge amount of spam. If you connect to `nostromo.info.ucl.ac.be` from the fixed stations in INGI's lab, you should not be blocked.
.. [#fblock] Nótese que usar `telnet` para conectarse a un host remoto sobre el puerto 25 puede no funcionar en todas las redes. Debido al problema del spam_, muchas redes de ISP_ no permiten a sus clientes usar el puerto TCP 25 directamente, y los obligan a usar el mail relay del ISP para reenviar su email.  Gracias a esta medida, si ha sido instalado un software que envía spam en la PC de uno de los clientes del ISP, este software no será capaz de enviar una cantidad grande de spam. Si uno se conecta a `nostromo.info.ucl.ac.be` desde las estaciones fijas en el laboratorio INGI, el tráfico no debería evidenciar bloqueo.

.. .. [#fmonitoring] There are many `monitoring tools <http://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems>`_ available. nagios_ is a very popular open source monitoring system. 
.. [#fmonitoring] Hay gran cantidad de `herramientas de monitorización <http://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems>`_ disponibles. nagios_ es un sistema de monitorización de código abierto muy popular. 

.. .. [#fsmtp] A shorter description of the SMTP protocol may be found on wikipedia at http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
.. [#fsmtp] Se puede ver una descripción más breve del protocolo SMTP en Wikipedia: http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol.

.. .. [#fsmtpevol] Since :rfc:`821`, SMTP has evolved a lot due notably to the growing usage of email and the need to protect the email system against spammers. It is unlikely that you will be able to explain all the additional lines that you will find in email headers, but we'll discuss them together.
.. [#fsmtpevol] Desde :rfc:`821`, SMTP ha sufrido una gran evolución, debido notablemente al creciente uso de email y la necesidad de proteger el sistema de email contra los `spammers`. No es probable que usted esté en condiciones de explicar todas las líneas adicionales que encontrará en las cabeceras de email, pero las discutiremos juntos. 

.. .. [#fservices] On Unix hosts, a subset of the port assignments is often placed in `/etc/services`
.. [#fservices] En los hosts Unix, con frecuencia se tiene un subconjunto de los puertos asignados en `/etc/services`.

.. .. [#fhttp] The minimum command sent to a HTTP server is `GET / HTTP/1.0` followed by CRLF and a blank line
.. [#fhttp] El comando minimal enviado a un servidor HTTP es `GET / HTTP/1.0` seguido por CRLF y una línea en blanco.

.. .. [#fhttp1] See section 5 of :rfc:`1945`
.. [#fhttp1] Véase sección 5 de :rfc:`1945`.

.. .. [#fhttp2] See section 6.1 of :rfc:`1945`
.. [#fhttp2] Véase sección 6.1 de :rfc:`1945`.

.. .. [#ftotem] Use dig_ to find the IP address used by `totem.info.ucl.ac.be`
.. [#ftotem] Use dig_ para hallar la dirección IP de `totem.info.ucl.ac.be`.

.. .. [#lang] The list of available language tags can be found at http://www.loc.gov/standards/iso639-2/php/code_list.php Additional information about the support of multiple languages in Internet protocols may be found in :rfc:`5646`
.. [#lang] La lista de rótulos disponibles puede verse en http://www.loc.gov/standards/iso639-2/php/code_list.php. Hay más información sobre el soporte de múltiple lenguajes en protocolos de Internet, en :rfc:`5646`.

.. include:: /links.rst
