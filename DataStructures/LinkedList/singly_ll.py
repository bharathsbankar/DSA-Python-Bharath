from itertools import count


class Node:
    def __init__(self, data,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node


    def insert_at_end(self,data):
        if self.head is None:
            # node=Node(data,self.head)
            # self.head=node
            return self.insert_at_beg(data)
        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data)
        itr.next=node


    def insert_new_values(self,list):
        self.head=None
        for data in list:
            self.insert_at_end(data)

    def length_ll(self):
        count=0
        it=self.head
        while it:
            count+=1
            it=it.next
        return count

    def remove_at(self,index):
        # to-do :check index is valid or not
        if index<0 or index>=self.length_ll():
            print(f"invalid index")
        if index==0:
            temp=self.head.next
            self.head.next=None
            self.head=temp
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                temp=itr.next.next
                itr.next.next=None
                itr.next=temp
                break
            itr=itr.next
            count+=1

    def insert_at_spec_index(self,data,index):
        if index < 0 or index >= self.length_ll():
            print(f"invalid index")
            return
        if index == 0:
            return self.insert_at_beg(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr=itr.next
            count += 1
        return

    def get_data_by_index(self,index):
        if index<0 or index>=self.length_ll():

            return f"invalid index"
        itr=self.head
        count=0
        while itr:
            if count==index:
                return itr.data
            itr=itr.next
            count+=1

    def remove_by_value(self,data):
        if self.head is None:
            print("!Empty list")
            return
        itr=self.head
        prev = itr
        if self.head.data==data:
            temp=self.head.next
            self.head.next=None
            self.head=temp
            print(data, " removed from list")
            return
        while itr:

            if itr.data==data:
                prev.next=itr.next
                itr.next=None
                itr=None

                print(data," removed from list")
                return
            prev = itr
            itr=itr.next
        print("!value not found in list")


    def insert_after_node(self,data_after,data_to_insert):
        if self.head is None:
            print("!Empty list")
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                if itr.next is None:
                    self.insert_at_end(data_to_insert)
                    return self.print_list()
                node=Node(data_to_insert,itr.next)
                itr.next=node
                self.print_list()
                return
            itr=itr.next
        print("!node not found")

    def reverse_list(self):
        if self.head is None:
            print("!Empty list")
            return
        if self.head.next is None:
            print("reversal list is : ",end=" " )
            return self.print_list()



    def print_list(self):
        if self.head is None:
            print(f"linkedlist is empty")
        itr=self.head
        while itr :
            if(itr.next is None):
                print(itr.data)
                break
            print(itr.data,"-> ",end="")
            itr=itr.next
        print()

    #problems
    def head_func(self,head):
        if head is None:
            return
        if head.next.next != None:
            print(head.data, end="")
            self.head_func(head.next)
        print(head.data, end="")

    def reverse_list(self,head):
        if head is None:
            return
        if head.next != None:

            self.reverse_list(head.next)
        print(head.data, end="->")

    def find_max(self):
        itr=self.head
        if itr is None:
            print("!empty list")
            return None
        count=0
        max_value=itr.data
        while itr:
            if itr.data>max_value:
                max_value=itr.data
                index_pos=count
            count+=1
            itr=itr.next
        return max_value,index_pos

    def find_min(self):
        itr=self.head
        if itr is None:
            print("!empty list")
            return None,None
        count=0
        min_value=itr.data
        index_pos=None
        while itr:
            if itr.data<min_value:
                min_value=itr.data
                index_pos=count
            count+=1
            itr=itr.next
        return min_value,index_pos

    def replace_max_with_value(self,value):
        max_value,index_pos=self.find_max()
        if index_pos is None:
            return
        # self.remove_at(index_pos)
        count=0
        itr=self.head
        while itr:
            if count==index_pos:
                itr.data=value

                return self.print_list()
            count+=1
            itr=itr.next



if __name__=='__main__':

    a=LinkedList()
    # list="Bharath","Akshay","srikanth","piggy","ani","abhi","kishan","bhimi","prodgy","adyaksha","BD","chowda"
    list=list(range(0,7))
    a.insert_new_values(list)
    a.print_list()
    print("length of a linked list : ",a.length_ll())
    # # a.insert_at_spec_index("data",65)
    # print(a.get_data_by_index(11))
    # a.insert_at_spec_index("data",5)
    # a.print_list()
    # print(a.length_ll())
    # a.remove_by_value("data")
    # a.print_list()
    # print(a.length_ll())
    # a.insert_after_node("chowda","Nikhil")
    a.remove_by_value("Bharath")
    # a.insert_at_spec_index("Bharath",0)
    a.print_list()
    print("length of a linked list : ", a.length_ll())
    # a.head_func(a.head)
    print()
    # print(a.head.data)
    # a.reverse_list(a.head)
    print()
    # print(a.head.data)
    # print(a.find_max())
    # print(a.head.data)
    # a.insert_at_spec_index(3,5)
    # print(a.find_max())
    a.replace_max_with_value(15)
    a.insert_at_spec_index(68,2)
    a.insert_at_spec_index(-25,a.length_ll()-1)
    a.print_list()
    print("max_value,index of max_value",a.find_max())
    print("min_value,index of min_value",a.find_min())



