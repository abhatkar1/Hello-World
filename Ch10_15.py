# (Sorted?) Write the following function that returns true if the list is already
# sorted in increasing order:
# def isSorted(lst):
# Write a test program that prompts the user to enter a list and displays whether the
# list is sorted or not. Here is a sample run:

# Enter list: 1 1 3 4 4 5 7 9 10 30 11
# The list is not sorted
#
# Enter list: 1 1 3 4 4 5 7 9 10 30
# The list is already sorted

#Insertion-sort

def isListSorted(listOfNumber):
    isSort = False
    # sortedList = [] + listOfNumber
    sortedList = list(listOfNumber)
    print(sortList(sortedList))
    if sortList(sortedList) == listOfNumber:
        isSort = True

    return isSort

def sortList(sortedList):
    for i in range(1, len(sortedList)):

        currentElement = sortedList[i]
        k = i - 1

        while k >= 0 and currentElement < sortedList[k]:
            sortedList[k + 1] = sortedList[k]
            k -= 1

        sortedList[k + 1] = currentElement

    return sortedList


def test():

    inputList = [eval(x) for x in input("Enter integeres separated by space").split()]

    print("The list is sorted" if isListSorted(inputList) else "The list is not sorted")


test()


