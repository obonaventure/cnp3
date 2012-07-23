#!/usr/bin/python 
# A simple http client that retrieves the first page of a web site, using
# the standard urllib2 library

import urllib2, sys

if len(sys.argv)!=2:
 print "Usage : ",sys.argv[0]," url"
 sys.exit(1)

url = sys.argv[1]
conn = urllib2.urlopen(url)
print conn.read()
