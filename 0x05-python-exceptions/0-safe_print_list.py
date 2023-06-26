#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if (x == 0 or not isinstance(my_list, list)):
        return 0
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            if (i > 0):
                print()
            return i
    print()
    return i+1
