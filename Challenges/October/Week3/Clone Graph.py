"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # BFS method 
        if not node :
            return node
        q = [node]
        hm = {}
        temp = Node(node.val)
        # hm mei key hai original node aur value hai copy node
        hm[node.val] = temp
        while q :
            curr = q.pop(0)
            for adj in curr.neighbors :
                if not adj.val in hm :
                    q.append(adj)
                    hm[adj.val] = Node(adj.val)
                
                hm[curr.val].neighbors.append(hm[adj.val])
        
        return temp
        
 # DFS method 
 
 class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hm = {}
        def dfs(node):
            nonlocal hm 
            if not node :
                return node
            temp = Node(node.val)
            hm[node] = temp
            for n in node.neighbors :
                if n in hm :
                    temp.neighbors.append(hm[n])
                else:
                    neigh = dfs(n)
                    temp.neighbors.append(neigh)
            
            return temp
        
        return dfs(node)
 
 
