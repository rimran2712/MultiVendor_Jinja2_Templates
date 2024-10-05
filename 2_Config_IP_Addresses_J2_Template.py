from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
from nornir_jinja2.plugins.tasks import template_file
import os
from rich import print


nr = InitNornir (config_file="Inventory/config.yaml")

# Clearing the Screen
os.system('clear')

'''
this program will configure IP addresses to all Multivendor devices as in Topology

Prerequisite: NA
Variable Files: load variable from Nornir inventory (hostfile)

'''

def config_ip_addresses_j2_template(task):
    ip_addresses_template = task.run (task=template_file, template="ip_addresses.j2", path=f"J2_Templates/{task.host.platform}")
    task.host['ip_add'] = ip_addresses_template.result
    ip_addresses_rendered = task.host['ip_add']
    ip_addresses_config = ip_addresses_rendered.splitlines()
    task.run (task=send_configs, configs=ip_addresses_config)

reseults = nr.run (task=config_ip_addresses_j2_template)
print_result (reseults)