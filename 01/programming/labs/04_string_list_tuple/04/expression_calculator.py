def calculate_expression(expression):
    """calculates expression
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    expression = expression[13:-1]
    expression = expression.split(sep=" ")
    try:
        result = int(expression[0])
    except ValueError:
        return "Неправильний вираз!"
    expression.pop(0)
    if len(expression) == 1:
        return "Неправильний вираз!"
    while len(expression) > 1:
        el = expression[0]
        if expression[1] == "на":
            expression.pop(1)
        num2 = checker(expression[1])
        if num2 == "Неправильний вираз!":
            return num2
        if el in ("додати", "плюс"):
            result = result + num2
        elif el in ("відняти", "мінус"):
            result = result - num2
        elif el == "поділити":
            if num2 == 0:
                return "Неправильний вираз!"
            result = result / num2
        elif el == "помножити":
            result = result * num2
        else:
            return "Неправильний вираз!"
        del expression[:2]
    return result


def checker(num2):
    """function that checks if str can be converted into int
    >>> checker("8")
    8
    """
    try:
        int(num2)
    except ValueError:
        return "Неправильний вираз!"
    return int(num2)
