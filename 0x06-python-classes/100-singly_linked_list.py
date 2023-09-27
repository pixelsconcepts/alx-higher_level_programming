#!/usr/bin/python3
class Node:
    """A class that defines a node of a singly linked list."""

    @property
    def data(self):
        """Getter method for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute.

        Args:
            value (int): The value to set as data.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute.

        Args:
            value (Node or None): The next node in the linked list or None.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node or None): The next node in the linked list
            (default is None).
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self, head=None):
        """Initialize a new SinglyLinkedList instance.

        Args:
            head (Node, optional): The head node of the linked list
            (default is None).
        """
        self.head = head

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list
        (increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Generate a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
