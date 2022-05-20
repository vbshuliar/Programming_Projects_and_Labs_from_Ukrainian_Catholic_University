"""Board."""


class Board:
    """Board."""

    def __init__(self):
        """Receives information."""
        self.last_move = None
        field = []
        for row in range(3):
            temp = []
            for column in range(3):
                temp.append(" ")
            field.append(temp)
        self.field = field

    def __repr__(self):
        """Returns visualization of field."""
        output = []
        for row in self.field:
            output.append(str(row))
        return str("\n".join(output))

    def get_status(self):
        """Checks current status of the board."""
        turns = ["0", "x"]
        left = [(0, 0), (1, 1), (2, 2)]
        right = [(0, 2), (1, 1), (2, 0)]

        for turn in turns:
            for row in range(3):
                counter = 0
                for column in range(3):
                    if self.field[row][column] == turn:
                        counter += 1
                if counter == 3:
                    return turn

        for turn in turns:
            for column in range(3):
                counter = 0
                for row in range(3):
                    if self.field[row][column] == turn:
                        counter += 1
                if counter == 3:
                    return turn

        for turn in turns:
            counter = 0
            for row, column in left:
                if self.field[row][column] == turn:
                    counter += 1
            if counter == 3:
                return turn
            counter = 0
            for row, column in right:
                if self.field[row][column] == turn:
                    counter += 1
            if counter == 3:
                return turn

        for row in range(3):
            for column in range(3):
                if self.field[row][column] == " ":
                    return "continue"
        return "draw"

    def make_move(self, position, turn):
        """Makes movement."""
        if (
            position[0] not in range(3)
            or position[1] not in range(3)
            or turn not in ["x", "0"]
        ):
            raise IndexError
        if self.field[position[0]][position[1]] != " ":
            raise IndexError
        else:
            self.field[position[0]][position[1]] = turn

    def make_computer_move(self):
        """Makes computer movement."""
        


if __name__ == "__main__":
    test = Board()
    test.make_move((2, 2), "x")
    test.make_move((1, 1), "0")
    test.make_move((1, 2), "x")
    test.make_move((1, 0), "x")
    test.make_move((2, 0), "x")
    print(test)
