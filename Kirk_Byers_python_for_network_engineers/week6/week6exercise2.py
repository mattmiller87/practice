'''
2. Write a function that converts a list to a dictionary where the 
index of the list is used as the key to the new dictionary 
(the function should return the new dictionary).

'''

a_list = range(10)

def list_to_dict(a_list):
	a_dict = {}
	i = 1
	for item in a_list:
		if not item in a_dict:
			a_dict[item] = {}
	return a_dict

print list_to_dict(a_list)
