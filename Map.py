# python provides  a function to iterate over list or tuple 
#and it returns new tuple or list
# syntax for map
# def fn(bonus):
    # bonus*2
# list=[200,300,500,700,900]
# iterator = map(fn, list)
# print(iterator)
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]

TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX,item[1]*10 ,item[0]+item[0]], carts)

print(list(carts))
#statement print