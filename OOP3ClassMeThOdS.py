#Class method is not bound to any instance .They are bound to only class
#To define class methods we use class decorator- @classmethod

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}.I'm {self.age}"
    @classmethod
    def create_anonymous(cls):
        print(cls,"class")
        return Person("John","Doe",25)

Person.create_anonymous()
# The create_anonymous() method cannot access instance attributes. But it can access class attributes via the cls variable

#ClassName.method_name()
# When a method creates an instance of the class and returns it, the method is called a factory method. 
# For example, the create_anonymous() is a factory method because it returns a new instance of the Person class.