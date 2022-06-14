# note: this exercise used lab gear with specific defaults, config, hosts, and groups yaml files
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir.core.filter import F

# 3

nr = InitNornir(config_file="config.yaml")
ios_filt = F(groups__contains="ios")
eos_filt = F(groups__contains="eos")
nr = nr.filter(ios_filt | eos_filt)

aggresults = nr.run(task=netmiko_send_command, command_string="show ip arp")

for host, host_data in aggresults.items():
    for item in host_data[0].result.split('\n'):
        if "10.220.88.1" in item: # hard coded gateway
            print(f"Host: {host}, Gateway: {item}")

