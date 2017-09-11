# (Reverse number) Write a program that prompts the user to enter a four-digit integer
# and displays the number in reverse
# order.
# Here is a sample run:
# Enter an integer: 3125
# The reversed number is 5213

N = eval(input("Enter a four-digit number: "))
strReverseNumber = ''

for i in range(4):
    reverseNumber = N % 10
    N = N // 10
    strReverseNumber += str(reverseNumber)
    
print("The reversed number is", strReverseNumber)