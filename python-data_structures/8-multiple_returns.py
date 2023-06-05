#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) is not None):
        size = len(sentence)
        fchr = sentence[0]
        return (size, fchr)
    else:
        return (0, None)
