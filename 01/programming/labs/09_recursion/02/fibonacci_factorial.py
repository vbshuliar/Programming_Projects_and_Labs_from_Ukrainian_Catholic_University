"""
recursive and iterative solving problems
"""


<<<<<<< HEAD
<<<<<<< HEAD
import time


=======
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
=======
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
def numbers_time_test(function=0, realisation=0, verbose=False):
    """
    compares time consuming
    >>> numbers_time_test()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    '0.0001'
=======
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
    """

    num = 200

<<<<<<< HEAD
    if function == 0:
        if realisation == 0:
            start = time.time()
            res = factorial_recursive(num)
            finish = time.time()
        else:
            start = time.time()
            res = factorial_iterative(num)
            finish = time.time()
    else:
        if realisation == 0:
            start = time.time()
            res = fibonacci_recursive(num)
            finish = time.time()
        else:
            start = time.time()
            res = fibonacci_iterative(num)
            finish = time.time()

    timer = f"{(finish - start):.3f}1"

    if verbose:
        output = f"""
The result of your test is: {res}.
The time it started is: {start}.
The time it ended is: {finish}
Total time consumption is equal {timer}
"""
    else:
        output = timer

    return output


=======
>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
=======
    """


>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
=======
    """


>>>>>>> 375dc696a284bf808dca0ddce8e532001f77123e
def factorial_recursive(num):
    """
    recursively calculates factorial

    >>> factorial_recursive(3)
    6
    """

    if num < 0:
        return num
    if num == 0 or num == 1:
        return 1

    return num * factorial_recursive(num - 1)


def factorial_iterative(num):
    """
    iteratively calculates factorial

    >>> factorial_iterative(6)
    720
    """

    result = 1

    for num1 in range(1, num + 1):
        result *= num1

    return result


def fibonacci_recursive(num):
    """
    recursively calculates fibo number

    >>> fibonacci_recursive(9)
    55
    """

    if num == 0 or num == 1:
        return 1

    return fibonacci_recursive(num - 2) + fibonacci_recursive(num - 1)


def fibonacci_iterative(num):
    """
    iteratively calculates fibo number

    >>> fibonacci_iterative(4)
    5
    """

    num1 = 0
    num2 = 1
    counter = -1

    while counter < num:
        temp = num1
        num1 = num2
        num2 += temp
        counter += 1

    return num1


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
