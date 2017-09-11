# (Compute the greatest common divisor) For Listing 5.8, another solution to find
# the greatest common divisor of two integers n1 and n2 is as follows: First find
# d to be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ...,
# 2, or 1 is a divisor for both n1 and n2 in this order. The first such common
# divisor is the greatest common divisor for n1 and n2.

number1 = eval(input("Enter first number:"))
number2 = eval(input("Enter second number:"))

if number1 < number2:
    number1, number2 = number2, number1

# divisor = number2 // 2
divisor = number2

GCD = 1

if number1 % number2 == 0:
    GCD = number2
else:
    for i in range (divisor, 0 , -1):
        if (number1 % i == 0) and (number2 % i == 0):
            GCD = i
            break

print("GCD of the two numbers is", GCD)