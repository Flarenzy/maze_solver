"""Main module."""
from window import Window


def main() -> int:
    win = Window(800, 800)
    win.wait_for_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
