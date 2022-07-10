"""
boy and girl name stats
"""


def find_names(file_path):
    """
    most frequent names, names count, letter

    >>> temp = find_names("./girl_names")
    >>> len(temp[1][1])
    201w
    """

    with open(file_path, 'r', encoding="utf-8", errors="ignore") as file1:
        lst = file1.readlines()
        lst.pop(0)
        for i in range(len(lst)):
            lst[i] = (lst[i].rstrip().split("\t"))
            lst[i][0] = lst[i][0].rstrip()
            lst[i][1] = int(lst[i][1][1:-1])

    first = lst.copy()

    for i in range(len(first)):
        first[i] = first[i][1]

    first = quick_sort(first)

    for i in lst:
        for j in range(len(first)):
            if first[j] is i[1]:
                first[j] = i[0]
    first = set(first)
    counter = 0
    names = set()
    temp = []

    names, counter, temp = linear_search(lst, 1)

    second = (counter, names)
    third = {}

    for i in temp:
        if i in third.keys():
            third[i] += 1
        else:
            third[i] = 1

    third = list(third.items())

    letters = third.copy()

    for i in range(len(letters)):
        letters[i] = letters[i][1]

    letters = quick_sort(letters)
    letters = letters[-1]

    test_list = third.copy()

    for i in test_list:
        if i[1] == letters:
            third = i

    third = list(third)
    counter = 0

    for i in lst:
        if third[0] == i[0][0]:
            counter += i[1]

    third.append(counter)
    third = tuple(third)

    return (first, second, third)


def linear_search(list_of_values, value):
    """
    linear search algorithm

    >>> linear_search([['АВЕЛІНА', 1], ['АВРОРА', 2], ['АГАТА', 3]], 1)
    ({'АВЕЛІНА'}, 1, ['А', 'А', 'А'])
    """

    lst = []
    counter = 0
    temp = []

    for num1 in range(len(list_of_values)):
        if list_of_values[num1][1] == value:
            lst.append(list_of_values[num1][0])
            counter += 1
        temp.append(list_of_values[num1][0][0])

    return set(lst), counter, temp


def quick_sort(lst):
    """
    quick sort algorithm

    >>> quick_sort([6, 2, 1, 4])
    [2, 4, 6]
    """

    smaller, pivots, bigger = [], [], []

    if len(lst) <= 1:
        return lst

    pivot = lst[0]

    for num1 in lst:
        if num1 < pivot:
            smaller.append(num1)
        elif num1 > pivot:
            bigger.append(num1)
        else:
            pivots.append(num1)

    bigger = quick_sort(bigger)
    smaller = quick_sort(smaller)

    result = smaller + pivots + bigger

    return result[-3:]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
