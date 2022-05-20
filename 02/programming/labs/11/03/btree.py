"""Binary search tree."""

from btnode import Node


class LinkedBST:
    """Linked binary search tree."""

    def __init__(self, value):
        """Initializes a tree."""
        self.root = Node(value)

    def set_left(self, value):
        """Sets left."""
        self.root.left = value

    def get_left(self):
        """Returns left."""
        return self.root.left

    def set_right(self, value):
        """Sets right."""
        self.root.right = value

    def get_right(self):
        """Returns right."""
        return self.root.right

    def set_root(self, new):
        """Sets root."""
        self.root.value = new

    def get_root(self):
        """Returns root."""
        return self.root.value

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        print(self.root)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        if self.left:
            self.left.inorder()
        print(self.root)
        if self.right:
            self.right.inorder()

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root)
