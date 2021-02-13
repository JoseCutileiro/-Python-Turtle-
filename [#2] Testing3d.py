"""
LEARNING PROJECT

Project by: José Cutileiro
Objective: Base 2d figures with 3d effects using a simple version of SPRITE STACKING
Be free to use any of this code

**NOTES**
-> Learn more about 3d graphics using python turtle
-> Play with the numbers and should understand what everything is doing

VERSION 1.0.0
"""

import turtle
from random import *

# USER INPUT
cor1 = input("Primeira cor: ")
cor2 = input("segunda cor: ")
cor3 = input("terceira cor: ")
cor4 = input("quarta cor: ")


# Starting turtle projects
t = turtle.Turtle()



cores = [cor1,cor2,cor3,cor4]    # 4 colors to give a 3d cool looking effect
screen = turtle.Screen()
screen.bgcolor("white")

# Original cords
x,y = 0,0

# Increase speed in order to make te process more interesting
t.speed(10000)

"""
Right to left figures    ( if you want to do left to right figures change the x value to 1 instead of -1)
"""

# CUBE
for i in range(20):
    r = randint(0,3)
    cor = cores[r]
    t.color(cor)
    t.goto(x,y)
    for i in range(4):
        t.forward(40)
        t.left(90)

    x -= 1
    y -= 1

t.penup()
# Cilinder

x = -100
y = 0
t.goto(x,y)
t.pendown()
for i in range(60):
    r = randint(0,3)
    cor = cores[r]
    t.color(cor)
    t.goto(x,y)
    t.circle(40)
    x -=4
    y -=4

t.penup()

# Ball
x = 400
y = 0
raio = 1
ate_big = 0
t.goto(x,y)
t.pendown()
for i in range(320):
    r = randint(0,3)
    cor = cores[r]
    t.color(cor)
    t.goto(x,y)
    if raio ==160:
        ate_big = 1
    if ate_big == 0:
        t.circle(raio)
        raio += 1
        x -= 1
        y -= 1
    if ate_big == 1:
        t.circle(raio)
        raio -= 1
        x -= 1
        y+= 1

t.penup()
# Prisma  (base de triangulo equilatero)

x = -300
y = 0

t.goto(x,y)
t.pendown()

for i in range(40):
    r = randint(0,3)
    cor = cores[r]
    t.color(cor)
    t.goto(x,y)
    for i in range(3):
        t.forward(80)
        t.left(120)
    x -=2
    y-=2



turtle.mainloop()