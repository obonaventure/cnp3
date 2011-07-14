import socket
import sys
HOSTIP=sys.argv[1]
PORT=int(sys.argv[2])
MSG="Hello, World!"
s = socket.socket( socket.AF_INET6, socket.SOCK_DGRAM ) 
s.sendto( MSG, (HOSTIP, PORT,0,0) )
