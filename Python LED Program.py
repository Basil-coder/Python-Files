from turtle import *
import random

screen = Screen()
screen.screensize(400,400,"black")

pen = Pen()
pen.speed(75)

size = 20

for i in range(150):

    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)

    randcol = (r,b,g)

    colormode(255)

    pen.color(randcol)

    pen.circle(size,steps = 4)
    pen.right(55)

    size = size +3
    

