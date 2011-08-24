#!/usr/bin/python 
# A simple http client that retrieves the first page of a web site

import socket, sys

if len(sys.argv)!=3 and len(sys.argv)!=2:
    print "Usage : ",sys.argv[0]," hostname [port]"

hostname = sys.argv[1]
if len(sys.argv)==3 :
    port=int(sys.argv[2])
else:
    port = 80

READBUF=16384   # size of data read from web server
s=None

for res in socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM): 
    af, socktype, proto, canonname, sa = res
    # create socket
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error:
        s = None
        continue
    # connect to remote host
    try:
        print "Trying "+sa[0]
        s.connect(sa)
    except socket.error, msg:
        # socket failed
        s.close()
        s = None
        continue
    if s :
        print "Connected to "+sa[0]
        s.send('GET / HTTP/1.1\r\nHost:'+hostname+'\r\n\r\n')
        finished=False
        count=0
        while not finished:
            data=s.recv(READBUF)
            count=count+1
            if len(data)!=0:
                print repr(data)
            else:
                finished=True
        s.shutdown(socket.SHUT_WR)        
        s.close()
        print "Data was received in ",count," recv calls"
        break
