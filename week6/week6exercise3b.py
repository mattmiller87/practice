'''
3a.Convert the IP address validation code (Class4, exercise1) into a function,
take one variable 'ip_address' and return either True or False
(depending on whether 'ip_address' is a valid IP). Only include IP address
checking in the function--no prompting for input, no printing to standard output.


3b. Import this IP address validation function into the Python interpreter shell 
and test it (use both 'import x' and 'from x import y').

'''

from week6exercise3a import * #import week6exercise3a

def print_ip_addr():
	ip_addr = return_valid_ip(ip_address)
	print "This is a valid ip: %s" %ip_addr

print_ip_addr()


