BGP 
===


1. In the network shown below, draw the iBGP and eBGP sessions that must be established among the routers.

 .. figure:: ../S9/fig/BGP-figs-007-c.png
    :align: center
    :scale: 70
   
    A small domain

2. Consider the network shown below. Assume that `R3` and `R5` use the `MED` attribute when advertising a route towards `R1` and `R2`. The `MED` attribute that they advertise is the IGP cost to their nexthop.

 .. figure:: ../S9/fig/BGP-figs-005-c.png
    :align: center
    :scale: 70
   
    A small internetwork

 #. Consider that `R5` is attached to prefix `p1` and advertises this prefix. What are the routes received and chosen by `R1` and `R2` ?
 #. Consider that `R9` is attached to prefix `p2` and advertises this prefix. What are the routes received and chosen by `R1` and `R2` ?
 #. Consider that `R6` is attached to prefix `p3` and advertises this prefix. What are the paths received and chosen by `R1` and `R2` ?

3. Consider the network shown below. In this network, `RA` advertises prefix `p`. Shown the iBGP sessions in this network and all the BGP messages that are exchanged when :

 .. figure:: ../S9/fig/BGP-figs-006-c.png
    :align: center
    :scale: 70
   
    A small internetwork

 - `RA` advertises `p` first on link `RA-R1` and later on link `RA-R3`
 - Link `RA-R3` fails
 - Perform the same analysis again by considering now that `R3` inserts a `local-pref` value of `100` in the routes received from `RA` while `R1` inserts a `local-pref` value of `50`.

4. Consider now the network shown below where the link costs are specified. Compute the routing tables on all routers when :

 - prefix `p1` is advertised by `RA`, `RB` and `RC` with an AS Path of length 1
 - prefix `p2` is advertised by `RA` with an AS Path length of 2 and by `RB` and `RC` with an AS Path of length 1
 - What happens in these two situations when the link `R3-R5` fails ?

 .. figure:: ../S9/fig/BGP-figs-008-c.png
    :align: center
    :scale: 70
  
    A small internetwork

5. There are currently 13 IPv4 addresses that are associated to the root servers of the Domain Name System. However, http://www.root-servers.org/ indicates that there are more than 100 different physical servers that support. This is a large anycast service. How would you configure BGP routers to provide such anycast service ?

6. Consider the network shown in the figure below. In this network, `R0` advertises prefix `p` and all link metrics are set to `1`

 - Draw the iBGP and eBGP sessions
 - Assume that session `R0-R8` is down when `R0` advertises `p` over `R0-R7`. What are the BGP messages exchanged and the routes chosen by each router in the network ?
 - Session `R0-R8` is established and `R0` advertises prefix `p` over this session as well
 - Do the routes selected by each router change if the `MED` attribute is used on the `R7-R6` and `R3-R10` sessions, but not on the `R4-R9` and `R6-R8` sessions ?
 - Is it possible to configure the routers in the `R1 - R6` network such that `R4` reaches prefix `p` via `R6-R8` while `R2`uses the `R3-R10` link ?

 .. figure:: ../S11/fig/revision-figs-003-c.png
    :align: center
    :scale: 30 

    A simple Internet

7. The `MED` attribute is often set at the IGP cost to reach the BGP nexthop of the advertised prefix. However, routers can also be configured to always use the same `MED` values for all routes advertised over a given session. How would you use it in the figure above so that link `R10-R3` is the primary link while `R7-R6` is a backup link ? Is there an advantage or drawback of using the `MED` attribute for this application compared to `local-pref` ?

8. In the figure above, assume that the managers of `R8` and `R9` would like to use the `R8-R6` link as a backup link, but the managers of `R4` and `R6` do no agree to use the `MED` attribute nor to use a different `local-pref` for the routes learned from 
