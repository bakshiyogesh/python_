# Private attributes can be only accessible from the methods of the class. 
# In other words, they cannot be accessible from outside of the class.

# Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class.

# By convention, you can define a private attribute by prefixing a single underscore (_):

class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0
counter=Counter()
counter._current=3
# If you prefix an attribute name with double underscores (__) like this:
#__attrbute
# Python will automatically change the name of the __attribute to:
# _class__attribute
# This is called the name mangling in Python.
# By doing this, you cannot access the __attribute directly from the outside of a class like:

#instance.__attribute
# However, you still can access it using the _class__attribute name:

# instance._class__attribute