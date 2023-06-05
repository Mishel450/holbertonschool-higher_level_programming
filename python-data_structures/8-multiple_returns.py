#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) is not None):
        size = len(sentence)
        if (sentence[0] is not None):
            fchr = sentence[0]
        else:
            fchr = None
        return (size, fchr)
    else:
        return (len(sentence), None)
