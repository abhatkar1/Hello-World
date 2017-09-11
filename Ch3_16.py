# (Turtle: draw shapes) Write a program that draws a triangle, square, pentagon,
# hexagon, and octagon, as shown in Figure 3.6b. Note that the bottom edges of
# these shapes are parallel to the x-axis. (Hint: For a triangle with a bottom line
# parallel to the x-axis, set the turtle's heading to 60 degrees.)

import turtle

turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
#turtle should be at 60 degrees to X-axis
turtle.left(60)
turtle.begin_fill()
turtle.circle(50, steps = 3)
turtle.color("Blue")
turtle.end_fill()
# turtle.reset()
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("Yellow")
#turtle should be at 45 degrees to X-axis
turtle.right(15)
turtle.circle(50, steps = 4)
turtle.end_fill()

# turtle.reset()
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
#turtle should be at 36 degrees with X-axis
turtle.begin_fill()
turtle.right(9)
turtle.circle(50, steps = 5)
turtle.color("Red")
turtle.end_fill()
# turtle.reset()
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("Green")
turtle.right(6)
turtle.circle(50, steps = 6)
turtle.end_fill()

# turtle.reset()
turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.right(8.5)
turtle.color("Cyan")
turtle.circle(50, steps = 8)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,100)
turtle.pendown()

turtle.write("Draw Shapes", font = ("Times New Roman", 50))
turtle.hideturtle()

turtle.done()