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
    
    def move(self, dx: int) -> None:
        """Изменяет координаты платформы.

        Args:
            dx (int): Смещение по горизонтали в символах.
        """