import unicurses as curses

from Arcanoid.color_themes import init_color_themes, PLATFORM_DESC_COLOR

def main(stdscr):
    curses.start_color()
    init_color_themes()

    curses.curs_set(0)
    curses.move(0, 0)
    
    while 1:
        curses.clear()
        y, x = curses.getmaxyx(stdscr)
        curses.addstr(f"{x} {y}", (PLATFORM_DESC_COLOR))
        curses.refresh()
        curses.napms(100)

curses.wrapper(main)
