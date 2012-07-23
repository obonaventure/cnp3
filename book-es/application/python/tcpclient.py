# simple tcp client - supports v4 and v6

import socket
import os
import sys
import random

MSG="GET / HTTP/1.0\r\n\r\n"

if len(sys.argv) !=3:
    print "Usage : ",sys.argv[0]," host port"

host=sys.argv[1]
port=sys.argv[2]

# Query DNS
try:
    addresses=socket.getaddrinfo(host,port)
    random.shuffle(addresses)
    # (family, socktype, proto, canonname, sockaddr)
    for a in addresses :
        # try first address of list
        try:
            if a[1]==socket.SOCK_STREAM:
                s=socket.socket(a[0],a[1])
                print "connecting to ",a[4]
                s.connect(a[4])
                print "connected to ",a[4]
                s.send(MSG)
                
                MAXLEN = 1024
                data = s.recv(MAXLEN)
                s.close()
                print 'Received :',data
                break
        except socket.error:
            # try next address in list
            pass
        
except socket.gaierror: 
    print "Host ",host," not found :"
            
