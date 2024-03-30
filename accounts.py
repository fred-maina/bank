from bank_account import Bank  
import random
bank=Bank("KCB BANK")
def account_operations(account_number):
    print("Welcome to your account choose any of the following Services: ")
    try:
        while (True):
            j=int(input("choose 1 for account balance and Information. Choose 2 to deposit choose 3 to withdraw and 4 to exit: "))
            if j == 1:
                bank.displayInformation(account_number)
            elif j == 2:
                amount=int(input("Enter the amount of money you would like to Deposit: "))
                pin=int(input("Input Your PIN"))
                bank.perform_transaction(account_number,pin,"Deposit",amount)
            elif j ==3 :
                amount=int(input("Please Input the amount You would Like to Withdraw: "))
                pin=int(input("Input Your PIN: "))
                bank.perform_transaction(account_number,pin,"Withdraw",amount)
            elif j == 4 :
                print("Thank you for banking with us. Have a Great day")
                break
            else:
                print("Invalid Selection Please Try Again")
    except ValueError as v:
        print(v)
def account_creation():
    try:
        global accountNumber
        accountNumber = random.randint(1000000, 9999999)
        name = input("Enter your Name: ")
        
        # Loop until a valid PIN is entered
        while True:
            pin = input("Choose a 4 digit pin: ")
            if len(pin) != 4 or not pin.isdigit():
                print("Invalid PIN. Please input a 4 digit numeric pin!")
            else:
                pin = int(pin)
                break
        bank.createAccount(accountNumber, name, pin)
        account_operations(accountNumber)
    except ValueError as v:
        print(v)

if __name__ == "__main__" :
    print("Hello There Welcome to KCB Bank Self-service Menu: ")
    try:
        i=int(input("Input 1 if you would like to Create a New Acount or 2 To go to your Account: "))
        if i == 1:
            account_creation()
        elif i == 2:
            try:
                account_operations(accountNumber)
            except NameError as n:
                print("No accounts have been Added Please Create a new Account")
                account_creation()
    except ValueError as v:
        print(v)
