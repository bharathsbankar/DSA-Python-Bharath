#-----------------TREE------------------------
# Bharath(CE0)
#     |__abc(devlopment)
#         |__bcd(employee)
#         |__cde(employee)
#      |__xyz(testing)
#          |__yze(employee)
#          |__zef(employee)
# to print name tree,designation tree , name and designation tree
# -#to print tree based on level
# -
class Tree:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.parent=None
        self.children=[]

    def add_child(self,child):
        self.children.append(child)
        child.parent=self

    def get_level(self):
        level=0
        temp=self
        while temp.parent:
            level+=1
            temp=temp.parent
        return level

    def print_tree(self,string="both"):
        temp=self.get_level()
        indent="    "*temp
        prefix=indent+"|__" if temp!=0 else ""
        if string=="name":
            print(prefix+self.name)
        elif string=="designation":
            print(prefix + self.designation)
        elif string=="both":

            print(prefix + self.name + "(" + self.designation + ")")
        else:
            return
        if self.children:
            for child in self.children:
                child.print_tree(string)

    def print_level_tree(self,level=0):
        if self.get_level()>level:
            return
        temp=self.get_level()
        indent="    "*temp
        prefix=indent+"|__" if temp!=0 else ""
        print(prefix + self.name + "(" + self.designation + ")")

        if self.children:
            for child in self.children:
                child.print_level_tree(level)







def build_tree():
    Bharath=Tree("Bharath","CE0")
    abc=Tree("abc","devlopment")
    bcd=Tree("bcd","employee")
    cde=Tree("cde","employee")
    xyz=Tree("xyz","testing")
    yze=Tree("yze","employee")
    zef=Tree("zef","employee")
    Bharath.add_child(abc)
    Bharath.add_child(xyz)
    abc.add_child(bcd)
    abc.add_child(cde)
    xyz.add_child(yze)
    xyz.add_child(zef)
    return Bharath




if __name__ == "__main__":
    node=build_tree()
    # print("<<< Name TREE >>>\n ")
    # node.print_tree("name")
    # print("\n\n\n<<< Designation TREE >>>\n ")
    # node.print_tree("designation")
    # print("\n\n\n<<< Name and Designation TREE >>>\n ")
    # node.print_tree("both")
    node.print_level_tree(2)