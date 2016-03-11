#!/usr/bin/evn python

import sys


if len(sys.argv)  == 2:
	ip_addr = sys.argv.pop()
	print "The IP Address is: %s" % ip_addr
else:
	print "Please provide input after 'python test6.py' such as 'python test.py 10.88.16.0'"