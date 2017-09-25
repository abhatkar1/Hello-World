# (The Point class) Design a class named Point to represent a point with x- and ycoordinates.
# The class contains:
# ■ Two private data fields x and y that represent the coordinates with get methods.
# ■ A constructor that constructs a point with specified coordinates with default
# point (0, 0).
# ■ A method named distance that returns the distance from this point to another
# point of the Point type.
# ■ A method named isNearBy(p1) that returns true if point p1 is close to this
# point. Two points are close if their distance is less than 5.
# ■ Implement the _ _str__ method to return a string in the form (x, y).
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter two points, displays the distance between
# them, and indicates whether they are near each other. Here are sample runs:

import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def distance(self, point):
        return math.sqrt((self.__x - point.__x)**2 + (self.__y - point.__y)**2)

    def isNearBy(self, p1):
        return True if self.distance(p1) < 5 else False

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

def testPoint():
    x1,y1,x2,y2 = eval(input("Enter the x- and y-coordinates of the two points:"))
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("The two points are", str(p1),"and",str(p2))
    print("The distance between the two points is", format(p1.distance(p2),".2f"))
    print("The two points are nearby" if p1.isNearBy(p2) else "The two points are not nearby")

testPoint()