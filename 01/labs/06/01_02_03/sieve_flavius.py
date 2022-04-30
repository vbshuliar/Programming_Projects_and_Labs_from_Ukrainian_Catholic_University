"""module checks lucky numbers
"""
from typing import List


def sieve_flavius(argument: int) -> List[int]:
    """returns lucky numbers
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    """
    res1 = []
    for i in range(argument):
        res1.append(i)
    res2 = []
    for i in res1:
        if res1[i] % 2 != 0:
            res2.append(res1[i])
    res3 = []
    ind = 1
    for i, j in enumerate(res2):
        if ind % 3 != 0:
            res3.append(res2[i])
        ind += 1
        j += 0
    ind = 1
    res4 = []
    for i, j in enumerate(res3):
        if ind % 7 != 0:
            res4.append(res3[i])
        ind += 1
        j += 0
    return res4
