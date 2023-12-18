class Student:
    def __init__(self):
        print('----------New Input Created-----------')
        self.name = input("Enter the name : ")
        self.roll_no = input("Enter the Roll_No. : ")
        self.age = input("Enter the age : ")
        self.gender = input("Enter the Gender : ")
        print('----------New Input Ended-----------')
        print()

    #methods
    def info(self):
        #-----------New--------------------
        print(f'Name = {self.name}')
        print(f'Roll_no     = {self.roll_no}')
        print(f'Age = {self.age}')
        print(f'Gender = {self.gender}')
        print()
        #-------------Ended---------------



s1 = Student()
s2 = Student()
s1.info()
s2.info()



# s1.name = 'ujjwal'
# s1.roll_no = '12345'
# s1.gender = 'Female'
# s1.age = '23'


# s1.name = 'ujjwal'
# s1.roll_no = '12345'
# print(s1.name)
# print(s1.roll_no)
# print('-------------')
# s2.name = 'gunjan'
# s2.roll_no = 'gunjan gaur'
# print(s2.name)
# print(s2.roll_no)










