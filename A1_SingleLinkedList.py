
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    
    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                 temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item," ")
            temp = temp.next
    
    def delete_first(self):
        temp = self.start
        if self.start is not None:
            self.start = temp.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item==data:
                self.start ==temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp =temp.next
    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
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
    
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_last(10)
mylist.insert_at_start(45)
# mylist.insert_after(mylist.search(10),7)
# # mylist.delete_first()
# # mylist.delete_last()
# # mylist.delete_item(10)
# mylist.print_list()
# for n in mylist:
#     print(n,end=" ")

class Node():
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

class SingleLinkedList():
    def __init__(self, start=None):
        self.start = start
    
    def insert_at_start(self,data):
        n = Node(data)
        if self.start is not None:
            n.next = self.start
            self.start = n
        else:
            self.start = n
        return n 

    def insert_at_last(self,data):
            n = Node(data)
            temp = self.start
            if self.start is not None:
                while temp.next is not None:
                    temp = temp.next
                temp.next = n
            else:
                self.start = n
            return n 
    
    def search(self, data):
        temp = self.start
        while temp.next is not None:
            if temp.item == data:
                return temp
            else:
                temp = temp.next
        return temp
    
    def insert_after(self,prevD, data):
        n = Node(data)
        temp = self.search(prevD)
        n.next = temp.next
        temp.next = n
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, temp)
            temp = temp.next
    
    def delete_first(self):
        self.start = self.start.next
    
    def delete_last(self):
        temp = self.start
        if temp.next is None:
            self.start = None
        else:
            while temp.next is not None:
                    if temp.next.next == None:
                        temp.next = None
                        break
                    temp = temp.next

    
    def delete_item(self,data):
        temp = self.start
        while temp.next is not None:
            if temp.item == data:
                break
            else:
                temp = temp.next
        
        if temp == self.start:
            self.start = temp.next
        else:
            temp1 = self.start
            while temp1.next is not None:
                if temp1.next == temp:
                    temp1.next = temp.next
                    break
                else:
                    temp1 = temp1.next
        
        

    
mylist = SingleLinkedList()
mylist.insert_at_start(4)
mylist.insert_at_start(1)
mylist.insert_at_last(5)
mylist.insert_at_last(12)
mylist.insert_after(5,8)
# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_item(5)
# mylist.delete_item(1)
mylist.delete_item(5)
mylist.insert_after(12,8)
mylist.print_list()


