class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize=batterysize
my_tesla=ElectricCar("Tesla","Model S","85kwh")
print(my_tesla)
