# By definition, a method is a function that is bound to an instance of a class.
# So when you define a function inside a class, 
# it’s purely a function. However, 
# when you access that function via an object, the function becomes a method.
class Request:
    def send(se):
        print('Sent',se)

variable=Request()
variable.send()
# Python always implicitly passes the object to the method as the first argument and we get error 

# Instance variables are bound to a specific instance of a class.
# Python stores instance variables in the __dict__ attribute of the instance. Each instance has its own __dict__ attribute and the keys in this __dict__ may be different.
