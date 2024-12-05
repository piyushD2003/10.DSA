class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        temp = self.start
        n = Node(data,self.start)
        if temp is not None:
            self.start.prev = n
        self.start = n
    
    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
            temp =self.start
            while temp.next is not None:
                temp = temp.next
            temp.next =n
            n.prev = temp
    
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next,temp)
            temp.next = n
            n.next.prev = n
        

    def print_DLL(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next

    def delete_at_first(self):
        if self.start is None:
            pass
         
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next= None
    
    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            if self.start.item == data:
                self.start = self.start.next
                self.start.prev = None
            else: 
                temp = self.start
                while temp.next.item != data:
                    temp = temp.next
                if temp.next is not None:
                    if temp.next.next is None:
                        temp.next = None
                    else:
                        temp.next= temp.next.next
                        temp.next.prev = temp

    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

my_list = DLL()
my_list.insert_at_start(34)
my_list.insert_at_last(5) 
my_list.insert_at_start(14)
my_list.insert_at_start(54)
my_list.insert_at_last(100) 
my_list.insert_at_start(50)
my_list.insert_after(my_list.search(14),4)
my_list.print_DLL()
my_list.delete_item(100)
my_list.delete_at_first()
my_list.delete_at_last()

print("\n\nAfter deletion")
for n in my_list:
    print(n,end=" ")