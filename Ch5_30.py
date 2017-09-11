# (Display the first days of each month) Write a program that prompts the user
# to enter the year and first day of the year, and displays the first day of each month
# in the year on the console. For example, if the user entered year 2013, and 2 for
# Tuesday, January 1, 2013, your program should display the following output:
# January 1, 2013 is Tuesday
# ...
# December 1, 2013 is Sunday

import calendar

def checkLeapYear(year):
    isLeapYear = False
    if year % 4 == 0 and year % 100 != 0:
        isLeapYear = True
    if year % 400 == 0:
        isLeapYear = True

    return isLeapYear

days ={
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

year = eval(input("Enter the year:"))

print(days)

firstDayOfYear = eval(input("Choose the first day of the year and enter 0 for Sunday, 1 for Monday, and so on:"))

JanuaryLikeMonths = [1, 3, 5, 7, 8, 10, 12]
AprilLikeMonths = [4, 6, 9, 11]

FirstDayOfMonth = [firstDayOfYear]

# For fetching first day of February, we add no of days in January
for i in range(1, 12):
    firstDay = 0
    if i in JanuaryLikeMonths:
        firstDay = (firstDayOfYear + 31) % 7
        FirstDayOfMonth.append(firstDay)
    elif i in AprilLikeMonths:
        firstDay = (firstDayOfYear + 30) % 7
        FirstDayOfMonth.append(firstDay)
    else:
        isLeapYear = checkLeapYear(year)
        if isLeapYear:
            firstDay = (firstDayOfYear + 29) % 7
        else:
            firstDay = (firstDayOfYear + 28) % 7
        FirstDayOfMonth.append(firstDay)
    firstDayOfYear = firstDay

for j in range(1, len(FirstDayOfMonth)+1):
    print(calendar.month_name[j], "1 is", days[FirstDayOfMonth[j - 1]])
