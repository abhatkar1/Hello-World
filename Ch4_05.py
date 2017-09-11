# (Find future dates) Write a program that prompts the user to enter an integer for
# today's day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and display
# the future day of the week. Here is a sample run:
# 
# Enter today's day: 1
# Enter the number of days elapsed since today: 3
# Today is Monday and the future day is Thursday

Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = 0,1,2,3,4,5,6

today = eval(input("Enter the day of the week:"))

futureDaysToAdd = eval(input("Enter the number of days elapsed since today:"))

futureDayNo = (today + futureDaysToAdd) % 7


if today == 0:
    todayDay = "Sunday"
elif today == 1:
    todayDay = "Monday"
elif today == 2:
    todayDay = "Tuesday"
elif today == 3:
    todayDay = "Wednesday"
elif today == 4:
    todayDay = "Thursday"
elif today == 5:
    todayDay = "Friday"
else:
    todayDay = "Saturday"


if futureDayNo == 0:
    futureDay = "Sunday"
elif futureDayNo == 1:
    futureDay = "Monday"
elif futureDayNo == 2:
    futureDay = "Tuesday"
elif futureDayNo == 3:
    futureDay = "Wednesday"
elif futureDayNo == 4:
    futureDay = "Thursday"
elif futureDayNo == 5:
    futureDay = "Friday"
else:
    futureDay = "Saturday"
    
print("Today is", todayDay, "and future day is", futureDay)
