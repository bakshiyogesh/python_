def printN(n):
    if n>0:
        printN(n-1)
        print(n,end='')

printN(6)
## NNumbersInReverseOrder
def printNReverse(n):
    if n>0:
        print(n,end='')
        print(n-1)
## NOddNumbers
def printNOddNumbers(n):
    if n>0:
        printNOddNumbers(n-1)
        print(2*n-1,end='')
## NEvenNumbers
def printNOddNumbers(n):
    if n>0:
        printNOddNumbers(n-1)
        print(2*n,end='')
## NEvenNumbersInReverseOrder
def printNEvenNumbersReverse(n):
    if n>0:
        printNEvenNumbersReverse(n-1)
        print(2*n,end='')
## NOddNmbersInReverseOrder
def printNOddNumbersInReverseOrder(n):
    if n>0:
        printNOddNumbersInReverseOrder(n-1)
        print(2*n-1,end='')

