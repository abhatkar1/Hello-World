# (Bubble sort) Write a sort function that uses the bubble-sort algorithm. The
# bubble-sort algorithm makes several passes through the list. On each pass,
# successive neighboring pairs are compared. If a pair is in decreasing order,
# its values are swapped; otherwise, the values remain unchanged. The technique
# is called a bubble
# sort
# or sinking sort because the smaller values gradually
# “bubble”
# their way
# to the top and the larger
# values
# “sink” to the bottom.
# Write
# a test program that reads in ten numbers, invokes
# the function, and displays
# the sorted numbers.

def bubbleSort(inputList):

    for i in range(1, len(inputList)):
        for j in range(i):
            if inputList[j] > inputList[j+1]:
                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]

    return inputList

def test():

    inputList = [x for x in input("Enter a list of numbers separated by space").split()]

    print(bubbleSort(inputList))

test()
