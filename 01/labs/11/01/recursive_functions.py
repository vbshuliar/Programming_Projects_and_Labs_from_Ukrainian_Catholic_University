"""
recursive solving problems
"""


def create_table(num1, num2):
    """
    table of nums

    num1 - height
    num2 - width

    >>> create_table(3, 6)
<<<<<<< HEAD
<<<<<<< HEAD
    """
    num1 = num2
    num2 = num1
=======
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21]]
    """
    pass
<<<<<<< HEAD
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
=======
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
=======
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21]]
    """
    pass
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e


def flatten(lst):
    """
    analazyses list and flattens it

    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    """

<<<<<<< HEAD
    if isinstance(lst, list) and len(lst) == 0:
        return []

<<<<<<< HEAD
    if not isinstance(lst, list):
        return lst

    if not isinstance(lst[0], list):
        return [lst[0]] + flatten(lst[1:])

    if isinstance(lst, list):
        return flatten(lst[0]) + flatten(lst[1:])

=======
=======
    if type(lst) is list and len(lst) == 0:
        return []

>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
    if type(lst) is not list:
        return lst

    if type(lst[0]) is not list:
        return [lst[0]] + flatten(lst[1:])

    if type(lst) is list:
        return flatten(lst[0]) + flatten(lst[1:])

<<<<<<< HEAD
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
=======
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
