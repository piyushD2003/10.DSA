class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self,data,priority):
        n = Node(data, priority)
        if not self.start or priority<self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority<= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.count +=1
    def pop(self):
        if self.is_empty():
            pass
        elif self.start.item ==None:
            self.start = None
        else:
            self.start = self.start.next
            self.count -=1
    def size(self):
        return self.count
    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp," ", temp.item," ",temp.next)
            temp = temp.next

ls = PriorityQueue()
ls.push(7,2)
ls.push(2,4)
ls.push(3,3)
ls.push(8,0)
ls.pop()
ls.pop()
ls.print_list()
print(ls.size())

