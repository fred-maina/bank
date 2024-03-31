def verify_pin(func):
    """
    Decorator function to verify the PIN before performing a transaction.

    Parameters:
        func (function): The function to be decorated.

    Returns:
        function: Decorated function.
    """
    def wrapper(self, account_number, pin, transactionType, amount, *args, **kwargs):
        """
        Wrapper function to verify the PIN before performing a transaction.

        Parameters:
            self (object): The instance of the class.
            account_number (int): The account number.
            pin (int): The PIN of the account.
            transactionType (str): Type of transaction (e.g., "Deposit", "Withdraw").
            amount (float): The amount of money involved in the transaction.
            *args (tuple): Additional positional arguments.
            **kwargs (dict): Additional keyword arguments.

        Returns:
            None
        """
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return func(self, account_number, pin, transactionType, amount, *args, **kwargs)
        else:
            print("Invalid PIN. Transaction denied.")

    return wrapper


class Transaction:
    """
    Class representing a transaction.

    Attributes:
        transactionType (str): Type of transaction.
        amount (float): Amount of money involved in the transaction.
    """

    def __init__(self, transactionType, amount):
        """
        Initialize a Transaction object.

        Parameters:
            transactionType (str): Type of transaction (e.g., "Deposit", "Withdraw").
            amount (float): Amount of money involved in the transaction.
        """
        self.transactionType = transactionType
        self.amount = amount


class Account:
    """
    Class representing a bank account.

    Attributes:
        account_number (int): The account number.
        account_holder (str): Name of the account holder.
        pin (int): PIN of the account.
        balance (float): Current balance of the account.
    """

    def __init__(self, account_number, account_holder, pin, initialBalance=0):
        """
        Initialize an Account object.

        Parameters:
            account_number (int): The account number.
            account_holder (str): Name of the account holder.
            pin (int): PIN of the account.
            initialBalance (float): Initial balance of the account (default is 0).
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initialBalance
        self.pin = pin

    def deposit(self, amount):
        """
        Deposit money into the account.

        Parameters:
            amount (float): The amount of money to be deposited.

        Returns:
            None
        """
        self.balance += amount
        print(f"Successfully deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Parameters:
            amount (float): The amount of money to be withdrawn.

        Returns:
            None
        """
        if amount > self.balance:
            print(f"Insufficient funds to withdraw {amount}")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn {amount}. New balance is {self.balance}")

    def check_balance(self):
        """
        Check the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.balance


class Bank:
    """
    Class representing a bank.

    Attributes:
        name (str): The name of the bank.
        accounts (dict): Dictionary to store accounts (key: account number, value: Account object).
    """

    def __init__(self, name):
        """
        Initialize a Bank object.

        Parameters:
            name (str): The name of the bank.
        """
        self.name = name
        self.accounts = {}

    def createAccount(self, accountNum, accountHolder, pin, initialBalance=0):
        """
        Create a new bank account.

        Parameters:
            accountNum (int): The account number.
            accountHolder (str): Name of the account holder.
            pin (int): PIN of the account.
            initialBalance (float): Initial balance of the account (default is 0).

        Returns:
            None
        """
        if accountNum in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[accountNum] = Account(accountNum, accountHolder, pin, initialBalance)
            print(f"Account created successfully with initial balance of {initialBalance}. Your account number is {accountNum}")

    @verify_pin
    def perform_transaction(self, account_number, pin, transactionType, amount):
        """
        Perform a transaction on a bank account.

        Parameters:
            account_number (int): The account number.
            pin (int): PIN of the account.
            transactionType (str): Type of transaction (e.g., "Deposit", "Withdraw").
            amount (float): The amount of money involved in the transaction.

        Returns:
            None
        """
        if account_number not in self.accounts:
            print("Account does not exist!")
        else:
            account = self.accounts[account_number]
            if transactionType == "Deposit":
                account.deposit(amount)
            elif transactionType == "Withdraw":
                account.withdraw(amount)
            else:
                print("Invalid transaction type")

    def displayInformation(self, account_number):
        """
        Display information about a bank account.

        Parameters:
            account_number (int): The account number.

        Returns:
            None
        """
        if account_number not in self.accounts:
            print("Account does not exist")
        else:
            account = self.accounts[account_number]
            print(f"Account Holder: {account.account_holder}. Account Number: {account.account_number}. Account Balance: {account.check_balance()}")
