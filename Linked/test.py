"""
tests different linked structures
"""

from node import Node, TwoWayNode
from circularlist import CircularLinkedList


def one_way():
    """
    One-way Linked structure example
    """
    head = None

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)

    # Print the contents of the structure
    while head is not None:
        print(head.data)
        head = head.next

    head = Node(None, None)
    head.next = head

    for count in range(1, 6):
        head.next = Node(count, head.next)

    probe = head.next
    while probe is not head:
        print("!", probe.data)
        probe = probe.next


def two_way():
    """
    Two-way linked example
    """
    # Create a doubly linked structure with one node
    head = TwoWayNode(1)
    tail = head

    # Add four nodes to the end of the doubly linked structure
    for data in range(2, 6):
        node = TwoWayNode(data, tail)
        print('1', node.data, node.next, node.previous)
        tail.next = node
        tail = tail.next
        print('2', node.data, node.next, node.previous)

    # Print the contents of the linked structure in reverse order
    probe = tail
    while probe is not None:
        print(probe.data)
        probe = probe.previous


def circular():
    """
    Circular Linked List example
    """
    c = CircularLinkedList()
    for count in range(1, 6):
        c.add(count)

    probe = c.head.next
    while probe is not c.head:
        print(probe.data)
        probe = probe.next


if __name__ == '__main__':
    one_way()
    # two_way()
    # circular()
