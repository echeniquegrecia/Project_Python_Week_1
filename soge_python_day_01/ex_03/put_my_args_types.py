#!/usr/bin/python3.6
import sys

def put_my_args_types(*args):
    for arg in args:
        print("Argument " + str(arg) +" is an " + type(arg).__name__)