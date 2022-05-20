"""Game."""
from board import Board
import sys


def main():
    """Game loop."""
    board = Board()
    while True:
        decision = turn(board)
        board.make_move(decision, "x")
        print(board)
        board_status(board.get_status())
        # board.make_computer_move()
        # board_status(board.get_status())


def board_status(status):
    """Checks board's status."""
    if status == "draw":
        print("Draw!")
        sys.exit()
    elif status == "x":
        print("Winner: 'x'!")
        sys.exit()
    elif status == "0":
        print("Winner: '0'!")
        sys.exit()


def turn(board):
    """Gets user's input."""

    def get_row():
        """Gets row."""
        print("Enter row:")
        row = input(">>> ")
        if row not in ["0", "1", "2"]:
            print("Wrong input.")
            return get_row()
        return int(row)

    def get_column():
        """Gets column"""
        print("Enter column:")
        column = input(">>> ")
        if column not in ["0", "1", "2"]:
            print("Wrong input.")
            return get_column()
        return int(column)

    row = get_row()
    column = get_column()

    if board.field[row][column] != " ":
        print("Wrong input.")
        return turn(board)

    return (row, column)


if __name__ == "__main__":
    main()
