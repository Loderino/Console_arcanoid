import unicurses as curses

__PLATFORM_DESC = 1
__BALL = 2
__BRICK_1 = 3
__BRICK_2 = 4
__BRICK_3 = 5

def init_color_themes() -> None:
    """
    Инициирует цветовые пары для разных элементов игры, таких, как платформа, кирпичи, мячи.
    """
    curses.init_pair(__PLATFORM_DESC, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(__BALL, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(__BRICK_1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(__BRICK_2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(__BRICK_3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

PLATFORM_DESC_COLOR = curses.color_pair(__PLATFORM_DESC)
BALL_COLOR = curses.color_pair(__BALL)
BRICK_TYPE_1_COLOR = curses.color_pair(__BRICK_1)
BRICK_TYPE_2_COLOR = curses.color_pair(__BRICK_2)
BRICK_TYPE_3_COLOR = curses.color_pair(__BRICK_3)
