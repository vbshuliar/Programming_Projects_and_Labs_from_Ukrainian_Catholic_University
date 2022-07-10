"""LifeGrid 5x5."""
from lifegrid import LifeGrid

INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]
GRID_WIDTH = 5
GRID_HEIGHT = 5
NUM_GENS = 8


def main():
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)


def evolve(grid):
    live_cells = []

    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            neighbors = grid.num_live_neighbors(i, j)

            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

    grid.configure(live_cells)


def draw(grid):
    return str(grid)
