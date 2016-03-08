'''
3a.Convert the IP address validation code (Class4, exercise1) into a function,
take one variable 'ip_address' and return either True or False
(depending on whether 'ip_address' is a valid IP). Only include IP address
checking in the function--no prompting for input, no printing to standard output.


3b. Import this IP address validation function into the Python interpreter shell 
and test it (use both 'import x' and 'from x import y').

'''

ip_address = "10.20.30.10"

def return_valid_ip(ip_addr):

	running = True #variable that can be changed to stop the while loop

	while running:
		ip_parts = ip_addr.split(".")
		valid_ip = True #variable that can be changed to force stay within while loop
		
		#section 1 of while loop - check for 4 octets
		if len(ip_parts) != 4:
			print "Error: Valid IP address with 4 octets not entered"
			continue

		#section 2 of while loop - check for integers in octet positions
		#used next line for find the error exception
		#first_octet_int = int('test')
		#Python returned = ValueError: invalid literal for int() with base 10: 'test'
		for i, octet in enumerate(ip_parts): #iterate through ip_parts list
			try: #is each octet an integer?
				ip_parts[i] = int(octet)
			except ValueError as e:
				print "Error: integer needed at each octet."
				valid_ip = False

		if valid_ip is False:
			continue

		#section 3 of while loop - check to make sure octets form a valid IP Address
		#stole this to save time - mine isn't built the same
		# Check first_octet meets conditions
		first_octet,second_octet,third_octet,fourth_octet = ip_parts
		if (first_octet < 1) or (first_octet > 223):
			print "Error: octet1, if1"
			valid_ip = False
		elif first_octet == 127:
			print "Error: octet1, elif2"
			valid_ip = False

		# Check 169.254.X.X condition
		if first_octet == 169 and second_octet == 254:
			print "Error: APIPA"
			valid_ip = False
			
		# Check 2nd - 4th octets
		for octet in (second_octet, third_octet, fourth_octet):
			if (octet < 0) or (octet > 255):
				print "Error1"
				valid_ip = False
				
		if valid_ip is True:
			running = False
		else:
			print "Error: IP address did not qualify as valid."

	return ip_addr

