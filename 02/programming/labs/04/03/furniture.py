"""Furniture."""


class Furniture:
    """Furniture."""

    def __init__(self, style, assign):
        """
        Receives information.
        >>> my_furniture = Furniture("empire", "bedroom")
        >>> my_furniture.style
        'empire'
        """
        self.style = style
        self.assign = assign

    def __str__(self):
        """
        Brief information.
        >>> my_furniture = Furniture("empire", "bedroom")
        >>> print(my_furniture)
        <furniture style is empire>
        """
        return f"<furniture style is {self.style}>"

    def __eq__(self, object):
        """
        Checks whether objects are similar.
        >>> furniture1 = Furniture("a", "b")
        >>> furniture2 = Furniture("a", "b")
        >>> assert furniture1 == furniture2
        """
        if self.style == object.style and self.assign == object.assign:
            return True
        return False


class Chair(Furniture):
    """Chair."""

    def __init__(self, style, assign, tipe):
        """
        Receives information.
        >>> my_chair = Chair("empire", "bedroom", "armchair")
        >>> my_chair.tipe
        'armchair'
        """
        super().__init__(style, assign)
        self.tipe = tipe

    def __str__(self):
        """
        Brief information.
        >>> my_chair = Chair("empire", "bedroom", "armchair")
        >>> print(my_chair)
        <This armchair furniture style is empire>
        """
        return f"<This {self.tipe} furniture style is {self.style}>"

    def get_assign(self):
        """
        Returns assignment.
        >>> my_chair = Chair("empire", "bedroom", "armchair")
        >>> my_chair.get_assign()
        'bedroom'
        """
        return self.assign


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
