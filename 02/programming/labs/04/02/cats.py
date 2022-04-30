"""Cats."""


class Animal:
    """Animal."""

    def __init__(self, phylum, clas):
        """
        Receives information.
        >>> animal1 = Animal("chordata", "mammalia")
        >>> animal1.phylum == "chordata"
        True
        """
        self.phylum = phylum
        self.clas = clas

    def __str__(self):
        """
        Brief information.
        >>> animal1 = Animal("chordata", "mammalia")
        >>> print(animal1)
        <animal class is mammalia>
        """
        return f"<animal class is {self.clas}>"

    def __eq__(self, animal):
        """
        Checks whether animals are equal.
        >>> animal1 = Animal("a", "b")
        >>> animal2 = Animal("a", "b")
        >>> assert animal1 == animal2
        """
        if self.phylum == animal.phylum and self.clas == animal.clas:
            return True
        return False


class Cat(Animal):
    """Cat."""

    def __init__(self, phylum, clas, genus):
        """
        Receives information.
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> cat1.phylum
        'chordata'
        """
        super().__init__(phylum, clas)
        self.genus = genus

    def sound(self):
        """
        Cat's sound.
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> cat1.sound()
        'Meow'
        """
        return "Meow"

    def __str__(self):
        """
        Brief information.
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> print(cat1)
        <This felis animal class is mammalia>
        """
        return f"<This {self.genus} animal class is {self.clas}>"


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
