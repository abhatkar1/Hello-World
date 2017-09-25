# (Algebra: add two matrices) Write a function to add two matrices. The header of
# the function is:
# def addMatrix(a, b):
# In order to be added, the two matrices must have the same dimensions and the
# same or compatible types of elements. Let c be the resulting matrix. Each element
# Cij is Aij + Bij.

# Write a test program that prompts the user to enter two matrices and displays
# their sum. Here is a sample run:
# Enter matrix1: 1 2 3 4 5 6 7 8 9
# Enter matrix2: 0 2 4 1 4.5 2.2 1.1 4.3 5.2
# The matrices are added as follows:
# 1.0 2.0 3.0   0.0 2.0 4.0     1.0 4.0 11.0
# 4.0 5.0 6.0    +  1.0 4.5 2.2  =  5.0 11.5 8.2
# 11.0 8.0 11.0     1.1 4.3 5.2     8.1 12.3 14.2

def isAdditionPossible(m, n):
    isPossible = True

    #check if dimensions and type are same
    if len(m) != len(n):
        isPossible = False
    else:
        for i in range(len(m)):
            if len(m[i]) != len(n[i]):
                isPossible = False
                break
            else:
                for j in range(len(m[i])):
                    if not isinstance(m[i][j], float) or not isinstance(n[i][j], float):
                        isPossible = False
                        break


    return isPossible

def addMatrix(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j] + b[i][j])

    return c

def displayMatrix(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            print(n[i][j], end=" ")
        print()

def getFormattedMatrix(n, rows, columns):
    mat = []
    nIndex = 0
    for i in range(rows):
        mat.append([])
        for j in range(columns):
            mat[i].append(n[nIndex])
            nIndex += 1
    return mat

def test():
    matA = [float(x) for x in input("Input first 3x3 matrix in a single row:").strip().split()]
    matB = [float(x) for x in input("Input second 3x3 matrix in a single row:").strip().split()]

    matA = getFormattedMatrix(matA, 3, 3)
    matB = getFormattedMatrix(matB, 3, 3)

    if isAdditionPossible(matA, matB):
        matC = addMatrix(matA, matB)

        print("Matrix A =")
        displayMatrix(matA)

        print("Matrix B =")
        displayMatrix(matB)

        print("Matrix C = Matrix A + Matrix B =")
        displayMatrix(matC)
    else:
        print("Addition not possible")
test()