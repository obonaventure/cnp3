.. Copyright |copy| 2010 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by-sa/3.0/>`_

========================================================
Computer Networking : Principles, Protocols and Practice
========================================================

Contents:

.. toctree::
   :maxdepth: 2

The application layer
=====================

This set of questions covers several application layer protocols. We expect each group to organise themselves appropriately in order to provide detailed answers to every question.


The Domain Name System
.......................

The Domain Name System (DNS) plays a key role in the Internet today as it allows
 applications to use fully qualified domain names (FQDN) instead of IPv4 or IPv6
 addresses. Many tools enable queries through DNS servers. For this exercise, we will use dig_ ,which is installed on most Unix systems. 

A typical usage of dig is as follows :: 

  dig @server -t type fqdn 

where

`server` is the IP address or the name of a DNS server or resolver
`type` is the type of DNS record that is requested by the query such as
`NS` for a nameserver, `A` for an IPv4 address, `AAAA` for an IPv6 address, `MX` for a mail relay, ...
`fqdn` is the fully qualified domain name being queried

#. What are the IP addresses of the resolvers that the `dig` implementation you are using relies on [#fdig]_ ?

#. What is the IP address that corresponds to `inl.info.ucl.ac.be ? Which type of DNS query does `dig` send to request this information ?

#. Which type of DNS request do you need to send to obtain the nameservers that are responsible for a given domain ?

#. What are the nameservers that are responsible for the `be` top-level domain ? Where are they located ? Is it possible to use IPv6 to query them ?

#. When run without any parameter, `dig` queries one of the root DNS servers and retrieves the list of names of all DNS servers. For technical reasons, there are only 13 different root DNS servers. This information is also available as a text file from http://www.internic.net/zones/named.root What are the IPv4 addresses of all these servers. Do they all support IPv6 [#rs]_ ? 

#. Assume now that you are residing in a network where there is no DNS resolver and that you need to start your query from the DNS root.

   - Use `dig` to send a query to one of these root servers to find the IP address of the DNS server(s) (NS record) responsible for the `org` top-level domain
   - Use `dig` to send a query to one of these DNS servers to find the IP address of the DNS server(s) (NS record) responsible for root-servers.org`
   - Continue until you find the server responsible for `www.root-servers.org`
   - What is the lifetime associated to this IP address ?

#. Perform the same analysis for a popular website such as `www.google.com`. What is the lifetime associated to this IP address ? If you perform the same request several times, do you always receive the same answer ? Can you explain why a lifetime is associated to the DNS replies ?

#. Use `dig` to find the mail relays used by the `uclouvain.be` and `gmail.com` domains. What is the `TTL` of these records (use the `+ttlid` option when using `dig`) ? Can you explain the preferences used by the `MX`records. You can find more information about the MX records in rfc794_ 

#. Use `dig` to query the IPv6 address (DNS record AAAA) of the following hosts

   - `www.sixxs.net`
   - `www.google.com`
   - `ipv6.google.com`

#. When `dig` is run, the header section in its output indicates the `id` the DNS identifier used to send the query. Does your implementation of `dig` generates random identifiers ? ::

	dig -t MX gmail.com

	; <<>> DiG 9.4.3-P3 <<>> -t MX gmail.com
	;; global options:  printcmd   
	;; Got answer:
	;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25718


#. A DNS implementation such as `dig` and more importantly a name resolver such as bind_ or unbound_, always checks that the received DNS reply contains the same identifier as the DNS request that it sent. Why is this so important ?

   - Imagine an attacker who is able to send forged DNS replies to, for example, associate `www.bigbank.com` to his own IP address. How could he attack a DNS implementation that

     - sends DNS requests containing always the same identifier
     - sends DNS requests containing identifiers that are incremented by one after each request
     - sends DNS requests containing random identifiers

#. The DNS protocol can run over UDP and TCP. Most DNS servers prefer to use UDP because it consumes fewer resources on the server. However, TCP is useful when a large answer is expected or when a large answer must Use `time dig +tcp ` to query a root DNS server. Is it faster to receive an answer via TCP or via UDP ?


Internet email protocols
.........................	

Many Internet protocols are ASCII_-based protocols where the client sends requests as one line of ASCII_ text terminated by `CRLF`, and the server replies with one of more lines of ASCII_ text. Using these ASCII messages has several advantages compared to protocols that rely on binary encoded messages

   - the messages exchanged by the client and the server can easily be understood by a developer or network engineer by simply reading the messages
   - it is often easy to write a small prototype that implements a part of the protocol
   - it is possible to test a server manually by using telnet_ Telnet is a protocol that allows to obtain a terminal on a remote server. For this, telnet opens a TCP connection with the remote server on port 23. However, most `telnet` implementations allow the user to specify an alternate port as `telnet hosts port` When used with a port number as parameter, `telnet` opens a TCP connection to the remote host on the specified port. `telnet` can thus be used to test any server using an ASCII-based protocol on top of TCP. Note that if you need to stop a running `telnet` session, Ctrl-C will not work as it will be sent by `telnet`to the remote host over the TCP connection. On many `telnet` implementations you can type `Ctrl-]` to freeze the TCP connection and return to the telnet interface.

.. warning::
   Do *not* try this on a random SMTP server. The exercises proposed in this section should only be run on the lab SMTP server. If you try them on a production SMTP server, the administrator of this server may become angry.

#. Assume that your are sending an email from your `@student.uclouvain.be` inside the university to another student's `@student.uclouvain.be` address. Which protocols are involved in the transmission of this email ?

#. Same question when you are sending an email from  your `@student.uclouvain.be` inside the university to another student's `@gmail.com` address

#. Before the advent of webmail and feature rich mailers, email was written and read by using command line tools on servers. Using your account on `sirius.info.ucl.ac.be` use the `/bin/mail` command line tool to send an email to yourself *on this host*. This server stores local emails in the `/var/mail` directory with one file per user. Check with `/bin/more` the content of your mail file and try to understand which lines have been added by the server in the header of your email.

#. Use your preferred email tool to send an email message to yourself containing a single line of text. Most email tools have the ability to show the `source` of the message, use this function to look at the message that you sent and the message that you received. Can you find an explanation for all the lines that have been added to your single line email [#fsmtpevol]_ ?

#. The first version of the SMTP protocol was defined in rfc821_. The current draft standard for SMTP is defined in rfc5321_ Considering from rfc821_ what are the main commands of the `SMTP` protocol [#fsmtp]_ ? 

#. When using SMTP, how do you recognise a positive reply from a negative one ?

#. A SMTP server is a daemon process that can fail due to a bug or lack of resources (e.g. memory). Network administrators often install tools [#fmonitoring] that regularly connect to their servers to check that they are operating correctly. A simple solution is to open a TCP connection on port 25 to the SMTP server's host [#fblock]. If the connection is established, this implies that there is a processing listening. What is the reply sent by the SMTP server when you type the following command ::
   telnet smtpserver 25

#. Continue the SMTP session that you started above by sending the greetings command (`EHLO` followed by the fully qualified domain name of your host) and terminate the session by sending the `QUIT` command.

#. The minimum SMTP session above allows to verify that the SMTP is running. However, this does not always imply that mail can be delivered. For example, large SMTP servers often use a database to store all the email addresses that they serve. To verify the correct operation of such a server, one possibility is to use the VRFY command. Open an SMTP session on the lab's SMTP server and use this command to verify that your account is active. 

#. Now that you know the basics of opening and closing an SMTP session, you can now send email manually by using the `MAIL FROM:`, `RCPT TO:` and `DATA` commands. Use these commands to manually send an email to INGI2141@smtpserver. Do not forget to include the `From:`, `To:` and `Subject:` lines in your header.
 
#. By using SMTP, is it possible to send an email that contains the following ASCII art ::

   .
   ..
   ...

#. Most email agents allow you to send email in carbon-copy (`cc:`) and also in blind-carbon (`bcc:`) to a recipient. How does a SMTP server supports these two types of destinations ?

#. In the early days, email was read by using tools such as `/bin/mail` or more advanced text-based mail readers such as pine_ or elm_ . Today, emails are stored on dedicated servers and retrieved by using protocols such as POP_ or IMAP_ From the user's viewpoint, can you list the advantages and drawbacks of these two protocols ?

#. The TCP protocol supports 65536 different ports numbers. Many of these port numbers have been reserved for some applications. The official repository of the reserved port numbers is maintained by the Internet Assigned Numbers Authority (IANA_) on http://www.iana.org/assignments/port-numbers [#fservices]_ Using this information, what is the default port number for the POP3 protocol ? Does it run on top of UDP or TCP ?

#. The Post Office Protocol (POP) is a rather simple protocol described in rfc1939_ POP operates in three phases. The first phase is the authorization phase where the client provides a username and a password. The second phase is the transaction phase where the client can retrieve emails. The last phase is the update phase where the client finalises the transaction. What are the main POP commands and their parameters ? When a POP server returns an answer, how can you easily determine whether the answer is positive or negative ? 

#. On smartphones, users often want to avoid downloading large emails over a slow wireless connection. How could a POP client only download emails that are smaller than 5 KBytes ?

#. Open a POP session with the lab's POP by using the username and password that you received. Verify that your username and password are correct.

#. The lab's POP server contains a script that runs every minute and sends two emails to your account if your email folder is free. Use POP to retrieve these two emails and provide your two secret messages.



The HyperText Transfer Protocol
................................


#. What are the main methods supported by the first version of the HyperText Transfer Protocol (HTTP) defined in rfc1945_ [#fhttp1]_ ? What are the main types of replies sent by a http server [#fhttp2]_ ?

#.  System administrators who are responsible for web servers often want to monitor these servers and check that they are running correctly. As a HTTP server uses TCP on port 80, the simplest solution is to open a TCP connection on port 80 and check that the TCP connection is accepted by the remote host. However, as HTTP is an ASCII-based protocol, it is also very easy to write a small script that downloads a web page on the server and compares its content with the expected one. Use `telnet` to verify that a web server is running on host `rembrandt.info.ucl.ac.be` [#fhttp]_

#. Instead of using `telnet` on port 80, it is also possible to use a command-line tool such as curl_ Use curl_ with the `--trace-ascii tracefile` option to store in `tracefile` all the information exchanged by curl when accessing the server.

   - what is the version of HTTP used by curl ?
   - can you explain the different headers placed by curl in the request ?
   - can you explain the different headers found in the response ?

#. HTTP 1.1, specified in rfc2616_ forces the client to use the `Host:` in all its requests. HTTP 1.0 does not define the `Host:` header, by most implementations support it. By using `telnet` and `curl` retrieve the first page of the http://totem.info.ucl.ac.be webserver. Explain the difference between the two [#ftotem]. 

#. By using dig_ and curl_ , determine on which physical host the http://www.info.ucl.ac.be, http://inl.info.ucl.ac.be and http://totem.info.ucl.ac.be are hosted

#. Use curl_ with the `--trace-ascii filename` to retrieve http://www.google.com . Explain what a browser such as firefox would do when retrieving this URL.

#. The headers send in a HTTP request allow the client to provide additional information to the user. One of these headers is the Language header that allows to indicate the preferred language of the client [#lang]_. For example, `curl -HAccept-Language:en http://www.google.be' will send to `http://www.google.be` a HTTP request indicating English (en) as the preferred language. Does google provide a different page in French (fr) and Walloon (wa) ? Same question for http://www.uclouvain.be (given the size of the homepage, use diff to compare the different pages retrieved from www.uclouvain.be)

#. Compare the size of the http://www.yahoo.com and http://www.google.com web pages. 


.. [#fdig] On a Linux machine, the *Description* section of the `dig` manpage tells you where `dig` finds the list of nameservers to query.

.. [#rs] You may obtain additional information about the root DNS servers from http://www.root-servers.org

.. [#fblock] Note that using `telnet` to connect to a remote host on port 25 may not work in all networks. Due to the spam_ problem, many :term:`ISP` networks do not allow their customers to use port TCP 25 directly and force them to use the ISP's mail relay to forward their email. Thanks to this, if a software sending spam has been installed on the PC of one of the ISP's customers, this software will not be able to send a huge amount of spam. If you connect to the SMTP server from the lab, you should not be blocked.

.. [#fmonitoring] There are many `monitoring tools <http://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems>`_ available. nagios_ is a very popular open source monitoring system. 

.. [#fsmtp] A shorter description of the SMTP protocol may be found on wikipedia at http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol

.. [#fsmtpevol] Since rfc821_, SMTP has evolved a lot due notably to the growing usage of email and the need to protect the email system against spammers. It is unlikely that you will be able to explain all the additional lines that you will find in email headers, but we'll discuss them together.

.. [#fservices] On Unix hosts, a subset of the port assignments is often placed in `/etc/services`

.. [#fhttp] The minimum command sent to a HTTP server is `GET / HTTP/1.0` followed by CRLF and a blank line

.. [#fhttp1] See section 5 of rfc1945_

.. [#fhttp2] See section 6.1 of rfc1945_

.. [#ftotem] Use dig_ to find the IP address used by `totem.info.ucl.ac.be`

.. [#lang] The list of available language tags can be found at http://www.loc.gov/standards/iso639-2/php/code_list.php Additional information about the support of multiple languages in Internet protocols may be found in rfc5646_

.. include:: ../links.rst
