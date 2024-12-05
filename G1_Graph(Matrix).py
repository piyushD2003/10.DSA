class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_matrix =[[0]*vno for e in range(vno)]
        print(len(self.adj_matrix))
        
    def add_edge(self,u,v,wgt=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]= wgt
            self.adj_matrix[v][u]= wgt
        else:
            raise IndexError
        
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]= 0
            self.adj_matrix[v][u]= 0
        else:
            raise IndexError
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            raise IndexError
    
    def print_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))

            # for column in row:
            #     print(column,end=" ")
            # print()
        
g = Graph(5)
g.add_edge(0,0)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(3,2)
g.add_edge(3,4)
g.remove_edge(3,4)

g.print_matrix()