# The Time class) Design a class named Time. The class contains:
# ■ The private data fields hour, minute, and second that represent a time.
# ■ A constructor that constructs a Time object that initializes hour, minute, and
# second using the current time.
# ■ The get methods for the data fields hour, minute, and second, respectively.
# ■ A method named setTime(elapseTime) that sets a new time for the object
# using the elapsed time in seconds. For example, if the elapsed time is 555550
# seconds, the hour is 10, the minute is 19, and the second is 12.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that creates a Time object and displays its hour, minute, and second.
# Your program then prompts the user to enter an elapsed time, sets its elapsed
# time in the Time object, and displays its hour, minute, and second. Here is a
# sample run:
# Current time is 12:41:6
# Enter the elapsed time:
# The hour:minute:second for the elapsed time is 22:41:45
# 55550505
# (Hint: The initializer will extract the hour, minute, and second from the elapsed
# time. The current elapsed time can be obtained using time.time(), as shown in
# Listing 2.7, ShowCurrentTime.py.)

import datetime

class Time:
    def __init__(self):
        currentTime = datetime.datetime.now()
        self.__hour = currentTime.hour
        self.__minute = currentTime.minute
        self.__second = currentTime.second

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapsedTime):
        hours = elapsedTime // 3600
        # days = hours // 24
        self.__hour = hours % 24
        elapsedTime = elapsedTime % 3600
        self.__minute = elapsedTime // 60
        elapsedTime = elapsedTime % 60
        self.__second = elapsedTime

def testTime():
    time1 = Time()
    print("Current time is ", time1.getHour(), ":", time1.getMinute(), ":", time1.getSecond())
    elapsedTime = eval(input("Enter the elapsed time in seconds:"))

    time1.setTime(elapsedTime)

    print("The Hour:Minute:Second for elapsed time is", time1.getHour(), ":", time1.getMinute(), ":", time1.getSecond())

testTime()
