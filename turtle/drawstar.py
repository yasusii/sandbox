import sys
import turtle

def draw_star(size, points):
    if size <= 0:
        print('size must be greater than 0', file=sys.stderr)
        sys.exit(1)

    angle = 360 / points
    r1 = 175
    r2 = angle + 360 - r1
        
    t = turtle.Pen()
    t.color(0.9, 0.75, 0)
    t.begin_fill()
    for x in range(points * 2):
        t.forward(size)
        if x % 2:
            t.left(r2)
        else:
            t.left(r1)
    t.end_fill()

draw_star(100, 20)
input()
        
