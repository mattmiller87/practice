#!/usr/bin/env python


#while loops
'''
i = 0
while True:
	if i >= 11:
		break
	print i
	print "hello"
	i += 1
'''

#building and using dicitonaries
#normal variables, vs dictionary
'''
name = sf-rtr-1
ip_addr = 1.1.1.1
serial_number = FTX000001
os_version = 12.4.22T
'''
#becomes


a = {
	'name': 'sf-rtr-1',
	'ip_addr': '1.1.1.1',
	'serial_number': 'FTX000001',
	'os_version': '12.4.22T',
}

print a

a['name'] = 'la-rtr-1' #changes name
a['model'] = '1941' #adds new key

print a

print a.get('name')

print 'model' in a

print a.keys() #returns keys
print a.values() #returns values

for key in a.keys():
	print key

for value in a.values():
	print value

import pprint

pprint.pprint(a.items())

for k,v in a.items(): #for key, value in key-value item pair
	print k + ": " + v

#exceptions
b = {}
c = []
print 'hello'

b['name'] = 'whatever'

try:
	print 'string2'
	print b['name']
	print c[0]
	print 'string3'
except KeyError as e:
	print 'There was a key exception'
except IndexError as e:
	print str(e)
	print 'There was an index exception'
print 'string4'