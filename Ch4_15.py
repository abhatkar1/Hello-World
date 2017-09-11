# (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
# number. The program prompts the user to enter a three-digit number and determines
# whether the user wins according to the following
# rules:
# 1. If the user input matches the lottery number in the exact order, the award is
# $10,000.
# 2. If all the digits in the user input match all the digits in the lottery number, the
# award is $3,000.
# 3. If one digit in the user input matches a digit in the lottery number, the award is
# $1,000.

import random

lotteryNumber = random.randint(100,999)
# print(lotteryNumber)
userNumber = eval(input("Enter the 3 digit ticket number:"))

lotteryNumber1 = lotteryNumber % 10

lotteryNumber2 = (lotteryNumber // 10) % 10

lotteryNumber3 = (lotteryNumber // 100) % 10

userNumber1 = userNumber % 10

userNumber2 = (userNumber // 10) % 10

userNumber3 = (userNumber // 100) % 10

result = ''

if userNumber == lotteryNumber:
    result = "Perfect match! Congratulations! You won $10,000!"
elif ((userNumber1 == lotteryNumber1 and userNumber2 == lotteryNumber3 and userNumber3 == lotteryNumber2) or
       (userNumber1 == lotteryNumber2 and ((userNumber2 == lotteryNumber3 and userNumber3 == lotteryNumber1) or 
                                           (userNumber2 == lotteryNumber1 and userNumber3 == lotteryNumber3))) or
      (userNumber1 == lotteryNumber3 and ((userNumber2 == lotteryNumber1 and userNumber3 == lotteryNumber2) or 
                                           (userNumber2 == lotteryNumber2 and userNumber3 == lotteryNumber1)))):
    result = "Three digits match! Congratulations! You won $3,000!"
elif ((lotteryNumber1 == userNumber1 or lotteryNumber1 == userNumber2 or lotteryNumber1 == userNumber3 or  
    lotteryNumber2 == userNumber1 or lotteryNumber2 == userNumber2 or lotteryNumber2 == userNumber3 or 
    lotteryNumber3 == userNumber1 or lotteryNumber3 == userNumber2 or lotteryNumber3 == userNumber3)):
    result = "One or Two digits match! Congratulations! You won $1,000!"
else:
    result = "Sorry, better luck next time."    
print(result,"\nThe lottery number is", lotteryNumber)