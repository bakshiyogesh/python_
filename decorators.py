#to define decorator we need to define a function inside a function for eg 
def timer(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f"{func.__name__}")
        return result
    return wrapper

@timer
def example_function(num):
    return num **2

example_function(3)
