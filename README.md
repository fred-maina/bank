# Bank Management System

This project is a Python-based Bank Management System designed for practicing Python programming skills. It covers many basic python skills.
Feel free to contribute and fork these repo. 

## Project Overview

The Bank Management System consists of several classes:

### `Transaction` Class
- Represents a transaction with attributes for transaction type and amount.

### `Account` Class
- Represents a bank account with attributes for account number, account holder, PIN, and balance.
- Includes methods for depositing, withdrawing, and checking balance.

### `Bank` Class
- Represents a bank with attributes for bank name and a dictionary of accounts.
- Includes methods for creating accounts, performing transactions, and displaying account information.

## Usage

1. **Creating an Account:**
   - Users can create a new account by providing their name and choosing a 4-digit PIN.
   - The account number is generated automatically.

2. **Performing Transactions:**
   - Users can perform transactions such as deposits and withdrawals.
   - Each transaction requires the account number and PIN for validation.

3. **Displaying Account Information:**
   - Users can view their account information including the account holder's name, account number, and balance.

4. **Self-Service Menu:**
   - Users are presented with a self-service menu upon running the program, where they can choose to create a new account or access an existing account.

## Code Highlights.

- **Validation:** The system ensures that the PIN entered during account creation is exactly 4 digits long and consists only of numeric characters.
- **Decorator Usage:** The `verify_pin` decorator is used to verify the PIN before allowing transactions to proceed, enhancing security.
- **Random Account Number Generation:** The system generates a random account number for each new account, ensuring uniqueness.

## Implementation

To run the Bank Management System, execute the following command:

```bash
python accounts.py

