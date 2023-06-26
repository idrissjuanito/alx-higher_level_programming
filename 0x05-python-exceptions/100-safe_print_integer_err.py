from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value, end=""))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=stderr)