class Queue:
    def __init__(self):
        self.ls = []
   
    def is_empty(self):
        return len(self.ls)== 0
    
    def enqueue(self,data):
        self.ls.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.ls.pop(0)

    def get_front(self):
        if not self.is_empty():
            return self.ls[0]
        
    def get_rear(self):
        if not self.is_empty():
            return self.ls[-1]
    
    def size(self):
        return len(self.ls)

ls = Queue()
ls.enqueue(10)
ls.enqueue(20)
ls.enqueue(30)
ls.enqueue(40)
print(ls.get_rear())
print(ls.get_front())
ls.dequeue()
ls.enqueue(23)
print(ls.get_rear())
print(ls.get_front())
print(ls.size())