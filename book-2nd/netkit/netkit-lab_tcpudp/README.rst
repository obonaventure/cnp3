============================
Labo 2: Hack on tcp behavior
============================
Rajouter tcptrace dans les modules netkit
------------------------------------------

Situation
---------


In this lab, you will find 2 hosts connected to a router. Behind this router
there is a webserver on a different collision domain than the hosts.
On the webserver, you have files you can download. The router has a fixed
maximum bandwidth of 1 Mb/s.

  .. figure:: webserver.png
     :align: center
     :scale: 100

Instructions
------------

The goal of this lab is to have a better understanding of TCP by modifiyng its
options. You will have to analyse tcpdump traces of your download (man tcpdump) with tcptrace (http://www.tcptrace.org/manual.html)
and makes some conclusion about the value given to some particular options.
tcp is highly modifiable, and as you will see, some change can improve network
performance or lose network performance.

To modify tcp options, use the python script set_tcp_options.py. You can print
the help with the command python set_tcp_options.py -h

Our default options are 

.. code-block:: console

   tcp_adv_win_scale = 0
   tcp_allowed_congestion_control = "reno"
   tcp_dsack = 0
   tcp_ecn = 0
   tcp_fack = 0
   tcp_frt = 0
   tcp_keepalive_time = 7200
   tcp_keepalive_intvl = 15
   tcp_low_latency = 0
   tcp_moderate_rcvbuf = 0
   tcp_mtu_probing = 2
   tcp_no_metrics_save = 1
   tcp_reordering = 3
   tcp_rmem = '4096 4096 4096'
   tcp_sack = 0
   tcp_slow_start_after_idle = 1
   tcp_timestamps = 0
   tcp_window_scaling = 0
   tcp_wmem = '4096 4096 4096'

All others are set to their default value

After that the tcp options have been set as you want, you can start netkit.
Each hosts will be configured as you requested.

Inside netkit, you can use the script "download" located to /root/client_download which will simulate a download of a file from the webserver with lack of performance from the client side.

From any pc, you can do a wget http://webserver/download.php to simulate a
download with lack of performance from the server.



