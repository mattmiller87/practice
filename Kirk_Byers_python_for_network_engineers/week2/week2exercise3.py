'''
III. You have the following four lines from 'show ip bgp':

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

Note, in each case the AS_PATH starts with '701'.

Using split() and a list slice, how could you process each of these such that--for each entry, you return an ip_prefix and the AS_PATH (the ip_prefix should be a string; the AS_PATH should be a list):
Your output should look like this:

ip_prefix             as_path                                           
1.0.192.0/18       ['701', '38040', '9737']                          
1.1.1.0/24           ['701', '1299', '15169']                          
1.1.42.0/24         ['701', '9505', '17408', '2.1465']                
1.0.192.0/19       ['701', '6762', '6762', '6762', '6762', '38040', '9737']

Ideally, your logic should be the same for each entry (I say this because once I teach you for loops, then I want to be able to process all of these in one four loop).

If you can't figure this out using a list slice, you could also solve this using pop().
'''

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
