# (Game: ATM machine) Use the Account class created in Exercise 7.3 to simulate
# an ATM machine. Create ten accounts in a list with the ids 0, 1, ..., 9, and an initial
# balance of $100. The system prompts the user to enter an id. If the id is entered
# incorrectly,
# ask the user to enter a correct id. Once an id is accepted, the main
# menu is displayed as shown in the sample run. You can enter a choice of 1 for
# viewing the current balance, 2 for withdrawing money, 3 for depositing money,
# and 4 for exiting the main menu. Once you exit, the system will prompt for an id
# again. So, once the system starts, it won’t stop.
#
# Enter an account id: 4
# Main menu
# 1: check balance
# 2: withdraw
# 3: deposit
# 4: exit

# 7.3
# (The Account class) Design a class named Account that contains:
# ■ A private int data field named id for the account.
# ■ A private float data field named balance for the account.
# ■ A private float data field named annualInterestRate that stores the current
# interest rate.
# ■ A constructor that creates an account with the specified id (default 0), initial
# balance (default 100), and annual interest rate (default 0).
# ■ The accessor and mutator methods for id, balance, and annualInterestRate.
# ■ A method named getMonthlyInterestRate() that returns the monthly
# interest rate.
# ■ A method named getMonthlyInterest() that returns the monthly interest.
# ■ A method named withdraw that withdraws a specified amount from the
# account.
# ■ A method named deposit that deposits a specified amount to the account.
# Draw the UML diagram for the class, and then implement the class. (Hint: The
# method getMonthlyInterest() is to return the monthly interest amount, not
# the interest rate. Use this formula to calculate the monthly interest: balance *
# monthlyInterestRate. monthlyInterestRate is annualInterestRate
# / 12. Note that annualInterestRate is a percent (like 4.5%). You need to
# divide it by 100.)
# Write a test program that creates an Account object with an account id of 1122, a
# balance of $20,000, and an annual interest rate of 4.5%. Use the withdraw
# method to withdraw $2,500, use the deposit method to deposit $3,000, and print
# the id, balance, monthly interest rate, and monthly interest.

class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getID(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getRate(self):
        return self.__annualInterestRate

    def setID(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setRate(self, rate):
        self.__annualInterestRate = rate

    def getMonthlyInterestRate(self):
        return float(format(self.__annualInterestRate / 12, ".3f"))

    def getMonthlyInterest(self):
        return (self.__balance * self.getMonthlyInterest())

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

def ATMGame():
    listOfAccounts = []

    for i in range(10):
        listOfAccounts.append(Account(i))

    while True:
        inputID = eval(input("Enter Account ID:"))

        isFound = False

        for account in listOfAccounts:
            if inputID == account.getID():
                isFound = True
                while True:
                    print("Main menu")
                    print("1: Check Balance")
                    print("2: Withdraw")
                    print("3: Deposit")
                    print("4: Exit")
                    choice = eval(input())

                    if choice == 1:
                        print("The balance is:",account.getBalance())
                    elif choice == 2:
                        amount = eval(input("Enter amount to withdraw:"))
                        account.withdraw(amount)
                    elif choice == 3:
                        amount = eval(input("Enter amount to deposit:"))
                        account.deposit(amount)
                    else:
                        break
        if not isFound:
            print("Incorrect ID!")

ATMGame()
