import socket, sys

HOST_IP=sys.argv[1]   
HOST_PORT=int(sys.argv[2])
BUFF_LEN=8192

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # UDP
s.bind( (HOST_IP,HOST_PORT) )

while True:
    data, addr = s.recvfrom( BUFF_LEN ) # buffer size is 1024 bytes
    print "received message:", data
