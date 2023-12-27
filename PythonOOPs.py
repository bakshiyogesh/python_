class Person:
    pass
# Python is dynamic. It means that you can add an attribute to an instance of a class dynamically at runtime.
# For example, the following adds the name attribute to the person object:
person=Person()
person.name = 'John'

# However, if you create another Person object, the new object won’t have the name attribute.
# To define and initialize an attribute for all instances of a class, you use the __init__ method. The following defines the Person class with two instance attributes name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# When you create a Person object, Python automatically calls the __init__ method to initialize the instance attributes. In the __init__ method, the self is the instance of the Person class.
# The following creates a Person object named person:
person = Person('John', 25)

# Like a class attribute, a class method is shared by all instances of the class.
#  The first argument of a class method is the class itself.
#  By convention, its name is cls.
#  Python automatically passes this argument to the class method.
#  Also, you use the @classmethod decorator to decorate a class method.

class Persona:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Persona.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        print(cls,"checking for cls what it defines")
        return Persona('Anonymous', 22)
# @staticmethod decorator to decorate a class method 
    @staticmethod
    def create_anonymous():
        print('static method ')

personaClass=Persona("mn",80);
personaClass.create_anonymous()
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.
# To call a static method, you use the ClassName.static_method_name() syntax. For example:  
# f = TemperatureConverter.celsius_to_fahrenheit(30)
# print(f)  # 86