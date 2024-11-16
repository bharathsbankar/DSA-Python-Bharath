#first element in an unsorted list is taken as a pivot element
#pivot element needs to placed in a correct position in alist such that every element from left and right of pivot must be minimaum and maximaum respectively
# Partitioning : process of placing pivot element in correct position in a list

#------------Hoare partition------------------
def partition(list,start,end):

    pivot_index=start
    pivot=list[pivot_index]

    while start<end:
    #outer while loop iterates till we find the position (i.e end) which can be swapped with pivot
        while start<len(list) and( not list[start] > pivot):
        #inner while loop iterates till list[start]>pivot
            start+=1
        while not list[end] <= pivot:
        #inner while loop iterates till it lis[end]<=pivot is found
            end-=1
        if start<end:
            #if block is used to swap only between start and end  but not with pivot_index and end
            list[start],list[end]=list[end],list[start]
    if end!=pivot_index:
        # swapping with pivot element by list[end]
        list[pivot_index],list[end]=list[end],list[pivot_index]
    return end# end will be used as partition index

def quick_sort(elements,start,end):
    if start < end:
        pi=partition(elements,start,end)
        quick_sort(elements,start,pi-1)
        quick_sort(elements,pi+1,end)










if __name__=="__main__":
    elements=[11,9,27,7,2,15,28]
    print(f"before sorting :{elements}")
    quick_sort(elements,0,len(elements)-1)
    print(f"after sorting :{elements}")