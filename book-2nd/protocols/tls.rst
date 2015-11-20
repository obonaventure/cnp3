.. Copyright |copy| 2015 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. _TLS:

Transport Layer Security
========================

.. index:: SSL

The Transport Layer Security family of protocols were initially
proposed under the name Secure Socket Layer (SSL). The first deployments
used this name and many researchers still refer to this security
protocol as SSL [FKC1996]_. In this chapter, we use the official name that was
standardised by the IETF : TLS for `Transport Layer Security`.

The TLS protocol was designed to be usable by a wide range of applications
that use the transport layer to reliably exchange information. TLS is mainly
used over the TCP protocol. There are variants of TLS that operate
over SCTP :rfc:`3436` or UDP :rfc:`6347`, 
but these are outside the scope of  this chapter.

A TLS session operates over a TCP connection. TLS is responsible for the
encryption and the authentication of the SDUs exchanged by the application
layer protocol while TCP provides the reliable delivery of this encrypted
and authenticated bytestream. TLS can be used with many different
application layer protocols. The most frequent ones are HTTP (HTTP over TLS
is called HTTPS), SMTP :rfc:`3207` or POP and IMAP :rfc:`2595`. 

A TLS session can be initiated in two different ways. First, the application
can use a dedicated TCP port number for application layer protocol x-over-TLS.
This is the solution used by many HTTP servers that reserve port :math:`443`
for HTTP over TLS. This solution works, but it requires to reserve two ports
for each application : one where the application-layer protocol is used
directly over TCP and another one where the application-layer protocol
is used over TLS. Given the limited number of TCP ports that are available,
this is not a scalable solution. The table below provides some of
the reserved port numbers for application layer protocols on top of TLS.

==================   ============  ==========
Application          TCP port      TLS port
==================   ============  ==========
POP3                 110           995
IMAP                 143           993
NNTP                 119           563
HTTP                 80            443
FTP                  21            990
==================   ============  ==========


A second approach to initiate a TLS session is to use the standard 
TCP port number for the application layer protocol and define a special 
message in this protocol to trigger the start of the
TLS session. This is the solution used for SMTP with the ``STARTTLS`` message.
This extension to SMTP :rfc:`3207` defines the new STARTTLS command.
The client can issue this command to indicate to the server that
it wants to start a TLS session as shown in the example below
captured during a session on port 25.


.. code-block:: console

          220 server.example.org ESMTP
          EHLO client.example.net
          250-server.example.org
          250-PIPELINING
          250-SIZE 250000000
          250-ETRN
          250-STARTTLS
          250-ENHANCEDSTATUSCODES
          250-8BITMIME
          250 DSN
          STARTTLS
          220 2.0.0 Ready to start TLS


In the remaining parts of this chapter, we assume that the TLS session
starts immediately after the establishment of the TCP connection. This
corresponds to the deployments on webservers. We focus our presentation
of TLS on this very popular use case. TLS is a complex protocol that 
supports other features than the one used by webservers. A more detailed
presentation of TLS may be found in [KPS2002]_ and [Ristic2015]_. 

A TLS session is divided in two phases : the handshake and the data transfert.
During the handshake, the client
and the server negotiate the security parameters and the keys that will
be used to secure the data transfer. During the second phase, all the messages
exchanged are encrypted and authenticated with the negotiated algorithms
and keys. 

The TLS handshake
-----------------

When used to interact with a regular web server, the TLS handshake has 
three important objectives :

 1. Securely negotiate the cryptographic algorithms that will be used by the
    client and the server on the TLS session
 2. Verify that the client interacts with a valid server
 3. Securely agree on the keys that will be used to encrypt and authenticate
    the messages exchanged over the TLS session


.. index:: TLS ClientHello

Let us first discuss the negotiation of the cryptographic algorithms and
parameters. Like all security protocols, TLS includes some agility in its
design since new cryptographic algorithms appear over the years and
some older algorithms become deprecated once cryptanalysts find flaws
in some of them. The TLS handshakes starts with the ``ClientHello`` message
that is sent by the client. This message carries the following information : 

 - `Protocol version number` : this is the version of the TLS protocol supported
   by the client. The server should use the same version of the TLS protocol as
   the client, 
   but may opt for an older version. The current TLS standard is version 1.2
   but the IETF is currently preparing version 1.3 and some implementations
   already support this non-standard version.
 - `Random number` : security protocols rely on random numbers. The client
   sends a 32 bytes long random number where usually four of these bytes 
   correspond
   to the client's clock. This random number will be used, together with the
   server's random number, as a seed to generate the security keys.
 - `Cipher suites` : this ordered list contains the set of cryptographic 
   algorithms that are supported by the client, with the most preferred one
   listed first. In contrast with ``ssh`` that allows to negotiate independant
   algorithms for encryption, key exchange and authentication, TLS relies on
   suites that combine these algorithms together. Many cryptographic suites
   have been defined for TLS. Various recommendations
   have been published on the security of some of these suites :rfc:`7525`.
 - `Compression algorithm` : the client may propose the utilisation of a
   specific compression algorithm (e.g. zlib). In theory, compressing the data
   before encrypting it is an intelligent way to reduce the amount of data
   exchanged. Unfortunately, its implementation in TLS lead to attacks. For
   this reason, compression is usually disabled in TLS :rfc:`7525`.
 - `Extensions` : TLS supports various extensions in the ``ClientHello`` 
   message. These extensions :rfc:`6066` are important to allow the protocol
   to evolve, but many of them go beyond the scope of this chapter.

.. index:: TLS SNI

.. note:: The ``Server Name Indication (SNI)``

   The ``Server Name Indication (SNI)`` extension defined in :rfc:`6066`
   is an important TLS extension for the scalability of this protocol.
   It is simply used by the client to indicate the name of the server
   that it wishes to contact. The IP address associated to this name
   has been queried from the DNS and used to establish the TCP connection.
   Why should the client indicate the server name in the TLS
   ``ClientHello`` ?  The motivation is the same as for the ``Host`` 
   header line in HTTP/1.0. With the SNI extension, a single TLS server
   can support several web sites that use different domain names. Thanks
   to the SNI extension, the server knows the concerned domain name at
   the start of the TLS session. Without this extension, hosting providers 
   would have been forced use one IP address per TLS-enabled server. 

.. index:: TLS ServerHello, TLS Certificate

The server replies to the ``ClientHello`` message with several messages :

 - the ``ServerHello`` message that contains the protocol version chosen by 
   the server (assumed to be the same as the client version in this chapter),
   the 32 random bytes chosen by the server, the `Cipher Suite` selected by
   the server from the list advertised by the client 
   and a `Session Id`. This `Session Id` is an identifier which
   is chosen by the server and that identifies the TLS session and the
   security parameters (algorithms and keys) negotiated for this session. 
   It is used to support session resumption. 
 - the ``Certificate`` message provides the certificate (or usually chain of 
   certificates) that binds a domain name to the public key used by 
   the server. TLS uses the server certificates
   to authenticate the server. It relies on a Public Key Infrastructure that
   is composed of a set of root certification authorities that 
   issue certificates to certification authorities that in the end
   issue certificates to servers. TLS clients are usually configured with 
   the public keys of the main root certification authorities and can use
   this information to validate the certificates that they receive from
   servers. For historical reasons, the TLS certificates are encoded
   in ASN.1 format. The details of the ASN.1 syntax [Dubuisson2000]_ 
   are outside the scope of this book.
 - the ``ServerKeyExchange`` message is used by the server to transmit the
   information that is required to perform the key exchange. The content
   of this message is function of the selected key exchange algorithm.
 - the ``ServerHelloDone`` indicates that the server has sent all the messages
   for the first phase of the handshake.

.. index:: TLS Key exchange

At this point, it is time to describe the TLS key exchange. TLS supports
different key exchange mechanisms that can be negotiated as part of the
selection of the cipher suite. We focus on two of them to highlight
their differences : 

 - ``RSA``. This key exchange algorithm uses the encryption capabilities of
   the RSA public-key algorithm. The client has validated the server's
   public key thanks to the ``Certificate`` message. It then generates
   a (48 bytes) random number, encrypts it with the server public key
   and sends the encrypted number to the server in the ``ClientKeyExchange``
   message. The server uses its private key to decrypt the random
   number. At this point, the client and the server share the same
   (48 bytes long) secret and use it to derive the secret keys required
   to encrypt and authenticate data in the second phase. With this
   key exchange algorithm, the server does not need to send a
   ``ServerKeyExchange`` message.
 - ``DHE_RSA``. This key exchange algorithm is the Ephemeral Diffie Hellman
   key exchange with RSA signatures to authenticate the key exchange. It
   operates as a classical authenticated Diffie Hellman key exchange. 
   If this key exchange
   has been selected by the server, it sends its Diffie Hellman parameters
   in the ``ServerKeyExchange`` message and signs them with its private
   key. The client then continues the key exchange and sends the results of
   its own computation in the ``ClientKeyExchange`` message. ``DHE_RSA``
   is thus an authenticated Diffie Hellman key exchange where the initial
   message is sent by the server (instead of the client as in our first example
   but since the protocol is symmetric, this does not matter). 

.. index:: Perfect Forward Secrecy

An important difference between ``DHE_RSA`` and ``RSA`` is their reaction 
against attacks. ``DHE_RSA`` is considered by many to be stronger than ``RSA``
because it supports `Perfect Forward Secrecy`. This property is important
against attackers that are able to eavesdrop all the (encrypted) data 
sent and received by a server. Consider that Eve is such an attacker and
that she has stored all the packets exchanged by Bob's server during the last
six months. If she manages, by any means, to obtain Bob's private key, she
will be able to decrypt all the keys used to secure the TLS sessions with
Bob's server during this period. With ``DHE_RSA``, a similar attack is
less devastating. If Eve knows Bob's private, she will be able to launch
a man-in-the-middle attack against the future TLS sessions with Bob's server.
However, she will not be able to recover the keys used for all the past
sessions that she captured. 

.. index:: Perfect Forward Secrecy

.. note:: Perfect Forward Secrecy

   Perfect Forward Secrecy (PFS) is an important property for key 
   exchange protocols. A protocol provides PFS if its design guarantees that
   the keys used for former sessions will not be compromised even if the
   private key of the server is compromised. This is a very important 
   property. ``DHE_RSA`` provides Perfect Forward Secrecy, but the 
   ``RSA`` key exchange does not provide this property. In practice,
   ``DHE_RSA`` is costly from a computational viewpoint. Recent implementations
   of TLS prefer to thus ``ECDHE_RSA`` or ``ECDHE_ECDSA`` when
   Perfect Forward Secrecy is required.


All the information required for the key exchange has now been transmitted. 
There are two important messages that will be sent by the client and the server
to conclude the handshake and start the data transfer phase.

The client sends the ``ChangeCipherSpec`` message followed by the ``Finished``
message. The ``ChangeCipherSpec`` message indicates that the client has received
all the information required to generate the security keys for this TLS
session. This messages can also appear later in the session to indicate a
change in the encryption algorithms that are used, but this usage is outside
the scope of this book. The ``Finished`` message is more important. It confirms
to the server that the TLS handshake has been performed correctly and that no
attacker has been able to modify the data sent by the client or the server.
This is the first message that is encrypted with the selected security keys.
It contains a hash of all the messages that were exchanged during the handshake.

The server also sends a ``ChangeCipherSpec`` message followed by a ``Finished``
message.

.. note:: TLS Cipher suites

   A TLS cipher suite is usually represented as an ASCII string 
   that starts with TLS and contains the acronym of the key exchange algorithm,
   the encryption scheme with the key size and its mode of operation and
   the authentication algorithm. For example, 
   ``TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`` is a TLS cipher suite that uses
   the ``DHE_RSA`` key exchange algorithm with 128 bits AES in GCM mode for 
   encryption and SHA-256 for authentication. The official list of TLS
   cipher suites is maintained by IANA [#fianaTLS]_. The NULL acronym
   indicates that no algorithm has been specified. For example, 
   ``TLS_ECDH_RSA_WITH_NULL_SHA`` is a cipher suite that does not use
   any encryption but still uses the ``ECDH_RSA`` key exchange and 
   ``SHA`` for authentication.

The TLS record protocol
-----------------------

The handshake is now finished and the client and the server will exchange
authenticate and encrypted records. TLS defines different formats for the 
records depending on the crypto algorithms that have been negotiated
for the session. A detailed discussion of these different types of 
records is outside the scope of this introduction. For illustration, we
briefly describe one record format.

As other security protocols, TLS uses different keys to encrypt and 
authenticate records. These keys are derived from the MasterSecret that
is either randomly generated by the client with the ``RSA`` key exchange
or derived from the Diffie Hellman parameters with the ``DH_RSA``
key exchange. The exact algorithm used to derive the keys is defined 
in :rfc:`5246`.

A TLS record is always composed of four different fields :

 - a `Type` that indicates the type of record. The most frequent type
   is `application data` which corresponds to a record containing encrypted
   data. The other types are `handshake`, `change_cipher_spec` and
   `alert`. 
 - a `Protocol Version` field that indicates the version of the TLS protocol
   used. This version is composed of two sub fields : a major and a
   minor version number.
 - a `Length` field. A TLS record cannot be longer than 16,384 bytes.
 - a `TLSPlainText` that contains the encrypted data

TLS supports several methods to generate the encrypted records. The selected
method depends on the cryptographic algorithms that have been negotiated for
the TLS session. A detailed presentation of the different methods that can
be used to produce the `TLSPlainText` from the user data is outside the scope
of this book. As an example, we study one method : Stream Encryption. This
method is used with cryptographic algorithms which can operate on a stream
of bytes. The method starts with a sequence of bytes provided by the
user application : the plain text. The first step is to compute the
authentication code to verify the integrity of the data. For this, TLS
computes :math:`MAC(SeqNum, Header, PlainText)` using HMAC 
where `SeqNum` is a sequence
number which is incremented by one for each new TLS record transmitted. The
`Header` is the header of the TLS record described above and `PlainText` is
the information that needs to be encrypted. Note that the sequence number
is maintained at the two endpoints of the TLS session, but it is not transmitted
inside the TLS record. This sequence number is used to prevent replay attacks.

                
.. index:: MAC-then-encrypt, Encrypt-then-MAC

.. note:: MAC-then-encrypt or Encrypt-then-MAC

   When secure protocols use Message Authentication and Encryption, they
   need to specify how these two algorithms are combined. A first
   solution, which is used by the current version of TLS, is to compute 
   the authentication code and then encrypt both the data and the 
   authentication code. A drawback of this approach is that the receiver 
   of an encrypted TLS record must first attempt to decrypt data that
   has potentially been modified by an attacker before being able
   to verify the authenticity of the record. A better approach is
   for the sender to first encrypt the data and then compute the
   authentication code over the encrypted data. This is the encrypt-then-MAC
   approach proposed in :rfc:`7366`. With encrypt-then-MAC, the receiver
   first checks the authentication code before attempting to decrypt the
   record. 




.. rubric:: Footnotes

.. [#fianaTLS] See http://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-4


.. include:: /links.rst
