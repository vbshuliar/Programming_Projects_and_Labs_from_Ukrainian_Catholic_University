"""module checks happy tickets
"""


def happy_number(number: int) -> bool:
    """checks whether number if happy
    >>> happy_number(12345)
    False
    """
    number = str(number)
    if len(number) > 8:
        return None
    number = number.zfill(8)
    arg1 = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])
    arg2 = int(number[4]) + int(number[5]) + int(number[6]) + int(number[7])
    if arg1 == arg2:
        return True
    return False


def count_happy_numbers(num: int) -> int:
    """counts happy numbers
    >>> count_happy_numbers(1)
    1
    """
    counter = 0
    tempor = happy_numbers(0, num)
    for i in tempor:
        counter += 1
        i += 0
    return counter


def happy_numbers(num1: int, num: int) -> list:
    """creates list of happy numbers
    >>> happy_numbers(0, 1000)
    [0]
    """
    amount_tickets = num - num1
    tickets = []
    for i in range(amount_tickets + 1):
        temp = num1 + i
        if happy_number(temp) is True:
            tickets.append(temp)
    return tickets
