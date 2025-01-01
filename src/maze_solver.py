import logging

from src.constants import CELL_SIZE_X
from src.constants import CELL_SIZE_Y
from src.constants import MAZE_COLUMNS
from src.constants import MAZE_ROWS
from src.constants import MAZE_X_COORDINATE
from src.constants import MAZE_Y_COORDINATE
from src.constants import WINDOW_HEIGHT
from src.constants import WINDOW_WIDTH
from src.maze import Maze
from src.window import Window

logger = logging.getLogger(__name__)
logging.basicConfig(filename="maze_solver.log", level=logging.INFO)


def main() -> int:
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    maze = Maze(MAZE_X_COORDINATE, MAZE_Y_COORDINATE,
                MAZE_ROWS, MAZE_COLUMNS,
                CELL_SIZE_X, CELL_SIZE_Y, win)
    maze.draw_maze()
    win.wait_for_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
