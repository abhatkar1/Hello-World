# (Display matrix of 0s and 1s) Write a function that displays an n-by-n matrix using
# the following header:
# def printMatrix(n):
# Each element is 0 or 1, which is generated randomly. Write a test program that
# prompts the user to enter n and displays an n-by-n matrix. Here is a sample run:
# Enter n: 3
# 0 1 0
# 0 0 0
# 1 1 1

import random

def printMatrix(n):
    for j in range(n):
        for i in range(n):
            element = random.randint(0, 1)
            print(element, end = " ")
        print()

def test():
    n = eval(input("Enter the value of n:"))
    printMatrix(n)

test()