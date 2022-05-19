"""
File: linkedbst.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from math import log
from random import sample
from time import time
from sys import setrecursionlimit


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it'variable present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            variable = ""
            if node != None:
                variable += recurse(node.right, level + 1)
                variable += "| " * level
                variable += str(node.data) + "\n"
                variable += recurse(node.left, level + 1)
            return variable

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item'variable position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item'variable spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree." "")

        # Helper function to adjust placement of an item
        def lift_in_max(top):
            # Replace top'variable datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top'variable left subtree
            #       has been removed
            # Post: top.data = maximum value in top'variable left subtree
            parent = top
            current_node = top.left
            while not current_node.right == None:
                parent = current_node
                current_node = current_node.right
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else:
                parent.right = current_node.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        removed_item = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        direction = "L"
        current_node = self._root
        while not current_node == None:
            if current_node.data == item:
                removed_item = current_node.data
                break
            parent = current_node
            if current_node.data > item:
                direction = "L"
                current_node = current_node.left
            else:
                direction = "R"
                current_node = current_node.right

        # Return None if the item is absent
        if removed_item == None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node'variable value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not current_node.left == None and not current_node.right == None:
            lift_in_max(current_node)
        else:

            # Case 2: The node has no left child
            if current_node.left == None:
                new_child = current_node.right

                # Case 3: The node has no right child
            else:
                new_child = current_node.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == "L":
                parent.left = new_child
            else:
                parent.right = new_child

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection'variable size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = pre_root.left
        return removed_item

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with new_item and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                old_data = probe.data
                probe.data = new_item
                return old_data
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """
        Return the height of tree
        :return: int
        """

        def recurse(top):
            """
            Helper function
            :param top:
            :return:
            """
            if not top.left and not top.right:
                return 0
            left_nodes = recurse(top.left) if top.left else -1
            right_nodes = recurse(top.right) if top.right else -1

            return max(left_nodes, right_nodes) + 1

        return recurse(self._root)

    def is_balanced(self):
        """
        Return True if tree is balanced
        :return:
        """
        return self.height() < 2 * log(self._size + 1, 2) - 1

    def range_find(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:
        :param high:
        :return:
        '''
        temp = []
        result = []
        for _ in iter(self):
            temp.append(_)
        for _ in temp:
            if _ >= low and _ <= high:
                result.append(_)

        return sorted(result)

    def rebalance(self):
        """
        Rebalances the tree.
        :return:
        """
        temp = self.inorder()

        def recurse(temp):
            elem = len(temp) // 2
            try:
                node = BSTNode(temp[elem])
            except IndexError:
                node = None

            if len(temp) > 1:
                node.left = recurse(temp[:elem])
                node.right = recurse(temp[elem + 1 :])
            return node

        self._root = recurse(list(temp))

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        temp = []
        for _ in iter(self.inorder()):
            if _ > item:
                temp.append(_)
        return sorted(temp)[0] if len(temp) > 0 else None

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        temp = []
        for _ in iter(self.inorder()):
            if _ < item:
                temp.append(_)

        return sorted(temp)[-1] if len(temp) > 0 else None

    def demo_bst(self, path):
        """
        Demonstration of efficiency binary search tree for the search tasks.
        :param path:
        :type path:
        :return:
        :rtype:
        """
        setrecursionlimit(100000)
        with open(path, "r") as data:
            words = sample(data.read().split(), 10000)

        start = time()
        sorted_words = sorted(words)
        for _ in words:
            sorted_words.index(_)
        print(f"Sorted list: {time() - start}.")

        print("Please wait now for about 30 seconds.")
        bst = LinkedBST(sorted_words)
        start = time()
        for _ in words:
            bst.find(_)
        print(f"Sorted tree: {time() - start}.")

        start = time()
        bst = LinkedBST(words)
        for _ in words:
            bst.find(_)
        print(f"Chaotic tree: {time() - start}.")

        bst.rebalance()
        start = time()
        for _ in words:
            bst.find(_)
        print(f"Rebalanced tree: {time() - start}.")


if __name__ == "__main__":
    print(LinkedBST().demo_bst("everything/binary_search_tree-master/words.txt"))
