# lamda functions
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


Proper_name = get_full_name(
    'Shri Krishna',
    'Maharaj',
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(Proper_name)

#Pyhton lamda in loop
callabes=[]
for i in (1,2,3,4):
    callabes.append(lamda a=i:a)
for f in callabes:
    print(f())

callables=[]
for i in (1,2,3,4):
    callables.append(lamda a=i:a)
for f in callables:
    print(f())
# result will be [4,4,4,4] because lambda  expression refering to  i variable not current value.  

def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b
name=add.__doc__
#To acess the __doc__ property of a  function use function.__doc__
print(name)

#we can also use help() function to get documentation of a function
