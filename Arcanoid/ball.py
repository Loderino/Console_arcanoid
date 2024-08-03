class Ball:
    """Класс мяча"""
    def __init__(self, x: int, y: int, period: int):
        """
        Создаёт экземпляр мяча.

        Args:
            x (int): x-координата мяча.
            y (int): y-координата мяча.
            period (int): период, в течение которого мяч не движется. Чем он больше, тем медленнее мяч.
        """
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.sym="O"
        self.period = period
        self.current_stage = 0
        self.is_dead = False
        self.observer = None

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта. Вызывается при приведении объекта к типу str.

        Returns:
            str: строковое представление объекта.
        """
        return self.sym
    
    def check_for_bounds(self, x_lim:int) -> None:
        """
        Проверяет, достиг ли мяч границ игрового поля и изменяет направление движения мяча.

        Args:
            x_lim (int): x-координата правой стенки игровой области.
        """
        if self.x+self.dx>=x_lim or self.x+self.dx<0:
                self.dx = -self.dx
        if self.y+self.dy<0:
                self.dy = -self.dy

    def move(self, x_lim: int, y_lim: int) -> None:
        """
        Метод движения мяча. Меняет координаты мяча, если прошёл период ожидания.

        Args:
            x_lim (int): x-координата правой стенки игровой области.
            y_limit (int): y-координата, ниже которой мяч считается утраченным.
        """
        if not self.is_dead:
            self.check_for_bounds(x_lim)
            self.x+=self.dx*(self.current_stage//(self.period-1))
            self.y+=self.dy*(self.current_stage//(self.period-1))
            self.current_stage = (self.current_stage+1)%self.period
            if not self.current_stage:
                self.check_for_bounds(x_lim)
                self.observer.notice(self)
            if self.y == y_lim:
                self.is_dead = True
                self.sym=" "

    def add_observer(self, observer) -> None:
        """
        Инициирует наблюдателя за мячом.

        Args:
            observer (Map): наблюдатель - экземпляр класса Map.
        """
        self.observer = observer

    def get_pixels_coordinates(self) -> tuple[int, int]:
        """
        Возвращает координаты символа мяча.

        Returns:
            tuple[int, int]: кортеж, представляющий координаты символа мяча: (x, y).
        """
        return (self.x, self.y)