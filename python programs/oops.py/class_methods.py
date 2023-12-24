#class method jab bnate hai jab aapko object bnana hou using diffrent waylike file params or internet


class Student:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

    @classmethod
    def create_student_using_params(cls, name, age, gender):    # 1 parameter params nhi lega, cls is student class
        obj = cls(name, age, gender)                            # 2 cls
        return obj
    
    @classmethod
    def create_student_using_file(cls, file_name):
        f = open(file_name, "r")
        student_data = f.read()
        name, age, gender = student_data.split()
        f.close()
        obj = cls(name, age, gender)
        return obj

# s1 = Student('Ujjwal Sharma', '21', 'Male')
# s1 = Student.create_student_using_params('Ujjwal Sharma', '21', 'Male')
    
s1 = Student.create_student_using_file('student.txt')
s1.display()















