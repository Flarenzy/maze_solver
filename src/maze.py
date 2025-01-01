import time

from src.cell import Cell
from src.window import Window


class Maze:
    def __init__(self, x1: float, y1: float,
                 num_rows: int, num_cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Window) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = self._create_cells()
        self._draw_cells()

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
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].set_window(self.win)
                self._draw_cell(i, j)

    def _animate(self) -> None:
        self.win.redraw()
        time.sleep(0.01)
