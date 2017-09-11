# (Turtle: draw a line) Write a program that prompts the user to enter two points and draw
# a line to connect the points and displays the coordinates of the points, as
# shown in Figure 3.7c.

import turtle

x1, y1 = eval(input("Enter the coordinates of point1 in x,y form:"))

x2, y2 = eval(input("Enter coordinates of point2 in x,y form:"))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.dot(5)
turtle.penup()
turtle.goto(x1, y1 - 5)
turtle.pendown()
turtle.write('('+ str(x1) + ',' + str(y1) + ')')


turtle.goto(x2, y2)
turtle.dot(5)

turtle.penup()
turtle.goto(x2, y2 + 5)
turtle.pendown()
turtle.write('('+ str(x2) + ',' + str(y2)+ ')')

turtle.hideturtle()
turtle.done()