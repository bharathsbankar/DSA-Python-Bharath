#-----------LOMUTO partition----------------
    #last element is considered as pivot element ( we can also consider either first or middle element)
    # we use p_index and i as a counters
    # first element index is considered as p_index
    #p_index iterates until list[p_index]>pivot
    #when list[p_index] >= pivot:
        #the i counter starts from p_index and iterates until list[i] < pivot
            #now elements in p_index and i will be swapped



def partition(elements,end):
    pivot_index=0
    pivot=elements[end]
    while not pivot_index == end:
        while pivot_index<len(elements)-1 and ( not elements[pivot_index] >= pivot):
            pivot_index+=1
        i=pivot_index
        while i<len(elements)-1 and (not i < pivot):
            i+=1
        if elements[pivot_index] > elements[i]:
            elements[pivot_index],elements[i]=elements[i],elements[pivot_index]
    return pivot_index





def quick_sort(elements,end):
    pi=partition(elements,end)


if __name__=="__main__":
    elements=[11,9,27,7,2,15,28]
    print(f"before sorting :{elements}")
    #fuction call
    quick_sort(elements,end=len(elements)-1)
    print(f"after sorting :{elements}")