from abc import ABC, abstractmethod

# jab aap chahate hou ki method required ho jaye jis jis class mai inherit hua hou
# jis class ke andar abstract class method bna hou vo call nhi hoti

class Car(ABC):
    @abstractmethod
    def sound(self):         # this is abstract method
        print('happy')
        pass

class Audi(Car):
    def __init__(self, engine) -> None:
        self.engine = engine

    def sound(self):
        print("Audi")

obj = Audi("120000cc")
obj.sound()


# print(Car().sound())





