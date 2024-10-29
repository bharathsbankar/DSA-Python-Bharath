class Node():
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        return  str(self.print_list())


    def insert_at_beg(self,data):
        if self.head is None:
            node = Node(data, None, self.head)
            self.head = node
            self.tail=node
            return
        node=Node(data,None,self.head)
        self.head.prev=node
        self.head=node

    def insert_new_values(self,list):
        self.head=None
        for data in list:
            self.insert_at_end(data)

    def insert_at_spec_index(self,data,index):
        if index < 0 or index >= self.length_dll():
            print(f"invalid index")
        if index == 0:
            return self.insert_at_beg(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr,itr.next)
                temp=itr.next
                temp.prev=node
                itr.next = node
                break
            itr=itr.next
            count += 1

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

    def remove_by_value(self, data):
        if self.head is None:
            print("!Empty list")
            return
        itr = self.head
        prev_node = itr
        if self.head.data == data:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            print(data, " removed from list")
            return
        while itr:

            if itr.data == data:
                if itr.next is None:

                    prev_node.next = itr.next
                    itr.next = None
                    itr.prev = None
                    itr = None

                    print(data, " removed from list")
                    return

                temp=itr.next
                prev_node.next=itr.next
                temp.prev=prev_node
                itr.next = None
                itr.prev = None
                itr = None

                print(data, " removed from list")
                return

            prev_node = itr
            itr = itr.next
        print("!value not found in list")

    def insert_at_end(self,data):
        if self.head is None:
            return self.insert_at_beg(data)
        itr=self.head
        while itr:
            if itr.next is None:
                node=Node(data,itr,None)
                itr.next=node
                self.tail=node
                return
            itr=itr.next

    def length_dll(self):
        count = 0
        it = self.head
        while it:
            count += 1
            it = it.next
        return count

    def insert_after_node(self, data_after, data_to_insert):
        if self.head is None:
            print("!Empty list")
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                if itr.next is None:
                    self.insert_at_end(data_to_insert)
                    return self.print_list()
                temp=itr.next
                node = Node(data_to_insert, itr,itr.next)
                itr.next = node
                temp.prev=node
                self.print_list()
                return
            itr = itr.next
        print("!node not found")

    def print_list(self):
        if self.head is None:
            print("list is empty")
        itr=self.head
        while itr:
            if itr.next is None:
                print(itr.data)
                break
            print(itr.data,"->",end=" ")
            itr=itr.next
    def print_reverse(self):
        tail=self.tail
        while tail:
            if tail.prev is None:
                print(tail.data)
                return
            print(tail.data,"->",end=" ")
            tail=tail.prev
        print("empty list")


if __name__=='__main__':
    a=LinkedList()
    a.insert_at_beg("Bharath")
    a.insert_at_beg("Akshay")
    a.insert_at_beg("srikanth")
    a.print_list()
    a.print_reverse()
    print(f"head-data : {a.head.data} ; tail-data : {a.tail.data}")
    # a.remove_by_value("Akshay")
    # a.insert_after_node("Bharath","Nikhil")
    # a.print_list()
    print(a)
    print(a.tail.data)
    a.insert_at_spec_index("data",1)
    print(a)
    print(a.tail.data)
