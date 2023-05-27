# from Car.car import Car
# from Car.functions import checkEngine
# lambo = Car.common()
# checkEngine()

class Car:
    sterringWheel = 1
    def __init__(self,name,wheels) -> None:
        self.name = name
        self.wheels = wheels

    def drive(self):
        print(f"{self.name} is driving with {self.wheels} wheels")
    
    @classmethod 
    def common(cls):
        print(f"All cars have only {cls.sterringWheel} sterring Wheel")

Marceedee = Car("marcedee",5)
Marceedee.drive()
# print(Car.sterringWheel)
# Car.common()