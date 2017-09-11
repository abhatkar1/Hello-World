# (Find the two highest scores) Write a program that prompts the user to enter the
# number of students and each student's score, and displays the highest and
# secondhighest scores.

noOfStudents = eval(input("Enter the number of students:"))

secondHighestScore = 0
highestScore = 0
for i in range (0, noOfStudents):
    currentStudentScore = eval(input("Enter the score of the student " + str(i+1) + " :"))
    if (currentStudentScore > highestScore):
        secondHighestScore = highestScore
        highestScore = currentStudentScore
    if (highestScore > currentStudentScore > secondHighestScore):
            secondHighestScore = currentStudentScore

print("The top 2 scores in descending order are", highestScore, "and", secondHighestScore) 