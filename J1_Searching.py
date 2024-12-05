def BinarySearch(list,num,min,max):
    mid = (min+max-1)//2
    if max>=max:
        if list[mid]== num:
            print(mid)
        if list[mid]>num:
            BinarySearch(list,num,0,mid-1)
        if list[mid]<num:
            BinarySearch(list,num,mid+1,max)
l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(len(l))
BinarySearch(l,6,0,len(l)-1)