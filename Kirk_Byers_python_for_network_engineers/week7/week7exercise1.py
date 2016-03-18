'''
1. In the following directory there are six CDP files: 
  https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/CDP_DATA

   a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.

   b. Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote hostnames, remote IP addresses, and remote platforms.  Your output should look similar to the following:

   remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
                    IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
            platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']
'''
import re


with open("cdp_data/r1_cdp.txt", "rU") as a_file:
	hostname_list = []
	ip_list = []
	model_list = []
	vendor_list = []
	device_type_list = []
	for line in a_file:
		remote_hostname = re.findall(r'Device ID: (\w+)', line )
		remote_ip = re.findall(r'IP address: (.+)', line )
		remote_platform = re.search(r'Platform: (.+) (.+),', line )
		remote_capabilities = re.search(r'Capabilities: (.+) ', line )
		if remote_hostname:
			hostname_list.append(remote_hostname)
		if remote_ip:
			ip_list.append(remote_ip)
		if remote_platform:
			model_list.append(remote_platform.group(2))
			vendor_list.append(remote_platform.group(1))
		if remote_capabilities:
			if "Router" in remote_capabilities.group(1):
				device_type_list.append("Router")
			elif "Switch" in remote_capabilities.group(1):
				device_type_list.append("Switch")
	#print hostname_list
	#print ip_list
	#print model_list
	#print vendor_list
	#print device_type_list


with open("cdp_data/sw1_cdp.txt", "rU") as a_file:
	hostname_list = []
	ip_list = []
	vendor_model_list = []
	for line in a_file:
		remote_hostname = re.findall(r'Device ID: (\w+)', line )
		remote_ip = re.findall(r'IP address: (.+)', line )
		remote_platform = re.search(r'Platform: (.+) (.+),', line )
		remote_capabilities = re.search(r'Capabilities: (.+) ', line )
		if remote_hostname:
			hostname_list.append(remote_hostname)
		if remote_ip:
			ip_list.append(remote_ip)
		if remote_platform:
			vendor_model_list.append(remote_platform.group(1) + " " + remote_platform.group(2))
		if remote_capabilities:
			if "Router" in remote_capabilities.group(1):
				device_type_list.append("Router")
			elif "Switch" in remote_capabilities.group(1):
				device_type_list.append("Switch")
	print hostname_list
	print ip_list
	print vendor_model_list
