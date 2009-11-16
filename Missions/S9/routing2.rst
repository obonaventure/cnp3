OSPF and BGP
============


In this set of exercices, you will explore in more details the operation of a link-state routing protocol such as OSPF and the operation of BGP.

The deadline for this exercise is Tuesday November 24th, 13.00.



Link state routing
------------------






BGP
---

1 Consider the network shown in the figure below and explain the path that will be followed by the packets to reach `194.100.10.0/23`
 .. figure:: fig/BGP-figs-001-c.png
    :align: center
    :scale: 50
   
    A stub connected to one provider

2 Consider, now, as shown in the figure below that the stub AS is now connected also to provider `AS789`. Via which provider will the packets destined to `194.100.10.0/23` will be received by `AS4567` ? Propose a modification to the BGP configuration of `AS123` ?
 .. figure:: fig/BGP-figs-002-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

3 Consider that stub shown in the figure below decides to advertise two `/24` prefixes instead of its allocated `/23` prefix. 

  #. Via which provider does `AS4567` receive the packets destined to `194.100.11.99` and `194.100.10.1` ? 
  #. What happens when link `R1-R3` fails ?
  #. What are the consequences these advertisements on the size of the BGP routing maintained by routers in the global Internet ?
  #. Propose a configuration on `R1` that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS4567` if one of `AS4567`'s interdomain links fails ?

 .. figure:: fig/BGP-figs-003-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

