# (Science: day of the week) Zeller's congruence is an algorithm developed by
# Christian Zeller to calculate the day of the week. The formula is
# Write a program that prompts the user to enter a year, month, and day of the
# month, and then it displays the name of the day of the week. Here are some sample
# runs:
# Enter year: (e.g., 2008): 2013
# Enter month: 1-12: 1
# Enter the day of the month: 1-31: 25
# Day of the week is Friday

import math

inputYear = eval(input("Enter year:"))
inputMonth = eval(input("Enter month: 1-12:"))
inputDay = eval(input("Enter the day of the month: 1-31:"))

q = inputDay # day of the month

if inputMonth > 2:
    m = inputMonth #month
    j = math.floor(inputYear / 100) #century 
    k = inputYear % 100 #year of the century
else:
#     for Jan and Feb month is 13 and 14 of PREVIOUS year
    m = inputMonth + 12 # month 
    j = math.floor((inputYear - 1) / 100) #century
    k = (inputYear - 1) % 100 

#Using Zeller's congruence formula
h = (q + math.floor((26 * (m + 1)) / 10) + k + math.floor(k / 4) 
     + math.floor(j / 4) + 5 * j) % 7

#Using dictionary to store the code for the days
ReturnDay = {
        0 : "Saturday",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday"
}

day = ReturnDay[h]

print("Day of the week is", day)
