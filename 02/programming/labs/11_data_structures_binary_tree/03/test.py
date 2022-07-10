"""
Board class
"""


class Board:
    """
    Board class that contains board and processes every mechanic of the game
    """

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.last_turn = None

    def __str__(self):
        output = ""
        signs = []
        for row in range(len(self.board)):
            for col in range(3):
                signs.append(
                    str(self.board[row][col])
                    if str(self.board[row][col]) != " "
                    else "_"
                )
        for i in range(3):
            output += " | ".join(signs[3 * i : 3 * (i + 1)]) + "\n"
        return output[:-1]

    def get_status(self):
        """
        Method to check if the game ended (4 possible outputs: 'x', '0', 'draw',
        'continue')
        @return:
        """
        # Horizontal check
        for row in range(3):
            sign = None
            count = 0
            for col in range(3):
                if (
                    (sign is None and self.board[row][col] == "x")
                    or (sign is None and self.board[row][col] == "0")
                    or sign == self.board[row][col]
                ):
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Vertical check
        for col in range(3):
            sign = None
            count = 0
            for row in range(3):
                if (
                    (sign is None and self.board[row][col] == "x")
                    or (sign is None and self.board[row][col] == "0")
                    or sign == self.board[row][col]
                ):
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Diagonal check
        for set_of_coord in [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]:
            sign = None
            count = 0
            for row, col in set_of_coord:
                if (
                    (sign is None and self.board[row][col] == "x")
                    or (sign is None and self.board[row][col] == "0")
                    or sign == self.board[row][col]
                ):
                    sign = self.board[row][col]
                    count += 1
                else:
                    continue
            if count == 3:
                return sign

        # Draw check
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return "continue"
        return "draw"

    def make_move(self, position, turn):
        """
        Method for players moves
        @param position:
        @param turn:
        @return:
        """
        if (
            not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or position[0] > 2
            or position[0] < 0
            or position[1] > 2
            or position[1] < 0
        ):
            raise IndexError
        if self.board[position[0]][position[1]] == " ":
            self.board[position[0]][position[1]] = turn
            self.last_turn = (position[0], position[1])
        else:
            raise IndexError
        return self

    @staticmethod
    def get_moves(board):
        """
        Function that returns two moves, that are sorted by the Y coordinate,
        then by X coordinate
        @param board:
        @return:
        """
        lister = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    lister.append((row, col))
        return lister

    def make_computer_move(self):
        """
        Function that makes move of computer
        @return:
        """
        decision_tree = LinkedBinaryTree(self)

        def recurse_create(root, turn="0"):
            if root.value.get_status() != "continue":
                returns = {"0": 1, "x": -1, "draw": 0}
                return returns[root.value.get_status()]
            moves = Board.get_moves(root.value.board)
            for move in moves:
                root.insert(
                    recurse_create(
                        Node(copy.deepcopy(root.value).make_move(move, turn)),
                        "0" if turn == "x" else "x",
                    )
                )
            return root

        def recurse_sum(root):
            """
            Fuction that sums the leaves of bin tree
            @param root:
            @return:
            """
            if root is None:
                return 0
            if isinstance(root, int):
                return root
            else:
                return sum([recurse_sum(elem) for elem in root.childs])

        recurse_create(decision_tree.key)
        moves = list(enumerate(decision_tree.key.childs))
        for ind in range(len(moves)):
            moves[ind] = [
                moves[ind][0],
                moves[ind][1],
                -recurse_sum(moves[ind][1]),
                moves[ind][1].height() if not isinstance(moves[ind][1], int) else 1,
            ]
        moves = sorted(moves, key=lambda x: x[2])
        moves = sorted(moves, key=lambda x: x[3])
        go = True
        for move in moves:
            if move[3] == 1 and go:
                self.make_move(Board.get_moves(self.board)[move[0]], "0")
                go = False
        if go:
            self.make_move(Board.get_moves(self.board)[moves[0][0]], "0")


if __name__ == "__main__":
    test = Board()
    test.make_move((0, 0), "0")
    print(test.get_status())
    test.make_move((0, 1), "x")
    print(test.get_status())
    test.make_move((0, 2), "0")
    print(test.get_status())
    test.make_move((1, 0), "0")
    print(test.get_status())
    test.make_move((1, 1), "x")
    print(test.get_status())
    test.make_move((1, 2), "0")
    print(test.get_status())
    test.make_move((2, 0), "x")
    print(test.get_status())
    test.make_move((2, 1), "0")
    print(test.get_status())
    test.make_move((2, 2), "x")
    print(test.get_status())

    test = Board()
    test.make_move((0, 0), "0")
    print(test.get_status())
    test.make_move((0, 1), "0")
    print(test.get_status())
    test.make_move((0, 2), "0")
    print(test.get_status())
    test.make_move((1, 0), "x")
    print(test.get_status())
    test.make_move((1, 1), "x")
    print(test.get_status())
    test.make_move((1, 2), "x")
    print(test.get_status())
    test.make_move((2, 0), "x")
    print(test.get_status())
    test.make_move((2, 1), "0")
    print(test.get_status())
    test.make_move((2, 2), "x")
    print(test.get_status())

    test = Board()
    test.make_move((0, 0), "0")
    print(test.get_status())
    test.make_move((0, 1), "0")
    print(test.get_status())
    test.make_move((0, 2), "0")
    print(test.get_status())
    test.make_move((1, 0), "x")
    print(test.get_status())
    test.make_move((1, 1), "x")
    print(test.get_status())
    test.make_move((1, 2), "x")
    print(test.get_status())
    test.make_move((2, 0), "0")
    print(test.get_status())
    test.make_move((2, 1), "0")
    print(test.get_status())
    test.make_move((2, 2), "0")
    print(test.get_status())
