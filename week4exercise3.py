'''
III. Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name as the key.

During this conversion process, you will have to convert strings to integers.  For these string to integer conversions use try/except to catch any string to integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.
'''

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

#from before
import re

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

list_of_entries = [entry1, entry2, entry3, entry4]

print "%-20s %-20s" % ("IP PREFIX","AS PATH") #table header printed

for item in list_of_entries: #loop through list_of_entries
	entry_comma = re.sub(r'  +', ",", item) #replace 2 spaces or more with comma
	split_entry = entry_comma.split(",")
	dict = {
		'star': split_entry[0], #[0] = *
		'ip_prefix': split_entry[1], #[1] = 1.0.192.0/18
		'next_hop': split_entry[2], #[2] = 157.130.10.233
		'as_path': split_entry[3] #[3] = 0 701 9505 17408 2.1465 i
	}
	print "%-20s %-20s" % (dict['ip_prefix'],dict['as_path']) #table information printed