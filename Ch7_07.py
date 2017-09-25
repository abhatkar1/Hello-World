# (Algebra: 2 x 2 linear equations) Design a class named LinearEquation for a
# 2 x 2 system of linear equations:
# ax + by = e     cx + dy = f
#
#     ed - bf
# x = --------
#     ad - bc
#
#     af - ec
# y = -------
#     ad - bc
#
# The class contains:
# ■ The private data fields a, b, c, d, e, and f with get methods.
# ■ A constructor with the arguments for a, b, c, d, e, and f.
# ■ Six get methods for a, b, c, d, e, and f.
# ■ A method named isSolvable() that returns true if ad - bc is not 0.
# ■ The methods getX() and getY() that return the solution for the equation.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter a, b, c, d, e, and f and displays the result.
# If ad - bc is 0, report that “The equation has no solution.” See Exercise 4.3 for
# sample runs.
#
# Enter a, b, c, d, e, f:
# 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
# x is -2.0 and y is 3.0
# Enter a, b, c, d, e, f:
# 1.0, 2.0, 2.0, 4.0, 4.0, 5.0
# The equation has no solution


class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        if (self.__a * self.__d - self.__b * self.__c) != 0:
            return True
        else:
            return False

    def getX(self):
        Num = (self.__e * self.__d - self.__b * self.__f)
        Den = (self.__a * self.__d - self.__b * self.__c)
        return format(Num / Den, ".2f")

    def getY(self):
        Num = (self.__a * self.__f - self.__e * self.__c)
        Den = (self.__a * self.__d - self.__b * self.__c)
        return format(Num / Den, ".2f")


def testLinearEquation():

    a, b, c, d, e, f = eval(input("Enter values of a, b, c, d, e, f:"))
    # System1 = LinearEquation(9.0, 4.0, 3.0, -5.0, -6.0, -21.0)
    # System2 = LinearEquation(1.0, 2.0, 2.0, 4.0, 4.0, 5.0)

    System = LinearEquation(a, b, c, d, e, f)

    # for linearEquation in System1, System2:
    linearEquation = System
    if linearEquation.isSolvable():
        print("x is", linearEquation.getX())
        print("y is", linearEquation.getY())
        print("=============================")
    else:
        print("The equation has no solution")
        print("=============================")

testLinearEquation()