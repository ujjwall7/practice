class Father:
    father_name = ""

    def displayFatherName(self):
        print(self.father_name)

class Mother(Father):
    mother_name = ""

    def displayMotherName(self):
        print(self.mother_name)

class Child(Mother):
    child_name = ""

    def displayChildName(self):
        print(self.child_name)


obj = Child()
obj.father_name = "ujjwal sharma"
obj.mother_name = "gunjan sharma"
obj.child_name = "shiva sharma"

obj.displayFatherName()
obj.displayMotherName()
obj.displayChildName()



