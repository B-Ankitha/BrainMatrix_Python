import time

# User class to represent a bank account
class User:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

# ATM class to handle user authentication and operations
class ATM:
    def __init__(self):
        self.users = {}  # To store user data (account_number -> User)
        self.logged_in_user = None

    def add_user(self, account_number, pin, balance=0):
        self.users[account_number] = User(account_number, pin, balance)

    def authenticate_user(self, account_number, pin):
        if account_number in self.users:
            user = self.users[account_number]
            if user.pin == pin:
                self.logged_in_user = user
                return True
        return False

    def show_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def atm_operations(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == '1':
                print(f"Your balance is: ${self.logged_in_user.check_balance()}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    self.logged_in_user.deposit(amount)
                    print(f"Deposited ${amount}. New balance: ${self.logged_in_user.check_balance()}")
                else:
                    print("Invalid amount")
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    result = self.logged_in_user.withdraw(amount)
                    if result == "Insufficient funds":
                        print("Error: Insufficient funds")
                    else:
                        print(f"Withdrawn ${amount}. New balance: ${self.logged_in_user.check_balance()}")
                else:
                    print("Invalid amount")
            elif choice == '4':
                print("Exiting ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an ATM instance and add some users
atm = ATM()
atm.add_user(account_number="123456", pin="1234", balance=500)
atm.add_user(account_number="654321", pin="4321", balance=1000)

def main():
    print("Welcome to the Python ATM!")
    while True:
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if atm.authenticate_user(account_number, pin):
            print("Authentication successful!")
            atm.atm_operations()
            break
        else:
            print("Invalid account number or PIN. Please try again.")

# Run the ATM
if __name__ == "__main__":
    main()
