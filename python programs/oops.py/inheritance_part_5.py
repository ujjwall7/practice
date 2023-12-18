class Car:
    def __init__(self) -> None:
        self.color = input("Enter Car Colour = ")
        self.type = input("Enter Car Type = ")
        self.mileage = input("Enter Car Mileage = ")
        self.seat_capacity = int(input("Enter Car Seat Capacity = "))

    def base_info(self):
         print(f'Color = {self.color}')    
         print(f'Type = {self.type}')
         print(f'Mileage = {self.mileage}')
         print(f'Seat Capacity = {self.seat_capacity}')

class Audi(Car):
    def __init__(self) -> None:
        super().__init__()    # super means meri upar wali class
        # print("AUDI INIT")
        self.electric = input("Enter Electric = ")
        self.city = input("Enter City = ")
    
    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()


obj = Audi()
obj.show_full_info()
# obj.base_info()
# obj.audi_info()


