#Write a program that draws a star
import turtle

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.write("Star", font = ("Calibri", "18", "bold"))

#We start from the horizontal line
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.forward(250)

#Remaining 4 slanted lines
for i in range(0, 4):
    turtle.right(180-36)
    turtle.forward(250)

'''
turtle.right(180-36)
turtle.forward(250)

turtle.right(180-36)
turtle.forward(250)

turtle.right(180-36)
turtle.forward(250)
'''
turtle.hideturtle()
turtle.done()