class Student:
    def __init__(self, name, age, gender) -> None:
        self._name = name
        self._age = age
        self._gender = gender
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, NewGender):
        self._gender = NewGender


s1 = Student("Ujjwal sharma", 23, "Male")
print(f"{s1.gender = }")

s1.gender = "Female"
print(f"{s1.gender = }")



























