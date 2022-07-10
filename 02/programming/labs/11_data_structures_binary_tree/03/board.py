"""Board."""


class Board:
    """Board."""

    def __init__(self):
        """Receives information."""
        self.last_move = None
        field = []
        for line in range(3):
            temp = []
            for column in range(3):
                line, column = column, line
                temp.append(" ")
            field.append(temp)
        self.field = field

    def __str__(self):
        """Returns visualization of field."""
        output = []
        for line in self.field:
            output.append(str(line))
        return str("\n".join(output))

    def get_status(self):
        """Checks current status of the board."""

        left = [(0, 0), (1, 1), (2, 2)]
        right = [(0, 2), (1, 1), (2, 0)]
        result = None

        for _ in range(3):
            if (
                self.field[_][0] == "x"
                and self.field[_][1] == "x"
                and self.field[_][2] == "x"
            ):
                result = "x"
            if (
                self.field[_][0] == "0"
                and self.field[_][1] == "0"
                and self.field[_][2] == "0"
            ):
                result = "0"

        if result:
            return result

        for _ in range(3):
            if (
                self.field[0][_] == "x"
                and self.field[1][_] == "x"
                and self.field[2][_] == "x"
            ):
                result = "x"
            if (
                self.field[0][_] == "0"
                and self.field[1][_] == "0"
                and self.field[2][_] == "0"
            ):
                result = "0"

        if result:
            return result

        counter = 0
        for line, column in left:
            if self.field[line][column] == "x":
                counter += 1
        if counter == 3:
            result = "x"

        counter = 0
        for line, column in right:
            if self.field[line][column] == "x":
                counter += 1
        if counter == 3:
            result = "x"

        counter = 0
        for line, column in left:
            if self.field[line][column] == "0":
                counter += 1
        if counter == 3:
            result = "0"

        counter = 0
        for line, column in right:
            if self.field[line][column] == "0":
                counter += 1
        if counter == 3:
            result = "0"

        if result:
            return result

        for line in range(3):
            for column in range(3):
                if self.field[line][column] == " ":
                    return "continue"
        return "draw"

    def make_move(self, position, turn):
        """Makes movement."""
        if turn not in ["x", "0"]:
            raise IndexError
        if position[0] not in range(3) or position[1] not in range(3):
            raise IndexError
        if self.field[position[0]][position[1]] == " ":
            self.field[position[0]][position[1]] = turn
            self.last_move = position
        else:
            raise IndexError

    def make_computer_move(self):
        """Computer makes move."""


if __name__ == "__main__":
    pass
