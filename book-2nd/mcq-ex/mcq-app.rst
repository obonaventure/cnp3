.. Copyright |copy| 2014 by Olivier Bonaventure 
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

*********************
Internet applications
*********************

Multiple choice questions
=========================

:task_id: app




The Domain Name System
----------------------

.. question:: DNS1
   :nb_prop: 3
   :nb_pos: 1

   1. Which of the following DNS Resource Records should be queried to retrieve the IPv6 address associated to a name ? 

   .. positive:: The `AAAA` record. 

   .. negative:: The `A` record. 

      .. comment:: This record is used to retrieve the IPv4 address associated to a name.

   .. negative:: The `NS` record.

      .. comment:: This record is used to retrieve the name server that is responsible for a given domain name.

   .. negative:: The `MX` record.

      .. comment:: This record is used to retrieve the mail server that is responsible for a given domain name.


.. question:: DNS2
   :nb_prop: 3
   :nb_pos: 1

   2. You use the DNS to retrieve the `IPv4` address associated to the name `cnp3book.info.ucl.ac.be`. Assuming that you need to start your query from the root of the domain name system, which of the following DNS record will you *never* query to obtain this information.

   .. negative:: The `AAAA` record. 

      .. comment:: This record is used to retrieve the IPv6 address associated to a name. Although you query an IPv4 address, you might need to query a nameserver that uses IPv6 to retrieve this information.

   .. negative:: The `A` record. 

      .. comment:: This record is used to retrieve the IPv4 address associated to a name.

   .. negative:: The `NS` record.

      .. comment:: This record is used to retrieve the name server that is responsible for a given domain name.

   .. positive:: The `MX` record.

      .. comment:: This record is used to retrieve the mail server that is responsible for a given domain name. 


Electronic mail
---------------

.. question:: email1
   :nb_prop: 4
   :nb_pos: 2

   1. Which of the following affirmations about electronic mail on the Internet are valid ? Select all the correct ones in the list.

   .. positive:: The SMTP protocol is used to deliver email messages between servers and also between a client an a server.
 
   .. negative:: The SMTP protocol is used by the recipient to retrieve his/her email messages. 

      .. comment:: This action is performed by using the POP and IMAP protocols.

   .. positive:: The POP and IMAP protocols are used by the recipient to retrieve his/her email messages. 

   .. negative:: The SMTP protocol runs above the User Datagram Protocol (UDP).

   .. negative:: The POP protocol runs above the User Datagram Protocol (UDP).

   .. positive:: An email is a sequence of ASCII lines. The first lines contain the information required to deliver the email. An empty line is used to separate the header from the content of the email.

.. question:: email2
   :nb_prop: 3
   :nb_pos: 1

   2. The format of the Internet emails is defined in :rfc:`2822`. This specification describes all the nitty details of the format of email messages. The bullets below show several email messages. Only one of them is syntactically valid. Which one ?

   .. positive:: 

      .. code-block:: console 

         From: Alice <alice@example.net>
         To: Bob <mary@example.com>
         Subject: Saying Hello 
         Date: Fri, 21 Nov 1997 09:55:06 -0600 

         This is a message just to say hello. 
         So, "Hello". 

   .. positive::

      .. code-block:: console 

         From: Alice <alice@example.net>
         Subject: Saying Hello 
         Date: Fri, 21 Nov 1997 09:55:06 -0600 
         To: Bob <mary@example.com>


         This is a message just to say hello. 
         So, "Hello". 

   .. negative:: 

      .. code-block:: console 

         From: Alice "alice@example.net"
         Subject: Saying Hello 
         Date: Fri, 21 Nov 1997 09:55:06 -0600 
         To: Bob "mary@example.com"

         This is a message just to say hello. 
         So, "Hello". 

      .. comment:: The email addresses used in the header must be enclosed with `<` and `>`. 


   .. negative:: 

      .. code-block:: console 

         From: Alice <alice@example.net>
         Subject: Saying Hello 
         Date: Fri, 21 Nov 1997 09:55:06 -0600 
         To: Bob <mary@example.com>
         This is a message just to say hello. 
         So, "Hello". 

      .. comment:: The email header must be terminated by an empty line before the content of the message. 

   .. negative:: 

      .. code-block:: console 

         From: Alice "alice@example.net"
         Subject: Saying Hello 
         Date: Fri, 21 Nov 1997 09:55:06 -0600 
         To: Bob "mary@example.com"
         This is a message just to say hello. 
         So, "Hello". 

      .. comment:: The email header must be terminated by an empty line before the content of the message.  The email addresses used in the header must be enclosed with `<` and `>`. 


   .. negative:: 

      .. code-block:: console 

         From: Alice <alice@example.net>
         Subject: Saying Hello 
         To: Bob <mary@example.com>

         This is a message just to say hello. 
         So, "Hello" .


      .. comment:: The `Date:` header line is mandatory inside an email.

.. question:: smtp1
   :nb_prop: 4
   :nb_pos: 3 

   3. The SMTP protocol is a key protocol for the delivery of Internet email messages. This protocol is a stateful protocol where the client sends commands to the server. Which of the following affirmations about the SMTP commands are correct ?  Select all the valid ones. 

   .. positive:: The `HELO` command is the first command sent by a client on an SMTP session. It is always followed by a domain name as in the example below :
  
      .. code-block:: console 

         HELO uclouvain.be

   .. negative:: The `HELO` command can be issued at any time during an SMTP session. 

      .. comment:: The `HELO` command must be the first command issued on an SMTP session. It is always followed by a domain name

   .. positive:: The `MAIL FROM:` command must be issued before the `DATA` command. It contains as parameter a valid email address as in the example below :

      .. code-block:: console 

         MAIL FROM: <alice@example.net>

   .. negative:: The `MAIL FROM:` command can only be issued after the `DATA` command. It contains as parameter a valid email address as in the example below :

      .. code-block:: console 

         MAIL FROM: <bob@example.com>

   .. positive:: The `DATA` command can only be issued once the `MAIL FROM:` and `RCPT TO:` commands have been issued. It is followed by the entire email message that is transmitted. 

   .. positive:: The `QUIT` command is the last command from an SMTP session. It terminates the session.

.. question:: base64
   :nb_prop: 3
   :nb_pos: 1

   4. The Base64 format, defined in :rfc:`2045` and :rfc:`4648` allows to encode any binary information in a sequence of ASCII characters. Only one affirmation below concerning Base64 is valid. Which one ?

   .. positive:: Base64 encodes three 8 bits ASCII characters as a sequence of four characters. 

   .. negative:: Base64 encodes four 8 bits ASCII characters as a sequence of three characters. 

   .. positive:: A Base64 encoded string may contains the characters `A-Z`, `a-z`, `0-9` as well as `+`, `/` and `=` 

   .. negative:: A Base64 encoded string can only contain letters (`A-Z` and `a-z`) and digits (`0-9`)

      .. comment:: This is not sufficient. Base64 requires 64 different symbols. By using the letters and digits, there are only 62 symbols.

   .. positive:: A Base64 encoded string may contain the character `=`.

      .. comment:: This happens when the number of bytes to be encoded is not a multiple of three.

   .. negative:: A Base64 encoded string may never contain the character `=`.
      .. comment:: This character may be used, only in the last characters of the Base64 encoded string if the number of bytes to be encoded is not a multiple of three.

The HyperText Transfer Protocol
-------------------------------   

.. question:: http1
   :nb_pos: 2
   :nb_prop: 4

   1. The Uniform Resource Identifiers (URI) defined in :rfc:`3986` are a key element of the `world wide web`. Among the URIs below, select the ones that are valid URIs.

   .. positive:: ``http://example.net``

   .. negative:: ``http:example.net``
 
      .. comment:: In a URI, must be followed by the characters `:` and ``//`
   .. positive:: ``http://example.net@/example.com``

      .. comment:: This URI is valid, the string ``example.net`` corresponds to the authority part of the BNF that defines the format of the URI.

   .. negative:: ``http://example.com:user/index.html``

      .. comment:: This URI is invalid, the string ``example.com`` corresponds to a server name. The string after the `:` should be an integer that represents a port number. 

   .. negative:: ``http:80//example.com/index.html``

      .. comment:: This URI is invalid, the string ``example.com`` corresponds to a server name. To indicate a port number, `:80` should appear after ``example.com``. 


.. question:: http2
   :nb_pos: 2
   :nb_prop: 3

   2. The Uniform Resource Identifiers (URI) defined in :rfc:`3986` are used to indicate the domain name of the server that needs to be contacted to retrieve a document. Which of the following affirmations are valid for these URIs ? 

   .. positive:: In the ``http://example.net/example.com`` URI, the server name is ``example.com``

   .. negative:: In the ``http://example.net/example.com`` URI, the server name is ``example.net``

   .. positive:: In the ``http://example.net:1234/example.com/test.com`` URI, the server name is ``example.net``

   .. negative:: In the ``http://example.net:1234/example.com/test.com`` URI, the server name is ``example.com``

   .. negative:: In the ``http://example.net:1234/example.com/test.com`` URI, the server name is ``test.com``

   .. positive:: In the ``http://example.com@/example.net/test.com`` URI, the server name is ``example.net``

   .. negative:: In the ``http://example.com@/example.net/test.com`` URI, the server name is ``test.com``

.. question:: http3
   :nb_pos: 1
   :nb_prop: 3

   3. Which of the following affirmations are valid concerning the HTTP protocol ? Select all the valid affirmations from the ones listed below.

   .. positive:: HTTP is a stateless protocol.

   .. negative:: HTTP is a stateful protocol.

      .. comment:: HTTP is a stateless protocol.           

   .. positive:: HTTP supports three different methods : `GET`, `HEAD` and `POST`

   .. negative:: HTTP supports a single method : `GET`

      .. comment:: HTTP supports three different methods : `GET`, `HEAD` and `POST`. 

   .. positive:: A HTTP request contains a method and sequence of header lines. It ends with a blank line.

   .. negative:: The HTTP protocol can only be used to receive documents from a server.
 
      .. comment:: This is incorrect. With the `POST` method, it is possible to send information to a server.


.. question:: http4
   :nb_pos: 2
   :nb_prop: 3

   4. The extensibility of the HTTP protocol comes from the various header lines that it supports. Some of these header lines appear inside requests while others appear inside responses. Among the following affirmations about these headers, select the ones that are valid.

   .. positive:: The `Host` header line can appear inside an HTTP request. It indicates the name of the server from which the document can be retrieved.

   .. negative:: The `Server` header line can appear inside an HTTP request. It indicates the name of the server from which the document can be retrieved.

      .. comment:: This is incorrect. The `Server` header line can only appear inside *HTTP responses*. The header line that can appear inside HTTP requests is the `Host` line.

   .. positive:: The `Last-Modified` header line is included in the HTTP responses. It contains as parameter the last modification date of the retrieved document.

   .. negative:: The `User-Agent` header line can appear inside HTTP responses. It indicates the application that should process the response.

      .. comment:: This is incorrect, this header line can only appear inside HTTP requests. It indicates the application that was used to create the HTTP request.

   .. positive:: The `Referrer` header line may appear in HTTP requests. It indicates the URI that was visited before retrieving this URI.

   .. positive:: The `Content-Length`, `Content-Type` and `Content-Encoding` header lines may appear inside HTTP requests.

      .. comment:: Consider for example a `POST` request that contains a document that is transmitted to the server.

   .. negative:: The `Content-Length`, `Content-Type` and `Content-Encoding` header lines can only appear inside HTTP responses.

      .. comment:: This is incorrect. These header lines can also appear inside HTTP requests. Consider for example a `POST` request that contains a document that is transmitted to the server.
  



