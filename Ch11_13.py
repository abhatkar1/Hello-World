# (Locate the largest element) Write the following function that returns the location
# of the largest element in a two-dimensional list:
# def locateLargest(a):
# The return value is a one-dimensional list that contains two elements. These
# two elements indicate the row and column indexes of the largest element in the
# two-dimensional list. Write a test program that prompts the user to enter a two dimensional
# list and displays the location of the largest element in the list. Here is a sample run:
# Enter the number of rows in the list:3
# Enter a row:23.5 35 2 10
# Enter a row:4.5 3 45 3.5
# Enter a row:35 44 5.5 11.6
# The location of the largest element is at (1, 2)

def locateLargest(a):
    # largestRow = 0
    # largestColumn = 0
    largestElement = max(a[0])
    for i in range(1, len(a)):
        if max(a[i]) >= largestElement:
            largestElement = max(a[i])

    listOfLargestElementLocation = []

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == largestElement:
                listOfLargestElementLocation.append([i, j])

    return listOfLargestElementLocation

def test():
    noOfRows = eval(input("Enter number of rows:"))
    matrixA = []
    for i in range(noOfRows):
        row = [float(x) for x in input("Enter elements of row " + str(i + 1) + " : ").strip().split()]
        matrixA.append(row)
    largestElementPositions = locateLargest(matrixA)

    print("The location of the largest element is",largestElementPositions)

test()