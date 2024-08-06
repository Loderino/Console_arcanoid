import os
import unicurses as curses

from arcanoid import get_game_params, MAPS_PATH, SCREENS_PATH
from arcanoid.map import Map
from arcanoid.utils import read_map_from_file
from arcanoid.color_themes import (init_color_themes, 
                                   PLATFORM_DESC_COLOR, BALL_COLOR, BRICK_TYPE_1_COLOR, BRICK_TYPE_2_COLOR, BRICK_TYPE_3_COLOR)

bricks_colors = (BRICK_TYPE_1_COLOR, BRICK_TYPE_2_COLOR, BRICK_TYPE_3_COLOR)
game_params = get_game_params()

def redraw_screen(game_map: Map) -> None:
    """
    Перерисовывает экран, если есть изменения на карте.

    Args:
        game_map (Map): Объект карты.
    """
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

def check_for_small_screen(stdscr) -> None:
    """
    Блокирует игру, пока терминал не будет расширен до минимальных размеров, установленных в конфигурациях игры.
    """
    height, width = curses.getmaxyx(stdscr)
    while height<game_params["min_game_height"] or width<game_params["min_game_width"]:
        curses.clear()
        curses.addstr("Для продолжения игры расширьте окно")
        curses.refresh()
        curses.napms(100)
        height, width = curses.getmaxyx(stdscr)

def select_level(stdscr) -> str:
    """Функция для показа экрана выбора уровня"""
    files = os.listdir(MAPS_PATH)
    if not len(files):
        raise Exception("Отсутствует директория с картами")
    current_pos = 0
    symbols = read_map_from_file(SCREENS_PATH+"logo.txt")
    is_changed = True
    while True:
        check_for_small_screen(stdscr)
        if is_changed:
            curses.erase()
            for symbol in symbols:
                curses.move(symbol.y, symbol.x)
                curses.addch(symbol.sym)
            curses.move(12, 64)
            curses.addstr("Выберите уровень")

            curses.move(14, 64)
            curses.addstr(f"-> {files[current_pos].strip('.txt')}")
            
            curses.refresh()
            is_changed = False
        
        key = curses.getch()
        if key in (curses.KEY_LEFT, curses.KEY_UP):
            current_pos = (current_pos-1)%len(files)
            is_changed = True
        elif key in (curses.KEY_RIGHT, curses.KEY_DOWN):
            current_pos = (current_pos+1)%len(files)
            is_changed = True
        elif key == ord("\n"):
            return MAPS_PATH+files[current_pos]
        curses.flushinp()
        curses.napms(100)
        


def main(stdscr) -> None:
    """
    Основная функция игры.
    """
    curses.start_color()
    init_color_themes()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.nodelay(stdscr, True)
    curses.keypad(stdscr, True)
    
    while True:
        check_for_small_screen(stdscr)
        level_file = select_level(stdscr)
        game_map = Map(level_file)
        game_map.initialize_platform()

        platform_desk = game_map.platform_desk
        while len(game_map.balls)>0 and len(game_map.bricks)>0:
            check_for_small_screen(stdscr)

            key = curses.getch()
            if key == curses.KEY_RESIZE:
                game_map.resize(*curses.getmaxyx(stdscr)[::-1])
            if key == ord(' '):
                game_map.launch_ball()
            if key in [ord('a'), ord('A'), curses.KEY_LEFT]:
                platform_desk.move(-1)
            if key in [ord('d'), ord('D'), curses.KEY_RIGHT]:
                platform_desk.move(1)

            curses.flushinp()
            game_map.move_balls()
            redraw_screen(game_map)
            
            curses.napms(10)

        symbols = read_map_from_file(SCREENS_PATH+("victory.txt" if game_map.balls else "game_over.txt"))
        while True:
            check_for_small_screen(stdscr)
            curses.erase()
            for symbol in symbols:
                curses.move(symbol.y, symbol.x)
                curses.addch(symbol.sym)
            curses.move(12, 64)
            curses.addstr("Нажмите enter")
            curses.refresh()
    
            key = curses.getch()
            if key == ord("\n"):
                break
            curses.flushinp()
            curses.napms(100)
