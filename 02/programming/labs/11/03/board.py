"""Board."""
from btree import Tree
from btnode import Node
from copy import deepcopy
from sys import setrecursionlimit

setrecursionlimit(100000)


class Board:
    """Board."""

    score = {"0": 1, "x": -1, "draw": 0}

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
        if position[0] not in range(3) or position[1] not in range(3):
            raise IndexError
        if turn not in ["x", "0"]:
            raise TypeError
        if self.field[position[0]][position[1]] != " ":
            raise IndexError
        self.field[position[0]][position[1]] = turn

    def make_computer_move(self):
        """Makes computer movement."""
        my_turn = "0"
        tree = Tree(self)

        def variants(field):
            """Finds two moves."""
            movements = []
            for row in range(3):
                for column in range(3):
                    if field[row][column] == " ":
                        movements.append((row, column))
                        if len(movements) == 2:
                            return movements
            return movements

        def tree_creator(root, turn="0"):
            """Recursively creates binary search tree."""

            game_status = root.value.get_status()
            possible = variants(root.value.board)

            if len(possible) == 0:
                return "draw"

            elif game_status == "continue":
                return self.score[game_status]

            elif len(possible) >= 1:
                if turn == "x":
                    root.left = tree_creator(
                        Node(deepcopy(root.value).make_move(possible[0], turn)), turn
                    )
                else:
                    root.left = tree_creator(
                        Node(deepcopy(root.value).make_move(possible[0], turn)), "x"
                    )

            if len(possible) == 2:
                if turn == "x":
                    root.right = tree_creator(
                        Node(deepcopy(root.value).make_move(possible[1], turn)), turn
                    )
                else:
                    root.right = tree_creator(
                        Node(deepcopy(root.value).make_move(possible[1], turn)), "x"
                    )

        tree_creator(tree.key)

        def points_counter(root):
            """Counts points."""
            if type(root) == int:
                return root

            if not root:
                return 0

            return points_counter(root.left) + points_counter(root.right)

        if type(tree.key.left) == int and tree.key.left == 1:
            self.make_move(variants(self.board)[0], my_turn)

        elif type(tree.key.left) == int and tree.key.right == 1:
            self.make_move(variants(self.board)[1], my_turn)

        else:
            if points_counter(tree.key.right) < points_counter(tree.key.left):
                self.make_move(variants(self.board)[0], my_turn)
            else:
                self.make_move(variants(self.board)[1], my_turn)


if __name__ == "__main__":
    test = Board()
    test.make_move((2, 2), "x")
    test.make_move((1, 1), "0")
    test.make_move((1, 2), "x")
    test.make_computer_move()
    print(test)
