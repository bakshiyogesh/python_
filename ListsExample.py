# A list is an ordered collection of items.
# Python uses the square brackets ([]) to indicate a list
#empty_list=[]
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Alist maintain the order
# A list can contain other lists. The following example defines a list of lists:

coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)

# A list is dynamic. 
# It means that you can modify elements in the list, add new elements to the list, and remove elements from a list.
# The append() method appends an element to the end of a list. For example:

numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)

print(numbers)
# The insert() method adds a new element at any position in the list.

# For example, the following inserts the number 100 at index 2 of the numbers list:

numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)

print(numbers)
# The del statement allows you to remove an element from a list by specifying the position of the element.

numbers = [1, 3, 2, 7, 9, 4]
del numbers[0]

print(numbers)
# The pop() method removes the last element from a list and returns that element:

numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop(4)

print("poped element:",last)
print("list element after pop:",numbers)

# To remove an element by value, you use the remove() method. Note that the remove() method removes only the first element it encounters in the list.
numbers = [1, 3, 2, 7, 9, 4, 9]

numbers.remove(9)
print(numbers)