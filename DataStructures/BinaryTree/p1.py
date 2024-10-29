#---------------------BINARY SEARCH TREE -----------------------
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    def pre_order_traversal(self):
        #root-left-right
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements



    def delete(self, val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
            #by default python will return in else   case
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
            #by default else case will return none
        else:
            #val==self.dat <match> is found in else case
            #3 cases
            #case 1 : leaf node
            if self.left is None and self.right is None:
                return None
            #case 2: one child node either left or right
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            #case 3: both child nodes were present
            else:
                #self must be replaced by either minimaum of right subtree or maximaum of left subtree
                max_val=self.left.find_max()
                self.data=max_val
                self.left=self.left.delete(max_val)
        return self


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in elements[1:]:
        root.add_child(i)

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([15,12,14,7,20,88,23,27])
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    # numbers_tree.delete(20)
    # print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    #
    # numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.delete(9)
    # print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]
    #
    # numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # numbers_tree.delete(17)
    # print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
