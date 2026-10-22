balance = 0
transactions = []

def check_balance():
    print("\nCurrent Balance: ₹", balance)


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Invalid amount!")
    else:
        balance += amount
        transactions.append("Deposited: ₹" + str(amount))
        print("Amount deposited successfully!")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append("Withdrawn: ₹" + str(amount))
        print("Please collect your cash.")


def transaction_history():
    print("\n===== TRANSACTION HISTORY =====")

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transaction_history()

    elif choice == "5":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice! Try again.")
