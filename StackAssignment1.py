class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
           return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
stack=Stack()
stack.push(20)
stack.push(40)
stack.push(50)
print("popped item:",stack.pop())