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

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 1200 )

    def getMonthlyInterest(self):
        return (self.__balance * self.getMonthlyInterestRate())

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

def testAccount():
    account1 = Account(id=1122, balance=20000, annualInterestRate=4.5)
    account1.withdraw(2500)
    account1.deposit(3000)
    print("Account1 Details:")
    print("Id =", account1.getId())
    print("Balance =", account1.getBalance())
    print("Monthly Rate =", account1.getMonthlyInterestRate())
    print("Monthly Interest =", account1.getMonthlyInterest())


testAccount()


