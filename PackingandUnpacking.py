# like js we can destructure the tuples an list into multiple variables
#but in python it is known as unpacking variables
color=['red','yellow']
red,blue=color # but how many variables are you unpacking these are almost equal to in the list.
#otherwise it gives error to many values to unpack
#by putting (*) in front of a variable name whose elements are left they stored in last variable
colors=['green','blue','yellow','red','purple']
red,yellow,*blue=colors
for index,value in enumerate(colors): #we used enumerate function here to acess index of element of a list 
    print(f"{index}: {value}")
    #enumerate() returns a tuple that contains the current index and element of the list.
# To find the index of an element in a list, you use the index() function.
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

result = cities.index('Mumbai')
print("index is:",result)
# in operator to check value exist or not and give boolean value true or false