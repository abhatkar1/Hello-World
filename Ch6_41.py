# (Turtle: draw points, rectangles, and circles) Use the functions defined in Listing
# 6.14 to write a program that displays a rectangle centered at (- 75, 0) with width
# and height 100 and a circle centered at (50, 0) with radius 50. Fill 10 random
# points inside the rectangle and 10 inside the circle, as shown in Figure 6.11c.
import turtle

t = turtle.Turtle()

# Draw a line from (x1, y1) to (x2, y2)

def drawLine(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Write a string s at a specified location (x, y)

def writeText(s, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(s)

# Draw a point at a specified location (x, y)
def drawPoint(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(6)

# Draw a circle with a given centre (x, y) and a given radius r
def drawCircle(x = 0, y = 0, r = 10):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.circle(r)

# Draw a rectangle with the centre at (x, y) and of given width and height
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    t.penup()
    t.goto(x + width / 2, y + height / 2)
    t.right(90)
    t.pendown()
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)

import random

def main():
    drawRectangle(x = -75, y = 0, height = 100, width = 100)
    drawCircle(x = 50, y = 0, r = 50)
    count = 0
    while count < 10:
        x2 = random.randint(0, 100)
        y2 = random.randint(-50, 50)

        if (x2 - 50) ** 2 + y2 ** 2 < (50 ** 2):
            drawPoint(x2, y2)
            # Drawing inside the rectangle only when we draw inside the circle so as to keep only one count for both
            x1 = random.randint(-125, -25)
            y1 = random.randint(-50, 50)
            # Subtracting 1 from x and y to keep the point inside the rectangle
            drawPoint(x1 - 1, y1 - 1)
            count += 1
main()
t.hideturtle()
turtle.done()