"""Points module."""


class Point:
    """Point class."""

    def __init__(self, x, y):
        """
        Receives coordinates.
        >>> dot = Point(3, 1)
        >>> dot.x
        3
        """
        self.x = x
        self.y = y


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
