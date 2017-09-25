# (Financial: credit card number validation) Credit card numbers follow certain
# patterns: It must have between 13 and 16 digits, and the number must start with:
# ■ 4 for Visa cards
# ■ 5 for MasterCard credit cards
# ■ 37 for American Express cards
# ■ 6 for Discover cards
# In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card num-
# bers. The algorithm is useful to determine whether a card number is entered correctly
# or whether a credit card is scanned correctly by a scanner.
# Credit card
# numbers
# are generated following
# this validity
# check, commonly known
# as the
# Luhn
# check
# or the Mod 10 check, which can be described as follows (for illustration,
# consider the card number 4388576018402626):
# 1. Double every second digit from right to left. If doubling of a digit results in a
# two-digit number, add up the two digits to get a single-digit number.
# 2. Now add all single-digit numbers from Step 1.
# 4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37
# 3. Add all digits in the odd places from right to left in the card number.
# 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38
# 4. Sum the results from Steps 2 and 3.
# 37 + 38 = 75
# 5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise,
# it is invalid. For example, the number 4388576018402626 is invalid, but the
# number 4388576018410707 is valid.
# Write a program that prompts the user to enter a credit card number as an  integer.
# Display whether the number is valid or invalid. Design your program to use the
# following functions:
# # Return true if the card number is valid
# def isValid(number):
# # Get the result from Step 2
# def sumOfDoubleEvenPlace(number):
# # Return this number if it is a single digit, otherwise, return
# # the sum of the two digits
# def getDigit(number):
# # Return sum of odd place digits in number
# def sumOfOddPlace(number):
# Return true if the digit d is a prefix for number
# def prefixMatched(number, d):
# # Return the number of digits in d
# def getSize(d):
# # Return the first k number of digits from number. If the
# # number of digits in number is less than k, return number.
# def getPrefix(number, k):

VISA_CARD_PREFIX = 4
MASTER_CARD_PREFIX = 5
DISCOVER_CARD_PREFIX = 6
AMEX_CARD_PREFIX = 37

# Return true if the card number is valid
def isValid(number):

    if 13 < getSize(number) < 16:
        return "Invalid"
    else:
        for i in VISA_CARD_PREFIX, MASTER_CARD_PREFIX, DISCOVER_CARD_PREFIX, AMEX_CARD_PREFIX:
            if prefixMatched(number, i):
                break
            else:
                return "Invalid"

        #Performing the Luhn check (Mod 10 check)
        sumOfDoubleEvenPlaceNumbers = sumOfDoubleEvenPlace(number)
        sumOfOddPlacedNumbers = sumOfOddPlace(number)
        if (sumOfDoubleEvenPlaceNumbers + sumOfOddPlacedNumbers) % 10 == 0:
            result = "Valid"
        else:
            result = "Invalid"
        return result

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sum = 0
    position = 0
    while number > 0:
        position += 1
        if position % 2 == 0:
            sum += getDigit(2 * (number % 10))
        number //= 10
    return sum




# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    digit = 0
    if number // 10 <= 0:
        digit = number
    else:
        digit += (number % 10) + (number // 10)
    return digit


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sum = 0
    position = 0
    while number > 0:
        position += 1
        if position % 2 != 0:
            sum += (number % 10)
        number //= 10
    return sum



# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    strNumber = str(number)
    sizeOfD = getSize(d)
    prefix = getPrefix(number, sizeOfD)
    if prefix == d:
        return True
    else:
        return False

# Return the number of digits in d
def getSize(d):
    return len(str(d))



# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    sizeOfNumber = getSize(number)
    if sizeOfNumber > k:
        strNumber = str(number)
        firstKDigits = int(strNumber[:k])
        return firstKDigits
    else:
        return number

def main():
    cardNumber = eval(input("Enter the card number:"))
    print("The number you entered is", isValid(cardNumber))

main()