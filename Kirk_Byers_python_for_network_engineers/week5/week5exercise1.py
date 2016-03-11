'''
1. Parse the CDP data (see link above) to obtain the following information: hostname, ip, model, vendor, and device_type (device_type will be either 'router', 'switch', or 'unknown').

From this data create a dictionary of all the network devices.

The network_devices dictionary should have the following format:

network_devices = {
	 'SW1': { 'ip': '10.1.1.22', 'model': 'WS-C2950-24', 'vendor': 'cisco', 'device_type': 'switch' },
	 'R1': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
	  ...
	 'R5': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
 }

Note, this data structure is a dictionary that contains additional dictionaries.  The key to the outer dictionary is a hostname and the data corresponding to this key is another dictionary.  For example, for 'R1':

>>> network_devices['R1']
{'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router'}

You can access a given attribute in the inner dictionary as follows:
>>> a_dict['R1']['ip']
'10.1.1.1'


If this is confusing, you might want to experiment with it in the Python shell:

##### Python Shell - experimenting with dictionary of dictionaries #####

# Initialize network_devices to be a blank dictionary
>>> network_devices = {}

# Assign the key 'R1' to network_devices using a value of a blank dictionary (in other words, I am adding a key:value pair to network_devices where the key is 'R1' and the value is {} )
>>> network_devices['R1'] = {}

# Look at network_devices at this point
>>> network_devices
{'R1': {}}

# Add the 'ip' and 'vendor' fields to the inner dictionary
>>> network_devices['R1']['ip'] = '10.1.1.1'
>>> network_devices['R1']['vendor'] = 'Cisco'
>>> network_devices
{'R1': {'ip': '10.1.1.1', 'vendor': 'Cisco'}}

##### Python Shell - experimenting end #####


For the output to this exercise, print network_devices to standard output.  Your output should look similar to the following (six network devices with their associated attributes).  

{'R1': {'device_type': 'Router',
		'ip': '10.1.1.1',
		'model': '881',
		'vendor': 'Cisco'},
 'R2': {'device_type': 'Router',
		'ip': '10.1.1.2',
		'model': '881',
		'vendor': 'Cisco'},
 'R3': {'device_type': 'Router',
		'ip': '10.1.1.3',
		'model': '881',
		'vendor': 'Cisco'},
 'R4': {'device_type': 'Router',
		'ip': '10.1.1.4',
		'model': '881',
		'vendor': 'Cisco'},
 'R5': {'device_type': 'Router',
		'ip': '10.1.1.5',
		'model': '881',
		'vendor': 'Cisco'},
 'SW1': {'device_type': 'Switch',
		 'ip': '10.1.1.22',
		 'model': 'WS-C2950-24',
		 'vendor': 'cisco'}}
'''
#import the variables from week5exercise_data.py
#sw1_show_cdp_neighbors sw1_show_cdp_neighbors_detail
#r1_show_cdp_neighbors  r1_show_cdp_neighbors_detail
#r2_show_cdp_neighbors  r2_show_cdp_neighbors_detail
#r3_show_cdp_neighbors  r3_show_cdp_neighbors_detail
#r4_show_cdp_neighbors  r4_show_cdp_neighbors_detail
#r5_show_cdp_neighbors  r5_show_cdp_neighbors_detail

import pprint
from week5exercise_data import *

# run pull_cdp_information_into_dict and then print that using to_screen
def task_1():
	data = pull_cdp_information_into_dict()
	to_screen(data)


#this function prints anything to screen
def to_screen(data):
	pprint.pprint(data)


def pull_cdp_information_into_dict():
	#combine the show cdp neighbors detail into 1 list
	cdp_neighbors_details = (
		sw1_show_cdp_neighbors_detail,
		r1_show_cdp_neighbors_detail,
		r2_show_cdp_neighbors_detail,
		r3_show_cdp_neighbors_detail,
		r4_show_cdp_neighbors_detail,
		r5_show_cdp_neighbors_detail,
	)


	network_devices = {} #make a blank dict

	for data in cdp_neighbors_details:
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

task_1()