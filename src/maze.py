import logging
import time
from typing import Optional

from src.cell import Cell
from src.window import Window


logger = logging.getLogger(__name__)


class Maze:
    def __init__(self, x1: float, y1: float,
                 num_rows: int, num_cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Optional[Window] = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

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
