# Static methods
# Class methods
from datetime import datetime



class Calender:
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event_name):
        self.events.append(event_name)
    
    def display_event(self):
        print(f"Events = {self.events}")

    @staticmethod               #class ke variables access nhi kar sakta
    def is_weekend(date:datetime):
        if date.weekday() > 4:
            print("It is a weekend")
        else:
            print("It is a weekday")


        
obj = Calender()
obj.add_event('Dsa')
obj.add_event('oops')
obj.add_event('Daa')
obj.display_event()

current_date = datetime.now()
Calender.is_weekend(current_date)










