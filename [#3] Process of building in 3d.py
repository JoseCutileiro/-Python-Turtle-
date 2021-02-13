"""
Project by: José Cutileiro
A new way to paint in 2d
"""

import turtle
from random import *

# Starting turtle projects
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")

t.speed(0)

# Original cords
x,y = 0,0

# Sun
t.penup()
x = -400
y = 300
raio = 1
ate_big = 0
t.goto(x,y)
t.pendown()
cores = ["yellow","gold1","gold2","tan"]
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
t.goto(0,0)
x = 0
y = 0
t.pendown()
#---------------COPULA--------------------#
t.penup()

x +=33
y -= 22

raio = 1
ate_big = 0
t.goto(x,y)
t.pendown()
cores = ["red","blue","green","yellow"]
for i in range(40):
    r = randint(0,3)
    cor = cores[r]
    t.color(cor)
    t.goto(x,y)
    if raio ==20:
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
t.goto(0,0)
x = 0
y = 0
t.pendown()


#------------------------HOUSE-----------------------------#
# CUBE
cores = ["chocolate4","chocolate4","chocolate3","chocolate3"]    # 4 colors to give a 3d cool looking effect
for i in range(13):

    for i in range(33):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x -= 3
        y -= 3


    t.forward(10)

    for i in range(33):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x += 5



    for i in range(33):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x += 3
        y += 3

    for i in range(33):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x -= 5

    y += 10

#-------------------Telhado------------------#
cores = ["firebrick4","firebrick4","firebrick4","firebrick4"]    # 4 colors to give a 3d cool looking effect

x -=7
tamanho = 39
for i in range(5):


    for i in range(tamanho):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x -= 3
        y -= 3


    t.forward(10)

    for i in range(tamanho):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x += 5



    for i in range(tamanho):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x += 3
        y += 3

    for i in range(tamanho):
        r = randint(0,3)
        cor = cores[r]
        t.color(cor)
        t.goto(x,y)
        for i in range(4):
            t.forward(10)
            t.left(90)

        x -= 5

    y += 10

    tamanho -= 4
    x += 5

turtle.mainloop()