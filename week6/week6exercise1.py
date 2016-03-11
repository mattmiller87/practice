'''
1. Create a function that returns the multiplication product of three parameters
	--x, y, and z. z should have a default value of 1.
    a. Call the function with all positional arguments.
    b. Call the function with all named arguments.  
    c. Call the function with a mix of positional and named arguments.
    d. Call the function with only two arguments and use the default value for z.
'''

def multiplication_function(x,y,z=1):
	return x*y*z

a = multiplication_function(2,3,4)
b = multiplication_function(x=2,y=4,z=5)
c = multiplication_function(3,y=4,z=5)
d = multiplication_function(10,20)

print "This is the answer for a: %s" %a
print "This is the answer for b: %s" %b
print "This is the answer for c: %s" %c
print "This is the answer for d: %s" %d