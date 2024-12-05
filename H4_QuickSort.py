def QuickSort(list):
    if len(list)<=1:
        return list
    else:
        pivot = list[0]
        lesser = [x for x in list[1:] if x<=pivot]
        greater = [x for x in list[1:] if x>=pivot]
        return QuickSort(lesser) +[pivot] + QuickSort(greater)
l = [5,3,8,6,1,2]
print(QuickSort(l))
