# (Sort students) Write a program that prompts the user to enter the students’
# names and their scores on one line, and prints student names in increasing order
# of their scores. (Hint: Create a list. Each element in the list is a sublist with two
# elements: score and name. Apply the sort method to sort the list. This will sort
# the list on scores.)
# Enter students’ names and scores: John 34 Jim 45 Peter 59 Tim 45
# John 34
# Jim 45
# Tim 45
# Peter 59

def reverseIndices(listOfStudentAndScores):
    for i in range(len(listOfStudentAndScores)):
        listOfStudentAndScores[i][0], listOfStudentAndScores[i][1] = listOfStudentAndScores[i][1], \
                                                                     listOfStudentAndScores[i][0]
    return listOfStudentAndScores

inputLine = input("Write students' names and scores on one line (e.g. John 34 Jim 45 Peter 59 Tim 45): ")

# listOfStudentAndScores = [[x,y] for x in inputLine.strip().split() if x.isalpha() for y in inputLine.strip().split() if y.isdigit()]
listOfStudentAndScores = []
listOfInputElements = inputLine.strip().split()

studentCounter = 0
elementCounter = 0
isEnd = False
while not isEnd:
    if elementCounter == len(listOfInputElements):
        isEnd = True
    else:
        if elementCounter % 2 == 0:
            listOfStudentAndScores.append([])
            studentCounter += 1

        listOfStudentAndScores[studentCounter - 1].append(listOfInputElements[elementCounter])

        elementCounter += 1

reverseIndices(listOfStudentAndScores)
listOfStudentAndScores.sort()
reverseIndices(listOfStudentAndScores)

for i in range(len(listOfStudentAndScores)):
    for element in listOfStudentAndScores[i]:
        print(format(element, "10"), end=" ")
    print()


# print(listOfStudentAndScores)