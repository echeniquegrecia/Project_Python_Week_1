#!/usr/bin/env python3
import os
import yaml

def start():
    with open("/home/grecia/soge/soge_python_my_apache/myApache/configs/core.yml", 'r') as stream:
        try:
            return (yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)