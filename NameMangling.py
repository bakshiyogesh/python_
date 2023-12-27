#if you prefix an attribute name with double underscores(__) like this:
#__attribute
#python will automatically change name of __attribute to:

#_class__attribute
#This is called name mangling in python
# By doing this, you cannot access the __attribute directly from the outside of a class like:

# instance.__attribute
#However you can acess it using the_class_attribute name:
#instancre._class__attribute
class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))