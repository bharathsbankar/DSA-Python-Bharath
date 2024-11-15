list=[1,4,2,5,3]
print(f"list {list}")
def selectionSort(list):
    # index=0
    for i in range(len(list)-1):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                # min=list[j]
                min=j
        list[i],list[min]=list[min],list[i]
        print(list)
    return list



print(f"list  after sorting : {selectionSort(list)}")


