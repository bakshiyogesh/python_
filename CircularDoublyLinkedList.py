class Node:
    def __init__(self,item=None,prev=None,start=None):
        self.start=start
        self.item=item
        self.prev=prev

class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
         n=Node(data)
         if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
         else:
            n.next=self.start
            n.prev=self.start.prev
            # n.start.prev=n
            self.start.prev.next=n
    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
            while temp!=self.start:
                if temp.item==data:
                    return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp,temp.next)
            temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end='')
            temp=temp.next
            while temp!=self.start:
                print(temp.item,end='')
                temp=temp.next
    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
        else :
            self.start.prev.prev.next=self.start
            self.start=self.start.prev.prev
    def delte_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp!=self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1: #count is flag variable used for circular list due to which the it will again point to first element 
            raise StopIteration
        else:
            self.current=1
            data=self.current.item
            self.current=self.current.next
            return data

mylist=CDLL()
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(90)
mylist.insert_at_last(60)
mylist.insert_after(mylist.search(90),50)
for data in mylist:
    print (data,end='')           

            