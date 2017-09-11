# (Financial application: compute future tuition) Suppose that the tuition for a
# university is $10,000 this year and increases 5% every year. Write a program
# that computes the tuition in ten years and the total cost of four years' worth
# of tuition starting ten years from now.

tuition = 10000
increaseRate = 0.05
noOfYears = 10
tuitionAfterTenYears = 0
totalCostStartingTenYearsFromNow = 0
for i in range(0,14):
    tuition = tuition * (1 + increaseRate)
    if i == 9:
        tuitionAfterTenYears = tuition
    if i >= 10:
        #starting ten years from now means he would start with fees for 11th
        #year, hence i = 10
        totalCostStartingTenYearsFromNow += tuition

print("The tuition in ten years would be", format(tuitionAfterTenYears,".2f"))
print("The total cost of four years' worth of tuition starting ten years from now would be", format(totalCostStartingTenYearsFromNow,".2f"))