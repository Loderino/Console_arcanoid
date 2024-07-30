import unicurses as curses

__PLATFORM_DESC = 1
__BALL = 2

def init_color_themes() -> None:
    """
    Инициирует цветовые пары для разных элементов игры, таких, как платформа, кирпичи, мячи.
    """
    curses.init_pair(__PLATFORM_DESC, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(__BALL, curses.COLOR_WHITE, curses.COLOR_BLACK)

PLATFORM_DESC_COLOR = curses.color_pair(__PLATFORM_DESC)
BALL_COLOR = curses.color_pair(__BALL)
