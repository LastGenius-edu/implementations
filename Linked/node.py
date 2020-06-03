"""
Nodes
"""


class Node:
    """
    Node classes for one-way linked structures and two-way
    linked structures.
    """

    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class TwoWayNode(Node):
    """
    Two way Linked Node
    """

    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
