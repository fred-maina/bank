from bank_account import Bank  # Importing Bank class from bank_account module
import random

bank = Bank("Py Bank")  # Creating an instance of Bank class with the bank name "Py Bank"

def account_operations(account_number):
    """
    Function to perform operations on a bank account.

    Parameters:
        account_number (int): The account number of the bank account.

    Returns:
        None
    """
    print("Welcome to your account. Choose any of the following services: ")
    while True:
        try:
            j = int(input("Choose 1 for account balance and information. Choose 2 to deposit. Choose 3 to withdraw. Choose 4 to exit: "))
            if j == 1:
                bank.displayInformation(account_number)
            elif j == 2:
                amount = int(input("Enter the amount of money you would like to deposit: "))
                pin = int(input("Input your PIN: "))
                bank.perform_transaction(account_number, pin, "Deposit", amount)
            elif j == 3:
                amount = int(input("Please input the amount you would like to withdraw: "))
                pin = int(input("Input your PIN: "))
                bank.perform_transaction(account_number, pin, "Withdraw", amount)
            elif j == 4:
                print("Thank you for banking with us. Have a great day!")
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError as v:
            print("Invalid selection. Please try again.")

def account_creation():
    """
    Function to create a new bank account.

    Parameters:
        None

    Returns:
        None
    """
    try:
        global accountNumber
        accountNumber = random.randint(1000000, 9999999)  # Generate a random account number
        name = input("Enter your name: ")
        
        # Loop until a valid PIN is entered
        while True:
            pin = input("Choose a 4 digit PIN: ")
            if len(pin) != 4 or not pin.isdigit():
                print("Invalid PIN. Please input a 4 digit numeric PIN!")
            else:
                pin = int(pin)
                break
        bank.createAccount(accountNumber, name, pin)  # Create a new account
        account_operations(accountNumber)  # Perform account operations for the newly created account
    except ValueError as v:
        print(v)

if __name__ == "__main__":
    print("Hello there! Welcome to Py-Bank Self-service Menu: ")
    try:
        i = int(input("Input 1 if you would like to create a new account or 2 to go to your account: "))
        if i == 1:
            account_creation()  # Create a new account
        elif i == 2:
            try:
                account_operations(accountNumber)  # Perform account operations for an existing account
            except NameError as n:
                print("No accounts have been added. Please create a new account.")
                account_creation()  # If no accounts exist, create a new account
    except ValueError as v:
        print(v)
