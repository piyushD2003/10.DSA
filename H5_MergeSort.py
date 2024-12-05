def MergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        leftlist = list[:mid]
        rightlist = list[mid:]
        
        print(leftlist," ",rightlist)
        MergeSort(leftlist)
        MergeSort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list[k]=leftlist[i]
                i+=1
            else:
                list[k]=rightlist[j]
                j+=1
            k+=1
            
        while i<len(leftlist):
            list[k]= leftlist[i]
            i+=1
            k+=1
        
        while j<len(rightlist):
            list[k]= rightlist[j]
            j+=1
            k+=1

l = [5,3,8,6,1,2]
MergeSort(l)
print(l)