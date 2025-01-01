import logging

from src.window import Window
from src.shapes import Line
from src.shapes import Point
from src.constants import CELL_LINE_COLOR
from src.constants import MOVE_COLOR
from src.constants import MOVE_COLOR_UNDO


logger = logging.getLogger(__name__)


class Cell:
    """Grid cell's on a canvas. Can have all or none 4 walls.
    """
    def __init__(self, has_left_wall: bool = True,
                 has_right_wall: bool = True,
                 has_bottom_wall: bool = True,
                 has_top_wall: bool = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_top_wall = has_top_wall
        self._x1 = None  # top left coordinates
        self._y1 = None
        self._x2 = None  # top right coordinates
        self._y2 = None
        self._win = None

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if not self._x1:
            self._x1 = x1
            self._y1 = y1
            self._x2 = x2
            self._y2 = y2
        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw(line, CELL_LINE_COLOR)
        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            line = Line(p1, p2)
            logger.info(f"left wall line:{line}")
            self._win.draw(line, CELL_LINE_COLOR)
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw(line, CELL_LINE_COLOR)
        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            line = Line(p1, p2)
            self._win.draw(line, CELL_LINE_COLOR)

    def set_window(self, win: Window) -> None:
        self._win = win

    def draw_move(self, to_cell: 'Cell', undo: bool = False) -> None:
        center_x = self._x2 - (self._x2 - self._x1) / 2
        center_y = self._y2 - (self._y2 - self._y1) / 2
        other_center_x = to_cell._x2 - (to_cell._x2 - to_cell._x1) / 2
        other_center_y = to_cell._y2 - (to_cell._y2 - to_cell._y1) / 2
        logger.info(f"self: {self._x1}, {self._y1}, {self._x2}, {self._y2}")
        logger.info(f"other: {to_cell._x1}, {to_cell._y1}, {to_cell._x2}, {to_cell._y2}")
        logger.info(f"center: {center_x}, {center_y}\n"
                    f"other: {other_center_x}, {other_center_y}")
        p1 = Point(center_x, center_y)
        p2 = Point(other_center_x, other_center_y)
        clr = MOVE_COLOR if not undo else MOVE_COLOR_UNDO
        self._win.draw(Line(p1, p2), clr)
