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
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
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

