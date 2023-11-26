#Set in python
#To define set we use curly braces {}
skill={'pro-player','chess','sytemm-design'}
#You can't define empty set as:
# empty={} it is by default intialize a empty dictionary
#Therefore, you need to use the built-in set() function:

empty_set  = set()
# Note that the original order of elements may not be preserved.

# To negate the in operator, you use the not operator
#adding a element to a set
empty_set.add('name')
#To make it more convenient, the set has the discard() method that allows you to remove an element. And it doesn’t raise an error if the element is not in the list:
#set.discard(element)

# To remove and return an element from a set, you use the pop() method.
# Since the elements in a set have no specific order, the pop() method removes an unspecified element from a set.

# To remove all elements from a set, you use the clear() method:
# set.clear()
 
# To make a set immutable, you use the built-in function called frozenset(). The frozenset() returns a new immutable set from an existing one. For example:

skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)
tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)

#Python Set Union

s1={'python','java'}
a2={'java','swift'}
s=s1.union(a2)

# OR
set1=s1|a2
#Diffrence in union method or Set Union method is that union method accepts one or two iterables
#while set union (|) only allows set not iterables
# you can use the set intersection() method or set intersection operator (&) to intersect two or more sets:
  

#SET INTERSECTION  
# new_set = set1.intersection(set2, set3)
# new_set = set1 & set2 & set3

# The set intersection operator only allows sets, while the set intersection() method can accept any iterables, like strings, lists, and dictionaries.
 #SET DIFFRENCE
#Using set diffrence operator 
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2 - s1

print(s)

#using diffrence() method
scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores.difference(numbers)

# print(new_scores)



#  The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) while the set difference operator (-) only allows sets.