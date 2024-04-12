import re
import time

pattern = re.compile(r'^(?=.*[a-z]|[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}|:<>?/~`])[A-Za-z\d!@#$%^&*()_+{}|:<>?/~`]{8,}$')


class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Welcome to Bank System")

    def CashCredit(self):
        amount = float(input("Enter amount to be credited: "))
        self.balance += amount
        print("\n Amount Credited:", amount)

    def CashWithdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Withdraw:", amount)
        else:
            print("\n Insufficient balance  ")

    def Display(self):
        print("\n Available Balance=", self.balance)

    def CheckPwd(self, password):
        if bool(pattern.match(password)) and password[0].isupper():
            return True
        return False

    def loggedIn(self):
        time.sleep(5)
        print("Logged in successfully to Bank System")
        self.CashCredit()
        self.CashWithdraw()
        self.Display()


acc = Bank_Account()

inputPwd1 = input("Enter the Password: ")

if not acc.CheckPwd(inputPwd1):
    print("Enter a valid password")
else:
    inputPwd2 = input("Confirm Password again: ")

    if inputPwd1 == inputPwd2:
        print("Successfully changed password")
        acc.loggedIn()
    else:
        print("Invalid credentials")
