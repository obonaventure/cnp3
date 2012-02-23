#!/usr/bin/python 
# A simple http client that retrieves the first page of a web site, using
# the standard httplib library

import httplib, sys

if len(sys.argv)!=3 and len(sys.argv)!=2:
 print "Usage : ",sys.argv[0]," hostname [port]"
 sys.exit(1)
 
path = '/'
hostname = sys.argv[1]
if len(sys.argv)==3 :
 port = int(sys.argv[2])
else:
 port = 80

conn = httplib.HTTPConnection(hostname, port)
conn.request("GET", path)
r = conn.getresponse()
print "Response is %i (%s)" % (r.status, r.reason)
print r.read()
