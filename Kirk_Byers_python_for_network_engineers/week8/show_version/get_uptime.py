#twb-sf-881 uptime is 12 weeks, 5 days, 1 hour, 4 minutes

import re

def obtain_uptime(data):
	uptime_line = re.search(r".*uptime is (.+)", data) #match a line contains uptime is, create a group on the uptime
	if uptime_line:
		uptime = uptime_line.group(1) #return that group as uptime
		return uptime
	else:
		return None

def main():
	'''
	Obtain the uptime from the show version output
	Prints to STDOUT '12 weeks, 5 days, 1 hour, 4 minutes'
	'''
	with open("../show_version.txt") as show_ver_file:
		show_version = show_ver_file.read()

	print obtain_uptime(show_version)


if __name__ == "__main__":
	main()