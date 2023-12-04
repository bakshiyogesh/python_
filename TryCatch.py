#Try catch block

    
try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ZeroDivisionError:
    print('Error! Please enter a number except Zero.')
except ValueError as value:
    print("Vlue Error")
except Exception as ex:
    print("Exception Error")
finally:
    print("resource closed.")
