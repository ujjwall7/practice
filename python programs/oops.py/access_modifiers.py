# protected (single under score use to protected neeche wali class bhi access kar paye variable ko)
# jo protected hota hai vo object se access nhi hota hai

class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter father name : ")
        self._bank_balance = int(input("Enter father bank balance : "))
        self.__phone = int(input("Enter Phone Model : "))

    def displayFather(self) -> None:
        print(f"Father name = {self.father_name}")
        print(f"Father Bank Balance = {self._bank_balance}")
        print(f"Father Phone = {self.__phone}")

class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name = input("Enter child name : ")

    def displayChildInfo(self):
        print(f"Child name = {self.child_name}")
        print(f"Father name = {self.father_name}")
        print(f"Father Bank Balance = {self._bank_balance}")




obj = Child()
obj.displayChildInfo()













