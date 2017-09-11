# Turtle: plot the square function) Write a program that draws a diagram for the
# function f(x) = x^2

import turtle
import math

scale_factor = 10

t = turtle.Turtle()

xCoordinateList = [scale_factor * x for x in range(-10, 11)]
yCoordinateList = [x**2 for x in range(-10, 11)]

# print(xCoordinateList)
# print(yCoordinateList)

# Plot X-axis
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(200, 0)
t.penup()
t.goto(205, 0)
t.write("X-axis")

# Plot  Y-axis
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)

t.penup()
t.goto(0, 205)
t.write("Y-axis")

t.penup()
# end of plotting axes

for i in range(len(xCoordinateList)):
    t.goto(xCoordinateList[i], yCoordinateList[i])
    t.pendown()
    t.dot(3)

t.hideturtle()

turtle.done()

