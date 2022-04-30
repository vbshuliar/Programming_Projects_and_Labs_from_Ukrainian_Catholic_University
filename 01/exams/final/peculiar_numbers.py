def read_numbers(path: str) -> list:
    """
    Read the numbers file and return a list of numbers as strings.

    >>> read_numbers("digits.txt")
    ['731711196', '116410407', '???324321', '995549301',
    '672734697', '158484???', '456???233']
    """

    temp, output = [], []
    with open(path, "r") as digits:
        result = digits.readlines()
    for each in result:
        temp.append(each.rstrip())
    for num in range(len(temp[0])):
        temp_lst = []
        for each in range(9):
            temp_lst.append(temp[each][num])
        output.append("".join(temp_lst))

    return output


def find_missing_numbers(numbers: list) -> list:
    """
    Find positions where the missing numbers "???" are located.
    Return list of tuples (column_index, name_of_the_digit)
    where name_of_the_digit could be any of {first, central, last}
    depending on their position.

    >>> find_missing_numbers(['731711196', '116410407', '???324321',\
     '995549301', '672734697', '158484???', '456???233'])
    [(2, 'first'), (5, 'last'), (6, 'central')]
    """

    result = []
    for each in range(len(numbers)):
        if "???" in numbers[each]:
            temp = numbers[each].find("???")
            if temp == 0:
                result.append((each, "first"))
            elif temp == 3:
                result.append((each, "central"))
            elif temp == 6:
                result.append((each, "last"))

    return result


def impute_missing_numbers(numbers: list, missing_positions: list, inplace=False):
    """
    Impute missing numbers, if inplace=False, replace the found missing
    numbers in their lines and return a list of found missing numbers,
    if inplace=True, replace the found missing numbers in their lines.

    >>> impute_missing_numbers(['731711196', '116410407', '???324321', \
    '995549301', '672734697', '158484???', '456???233'] \
    , missing_positions=[(2, 'first'), (5, 'last'), (6, 'central')], inplace=False)
    [(2, 'first', '525'), (5, 'last', '018'), (6, 'central', '394')]
    >>> impute_missing_numbers(['731711196', '116410407', '???324321', \
    '995549301', '672734697', '158484???', '456???233'] \
    , missing_positions=[(2, 'first'), (5, 'last'), (6, 'central')], inplace=True)
    """

    for ind, num in enumerate(missing_positions):
        temp = numbers[num[0]]
        if num[1] == "first":
            result = str(int(temp[3:6]) * 2 - int(temp[6:9][::-1]))
        elif num[1] == "central":
            result = str(int((int(temp[0:3]) + int(temp[6:9][::-1])) / 2))
        elif num[1] == "last":
            result = str(int(temp[3:6]) * 2 - int(temp[0:3]))[::-1]
        missing_positions[ind] = (num[0], num[1], str(result))

    if not inplace:
        return missing_positions


def check_central_numbers(numbers: list) -> bool:
    """Check the peculiarity of the numbers.
    Check compliance with the rules.

    >>> check_central_numbers(['731711196', '116410407', \
    '525324321', '995549301', '672734697', '158484018', '456394233'])
    True
    >>> check_central_numbers(['731711194', '116410407', \
    '525324321', '995549301', '672734697', '158484018', '456394233'])
    False
    """

    pass


def write_imputed(imputed_numbers: list):
    """
    Write the imputed and checked results
    to the "peculiar_numbers_imputed.txt" file.
    """

    pass


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
