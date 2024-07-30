class Ball:
    def __init__(self, x: int, y: int, period: int):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.sym="O"
        self.period = period
        self.current_stage = 0
        self.is_dead = False

    def __str__(self) -> None:
        return self.sym

    def move(self, maxx_limit: int, maxy_limit: int, shift_x: int = 0, shift_y: int = 0) -> None:
        if not self.is_dead:
            self.x += shift_x
            self.y += shift_y

            if self.x+self.dx>=maxx_limit or self.x+self.dx<0:
                self.dx = -self.dx
            if self.y+self.dy<0:
                self.dy = -self.dy

            self.x+=self.dx*(self.current_stage//(self.period-1))
            self.y+=self.dy*(self.current_stage//(self.period-1))
            self.current_stage = (self.current_stage+1)%self.period
            if self.y == maxy_limit:
                self.is_dead = True
                self.sym=" "