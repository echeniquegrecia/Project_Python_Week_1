#!/usr/bin/python3.6
import sys

def validate_my_parameters(int_required, str_required, float_required, *args):

    list_int = []
    list_str = []
    list_float = []

    for arg in args:
        if type(arg) is int:
            list_int.append(arg)
        elif type(arg) is str:
            list_str.append(arg)
        elif type(arg) is float:
            list_float.append(arg)

    if len(list_int) == int_required:
        int_required = True
    else:
        int_required = False
    if len(list_str) == str_required:
        str_required = True
    else:
        str_required = False
    if len(list_float) == float_required:
        float_required = True
    else:
        float_required = False

    return (int_required, str_required, float_required)