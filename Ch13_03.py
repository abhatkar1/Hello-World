# (Process scores in a text file) Suppose that a text file contains an unspecified number
# of scores. Write a program that reads the scores from the file
# and displays their total and average. Scores are separated by blanks. Your program should prompt
# the user to enter a filename. Here is a sample run:
# Enter a filename: scores.txt
# There are 70 scores
# The total is 800
# The average is 33.33

import os.path
fileName = input("Enter the file name:")
if os.path.isfile(fileName):
    inFile = open(fileName, "r")
    listOfScores = []
    for line in inFile:
        Scores = [float(x) for x in line.strip().split()]
        listOfScores.extend(Scores)
    noOfScores = len(listOfScores)
    total = sum(listOfScores)
    average = total / noOfScores

    print("There are",noOfScores,"scores")
    print("The total is",total)
    print("The average is",average)


