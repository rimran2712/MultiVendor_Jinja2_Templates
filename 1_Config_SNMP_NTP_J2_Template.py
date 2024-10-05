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
this program will do basic SNMP and NTP configuration to all Multivendor devices as in Topology

Prerequisite: NA
Variable Files: load variable from Nornir inventory (hostfile)

'''
def config_snmp_ntp_j2_template(task):
    snmp_ntp_template = task.run (task=template_file, template="snmp_ntp.j2", path=f"J2_Templates/{task.host.platform}")
    task.host['snmp_ntp'] = snmp_ntp_template.result
    snmp_ntp_rendered = task.host['snmp_ntp']
    snmp_ntp_config = snmp_ntp_rendered.splitlines()
    task.run (task=send_configs, configs=snmp_ntp_config)

reseults = nr.run (task=config_snmp_ntp_j2_template)
print_result (reseults)