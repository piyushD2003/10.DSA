class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self, data):
        self.append(data)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return super().pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self[-1]
    
    def size(self):
        return len(self)
    

ls = Stack()
ls.push(34)
ls.push(4)
ls.push(31)
print(ls.peek())