def SelectionSort(list):
    flag = False
    for i in range(len(list)-1):
        flag = False
        print(list)
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]
                flag = True
        if not flag:
            break
    return list

l = [5,3,2,6,1,8]
print("Sorted:", SelectionSort(l))