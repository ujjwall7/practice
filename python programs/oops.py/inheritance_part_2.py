class Car:
    def set_info(
            self, color: str, type: str, mileage: str, seat_capacity: int
            ) -> None:
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
         print(f'Color = {self.color}')    
         print(f'Type = {self.type}')
         print(f'Mileage = {self.mileage}')
         print(f'Seat Capacity = {self.seat_capacity}')

class Audi(Car):
    def set_audi_info(self, electric: bool, city: str):
        self.electric = electric
        self.city = city
    
    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")


obj = Audi()
obj.set_info("Blue",
            "Petrol",
            "100KMH",
            8)
obj.set_audi_info(True, "Faridabad")
obj.base_info()
obj.audi_info()



