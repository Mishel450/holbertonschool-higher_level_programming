#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if (size == 0):
        return (0, "None")
    else:
        return (size, sentence[0])
