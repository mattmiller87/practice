'''
2. In the following directory there is a file 'ospf_single_interface.txt':

https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/OSPF_DATA

Open this file and extract the interface, IP address, area, type, cost, hello timer, and dead timer.  Use regular expressions to accomplish your extraction.

Your output should look similar to the following:

Int:        GigabitEthernet0/1
IP:        172.16.13.150/29
Area:    30395
Type:    BROADCAST
Cost:    1
Hello:   10
Dead:   40
'''

import re, pprint

with open("ospf_data/ospf_single_interface.txt", "rU") as a_file:
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

order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')
for k in order:
    print "%10s: %-20s" % (k, ospf_dict[k])