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

Prerequisite: please make sure device's interfaces configured with IP addresses 
either manually or using above script "2_Config_IP_Addresses_J2_Template"

Variable Files: load variable from Nornir inventory (hostfile)
'''
def config_ospf_j2_template(task):
    ospf_template = task.run (task=template_file, template="ospf.j2", path=f"J2_Templates/{task.host.platform}")
    task.host['ospf_cfg'] = ospf_template.result
    ospf_cfg_rendered = task.host['ospf_cfg']
    ospf_config = ospf_cfg_rendered.splitlines()
    task.run (task=send_configs, configs=ospf_config)

reseults = nr.run (task=config_ospf_j2_template)
print_result (reseults)