"""Triangle visualization."""

import point


class Triangle:
    """Triangle class."""

    def __init__(self, point_1, point_2, point_3):
        """
        Takes info about triangle.
        >>> triangle = Triangle(point.Point(1,1), \
point.Point(3,1), point.Point(2,3))
        >>> triangle.point_1.x
        1
        """
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def is_triangle(self):
        """
        Checks if figure is triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), \
point.Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        vector_1, vector_2, vector_3 = vector(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            self.point_3.x,
            self.point_3.y,
        )
        if (
            vector_1 >= vector_2 + vector_3
            or vector_2 >= vector_1 + vector_3
            or vector_3 >= vector_1 + vector_2
            or vector_1 <= 0
            or vector_2 <= 0
            or vector_3 <= 0
        ):
            return False
        return True

    def perimeter(self):
        """
        Measures perimeter of the triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        vector_1, vector_2, vector_3 = vector(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            self.point_3.x,
            self.point_3.y,
        )
        return vector_1 + vector_2 + vector_3

    def area(self):
        """
        Measures area of the triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        """
        vector_1, vector_2, vector_3 = vector(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            self.point_3.x,
            self.point_3.y,
        )
        return 0.25 * (
            (vector_1 + vector_2 + vector_3)
            * (vector_2 + vector_3 - vector_1)
            * (vector_1 + vector_3 - vector_2)
            * (vector_1 + vector_2 - vector_3)
        ) ** (1 / 2)


def vector(x1_coord, y1_coord, x2_coord, y2_coord, x3_coord, y3_coord):
    """
    Measures lenght of vector.
    >>> print(vector(1,1,2,2,3,3))
    (1.4142135623730951, 1.4142135623730951, 2.8284271247461903)
    """
    measure = lambda x1_coord, y1_coord, x2_coord, y2_coord: (
        (x2_coord - x1_coord) ** 2 + (y2_coord - y1_coord) ** 2
    ) ** (1 / 2)
    vector_1 = measure(x1_coord, y1_coord, x2_coord, y2_coord)
    vector_2 = measure(x2_coord, y2_coord, x3_coord, y3_coord)
    vector_3 = measure(x3_coord, y3_coord, x1_coord, y1_coord)
    return vector_1, vector_2, vector_3


fix = point.Point(1, 1)
if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
