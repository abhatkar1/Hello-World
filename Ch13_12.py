# (The TriangleError class) Define an exception class named TriangleError
# that extends RuntimeError. The TriangleError class contains the private
# data fields side1, side2, and side3 with accessor methods for the three
# sides of a triangle. Modify the Triangle class in Exercise 12.1 to throw a
# TriangleError exception if the three given sides cannot form a triangle.

class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__(self)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

class GeometricObject:
    def __init__(self, color="green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return True if int(self.__filled) == 1 else False

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        if self.checkTrianglePossible(side1, side2, side3):
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
        else:
            raise TriangleError(side1, side2, side3)

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        semiPerim = self.getPerimeter() / 2
        area = (semiPerim * (semiPerim - self.__side1) * (semiPerim - self.__side2) * (semiPerim - self.__side3)) ** 0.5
        return format(area,".2f")

    def getPerimeter(self):
        return (self.__side1 + self.__side2 + self.__side3)

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)

    def checkTrianglePossible(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

def test():
    try:
        side1, side2, side3 = eval(input("Enter the 3 sides of the triangle:"))
        color = input("Enter the color of the triangle:")
        isFilled = eval(input("Enter whether the triangle is filled with color (1: filled, 0: not filled) :"))

        triangle1 = Triangle(side1, side2, side3)
        triangle1.setColor(color)
        triangle1.setFilled(isFilled)

        print("Area:", triangle1.getArea())

        print("Perimeter:", triangle1.getPerimeter())

        print("Color:", triangle1.getColor())

        print("Filled:", triangle1.isFilled())
    except TriangleError as TE:
        print("Sides", TE.getSide1(), TE.getSide2(), TE.getSide3(), "cannot form a triangle!")


test()