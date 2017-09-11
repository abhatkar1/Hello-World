# (Geometry: area of a triangle) Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
# The formula for computing the area of a triangle is
# Here is a sample run:
# area = sqrt(s(s - side1)(s - side2)(s - side3))
# s = (side1 + side2 + side3) / 2
# Enter three points for a triangle: 1.5, -3.4, 4.6, 5,9.5, -3.4
# The area of the triangle is 33.6
import math

x1,y1 = eval(input("Enter first point of the triangle: "))
x2,y2 = eval(input("Enter second point of the triangle: "))
x3,y3 = eval(input("Enter third point of the triangle: "))

side1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)

side2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)

side3 = math.sqrt((x1-x3)**2 + (y1-y3)**2)

s = (side1 + side2 + side3)/2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is ", round(area,2)