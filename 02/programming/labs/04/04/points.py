"""Points."""


class Point:
    """2D Point."""

    def __init__(self, x, y):
        """
        Receives information.
        >>> my_point = Point(2, 5)
        >>> my_point.x
        2
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Bried information.
        >>> my_point = Point(2, 5)
        >>> print(my_point)
        Point in two-dimensional space with coordinates (2, 5)
        """
        if "z" in list(self.__dict__):
            return f"Point in three-dimensional space with coordinates {self.x, self.y, self.z}"
        return f"Point in two-dimensional space with coordinates {self.x, self.y}"

    def vector_length(self):
        """
        Vector length.
        >>> my_point = Point(2, 5)
        >>> my_point.vector_length()
        5.39
        """
        if "z" in list(self.__dict__):
            return round((self.x**2 + self.y**2 + self.z**2) ** (1 / 2), 2)
        return round((self.x**2 + self.y**2) ** (1 / 2), 2)

    def __repr__(self):
        """
        Returns info in required format.
        >>> my_point = Point(2, 5)
        >>> my_point
        Point(x=2, y=5)
        """
        if "z" in list(self.__dict__):
            return f"Point(x={self.x}, y={self.y}, z={self.z})"
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, obj):
        """
        Checks for equality.
        >>> Point(3, 4) == Point(3, 4)
        True
        """
        if self.vector_length() == obj.vector_length():
            return True
        else:
            return False


class Point3D(Point):
    """3D Point."""

    def __init__(self, x, y, z=0):
        """
        Receives information.
        >>> my_point3d = Point3D(2, 5, 6)
        >>> my_point3d.z
        6
        """
        super().__init__(x, y)
        self.z = z


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
    point1 = Point(17, 2)
    assert (point1.y, point1.x) == (2, 17)
    assert str(point1) == "Point in two-dimensional space with coordinates (17, 2)"

    point2 = Point3D(17, 4, 2)
    assert (point2.y, point2.z, point2.x) == (4, 2, 17)
    assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
    assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"

    assert Point(3, 4) == Point(3, 4)
    assert Point(3, 4) != Point(2, 3)

    assert Point(5, 4) == Point3D(5, 4, 0)
    assert Point3D(5, 4, 0) == Point(5, 4)

    assert Point(5, 4) != Point3D(5, 4, 1)
    assert Point3D(5, 4, 1) != Point(5, 4)

    assert Point3D(8, 7, 0) == Point3D(8, 7)

    assert Point(3, 4).vector_length() == 5
    assert Point(4, 5).vector_length() == 6.4
    assert Point(6, -12).vector_length() == 13.42
    assert Point(100, 0).vector_length() == 100

    assert Point3D(-6, -12, 0).vector_length() == 13.42, Point3D(
        -6, -12, 0
    ).vector_length()
    assert Point3D(3, 4, 12).vector_length() == 13
    assert Point3D(-13, 14, -15).vector_length() == 24.29
