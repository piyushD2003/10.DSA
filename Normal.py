
print("This is DFS...")

def dfs(graph, visited, node): 
    if node not in visited: 
        visited.append(node) 
        for n in graph[node]: 
            dfs(graph, visited, n) 
    return visited 
graph = {'A': ['B', 'C'], 
         'B': ['D', 'E'], 
         'C': ['F'], 
         'D': [], 
         'E': ['F'], 
         'F': []} 
visited = dfs(graph, [], 'A') 
print(visited) 


print()
print("This is BFS...")
def bfs(graph, visited, queue): 
     if queue: 
         node = queue.pop(0) 
         if node not in visited: 
             visited.append(node) 
             for n in graph[node]: 
                 queue.append(n) 
         bfs(graph, visited, queue) 
     return visited
# def Bfs(graph,[],'A'):
graph = {'A': ['B', 'C'], 
          'B': ['D', 'E'], 
          'C': ['F'], 
          'D': [], 
          'E': ['F'], 
          'F': []} 
visited = bfs(graph, [], ['A']) 
print(visited)