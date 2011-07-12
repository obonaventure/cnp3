
import socket
import sys
HOSTNAME=sys.argv[1]
PORT=int(sys.argv[2])
MSG="Hello, World!"
for a in socket.getaddrinfo(HOSTNAME, PORT, socket.AF_UNSPEC,socket.SOCK_DGRAM,0, socket.AI_PASSIVE) :
    address_family,sock_type,protocol,canonicalname, sockaddr=a
    try:
        s = socket.socket( address_family, sock_type ) 
    except socket.error:
        s= None
        print "Could not create socket"
        continue
    if s is not None:
        s.sendto( MSG, sockaddr)
        break
