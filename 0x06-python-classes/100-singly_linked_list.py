#!/usr/bin/python3

""" File contains Node class for singly linked list
 """


class Node:
    """ Node class for defining The nodes of a linked list

        Args:
            data (int): and integer value for the node
            next_node (Node): the next_node object
        Attributes:
            data (int): and integer value for the node
            next_node (Node): the next_node object
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter method for data of a linked list

        Returns:
            the node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not type(value) is int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for retrieving the next node of a linked list

        Returns:
            The next_node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value and not type(value) is type(self):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class that manages a linked list

        Args:
            head (Node): first node of the
        Attributes:
            head (Node): first node of the
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        strn = ""
        tmp = self.__head
        if tmp:
            while tmp:
                strn += str(tmp.data) + "\n"
                tmp = tmp.next_node
        return strn[:-1]

    def sorted_insert(self, value):
        """ inserts a node in a sorted linked list

        Args:
            value (int): Value of the node to insert

        Returns: Nothing
        """
        n = Node(value)
        if not self.__head:
            self.__head = n
        else:
            tmp = self.__head
            prev_node = None
            while (tmp):
                if tmp.data > n.data:
                    break
                prev_node = tmp
                tmp = tmp.next_node
            if not prev_node:
                n.next_node = self.__head
                self.__head = n
            else:
                n.next_node = prev_node.next_node
                prev_node.next_node = n
