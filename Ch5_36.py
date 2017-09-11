# (Game: scissor, rock, paper) Programming Exercise 4.17 gives a program that
# plays the scissor, rock, paper game. Revise the program to let the user play continuously
# until either the user or the computer wins more than two
# times.
#
# 4.17
# (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
# game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap
# a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws. Here are sample runs:
# scissor (0), rock (1), paper (2): 1
# The computer is scissor. You are rock. You won.
# scissor (0), rock (1), paper (2): 2
# The computer is paper. You are paper too. It is a draw.

import random

gameDictionary = {
    0: "Scissor",
    1: "Rock",
    2: "Paper"
}


userWins = 0
compWins = 0
while userWins <= 2 and compWins <= 2:
    userChoice = eval(input(("scissor (0), rock (1), paper (2):")))
    compChoice = random.randint(0, 2)
    difference = compChoice - userChoice
    if userChoice == compChoice:
        msg = "The computer is " + gameDictionary[compChoice] + ". You are " + gameDictionary[userChoice] + " too. It is a draw."
    elif difference % 3 == 1:
        msg = "The computer is " + gameDictionary[compChoice] + ". You are " + gameDictionary[userChoice] + ". Sorry, you lost."
        compWins += 1
    elif difference % 3 == 2:
        msg = "The computer is " + gameDictionary[compChoice] + ". You are " + gameDictionary[userChoice] + ". Congratulations, you won."
        userWins += 1
    print(msg)

if userWins >= 2:
    print("You won the series.")
else:
    print("You lost the series.")