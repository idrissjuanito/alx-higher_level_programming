#!/usr/bin/python3


def multiple_returns(sentence):
    f_char = None if len(sentence) == 0 else sentence[0]

    return (len(sentence), f_char)
