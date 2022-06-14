from nornir import InitNornir
from nornir.core.filter import F
from nornir_netmiko import netmiko_send_command
from pprint import pprint

nr = InitNornir(config_file=config.yaml)
