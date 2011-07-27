# A too simple HTTP server

import socket, sys, time

# Server runs on all IP addresses by default
HOST=''
# 8080 can be used without root priviledges
PORT=8080 
BUFLEN=8192 # buffer size

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
try:
    print "Starting HTTP server on port ", PORT
    s.bind((HOST,PORT,0,0))
except socket.error :
    print "Cannot bind to port :",PORT
    sys.exit(-1)

s.listen(10) # maximum 10 queued connections

while True:
    # a real server would be multithreaded and would catch exceptions
    conn, addr = s.accept()
    print "Connection from ", addr
    data=''
    while not '\n' in data :  # wait until first line has been received
        data = data+conn.recv(BUFLEN) 
    if data.startswith('GET'):
        # GET request
        conn.send('HTTP/1.0 404 Not Found\n')
        # a real server should serve files
    else:
        # other type of HTTP request
        conn.send('HTTP/1.0 501 Not implemented\n')

    now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    conn.send('Date: ' + now +'\n')
    conn.send('Server: Dummy-HTTP-Server\n')
    conn.send('\n')
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
