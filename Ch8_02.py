# (Check substrings) You can check whether a string is a substring of another string
# by using the find method in the str class. Write your own function to implement
# find. Write a program that prompts the user to enter two strings and then checks
# whether the first string is a substring of the second string.

def checkSubstring(mainString, substring):
    # if substring in mainString:
    #     return True
    # else:
    #     return False
    for i in range(len(mainString)):
        if (i + len(substring)) <= len(mainString):
             if mainString[i: i + len(substring)] == substring:
                 return True
    return False

def test():

    subString = input("Enter the substring:")
    mainString = input("Enter the main string:")

    if checkSubstring(mainString, subString):
        print("Substring part of main string")
    else:
        print("Substring not part of main string")

test()