# (Sum the digits in an integer) Write a program that reads an integer between 0 and
# 1000 and adds all the digits in the integer. For example, if an integer is 932, the
# sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
# operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
# 10 = 93.) Here is a sample run: 
# Enter a number between 0 and 1000: 999
# The sum of the digits is 27

N = eval(input("Enter a number between 0 and 100:"))

sumOfDigits = 0

while N > 0:
    sumOfDigits += N % 10
    N = N // 10
    
print("Sum of the digits is", sumOfDigits)    