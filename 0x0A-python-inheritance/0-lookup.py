""" Module contains a lookup function """


def lookup(obj):
    """ takes and object and looks up all attributes available on it

    Args:
        obj (object): object to lookup

    Returns:
        List of all available attributes in the object
    """
    return list(obj.__dict__)
