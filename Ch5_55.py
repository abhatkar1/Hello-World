# (Turtle: chessboard) Write a program to draw a chessboard

import turtle

t = turtle.Turtle()

xCoordinateList = [x for x in range(-80, 81, 20)]
yCoordinateList = [x for x in range(-80, 81, 20)]

print(xCoordinateList)
print(yCoordinateList)

for yPoint in yCoordinateList:
    t.penup()
    t.goto(-80, yPoint)
    t.pendown()
    t.forward(160)

t.setheading(90)

for xPoint in xCoordinateList:
    t.penup()
    t.goto(xPoint, -80)
    t.pendown()
    t.forward(160)

t.setheading(0)
# t.clear()
t.right(45)
t.speed(10)
for i in range(len(yCoordinateList) - 1):
    for j in range(len(xCoordinateList) - 1):
        if i % 2 == 0:
            if j % 2 != 0:
                t.penup()
                t.goto(xCoordinateList[j], yCoordinateList[i])
                t.begin_fill()
                t.color("black")
                t.circle(15, steps = 4)
                t.end_fill()
        else:
            if j % 2 == 0:
                t.penup()
                t.goto(xCoordinateList[j], yCoordinateList[i])
                t.begin_fill()
                t.color("black")
                t.circle(15, steps = 4)
                t.end_fill()

t.hideturtle()

turtle.done()