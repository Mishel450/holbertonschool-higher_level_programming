#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if (sentence[0] is not None):
        fchr = sentence[0]
    else:
        fchr = None
    return (size, fchr)
