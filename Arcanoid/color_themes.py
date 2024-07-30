import unicurses as curses

__PLATFORM_DESC = 1

def init_color_themes() -> None:
    """
    Инициирует цветовые пары для разных элементов игры, таких, как платформа, кирпичи, мячи.
    """
    curses.init_pair(__PLATFORM_DESC, curses.COLOR_BLUE, curses.COLOR_BLACK)

PLATFORM_DESC_COLOR = curses.color_pair(__PLATFORM_DESC)
