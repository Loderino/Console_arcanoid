import random

from Arcanoid.platform_desk import PlatformDesk
from Arcanoid.ball import Ball

class Brick:
    def __init__(self, x: int, y: int, width: int = 1, height: int = 1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sym = "#"

    def __str__(self):
        return "\n".join([self.sym*self.width]*self.height)
    
    def has_pixel(self, x, y):
        if self.x==x and self.y==y:
            return True
        return False
    
    def get_active_pixels(self):
        return (self.x, self.y)
    
    
class Map:
    def __init__(self, xlim, ylim):
        self.xlim=xlim
        self.ylim=ylim
        self.platform_desk=None
        self.balls = []
        self.bricks = []
        self.active_pixels={}
        self.is_changed = False
        self.initialize_bricks()

    def check_for_change(self):
        if self.is_changed:
            self.is_changed=False
            return True
        return False

    def initialize_platform(self):
        self.platform_desk = PlatformDesk(self.xlim//2, self.ylim-2)
        self.balls.append(Ball(self.platform_desk.x+self.platform_desk.size//2, self.platform_desk.y-1, 8))
        self.platform_desk.add_observer(self)
        self.balls[0].add_observer(self)
        self.active_pixels[self.platform_desk] = set(self.platform_desk.get_pixels_coordinates())
        self.active_pixels[self.balls[0]] = self.balls[0].get_pixels_coordinates()

    def initialize_bricks(self):
        self.bricks = [Brick(x, y) for x in range(100) for y in range(10)]
        self.active_pixels["bricks"] = set([brick.get_active_pixels() for brick in self.bricks])


    def resize(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim
        self.platform_desk.change_y_pos(ylim-2)

    def notice(self, obj):
        self.is_changed=True
        pixels = obj.get_pixels_coordinates()
        if obj is self.platform_desk:
            self.active_pixels[obj] = set(pixels)
            if self.platform_desk.has_ball:
                self.balls[0].y = pixels[0][1]-1
                self.balls[0].x = pixels[len(pixels)//2+1][0]
                self.active_pixels[self.balls[0]]=(self.balls[0].x, self.balls[0].y)
        
        elif obj in self.balls:
            self.active_pixels[obj] = (obj.x, obj.y)
            if (obj.x+obj.dx, obj.y+obj.dy) in self.active_pixels[self.platform_desk]:
                obj.dy=-abs(obj.dy)
            elif (obj.x+obj.dx, obj.y+obj.dy) in self.active_pixels["bricks"]:
                self.active_pixels["bricks"].remove((obj.x+obj.dx, obj.y+obj.dy))
                self.crush_brick(obj.x+obj.dx, obj.y+obj.dy)
                obj.dx*=-1
                obj.dy*=-1

    def crush_brick(self, x, y):
        for brick in self.bricks:
            if brick.has_pixel(x, y):
                self.bricks.remove(brick)
                break


    def launch_ball(self):
        self.platform_desk.launch()
        for ball in self.balls:
            ball.dx = random.choice([-1, 1])
            ball.dy = -1

    def move_balls(self):
        for ball in self.balls:
            ball.move(self.xlim, self.ylim)
            if ball.is_dead:
                self.active_pixels.pop(ball)
                self.balls.remove(ball) ###