'''
1. In the following directory there are six CDP files: 
  https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/CDP_DATA

These CDP files correspond to the following network (same network as exercise1 from class #5):
  https://pynet.twb-tech.com/static/img/simple_diagram1.png​

   a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.

   b. Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote hostnames, remote IP addresses, and remote platforms.  Your output should look similar to the following:

   remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
                    IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
            platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']
'''

