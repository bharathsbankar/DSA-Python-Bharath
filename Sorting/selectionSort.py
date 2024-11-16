list=[1,4,2,5,3]
print(f"list {list}")
def selectionSort(list):
    # index=0

    for i in range(len(list)-1):
        pos = i

        for j in range(i+1,len(list)):
            if list[pos]>list[j]:
                pos=j

        if pos !=i:
            list[i], list[pos] = list[pos], list[i]

        print(list)
    return list



print(f"list  after sorting : {selectionSort(list)}")


