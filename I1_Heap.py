class Heap:
    def __init__(self):
        self.heap = []
    
    def create(self,list):
        for e in list:
            self.insert(e)

    def insert(self,e):
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index-1)//2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] =e
    
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==0:
            self.heap.pop()
        max_value = self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftChildIndex = 2*index+1
        RightChildIndex = 2*index+2
        while leftChildIndex <len(self.heap):
            if RightChildIndex<len(self.heap):
                if self.heap[leftChildIndex] >self.heap[RightChildIndex]:
                    if self.heap[leftChildIndex]>temp:
                        self.heap[index]= self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                else:
                    if self.heap[RightChildIndex]>temp:
                        self.heap[index]= self.heap[RightChildIndex]
                        index = RightChildIndex
                    else:
                        break
            else:#No right 
                if self.heap[leftChildIndex]>temp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else:
                    break
            leftChildIndex = 2*index+1
            RightChildIndex = 2*index+2
        self.heap[index]=temp
        return max_value
    
    def heapSort(self,list1):
        self.create(list1)
        list2=[]
        while len(self.heap)>1:
                list2.insert(0,self.delete())
                print(len(self.heap)," ",list2)
        return list2
    
class EmptyHeapException(Exception):
    def __init__(self,msg="empty heap"):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
h = Heap()
# h.create([4,6,5,1,8,9])
print(h.heapSort([4,8,3,1,0,9,7]))