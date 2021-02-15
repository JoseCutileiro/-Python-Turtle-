
"""
Project by: José Cutileiro
TESTING Python TURTLE TO CREATE A GAME

Note: this is not a game but the basics to create one are very detailed in here
"""

import turtle
from random import *
import time




"""
CREATE SCREEN
"""

win = turtle.Screen()
win.title("Python turtle game")
win.bgcolor("tan")
win.setup(1200,600)
win.tracer(0)
x = 1

"""
Custom shapes
"""
# **Future versions **

"""
CREATE SNAKE
"""

cobra = turtle.Turtle()
cobra.speed(0)     # Snake is currently stopped

cobra.shape("square")   # Snake is a circle by default
cobra.turtlesize(1)
cobra.color("white")    # Snake color == black

cobra.penup()   # Has we have seen in previous projects 'cobra' is now a 'pen' but we dont want it to paint
pass            # so we use this command

cobra.direction = "cima"


"""
CREATE POINTS
"""

point = turtle.Turtle()
point.speed(0)
point.shape("circle")
point.color("green")
point.penup()
point.shapesize(0.50, 0.50)
point.goto(randint(-550,550) , randint(-300,300))


"""
EXECUTE MOVEMENT
"""
# Move function (left,right,up,down//esquerda,direita,cima,baixo)


def move():
    if cobra.direction == "cima":
        y = cobra.ycor()
        cobra.sety(y + 4)
        for i in range(len(segments)):
            y = segments[i].ycor()
            segments[i].sety(y ++4)

    if cobra.direction == "baixo":
        y = cobra.ycor()
        cobra.sety(y - 4)
        for i in range(len(segments)):
            y = segments[i].ycor()
            segments[i].sety(y -4)


    if cobra.direction == "direita":
        x = cobra.xcor()
        cobra.setx(x + 4)
        for i in range(len(segments)):
            x = segments[i].xcor()
            segments[i].setx(x +4)

    if cobra.direction == "esquerda":
        x = cobra.xcor()
        cobra.setx(x - 4)
        for i in range(len(segments)):
            x = segments[i].xcor()
            segments[i].setx(x -4)


"""
MOVEMENT CONTROL
"""
# Note: You cant change directly from down to up or
# up to down or left to right or right to left, you can only change 90º max


def go_up():
    if cobra.direction != "baixo":
        cobra.direction = "cima"


def go_down():
    if cobra.direction != "cima":
        cobra.direction = "baixo"


def go_right():
    if cobra.direction != "esquerda":
        cobra.direction = "direita"


def go_left():
    if cobra.direction != "direita":
        cobra.direction = "esquerda"


"""
READ KEYBOARD

win.onkey(function executed when key pressed)
"""

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")


"""
Segments control
"""

segments = []




for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)



"""
Check colisions
"""
def colissions():
    if cobra.distance(point) < 15:
        point.goto(randint(-550, 550), randint(-300, 300))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        x = cobra.xcor()
        y  = cobra.ycor()
        new_segment.goto(randint(x-20,x+20),randint(y-20,y+20))

    for e in segments:
        if e.distance(point) < 15:
            point.goto(randint(-550, 550), randint(-300, 300))
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("black")
            new_segment.penup()
            segments.append(new_segment)
            x = e.xcor()
            y = e.ycor()
            new_segment.goto(randint(x-20,x+ 20), randint(y-20,y+ 20))

"""
LASERZ
"""
lazers = []

def new_lazer(lazers):
    lazer = turtle.Turtle()
    lazer.color("red")
    lazer.shape("square")
    lazer.penup()
    lazers.append(lazer)


def move_lazer(lazers):
    for e in lazers:
        x = e.xcor()
        y = e.ycor()
        e.goto(x+randint(-4,4),y+randint(-4,4))






"""
MAIN CODE
"""
delay = 0.01
i = 0
while True:

    win.update()
    move()
    colissions()
    time.sleep(delay)
    i = i + 1
    move_lazer(lazers)
    if i > 100:
        i = 0
        new_lazer(lazers)

