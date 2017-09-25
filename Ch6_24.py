# (Palindromic prime) A palindromic prime is a prime number that is also palin-
# dromic. For example, 131 is a prime and also a palindromic prime, as are 313 and
# 757. Write a program that displays the first 100 palindromic prime numbers. Display
# 10 numbers per line and align the numbers properly,
# as follows:
#   2     3     5     7    11   101   131   151   181   191
# 313   353   373   383   727   757   787   797   919   929

def reverse(n):
    reversedNum = ""
    while n > 0:
        reversedNum += str(n % 10)
        n //= 10
    return int(reversedNum)

def isPalindrome(n):
    if n == reverse(n):
        return True
    else:
        return False

def isPrime(n):
    divisor = 2
    while divisor <= (n ** 0.5):
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def isPalindromicPrime(n):
    count = 0
    number = 101
    while count < n:
        if isPalindrome(number) and isPrime(number):
            count += 1
            print(format(number, "7d"), end = " ")
            if count % 10 == 0:
                print()
        number += 1

isPalindromicPrime(100)