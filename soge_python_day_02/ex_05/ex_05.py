#!/usr/bin/python3

def format_my_args(*args):
    my_format = {
        int : lambda item: "i^:"+ str(item),
        float : lambda item: "ff::"+ str(item),
        str : lambda item: "[[" + item + "]]"
    }

    for item in args:
        if type(item) in my_format:
            print(my_format[type(item)](item))
        else:
            print("Unknown value")