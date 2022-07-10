"""Testing of the program."""
from LinkedBinaryTree import BinaryTree


def main():
    """Tests for the binary tree."""

    test = BinaryTree()

    # Testing root setting.
    test.set_root(4)

    # Testing add functions.
    test.add_left(4, 1)
    test.add_left(1, 2)
    test.add_right(1, 3)
    test.add_right(4, 7)

    # Testing getting functions.
    test_left_child = test.get_left(4)
    assert test_left_child._value == 1
    print(test.get_left(4)._value)

    test_right_child = test.get_right(4)
    assert test_right_child._value == 7
    print(test.get_right(4)._value)

    # Testing leaf checking functions.
    test_is_leaf = test.is_leaf(7)
    assert test_is_leaf == True
    print(test.is_leaf(7))

    test_is_leaf = test.is_leaf(4)
    assert test_is_leaf == False
    print(test.is_leaf(4))

    # Testing inorder.
    test_inorder = test.inorder()
    assert test_inorder == [2, 1, 3, 4, 7]
    print(test_inorder)

    print("Tests passed!")


if __name__ == "__main__":
    main()
