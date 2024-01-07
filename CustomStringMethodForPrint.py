#To customize the string represenstation of an instance of a class
# The class needs to implement __str__ method
#Python will call __str__ method automatically

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'
person=Person("Chattarpati Shiva ji","Maharaj",20)
print(person)