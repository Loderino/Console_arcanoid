import random

from Arcanoid.ball import Ball

class PlatformDesk:
    """Класс платформы"""
    def __init__(self, x, y, size=11):
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
        self.balls = [Ball(self.x+self.size//2, self.y-1, 8)]
        self.has_ball = True
    
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
            if self.has_ball:
                for ball in self.balls:
                    ball.move(0, 0, shift_x=dx)

    def change_y_pos(self, y):
        self.y = y
        if self.has_ball:
            for ball in self.balls:
                ball.y = y-1

    def launch(self):
        if self.has_ball:
            self.has_ball = False
            for ball in self.balls:
                ball.dx = random.choice([-1, 1])
                ball.dy = 1

    def check_balls(self):
        self.balls = list(filter(lambda ball: not ball.is_dead, self.balls))