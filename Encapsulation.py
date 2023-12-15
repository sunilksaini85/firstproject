class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()
    def menu(self):
        user_input = input('''
                Hello!how would you to proceed?
                1. enter 1 to create pin
                2. enter 2 to deposit
                3. enter 3 to widraw
                4. enter 4 to check balance
                5. enter 5 to exit
                '''"\n\n\n")
        
        if user_input=="1":
            self.Create_Pin()
         
        elif user_input=="2":
            self.deposit_balance()
        elif user_input=="3":
            self.Withdraw_balance()
        elif user_input=="4":
            self.Check_Balance()

    def Create_Pin(self):
        self.__pin = input("Create your new pin ")
        print("pin created successfully")

    def get_pin(self):       # Getter method
        return self.__pin
    
    def set_pin(self,new):  #setter method
        self.__pin = new
        print(self.__pin, "pin successfuly set")

sbi = Atm()
print()
print()
print(sbi.get_pin())
print()
print()
print(sbi.set_pin(88978))
print()
print()
print(sbi.get_pin())
print()
