"""Linked binary tree."""
from node import Node


class BinaryTree:
    """Linked binary tree class."""

    def __init__(self):
        """Initializes class object."""
        self._root = None

    def add_left(self, parent, number):
        """Adds left child."""
        if not self._root:
            raise IndexError("There is no even the root of the tree.")
        else:
            position = self.find_node(parent)
            position._left = Node(number)

    def add_right(self, parent, number):
        """Adds right child."""
        if not self._root:
            raise IndexError("There is no even the root of the tree.")
        else:
            position = self.find_node(parent)
            position._right = Node(number)

    def find_node(self, number):
        """Finds a node by its value."""
        if not self._root:
            raise IndexError("There is no even the root of the tree.")

        def recurse(cursor):
            """Rercursive function."""
            if cursor:
                recurse(cursor._left)
                nodes.append(cursor)
                recurse(cursor._right)

        nodes = []
        recurse(self._root)
        for each in nodes:
            if each._value == number:
                return each

    def get_left(self, parent):
        """Returns left child."""
        position = self.find_node(parent)
        return position._left

    def get_right(self, parent):
        """Returns right child."""
        position = self.find_node(parent)
        return position._right

    def set_root(self, new_root):
        """Sets a root in a Binary tree."""
        self._root = Node(new_root)

    def get_root(self):
        """Returns a root of a Binary tree."""
        return self._root._value

    def inorder(self):
        """Returns inorder."""
        inorder_list = list()

        def recurse(cursor):
            """Recursive function."""
            if cursor != None:
                recurse(cursor._left)
                inorder_list.append(cursor._value)
                recurse(cursor._right)

        recurse(self._root)
        return inorder_list

    def leaf_paths(self):
        """Returns all leaves paths."""

        def recurse(cursor):
            """Recursive function"""
            pass

        pass

    def is_leaf(self, number):
        """Checks whether the node is a leaf."""
        position = self.find_node(number)
        if not position._left and not position._right:
            return True
        return False


if __name__ == "__main__":
    tree = BinaryTree()
    tree.set_root("4")
    tree.add_left("4", "1")
    tree.add_left("1", "2")
    tree.add_right("1", "3")
    tree.add_left("2", "7")
    tree.add_right("2", "5")
    tree.add_right("3", "8")

    a = tree.inorder()
    print(a)
