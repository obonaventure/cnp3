.. Copyright |copy| 2013 by Justin Vellemans, Florentin Rochet, David Lebrun, Juan Antonio Cordero, Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_

Inter-domain routing
====================

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues/new


Exercises
---------

1. Consider the interdomain topology shown in the figure below.


.. graphviz::

   digraph foo {
      randkir=LR;
      AS1 -> AS3 [label=<<font color="red">$</font>>, color=red];
      AS1 -> AS2 [label=<<font color="red">$</font>>, color=red];
      AS2 -> AS3 [dir=none,label=<<font color="blue">=</font>>, color=blue];
      AS4 -> AS2 [label=<<font color="red">$</font>>, color=red];
      AS4 -> AS3 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
   }


In this network, what are the paths :

  - from `AS1` to `AS4` 
  - from `AS4` to `AS2` 
  - from `AS4` to `AS1`


2. Consider the interdomain topology shown in the figure below. Assuming, that `AS1` advertises prefix ``2001:db8:1::/48``,  `AS2` prefix ``2001:db8:2::/48``, ... compute the routing tables of the different ASes.


.. graphviz::

   digraph foo {
      randkir=LR;
      AS1 -> AS4 [label=<<font color="red">$</font>>, color=red];
      AS3 -> AS4 [label=<<font color="red">$</font>>, color=red];
      AS3 -> AS1 [label=<<font color="red">$</font>>, color=red];
      AS2 -> AS3 [dir=none,label=<<font color="blue">=</font>>, color=blue];
      AS2 -> AS1 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
   }


Are all ASes capable of reaching all the other ASes in this simple Internet ?

3. The interdomain topology below is composed of four domains. For this exercise, we assume that there are no routing policies, i.e. each domain advertise all its best paths to its peers. We focus on the prefix `p` advertised by `AS1`.

.. graphviz::

   graph foo {
      randkir=LR;
      AS1 -- AS3; 
      AS1 -- AS2;
      AS3 -- AS4; 
      AS1 -- AS4;
   }

Assume that the BGP sessions are activated in the following order :

  - `AS1-AS2`
  - `AS2-AS1` 
  - `AS3-AS4` 
  - `AS1-AS3`
  - `AS1-AS4`

At each step of this activation sequence, show the BGP messages for prefix `p` that are exchanged and provide the BGP routing table of the different ASes. Assume that BGP always prefers the short AS-Path.

Once the interdomain network has fully converged, analyze the consequence of a failure of the following BGP sessions on the routes towards prefix `p` :

  - `AS1-AS2`
  - `AS1-AS4`



4. Consider the interdomain topology shown in the figure below. Assuming, that `AS1` advertises prefix ``2001:db8:1::/48``,  `AS2` prefix ``2001:db8:2::/48``, ... compute the routing tables of the different ASes.


  .. graphviz::

     digraph foo {
       randkir=LR;
       AS4 -> AS1 [label=<<font color="red">$</font>>, color=red];
       AS4 -> AS2 [label=<<font color="red">$</font>>, color=red];
       AS3 -> AS2 [dir=none,label=<<font color="blue">=</font>>, color=blue];
       AS2 -> AS1 [dir=none,label=<<font color="blue">=</font>>, color=blue];
       AS3 -> AS1 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
       AS3 -> AS5 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
       AS4 -> AS5 [dir=none,label=<<font color="blue">=</font>>, color=blue];   
       }

 In this internet, some ASes cannot reach all other ASes. Can you fix the problem by adding one shared-cost peering link or one customer-provider peering link ?

5. Consider the network below in which a stub domain, `AS456`, is connected to two providers `AS123` and `AS789`. `AS456` advertises its prefix to both its providers. On the other hand, `AS123` advertises ``2001:db8:dead::/48`` while `AS789` advertises ``2001:db8:beef::/48`` and ``2001:db8:dead:cafe::/63``. Via which provider will the packets destined to ``2001:db8:dead:cafe::1`` will be received by `AS456` ?

  .. figure:: fig/ex-bgp-stub-two-providers.png
     :align: center
     :scale: 100


 
 Should `AS123` change its configuration ? 

6. Consider that the AS stub (`AS456`) shown in the figure below decides to advertise two ``/48`` prefixes instead of its allocated ``/47`` prefix.


  .. figure:: fig/ex-bgp-stub-two-providers-specific.png
     :align: center
     :scale: 100


 - Via which provider does `AS456` receive the packets destined to ``2001:db8:caff::bb`` and ``2001:db8:cafe::aa`` ?
  
  - How is the reachability of these addresses affected when link `R1`-`R3` fails ?

  - Propose a configuration on R1 that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS456` if one of `AS456`'s interdomain links fails.

7. Consider the network shown below. In this network, the metric of each link is set to `1` except link `A-B` whose metric is set to `4` in both directions. In this network, there are two paths with the same cost between `D` and `C`. Old routers would randomly select one of these equal cost paths and install it in their forwarding table. Recent routers are able to use up to `N` equal cost paths towards the same destination. 

 .. figure:: ../../book/network/svg/ex-five-routers-weigth4.png
    :align: center
    :scale: 30

    A simple network 

 On recent routers, a lookup in the forwarding table for a destination address returns a set of outgoing interfaces. How would you design an algorithm that selects the outgoing interface used for each packet, knowing that to avoid reordering, all segments of a given TCP connection should follow the same path ? 

8. A ``traceroute6`` towards ``ipv6.google.com`` provides the following output :

   .. code-block:: console

      traceroute6 to ipv6.l.google.com (2a00:1450:4009:800::1001) from 2a02:2788:2c4:16f:5099:ccba:671d:e085, 64 hops max, 12 byte packets
      1  2a02:2788:2c4:16f:a221:b7ff:fed8:aa90  4.777 ms  1.189 ms  1.023 ms
      2  2a02:2788:2c0::1  8.746 ms  7.934 ms  10.024 ms
      3  2a02:2788:2c0:3::1  10.039 ms  14.967 ms  8.943 ms
      4  2a02:2788:ffff:12::1  9.808 ms  11.076 ms  13.658 ms
      5  xe-4-2.r00.brslbe01.be.bb.gin.ntt.net  10.043 ms  10.408 ms  9.551 ms
      6  ae-10.r02.amstnl02.nl.bb.gin.ntt.net  15.591 ms  18.416 ms  15.665 ms
      7  core1.ams.net.google.com  21.259 ms  24.261 ms  20.826 ms
      8  2001:4860::1:0:4b3  19.134 ms
         2001:4860::1:0:8  22.208 ms
         2001:4860::1:0:4b3  19.713 ms
      9  2001:4860::8:0:519f  26.712 ms
         2001:4860::8:0:51a0  25.313 ms  19.392 ms
      10  2001:4860::8:0:5bb8  24.197 ms
          2001:4860::8:0:5bb9  25.337 ms  26.264 ms
      11  2001:4860::1:0:3067  29.431 ms  31.585 ms  29.260 ms
      12  2001:4860:0:1::9  24.806 ms  24.297 ms  23.819 ms
      13  lhr14s23-in-x01.1e100.net  29.406 ms  25.729 ms  29.160 ms


 Can you explain why at the eighth, ninth and tenth hopes several IPv6 addresses are reported in the ``traceroute6`` output ?

9. `Section 3.3 <https://tools.ietf.org/html/rfc4443#section-3.3>`_ of :rfc:`4443` explains two different reasons why an IPv6 enabled device could generate an ICMPv6 Time Exceeded message. Explain when a router could generate such a message with ``Code==0`` and when a host could generate such a message with ``Code==1``. 

10. `Section 3.1 <https://tools.ietf.org/html/rfc4443#section-3.1>`_ of :rfc:`4443` seven different Codes for the ICMPv6 Destination Unreachable Message. Under which circumstances would a router generate such an ICMPv6 message with :

   - ``Code==0``

 .. No address in forwarding table

   - ``Code==1`` 

 .. firewall

   - ``Code==3`` 
   
 .. host unreachable on LAN

   - ``Code==4``
  
 .. no daemon running on this destination port (likely UDP)

11. An ICMPv6 error message includes in its message body the beginning of the IPv6 packet that triggered this error. How many bytes of the original packet must be returned to allow the host to recover the original source and destination addresses and source and destination ports of the packet that caused the error ?
  
  .. 40 bytes for IPv6 and 4 bytes for the port numbers



.. include:: /links.rst
