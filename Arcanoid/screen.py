import unicurses as curses

from Arcanoid.color_themes import init_color_themes, PLATFORM_DESC_COLOR
from Arcanoid.platform_desk import PlatformDesk


def main(stdscr):
    curses.start_color()
    init_color_themes()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.nodelay(stdscr, True) # позволяет использовать getch без блокирования программы
    curses.keypad(stdscr, True)  # Позволяет считывать специальные клавиши, такие как стрелки

    height, width = curses.getmaxyx(stdscr)
    platform_desk = PlatformDesk(width//2-1)

    while 1:
        height, width = curses.getmaxyx(stdscr)
        curses.clear()
        key = curses.getch()
        if key in [ord('a'), ord('A'), curses.KEY_LEFT]:
            platform_desk.move(-1, width)
        elif key in [ord('d'), ord('D'), curses.KEY_RIGHT]:
            platform_desk.move(1, width)
        curses.move(height-1, platform_desk.x)
        curses.addstr(str(platform_desk), PLATFORM_DESC_COLOR)
        curses.refresh()
        curses.napms(10)

curses.wrapper(main)
