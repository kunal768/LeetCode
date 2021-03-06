# this is understandable 

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(lambda : [])
        for u,v in dislikes :
            graph[u].append(v)
            graph[v].append(u)
        
        color = dict()
        def dfs(node):
            for adj in graph[node]:
                if adj in color:
                    if color[adj] == color[node]:
                        return False
                else:
                    color[adj] = 1 - color[node]
                    if not dfs(adj):
                        return False
            return True
        for node in graph:
            if node not in color :
                color[node] = 0 
                if not dfs(node):
                    return False
        return True
        



# check if graph is bipartite
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(lambda : [])
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = {}
        def dfs(node,c = 0):
            if node in color :
                return color[node] == c 
            color[node] = c
            for adj in graph[node]:
                if not dfs(adj,1-c):
                    return False
            return True
            
        
        for node in range(1,N+1):
            if not node in color :
                if not dfs(node):
                    return False
        return True 
    
