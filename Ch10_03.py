# (Count occurrence of numbers) Write a program that reads some integers
# between 1 and 100 and counts the occurrences of each. Here is a sample run of
# the program:
# Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2
# 2 occurs 2 times
# 3 occurs 1 time
# 4 occurs 1 time
# 5 occurs 2 times
# 6 occurs 1 time
# 23 occurs 1 time
# 43 occurs 1 time

inputList = [eval(x) for x in input("Enter integers between 1 and 100 separated by space (e.g. 1 2 3):").split()]

newList = []
for i in range(len(inputList)):
    if inputList[i] not in newList:
        newList.append(inputList[i])

newList.sort()

for j in newList:
    print(j, "occurs", inputList.count(j), "times" if inputList.count(j) > 1 else "time")

