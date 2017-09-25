# (Count the occurrences of each keyword) Write a program that reads in a Python
# source code file and counts the occurrence of each keyword in the file. Your program
# should prompt the user to enter the Python source code filename.

import os.path
import sys

def countWordsInFile(line, countWords):
    lineNoSymbols = removeSymbols(line)
    words = lineNoSymbols.split()
    for word in words:
        if word in countWords:
            countWords[word] += 1
        else:
            countWords[word] = 1


def removeSymbols(line):
    characters = {'!','@','#','$','%','^','&','*','(',')','-','+','=','"','\'','<','>','/','?',';',':',',','.','[',']'}
    for ch in line:
        if ch in characters:
            line = line.replace(ch, ' ')
    return line

def test():
    filename = input("Enter Python source code filename:")

    if not os.path.isfile(filename):
        print("The filename", filename, "is invalid!")
        sys.exit()

    infile = open(filename, "r")

    countWords = {}

    for line in infile:
        countWordsInFile(line, countWords)

    #Starting with highest frequency
    pairs = list(countWords.items())

    reversedPairs = [[x, y] for (y, x) in pairs]

    reversedPairs.sort(reverse=1)

    for i in range(len(reversedPairs)):
        print(format(reversedPairs[i][1], "15") + "\t" + str(reversedPairs[i][0]))

test()