'''
IV. Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.
    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.

    For output, print the IP and whether it is valid or not.
 '''

 #!/usr/bin/evn python

import sys


if len(sys.argv)  == 2:
	ip_addr = sys.argv.pop()
	#print "The IP Address is: %s" % ip_addr
else:
	print "Error:missing sys.argv ip address,eg('python test.py 10.88.16.0')"



ip_parts = ip_addr.split(".")

ip_fix = ".".join(ip_parts)

while True:
	if len(ip_parts) == 4:
		first_octet_str,second_octet_str,third_octet_str,forth_octet_str = ip_parts
		print first_octet_str + "." + second_octet_str + "." + third_octet_str + "." + forth_octet_str
		if forth_octet_str is None:
			print "Error: Forth Octet not provided."
			break
		else:
			first_octet = int(first_octet_str)
			second_octet = int(second_octet_str)
			third_octet = int(third_octet_str)
			forth_octet = int(forth_octet_str)
			if first_octet > 223:
				print "Error: First Octet must be between 1-223"
			elif first_octet == 127:
				print "Error: First Octet cannot be 127 - reserved for loopback"
			else:
				if (first_octet == 169) and (second_octet == 254):
					print "Error: APIPA address provided"
				elif (first_octet > 255) or (second_octet > 255) or (third_octet > 255) or (forth_octet > 255):
					print "Error: IP address must be between 1-255"
				else:
					print "IP Address: %s is valid." % ip_fix
	else:
		print "Error:missing octet in ip address"
	break





