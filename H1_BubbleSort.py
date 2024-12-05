def BubbleSort(list):
    for i in range(1,len(list)):
        flag =False
        for j in range(len(list)-i):
            flag = False
            if list[j]>=list[j+1]:
                list[j],list[j+1]= list[j+1],list[j]
                flag = True
        if not flag:
            break
        print(list)
    return list

print(BubbleSort([4,1,8,3,5,1,3]))