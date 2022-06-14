from nornir import InitNornir
from nornir.core.filter import F


nr = InitNornir(config_file="config.yaml")
# 1a
# print(nr.inventory.hosts['arista3'].data)
# print(nr.inventory.hosts['arista3'].items())
# 1b - edited groups.yaml and hosts.yaml files

# 2a
# print(nr.filter(name="arista1").inventory.hosts)
# 2b
# wan = nr.filter(role="WAN")
# print(f"wan devices: {wan.inventory.hosts}")
# print(f"wan devices using port 22: {wan.filter(port=22).inventory.hosts}")
# 2c
# sfo = nr.filter(F(groups__contains="sfo"))
# print(f"sfo devices: {sfo.inventory.hosts}")

# 3a
# print(f"agg devices: {agg.inventory.hosts}")
# agg = nr.filter(F(role="AGG"))
# 3b
# sea_or_sfo = nr.filter(F(groups__contains="sea") | F(groups__contains="sfo"))
# print(f"sea or sfo devices: {sea_or_sfo.inventory.hosts}")
# 3c
# wan_and_racecar = nr.filter(F(role="WAN") & F(site_details__wifi_password__contains="racecar"))
# print(f"wan and wifi pass is racecar: {wan_and_racecar.inventory.hosts}")
# 3d
wan_and_racecar = nr.filter(F(role="WAN") & ~F(site_details__wifi_password__contains="racecar"))
print(f"wan and wifi pass is racecar: {wan_and_racecar.inventory.hosts}")