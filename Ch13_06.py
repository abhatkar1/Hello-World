# Count words) Write a program that counts the number of words in President
# Abraham Lincoln’s Gettysburg Address from http://cs.armstrong.edu/liang/data/
# Lincoln.txt.

import urllib.request

urlInput = urllib.request.urlopen(r"http://cs.armstrong.edu/liang/data/Lincoln.txt")

s = urlInput.read().decode()

count = 0

listOfWords = s.strip().split()

for word in listOfWords:
    word = word.strip(',')
    word = word.strip('.')
    if word.isalpha() or '\'' in word:
        count += 1

print("Number of words in President Abraham Lincoln's Gettysburg Address:", count)