
# This file is used to create topologies for the webserver lab.
#
#


import os
import sys
import getopt

def configure(onHosts):
    for host in onHosts:
        if host == "r":
	    create_router()
	elif host == "client1":
	    create_client1()
	elif host == "client2":
	    create_client2()
	elif host == "server":
	    create_webserver()
	

def create_router():
    f=open('r.startup','w')
    f.write('ifconfig eth0 up \nifconfig eth0 add 2001:db8:0b0:15:da:b055::1/96\nifconfig eth1 up\nifconfig eth1 add 2001:db8:be:600d::1/64 \nsysctl -w net.ipv6.conf.all.forwarding=1\ninsmod sch_htb\ntc qdisc del dev eth0\ntc qdisc add dev eth0 root handle 1: htb default 1 \ntc class add dev eth0 parent 1: classid 1:1 htb rate 1000kbit\n')
    f.close()

def create_webserver():
    f=open('server.startup','w')
    f.write('ifconfig eth0 up\nifconfig eth0 add 2001:db8:be:600d::2/64\n/etc/init.d/apache2 start\nroute -A inet6 add default gw 2001:DB8:be:600d::1\n')
    #create files on the webserver
    f.write('dd if=/dev/zero of=/var/www/1Mo.zero bs=1K count=1000\n')
    f.write('dd if=/dev/zero of=/var/www/10Mo.zero bs=1K count=10000\n')
    f.write('dd if=/dev/zero of=/var/www/100Mo.zero bs=1K count=100000\n')
    f.close()

def create_client2():
    f=open('client2.startup','w')
    f.write('ifconfig eth0 up\nifconfig eth0 add 2001:db8:0b0:15:da:b055::3/96\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1\n')
    f.write('echo "2001:db8:be:600d::2 webserver" > /etc/hosts\n')
    f.close()

def create_client1():
    f=open('client1.startup','w')
    f.write('ifconfig eth0 up\nifconfig eth0 add 2001:db8:0b0:15:da:b055::2/96 \nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1\n')
    f.write('echo "2001:db8:be:600d::2 webserver" > /etc/hosts\n')
    f.close()

def create_conf():
    f=open('lab.conf','w')
    f.write('LAB_DESCRIPTION="A lab showing problems that can occurs when using tcp protocol to download files on a webserver"\n LAB_VERSION=1\n LAB_AUTHOR="O. Bonaventure, J. Vellemans, F. Rochet"')
    f.write('client1[0]=A\nClient2[0]=A\nr[0]=A\nr[1]=B\nserver[0]=B')
    f.close()

#main function
def main(argv):
    create_conf()
    configure(["r", "server", "client1", "client2"])
    
if __name__=="__main__":
    main(sys.argv[1:])
