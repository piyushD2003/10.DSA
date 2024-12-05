class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self,end=None):
        self.end = end
    
    def is_empty(self):
        return self.end == None

    def insert_at_start(self,data):
        n =Node(data)
        if self.is_empty():
            n.next = n
            self.end = n
        else:
            n.next = self.end.next
            self.end.next = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.end = n
        else:
            n.next = self.end.next
            self.end.next = n
            self.end = n
    def search(self,data):
        temp = self.end.next
        if self.end.item == data:
            return self.end
        else:
            while temp is not self.end:
                if temp.item == data:
                    return temp
                temp =temp.next
            return None
            
    def insert_after(self,temp,data):
        n = Node(data,temp.next)
        if temp == self.end:
            temp.next = n
            self.end = n
        else:
            temp.next = n
    
    def delete_at_start(self):
        if self.end == self.end.next:
            self.end = None
        else:
            self.end.next = self.end.next.next
    
    def delete_at_last(self):
        if self.end == self.end.next:
            self.end = None
        else:
            temp = self.end.next
            while temp.next is not self.end:
                temp = temp.next
            temp.next = self.end.next
            self.end = temp
    
    def delete_item(self, data):
        if self.end.item == data:
            self.delete_at_last()
        elif self.end.next.item ==data:
            self.delete_at_start()
        else:
            temp = self.end.next
            while temp is not self.end:
                if temp.next.item == data:
                    temp.next = temp.next.next
                temp = temp.next
        
    def print_list(self):
        if not self.is_empty():
            temp = self.end.next
            while temp is not self.end:
                print(temp," ",temp.item," ",temp.next)
                temp = temp.next
            print(self.end," ",self.end.item," ",self.end.next)
        else:
            print(self.end)
    
    def __iter__(self):
        if self.end ==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.end.next)
class CLLIterator:
    def __init__(self,end):
        self.current = end
        self.start = end
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
    
mylist = CLL()
mylist.insert_at_start(3)
mylist.insert_at_last(8)
mylist.insert_at_last(9)
mylist.insert_at_start(2)
mylist.insert_at_last(10)
mylist.insert_after(mylist.search(10),7)
mylist.print_list()
# mylist.delete_item(2)
for n in mylist:
    print(n,end=" ")