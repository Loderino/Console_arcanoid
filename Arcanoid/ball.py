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
        self.observer = None

    def __str__(self) -> None:
        return self.sym
    
    def check_for_bounds(self, x_lim:int):
        if self.x+self.dx>=x_lim or self.x+self.dx<0:
                self.dx = -self.dx
        if self.y+self.dy<0:
                self.dy = -self.dy

    def move(self, x_lim: int, maxy_limit: int) -> None:
        if not self.is_dead:
            self.check_for_bounds(x_lim)
            self.x+=self.dx*(self.current_stage//(self.period-1))
            self.y+=self.dy*(self.current_stage//(self.period-1))
            self.current_stage = (self.current_stage+1)%self.period
            if not self.current_stage:
                self.check_for_bounds(x_lim)
                self.observer.notice(self)
            if self.y == maxy_limit:
                self.is_dead = True
                self.sym=" "

    def add_observer(self, observer):
        self.observer = observer

    def get_pixels_coordinates(self):
        return (self.x, self.y)