#!/usr/bin/python3

import hidden_4
for n in dir(hidden_4):
    if not n.startswith("__"):
        print(n)
