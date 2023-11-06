# A tuple is a list that cannot change.
#  Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.                                                                                                                                                                                             
# A tuple is like a list except that it uses parentheses () instead of square brackets []
# Since a tuple is immutable, you cannot change its elements. The following example attempts to change the first element of the rgb tuple to 'yellow':

rgb = ('red', 'green', 'blue')
rgb[0] = 'yellow'
#it will throw error   
# To define a tuple with one element, you need to include a trailing comma after the first element. For example:

numbers = (3,)
print(type(numbers))