#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = -1
    if not a_dictionary:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > max_score:
                max_score = value
                res = key
    return res
