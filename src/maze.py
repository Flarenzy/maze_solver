import logging
import time
import random
from typing import Optional

from src.cell import Cell
from src.window import Window


logger = logging.getLogger(__name__)


class Maze:
    def __init__(self, x1: float, y1: float,
                 num_rows: int, num_cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Optional[Window] = None,
                 seed: Optional[int] = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            logger.info(f"Seeding random with seed:{seed}")
            random.seed(seed)

    def _create_cells(self) -> list[list[Cell]]:
        return [[Cell() for _ in range(self.num_rows)]
                for _ in range(self.num_cols)]

    def _draw_cell(self, i: int, j: int) -> None:
        cell: Cell = self._cells[i][j]
        x0 = self.x1 + i * self.cell_size_x
        y0 = self.y1 + j * self.cell_size_y
        x1 = x0 + self.cell_size_x
        y2 = y0 + self.cell_size_y
        cell.draw(x0, y0, x1, y2)
        self._animate()

    def _draw_cells(self) -> None:
        if self.win is None:
            raise AttributeError("Missing window to draw on!")
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].set_window(self.win)
                self._draw_cell(i, j)

    def _animate(self) -> None:
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def draw_maze(self) -> None:
        self._cells: list[list[Cell]] = self._create_cells()
        self._draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        logger.info("Created maze.")

    def _break_entrance_and_exit(self) -> None:
        if not self._cells:
            return
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        n = self.num_cols - 1
        m = self.num_rows - 1
        self._cells[n][m].has_bottom_wall = False
        self._draw_cell(n, m)

    def _break_walls_r(self, i: int, j: int) -> None:
        if not self._cells:
            return
        logger.debug(f"Breaking wall of cell at {i} {j}")
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            posible_dir = []
            direction_to_index = {
                "top": (i, j - 1),
                "bottom": (i, j + 1),
                "left": (i - 1, j),
                "right": (i+1, j),
            }
            if i + 1 < self.num_cols and j < self.num_rows:
                if not self._cells[i + 1][j].visited:
                    to_visit.extend([i+1, j])
                    posible_dir.append("right")
            if i - 1 >= 0 and j >= 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.extend([i - 1, j])
                    posible_dir.append("left")
            if i < self.num_cols and j + 1 < self.num_rows:
                if not self._cells[i][j + 1].visited:
                    to_visit.extend([i, j + 1])
                    posible_dir.append("bottom")
            if i < self.num_cols and j - 1 > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.extend([i, j - 1])
                    posible_dir.append("top")
            if not to_visit:
                self._draw_cell(i, j)
                break
            direction = random.choice(posible_dir)
            self._cells[i][j].knock_down_wall(direction)
            self._break_walls_r(direction_to_index[direction][0],
                                direction_to_index[direction][1])
            # direction = random.choice()

    def _reset_cells_visited(self) -> None:
        if not self._cells:
            return
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
        logger.info("Reset all cells visited property to False")
