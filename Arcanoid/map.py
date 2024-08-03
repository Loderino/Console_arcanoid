import random

from Arcanoid import BALL_SPEED, PLATFORM_SIZE, PLATFORM_SPEED, LEVEL, MAPS_PATH
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
        self.platform_desk = PlatformDesk(self.xlim//2-PLATFORM_SIZE//2, self.ylim-2, size=PLATFORM_SIZE, speed=PLATFORM_SPEED)
        self.balls.append(Ball(self.platform_desk.x+self.platform_desk.size//2, self.platform_desk.y-1, BALL_SPEED))
        self.platform_desk.add_observer(self)
        self.balls[0].add_observer(self)
        self.active_pixels[self.platform_desk] = self.platform_desk.get_pixels_coordinates()
        self.active_pixels[self.balls[0]] = self.balls[0].get_pixels_coordinates()

    def initialize_bricks(self):
        with open(f"{MAPS_PATH}level{LEVEL}.txt") as file:
            for y_index, line in enumerate(file):
                for x_index, sym in enumerate(line):
                    if sym=="#":
                        self.bricks.append(Brick(x_index, y_index))
        self.active_pixels["bricks"] = set([brick.get_active_pixels() for brick in self.bricks])


    def resize(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim
        self.platform_desk.change_y_pos(ylim-2)

    def notice(self, obj):
        self.is_changed=True
        pixels = obj.get_pixels_coordinates()
        if obj is self.platform_desk:
            self.active_pixels[obj] = pixels
            if self.platform_desk.has_ball:
                self.balls[0].y = pixels[0][1]-1
                self.balls[0].x = pixels[(len(pixels)-1)//2][0]
                self.active_pixels[self.balls[0]]=(self.balls[0].x, self.balls[0].y)
        
        elif obj in self.balls:
            self.active_pixels[obj] = (obj.x, obj.y)
            try:
                platform_index = self.active_pixels[self.platform_desk].index((obj.x+obj.dx, obj.y+obj.dy))
                if platform_index/self.platform_desk.size < 0.25:
                    obj.dx= -2
                elif platform_index/self.platform_desk.size < 0.5:
                    obj.dx= -1
                elif platform_index/self.platform_desk.size < 0.75:
                    obj.dx= 1
                else:
                    obj.dx= 2
                obj.dy=-abs(obj.dy)
            except ValueError:
                pass
            
            if abs(obj.dx)==1:
                potential_pixel_x = (obj.x-obj.dx, obj.y)
                potential_pixel_y = (obj.x, obj.y-obj.dy)
                if set([obj.get_pixels_coordinates(), potential_pixel_x, potential_pixel_y]).intersection(self.active_pixels["bricks"]):
                    if potential_pixel_x in self.active_pixels["bricks"]:
                        obj.dy*=-1
                        obj.x-=obj.dx
                        obj.y+=obj.dy
                        self.crush_brick(*potential_pixel_x)

                    elif potential_pixel_y in self.active_pixels["bricks"]:
                        obj.dx*=-1
                        obj.y-=obj.dy
                        obj.x+=obj.dx
                        self.crush_brick(*potential_pixel_y)
                    
                    else:
                        obj.dx*=-1
                        obj.dy*=-1
                        self.crush_brick(*obj.get_pixels_coordinates())
            
            elif abs(obj.dx)==2:
                potential_pixel_x_1 = (obj.x-obj.dx//2, obj.y-obj.dy)
                potential_pixel_y = (obj.x-obj.dx//2, obj.y)
                potential_pixel_x_2 = (obj.x, obj.y-obj.dy)
                if set([obj.get_pixels_coordinates(), potential_pixel_x_1, potential_pixel_x_2, potential_pixel_y]).intersection(self.active_pixels["bricks"]):
                    
                    if potential_pixel_x_1 in self.active_pixels["bricks"]:
                        obj.y-=obj.dy
                        obj.x-=obj.dx
                        obj.dx*=-1
                        self.crush_brick(*potential_pixel_x_1)
                    
                    elif potential_pixel_y in self.active_pixels["bricks"]:
                        obj.x-=obj.dx//2
                        obj.y-=obj.dy
                        obj.dy*=-1
                        self.crush_brick(*potential_pixel_y)

                    elif potential_pixel_x_2 in self.active_pixels["bricks"]:
                        obj.y-=obj.dy
                        obj.x-=obj.dx//2
                        obj.dx*=-1
                        self.crush_brick(*potential_pixel_x_2)
                    
                    else:
                        obj.dx*=-1
                        self.crush_brick(*obj.get_pixels_coordinates())


    def crush_brick(self, x, y):
        for brick in self.bricks:
            if brick.has_pixel(x, y):
                self.bricks.remove(brick)
                self.active_pixels["bricks"].remove((x, y))
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