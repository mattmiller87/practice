# note: this exercise used lab gear with specific defaults, config, hosts, and groups yaml files
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.filter import F

def main():
    default_gateway = "10.220.88.1" # hard coded gateway
    nr = InitNornir(config_file="config.yaml")
    ios_filt = F(groups__contains="ios")
    eos_filt = F(groups__contains="eos")
    nr = nr.filter(ios_filt | eos_filt)
    aggresults = nr.run(task=napalm_get, getters=["arp_table"])

    for host, host_data in aggresults.items():
        for item in host_data[0].result["arp_table"]:
            if item["ip"] == default_gateway:
                print(f"Host: {host}, Gateway: {item}")


if __name__ == "__main__":
    main()
