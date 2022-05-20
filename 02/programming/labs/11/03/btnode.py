"""Binary search tree node."""


class Node(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, value, left=None, right=None):
        """Initializes a node."""
        self.value = value
        self.left = left
        self.right = right

    @property
    def value(self):
        """Getter for the value."""
        return self._value

    @value.setter
    def value(self, new):
        """Setter for the value."""
        self._value = new

    @property
    def left(self):
        """Getter for the left node."""
        return self._left

    @left.setter
    def left(self, value):
        """Setter for the left node."""
        self._left = Node(value)

    @property
    def right(self):
        """Getter for the right node."""
        return self._right

    @right.setter
    def right(self, value):
        """Setter for the right node."""
        self._right = Node(value)
