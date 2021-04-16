"""
Credits @José Cutileiro
License: GNU
Introduction to fractrals 2D (using python turtle)
"""

import turtle
from random import *
from math import *


"""
CREATE SCREEN
"""
p = turtle.Turtle()

win = turtle.Screen()
win.title("Python turtle game")
win.bgcolor("white")
win.setup(1200,600)

p.color("black")
p.pendown()
x = 500
i = 3
times = 8

# Max turtle speed by default
p.speed(0)


# recursive version
def sierpisnki(x, i, times):
    x /= 2           # ^ recursive iterations
    if times:
        while i != 0:
            p.forward(x)
            p.left(120)
            i -= 1
        times -= 1
        j=3
        while j:
            sierpisnki(x, 3, times)
            p.forward(x)
            p.left(120)
            j -= 1


def pixel(x, y):
    p.goto(x,y)
    p.pendown()
    p.circle(0.5)
    p.penup()


# Game of chaos
def sierpisnki_GOC(size):
    i = 5000        # <- Increase this value will give a better approximation
    p1 = (0,0)
    p2 = (size,0)
    p3 = (size/2,-sin(60)*size+size/2)
    r = (p1,p2,p3)
    new_p = (randint(0,size),randint(0,size))
    while i:
        pixel(new_p[0],new_p[1])
        rand = r[randint(0,2)]
        new_p = ((new_p[0]+rand[0])/2,(new_p[1]+rand[1])/2)
        i-=1


# Instant figure ?
turtle.tracer(0)   # <- Delete this will show the process

# GOC
p.penup()
p.goto(0,0)
sierpisnki_GOC(300)        # <- Game of chaos

# RECURSIVE
p.goto(-600,-300)
p.pendown()
sierpisnki(2*x, i, times)    # <- Recursive version


turtle.mainloop()


