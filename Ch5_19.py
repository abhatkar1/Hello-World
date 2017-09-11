# (Display  a pyramid ) Write a program that prompts the user to enter an integer
# from 1 to 15 and displays a pyramid, as shown in the following sample run:

def DrawPattern(noOfLines):

    for i in range(1, noOfLines+1):
        for j in range((noOfLines)-i):
            print(" ", end = "  ")

        for k in range(i, 0, -1):
            print(format(k, "<3d"), end = "")
            # print(k, end=" ")

        for m in range(1, i):
            # print(m+1, end = " ")
            print(format(m + 1, "<3d"), end="")

        print()


noOfLines = eval(input("Enter the number of lines:"))

DrawPattern(noOfLines)


