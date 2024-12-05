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
            
# mylist = SingleLinkedList()
# mylist.insert_at_start(4)
# mylist.insert_at_start(1)
# mylist.insert_at_last(5)
# mylist.insert_at_last(12)
# mylist.insert_after(5,8)
# # mylist.delete_first()
# # mylist.delete_last()
# # mylist.delete_item(5)
# # mylist.delete_item(1)
# mylist.delete_item(5)
# mylist.insert_after(12,8)
# mylist.print_list()

class Node2():
    def __init__(self, item=None, next=None, prev = None):
        self.item = item
        self.next = next
        self.prev = prev

class DoubleLinkedList():
    def __init__ (self, start=None):
        self.start = start
    
    def insert_at_start(self,data):
        n = Node2(data)
        if self.start is not None:
            self.start.prev = n
            n.next = self.start
        self.start = n

    def insert_at_last(self,data):
        pass

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.prev, temp, temp.next, temp.item)
            temp = temp.next

mylist = DoubleLinkedList()
mylist.insert_at_start(6)
mylist.insert_at_start(6)
mylist.insert_at_start(6)
mylist.insert_at_start(16)
mylist.print_list()

