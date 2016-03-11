'''
III. You have the following 'show ip int brief' output.

show_ip_int_brief = 
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up


From this output, create a list where each element in the list is a tuple consisting of (interface_name, ip_address, status, protocol).  Only include interfaces that are in the up/up state.

Print this list to standard output.
'''

import re

from collections import defaultdict

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

print "%-20s %-20s %-20s %-20s" % ("Interface","IP Address","Status","Protocol") #table header printed


def print_up_interfaces(output): #
	for data in output:
		if len(data) == 6:
			if (data[5] == "up") and (data[6] == "up"): #only display up/up interfaces
				print "%-20s %-20s %-20s %-20s" % (data[1],data[2],data[5],data[6])

def format_show_ip_int_brief(show_ip_int_brief):
	show_ip_int_brief_lines = show_ip_int_brief.split("\n")
	data = [] #create a blank list
	for line in show_ip_int_brief_lines:
		entry_comma = re.sub(r'  +', ",", line) #replace 2 spaces or more with comma
		split_entry = entry_comma.split(",") #create list
		data.append(split_entry) #add each line to the blank list
	sorted_data = change_list_to_dict(data) #hand change_list_to_dict the list "data", take the output and call it "sorted_data"
	return print_up_interfaces(sorted_data) #hand print_up_interfaces sorted_data

#present this function with a list[item1,item2, ... ] of data
#this function will give back a dict{1: item1, 2: item2, ... }
def change_list_to_dict(list):
	content = [] #create a blank list
	for element in list:
		dict = {} #create a blank dictionary
		i = 1 #start the dictionary count at 1
		for item in element[:]: #iterate through the list pulling out each item one by one
			dict[i] = item #associate the item with the key "i"
			i += 1 #add 1 to i to make the next key 2, for the next item
		content.append(dict) #add each line(dictionary once built) to the blank list
	return content

format_show_ip_int_brief(show_ip_int_brief)
