# (Reverse the numbers entered ) Write a program that reads a list of integers and
# displays them in the reverse order in which they were read.

listOfIntegers = [x for x in input("Enter integers separated by space").split()]
listOfIntegers.reverse()
print("Reverse order:")
for i in listOfIntegers:
    print(i, end = " ")
