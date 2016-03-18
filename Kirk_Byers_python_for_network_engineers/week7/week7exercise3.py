'''
3.  In the following directory there is a file 'ospf_data.txt':

https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/OSPF_DATA

This file contains the output from 'show ip ospf interface'.  Using functions and regular expressions parse this output to display the following (note, I ended up using re.split() as part of the solution to this problem):

Int:     Loopback0
IP:     10.90.3.38/32
Area: 30395
Type: LOOPBACK
Cost: 1

Int:     GigabitEthernet0/1
IP:      172.16.13.150/29
Area:  30395
Type:  BROADCAST
Cost:  1
Hello: 10
Dead: 40

Int:      GigabitEthernet0/0.2561
IP:      10.22.0.117/30
Area:  30395
Type:  POINT_TO_POINT
Cost:  1
Hello: 10
Dead: 40
'''

import re

def tasks():
	a_file = "ospf_data/ospf_data.txt"
	data = extract_ospf_information(a_file)
	print_dictionary(data)

def extract_ospf_information(files):
	with open(files, "rU") as a_file:
		ospf_dict = {}
		for line in a_file:
			interface = re.search(r'^(.+) is up, line protocol is up', line )
			ospf_ip_area = re.search(r"Internet Address (.+)/.+, Area (.+),", line)
			ospf_type_cost = re.search(r'Network Type (.+), Cost: (.+)', line )
			ospf_timers = re.search(r'Timer intervals configured, Hello (.+), Dead (.+?),', line )

			if interface:
				ospf_dict['Int'] = interface.group(1)
			if ospf_ip_area:
				ospf_dict['IP'] = ospf_ip_area.group(1)
				ospf_dict['Area'] = ospf_ip_area.group(2)
			if ospf_type_cost:
				ospf_dict['Type'] = ospf_type_cost.group(1)
				ospf_dict['Cost'] = ospf_type_cost.group(2)
			if ospf_timers:
				ospf_dict['Hello'] = ospf_timers.group(1)
				ospf_dict['Dead'] = ospf_timers.group(2)

		return ospf_dict

def print_dictionary(a_dict):
	order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')
	for k in order:
		print "%10s: %-20s" % (k, a_dict[k])



tasks()
