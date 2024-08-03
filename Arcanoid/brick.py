class Brick:
    """Класс кирпича"""
    def __init__(self, x: int, y: int):
        """
        Создаёт экземпляр кирпича.

        Args:
            x (int): x-координата кирпича.
            y (int): y-координата кирпича.
        """
        self.x = x
        self.y = y
        self.sym = "#"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта. Вызывается при приведении объекта к типу str.

        Returns:
            str: строковое представление объекта.
        """
        return self.sym
    
    def has_pixel(self, x: int, y: int) -> bool:
        """
        Проверяет, располагается ли 'пиксель' с координатами (x, y) к данному объекту.

        Args:
            x (int): x-координата пикселя.
            y (int): y-координата пикселя.

        Returns:
            bool: True, если пиксель (x,y) относится к данному кирпичу, иначе False.
        """
        return self.x==x and self.y==y
    
    def get_pixels_coordinates(self) -> tuple[int, int]:
        """
        Возвращает координаты символа кирпича.

        Returns:
            tuple[int, int]: кортеж, представляющий координаты символа кирпича: (x, y).
        """
        return (self.x, self.y)