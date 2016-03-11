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
	for dict in output:
		if (dict['data5'] == "up") and (dict['data6'] == "up"): #only display up/up interfaces
			print "%-20s %-20s %-20s %-20s" % (dict['data1'],dict['data2'],dict['data5'],dict['data6'])

def format_show_ip_int_brief(show_ip_int_brief):
	show_ip_int_brief_lines = show_ip_int_brief.split("\n")
	data = [] #create a blank list
	for line in show_ip_int_brief_lines:
		entry_comma = re.sub(r'  +', ",", line) #replace 2 spaces or more with comma
		split_entry = entry_comma.split(",") #create list
		data.append(split_entry) #add each line to the blank list
	sorted_data = read_text_with_6_columns(data)
	return print_up_interfaces(sorted_data) #hand print_up_interfaces sorted_data

def read_text_with_6_columns(data):
	content = [] #create a blank list
	for element in data:
		if len(element) == 6: #match only items with 6 columns
			column1,column2,column3,column4,column5,column6 = element #label the columns
			dict = { #give each column an arbitrary key, but mandatory order to keys
				'data1': column1,
				'data2': column2,
				'data3': column3,
				'data4': column4,
				'data5': column5,
				'data6': column6,
			}
			print dict
			content.append(dict) #add each line(dictionary once built) to the blank list
	return content

format_show_ip_int_brief(show_ip_int_brief)
