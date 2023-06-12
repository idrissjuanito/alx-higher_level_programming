#!/usr/bin/python3
from sys import argv, exit

if __name__ != "__main__":
    exit(1)
pluralize = "s" if len(argv) > 1 else ""
print("{} argument{}:".format(len(argv), pluralize))
for i in range(len(argv)):
    if not i == 0:
        print("{}: {}".format(i, argv[i]))
