#!/usr/bin/env python3
from .network import NetworkServer
from configs import read_core_yml

core_yml_dict = read_core_yml.start()
addons_list = []
for addon in core_yml_dict['addons']:
    addons_list.append(getattr(getattr(__import__('addons.'+ addon),addon),'Execute_Addon'))

def start():
    server = NetworkServer(addons_list)
    server.start()