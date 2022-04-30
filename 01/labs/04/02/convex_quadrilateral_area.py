def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """main function that outputs result

    Args:
        k1 (float): variable
        c1 (float): variable
        k2 (float): variable
        c2 (float): variable
        k3 (float): variable
        c3 (float): variable
        k4 (float): variable
        c4 (float): variable
    """

    x1, y1 = lines_intersection(k1, c1, k2, c2)
    x2, y2 = lines_intersection(k2, c2, k3, c3)
    x3, y3 = lines_intersection(k3, c3, k4, c4)
    x4, y4 = lines_intersection(k4, c4, k1, c1)

    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x4, y4)
    d = distance(x4, y4, x1, y1)
    f1 = distance(x1, y1, x3, y3)
    f2 = distance(x2, y2, x4, y4)

    result = quadrangle_area(a, b, c, d, f1, f2)

    return round(result, 2)


def lines_intersection(k1, c1, k2, c2):
    """function that returns us line intersection coordinates

    Args:
        k1 (float): variable
        c1 (float): variable
        k2 (float): variable
        c2 (float): variable

    Returns:
        tuple : result
    """

    if k1 == k2:
        return None

    xcord = (c2-c1)/(k1-k2)
    ycord = k1 * xcord + c1

    return round(xcord, 2), round(ycord, 2)


def distance(x1, y1, x2, y2):
    """function that returns distance

    Args:
        x1 (float): variable
        y1 (float): variable
        x2 (float): variable
        y2 (float): variable

    Returns:
        float: result
    """

    length = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

    return round(length, 2)


def quadrangle_area(a, b, c, d, f1, f2):
    """function that calculates area

    Args:
        a (float): variable
        b (float): variable
        c (float): variable
        d (float): variable
        f1 (float): variable
        f2 (float): variable

    Returns:
        float: result
    """

    if a <= 0 or b <= 0 or c <= 0:
        return None
    if d <= 0 or f1 <= 0 or f2 <= 0:
        return None
    if (4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)) <= 0:
        return None
    S = ((4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2)**(1/2))/4
    return round(S, 2)
