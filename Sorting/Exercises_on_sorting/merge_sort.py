def merge_two_sorted_lists(a,b,key,descending=False):

    a_len=len(a)
    b_len=len(b)
    k=i=j=0
    if not descending:
        while i<a_len and j<b_len:

            if a[i][key]<=b[j][key]:
                elements[k]=a[i]
                i+=1
            else:
                elements[k]=b[j]
                j+=1
            k+=1
        #still some elements may be left in a sub arrays

    else:
        while i < a_len and j < b_len:

            if a[i][key]>=b[j][key]:
                elements[k] = a[i]
                i += 1
            else:
                elements[k] = b[j]
                j += 1
            k += 1
    while i < a_len:
        elements[k]=a[i]
        i+=1
        k+=1
    while j<b_len:
        elements[k]=b[j]
        j+=1
        k+=1
        # still some elements may be left in a sub arrays


# def merge_sort_ele(data,key,descending=False):
#     elements=[]
#     for i in range(0,len(data)):
#         elements.append(data[i][key])
#     merge_sort(elements,descending)





def merge_sort(elements,key,descending=False):

    if len(elements)<=1:
        return
    mid=len(elements)//2
    left=elements[:mid]
    right=elements[mid:]

    merge_sort(left,key,descending=False)
    merge_sort(right,key,descending=False)

    merge_two_sorted_lists(left,right,key,descending=False)





if __name__=="__main__":
    # a=[5]
    # b=[7]
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    # print(elements[0]["time_hours"])

    merge_sort(elements,"time_hours")
    print(elements)
