
#Getter and setter
#The getter and setter methods provide an interface for accessing an instance attribute:
#The getter returns the value of an attribute
#The setter sets a new value for an attribute


#class Person:
#   def __init__(self,name,age):
#       self.name=name
#       self.set_age(age)
#   def set_age(self,age):
#       if age <=0:
#           raise ValueError('The age must be positive')
#       self._age=age
#   def get_age(self):
#       return self._age
# john=Person("john",18)
# john.set_age(-20)
# set_age(30)

#To define a getter and setter method while achieving backward compatibility, you can use the property() class.

#The Python property class
#The property class returns a property object. The property() class has the following syntax:
property(fget=None, fset=None, fdel=None, doc=None)

#fget function to get value of the attribute or Getter
#fset fucntion to set value of the attribute
#fdel function to delete value of the attribute
#doc is docsting i.e.,a comment

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

age = property(fget=get_age, fset=set_age)

