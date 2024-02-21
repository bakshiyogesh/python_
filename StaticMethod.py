#in static methods we doesnot need to pass a self agruement to function 
#It is defined by using @@staticmethod
class Car:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def general():
        print("general method as I.E static method.")
print(Car.general())
