# (Turtle: two circles) Write a program that prompts the user to enter the center
# coordinates and radii of two circles and determines whether the second circle is
# inside the first or overlaps with the first, as shown in Figure 4.16.

import math, turtle

x1, y1, radius1 = eval(input("Enter circle1's center x-, y-coordinates, and radius:"))

x2, y2, radius2 = eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

distanceBetweenCentres = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

absoluteDifferenceBetweenRadii = abs(radius1 - radius2)

sumOfRadii = radius1 + radius2

result = ''

if distanceBetweenCentres <= absoluteDifferenceBetweenRadii:
    result = "Circle2 is inside circle1"
elif distanceBetweenCentres <=sumOfRadii:
    result = "Circle2 overlaps circle1"
else:
    result = "Circle2 is outside circle1"
    
t = turtle.Turtle()

t.penup()
t.goto(x1, y1)
t.dot(5)
t.goto(x1, y1 - radius1)
t.pendown()

t.circle(radius1)

t.penup()
t.goto(x2, y2)
t.dot()
t.goto(x2, y2 - radius2)
t.pendown()

t.circle(radius2)

t.penup()
t.goto(((x1 + x2) / 2 - radius1 - radius2), -100)
t.pendown()

t.write(result, font = ("Calibri" , "12", "bold"))

t.hideturtle()

turtle.done()