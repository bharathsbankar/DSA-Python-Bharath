class TreeNode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]
        #children list must contain object of class TreeeNode type only
        #i.e childrens must also be of type TreeNode
    def add_child(self,child):#child must be of TreeNode type
        self.children.append(child)
        child.parent=self

    def print_tree(self):
        a=self.get_level()
        indent="  "*a
        prefix=indent+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for node in self.children:
                node.print_tree()

    def get_level(self):
        level=0

        while self.parent:
            level+=1
            self=self.parent
        return level

def build_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("laptop")
    root.add_child(laptop)
    asus=TreeNode("ASUS")
    mac=TreeNode("mac")
    hp=TreeNode("hp")
    laptop.add_child(asus)
    laptop.add_child(mac)
    laptop.add_child(hp)

    TV=TreeNode("TV")
    root.add_child(TV)
    mi=TreeNode("mi")
    lg=TreeNode("lg")
    sony=TreeNode("sony")
    TV.add_child(mi)
    TV.add_child(lg)
    TV.add_child(sony)

    headphones=TreeNode("headphones")
    root.add_child(headphones)
    noise=TreeNode("noise")
    jbl=TreeNode("jbl")
    apple=TreeNode("apple")
    headphones.add_child(noise)
    headphones.add_child(apple)
    headphones.add_child(jbl)

    return root



if __name__=='__main__':
    root=build_tree()

    root.print_tree()