#!/usr/bin/python3

def uppercase(str):
    for c in str:
        numChar = ord(c)
        if (numChar > 96 and numChar < 123):
            numChar -= 32
        print(chr(numChar), end="")
    print()
