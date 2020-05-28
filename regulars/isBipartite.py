class Solution:
    def isBipartite(self, graph):
        color = {}
        def dfs(node):
            for adj in graph[node] :
                if adj in color:
                    if color[adj] == color[node]:
                        return False
                else:
                    color[adj] = 1 - color[node]
                    if not dfs(adj):
                        return False 
            return True             
            
        for i in range(len(graph)):
            if not i in color :
                color[i] = 0
                if not dfs(i):
                    return False
        return True 
