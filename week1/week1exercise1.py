#Section 1. Use the split method to divide the following IPv6 address into groups of 4 hex digits (i.e. split on the ":")
a = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"

b = a.split(":")

print b

#Section 2. Use the join method to reunite your split IPv6 address back to its original value.
c = ":".join(b)

print c

#Section 3. In the test3.py script above, how would you modify this to remove the trailing newline on the end of 192.168.1.1? 
d = "192.168.1.1\n"

print d.strip()