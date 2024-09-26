.. Copyright |copy| 2013 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_


Remote Procedure Calls
======================

In the previous sections, we have described several protocols that enable humans to exchange messages and access to remote documents. This is not the only usage of computer networks and in many situations applications use the network to exchange information with other applications. When an application needs to perform a large computation on a host, it can sometimes be useful to request computations from other hosts. Many distributed systems have been built by distributing applications on different hosts and using `Remote Procedure Calls` as a basic building block.

In traditional programming languages, `procedure calls` allow programmers to better structure their code. Each procedure is identified by a name, a return type and a set of parameters. When a procedure is called, the current flow of program execution is diverted to execute the procedure. This procedure uses the provided parameters to perform its computation and returns one or more values. This programming model was designed with a single host in mind. In a nutshell, most programming languages support it as follows :

 1. The caller places the values of the parameters at a location (register, stack, ...) where the callee can access them
 2. The caller transfers the control of execution to the callee's procedure
 3. The callee accesses the parameters and performs the requested computation
 4. The callee places the return value(s) at a location (register, stack, ...) where the caller can access them
 5. The callee returns the control of execution to the caller's

This model was developed with a single host in mind. How should it be modified if the caller and the callee are different hosts connected through a network ? Since the two hosts can be different, the two main problems are the fact they do not share the same memory and that they do not necessarily use the same representation for numbers, characters, ... Let us examine how the five steps identified above can be supported through a network.

The first problem to be solved is how to transfer the information from the caller to the callee. This problem is not simple and includes two sub-problems. The first subproblem is the encoding of the information. How to encode the values of the parameters so that they can be transferred correctly through the network ? The second problem is how to reach the callee through the network ? The callee is identified by a procedure name, but to use the transport service, we need to convert this name into an address and a port number.

.. index:: XDR

Encoding data
-------------

The encoding problem exists in a wide range of applications. In the previous sections, we have described how character-based encodings are used by email and http. Although standard encoding techniques such as ASN.1 [Dubuisson2000]_ have been defined to cover most application needs, many applications have defined their specific encoding. `Remote Procedure Call` are no exception to this rule. The three most popular encoding methods are probably XDR :rfc:`1832` used by ONC-RPC :rfc:`1831`, XML, used by XML-RPC and JSON :rfc:`4627`.

The eXternal Data Representation (XDR) Standard, defined in :rfc:`1832` is an early specification that describes how information exchanged during Remote Procedure Calls should be encoded before being transmitted through a network. Since the transport service allows to transfer a block of bytes (with the connectionless service) or a stream of bytes (by using the connection-oriented service), XDR maps each datatype onto a sequence of bytes. The caller encodes each data in the appropriate sequence and the callee decodes the received information. Here are a few examples extracted from :rfc:`1832` to illustrate how this encoding/decoding can be performed.

For basic data types, :rfc:`1832` simply maps their representation into a sequence of bytes. For example a 32 bits integer is transmitted as follows (with the most significant byte first, which corresponds to big-endian encoding).


.. figure:: /protocols/pkt/xdr-integer.png
   :align: center
 

XDR also supports 64 bits integers and booleans. The booleans are mapped onto integers (`0` for `false` and `1` for `true`). For the floating point numbers, the encoding defined in the IEEE standard is used.


.. figure:: /protocols/pkt/xdr-integer-64.png
   :align: center

In this representation, the first bit (`S`) is the sign (`0` represents positive). The next 11 bits represent the exponent of the number (`E`), in base 2, and the remaining 52 bits are the fractional part of the number (`F`). The floating point number that corresponds to this representation is :math:`(-1)^{S} \times 2^{E-1023} \times 1.F`. XDR also allows to encode complex data types. A first example is the string of bytes. A string of bytes is composed of two parts : a length (encoded as an integer) and a sequence of bytes. For performance reasons, the encoding of a string is aligned to 32 bits boundaries. This implies that some padding bytes may be inserted during the encoding operation if the length of the string is not a multiple of 4. The structure of the string is shown below (source :rfc:`1832`).


.. figure:: /protocols/pkt/xdr-double.png
   :align: center



In some situations, it is necessary to encode fixed or variable length arrays. XDR :rfc:`1832` supports such arrays. For example, the encoding below corresponds to a variable length array containing n elements. The encoded representation starts with an integer that contains the number of elements and follows with all elements in sequence. It is also possible to encode a fixed-length array. In this case, the first integer is missing. 

.. figure:: /protocols/pkt/xdr-array.png
   :align: center


XDR also supports the definition of unions, structures, ... Additional details are provided in :rfc:`1832`. 

A second popular method to encode data is the JavaScript Object Notation (JSON). This syntax was initially defined to allow applications written in JavaScript to exchange data, but it has now wider usages. JSON :rfc:`4627` is a text-based representation. The simplest data type is the integer. It is represented as a sequence of digits in ASCII. Strings can also be encoding by using JSON. A JSON string always starts and ends with a quote character (`"`) as in the C language. As in the C language, some characters (like `"` or `\\`) must be escaped if they appear in a string. :rfc:`4627` describes this in details. Booleans are also supported by using the strings `false` and `true`. Like XDR, JSON supports more complex data types. A structure or object is defined as a comma separated list of elements enclosed in curly brackets. :rfc:`4627` provides the following example as an illustration.

.. code-block:: javascript

   {
      "Image": {
          "Width":  800,
          "Height": 600,
          "Title":  "View from 15th Floor",
          "Thumbnail": {
              "Url":    "http://www.example.com/image/481989943",
              "Height": 125,
              "Width":  100
          },
          "ID": 1234
        }
   } 


This object has one field named `Image`. It has five attributes. The first one, `Width`, is an integer set to 800. The third one is a string. The fourth attribute, `Thumbnail` is also an object composed of three different attributes, one string and two integers. JSON can also be used to encode arrays or lists. In this case, square brackets are used as delimiters. The snippet below shows an array which contains the prime integers that are smaller than ten.

.. code-block:: javascript

   { 
     "Primes" : [ 2, 3, 5, 7 ]
   }

Compared with XDR, the main advantage of JSON is that the transfer syntax is easily readable by a human. However, this comes at the expense of a less compact encoding. Some data encoded in JSON will usually take more space than when it is encoded with XDR. More compact encoding schemes have been defined, see e.g. [BH2013]_ and the references therein.


Reaching the callee
-------------------

The second subproblem is how to reach the callee. A simple solution to this problem is to make sure that the callee listens on a specific port on the remote machine and then exchange information with this server process. This is the solution chosen for JSON-RPC [JSON-RPC2]_. JSON-RPC can be used over the connectionless or the connection-oriented transport. A JSON-RPC request contains the following information :

 - `jsonrpc`: a string indicating the version of the protocol used. This is important to allow the protocol to evolve in the future.
 - `method`: a string that contains the name of the procedure which is invoked
 - `params`: a structure that contains the values of the parameters that are passed to the method
 - `id`: an identifier chosen by the caller

The JSON-RPC is encoded as a JSON object. For example, the example below shows an invokation of a method called `sum` with `1` and `3` as parameters.

.. code-block:: javascript

    {"jsonrpc": "2.0", "method": "sum", "params": [1, 3], "id": 1}

Upon reception of this JSON structure, the callee parses the object, locates the corresponding method and passes the parameters. This method returns a response which is also encoded as a JSON structure. This response contains the following information :

 - `jsonrpc`: a string indicating the version of the protocol used to encode the response
 - `id`: the same identifier as the identifier chosen by the caller
 - `result`: if the request succeeded, this member contains the result of the request (in our example, value `4`).
 - `error`: if the method called does not exist or its execution causes an error, the `result` element will be replaced by an `error` element which contains the following members :

    - `code`: a number that indicates the type of error. Several error codes are defined in [JSON-RPC2]_. For example, `-32700` indicates an error in parsing the request, `-32602` indicates invalid parameters and `-32601` indicates that the method could not be found on the server. Other error codes are listed in [JSON-RPC2]_.
    - `message`: a string (limited to one sentence) that provides a short description of the error.
    - `data`: an optional field that provides additional information about the error.

Coming back to our example with the call for the `sum` procedure, it would return the following JSON structure.

.. code-block:: javascript

   { "jsonrpc": "2.0", "result": 4, "id": 1} 


If the `sum` method is not implemented on the server, it would reply with the following response.

.. code-block:: javascript

   { "jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": "1"}


The `id` field, which is present in the request and the response plays the same role as the identifier field in the DNS message. It allows the caller to match the response with the request that it sent. This `id` is very important when JSON-RPC is used over the connectionless service which is unreliable. If a request is sent, it may need to be retransmitted and it is possible that a callee will receive twice the same request (e.g. if the response for the first request was lost). In the DNS, when a request is lost, it can be retransmitted without causing any difficulty. However with remote procedure calls in general, losses can cause some problems. Consider a method which is used to deposit money on a bank account. If the request is lost, it will be retransmitted and the deposit will be eventually performed. However, if the response is lost, the caller will also retransmit its request. This request will be received by the callee that will deposit the money again. To prevent this problem from affecting the application, either the programmer must ensure that the remote procedures that it calls can be safely called multiple times or the application must verify whether the request has been transmitted earlier. In most deployments, the programmers use remote methods that can be safely called multiple times without breaking the application logic. 

.. index:: portmapper

ONC-RPC uses a more complex method to allow a caller to reach the callee. On a host, server processes can run on different ports and given the limited number of port values (:math:`2^{16}` per host on the Internet), it is impossible to reserve one port number for each method. The solution used in ONC-RPC :rfc:`1831` is to use a special method which is called the `portmapper` :rfc:`1833`. The `portmapper` is a kind of directory that runs on a server that hosts methods. The `portmapper` runs on a standard port (`111` for ONC-RPC :rfc:`1833`). A server process that implements a method registers its method on the local `portmapper`. When a caller needs to call a method on a remote server, it first contacts the `portmapper` to obtain the port number of the server process which implements the method. The response from the portmapper allows it to directly contact the server process which implements the method.


.. rubric:: Footnotes


.. include:: /links.rst
