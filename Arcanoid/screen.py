import unicurses as curses

from Arcanoid.color_themes import init_color_themes, PLATFORM_DESC_COLOR, BALL_COLOR
from Arcanoid.platform_desk import PlatformDesk

def redraw_screen(platform_desk: PlatformDesk):
    curses.move(platform_desk.y, platform_desk.x)
    curses.addstr(str(platform_desk), PLATFORM_DESC_COLOR)
    for ball in platform_desk.balls:
        curses.move(ball.y, ball.x)
        curses.addch(str(ball), BALL_COLOR)

def move_balls(width: int, height: int, platform_desk: PlatformDesk):
    check_balls_flag = False
    for ball in platform_desk.balls:
        if ball.y+1 == platform_desk.y and 0 <= ball.x-platform_desk.x < platform_desk.size:
            ball.dy=-abs(ball.dy)
        ball.move(width, height)
        if ball.is_dead:
            check_balls_flag=True
    if check_balls_flag:
        platform_desk.check_balls()

def main(stdscr):
    curses.start_color()
    init_color_themes()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.nodelay(stdscr, True) # позволяет использовать getch без блокирования программы
    curses.keypad(stdscr, True)  # Позволяет считывать специальные клавиши, такие как стрелки

    height, width = curses.getmaxyx(stdscr)
    platform_desk = PlatformDesk(width//2-1, height-1)

    while len(platform_desk.balls)>0:
        height, width = curses.getmaxyx(stdscr)
        curses.clear()
        key = curses.getch()
        if key == curses.KEY_RESIZE:
            platform_desk.change_y_pos(height-1)
        if key == ord(' '):
            platform_desk.launch()
        if key in [ord('a'), ord('A'), curses.KEY_LEFT]:
            platform_desk.move(-1, width)
        if key in [ord('d'), ord('D'), curses.KEY_RIGHT]:
            platform_desk.move(1, width)

        move_balls(width, height, platform_desk)
        redraw_screen(platform_desk)
        curses.refresh()
        curses.napms(10)
    
curses.wrapper(main)
