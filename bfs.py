



# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_connected_component(graph, start):
    explored = []
   
    queue = [start]


    while queue:

          node = queue.pop(0)
          if node not in explored:
         
             explored.append(node)
             neighbours = graph[node]

    
          for neighbour in neighbours:
               queue.append(neighbour)
    return explored

bfs_connected_component(graph,'A') # returns 
















graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

visited = []

def dfs(graph,node):
    global visite
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)

    dfs(graph1,'A')
    print(visited)s