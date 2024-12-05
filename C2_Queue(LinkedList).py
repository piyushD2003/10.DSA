class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    
    def is_empty(self):
        return self.front == None
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            pass
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.count -= 1

    def get_front(self):
        return self.front.item
    
    def get_rear(self):
        return self.rear.item
    
    def size(self):
        return self.count

ls = Queue()
ls.enqueue(60)
ls.enqueue(70)
ls.enqueue(30)
ls.enqueue(40)
ls.enqueue(50)
print(ls.get_front())
print(ls.get_rear())
ls.dequeue()
print(ls.get_front())
print(ls.size())