class PriorityQueue:
    def __init__(self):
        self.ls = []

    def is_empty(self):
        return len(self.ls) == 0
    
    def push(self,data,priority):
        index = 0
        while index<len(self.ls) and self.ls[index][1]<=priority:
            index+=1
        self.ls.insert(index,(data, priority))
    
    def pop(self):
        if self.is_empty():
            pass
        else:
            self.ls.pop(0)
    
    def size(self):
        return len(self.ls)
    def show(self):
        print(self.ls)

ls = PriorityQueue()
ls.push("A",3)
ls.push("B",2)
ls.push("C",7)
ls.push("D",0)
ls.push("E",5)
# ls.pop()
# ls.pop()
ls.show()