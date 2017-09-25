# (Sum the major diagonal in a matrix) Write a function that sums all the numbers
# of the major diagonal in an n x n matrix of integers using the following header:
# def sumMajorDiagonal(m):
# The major diagonal is the diagonal that runs from the top left corner to the bottom
# right corner in the square matrix. Write a test program that reads a 4 x 4 matrix and
# displays the sum of all its elements on the major diagonal. Here is a sample run:
#
# Enter a 4-by-4 matrix row for row 1:1 2 3 4
# Enter a 4-by-4 matrix row for row 2:5 6.5 7 8
# Enter a 4-by-4 matrix row for row 3:9 10 11 12
# Enter a 4-by-4 matrix row for row 4:13 14 15 16
#
# Sum of the elements in the major diagonal is 34.5

def sumMajorDiagonal(m):
    sum = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                sum += m[i][j]
    return sum


def getSquareMatrix(n):
    matA = []
    for i in range(n):
            row = input("Enter row " + str(i + 1) + " of the matrix separated by space:").strip().split()
            matA.append([eval(x) for x in row])
    return matA


def test():
    sizeOfSquareMatrix = 4

    matrix = getSquareMatrix(sizeOfSquareMatrix)

    print("Sum of elements in major diagonal is", sumMajorDiagonal(matrix))


test()