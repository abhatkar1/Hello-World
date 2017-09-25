# (Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
# isPrime(number) function for testing whether a number is prime. Use this
# function to find the number of prime numbers less than 10,000.

#Check whether number is prime

import math

def isPrime(number):
    divisor = 2
    while divisor <= math.sqrt(number):
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

def getPrimeNumbers(n):
    count = 0
    for i in range(n):
        if isPrime(i):
            count += 1
            #print(format(i, "4d"), end =" ")
    return count

def test():
    print("Number of primes less than 10000 are", getPrimeNumbers(10000))

test()