# PYTHON-BANK-MANAGEMENT-PROJECT

The project is a simple Bank Management System implemented in Python. It uses classes, JSON for persistent storage, and basic input/output. Here is a breakdown of its components and working:

1. Imports

json: Used for reading and writing account information to a JSON file (data.json).

random and string: Used for generating random account numbers with letters, digits, and special characters.

pathlib.Path: Used to check if the data.json file exists before reading.

2. Bank Class

The entire functionality is wrapped inside the Bank class.

Class Variables

database: Stores the file name data.json.

data: Holds the list of user accounts (dictionaries). If the file exists, it loads data from JSON, otherwise prints a warning.

Private Methods

__update: Writes the current Bank.data into data.json as a JSON string.

__generateaccno: Creates a unique account number consisting of 3 letters, 3 digits, and 1 special character.

3. Public Methods

These methods simulate different banking operations:

createaccount
Collects user details (name, age, email, pin).
Validates: age must be 18 or above, pin must be exactly 4 digits.
Generates an account number and initializes balance to 0.
Adds the new account to Bank.data and updates the JSON file.

depositmoney
Prompts for account number and pin.
Searches for the matching user.
Validates the deposit amount (must be >0 and ≤100000).
Updates the balance and saves changes.

withdrawmoney
Prompts for account number and pin.
Searches for the user.
Validates the withdrawal amount (must be >0 and ≤ balance).
Deducts the balance and saves changes.

checkdetails
Prompts for account number and pin.
Displays all user details except balance, which is printed separately in a formatted way.

updatedetails
Prompts for account number and pin.
Allows updating name, email, or pin.
Skipped fields remain unchanged.
Keeps other data (age, account number, balance) intact.
Saves updates to JSON.

deleteaccount
Prompts for account number and pin.
If found, asks for confirmation (y/n).
If confirmed, deletes the account from Bank.data and updates JSON.

4. User Interface (Main Menu)

At the end, the program prints a simple menu:

1: Create account

2: Deposit money

3: Withdraw money

4: View details

5: Update details

6: Delete account

It then takes a numeric input and calls the corresponding method of the Bank object (user).

5. Overall Working

Data Persistence: Account details are stored in data.json so that accounts are preserved between runs.

Input/Output: All interactions are text-based through the console.

Security: Account access is verified by matching both account number and pin.

Error Handling: If a JSON error or missing file occurs, the program catches the exception and prints a message.

#OUTPUTS

<img width="543" height="323" alt="Image" src="https://github.com/user-attachments/assets/d7cfb3d9-1ab6-422e-b3e6-d3c90d670cae" />

<img width="533" height="235" alt="Image" src="https://github.com/user-attachments/assets/2034fb6b-ee1d-4232-b9bb-03cc09e2c299" />

<img width="539" height="242" alt="Image" src="https://github.com/user-attachments/assets/10673be0-9966-44be-9e27-2cc1eec140a7" />

<img width="531" height="284" alt="Image" src="https://github.com/user-attachments/assets/b27d8762-66ae-47db-98b8-88b3fec8937d" />

<img width="535" height="346" alt="Image" src="https://github.com/user-attachments/assets/b4bba298-30c7-4d37-b0d8-5ea2ea0e9764" />

<img width="534" height="194" alt="Image" src="https://github.com/user-attachments/assets/e7a76333-03a5-4f5a-a71f-fe71013e31ed" />

