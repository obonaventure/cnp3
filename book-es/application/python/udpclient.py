# simple udp client - supports v4 and v6

import socket
import os
import sys

MSG="Simple message"

if len(sys.argv) !=3:
    print "Usage : ",sys.argv[0]," host port"

host=sys.argv[1]
port=sys.argv[2]

# Query DNS
try:
    addresses=socket.getaddrinfo(host,port)

    # (family, socktype, proto, canonname, sockaddr)
    for a in addresses :
        # try first address of list
        try:
            s=socket.socket(a[0],a[1])
            s.connect(a[4])
            s.send(MSG)

            MAXLEN = 1024
            data = s.recv(MAXLEN)
            print 'Received :%d', socket.ntohl((data))

            s.close()

            break
        except socket.error:
            # try next address in list
            pass

except socket.gaierror: 
    print "Host ",host," not found :"
