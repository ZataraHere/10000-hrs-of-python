class Atm:

    def __init__(self):
        self.balance = 0
        self.pin = ""
        self.menu()

    def menu(self):
        while True:
            user_input = int(input(
                "\nHello, how would you like to proceed:\n"
                "1. Create PIN\n"
                "2. Deposit Cash\n"
                "3. Withdraw Cash\n"
                "4. Check Balance\n"
                "5. Exit\n"
                "Enter your choice: "
            ))

            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.check_balance()
            elif user_input == 5:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.pin = input("Set your PIN: ")
        print("PIN created successfully!")

    def deposit(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid PIN")

    def withdraw(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid PIN")

    def check_balance(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print("Your current balance is: Rs", self.balance)
        else:
            print("Invalid PIN")
