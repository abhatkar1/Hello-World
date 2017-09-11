# (Sum a series) Write a program to sum the following series:

#Note: Can also be done using for loop with steps of 2

def SumInfiniteSeries(N = 97):
    sum = 0
    n = 1
    denominator = 0
    while denominator <= N:


        numerator = 2 * n - 1
        denominator = numerator + 2

        sum += (numerator/denominator)
        n += 1
    return format(sum, ".2f")


sumOfSeries = SumInfiniteSeries()

print(sumOfSeries)