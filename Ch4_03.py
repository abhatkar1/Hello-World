# (Algebra: solve 2x2 linear equations) You can use Cramer's rule to solve the
# following 2x2 system of linear equation:
# ax + by = e
# cx + dy = f
#   x = (ed - bf) / (ad - bc)
#   y = (af - ec) / (ad - bc)
# Write a program that prompts the user to enter a, b, c, d, e, and f and display the
# result. If ad - bc is 0, report that The equation has no solution.
# Enter a, b, c, d, e, f:
# 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
# x is -2.0 and y is 3.0
# 
# Enter a, b, c, d, e, f:
# 1.0, 2.0, 2.0, 4.0, 4.0, 5.0
# The equation has no solution

a,b,c,d,e,f = eval(input("Enter 6 values for a, b, c, d, e and f:"))

discriminant = (a * d - b * c)

result = ''

if discriminant == 0:
    result += "The equation has no solution."
else:
    x = (e * d - b * f) / discriminant
    y = (a * f - e * c) / discriminant
    result = "x is " + format(x, ".1f") + " and y is " + format(y, ".1f")

print(result)