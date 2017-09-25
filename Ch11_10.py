# (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
# a 4 * 4 matrix, prints the matrix, and finds the rows and columns with the most
# 1s. Here is a sample run of the program:
# 0011
# 0011
# 1101
# 1010
# The largest row index: 2
# The largest column index: 2, 3

import random

def generateMatrix(n):
    matX = []
    for i in range(n):
        matX.append([])
        for j in range(n):
            matX[i].append(random.randint(0,1))

    return matX

def displayMatrix(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            print(n[i][j], end=" ")
        print()

def findMaxRows(A):
    listOfMaxRows = ""
    sumOfMaxRow = sum(A[0])

    for i in range(1, len(A)):
        if sumOfMaxRow < sum(A[i]):
            sumOfMaxRow = sum(A[i])
    for i in range(len(A)):
        if sumOfMaxRow == sum(A[i]):
            listOfMaxRows += str(i) + ", "
    return listOfMaxRows.strip(', ')

def findMaxColums(A):
    listOfMaxColumns = ""
    maxCol = 0

    listOfCountOfOnes = []
    for i in range(len(A[0])):
        countOfOnes = 0
        for j in range(len(A)):
            if A[j][i] == 1:
                countOfOnes += 1
        listOfCountOfOnes.append(countOfOnes)

    maxCountOfOnes = max(listOfCountOfOnes)

    for i in range(len(listOfCountOfOnes)):
        if listOfCountOfOnes[i] == maxCountOfOnes:
            listOfMaxColumns += str(i) + ", "

    return listOfMaxColumns.strip(', ')

def test():
    A = generateMatrix(4)
    displayMatrix(A)
    MaxRows = findMaxRows(A)
    MaxCols = findMaxColums(A)

    print("The largest row index:",MaxRows.strip())
    print("The largest column index:", MaxCols.strip())

test()
