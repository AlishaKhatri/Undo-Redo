# Implement your Node class here
class Node:
    """
    Represents one node in a linked data structure.

    Attributes:
        value: The data stored in the node.
        next: A reference to the next node.
    """

    def __init__(self, value):
        self.value = value
        self.next = None