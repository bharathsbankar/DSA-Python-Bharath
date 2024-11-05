#directed graph
class Graph:

    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start , end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("graph_dictionary would be :",self.graph_dict)

    def getPath(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]



    def no_of_incom_nodes(self,node):

        count=0
        for i in self.edges:
            if i[1]==node:
                count+=1
        return count


if __name__=="__main__":
    routes=[("RNR","DVG"),
            ("DVG","BLR"),
            ("CDR","BLR"),
            ("RNR","CDR"),
            ("CDR","DVG")
            ]
    g1=Graph(routes)
    start="RNR"
    end="RNR"
    print(f"path from {start} and {end} is :{g1.getPath(start,end)}")

