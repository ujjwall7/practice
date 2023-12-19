class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter father name : ")
        self._bank_balance = int(input("Enter father bank balance : "))
        self.__phone = int(input("Enter Phone Model : "))

    def __str__(self) -> str:
        return f"Father name = {self.father_name}\nFather Bank Balance = {self._bank_balance}\nFather Phone = {self.__phone}\n"

    def displayFather(self) -> None:
        print(f"Father name = {self.father_name}")
        print(f"Father Bank Balance = {self._bank_balance}")
        print(f"Father Phone = {self.__phone}")


obj_1 = Father()
obj_2 = Father()
print()
# obj.displayFather()
print(obj_1)
print(obj_2)











