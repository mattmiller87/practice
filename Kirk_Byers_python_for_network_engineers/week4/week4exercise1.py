'''
I. Prompt a user to input an IP address.  Re-using some of the code from class3, exercise4--determine if the IP address is valid.  Continue prompting the user to re-input an IP address until a valid IP address is input.

'''

running = True #variable that can be changed to stop the while loop

while running:
	ip_addr = raw_input("Please enter an IP address: ")
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

print "\nPass: The is address: %s is valid." % ip_addr