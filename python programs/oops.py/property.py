class Student:
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender

    def delete_gender(self):
        del self.gender


s1 = Student("ujjwal", 14, "M")
print(f"{s1.age} {s1.gender} {s1.name}")

s1.delete_gender()

# print(f"{s1.age} {s1.gender} {s1.name}")
















