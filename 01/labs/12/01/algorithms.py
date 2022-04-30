"""
search and sort algorithms
"""


def linear_search(list_of_values, value):
    """
    linear search algorithm

    >>> linear_search([10, 20, 30, 40, 50], 30)
    2

    >>> linear_search([10, 20, 30, 40, 50], 60)
    -1
    """

    for num1 in range(len(list_of_values)):
        if list_of_values[num1] == value:
            return num1

    return -1


def merge_sort(lst):
    """
    sorts list with merge algorithm

    >>> merge_sort([3, 2, 1, 4])
    [1, 2, 3, 4]
    """

    if len(lst) <= 1:
        return lst
    else:

        first = lst[:len(lst) // 2]
        second = lst[len(lst) // 2:]

        merge_sort(first)
        merge_sort(second)

        num1, num2, num3 = 0, 0, 0

        while num2 < len(second) and num1 < len(first):
            if first[num1] < second[num2]:
                lst[num3] = first[num1]
                num1, num3 = num1 + 1, num3 + 1
            else:
                lst[num3] = second[num2]
                num2, num3 = num2 + 1, num3 + 1

        while num2 < len(second):
            lst[num3] = second[num2]
            num2, num3 = num2 + 1, num3 + 1

        while num1 < len(first):
            lst[num3] = first[num1]
            num1, num3 = num1 + 1, num3 + 1

        return lst


def binary_search(list_of_values, value):
    """
    searches an element with binary algorithm

    >>> binary_search([2, 3, 5, 6, 7, 23, 100], 23)
    5

    >>> binary_search([10, 20, 30, 40], 50)
    -1
    """

    start = 0
    finish = len(list_of_values) - 1

    while start <= finish:
        mid = int(start + (finish - start) / 2)
        mid_val = list_of_values[mid]

        if value == mid_val:
            return mid
        if mid_val > value:
            finish = mid
            finish -= 1
        else:
            start = mid
            start += 1

    return -1


def selection_sort(lst):
    """
    selection sort algorithm

    >>> selection_sort([5, 2, 1, 4])
    [1, 2, 4, 5]
    """

    for num1 in range(0, len(lst) - 1):
        lower = num1

        for num2 in range(lower + 1, len(lst)):
            if lst[lower] > lst[num2]:
                lower = num2

        temp = lst[num1]
        lst[num1] = lst[lower]
        lst[lower] = temp

    return lst


def quick_sort(lst):
    """
    quick sort algorithm

    >>> quick_sort([6, 2, 1, 4])
    [1, 2, 4, 6]
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

    return result


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
