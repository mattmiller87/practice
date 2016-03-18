#Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)

import re

def obtain_version(data):
	version_line = re.search(r"Cisco IOS Software.*Version (.+?),", data) #match a line that starts with Cisco IOS Software, create a group on the Version
	if version_line:
		version = version_line.group(1) #return that group as version
		return version
	else:
		return None

def main():
	with open("../show_version.txt") as show_ver_file:
		show_version = show_ver_file.read()

	print obtain_version(show_version)


if __name__ == "__main__":
	main()