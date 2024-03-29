# Bank Management System

This project is a Python-based Bank Management System designed for practicing Python programming skills.

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

## Code Highlights

- **Validation:** The system ensures that the PIN entered during account creation is exactly 4 digits long and consists only of numeric characters.
- **Decorator Usage:** The `verify_pin` decorator is used to verify the PIN before allowing transactions to proceed, enhancing security.
- **Random Account Number Generation:** The system generates a random account number for each new account, ensuring uniqueness.

## Implementation

To run the Bank Management System, execute the following command:

```bash
python bank_management_system.py
'''
### Future Improvements

1. **Enhanced Error Handling**: Implement more robust error handling mechanisms throughout the code to handle unexpected user inputs or system errors gracefully.

2. **User Authentication**: Strengthen user authentication by implementing more secure methods such as hashing user passwords before storing them.

3. **Transaction History**: Add functionality to keep track of transaction history for each account, allowing users to review past transactions.

4. **User Interface**: Improve the user interface by creating a graphical user interface (GUI) using libraries like Tkinter or PyQt, making the banking experience more intuitive and user-friendly.

5. **Data Persistence**: Implement data persistence by integrating a database system (e.g., SQLite, MySQL) to store account information securely and enable data retrieval even after the program is closed and reopened.

6. **Account Types**: Introduce different types of accounts (e.g., savings, checking) with varying features and interest rates.

7. **Security Enhancements**: Implement additional security features such as two-factor authentication (2FA) or transaction verification codes to further protect user accounts from unauthorized access.

8. **Transaction Limits**: Set limits on transaction amounts or frequency to prevent potential fraud or misuse of accounts.

9. **Multi-Currency Support**: Add support for multiple currencies to allow users to perform transactions in different currencies based on their needs.

10. **Automated Tests**: Develop automated tests to ensure the reliability and correctness of the codebase, covering various scenarios and edge cases.
