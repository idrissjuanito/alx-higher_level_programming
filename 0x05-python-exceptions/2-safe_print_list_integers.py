#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if (x == 0 or not isinstance(my_list, list)):
        return 0
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            printed += 1
    print()
    return printed
