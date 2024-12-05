def InsertionSort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j= i-1
        while j>=0 and temp<list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp
    return list

l = [5,3,2,6,1,8]
print("Sorted: ",InsertionSort(l))
for i in reversed(range(1)):
    print(i)