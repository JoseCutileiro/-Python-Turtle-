"""

#4 TURTLE FOUNDATIONS

Project by: José Cutileiro
Usefull project: Make 2.5d figures using simple functions
be free to use any of this code

Version 0.1 - Available models: Cube // Front_wall // Side_wall // Square // Ball // Circle

** Future versions **

-> New figures
-> New examples
"""


import turtle
from random import *



# Starting turtle projects
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

# Increase speed in order to make te process more interesting
t.speed(0)


def cube(side,x,y,color_list):
    t.penup()
    for i in range(side//2):
        r = randint(0,len(color_list)-1)
        cor = color_list[r]
        t.color(cor)
        t.goto(x, y)
        t.pendown()
        for i in range(4):
            t.forward(side)
            t.left(90)

        x -= 1
        y -= 1

def front_wall(block,side,hight,x,y,color_list):
    for i in range(hight):
        t.penup()
        for i in range(side):
            r = randint(0,len(color_list)-1)
            cor = color_list[r]
            t.color(cor)
            t.goto(x, y)
            t.pendown()
            for i in range(4):
                t.forward(block)
                t.left(90)

            x += block
        t.penup()
        y+=block
        x = x-side*block
        t.goto(x,y)
        t.pendown()

def side_wall(block,side,hight,x,y,color_list):
    for i in range(hight):
        t.penup()
        for i in range(side):
            r = randint(0,len(color_list)-1)
            cor = color_list[r]
            t.color(cor)
            t.goto(x, y)
            t.pendown()
            for i in range(4):
                t.forward(block)
                t.left(90)

            x += block
            y += block
        y = y-side*block
        t.penup()
        y+=block
        x = x-side*block
        t.goto(x,y)
        t.pendown()


def square(side,x,y,cor):
    t.penup()
    t.color(cor)
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(side)
        t.left(90)


def ball(radius,x,y,color_list):
    raio = 1
    t.penup()
    ate_big = 0
    t.goto(x, y)
    t.pendown()
    for i in range(radius):
        r = randint(0, len(color_list)-1)
        cor = color_list[r]
        t.color(cor)
        t.goto(x, y)
        if raio == (radius//2):
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
            y += 1

def circle(radius,x,y,cor):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(cor)
    t.circle(radius)


# Examples of utilization

turtle.tracer(1000, 1000)     # Increase the speed
"""
# 1 -> Basic 3d figures
 
while True:

    for i in range(10):
        square(randint(0,100),randint(-300,300),randint(-300,300),"red")
        circle(randint(0, 100), randint(-300, 300), randint(-300, 300), "black")
        cube(randint(0,100),randint(-600,600),randint(-300,300),["red","black","gold","tan"])

front_wall(5,10,10,0,0,["green"])
front_wall(5,10,10,50,49,["white"])
side_wall(5,10,10,0,0,["red"])
# side_wall(5,10,10,50,0,["blue"])

"""

"""
# 2 -> A sophisticated 3d building



front_wall(5,30,30,0,0,["red"])
front_wall(5,30,30,150,150,["red"])
side_wall(5,30,30,0,0,["red"])
side_wall(5,30,30,150,0,["red","blue"])


front_wall(5,30,30,-100,0,["white","tan"])
front_wall(5,30,30,50,150,["white","tan"])
side_wall(5,30,30,-100,0,["white","tan"])
side_wall(5,30,30,50,0,["white","tan"])


front_wall(5,30,30,-200,0,["white","tan"])
front_wall(5,30,30,-50,150,["white","tan"])
side_wall(5,30,30,-200,0,["white","tan"])
side_wall(5,30,30,-50,0,["white","tan"])

"""

"""
# 3 -> A new 3d model using walls
y = 0

tamanho = 50
for i in range(3000):

    front_wall(5,tamanho,1,0,0+y,["red","tan"])
    side_wall(5,tamanho,1,0,0+y,["red","tan"])
    front_wall(5,tamanho,1,tamanho*5,tamanho*5+y,["red","tan"])
    side_wall(5,tamanho,1,tamanho*5,0+y,["red","tan"])
    y+=6
    tamanho -=1


"""
turtle.mainloop()




