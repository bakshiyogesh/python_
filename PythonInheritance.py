# A class can reuse another class by inheriting it. When a child class inherits from a parent class, the child class can access the attributes and methods of the parent class.
class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)

class Employee(Person):
    def __init__(self, name, age, job_title):
        print(self,"self variable here tells what:")
        super().__init__(name, age)
        self.job_title = job_title
    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."
#To override the method in parent in child component we use super() 
employee=Employee("Rishab",20,"developer")
employee.greet()
#If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
# storage west // output
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
# storage east //output