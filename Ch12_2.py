# (The Location class) Design a class named Location for locating a maximal
# value and its location in a two-dimensional list. The class contains the public data
# fields row, column, and maxValue that store the maximal value and its indexes in
# a two-dimensional list, with row and column as int types and maxValue as a
# float type.
# Write the following method that returns the location of the largest element in a
# two-dimensional list.
# def Location locateLargest(a):
# The return value is an instance of Location. Write a test program that prompts
# the user to enter a two-dimensional list and displays the location of the largest element
# in the list. Here is a sample run:
#
# Enter the number of rows and columns in the list:3, 4
# Enter row 0: 23.5 35 2 10
# Enter row 1: 4.5 3 45 3.5
# Enter row 2: 35 44 5.5 12.6
# The location of the largest element is 45 at (1, 2)
#

class Location:
    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue

def locateLargest(m):

    maxRow = 0
    maxColumn = 0
    maxValue = m[0][0]

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > maxValue:
                maxRow = i
                maxColumn = j
                maxValue = m[i][j]

    location1 = Location(maxRow, maxColumn, maxValue)
    return location1


def test():
    noOfRows,noOfCols = eval(input("Enter the number of rows and columns in the list:"))
    matrixA = []
    for i in range(noOfRows):
        row = [float(x) for x in input("Enter row " + str(i) + " : ").strip().split()]
        matrixA.append(row)

    locationOfMax = locateLargest(matrixA)

    print("The location of the largest element",locationOfMax.maxValue,"is (",locationOfMax.row,",",locationOfMax.column,")")

test()

