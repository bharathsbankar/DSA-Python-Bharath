class HashTable:
    def __init__(self,size):
        self.max=size
        # self.arr=[None for i in range(self.max)]
        self.arr=[None]*self.max

    def getHash(self,key):
        sum=0
        for i in key:
            # count+=1
            sum+=ord(i)
        return sum%self.max

    def __setitem__(self, key, value):
        h=self.getHash(key)
        while self.arr[h] is not None:
            if h == self.max - 1:
                h = 0
                continue
            h += 1
        self.arr[h] = (key, value)

    def __getitem__(self, key):
        h=self.getHash(key)
        while not self.arr[h][0]==key:
            if h==self.max-1:
                h=0
                continue

            h+=1
        return self.arr[h][1]
    def __str__(self):
        return str(self.arr)

if __name__=='__main__':
    a=HashTable(10)
    a["Bharath"]="xyz"
    # print(a.arr[0][0]=="Bharath")
    # print(a.arr)
    a["sharath"]="senio"
    a["rathsha"]="gate"
    a["ratshah"] = "IAS"
    print(a["ratshah"])
    print(a)
    # print(a.getHash("rathsha"))


