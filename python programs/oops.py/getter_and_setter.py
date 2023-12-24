class Student:      

    def get_values(self):
        print(f"{self.age} {self.gender} {self.name}")

    def set_values(self, name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender


s1 = Student()
s1.set_values('ujjwal', 10, 'M')
s1.get_values()























