'''
5. Write a program that prompts a user for an IP address, then checks if the IP address is valid,
 and then converts the IP address to binary (dotted decimal format). 
 Re-use the functions created in exercises 3 and 4 ('import' the functions into your new program).

'''

#!/usr/bin/evn python

import sys
from week6exercise3a import *
from week6exercise4 import *


def run_programs():
	return_valid_ip(ip_addr)
	binary = reconstruct_binary_as_address(break_down_ip_parts(ip_addr))
	if binary:
		print binary
	else:
		print "Something Went Wrong"

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    run_programs()
else:
    print "Please provide input after 'python test6.py' such as 'python test.py 10.88.16.0'"

