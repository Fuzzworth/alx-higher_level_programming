#!/usr/bin/python3
"""
Write a class Node that defines a node of a singly linked list by
"""


class Node:
    """
    Node Class

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Attributes:
        data (int): Human readable string describing the exception.
        next_node (Node): Exception error code.
    """

    def __init__(self, data, next_node=None):
        """
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            data (int): Description of `param1`.
            next_node (:obj:`Node`, optional): Description of `param2`

        Raises:
            TypeError: that are relevant to the interface.
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """int: data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (int): Description of `param1`.

        Raises:
            TypeError: that are relevant to the interface.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """:obj:`Node`: Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (:obj:`Node`:): Description of `param1`.

        Raises:
            TypeError: that are relevant to the interface.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """str: data string"""
        return str(self.__data)


class SinglyLinkedList(object):
    """
    SinglyLinkedList Class

    Attributes:
        head (Node): Human readable string describing the exception.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """str: string"""
        current_node = self.__head
        count = 0
        sll = ""
        while current_node is not None:
            if count > 0:
                sll += "\n"
            sll += "{:d}".format(current_node.data)
            count += 1
            current_node = current_node.next_node
        return sll

    def sorted_insert(self, value):
        """
        sorted insert function

        Args:
            value (int): integer

        """

        new_node = Node(value)
        current_node = self.__head
        previous_node = None
        if current_node is None:
            self.__head = new_node
        else:
            while current_node is not None:
                if (current_node.data >= new_node.data and
                        previous_node is None):
                    new_node.next_node = current_node
                    self.__head = new_node
                    break
                if current_node.data >= new_node.data:
                    previous_node.next_node = new_node
                    new_node.next_node = current_node
                    break
                previous_node = current_node
                current_node = current_node.next_node
            if current_node is None:
                if previous_node is not None:
                    previous_node.next_node = new_node
