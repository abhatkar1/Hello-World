# (Check password) Some Web sites impose certain rules for passwords. Write a
# function that checks whether a string is a valid password. Suppose the password
# rules are as follows:
# ■ A password must have at least eight characters.
# ■ A password must consist of only letters and digits.
# ■ A password must contain at least two digits.
# Write a program that prompts the user to enter a password and displays valid
# password if the rules are followed or invalid password otherwise.

def validatePassword(password):
    countOfDigits = 0
    if len(password) != 8 or password.isalnum() == False:
        return False
    else:
        for i in range(len(password)):
            if password[i].isdigit():
                countOfDigits += 1
        if countOfDigits < 2:
            return False

    return True

def testValidatePassword():
    password = input("Enter password to check its validity:")
    print("The password is valid" if validatePassword(password) else "The password is invalid")

testValidatePassword()