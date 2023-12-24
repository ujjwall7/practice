# jab hum kisi object ko khatam karna chahte hain. 
# Jaise ki agar aapne koi object banaya hai aur uske saath kuch resources judte hain jaise files ya connections,
# toh destructor se aap un resources ko saaf kar sakte hain. __del__ naam ka ek method hota hai

class Student:
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Deleting (Calling destructor)
    def __del__(self):
        print("Student Deleted")


s1 = Student("ujjwal", 14, "M")
del s1 #destructor 


