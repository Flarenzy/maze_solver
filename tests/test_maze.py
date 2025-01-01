import pytest

from src.constants import CELL_SIZE_X
from src.constants import CELL_SIZE_Y
from src.constants import MAZE_COLUMNS
from src.constants import MAZE_ROWS
from src.constants import MAZE_X_COORDINATE
from src.constants import MAZE_Y_COORDINATE
from src.maze import Maze


def test_maze_atrs():
    maze = Maze(MAZE_X_COORDINATE, MAZE_Y_COORDINATE,
                MAZE_ROWS, MAZE_COLUMNS,
                CELL_SIZE_X, CELL_SIZE_Y)
    assert maze.x1 == MAZE_X_COORDINATE
    assert maze.y1 == MAZE_Y_COORDINATE
    assert maze.num_cols == MAZE_COLUMNS
    assert maze.num_rows == MAZE_ROWS
    assert maze.cell_size_x == CELL_SIZE_X
    assert maze.cell_size_y == CELL_SIZE_Y
