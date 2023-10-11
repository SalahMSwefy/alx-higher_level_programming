#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = {}
    for i in a_dictionary:
        new_dir[i] = 2 * a_dictionary[i]
    return new_dir
