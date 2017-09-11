# (Turtle: draw a rectangle) Write a program that prompts the user to enter the
# center of a rectangle, width, and height, and displays the rectangle

centerX, centerY = eval(input("Enter the X and Y coordinates of the center of the rectangle: "))

width = eval(input("Enter the width of the rectangle: "))

height = eval(input("Enter the height of the rectangle: "))

import turtle

turtle.penup()
turtle.goto(centerX, centerY)
turtle.dot()
turtle.goto(centerX, (centerY + height / 2))

turtle.pendown()

turtle.forward(width/2)

turtle.right(90)

turtle.forward(height)

turtle.right(90)

turtle.forward(width)

turtle.right(90)

turtle.forward(height)

turtle.right(90)

turtle.forward(width/2)

turtle.hideturtle()

turtle.done()