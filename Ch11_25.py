# (Markov matrix) An n * n matrix is called a positive Markov matrix if each element
# is positive and the sum of the elements in each column is 1.
# Write the following function to check whether a matrix is a Markov matrix:
# def isMarkovMatrix(m):
# Write a test program that prompts the user to enter a 3 * 3 matrix of numbers and
# tests whether it is a Markov matrix. Here are sample runs:
# Enter a 3-by-3 matrix row by row:
# 0.15 0.875 0.375
# 0.55 0.005 0.225
# 0.30 0.12 0.4
# It is a Markov matrix

def isMarkovMatrix(m):
    isMarkov = True
    for column in range(len(m[0])):
        sumOfColumn = 0
        for row in range(len(m)):
            if m[row][column] < 0:
                isMarkov = False
                break
            sumOfColumn += m[row][column]

        if sumOfColumn != 1:
            isMarkov = False
            break;
    return isMarkov

def test():
    print("Enter a 3-by-3 matrix row by row:")
    inputMatrix = []
    for i in range(3):
        a = [float(x) for x in input().strip().split()]
        inputMatrix.append(a)
    print("It is a Markov matrix" if isMarkovMatrix(inputMatrix) else "It is not a Markov matrix")

test()
