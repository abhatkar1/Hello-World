# (Geometry: n-sided regular polygon) An n-sided regular polygon’s sides all have
# the same length and all of its angles have the same degree (i.e., the polygon is
# both equilateral and equiangular). Design a class named RegularPolygon that
# contains:
# ■ A private int data field named n that defines the number of sides in the polygon.
# ■ A private float data field named side that stores the length of the side.
# ■ A private float data field named x that defines the x-coordinate of the center of
# the polygon with default value 0.
# (Half question is missing from here, check the PDF)

import math

class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getNoOfSide(self):
        return self.__n

    def getLengthOfSide(self):
        return self.__side

    def getXCoordinateOfCenter(self):
        return self.__x

    def getYCoordinateOfCenter(self):
        return self.__y

    def setNoOfSide(self, n):
        self.__n = n

    def setLengthOfSide(self, side):
        self.__side = side

    def setXCoordinateOfCenter(self, x):
        self.__x = x

    def setYCoordinateOfCenter(self, y):
        self.__y = y

    def getPerimeter(self):
        return (self.__n * self.__side)

    def getArea(self):
        return ((self.__n * (self.__side ** 2)) / (4 * math.tan(math.pi / self.__n)))

def test():
    polygon1 = RegularPolygon()
    polygon2 = RegularPolygon(6, 4, 0, 0)
    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)

    for polygonObject in polygon1, polygon2, polygon3:
        print("Details of Polygon:")
        print("Perimeter of the polygon is:", polygonObject.getPerimeter())
        print("Area of polygon is:", polygonObject.getArea())
        print("===========================================================")

test()