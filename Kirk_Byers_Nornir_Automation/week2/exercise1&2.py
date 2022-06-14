from nornir import InitNornir

# 1b
# nr = InitNornir(config_file="config.yaml")
# workers = nr.config.runner.options
# print("Number of Workers: {}".format(workers['num_workers']))

# 1d
# nr = InitNornir(
#     config_file="config.yaml",
#     runner={"plugin": "threaded", "options": {"num_workers": 15}},
#     )
# workers = nr.config.runner.options
# print("Number of Workers: {}".format(workers['num_workers']))

# 2
from nornir.core.filter import F
nr = InitNornir(config_file="config.yaml")
filt = F(groups__contains="ios")
nr = nr.filter(filt)
# print(nr.inventory.hosts)

# 2b
from nornir_netmiko import netmiko_send_command

my_results = nr.run(task=netmiko_send_command, command_string="show run | in hostname")
print(f"object type: {type(my_results)}")
print(f"keys: {my_results.keys()}")
print(f"items: {my_results.items()}")
print(f"values: {my_results.values()}")

# 2c
host_results = my_results['cisco3']
print(type(host_results))
print(host_results[0])
print(host_results.__iter__) # is this object iterable?

# 2d
task_result = host_results[0]
print(f"object type: {type(task_result)}")
print(f"host: {task_result.host}")
print(f"task name: {task_result.name}")
print(f"task result: {task_result.result}")
print(f"task failed status: {task_result.failed}")
