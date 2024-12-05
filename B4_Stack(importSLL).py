from A1_SingleLinkedList import *
class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.count = 0
    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.count +=1
    
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.count -=1

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        
    def size(self):
        return self.count
    
ls = Stack()
ls.push(1)
ls.push(2)
ls.push(30)
ls.push(4)
ls.push(70)
print("Element at top :",ls.peek())
print("stack size:",ls.size())
ls.pop()
print("Element at top :",ls.peek())
print("stack size:",ls.size())