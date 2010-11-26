Interdomain Routing 
===================


1. Consider the network shown in the figure below and explain the path that will be followed by the packets to reach `194.100.10.0/23`

 .. figure:: fig/BGP-figs-001-c.png
    :align: center
    :scale: 50
   
    A stub connected to one provider

2. Consider, now, as shown in the figure below that the stub AS is now also connected to provider `AS789`. Via which provider will the packets destined to `194.100.10.0/23` will be received by `AS4567` ? Should `AS123` change its configuration ? 

 .. figure:: fig/BGP-figs-002-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers

3. Consider that stub shown in the figure below decides to advertise two `/24` prefixes instead of its allocated `/23` prefix. 

 #. Via which provider does `AS4567` receive the packets destined to `194.100.11.99` and `194.100.10.1` ? 
 #. How is the reachabilty of these addresses affected when link `R1-R3` fails ?
 #. Propose a configuration on `R1` that achieves the same objective as the one shown in the figure but also preserves the reachability of all IP addresses inside `AS4567` if one of `AS4567`'s interdomain links fails ?

 .. figure:: fig/BGP-figs-003-c.png
    :align: center
    :scale: 50
   
    A stub connected to two providers



