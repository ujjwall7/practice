class Car:
    def __init__(
            self, color: str, type: str, mileage: str, seat_capacity: int
            ) -> None:
        # self.color - > Class Variable , color upar se aa rha hai vo parameter
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
    def __init__(self) -> None:
        print("Audi init")

# obj = Car("Blue",
#           "Petrol",
#           "100KMH",
#            8)
# obj.base_info()

obj = Audi()
obj.color = "Black"
obj.type = "Petrol"
obj.mileage = "144KMH"
obj.seat_capacity = "25"
obj.base_info()


