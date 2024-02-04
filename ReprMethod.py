class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


person = Person('John', 'Doe', 25)
# use str()
print(person)

# use repr()
print(repr(person))
# The __str__ method returns a string representation of an object that is human-readable 
# while the __repr__ method returns a string representation of an object that is machine-readable.
