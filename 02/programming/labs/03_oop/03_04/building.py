"""Academic building module."""
import classroom


class AcademicBuilding:
    """Class for academic building."""

    def __init__(self, address: str, classrooms: list):
        """
        Information about academic building.
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC',\
        'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC',\
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
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        """
        Returns total equipment in academic building.
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC',\
        'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC',\
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
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC',\
        'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC',\
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


fix = classroom.Classroom("007", 12, ["TV"])
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
