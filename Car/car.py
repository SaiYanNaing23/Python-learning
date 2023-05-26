class Car:
    sterringWheel = 1
    def __init__(self,name,wheels) -> None:
        self.name = name
        self.wheels = wheels

    def drive(self):
        print(f"{self.name} is deiving... with {self.wheels} wheels")

    @classmethod
    def common(cls):
        print(f"All cars have only {cls.sterringWheel} sterringwheel")

