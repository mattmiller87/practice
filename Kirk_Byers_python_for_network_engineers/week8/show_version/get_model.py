#Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.

import re

def obtain_model(data):
	model_line = re.search(r"Cisco (.+?) .+bytes of memory", data) #match a line that starts with Cisco and ends with bytes of memory, create a group on the Cisco model
	if model_line:
		model = model_line.group(1) #return that group as model
		return model
	else:
		return None

def main():
	with open("../show_version.txt") as show_ver_file:
		show_ver = show_ver_file.read()

	print obtain_model(show_ver)


if __name__ == "__main__":
	main()