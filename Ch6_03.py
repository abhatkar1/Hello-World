# (Palindrome integer) Write the functions with the following headers:
# # Return the reversal of an integer, e.g. reverse(456) returns
# # 654
# def reverse(number):
# # Return true if number is a palindrome
# def isPalindrome(number):
# Use the reverse function to implement isPalindrome. A number is a palindrome
# if its reversal
# is the same as itself. Write a test program that prompts the
# user
# to enter an integer
# and reports whether the integer
# is a palindrome.
import time
def reverse(number):
    reverseNumber = ''
    while number > 0:
        reverseNumber += str(number % 10)
        number //= 10
    return reverseNumber

def isPalindrome(number):
    if str(number) == reverse(number):
        return "Palindrome"
    else:
        return "not Palindrome"

def test():
    number = eval(input("Enter a number to check if Palindrome:"))
    # a = time.time()
    # print("The number", number, "is", isPalindrome(number))
    # b = time.time()
    # print("Time taken: ", (b - a), "seconds")

test()