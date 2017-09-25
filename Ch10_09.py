# (Statistics: compute deviation) Exercise 5.46 computes the standard deviation of
# numbers. This exercise uses a different but equivalent formula to compute the
# standard deviation of n numbers.

# To compute the standard deviation with this formula, you have to store the
# individual numbers using a list, so that they can be used after the mean is
# obtained.
# Your program should contain the following functions:
# # Compute the standard deviation of values
# def deviation(x):
# # Compute the mean of a list of values
# def mean(x):
#
# Write a test program that prompts the user to enter a list of numbers and displays
# the mean and standard deviation, as shown in the following sample run:
# Sample Run:
# Enter numbers: 1.9 2.5 3.7 2 1 6 3 4 5 2
# The mean is 3.11
# The standard deviation is 1.55738

import math


def deviation(x):
    meanOfX = mean(x)
    # print(type(meanOfX))
    xMinusMean = [math.pow(eval(format((i - meanOfX),".2f")), 2) for i in x]
    # print(sum(xMinusMean))
    return format(math.sqrt(sum(xMinusMean) / (len(x) - 1)), ".5f")


def mean(x):
    return eval(format(sum(x)/len(x), ".2f"))

def test():
    listOfNumbers = [eval(x) for x in input("Enter a list of numbers separated by space:").split()]

    print("The mean is:", mean(listOfNumbers))

    print("The standard deviation is:", deviation(listOfNumbers))

test()