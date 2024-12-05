class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item = item
        self.next = next
        self.prev = prev
    
class CDLL:
    def __init__(self,start=None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n 
            self.start = n
    
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
    
    def search(self,data):
        if self.is_empty():
            print(None)
        elif self.start.prev.item == data:
                return self.start.prev
        else:
            temp = self.start
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next

    def insert_after(self,temp,data):
        if self.start.prev == temp:
            self.insert_at_last(data)
        else:
            n = Node(data,temp.next,temp)
            temp.next.prev = n
            temp.next = n

    def delete_at_start(self):
        if self.is_empty():
            self.start = None
        elif self.start == self.start.next:
            self.start = None
        else:
            self.start.next.prev = self.start.prev
            self.start.prev.next = self.start.next
            self.start = self.start.next
    
    def delete_at_last(self):
        if self.is_empty():
            self.start = None
        elif self.start == self.start.next:
            self.start = None
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev
    
    def delete_item(self,data):
        if self.start.item == data:
            self.delete_at_start()
        elif self.start.prev.item == data:
            self.delete_at_last()
        else:
            temp = self.start
            while temp.next != self.start:
                if temp.next.item == data:
                    temp.next.next.prev = temp
                    temp.next = temp.next.next
                temp = temp.next
    def print_list(self):
        if self.is_empty():
            print(self.start)
        else:
            temp = self.start
            while temp.next is not self.start:
                print(temp," ",temp.prev," ",temp.item," ",temp.next)
                temp = temp.next
            print(temp," ",temp.prev," ",temp.item," ",temp.next)
    def __iter__(self):
        if self.start ==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.start)
class CLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current ==None:
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count =1
        data = self.current.item
        self.current = self.current.next
        return data   
    

mylist = CDLL()
mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_at_start(3)
mylist.insert_at_start(5)
mylist.insert_at_last(6)
mylist.insert_at_last(7)
mylist.insert_after(mylist.search(7),100)
mylist.print_list()

print("\n\nAfter Deletion")
# mylist.delete_item(2)
for n in mylist:
    print(n,end=" ")
    
