from A1_SingleLinkedList import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.count = 0

    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.count +=1
    
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.count -=1
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
    
    def size(self):
        return self.count

ls = Stack()
ls.push(10)
ls.push(20)
ls.push(70)
ls.push(40)

print("Element at top :",ls.peek())
print("stack size:",ls.size())
ls.pop()
print("Element at top :",ls.peek())
print("stack size:",ls.size())