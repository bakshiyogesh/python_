def sumNNaturalNumbers(n):
    if n==0:
        return 0
    return n+sumNNaturalNumbers(n-1)

def sumNOddNumbers(n):
    if n==0:
        return 0
    return 2*n-1+sumNOddNumbers(n-1)

def sumNEvenNumbers(n):
    if n==0:
        return 0
    return 2*n+sumNOddNumbers(n-1)

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def sumNSquares(n):
    if n==1:
        return 1
    return n*n+sumNSquares(n-1)

