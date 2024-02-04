def greet():
    # """ Display a greeting to users """
    print('Hi')


greet()
# you can't define because for default param you have to define them from right to left otherwise it will give error
# def function_name(param1=value1, param2, param3):
# Keyword Arguements


def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet('Hello')
print(greeting)
# Answer Hi Hello
# Because when you pass the 'Hello' argument, the greet() function treats it as the first argument, not the second one.
# So you need to pass keyword arguements


def greet(name='there', message='Hi'):
    return f"{message} {name}"


greeting = greet(message='Hello')
print(greeting)
# To improve the readability, Python introduces the keyword arguments.

# The following shows the keyword argument syntax:
# When you use the keyword arguments, their names that matter, not their positions.
# fn(parameter1=value1,parameter2=value2)
#  Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.

# The following will result in an error because it uses the positional argument after a keyword argument:

# net_price = get_net_price(100, tax=0.08, 0.06)
# Code language: Python (python)

# Error:

# SyntaxError: positional argument follows keyword argument

# To fix this, you need to use the keyword argument for the third argument like this:

# net_price = get_net_price(100, tax=0.08, discount=0.06)
# print(net_price)
# All the arguments after the first keyword argument must also be keyword arguments too.



#Variable type agruement passing to function
# def sum(a *b):
#   print(a,b)
# here * is used for assining variables values to b and it acts as tuple here 
# 
# For passing keyword variable length arguement
# def sum(a **b):
# print(a,b)
#  sum('navin',sam:'eru',numb:9,mob:909)
#here doubele ** used here
