# (Geometry: intersection) Suppose two line segments intersect. The two endpoints
# for the first line segment are (x1, y1) and (x2, y2) and for the second line segment
# are (x3, y3) and (x4, y4). Write a program that prompts the user to enter these
# four endpoints and displays the intersecting point. (Hint: Use the
# LinearEquation class from Exercise 7.7.)
# Sample:
# Enter the endpoints of the first line segment: 2.0, 2.0, 0, 0
# Enter the endpoints of the second line segment: 0, 2.0, 2.0, 0
# The intersecting point is: (1.0, 1.0)

from Ch7_07 import LinearEquation

def main():
    x1, y1, x2, y2 = eval(input("Enter the two endpoints for first line segment:"))
    x3, y3, x4, y4 = eval(input("Enter the two endpoints for second line segment:"))

    a = calCoefficientX(x1, y1, x2, y2)
    b = -1
    e = calConstant(x1, y1, x2, y2)

    c = calCoefficientX(x3, y3, x4, y4)
    d = -1
    f = calConstant(x3, y3, x4, y4)

    systemOfLinearEquation1 = LinearEquation(a, b, c, d, e, f)

    print("Point of intersection is: (", format(float(systemOfLinearEquation1.getX()),".1f"), \
          ",",format(float(systemOfLinearEquation1.getY()),".1f"),")")

def calCoefficientX(x1, y1, x2, y2):
    coeffX = (x2 - x1) / (y2 - y1)
    return coeffX

def calConstant(x1, y1, x2, y2):
    const = ((x2 - x1)/(y2 - y1)) * y1 - x1
    return const

main()