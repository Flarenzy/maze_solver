import logging

from src.cell import Cell
from src.constants import WINDOW_HEIGHT
from src.constants import WINDOW_WIDTH
from src.shapes import Point
from src.window import Window

logger = logging.getLogger(__name__)
logging.basicConfig(filename="maze_solver.log", level=logging.INFO)


def main() -> int:
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    cells: list[Cell] = []
    for i in range(4):
        current_p1 = Point(0, i * 50)
        current_p2 = Point(50, (i + 1) * 50)
        logger.info(f"Created points p1:{current_p1} and p2:{current_p2}")
        cell = Cell()
        cell.set_window(win)
        cell.draw(current_p1.x, current_p1.y,
                  current_p2.x, current_p2.y)
        cells.append(cell)
        for j in range(4):
            current_p1.x = j * 50
            current_p2.x = (j + 1) * 50
            logger.info(f"Changed p1:{current_p1} and p2:{current_p2}")
            cell2 = Cell()
            cell2.set_window(win)
            cell2.draw(current_p1.x, current_p1.y,
                       current_p2.x, current_p2.y)
            cells.append(cell2)
    cell1 = cells[0]
    cell1.draw_move(cells[-1], undo=True)
    win.wait_for_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
