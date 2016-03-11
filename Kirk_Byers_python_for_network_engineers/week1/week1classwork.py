a = 10
b = 20
print a + b

print type(a)

c = u'whatever new'

print type(c)

d = '    whatever    \n'

print d
print d.strip()

e = '192.168.1.10'

print e
print e.split('.')

octets = e.split('.')

print ".".join(octets)

print d.strip.upper