"""
Implements circular linked list
"""

from node import Node


class CircularLinkedList:
    """
    Circular Linked List class
    """
    def __init__(self):
        """
        Creates empty lsit
        """
        self.head = Node(None, None)  # this is the sentinel node!
        self.head.next = self.head  # link it to itself

    def add(self, data):
        """
        Adds an element to the list
        :param data: data
        :return: None
        """
        self.head.next = Node(data, self.head.next)

    def __contains__(self, data):
        """
        Checks if data is in the list
        :param data:
        :return:
        """
        current = self.head.next
        while current != self.head:
            if current.data == data:  # element found
                return True
            current = current.next
        return False
