class Atm:

    __counter = 1        # class variable
    def __init__(self):
        self.__pin = ""      #  Instance variable
        self.__balance = 0
        self.sno = Atm.__counter
        self.sno = Atm.__counter+1
        print(self.sno)

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
            self.create_pin()

    def create_pin(self):
        self.__pin = str(input("Enter your pin "))
        print(self.__pin,"Pin created successfully.")

    def get_pin(self):
        # print(self.__pin)
        return self.__pin
    
    def set_pin(self,new):
        if type(new)==str:
            self.__pin = new
            # print(self.__pin)

hdfc = Atm()
# print(hdfc)
print()
print()

print()
print(hdfc.get_pin())
print()
print()
print()
print(hdfc.set_pin("8789"))
print()
print()
print()
print(hdfc.get_pin())


