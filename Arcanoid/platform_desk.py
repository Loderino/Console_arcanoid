class PlatformDesk:
    """Класс платформы"""
    def __init__(self, x, size=3):
        """Создаёт экземпляр платформы.

        Args:
            x (int): x-координата левого края платформы.
            size (int, optional): Размер платформы в символах. По умолчанию 3.
        """
        self.size=size
        self.x = x
        self.sym = "="
    
    def __str__(self) -> str:
        """
            Возвращает строковое представление объекта. Вызывается при приведении объекта к типу str.

        Returns:
            str: строковое представление объекта.
        """
        return self.sym*self.size

    def move(self, dx: int, max_limit: int) -> None:
        """Изменяет координаты платформы.

        Args:
            dx (int): Смещение по горизонтали в символах.
            max_limit (int): x-координата правой стенки рабочего окна.
        """
        if self.x+dx>=0 and self.x+dx+self.size<=max_limit:
            self.x+=dx