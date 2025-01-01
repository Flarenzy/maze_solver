import logging
from tkinter import Canvas


logger = logging.getLogger(__name__)


class Point:
    """Simple 2D coordinate with x and y.
    """
    def __init__(self, x: float, y: float) -> None:
        if x is None or y is None:
            raise TypeError("Point.__init__() is missing 2 required "
                            "positional arguments: 'x' and 'y'.")
        self.x = x
        self.y = y

    def __eq__(self: 'Point', other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x == other.x and self.y == other.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Line:
    """Line consisting of two 'Point's.
    """
    def __init__(self, point1: Point, point2: Point) -> None:
        if not point1 or not point2:
            raise TypeError("Line.__init__() is missing 2 required "
                            "positional arguments: 'point1' and 'point2'.")
        self.point1 = point1
        self.point2 = point2

    def __eq__(self: 'Line', other: object) -> bool:
        if not isinstance(other, Line):
            return NotImplemented
        return (self.point1 == other.point1
                and self.point2 == other.point2)

    def __repr__(self) -> str:
        return f"Line({self.point1}, {self.point2})"

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        logger.info(f"Drawing line with x1={self.point1.x}, y1={self.point1.x}"
                    f" and x2={self.point2.x}, y2={self.point2.y}")
        canvas.create_line(self.point1.x, self.point1.y,
                           self.point2.x, self.point2.y,
                           fill=fill_color, width=2)
