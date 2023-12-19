# many forms
# same name methods ho jiska object banega usko prefrence milega
# poly mor phism = ek hi method ke alag alag forms hai 

class Animal:
    def sound(self):
        print("Animal speaking")

class Dog(Animal):
    def sound(self): 
        print("Bhaw Bhaw Bhaw") 

class Cat(Animal):
    def sound(self):
        print("Meow Meow Meow")


obj = Dog()
obj.sound()









