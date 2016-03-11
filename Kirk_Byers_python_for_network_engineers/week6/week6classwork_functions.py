def hello_world():
	'''
	This is a docstring for hello wolrd
	it takes no variables
	and returns True
	'''
	print "hello world"
	print "world"
	return True

#hello_world()

#help(hello_world)
x = 10
y = 20
z = 30


def simple_funct():
	x = 100
	y = 200

	print x
	print y
	print z # first looks in local namespace (within function), when not found, then looks in global namespace (outside the function)

#simple_funct()


def simple_func():

	def simple_func2():
		x = 1000

		print x
		print y
		print z

	x = 100
	y = 200

	print x
	print y
	print z

	simple_func2()

#simple_func()

def a_sum(a_list):
	a_list.append("whatever")


a = range(10)

a_sum(a)

print a
