"""Building."""


class Building:
    """Building."""

    def __init__(self, address):
        """
        Receives information.
        >>> my_building = Building("James")
        >>> my_building.address
        'James'
        """
        self.address = address


class House(Building):
    """House."""

    def __init__(self, address, flats):
        """
        Receives information.
        >>> my_house = House("Clara", [1, 2, 3, 4, 5])
        >>> my_house.address
        'Clara'
        """
        super().__init__(address)
        self.flats = flats


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


class AcademicBuilding(Building):
    """Class for academic building."""

    def __init__(self, address: str, classrooms: list):
        """
        Information about academic building.
        >>> classroom_016 = Classroom('016', 80, ['PC',\
        'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC',\
        'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', \
        classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        >>> for room in building.classrooms:
        ...     print(room)
        Classroom 016 has a capacity of 80 persons and has the \
following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the \
following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the \
following equipment: PC, projector.
        """
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        Returns total equipment in academic building.
        >>> classroom_016 = Classroom('016', 80, ['PC',\
        'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC',\
        'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> len(building.total_equipment())
        4
        """
        data = {}
        for room in self.classrooms:
            for _ in room.equipment:
                if _ not in data:
                    data[_] = 1
                else:
                    data[_] += 1
        return list(data.items())

    def __str__(self):
        """
        Returns information about academic building.
        >>> classroom_016 = Classroom('016', 80, ['PC',\
        'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC',\
        'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the \
following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the \
following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the \
following equipment: PC, projector.
        """
        data = [self.address]
        for _ in self.classrooms:
            data.append(_.__str__())
        data = "\n".join(data)
        return f"{data}"


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
