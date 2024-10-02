from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
import os
from rich import print


nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/MultiVendor_Jinja2_Templates/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')


