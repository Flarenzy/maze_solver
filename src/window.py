from tkinter import BOTH
from tkinter import Canvas
from tkinter import Tk

from src.shapes import Line


class Window:
    """A window class.
    """
    def __init__(self, width: int, height: int) -> None:
        """Constructor
        :param width: The width of the window.
        :param height: The height of the window.

        :return: None.
        """
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self._is_running = False

    def redraw(self: 'Window') -> None:
        """Updates the current window by redrawing everything.
        """
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self: 'Window') -> None:
        """Wait for window to close.
        """
        self._is_running = True
        while self._is_running:
            self.redraw()

    def close(self: 'Window') -> None:
        """Closes the window.
        """
        self._is_running = False

    def draw(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)
