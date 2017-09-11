# (Game: pick a card ) Write a program that simulates picking a card from a deck of
# 52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
# Here is a sample run of the program:
# The card you picked is the Jack of Hearts

import random

rank = random.randint(1,13)
suit = random.randint(1,4)

# The program could have also been done using random.choice(Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# Jack, Queen, King) and similaryly for suit
RankDictionary = {
    1 : "Ace",
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10: 10,
    11 : "Jack",
    12 : "Queen",
    13 : "King"
        }

SuitDictionary = {
    1 : "Clubs",
    2 : "Diamonds",
    3 : "Hearts",
    4 : "Spades"
    }

print("The card you picked is the", RankDictionary[rank], "of", SuitDictionary[suit])