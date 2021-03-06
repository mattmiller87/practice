#!/usr/bin/env python
'''
Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note).
Python for Network Engineers
https://pynet.twb-tech.com
Learning Python
Create a second program that expands upon the program from Exercise I.
This program will keep track of which network devices are
physically adjacent to each other (physically connected to each
other).
You will accomplish this by adding a new field (adjacent_devices)
to your network_devices inner dictionary.  adjacent_devices will be a
list of hostnames that a given network device is physically
connected to.
For example, the dictionary entries for 'R1' and 'SW1' should look
as follows:
'R1': {'IP': '10.1.1.1',
		'adjacent_devices': ['SW1'],
		'device_type': 'Router',
		'model': '881',
		'vendor': 'Cisco'},
'SW1': {'IP': '10.1.1.22',
		 'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5'],
		 'device_type': 'Switch',
		 'model': 'WS-C2950-24',
		 'vendor': 'cisco'},
For output, print network_devices to standard output.
'''
import re
import pprint
from week5exercise_data import *

# run pull_cdp_information_into_dict and then print that using to_screen
def task_1():
	dictionary1 = pull_cdp_information_into_dict(cdp_neighbors_detail_list())
	dictionary2 = do_next_thing(cdp_neighbors_list())
	#to_screen(dictionary2)
	data = merge_nested_dictionaries(dictionary1,dictionary2)
	to_screen(data)

#this function prints anything to screen
def to_screen(data):
	pprint.pprint(data)

#provide this function with nested dictionaries where the first level dictionary keys might match but the second level key,value pair needs to be added to the first dictionary or new records need to be created
#{'R1': {'device_type': 'Router','ip': '10.1.1.1','model': '881','vendor': 'Cisco'},
# 'R2': {'device_type': 'Router','ip': '10.1.1.2','model': '881','vendor': 'Cisco'},
# 'SW1': {'device_type': 'Switch','ip': '10.1.1.22','model': 'WS-C2950-24','vendor': 'cisco'}}
#{'R1': {'adjacent_devices': ['SW1']},
# 'R2': {'adjacent_devices': ['SW1']},
# 'R3': {'adjacent_devices': ['SW1']},
# 'SW1': {'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5']}}
#return is single dictionary with all second level dictionary key,value pairs
#{'R1': {'adjacent_devices': ['SW1'],'device_type': 'Router','ip': '10.1.1.1','model': '881','vendor': 'Cisco'},
# 'R2': {'adjacent_devices': ['SW1'],'device_type': 'Router','ip': '10.1.1.2','model': '881','vendor': 'Cisco'},
# 'R3': {'adjacent_devices': ['SW1']},
# 'SW1': {'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5'],'device_type': 'Switch','ip': '10.1.1.22','model': 'WS-C2950-24','vendor': 'cisco'}}
def merge_nested_dictionaries(dictionary1,dictionary2):
	dict = {}
	for key,value in dictionary1.items(): #sort through dictionary1 keys
		dict[key] = value #keep dictionary1 key,value pairs
		if key in dictionary2.keys(): #if key in dictionary1 matches keys from dictionary2
			for dict2key,dict2vlaue in dictionary2.items(): #sort through records in dictionary2
				if key == dict2key: #if the keys are the same
					for k,v in dict2vlaue.items(): #sort through the second level dictionary in dictionary2
						dict[key][k] = v #adds dictionary2's key,value pairs to existing key from dictionary1
	for key,value in dictionary2.items(): #sort through dictionary2 keys
		if key not in dictionary1.keys(): #if keys in dictionary2 do not match keys from dictionary1
			dict[key] = value #create a new record using dictionary2's key
	return dict

def cdp_neighbors_list():
	#combine the show cdp neighbors into 1 list
	cdp_neighbors = (
		sw1_show_cdp_neighbors,
		r1_show_cdp_neighbors,
		r2_show_cdp_neighbors,
		r3_show_cdp_neighbors,
		r4_show_cdp_neighbors,
		r5_show_cdp_neighbors,
		r6_show_cdp_neighbors,
		)
	return cdp_neighbors

def do_next_thing(info):
	network_devices = {} #make a blank dict

	for data in info:
		data_split = data.split("\n")
		hostname = ""

		for line in data_split:
			if ">" in line:
				line_split = line.split(">")
				(hostname,junk) = line_split

				if not hostname in network_devices:
					network_devices[hostname] = {}

		(junk,content_messy) = data.split("Port ID")
		content_messy_join = "".join(content_messy)
		content_table = content_messy_join.strip()
		content_table_list = content_table.split("\n")

		network_devices[hostname] = {}
		list = []
		
		for line in content_table_list:
			clean_cdp = list_to_dynamic_dict(format_whitespace_column_data(line))
			list.append(clean_cdp)
		
		adjacent_devices_list = []
		for item in list:
			adjacent_devices_list.append(item[1])
		
		network_devices[hostname]['adjacent_devices'] = adjacent_devices_list

	return network_devices

def cdp_neighbors_detail_list():
	#combine the show cdp neighbors detail into 1 list
	cdp_neighbors_details = (
		sw1_show_cdp_neighbors_detail,
		r1_show_cdp_neighbors_detail,
		r2_show_cdp_neighbors_detail,
		r3_show_cdp_neighbors_detail,
		r4_show_cdp_neighbors_detail,
		r5_show_cdp_neighbors_detail,
		)
	return cdp_neighbors_details

#basically stole this from solution
def pull_cdp_information_into_dict(info):
	network_devices = {} #make a blank dict

	for data in info:
		data_split = data.split("\n")

		hostname = "" #set hostname to blank for this loop
		
		for line in data_split:
			if "----------------" in line:
				hostname = "" #set hostname to blank after dashes

			if "Device ID: " in line: #find hostname
				line_split = line.split('Device ID: ')
				(junk,hostname) = line_split

				if not hostname in network_devices: #if hostname is not network_devices dict, add new key and value for hostanme
					network_devices[hostname] = {}

			if "IP address: " in line: #find ip address
				line_split = line.split('IP address: ')
				(junk,ip_addr) = line_split

				if hostname: #if hostname in network_devices dict, add new key and value for ip address
					network_devices[hostname]['ip'] = ip_addr

			if "Platform: " in line: #find model
				line_split = line.split(',')
				(platform_messy, capabilities_messy) = line_split
				#in platform, find vendor and model
				(junk, model_vendor) = platform_messy.split('Platform: ')
				(vendor, model) = model_vendor.split()

				capabilities_split = capabilities_messy.split('Capabilities: ')
				(junk, capabilities) = capabilities_split
				if "Router" in capabilities:
					device_type = "Router"
				elif "Switch" in capabilities:
					device_type = "Switch"
				else:
					device_type = "Not Listed"

				if hostname: #if hostname in network_devices dict, add new keys and values for vendor, model, device type
					network_devices[hostname]['vendor'] = vendor
					network_devices[hostname]['model'] = model
					network_devices[hostname]['device_type'] = device_type
	return network_devices


#present this function with a whitespaced columned mass of data
#this function will return a list[item1,item2, ... ]
def format_whitespace_column_data(data):
	data_lines = data.split("\n") #
	content = [] #create a blank list
	for line in data_lines:
		replace_space_with_comma = re.sub(r'  +', ",", line) #replace 2 spaces or more with comma
		split_line = replace_space_with_comma.split(",") #create the content for the list
		content.append(split_line) #add the content to the blank list
	return content

#present this function with a list[item1,item2, ... ] of data
#this function will give back a dict{1: item1, 2: item2, ... }
def list_to_dynamic_dict(list):
	for element in list:
		dict = {} #create a blank dictionary
		i = 1 #start the dictionary count at 1
		for item in element[:]: #iterate through the list pulling out each item one by one
			dict[i] = item #associate the item with the key "i"
			i += 1 #add 1 to i to make the next key 2, for the next item
		return dict

task_1()