.. Copyright |copy| 2013 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

.. _DNSSEC:

Securing the Domain Name System
===============================

The Domain Name System provides a critical service in the Internet 
infrastructure since it maps the domain names that are used by endusers 
onto IP addresses. Since endusers rely on names to identify the servers
that they connect to, any incorrect information distributed by the DNS
would direct endusers' connections to invalid destinations. Unfortunately,
several attacks of this kind occurred in the past. A detailed analysis
of the security threats against the DNS appeared in :rfc:`3833`. We consider
three of these threats in this section and leave the others to :rfc:`3833`.

The first type of attack is `eavesdropping`. An attacker who can capture
packets sent to a DNS resolver or a DNS server can gain valuable information
about the DNS names that are used by a given enduser. If the attacker can
capture all the packets sent to a DNS resolver, he/she can collect a lot of
meta data about the domain names used by the enduser. Preventing this type
of attack has not been an objective of the initial design of the DNS. 
There are currently discussions with the IETF to carry DNS messages over
TLS sessions to protect against such attacks. However, these solutions
are not yet widely deployed.

The second type of attack is the `man-in-the-middle` attack. Consider that
Alice is sending DNS requests to her DNS resolver. Unfortunately, Mallory
sits in front of this resolver and can capture and modify all the packets
sent by Alice to her resolver. In this case, Mallory can easily modify
the DNS responses sent by the resolver to redirect Alice's packets to
a different IP address controlled by Mallory. This enables Mallory
to observe (and possibly modify) all the packets sent and received by
Alice. In practice, executing this attack is not simple since DNS resolvers
are usually installed in protected datacenters. However, if Mallory controls
the WiFi access point that Alice uses to access the Internet, he could easily
modify the packets on this access point and some software packages 
automate this type of attacks. 

If Mallory cannot control a router on the path
between Alice and her resolver, she could still launch a different attack.
To understand this attack, it is important to correctly understand how
the DNS protocol operates and the roles of the different fields of 
the DNS header which is reproduced in the figure below.

.. figure:: /../book/application/pkt/dnsheader.png
   :align: center
   :scale: 100

   DNS header

The first field of the header is the `Identification` field. When Alice
sends a DNS request, she places a 16-bits integer in this field and
remembers it. When she receives a response, she uses this `Identification`
field to locate the initial DNS request that she sent. The response is
only used if its `Identification` matches a pending DNS request (containing
the same question).

.. index:: cache poisoning attack (DNS)

Mallory has studied the DNS protocol and understands how it works. If he
can predict a popular domain for which Alice will regularly send DNS requests,
then he can prepare a set of DNS responses that map the name requested
by Alice to an IP address controlled by Mallory instead of the legitimate
DNS response. Each DNS response has a different `Identification`. Since there
are only 65,536 values for the `Identification` field, it is possible 
for Mallory to
send them to Alice hoping that one of them will be received while Alice
is waiting for a DNS response with the same identifier. In the past, 
it was difficult to send 65,536 DNS responses quickly enough. However, with
the high speed links that are available today, this is not an issue anymore.
A second concern for Mallory is that he must be able to send 
the DNS responses as if they were coming directly from the DNS resolver. 
This implies that Mallory must be able to send IP packets that appear to
originate from a different address. Although networks should be configured
to prevent this type of attack, this is not always the case and there
are networks where it is possible for a host to send packets with a
different source IP address [#fspoof]_. If the attack targets a single
enduser, e.g. Alice, this is annoying for this user. However, if the
attacker can target a DNS resolver that serves an entire company or an
entire ISP, the impact of the attack can be much larger in particular if
the injected DNS response carries a long TTL and thus resides in the
resolver's cache for a long period of time.

Fortunately, DNS implementors have found solutions to mitigate this type
of attack. The easiest approach would have been to update the format of the
DNS requests and responses to include a larger `Identifier` field. 
Unfortunately, this elegant solution was not possible with the DNS because
the DNS messages do not include any version number that would have enabled
such a change. Since the DNS messages are exchanged inside UDP segments,
the DNS implementors found an alternate solution to counter this attack. 
There are two ways for the DNS library used by Alice to send her DNS requests.
A first solution is to bind one UDP source port and always send the
DNS requests from this source port (the destination port is always port
``53``). The advantage of this solution is that Alice's DNS library can
easily receive the DNS responses by listening to her chosen port. 
Unfortunately, once the attacker has found the source port used by Alice,
he only needs to send 65,536 DNS responses to inject an invalid response.
Fortunately, Alice can send her DNS requests in a different way. Instead
of using the same source port for all DNS requests, she can use a different
source port for each request. In practice, each DNS request will be sent
from a different source port. From an implementation viewpoint, this
implies that Alice's DNS library will need to listen to one different port
number for each pending DNS request. This increases the complexity of
her implementation. From a security viewpoint there is a clear benefit
since the attacker needs to guess both the 16 bits `Identifier` and the
16 bits `UDP source port` to inject a fake DNS response. To generate all
possible DNS responses, the attacker would need to generate almost
:math:`2^{32}` different messages, which is excessive in today's networks. 
Most DNS implementations use this second approach to prevent these cache
poisoning attacks.

These attacks affect the DNS messages that are exchanged between a client
and its resolver or between a resolver and name servers. Another type of
attack exploits the possibility of providing several resource records inside
one DNS response. A frequent optimisation used by DNS servers and resolvers
is to include several related resource records in each response. For
example, if a client sends a DNS query for an `NS` record, it usually
receives in the response both the queried record, i.e. the name of
the DNS server that serves the queried domain, and the IP addresses of this
server. Some DNS servers return several `NS` records and the associated IP
addresses. The `cache poisoning` attack exploits this DNS optimisation.

Let us illustrate it on an example. 
Assume that Alice frequently uses the `example.net` domain and in 
particular the 
web server whose name is `www.example.net`. Mallory would like to redirect
the TCP connections established by Alice towards `www.example.net` to one
IP address that he controls. Assume that Mallory controls the 
`mallory.net` domain. Mallory can tune the DNS server of his domain and add
special DNS records to the responses that it sends. An attack could go
roughly as follows. Mallory forces Alice to visit the `www.mallory.net` web
site. He can achieve this by sending a spam message to Alice or buying
advertisements on a web site visited by Alice and redirect one of these
advertisements to `www.mallory.net`. When visiting the advertisement, Alice's
DNS resolver will send a DNS request for `www.mallory.net`. Since Mallory
control the DNS server, he can easily add in the response a `AAAA`
record that associates `www.example.net` to the IP address controlled by 
Mallory. If Alice's DNS library does not check the returned response, 
the cache entry for `www.example.net` will be replaced by the `AAAA` record
sent by Mallory. 

To cope with these security threats and improve the security of the
DNS, the IETF has defined several extensions that are known as DNSSEC.
DNSSEC exploits public-key cryptography to authenticate the content
of the DNS records that are sent by DNS servers and resolvers. DNSEC is
defined in three main documents :rfc:`4033`, :rfc:`4034`, :rfc:`4035`. 
With DNSSEC, each DNS zone uses one public-private key pair. This key pair
is only used to sign and authenticate DNS records. The DNS records are
not encrypted and DNSSEC does not provide any confidentiality. Other DNS
extensions are being developed to ensure the confidentiality of the 
information exchanged between a client and its resolvers :rfc:`7626`. 
Some of these extensions exchange DNS records over a TLS session which
provides the required confidentiality, but they are not yet deployed 
and outside the scope of this chapter. 

DNSSEC defines four new types of DNS records that are used together to
authenticate the information distributed by the DNS. 

 - the `DNSKEY` record allows to store the public key associated with 
   a zone. This record is encoded as a TLV and includes a `Base64`
   representation of the key and the identification of the public key
   algorithm. This allows the `DNSKEY` record to support different public 
   key algorithms.
 - the `RRSIG` record is used to encode the signature of a DNS record. This
   record contains several subfields. The most important ones are the
   algorithm used to generate the signature, the identifier of the public 
   key used to sign the record, the original TTL of the signed record and 
   the validity period for the signature. 
 - the `DS` record contains a hash of a public key. It is used by a parent
   zone to certify the public key used by one of its child zones.
 - the `NSEC` record is used when non-existent domain names are queried. 
   Its usage will be explained later

The simplest way to understand the operation of DNSSEC is to rely on a simple
example. Let us consider the `example.org` domain and assume that Alice
wants to retrieve the `AAAA` record for `www.example.org` using DNSSEC. 

.. index:: anchored key

The security of DNSSEC relies on `anchored keys`. An `anchored key` is a
public key that is considered as trusted by a resolver. In our example,
we assume that Alice's resolver has obtained the public key of the servers 
that manage the root zone in a secure way. This key
has been distributed outside of the DNS, e.g. it has been published in a
newspaper or has been received in a sealed letter. 

To obtain an authenticated record for `www.example.org`, Alice's resolver
first needs to retrieve the `NS` which is responsible for the `.org`
Top-Level Domain (TLD). This record is served by the DNS root server
and Alice's resolver can retrieve the signature (`RRSIG` record) for this
`NS` record. Since Alice knows the `DNSKEY` of the root, she can verify
the validity of this signature. 

The next step is to contact `ns.org`, the `NS` responsible for
the `.org` TLD to retrieve the `NS` record for the `example.org` domain.
This record is accompanied by a `RRSIG` record that authenticates it. This
`RRSIG` record is signed with the key of the `.org` domain. Alice's resolver
can retrieve this public key as the `DNSKEY` record for the `.org`, but how
can it trust this key since it is distributed by using the DNS and
could have been modified by attackers ? DNSSEC solves this problem by
using the `DS` record that is stored in the parent zone (in this case,
the root zone). This record contains a hash of a public key that
is signed with a `RRSIG` signature. Since Alice's resolver's
trusts the root key, it can validate the signature of the `DS` record
for the `.org` domain. It can then retrieve the `DNSKEY` record for this
domain from the DNS and compare the hash of this key with the `DS` record.
If they match, the public key of the `.org` domain can be trusted.
The same technique is used to obtain and validate the key of
the `example.org` domain. Once this key is trusted, Alice's resolver
can request the `AAAA` record for `www.example.org` and validate its
signature.

Thanks to the `DS` record, a resolver can validate the public keys of client
zones as long as their is a chain of `DS` -> `DNSKEY` records from an
anchored key. If the resolver trusts the public key of the root zone, it
can validate all DNS replies for which this chain exists. 

There are several details of the operation of DNSSEC that are worth
being discussed. First, a server that supports DNSSEC must have a 
public-private key pair. The public key is distributed with the
`DNSKEY` record. The private key is never distributed and it does not
even need to be stored on the server that uses the public key. DNSSEC does
not require the DNSSEC servers to perform any operation that requires
a private key in real time. All the `RRSIG` records can be computed 
offline, possibly on a different server than the server that returns
the DNSSEC replies. The initial motivation for this design choice was
the CPU complexity of computing the `RRSIG` signatures for zones that
contain millions of records. In the early days of DNSSEC, this was an 
operational constraint. Today, this is less an issue, but avoiding
costly signature operations in real time has two important benefits. 
First, this reduces the risk of denial of service attacks since an attacker
cannot force a DNSSEC server to perform computationally intensive signing
operations. Second, the private key can be stored offline, which means that
even if an attacker gains access to the DNSSEC server, it cannot retrieve
its private key. Using offline signatures for the `RRSIG` records has some
practical implications that are reflected in the content of this
record. First, each `RRSIG` record contains the original TTL of the 
signed record.
When DNS resolvers cache records, they change the value of the TTL of
these cached records and then return the modified records to their clients. 
When a resolver receives a signed DNS record, it must replace the
received TTL of the record with the original TTL (and check that the
received TTL is smaller than the original one) before checking the
signature. Second, the `RRSIG` records contain a validity period, i.e. 
a starting time and an ending time for the validity of the signature. This 
period is specified as two timestamps. This period is only the
validity of the signature. It does not affect the TTL of the signed record
and is independant from the TTL. In practice, the validity period is
important to allow DNS server operators to update their public/private
keys. When such a key is changed, e.g. because the private could have been
compromised, there is some period of time during which records signed
with the two keys coexist in the network. The validity period allows to
ensure that old signatures do not remain in DNS caches for ever. 

.. index:: NSEC

The last record introduced by DNSSEC is the `NSEC` record. It is used to
authenticate a negative response returned by a DNS server. If a resolver
requests a domain name that is not defined in the zone, the server
replies with an error message. The designers of the original version
of the DNS thought that these errors would not be very frequent
and resolvers were not required to cache those negative responses.
However, operational experience showed that queries for invalid domain
names are more frequent than initially expected and a large fraction
of the load on some servers is caused by repeated queries for invalid
names. Typical examples include queries for invalid TLDs to the root
DNS servers or queries caused by configuration errors [WF2003]_. 
Current DNS deployments allow resolvers to cache those negative answers
to reduce the load on the entire DNS :rfc:`2308`. 

The simplest way to allow a DNSSEC server to return signed negative responses
would be for the serve to return a signed response that contains the
received query and some information indicating the error. 
The client could then easily check the validity of the negative response.
Unfortunately, this would force the DNSSEC server to generate signatures
in real time. This implies that the private key must be stored in the
server memory, which leads to risks if an attacker can take control
of the server. Furthermore, those signatures are computationally complex
and a simple denial of service attack would be to send invalid queries
to a DNSSEC server.

Given the above security risks, DNSSEC opted for a different approach that
allows the negative replies to be authenticated by using offline signatures.
The `NSEC` record exploits the lexicographical ordering of all the domain
names. To understand its usage, consider a simple domain that contains 
three names (the associated `AAAA` and other records that are not
shown) :

.. code-block:: console

   alpha.example.org
   beta.example.org
   gamma.example.org


In this domain, the DNSSEC server adds three `NSEC` records. A `RRSIG`
signature is also computed for each of these records.

.. code-block:: console

   alpha.example.org
   alpha.example.org NSEC beta.example.org

   beta.example.org
   beta.example.org NSEC gamma.example.org

   gamma.example.org
   gamma.example.org NSEC alpha.example.org


If a resolver queries `delta.example.org`, the server will parse its
zone. If this name were present, it would have been placed, in lexicographical
order, between the `beta.example.org` and the `gamma.example.org` names.
To confirm that the `delta.example.org` name does not exist, the server
returns the `NSEC` record for `beta.example.org` that indicates that the
next valid name after `beta.example.org` is `gamma.example.org`. If 
the server receives a query for `pi.example.org`, this is the `NSEC` record
for `gamma.example.org` that will be returned. Since this record
contains a name that is before `pi.example.org` in lexicographical 
order, this indicates that `pi.example.org` does not exist. 


.. rubric:: Footnotes


.. [#fspoof] See http://spoofer.caida.org/summary.php for an ongoing 
measurement study that analyses the networks where an attacker could send
packets with any source IP address.

.. include:: /links.rst
