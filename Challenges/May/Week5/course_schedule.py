class Solution:
    def dfs(self,graph,node,color):
        color[node] = "gray"
        for adj in graph[node] :
            if color[adj] == "gray" :
                return True
            if color[adj] == "white" and self.dfs(graph,adj,color) == True :
                return True 
        
        color[node] = "black"
        return False
    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # basically if there is a back edge(cycle) in the directed graph that is from 1 to 1 or from 2 to 2 i cant finish the course
        
        graph = defaultdict(lambda : [])
        for i in prerequisites :
            graph[i[0]].append(i[1])
            
        color = []
        for i in range(numCourses) : 
            color.append("white")
        
        for node in list(graph.keys()) :
            if color[node] == "white" :
                if self.dfs(graph,node,color) == True :
                    return False
        return True
        
        
