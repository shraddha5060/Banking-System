import os
import datetime

FILE_NAME = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

# Log transaction details
def log_transaction(account_number, transaction_type, amount):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(f"{account_number},{transaction_type},{amount},{date}\n")

# Function to read all accounts from file
def read_accounts():
    if not os.path.exists(FILE_NAME):
        return {}

    accounts = {}
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
               # print(f"Skipping malformed line: {line.strip()}")
                continue
            acc_num, name, balance, password = parts
            try:
                accounts[acc_num] = {
                    "name": name,
                    "password": password,
                    "balance": float(balance)
                }
            except ValueError:
                #print(f"Skipping line with invalid balance: {line.strip()}")
                continue

    return accounts


# Function to update account balance in file
def update_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        for acc_num, details in accounts.items():
            file.write(f"{acc_num},{details['name']},{details['balance']},{details['password']}\n")

# Function to deposit money
def deposit(account_number):
    accounts = read_accounts()
    
    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))
    accounts[account_number]["balance"] += amount
    update_accounts(accounts)

    log_transaction(account_number, "Deposit", amount)
    print(f"Deposit successful! New balance: Rs {accounts[account_number]['balance']}")

# Function to withdraw money
def withdraw(account_number):
    accounts = read_accounts()
    
    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter withdrawal amount: "))
    
    if amount > accounts[account_number]["balance"]:
        print("Insufficient funds!")
        return

    accounts[account_number]["balance"] -= amount
    update_accounts(accounts)

    log_transaction(account_number, "Withdrawal", amount)
    print(f"Withdrawal successful! New balance: Rs {accounts[account_number]['balance']}")
# Function to view transactions for a specific account
def view_transactions(account_number):
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions found.")
        return

    print(f"\nTransaction history for Account {account_number}:")
    print("Type       | Amount   | Date")
    print("-" * 30)
    
    found = False
    with open(TRANSACTIONS_FILE, "r") as file:
        for line in file:
            acc_num, transaction_type, amount, date = line.strip().split(",")
            if acc_num == account_number:
                print(f"{transaction_type:<10} | Rs {amount:<7} | {date}")
                found = True

    if not found:
        print("No transactions available for this account.")

