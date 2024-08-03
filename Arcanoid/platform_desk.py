class PlatformDesk:
    """Класс платформы"""
    def __init__(self, x, y, size=11, speed=1):
        """Создаёт экземпляр платформы.

        Args:
            x (int): x-координата левого края платформы.
            y (int): y-координата платформы.
            size (int, optional): Размер платформы в символах. По умолчанию 11.
        """
        self.size=size
        self.x = x
        self.y = y
        self.sym = "="
        self.has_ball = True
        self.observer = None
        self.speed=speed
    
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
            for _ in range(self.speed):
                if self.x+dx>=0 and self.x+dx+self.size<=max_limit:
                    self.x+=dx
            self.observer.notice(self)
                
    def add_observer(self, observer):
        self.observer = observer

    def change_y_pos(self, y):
        self.y = y
        self.observer.notice(self)

    def launch(self):
        if self.has_ball:
            self.has_ball = False

    def get_pixels_coordinates(self):
        return [(self.x+shift, self.y) for shift in range(self.size)]