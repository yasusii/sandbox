import turtle

t = turtle.Pen()
t.color(0.9, 0.75, 0)
t.begin_fill()
for x in range(18):
    t.forward(100)
    if x % 2:
        t.left(225)
    else:
        t.left(175)
t.end_fill()
input()
        
