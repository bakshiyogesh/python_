# The sort() method sorts the original list in place. It means that the sort() method modifies the order of elements in the list.

# By default, the sort() method sorts the elements of a list using the less-than operator (<). In other words, it places the lower elements before the higher ones.

# To sort elements from higher to lower, you pass the reverse=True argument to the sort() method like this:

list.sort(reverse=True)

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
companies.sort(key=lambda company:company[2])
