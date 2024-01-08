# inplace operators overloading
class Item:
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
    @property
    def amount(self):
        return self.qty*self.price
    def __str__(self):
        return f'{self.name} {self.qty} ${self.price} ${self.amount}'

class Cart:
    def __init__(self):
        self.items=[]
        print(self.items)
    def __iadd__(self,item):
        if not isinstance(item,Item):
            raise ValueError('The Item is must be instance of item')
        self.items.append(item)
        return self
    @property
    def total (self):
        return sum([item.amount for item in self.items])
    def __str__(self):
        if not self.items:
            return 'Thec Cart is empty.'
        return '\n'.join([str(item) for item in self.items])
if __name__ == "__main__":
    cart =Cart()
    cart+=Item('Apple',5,2)
    cart+=Item("Banana",20,1)
    cart+=Item("Orange",10,1.5)
    print(cart)
    print('-'*30)
    print('Total:$',cart.total)

