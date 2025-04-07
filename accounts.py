import random
import os
from transaction import deposit, withdraw ,view_transactions # Corrected import

# File to store account details
FILE_NAME = "accounts.txt"

# Function to create a new account
def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    
    # Generate a random 6-digit account number
    account_number = random.randint(100000, 999999)
    print(f"Your account number: {account_number} ")
    # Take password input
    password = input("Enter a password: ")

    # Save account details to a file
    with open(FILE_NAME, "a") as file:
        file.write(f"{account_number},{name},{initial_deposit},{password}\n")

    print("\nAccount created successfully!")

# Function to read all accounts from file
def read_accounts():
    if not os.path.exists(FILE_NAME):
        return {}

    accounts = {}
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                #print(f"Skipping malformed line: {line.strip()}")
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


def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    accounts = read_accounts()

    if account_number in accounts and accounts[account_number]["password"] == password:
        print("\nLogin successful!")
        print(f"Welcome, {accounts[account_number]['name']}! Your current balance is Rs {accounts[account_number]['balance']}.")

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. View Transaction")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                deposit(account_number)  # Deposit function from transaction.py
            elif choice == "2":
                withdraw(account_number)# Withdraw function from transaction.py
            elif choice=="3":
                view_transactions(account_number)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid account number or password. Please try again.")

def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the banking system
if __name__ == "__main__":
    main()
