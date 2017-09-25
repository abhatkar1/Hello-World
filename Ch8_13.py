# (Longest common prefix) Write a method that returns the longest common prefix
# of two strings. For example, the longest common prefix of distance and
# disinfection is dis. The header of the method is:
# def prefix(s1, s2)
# If the two strings have no common prefix, the method returns an empty string.
# Write a main method that prompts the user to enter two strings and displays their
# common prefix.

def prefix(s1, s2):
    longestPrefix = ""
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    for i in range(len(s1)):
        if s2.startswith(s1[:i+1]):
            longestPrefix = s1[:i+1]
    return longestPrefix

def main():
    string1 = input("Enter string1:")
    string2 = input("Enter string2:")

    print("The longest common prefix is", prefix(string1, string2))

main()

