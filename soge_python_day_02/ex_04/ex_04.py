#!/usr/bin/python3

def convert_me_to_a_dict(my_list):
    my_dict= {}
    count = 0
    for item in my_list:
        my_dict.update({count:tuple([type(item).__name__, item])})
        count += 1
    return my_dict