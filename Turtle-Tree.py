from turtle import *


HEIGHT = 1000
WIDTH = 750
LENGTH = HEIGHT/7
ANGLE = 35
MAX_DEPTH = 7
PEN_SIZE = MAX_DEPTH

""" Set screen for recursive tree"""
tracer(False)
screensize(WIDTH, HEIGHT, 'white')


def set(heading):
    penup()
    goto(0, 0)
    #goto(0, 0 - HEIGHT/2 + HEIGHT/4)
    pensize(PEN_SIZE)
    pendown()
    setheading(heading)
    forward(LENGTH)
    penup()
set(90)

def tree(length, depth, init_heading, coords, pen_size, angle):
    """Draw a fractal tree"""
    '''Store Data'''
    init_heading = heading()
    coords = (xcor(), ycor())
    pensize(pen_size)
    '''Go Left'''
    setheading(init_heading+angle)
    pendown()
    forward(length)
    penup()
    '''Recurse Left'''
    if depth < MAX_DEPTH:
        tree(length*0.65, depth+1, angle, coords, pen_size*0.75, angle)
    '''Go Right'''
    goto(coords)
    setheading(init_heading-angle)
    pensize(pen_size)
    pendown()
    forward(length)
    penup()
    '''Recurse Right'''
    if depth < MAX_DEPTH:
        tree(length*0.65, depth + 1, angle, coords, pen_size*0.75, angle)
    return
i = 0
while True:
    clear()
    tracer(False)

    hideturtle()
    set(0-i*2)
    tree(LENGTH*0.65, 0, heading(), (xcor(), ycor()), PEN_SIZE*0.75, ANGLE+i)
    set(90 - i * 2)
    tree(LENGTH * 0.65, 0, heading(), (xcor(), ycor()), PEN_SIZE * 0.75, ANGLE + i*1.25)
    set(180-i*2)
    tree(LENGTH * 0.65, 0, heading(), (xcor(), ycor()), PEN_SIZE * 0.75, ANGLE + i*1.5)
    set(270 - i * 2)
    tree(LENGTH * 0.65, 0, heading(), (xcor(), ycor()), PEN_SIZE * 0.75, ANGLE + i*1.75)
    delay(500)
    update()
    tracer(False)

    i += 1

hideturtle()
mainloop()