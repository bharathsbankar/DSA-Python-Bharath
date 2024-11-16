





#timecomplexity : o(N^2)
#################################################

# # code for number of comparisons in bubble sort for n elements
# from functools import reduce
# def Comparisons_BubbleSort(n):
#     res=reduce(lambda a,b : a+b ,range(1,n))
#     return res
# a=int(input("enter number of elements :"))
# print(f"number of comparisons in buuble sort for {a} elements would be :{Comparisons_BubbleSort(a)}")
#
# ##########################################
# #code to check number of comparisons in bubble sort for n elements using recursion
#
def func(n):
    if n==1:
        return 1
    else:
        return n+func(n-1)

# print(f"no. of comparisons for {a} elements would be {func(a-1)}")
#
#
# ##################################################

#bubble sort implementation
list1=[0,-1,8,2,5]
list2=[0,-1,8,2,5]
print(f"list {list}")
def bubbleSort(list):
    global a,b # a denotes the total no.. of swappings done in sorting method
    # b is used to check total no.. of comparisons made in a  sorting method
    a,b=0,0
    for i in range(1,len(list)):#outer loop is for no.. of iterations the inner loop can be applied
        #inner loop is for no. of comparisons
        for j in range(len(list)-i):
            if list[j]>list[j+1]:#this condition sorts in ascending order
                #swap condition
                list[j],list[j+1]=list[j+1],list[j]
                a+=1
            b+=1


    return list

#below function does swappings at the end in ith iteration instead of doing when finding in maximaum element
def bSort(list):
    global ab
    ab = 0
    pos=0
    print(f"before sorting : {list}")
    for i in range(len(list)-1):#ex. : 4 elements , 3 iterations
        for j in range(len(list)-(i+1)):
            if list[j+1]<=list[j]:
                pos=j
            else:
                pos=j+1
        last_ele=len(list)-(i+1)
        if pos != last_ele:
            list[last_ele],list[pos]=list[pos],list[last_ele]
            ab+=1
    return list






compar=func(len(list1)-1)
print(f"list  after sorting : "
      f"{bubbleSort(list1)}"
      f"\n------ number of comparisons taken is {compar} \n ------- no.. of swapings is :{a} , for {len(list1)} elements ")
print(f"after sorting , {bSort(list2)} ,"
      f"\n -------number of comparisons taken is {compar} \n ------- no.. of swapings is :{ab} , for {len(list2)} elements")
