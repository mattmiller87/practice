from nornir import InitNornir
from nornir.core.filter import F
from nornir_napalm.plugins.tasks import napalm_get
from pprint import pprint

def main():
    nr = InitNornir(config_file="config.yaml")
    nxos_filt = F(groups__contains="nxos")
    nr = nr.filter(nxos_filt)
    # 6a
    # aggresults = nr.run(task=napalm_get, getters=["config"])
    # 6b
    # aggresults = nr.run(task=napalm_get, getters=["config"], retrieve="running")
    # 6c
    # aggresults = nr.run(
    #    task=napalm_get,
    #     getters=["config", "facts"], getters_options={"config": {"retrieve": "running"}})
    # print(aggresults)
    # 6d
    aggresults = nr.run(
        task=napalm_get,
         getters=["config", "facts"], getters_options={"config": {"retrieve": "all"}})
    device_data = {}
    for hostname, multi_result in aggresults.items():
        device_data[hostname] = {}
        config_startup = multi_result[0].result["config"]["startup"].split("\n")[4:]
        config_running = multi_result[0].result["config"]["running"].split("\n")[4:]
        if config_startup == config_running:
            device_data[hostname]["config_match"] = True
        else:
            device_data[hostname]["config_match"] = False
        facts = multi_result[0].result["facts"]
        device_data[hostname]["model"] = facts["model"]
        device_data[hostname]["uptime"] = facts["uptime"]
        device_data[hostname]["vendor"] = facts["vendor"]

    pprint(device_data)

if __name__ == "__main__":
    main()