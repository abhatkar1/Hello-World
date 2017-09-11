# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total. Here's a sample run:
# Enter the subtotal and a gratuity rate: 15.69, 15
# The gratuity is 2.35 and the total is 18.04

subTotal = eval(input("Enter the subtotal:"))
gratuityRate = eval(input("Enter the gratuity rate:"))

gratuityAmt = subTotal * gratuityRate / 100

totalAmt = subTotal + gratuityAmt

print("Gratuity: ", round(gratuityAmt,2))

print("Total: ", round(totalAmt,2))