class Car:
    def __init__(self,name,modal):
        self.__name=name
        self.__modal=modal
    @property
    def model(self):
        return self.__modal
#if you want  a property don't want to change then define property decorator @property 

