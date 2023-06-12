#!/usr/bin/python3
from sys import exit, argv

if __name__ != "__main__":
    exit(1)
args_len = len(argv)
sum = 0

if args_len > 1:
    for i in range(1, args_len):
        sum += int(argv[i])
print(sum)
