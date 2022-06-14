# note: this exercise used lab gear with specific defaults, config, hosts, and groups yaml files
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
import os

# 5a
def main():
    nr = InitNornir(config_file="config.yaml")
    nr.inventory.hosts["cisco3"].password = 'bogus' # 5b
    ios_filt = F(groups__contains="ios")
    nr = nr.filter(ios_filt)
    aggresults = nr.run(task=netmiko_send_command, command_string="show ip int brief")
    print_result(aggresults)
    # 5b
    print(f"object.failed_hosts: {aggresults.failed_hosts}")
    print(f"nr.data.failed_hosts: {nr.data.failed_hosts}")

    # 5c
    nr.inventory.hosts["cisco3"].password = os.environ["NORNIR_PASSWORD"]
    aggresults = nr.run(
        task=netmiko_send_command,
        command_string="show ip int brief",
        on_good=False,
        on_failed=True,
    )
    print(f"object.failed_hosts: {aggresults.failed_hosts}")
    print(f"nr.data.failed_hosts: {nr.data.failed_hosts}")

    # 5d
    nr.data.recover_host("cisco3")
    # nr.data.reset_failed_hosts() # extra option to reset all hosts
    print(f"nr.data.failed_hosts: {nr.data.failed_hosts}")


if __name__ == "__main__":
    main()
