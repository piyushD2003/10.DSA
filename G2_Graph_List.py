class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {key:[] for key in range(vno)}
    
    def add_edge(self,u,v,wgt=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            if u==v:
                self.adj_list[u].append((v,wgt))
            else:
                self.adj_list[u].append((v,wgt))
                self.adj_list[v].append((u,wgt))
        else:
            print("Invalid Vertices")
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u] = [(vertex,wgt) for vertex, wgt in self.adj_list[u] if vertex!= v]
            self.adj_list[v] = [(vertex,wgt) for vertex, wgt in self.adj_list[v] if vertex!= u]
        else:
            print("Invalid Vertices")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex == v for vertex,x in self.adj_list[u])
    
    def print_adj_list(self):
        for key in self.adj_list:
            print(key,":", self.adj_list[key])

    def BFS(self,N):
        vertex =[False]*(self.vertex_count)
        q = []
        q.append(N)
        vertex[N] = True
        while q:
            n = q[0]
            q.pop(0)
            print(n, end=" ")
            for i in self.adj_list[n]:
                if vertex[i[0]] == False:
                    q.append(i[0])
                    vertex[i[0]]=True

    def DFS(self,N):
        vertex =[False]*(self.vertex_count)
        q = []
        q.insert(0,N)
        vertex[N] = True
        while q:
            n = q[0]
            q.pop(0)
            print(n, end=" ")
            for i in self.adj_list[n]:
                if vertex[i[0]] == False:
                    q.insert(0,i[0])
                    vertex[i[0]]=True


g = Graph(5)

g.add_edge(0,1)
g.add_edge(2,0)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(4,2)
g.add_edge(3,4)
g.print_adj_list()
print(g.has_edge(2,0))
g.remove_edge(0,0)
# g.remove_edge(3,2)
g.print_adj_list()
g.BFS(0)
print()
g.DFS(3)