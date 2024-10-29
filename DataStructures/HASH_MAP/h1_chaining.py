#chaining
class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[ [] for i in range(self.MAX)]

    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    #hashing with chaining
    def __setitem__(self,key,value):
        h=self.getHash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                self.arr[h][index]=(key,value)
                return

        self.arr[h].append((key, value))





    def __getitem__(self,key):
        h=self.getHash(key)
        #for loop is used to traverse inside a list present in a[h]
        for index,element in enumerate(self.arr[h]):#enumerate() returns index and value
            if element[0]==key:
                return element[1]
        # return self.arr[h]

    def __delitem__(self, key):
        h=self.getHash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                print(element[0],"deleted")
                self.arr[h].pop(index)
                return


if __name__=='__main__':
    a=HashTable()
    a["akshay"]="shyena","hi"
    a["yahska"]="shyena!"
    a["akshay"]="google"

    print(a["akshay"],a[ "yahska"])
    del a["akshay"]
    print(a["akshay"], a["yahska"])

