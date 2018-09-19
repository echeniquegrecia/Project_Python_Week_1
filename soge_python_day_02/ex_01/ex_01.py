#!/usr/bin/python3

def get_my_generator(*args):
    for arg in args:
        yield arg

#verify generator
# a = get_my_generator("uu", 1, "rt")
# for i in a:
#     print i