from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


def plot(x, y, r, g, b):
    if (x >= 0 && x < 8 && y >= 0 && y < 8):
        sense.set_pixel(x, y, r, g, b)

class Sprite:

    def __init__(self, offsets, r = 255, g = 255, b = 255):
        self.offsets = offsets
        self.r = r;
        self.g = g;
        self.b = b;

    def put(self, x, y):
        points = {(x + ox, y + oy) for (ox, oy) in self.offsets}
        for px, py in points:
            plot(px, py, self.r, self.g, self.b)
        if hasattr(self, 'oldpoints'):
            for px, py in {(ox , oy)
                    for (ox, oy) in self.oldpoints
                    if (ox, oy) not in points}:
                plot(px, py, 0, 0, 0)
        self.oldpoints = points;

crosshair = Sprite([(-1,0),(1,0),(0,-1),(0,1)], 0, 0, 255)
bullet = Sprite([0,0], 255, 0, 0))

def main():
    sense.clear()
    cross = Sprite([(-1,0),(1,0),(0,-1),(0,1)])
    cross.put(3,3)
    sleep(.5)
    cross.put(1,3)

if __name__ == "__main__": main()

