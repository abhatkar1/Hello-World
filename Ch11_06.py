# (Algebra: multiply two matrices) Write a function to multiply two matrices. The
# header of the function is:
# def multiplyMatrix(a, b)
# To multiply matrix a by matrix b, the number of columns in a must be the same as
# the number of rows in b, and the two matrices must have elements of the same or
# compatible types. Let c be the result of the multiplication. Assume the column size
# of matrix a is n. Each element is
# Write a test program that prompts the user to enter two 3x3 matrices and dis-
# plays their product. Here is a sample run:
# Enter matrix1: 1 2 3 4 5 6 7 8 9
# Enter matrix2: 0 2 4 1 4.5 2.2 1.1 4.3 5.2
# The multiplication of the matrices is
# 1 2 3      0 2.0 4.0      5.3 23.9 24
# 4 5 6   *  1 4.5 2.2  =   11.6 56.3 58.2
# 7 8 9      1.1 4.3 5.2    111.9 88.7 92.4

def isMultiplyPossible(A, B):
    isPossible = True
    if len(A[0]) != len(B):
        isPossible = False
    else:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if not isinstance(A[i][j], float):
                    isPossible = False
                    break
                    # number of columns of A is equal to number of rows of B
                for k in range(len(B[j])):
                    if not isinstance(B[j][k], float):
                        isPossible = False
                        break

    return isPossible

def multiplyMatrix(a, b):
    if isMultiplyPossible(a, b):
        mulMatrix = []
        for i in range(len(a)):
            mulMatrix.append([])
            for j in range(len(b[i])):
                element = 0
                for k in range(len(a[i])):
                    element += a[i][k] * b[k][j]
                mulMatrix[i].append(format(element,".1f"))
        return mulMatrix
    else:
        return "Multiplication not possible!"


def getFormattedMatrix(n, rows, columns):
    mat = []
    nIndex = 0
    for i in range(rows):
        mat.append([])
        for j in range(columns):
            mat[i].append(n[nIndex])
            nIndex += 1
    return mat

def displayMatrix(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            print(n[i][j], end=" ")
        print()

def test():
    a = [float(x) for x in input("Enter first 3x3 matrix elements in a single row:").strip().split()]
    b = [float(x) for x in input("Enter second 3x3 matrix in a single row:").strip().split()]

    a = getFormattedMatrix(a, 3, 3)
    b = getFormattedMatrix(b, 3, 3)

    c = multiplyMatrix(a, b)

    if bool(c):
        print("Matrix A")
        displayMatrix(a)
        print("Matrix B")
        displayMatrix(b)
        print("Matrix C = Matrix A * Matrix B =")
        displayMatrix(c)
    else:
        print(c)

test()