"""LifeGrid."""
from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """

    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        self._grid = Array2D(num_rows, num_cols)
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for row in range(self._grid.num_rows()):
            for column in range(self._grid.num_cols()):
                self.clear_cell(row, column)
        for _ in coord_list:
            self.set_cell(_[0], _[1])

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return bool(self._grid.__getitem__((row, col)) == self.LIVE_CELL)

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row, col), self.DEAD_CELL)

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row, col), self.LIVE_CELL)

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        alive = 0
        for temp_row in range(self._grid.num_rows()):
            for temp_col in range(self._grid.num_cols()):
                if (
                    temp_row in [row - 1, row + 1]
                    and temp_col in [col - 1, col, col + 1]
                    and self.is_live_cell(temp_row, temp_col)
                ):
                    alive += 1
                elif (
                    temp_row == row
                    and temp_col in [col - 1, col + 1]
                    and self.is_live_cell(temp_row, temp_col)
                ):
                    alive += 1
        return alive

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        data = ""
        for row in range(self._grid.num_rows()):
            for column in range(self._grid.num_cols()):
                data += "L" if self.is_live_cell(row, column) else "D"
            data += "\n" if row != self._grid.num_rows() - 1 else ""
        return data
