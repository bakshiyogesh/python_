# To use the reduce() function, you need to import it from the functools module using the following statement at the top of the file:
from functools import reduce
scores=[75,65,80,95,50]
total=reduce(lambda a,b:a+b,scores)
print(total)