import sys


def return_digits(number):
    """return digits
    >>> return_digits("1")
    ' 1 \\n11 \\n 1 \\n 1 \\n 1 \\n 1 \\n111'
    """
    Zero = ["  ***  ", " *   * ", "*     *",
            "*     *", "*     *", " *   * ", "  ***  "]
    One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
    Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
    Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
    Four = ["   *  ", "  **  ", " * *  ",
            "*  *  ", "******", "   *  ", "   *  "]
    Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
    Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
    Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
    Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
    Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
    Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
    output = []
    for count1 in range(7):
        res = ""
        for count2 in number:
            num = Digits[int(count2)][int(count1)]
            res = res + num.replace("*", count2)
        output.append(res)
    result = "\n".join(output)
    return result


if __name__ == "__main__":
    try:
        number = sys.argv[1]
        print(return_digits(number))
    except ValueError as err:
        print(err)
