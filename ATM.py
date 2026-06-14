balance = 10000
transactions = 0

while True:

    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice = "))

    match choice:

        case 1:
            print(f"Current balance = ₹{balance}")

        case 2:
            amount = int(input("Enter amount to deposit = ₹"))

            while amount <= 0:
                print("Amount must be greater than 0.")
                amount = int(input("Enter amount to deposit = ₹"))

            balance += amount
            transactions += 1

            print("Deposit successful!")
            print(f"Current balance = ₹{balance}")

        case 3:
            amount = int(input("Enter amount to withdraw = ₹"))

            while amount <= 0 or amount > balance:
                if amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    print("Insufficient balance.")

                amount = int(input("Enter amount to withdraw = ₹"))

            balance -= amount
            transactions += 1

            print("Withdrawal successful!")
            print(f"Current balance = ₹{balance}")

        case 4:
            print("\n------ SESSION SUMMARY ------")
            print(f"Final balance = ₹{balance}")
            print(f"Total transactions = {transactions}")
            print("Thank you for using the ATM.")
            break

        case _:
            print("Invalid choice. Please enter a number from 1 to 4.")