# The try...except...else statement works as follows:

# If an exception occurs in the try clause, Python skips the rest of the statements in the try clause and the except statement execute.
# In case no exception occurs in the try clause, the else clause will execute.
# When you include the finally clause, the else clause executes after the try clause and before the finally clause.
fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')