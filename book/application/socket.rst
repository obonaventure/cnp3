.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

Writing simple networked applications
#####################################

Networked applications are usually implemented by using the :term:`socket` API. This API was designed when TCP/IP was implemented first in the Unix BSD operating system [Sechrest]_ [LFJLMT]_ . This API has served as the model for many APIs between applications and the networking stack in an operating system. Although the socket API is very popular, other APIs have also been developed. For example, the STREAMS API has been added to several Unix System V variants [Rago1993]. The socket API is supported by most programming languages and several textbooks have been devoted to this API. Users of the C language can consult [DC2009]_, [Stevens1998]_, [SFR2004]_ or [Kerrisk2010]_. The Java implementation of the sockets API is described in [CD2008]_ and in the `Java tutorial <http://java.sun.com/docs/books/tutorial/networking/sockets/index.html>`_. Users of `python <http://www.python.org>`_ may consult the `socket section <http://docs.python.org/library/socket.html>`_ of the `python documentation <http://docs.python.org/>`_ .

A detailed discussion of the socket API is outside the scope of this section and the references cited above are a good starting point for a detailed discussion of all the nitty details of the socket API. As a starting point, it is interesting to compare the socket API with the service primitives that we have discussed in the previous chapter. Let us first consider the connectionless service which is the simplest service. Two primitives are defined for this service :

 - `DATA.request(destination,message)` is used to send a message to a specified destination. In this socket API, this corresponds to the `send` method.
 - `DATA.indication(message)` is issued by the transport service to deliver a message to the application. In the socket API, this corresponds to the return of the `recv` method that was called by the application. 

The `DATA` primitives are exchanged through a service access point. In the socket API, the equivalent to the service access point is the `socket`. A `socket` is a data structure which is maintained by the networking stack and is used by the application every time it needs to send or receive data through the networking stack. The `socket` method in the python_ API takes two main arguments :

 - an `address family` that specifies the type of address family and thus the underlying networking stack that will be used with the socket. `socket.AF_INET`, which corresponds to the TCP/IPv4 protocol stack is the default. `socket.AF_INET6` corresponds to the TCP/IPv6 protocol stack.
 - a `type` indicates the type of service which is expected from the networking stack. `socket.STREAM` is the default and corresponds to the reliable bytestream connection-oriented service. `socket.DGRAM` corresponds to the connectionless service.
 
.. However, it is important to understand the basics and the limitations of this API. We use the `python socket API <http://docs.python.org/library/socket.html>` to describe these issues. The socket API allows applications to interact with the transport services offered by the networking stack. The simplest transport service is the connectionless service. The simplest client application that uses this service will issue a `DATA.request` with its request and wait for a `DATA.indication` that contains the response.

.. index:: socket, sendto, AF_INET, AF_INET6, SOCK_DGRAM, SOCK_STREAM

A simple client that sends a request to a server is often shown as follows in descriptions of the socket API.

.. literalinclude:: python/simpleclientip.py
   :language: python

A typical usage of this application would be ::

  python client 127.0.0.1 1234

where `127.0.0.1` is the IPv4 address of the host (in this case the localhost) where the server is running and `1234` the port of the server.

The first operation is the creation of the `socket`. Two parameters must be specified while creating a `socket`. The first parameter indicates the address family and the second the socket type. The second operation is the transmission of the message by using `sendto` to the server. It should be noted that `sendto` takes as arguments the message to be transmitted and a tuple that contains the IPv4 address of the server and its port number. 

The code shown above supports only the TCP/IPv4 protocol stack. To use the TCP/IPv6 protocol stack the socket must be created by using the `socket.AF_INET6` address family. Forcing the application developer to select TCP/IPv4 or TCP/IPv6 when creating a socket is a major hurdle for the deployment and usage of TCP/IPv6 in the global Internet [Cheshire2010]_. While most operating systems support both TCP/IPv4 and TCP/IPv6, many applications still only use TCP/IPv4 by default. In the long term, the socket API should be able to handle TCP/IPv4 and TCP/IPv6 transparently and should not force the application developer to always specify whether it uses TCP/IPv4 or TCP/IPv6. 

.. index:: getaddrinfo, AF_UNSPEC

Another important issue with the socket API as supported by python_ is that it forces the application to deal with IP addresses instead of dealing directly with domain names. This limitations dates from the early days of the socket API in Unix 4.2BSD. At that time, the DNS was not widely available and only IP addresses could be used. Most applications rely on DNS names to interact with servers and this utilisation of the DNS plays a very important role to scale web servers and content distribution networks. To use domain names, the application needs to perform the DNS resolution by using the getaddrinfo method. This method queries the DNS and builds the sockaddr data structure which is used by other methods of the socket API. In python_, getaddrinfo takes several main arguments :

 - a `name` that is the domain name for which the DNS will be queried
 - an optional `port number` which is the port number of the remote server
 - an optional `address family` which indicates the address family used for the DNS request. `socket.AF_INET` (resp. `socket.AF_INET6`) indicates that an IPv4 (IPv6) address is expected. Furthermore, the python_ socket API allows an application to use `socket.AF_UNSPEC` to indicate that it is able to use either IPv4 or IPv6 addresses.
 - an optional `socket type` which can be either `socket.SOCK_DGRAM` or `socket.SOCK_STREAM`

In today's Internet where hosts are capable of supporting both IPv4 and IPv6, all applications should be able to handle both IPv4 and IPv6 addresses. When used with the `socket.AF_UNSPEC` parameter, the `socket.getaddrinfo` method returns a list of tuples containing all the information to create a socket ::

 import socket
 socket.getaddrinfo('inl.info.ucl.ac.be',80,socket.AF_UNSPEC,socket.SOCK_STREAM)
 [ (30, 1, 6, '', ('2001:6a8:3080:3::2', 80, 0, 0)), 
   (2, 1, 6, '', ('130.104.229.225', 80))]

In the example above, `socket.getaddrinfo` returns two tuples. The first one corresponds to the sockaddr containing the IPv6 address of the remote server and the second corresponds to the IPv4 information. Due to some peculiarities of IPv6 and IPv4, the format of the two tuples is not exactly the same, but the key information in both cases are the network layer address (`2001:6a8:3080:3::2` and `130.104.229.225`) and the port number (`80`). The other parameters are seldom used.

`socket.getaddrinfo` can be used to build a simple client that queries the DNS and contact the server by using either IPv4 or IPv6 depending on the addresses returned by the `socket.getaddrinfo` method. The client below iterates over the list of addresses returned by the DNS and sends its request to the first destination address for which it can create a socket. Other strategies are of course possible. For example, a host running in an IPv6 network might prefer to always use IPv6 when IPv6 are available [#fipv6pref]_. Another example is the happy eyeballs approach which is being discussed within the IETF_ [WY2011]_ . For example, [WY2011]_ mentions that some web browsers try to use the first address returned by `socket.getaddrinfo`. If there is no answer within some small delay (e.g. 300 milliseconds), the second address is tried, ...

.. literalinclude:: python/simpleclientname.py
   :language: python

.. index:: socket.connect, socket.send, socket.recv, socket.close, socket.shutdown

Now that we have described the utilisation of the socket API to write a simple client using the connectionless transport service, let us have a closer look at the reliable byte stream transport service. As explained above, this service is invoked by creating a `socket` of type `socket.SOCK_STREAM`. Once a socket has been created, a client will typically connect to the remote server, send some data, wait for an answer and eventually close the connection. These operations are performed by calling the following methods :

 - `socket.connect` : this method takes a `sockaddr` data structure, typically returned by `socket.getaddrinfo`, as argument. It may fail and raise an exception if the remote server cannot be reached.
 - `socket.send` : this method takes a string as argument and returns the number of bytes that were actually sent. The string will be transmitted as a sequence of consecutive bytes to the remote server. Applications are expected to check the value returned by this method and should resend the bytes that were not send.
 - `socket.recv` : this method takes an integer as argument that indicates the size of the buffer that has been allocated to receive the data. An important point to note about the utilisation of the `socket.recv` method is that as it runs above a bytestream service, it may return any amount of bytes (up to the size of the buffer provided by the application). The application needs to collect all the received data and there is no guarantee that some data sent by the remote host by using a single call to the `socket.send` method will be received by the destination with a single call to the `socket.recv` method. 
 - `socket.shutdown` : this method is used to release the underlying connection. On some platforms, it is possible to specify the direction of transfer to be released (e.g. `socket.SHUT_WR` to release the outgoing direction or `socket.SHUT_RDWR` to release both directions).
 - `socket.close`: this method is used to close the socket. It calls `socket.shutdown` if the underlying connection is still open.

With these methods, it is now possible to write a simple HTTP client. This client operates over both IPv6 and IPv4 and writes the homepage of the remote server on the standard output. It also reports the number of `socket.recv` calls that were used to retrieve the homepage[#fnumrecv]_. 


.. literalinclude:: python/httpclient.py
   :language: python


The second type of applications that can be written by using the socket API are the servers. A server is typically a server that runs forever waiting to process requests coming from remote clients. A server using the connectionless will typically start with the creation of a `socket` with the `socket.socket`. This socket can be created above the TCP/IPv4 networking stack (`socket.AF_INET`) or the TCP/IPv6 networking stack (`socket.AF_INET6`), but not both by default. If a server is willing to use the two networking stacks, it must create two threads, one to handle the TCP/IPv4 socket and the other to handle the TCP/IPv6 socket. It is unfortunately impossible to define a socket that can receive data from both networking stacks at the same time in the python_ socket API.

.. index:: socket.bind, socket.recvfrom

A server using the connectionless service will typically use two methods from the socket API in addition to those that we have already discussed.

 - `socket.bind` is used to bind a socket to a port number and optionally an IP address. Most servers will bind their socket to all available interfaces on the servers, but there are some situations where the server may prefer to be bound only to specific IP addresses. For example, a server running on smartphone might be bound to the IP address of the WiFi interface but not on the 3G interface that is more expensive.
 - `socket.recvfrom` is used to receive data from the underlying networking stack. This method returns both the sender's address and the received data.

The code below illustrates a very simple server running above the connectionless transport service that simply prints on the standard output all the received messages. This server uses the TCP/IPv6 networking stack.

.. literalinclude:: python/simpleserverudp.py
   :language: python

A server that uses the reliable byte stream service can also be built above the socket API. Such a server starts by creating a socket that is bound to the port that has been chosen for the server. Then the server calls the `socket.listen` method. This informs the underlying networking stack of the number of transport connection attempts that can be queued in the underlying networking stack waiting to be accepted and processed by the server. The server typically has a thread waiting on the `socket.accept()` method. This method returns as soon as a connection attempt is received by the underlying stack. It returns a socket that is bound to the established connection and the address of the remote host. With these methods, it is possible to write a very simple web server that always returns a `404` error to all `GET` requests and a `501` errors to all other requests. 

.. literalinclude:: python/simplehttpserver.py
   :language: python

This server is far from a production-quality web server. A real web server would use multiple threads and/or non-blocking IO to process a large number of concurrent requests. Furthermore, it would also need to handle all the errors that could happen while receiving data over a transport connection. These are outside the scope of this section and additional information on more complex networked applications may be found elsewhere. For example, [RG2010]_ provides an in-depth discussion of the utilisation of the socket API with python while [SFR2004]_ remains an excellent source of information on the socket API in C.



..  To be written : connect by name API is key !  http://www.stuartcheshire.org/IETF72/


.. [Cheshire2010]_



.. rubric:: Footnotes

.. [#fipv6pref] Most operating systems today prefer by default to use IPv6 when the DNS returns both an IPv4 and an IPv6 address for a name. See http://ipv6int.net/systems/ for more detailed information. 

.. [#fnumrecv] Experiments with the client indicate that the number of `socket.recv` calls can vary at each run. There are various factors that influence the number of such calls that are required to retrieved some information from a server. We'll discuss some of them after having explained the operation of the underlying transport protocol.
