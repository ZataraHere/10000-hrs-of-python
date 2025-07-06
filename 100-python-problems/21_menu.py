# 	Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
class Menu:

    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            user_input = int(input(
                "\nHello, how would you like to proceed:\n" 
                "1. Enter '1' for cm to ft conversion\n"
                "2. Enter '2' for km to miles conversion\n"
                "3. Enter '3' for USD to INR conversion\n"
                "4. Enter '4' to Exit\n" 
                "Enter your response: "
            ))

            if user_input == 1:
                self.cm_to_ft()
            elif user_input == 2:
                self.km_to_miles()
            elif user_input == 3:
                self.usd_to_inr()
            elif user_input == 4:
                print("Thank you for using the menu. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def cm_to_ft(self):
        cm = float(input("Enter the value in cm: "))
        ft = cm * 0.0328
        print(ft)

    def km_to_miles(self):
        km = float(input("Enter the value in km: "))
        miles = km * 0.621
        print(f"{km} km is {miles:.2f} miles.")

    def usd_to_inr(self):
        usd = float(input("Enter the value in USD: "))
        inr = usd * 85.5
        print(f"{usd} USD is ₹{inr:.2f} INR.")


obj = Menu()
