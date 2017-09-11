# (Turtle: plot the sine and cosine functions) Write a program that plots the sine
# function in red and cosine in blue, as shown in Figure 5.5b.

import turtle
import math

# flag = True

t = turtle.Turtle()

#For zooming
scale_factor = 30

#Plot X-axis and Y-axis
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(200, 0)

t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)

XPointsToPlot = [-2 * math.pi, -1 * math.pi, math.pi, 2 * math.pi, 0]
YPointsToPlot = [1, -1]

for xPoint in XPointsToPlot:
    t.penup()
    t.goto(scale_factor * xPoint, scale_factor * 0.5 * -1)
    t.pendown()
    t.write(format(xPoint, ".2f"))

for yPoint in YPointsToPlot:
    t.penup()
    t.goto(scale_factor * 0.5 * -1 , scale_factor * yPoint)
    t.pendown()
    t.write(yPoint)

t.penup()

#starting angle value
angle = (-5/2) * math.pi

sineValues = []
cosineValues = []
while angle < (5/2) * math.pi:


    x = scale_factor * (angle)
    y1 = scale_factor * math.cos(x)
    y2 = scale_factor * math.sin(x)

    sineValues.append([x, y2])
    cosineValues.append([x, y1])

    angle += (1/16) * math.pi

for lst in sineValues, cosineValues:
    t.penup()
    if lst == sineValues:
        t.color("red")
    else:
        t.color("blue")

    for row in range(len(lst)):
        t.goto(lst[row][0], lst[row][1])
        t.dot(3)
        if row == 0:
            t.pendown()

    # t.pendown()
    #
    # t.color("blue")
    # t.goto(x, y1)
    #
    # t.penup()
    #
    # t.goto(x, y2)
    #
    # t.pendown()
    # if angle == (-5/2) * math.pi:
    #     t.pendown()
    #

t.color("red")
t.penup()
t.goto(180, -200)
t.write("Red : Sine Function")
t.penup()
t.color("Blue")
t.goto(180, -220)
t.write("Blue : Cosine Function")

t.hideturtle()

turtle.done()