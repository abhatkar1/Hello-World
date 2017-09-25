# (Count consonants and vowels) Write a program that prompts the user to enter a
# text filename and displays the number of vowels and consonants in the file. Use
# a set to store the vowels A, E, I, O, and U.

import os.path
import sys

setOfVowels = {'a','e','i','o','u'}

filename = input("Enter the filename:")

if not os.path.isfile(filename):
    print("The file", filename, "is invalid!")
    sys.exit()

infile = open(filename, "r")

countOfVowels = 0
countOfConsonants = 0

s = infile.read()

for ch in s:
    ch = ch.lower()
    if ch in setOfVowels:
        countOfVowels += 1
    elif ord('a') < ord(ch) <= ord('z'):
        countOfConsonants += 1

print("The file has", countOfVowels, "vowels and", countOfConsonants, "consonants")