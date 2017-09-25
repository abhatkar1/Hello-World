# (The Triangle class) Design a class named Triangle that extends the
# GeometricObject class. The Triangle class contains:
# ■ Three float data fields named side1, side2, and side3 to denote the three
# sides of the triangle.
# ■ A constructor that creates a triangle with the specified side1, side2, and
# side3 with default values 1.0.
# ■ The accessor methods for all three data fields.
# ■ A method named getArea() that returns the area of this triangle.
# ■ A method named getPerimeter() that returns the perimeter of this triangle.
# ■ A method named __str__() that returns a string description for the triangle.
#     For    the    formula    to    compute    the
#    area    of    a    triangle, see    Exercise    2.14.The __str__() method is implemented as follows:
#     return "Triangle: side1 = " + str(side1) + " side2 = " +
#     str(side2) + " side3 = " + str(side3)
# Draw the UML diagrams for the classes Triangle and GeometricObject.
# Implement the Triangle class. Write a test program that prompts the user to
# enter the three sides of the triangle, a color, and 1 or 0 to indicate whether the triangle
# is filled.
# The program should create a Triangle
# object with these sides and
# set the color and filled properties using the input. The program should display the
# triangle’s area, perimeter, color, and True or False to indicate whether the triangle
# is filled
# or not.

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
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

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

def test():
    side1, side2, side3 = eval(input("Enter the 3 sides of the triangle:"))
    color = input("Enter the color of the triangle:")
    isFilled = eval(input("Enter whether the triangle is filled with color (1: filled, 0: not filled):"))

    triangle1 = Triangle(side1, side2, side3)
    triangle1.setColor(color)
    triangle1.setFilled(isFilled)

    print("Area:", triangle1.getArea())

    print("Perimeter:", triangle1.getPerimeter())

    print("Color:", triangle1.getColor())

    print("Filled:", triangle1.isFilled())

test()