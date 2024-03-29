def verify_pin(func):
    def wrapper(self, account_number, pin,transactionType,amount, *args, **kwargs):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return func(self, account_number,pin,transactionType,amount, *args, **kwargs)
        else:
            print("Invalid PIN. Transaction denied.")
    return wrapper
class Transaction():
    def __init__(self,transactionType,amount):
        self.transactionType=transactionType
        self.amount=amount
class Account:
    def __init__(self,account_number,account_holder,pin,initialBalance=0):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=initialBalance
        self.pin=pin
    def deposit(self,amount):
        self.balance += amount
        print(f"Successfully  deposited {amount} New balance is {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient funds to withdraw {amount}")
        else:
            self.balance -= amount
            print(f"Successfully Withdrawn {amount}. New balance is {self.balance}")
    def check_balance(self):
        return self.balance
class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts={}
    def createAccount(self,accountNum,accountHolder,pin,initialBalance=0):
        if accountNum in self.accounts:
            print("Account already Exists!")
        else:
            self.accounts[accountNum]=Account(accountNum,accountHolder,pin,initialBalance)
            print(f"Account Created Successfully with initial balance of {initialBalance} Your account number is {accountNum}")
    @verify_pin
    def perform_transaction(self,account_number,pin,transactionType,amount):
        if account_number not in self.accounts:
            print("Account Does not Exist!")
        else:
            account=self.accounts[account_number]
            if transactionType == "Deposit" :
                account.deposit(amount)
            elif transactionType == "Withdraw" :
                account.withdraw(amount)
            else:
                print("Invalid Transaction Type")
    def displayInformation(self,account_number):
        if account_number not in self.accounts:
            print("Account does not exist")
        else:
            account=self.accounts[account_number]
            print(f"Account Holder: {account.account_holder} Account Number : {account.account_number} Account balance : {account.check_balance()}")


