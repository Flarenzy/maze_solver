import random

from src.window import Window
from src.shapes import Line
from src.shapes import Point


def main() -> int:
    win = Window(800, 800)
    lst: list[Line] = []
    clr = "red"
    for _ in range(20):
        p1 = Point(random.randrange(1, 800), random.randrange(1, 800))
        p2 = Point(random.randrange(1, 800), random.randrange(1, 800))
        lst.append(Line(p1, p2))
    for line in lst:
        win.draw(line, clr)
        if clr == "red":
            clr = "blue"
        else:
            clr = "red"
    win.wait_for_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
