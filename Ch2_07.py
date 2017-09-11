# (Find the number of years and days) Write a program that prompts the user to
# enter the minutes (e.g., 1 billion), and displays the number of years and days for
# the minutes. For simplicity, assume a year has 365 days. Here is a sample run:
# Enter the number of minutes:
# 1000000000 minutes is approximately 1902 years and 214 days

numberOfMinutes = eval(input("Enter the number of Minutes:"))

numberOfHours = numberOfMinutes // 60

totalNumberOfDays = numberOfHours // 24

numberOfYears = totalNumberOfDays // 365

numberOfDays = totalNumberOfDays % 365

print(numberOfMinutes, "minutes is approximately", numberOfYears, "year(s) and ", numberOfDays, "days")