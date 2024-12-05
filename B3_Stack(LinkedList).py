class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self,start=None,count=0):
        self.start = start
        self.count = count
    
    def is_empty(self):
        return self.start == None
    
    def push(self,data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            n.next = self.start
            self.start = n
        self.count = self.count +1
    
    def pop(self):
        if self.is_empty():
            print("Already Empty")
        elif self.start.next == None:
            self.start = None
        else:
            self.start = self.start.next
            self.count = self.count -1
    
    def peek(self):
        if self.is_empty():
            print("Already Empty")
        else:
            return self.start.item
    
    def size(self):
        return self.count

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next

mylist = Stack()
mylist.push(2)
mylist.push(5)
mylist.push(8)
mylist.push(4)
mylist.push(31)
mylist.push(33)
mylist.print_list()
print("Top element:",mylist.peek())
mylist.pop()
mylist.pop()
print("Top element:",mylist.peek())
print(mylist.size())
mylist.print_list()