class Student:
    def __init__(self):
        self.name = input("Enter the name = ")
        self.age = int(input("Enter the age = "))

    def display_info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")

    def chage_name(self, new_name:str):
        self.name = new_name

obj = Student()
obj.display_info()
obj.chage_name("Shivaji maharaj")
obj.display_info()
