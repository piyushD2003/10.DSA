class Deque:
    def __init__(self):
        self.ls = []
    def is_empty(self):
        return len(self.ls)==0
    def insert_front(self,data):
        self.ls.insert(0,data)
    def insert_rear(self,data):
        self.ls.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.ls.pop(0)
    def delete_rear(self):
        if not self.is_empty():
            self.ls.pop()
    def get_front(self):
        if not self.is_empty():
            return self.ls[0]
    def get_rear(self):
        if not self.is_empty():
            return self.ls[-1]
    def size(self):
        return len(self.ls)

ls = Deque()
ls.insert_front(5)
ls.insert_front(50)
ls.insert_front(30)
ls.insert_rear(3)
# ls.delete_front()
ls.delete_rear()
print(ls.get_front()," ",ls.get_rear()," ",ls.size())