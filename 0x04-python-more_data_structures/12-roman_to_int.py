#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    roman_val = [1, 5, 10, 50, 100, 500, 1000]
    if not roman_string or type(roman_string) is not str:
        return num
    prev_val = None
    for i in range(len(roman_string)):
        r = roman_string[i]
        idx_val = romans.index(r)
        val = roman_val[idx_val]

        if prev_val and val > prev_val:
            num += val - prev_val * 2
            prev_val = None
            continue
        num += val
        prev_val = val
    return num
