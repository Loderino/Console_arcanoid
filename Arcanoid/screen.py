import unicurses as curses

from Arcanoid import GAME_SIZE_X, GAME_SIZE_Y
from Arcanoid.color_themes import init_color_themes, PLATFORM_DESC_COLOR, BALL_COLOR, BRICK_TYPE_1_COLOR, BRICK_TYPE_2_COLOR, BRICK_TYPE_3_COLOR
from Arcanoid.map import Map

bricks_colors = (BRICK_TYPE_1_COLOR, BRICK_TYPE_2_COLOR, BRICK_TYPE_3_COLOR)

def redraw_screen(game_map: Map):
    if game_map.check_for_change():
        curses.erase()
        curses.move(game_map.platform_desk.y, game_map.platform_desk.x)
        curses.addstr(str(game_map.platform_desk), PLATFORM_DESC_COLOR)
        for counter, brick in enumerate(game_map.bricks):
            curses.move(brick.y, brick.x)
            curses.addch(str(brick), bricks_colors[counter%len(bricks_colors)])
        for ball in game_map.balls:
            curses.move(ball.y, ball.x)
            curses.addch(str(ball), BALL_COLOR)
        curses.refresh()

def check_for_small_screen(stdscr):
    height, width = curses.getmaxyx(stdscr)
    while height<GAME_SIZE_Y or width<GAME_SIZE_X:
        curses.clear()
        curses.addstr("Для продолжения игры расширьте окно")
        curses.refresh()
        curses.napms(100)
        height, width = curses.getmaxyx(stdscr)

def main(stdscr):
    curses.start_color()
    init_color_themes()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.nodelay(stdscr, True) # позволяет использовать getch без блокирования программы
    curses.keypad(stdscr, True)  # Позволяет считывать специальные клавиши, такие как стрелки
    
    check_for_small_screen(stdscr)
    height, width = curses.getmaxyx(stdscr)
    game_map = Map(width, height)
    game_map.initialize_platform()

    platform_desk = game_map.platform_desk
    while len(game_map.balls)>0 and len(game_map.bricks)>0:
        check_for_small_screen(stdscr)
        height, width = curses.getmaxyx(stdscr)

        key = curses.getch()
        if key == curses.KEY_RESIZE:
            game_map.resize(*curses.getmaxyx(stdscr)[::-1])
        if key == ord(' '):
            game_map.launch_ball()
        if key in [ord('a'), ord('A'), curses.KEY_LEFT]:
            platform_desk.move(-1, width)
        if key in [ord('d'), ord('D'), curses.KEY_RIGHT]:
            platform_desk.move(1, width)

        curses.flushinp()
        game_map.move_balls()
        redraw_screen(game_map)
        
        curses.napms(10)
    
curses.wrapper(main)
