class Node:
    def __init__(self, item=None,next = None, prev =None):
        self.item = item
        self.next = next
        self.prev = prev
    
class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def is_empty(self):
        return self.rear == None
    
    def insert_front(self, data):
        n = Node(data)
        if self.is_empty():
            self.rear = n
            self.count+=1
        else:
            n.prev = self.front
            self.front.next = n
            self.count+=1
        self.front = n
    
    def insert_rear(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.count+=1
        else:
            n.next = self.rear
            self.rear.prev = n
            self.count+=1
        self.rear = n
    
    def delete_front(self):
        if self.is_empty():
            pass
        elif self.front == self.rear:
            self.front = None
            self.rear = None
            self.count-=1
        else:
            self.front.prev.next = None
            self.front = self.front.prev
            self.count-=1

    def delete_rear(self):
        if self.is_empty():
            pass
        elif self.rear == self.front:
            self.front = None
            self.rear = None
            self.count-=1
        else:
            self.rear.next.prev = None
            self.rear = self.rear.next
            self.count-=1

    def get_front(self):
         if self.is_empty():
            pass
         else:
             return self.front.item
         
    def get_rear(self):
         if self.is_empty():
            pass
         else:
             return self.rear.item

    def size(self):
        return self.count
    
    def print_DLL(self):
        temp = self.rear
        while temp is not None:
            print(temp, temp.prev," ",temp.item," ", temp.next)
            temp = temp.next

ls = Deque()
ls.insert_front(34)
ls.insert_front(14)
ls.insert_front(1)
ls.insert_rear(0)

ls.print_DLL()
ls.delete_front()
ls.delete_rear()

print("after deletion")
ls.print_DLL()
print(ls.get_front()," ",ls.get_rear()," ",ls.size())
