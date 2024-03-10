class Account:
    def __init__(self, account_number, password, balance):
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

def main():
    # Sample account data
    account = Account("123456789", "password123", 1000.0)

    # Login
    print("Welcome to the Bank Management System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Simple authentication
    if password == account.password:
        print("Login successful!")

        # Main menu
        while True:
            print("\nMain Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print("Deposit successful. Current balance:", account.balance)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful. Current balance:", account.balance)
                else:
                    print("Insufficient balance!")
            elif choice == "3":
                print("Current balance:", account.balance)
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice!")

    else:
        print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()



            
                    