# (Remove text) Write a program that removes all the occurrences of a specified
# string from a text file. Your program should prompt the user to enter a filename
# and a string to be removed. Here is a sample run:
# Enter a filename:test.txt
# Enter the string to be removed: morning
# Done

import os.path

filePath = input("Enter the absolute file name (e.g. C:\\Users\\Program.txt) :")
stringToBeRemoved = input("Enter the string to be removed:")

if (os.path.isfile(filePath)):
    inFile = open(filePath, "r")

    listOfLinesToWrite = []

    for line in inFile:
        while stringToBeRemoved in line:
            line = line.replace(stringToBeRemoved, "").strip()

        listOfLinesToWrite.append(line)
    inFile.close()
    
    outFile = open(filePath, "w")
    for line in listOfLinesToWrite:
        outFile.write(line + "\n")
    outFile.close()



