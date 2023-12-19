#Access modifiers
# public (jisko object bahar se variables and methods ko call kar skta hai),
#protected (), 
#private (obj bahar se nhi call kr skta private __ lga kar karte hai)

from random import randint



class Bank:
    def __init__(self) -> None:
        self.name = input("Enter your name : ")
        self.__account_no = randint(100010,6241259)
        self.__balance = 0

    def display_balance(self):                              # this is getter jo values get karta hai 
        print(f"balance = {self.__balance}")
    
    def setBalance(self, newamount):                        # this is setter jo values set karta hai 
        self.__balance = newamount

    def display(self):
        print(f"Account number = {self.__account_no}")
        print(f"Name = {self.name}")
        print(f"Balance = {self.__balance}\n")



obj = Bank()
obj.display()
print("#------private ko bhi access kar skte hai-----")
print(f"{obj._Bank__balance = }\n")   # Never do this, name mangling
#obj nam._class name__private variable name
print("#------Balance---------")
obj.setBalance(124)
obj.display_balance()




