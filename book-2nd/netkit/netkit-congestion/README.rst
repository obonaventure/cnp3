============================
Labo 2: Hack on tcp behavior
============================

Instructions
------------

The goal of this lab is to have a better understanding of TCP by modifiyng its
options. You will have to analyse tcpdump traces of your download (man tcpdump) with tcptrace (http://www.tcptrace.org/manual.html)
and makes some conclusion about the value given to some particular options.
tcp is highly modifiable, and as you will see, some change can improve network
performance or lose network performance.


Our default options are 
.. code-block::

  sysctl -w net.ipv4.tcp_wmem='65536 65536 65536' 
  sysctl -w net.ipv4.tcp_rmem='65536 65536 65536' 
  sysctl -w net.ipv4.tcp_no_metrics_save=1 
  sysctl -w net.ipv4.tcp_slow_start_after_idle=1 
  sysctl -w net.ipv4.tcp_ecn=0 
  sysctl -w net.ipv4.tcp_keepalive_time=7200 
  sysctl -w net.ipv4.tcp_moderate_rcvbuf=0 
  sysctl -w net.ipv4.tcp_timestamps=0 
  sysctl -w net.ipv4.tcp_keepalive_intvl=15 
  sysctl -w net.ipv4.tcp_dsack=0 
  sysctl -w net.ipv4.tcp_frto=0 
  sysctl -w net.ipv4.tcp_adv_win_scale=0 
  sysctl -w net.ipv4.tcp_reordering=3 
  sysctl -w net.ipv4.tcp_window_scaling=0 
  sysctl -w net.ipv4.tcp_low_latency=0 
  sysctl -w net.ipv4.tcp_mtu_probing=2 
  sysctl -w net.ipv4.tcp_sack=0 
  sysctl -w net.ipv4.tcp_allowed_congestion_control=reno 
  sysctl -w net.ipv4.tcp_fack=0 

All others are set to their default value

After that the tcp options have been set as you want, you can start netkit. Each hosts will be configured as you requested.

Inside netkit, you can use the script "download" located to /root/client_download which will simulate a download of a file from the webserver with lack of performance from the client side.

From any pc, you can do a wget http://webserver/download.php to simulate a
download with lack of performance from the server.



