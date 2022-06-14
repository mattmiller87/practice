from nornir import InitNornir

# 1
# nr = InitNornir()
# print(nr.inventory)
# print(nr.inventory.hosts)
# nr.inventory.hosts['localhost1']
# nr.inventory.hosts['localhost1'].hostname

# 2 & 3
# nr = InitNornir()
# for host, host_data in nr.inventory.hosts.items():
#     print(f"hostname: {host_data.hostname}")
#     print(f"groups: {host_data.groups}")
#     print(f"platform: {host_data.platform}")
#     print(f"username: {host_data.username}")
#     print(f"password: {host_data.password}")
#     print(f"port: {host_data.port}")


# 4
# def my_task(task):
#     print("Hello")
# 
# if __name__ == "__main__":
#     nr = InitNornir(config_file="config.yaml")
#     nr.run(task=my_task)

# 5
def my_task(task):
    host = task.host
    print(f"hostname: {host.hostname}")
    print(f"dns1: {host['dns1']}")
    print(f"dns2: {host['dns2']}")


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    nr.run(task=my_task)
