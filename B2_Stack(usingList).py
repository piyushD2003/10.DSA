class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)
mylist = Stack()
mylist.push(4)
mylist.push(5)
mylist.push(6)
print(mylist.peek())
print(mylist.pop())
print(mylist.peek())
print(mylist.size())
