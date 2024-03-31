class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
    def peak(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'start' found.")
stack=Stack()
stack.push(20)
stack.push(40)
stack.push(50)
print("popped item:",stack.insert(0,60))