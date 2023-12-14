# class tutorial
class Atm:
    def __init__(self):
        self.pin = ""       # instance variable because its in methods
        self.balance = 0
        self.Menu()

    def Menu(self):      # Methods beacause these are inside the class
        user_input = input('''
            Hello!how would you to proceed?
            1. enter 1 to create pin
            2. enter 2 to deposit
            3. enter 3 to widraw
            4. enter 4 to check balance
            5. enter 5 to exit
            '''"\n\n\n")
        print() 
        if user_input=="1":
            self.Create_Pin()
        elif user_input=="2":
            self.deposit_balance()
        elif user_input=="3":
            self.Withdraw_balance()
        elif user_input=="4":
            self.Check_Balance()
    

    def Create_Pin(self):
        self.pin = input("enter your pin  ")
        print("Pin ceated successfully")

        self.Menu()
    def deposit_balance(self):
        temp_pin = input("enter your pin  ")
        if self.pin == temp_pin:
           amount = int(input("Please enter deposit amout  "))
           self.balance = self.balance+amount
           print("Deposit Successfully")
        else:
            print("Invalid Pin, please enter correct pin.")
        self.Menu()

    def Withdraw_balance(self):
        temp_pin = input("Enter your Pin  ")
        if temp_pin==self.pin:
            amount = int(input("Please enter deposit amout  "))
            self.balance = self.balance-amount
            print("Widraw Successfully")

        else:
            print("Invalid Pin, please enter correct pin.")
        self.Menu()
    
    def Check_Balance(self):
        temp_pin = input("Enter your pin  ")
        if temp_pin==self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
        self.Menu()

hdfc = Atm()
print(hdfc)