#directed graph
import numpy as np #  for matrix purpouse
class Graph:

    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        self.temp=[]
        length=0
        for start , end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
            if start not in self.temp:
                length+=1
                self.temp.append(start)
            if end not in self.temp:
                length+=1
                self.temp.append(end)


        print("graph_dictionary would be :",self.graph_dict)
        # print(length)
        print(self.temp)

        self.matrix=np.zeros((length,length))
        for i in self.graph_dict:
            a=self.temp.index(i)
            for j in self.graph_dict[i]:
                b=self.temp.index(j)
                self.matrix[a,b]=1
        print(f" {self.matrix}")

    # def getPathMatrix(self,start,end,path=[]):
    #     a=self.temp.index[start]
    #     b=self.temp.index[end]
    #     for i in self.matrix[a]:
    #         if i == j:
    #             return








    def getPath(self,start,end,path=[]):
        path=path+[start] # path is used to trace a path in a recursion
        if start==end:
            # this condition checks that the latest start which is passed to a getPath() is same as the end , even before it checks whether the start is key for a dictionary or not
            return [path]
        if start not in self.graph_dict:
            #this condition defines that traversed path does not consist end and hence empty list is returned
            return []
        paths=[]#paths list is used to store a multiple paths that can exist from start to end in a graph
        for node in self.graph_dict[start]:
            if node not in path:# this condition prevents the traversing of an already traversed node
                new_paths=self.getPath(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths


    def getShortestPath(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return path
        if start not in self.graph_dict:
            return None
        sh_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.getShortestPath(node,end,path)
                if sp:
                    if sh_path is None or len(sp) < len(sh_path):
                        sh_path=sp
        return sh_path





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
    end="BLR"
    print(f"path from {start} and {end} is :{g1.getPath(start,end)}")
    print(f" shortest path from {start} and {end} is :{g1.getShortestPath(start, end)}")

