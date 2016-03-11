'''
II. Create an IP address converter (dotted decimal to binary):

    A. Prompt a user for an IP address in dotted decimal format.

    B. Convert this IP address to binary and display the binary result on the screen (a binary string for each octet).

    Example output:
    first_octet    second_octet     third_octet    fourth_octet
    0b1010        0b1011000        0b1010         0b10011
'''
ip_addr = raw_input("Please enter an IP address: ")

print "The IP Address you entered is: " + ip_addr

ip_parts = ip_addr.split(".")

ip_fix = ".".join(ip_parts)

first_octet_binary = bin(int(ip_parts[0]))
first_octet_hex = hex(int(ip_parts[0]))

second_octet_binary = bin(int(ip_parts[1]))
second_octet_hex = hex(int(ip_parts[1]))

third_octet_binary = bin(int(ip_parts[2]))
third_octet_hex = hex(int(ip_parts[2]))

forth_octet_binary = bin(int(ip_parts[3]))
forth_octet_hex = hex(int(ip_parts[3]))

print "%-20s %-20s %-20s %-20s" % ("FIRST_OCTET_BINARY","SECOND_OCTET_BINARY","THIRD_OCTET_BINARY","FORTH_OCTET_BINARY")
print "%-20s %-20s %-20s %-20s" % (first_octet_binary,second_octet_binary,third_octet_binary,forth_octet_binary)
print "%-20s %-20s %-20s %-20s" % (first_octet_hex,second_octet_hex,third_octet_hex,forth_octet_hex) #not required by exercise