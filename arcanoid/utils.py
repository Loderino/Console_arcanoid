from collections import namedtuple

Symbol = namedtuple("Symbol", ['sym', 'x', 'y'])

def read_map_from_file(filename: str) -> list[tuple[str, int, int]]:
    """
    Читает файл filename и возвращает список с информацией о каждом непробельном символе.

    Args:
        filename (str): путь к файлу.

    Returns:
        list[tuple[str, int, int]]: список именованных кортежей, содержащих поля sym (сам символ), x, y (координаты символа)
    """
    symbols = []
    with open(filename, encoding="utf-8") as file:
        for y_index, line in enumerate(file):
            for x_index, sym in enumerate(line):
                    if sym != " ":
                        symbols.append(Symbol(sym, x_index, y_index))
    return symbols