"""
module calculus
"""


def find_max_1(func, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function func in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    function_max = 0
    for num1 in points:
        try:
            x = points[num1]
            if type(func) != str:
                function_temp = func(x)
            else:
                function_temp = eval(func)
            if function_temp > function_max:
                function_max = function_temp
        except IndexError:
            pass
    return function_max


def find_max_2(func, points):
    """
    (function or str, list(number)) -> (number)

    Find and return list of points where function func has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    result = []
    function_max = 0
    for num1 in range(len(points)):
        x = points[num1]
        if type(func) == str:
            function_temp = eval(func)
        else:
            function_temp = func(x)
        if function_temp > function_max:
            function_max = function_temp
            result = []
            result.append(x)
        elif function_temp == function_max:
            function_max = function_temp
            result.append(x)
    return result


def compute_limit(seq):
    """
    (function or str) -> (number)

    Compute and return limit of num1 convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []
    num1 = 0
    while True:
        n = 10**num1
        if type(seq) is str:
            lst.append(eval(seq))
        else:
            lst.append(seq(n))
        if num1 != 0 and abs(lst[num1] - lst[num1 - 1]) < 0.001:
            if round(lst[num1], 1) == round(lst[num1], 2):
                return float(f"{lst[num1]:.1f}")
            return float(f"{lst[num1]:.2f}")
            break
        num1 += 1


def compute_derivative(func, x_0):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function func in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """

    aprox = []
    num1 = 0

    while True:
        dx_func = 10**-num1
        x = x_0 + dx_func

        if type(func) is str:
            difer = eval(func)
        else:
            difer = func(x)

        x = x_0

        if type(func) is str:
            difer -= eval(func)
        else:
            difer -= func(x)

        der = difer / dx_func
        aprox.append(der)

        if num1 != 0 and abs(aprox[num1] - aprox[num1 - 1]) < 0.001:
            if round(aprox[num1], 1) == round(aprox[num1], 2):
                return float(f"{aprox[num1]:.1f}")
            return float(f"{aprox[num1]:.2f}")
            break
        num1 += 1


def get_tangent(func, x_0):
    """
    (function or str, number) -> (str)

    Compute and return tangent line to function func in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """

    x = x_0
    f_x_0_der = str(compute_derivative(func, x_0))

    if type(func) is str:
        f_x_0 = eval(func)
    else:
        f_x_0 = func(x)

    if round(f_x_0, 1) == round(f_x_0, 2):
        f_x_0 = f"{f_x_0:.1f}"
    else:
        f_x_0 = f"{f_x_0:.2f}"

    pre_res_1 = f_x_0_der + " * x "

    if pre_res_1[0] == "-":
        pre_res_1 = "- " + pre_res_1[1:]

    pre_res_2 = float(f_x_0) - float(f_x_0_der) * x_0

    if round(pre_res_2, 1) == round(pre_res_2, 2):
        pre_res_2 = f"{pre_res_2:.1f}"
    else:
        pre_res_2 = f"{pre_res_2:.2f}"

    if str(pre_res_2)[0] == "-":
        pre_res_2 = "- " + str(pre_res_2)[1:]
    else:
        pre_res_2 = "+ " + str(pre_res_2)

    result = pre_res_1 + pre_res_2

    return result


# def get_root(func, num1, num2):
#     """
#     (function or str, number, number) -> (number)

#     Compute and return root of the function func in the interval (num1, num2).

#     >>> get_root('x', -1, 1)
#     0.0
#     >>> get_root(lambda x: x, -1, 1)
#     0.0
#     """
#     pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
