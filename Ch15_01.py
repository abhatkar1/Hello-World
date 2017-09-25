# (Sum the digits in an integer using recursion) Write a recursive function that computes
# the sum of the digits in an integer.
# Use the following
# function header:
# def sumDigits(n):
# For example, sumDigits(234) returns Write a test program
# that prompts the user to enter an integer and displays its sum.
# 2 + 3 + 4 = 9.


def sumDigits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sumDigits(n // 10)

def test():
    n = eval(input("Enter a number:"))
    print("Sum of the digits is", str(sumDigits(n)))

test()