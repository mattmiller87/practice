'''
I. Create an IP address converter (dotted decimal to binary).  This will be similar to what we did in class2 except:

    A. Make the IP address a command-line argument instead of prompting the user for it.
        ./binary_converter.py 10.88.17.23

    B. Simplify the script logic by using the flow-control statements that we learned in this class.

    C. Zero-pad the digits such that the binary output is always 8-binary digits long.  Strip off the leading '0b' characters.  For example,

        OLD:     0b1010
        NEW:    00001010

    D. Print to standard output using a dotted binary format.  For example,

        IP address          Binary
      10.88.17.23        00001010.01011000.00010001.00010111


    Note, you might need to use a 'while' loop and a 'break' statement for part C.

        while True:
            ...
            break       # on some condition (exit the while loop)

    Python will execute this loop again and again until the 'break' is encountered. 
'''

#!/usr/bin/evn python

import sys


if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    print "The IP Address is: %s" % ip_addr
else:
    print "Please provide input after 'python test6.py' such as 'python test.py 10.88.16.0'"


ip_parts = ip_addr.split(".")

ip_fix = ".".join(ip_parts)

first_octet_binary = bin(int(ip_parts[0]))
first_octet_binary_strip = str(first_octet_binary[2:]).zfill(8)

second_octet_binary = bin(int(ip_parts[1]))
second_octet_binary_strip = str(second_octet_binary[2:]).zfill(8)

third_octet_binary = bin(int(ip_parts[2]))
third_octet_binary_strip = str(third_octet_binary[2:]).zfill(8)

forth_octet_binary = bin(int(ip_parts[3]))
forth_octet_binary_strip = str(forth_octet_binary[2:]).zfill(8)

reconstruct_binary_as_address = first_octet_binary_strip + "." + second_octet_binary_strip + "." + third_octet_binary_strip + "." + forth_octet_binary_strip

print "%-20s %-20s" % ("IP Address","Binary") #table headers
print "%-20s %-20s" % (ip_addr,reconstruct_binary_as_address) #table content
