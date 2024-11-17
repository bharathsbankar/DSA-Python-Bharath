def merge_two_sorted_lists(a,b,elements):

    a_len=len(a)
    b_len=len(b)
    k=i=j=0
    while i<a_len and j<b_len:
        if a[i]<=b[j]:
            elements[k]=a[i]
            i+=1
        else:
            elements[k]=b[j]
            j+=1
        k+=1
    #still some elements may be left in a sub arrays
    while i < a_len:
        elements[k]=a[i]
        i+=1
        k+=1
    while j<b_len:
        elements[k]=b[j]
        j+=1
        k+=1


def merge_sort(elements):
    if len(elements)<=1:
        return
    mid=len(elements)//2
    left=elements[:mid]
    right=elements[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left,right,elements)





if __name__=="__main__":
    # a=[5]
    # b=[7]
    elements=[1,23,21,15,34]
    test_cases=[
        [10,3,15,7,8,23,98,29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5],[5,4,3,2,1]
    ]
    for i in test_cases:

        merge_sort(i)
        print(i)
