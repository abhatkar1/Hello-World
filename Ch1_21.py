# Turtle program to draw a clock and indicate the time 9:15
import turtle

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(0,-95)
turtle.pendown()
turtle.write("6")

turtle.penup()
turtle.goto(0,85)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(90,0)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(-95,0)
turtle.pendown()
turtle.write("9")

turtle.penup()
turtle.goto(-50,0)
turtle.pendown()

#Hour hand
turtle.pensize(3)
turtle.goto(0,0)
turtle.dot()

#Minute hand
turtle.pensize(2)
turtle.goto(65,0)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

#Second's hand
turtle.pensize(0.5)
turtle.goto(0,80)

# turtle.undo()
turtle.hideturtle()

turtle.penup()
turtle.done()
