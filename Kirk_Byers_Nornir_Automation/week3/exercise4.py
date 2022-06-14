from nornir import InitNornir
from nornir.core.filter import F
from nornir_netmiko import netmiko_send_command
from pprint import pprint

# 4a
nr = InitNornir(config_file="config.yaml")
# 4b
eos = nr.filter(F(groups__contains="eos"))
eosresults = eos.run(
    task=netmiko_send_command,
    command_string="show interface status",
    use_textfsm=True)
# for hostname, multi_result in eosresults.items():
#    pprint(multi_result[0])

# 4c
device_data = {}
for hostname, multi_result in eosresults.items():
    device_data[hostname] = {}
    for data in multi_result[0].result:
        device_data[hostname][data["port"]] = {}
        device_data[hostname][data["port"]]["status"] = data["status"]
        device_data[hostname][data["port"]]["vlan"] = data["vlan"]


pprint(device_data)