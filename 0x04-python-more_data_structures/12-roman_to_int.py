#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    roman_val = [1, 5, 10, 50, 100, 500, 1000]
    if not roman_string or type(roman_string) is not str:
        return num
    for i in range(len(roman_string)):
        r = roman_string[i]
        if r in romans:
            if r == "X" and roman_string[i - 1] == "I":
                num += 8
                continue
            num += roman_val[romans.index(r)]
    return num
