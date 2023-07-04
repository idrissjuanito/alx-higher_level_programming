#!/usr/bin/python3

""" End of line in string functions """

def text_indentation(text):
    """ strips spaces at beginning and end of text lines
    Args:
        text (str):
            The text to treat
    Returns:
        nothing
    """
    if not type(text) is str:
        raise TypeError("Text must be a string")
    line = ""
    for ch in text:
        if len(line) == 0 and ch == " ":
            continue
        if ch == " " and line[-1] == " ":
            continue
        line += ch
        if ch in ":?.":
            print(line)
            print()
            line = ""
    print(line, end="")
