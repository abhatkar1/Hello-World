# (Count the letters in a string) Write a function that counts the number of letters in
# a string using the following header:
# def countLetters(s):
# Write a test program that prompts the user to enter a string and displays the number
# of letters in the string.

def countLetters(s):
    count = 0
    for i in range(len(s)):
        if s[i].isalpha():
            count += 1
    return count

def testCountLetter():

    s = input("Enter the string:")
    print("The number of letters in the string are:", countLetters(s))

testCountLetter()
