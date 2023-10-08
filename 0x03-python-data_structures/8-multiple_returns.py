#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        frist = "None"
    else:
        frist = sentence[0]
    return (len(sentence), frist)
