#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    if (list_length == 0):
        return new_list
    if (not isinstance(my_list_1, list) or not isinstance(my_list_2, list)):
        return new_list
    for i in range(list_length):
        try:
            quot = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(quot)
            quot = 0
    return new_list
