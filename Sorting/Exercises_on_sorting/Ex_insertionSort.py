def insertionSort(list):
    print("before sorting - ",list)
    print(list[0])
    for i in range(1,len(list)):
        anchor=list[i]
        # anchor is the element that needs to be placed in a sorted fashion in left sorted list
        j=i-1
        pos=i
        #pos variable marks the position in a list the anchor element should be placed
        count_swapping=0
        #count_swapping is used to know how many swaps that we missed by following our own different algorithm
        while j>=0 and anchor<list[j]:
            pos=j
            j-=1
            count_swapping+=1
        if pos != i:
            value=list.pop(i)
            list.insert(pos,value)
        #upto this line is insertion sort algorithm
        #below is exercise part where we need to print the median value from sorted list in every iteration

        sum=0
        len_list=i+1
        #len_list used to find the median value from the sorted list
        if (len_list% 2) ==0:
            for k in list[0:len_list]:
                sum+=k
            print(sum/len_list)
        else:
            print(list[len_list//2])

    print("after sorting - ",list)
    # print("swapping count we missed",count_swapping)



if __name__=="__main__":
    insertionSort([2, 1, 5, 7, 2, 0, 5])







