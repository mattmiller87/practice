'''
4. Create a function using your dotted decimal to binary conversion code from Class3, exercise1.
 In the function--do not prompt for input and do not print to standard output. 
 The function should take one variable 'ip_address' and should return the IP address in 
 dotted binary format always padded to eight binary digits (for example, 00001010.01011000.00010001.00010111). 
 You might want to create other functions as well (for example, the zero-padding to eight binary digits).
'''

#!/usr/bin/evn python

import sys


if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    print "The IP Address is you entered is: %s" % ip_addr
else:
    print "Please provide input after 'python test6.py' such as 'python test.py 10.88.16.0'"

def task():
	a = reconstruct_binary_as_address(break_down_ip_parts(ip_addr))
	print "%-20s %-20s" % ("IP Address","Binary") #table headers
	print "%-20s %-20s" % (ip_addr,a) #table content

def break_down_ip_parts(ip_addr):
	ip_parts = ip_addr.split(".")
	binary_parts = []
	for decimal in ip_parts:
		binary = decimal_to_binary(decimal)
		binary_parts.append(binary)
	return binary_parts

def decimal_to_binary(decimal):
	binary = bin(int(decimal))
	binary_padded = str(binary).zfill(8)
	return binary_padded

def reconstruct_binary_as_address(binary_list):
	first_octet_binary = binary_list[0]
	second_octet_binary = binary_list[1]
	third_octet_binary = binary_list[2]
	fourth_octet_binary = binary_list[3]
	return "%s.%s.%s.%s" %(first_octet_binary,second_octet_binary,third_octet_binary,fourth_octet_binary)


task()









