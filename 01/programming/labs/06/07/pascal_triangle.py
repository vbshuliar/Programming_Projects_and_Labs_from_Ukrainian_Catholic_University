"""module that generates pascal triangle
"""


def generate_pascal_triangle(number1):
    """generates pascal triangle
    >>> print(generate_pascal_triangle(5))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    list_pascal = []
    for levels in range(number1):
        temp_list = []
        counter = 1
        while counter <= levels + 1:
            temp_list.append(1)
            counter += 1
        list_pascal.append(temp_list)
    for num1 in range(len(list_pascal)):
        for num2 in range(len(list_pascal[num1])):
            if num2 == 0:
                list_pascal[num1][num2] = 1
            else:
                try:
                    list_pascal[num1][num2] = list_pascal[num1 -
                                                          1][num2-1] + list_pascal[num1-1][num2]
                except IndexError:
                    list_pascal[num1][num2] = 1
    return list_pasca
