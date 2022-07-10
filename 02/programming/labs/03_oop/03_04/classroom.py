"""Classrom module."""


class Classroom:
    """Class for classroom."""

    def __init__(self, number: str, capacity: int, equipment: list):
        """
        Information about classroom.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.capacity
        80
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """
        Brief information about classroom.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the \
following equipment: PC, projector, mic.
        """
        return f"Classroom {self.number} has a capacity of {self.capacity}\
 persons and has the following equipment: {', '.join(self.equipment)}."

    def is_larger(self, compare):
        """
        Checks if capacity is bigger.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        if self.capacity > compare.capacity:
            return True
        return False

    def equipment_differences(self, compare):
        """
        Finds different equipment.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> len(classroom_016.equipment_differences(classroom_007)) == 3
        True
        """
        return list(set(self.equipment) - set(compare.equipment))

    def __repr__(self):
        """
        Returns text in required format.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        """
        return f"""Classroom('{self.number}', {self.capacity}, \
[{', '.join(list(map(lambda x: f"'{x}'", self.equipment)))}])"""


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
