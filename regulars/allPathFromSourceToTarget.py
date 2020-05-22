'''
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

    The number of nodes in the graph will be in the range [2, 15].
    You can print different paths in any order, but you should keep the order of nodes inside one path.
'''

'''

Approach #1: Recursion [Accepted]

Intuition

Since the graph is a directed, acyclic graph, any path from A to B is going to be composed of A plus a path from any neighbor of A to B. We can use a recursion to return the answer.

Algorithm

Let N be the number of nodes in the graph. If we are at node N-1, the answer is just the path {N-1}. Otherwise, if we are at node node, the answer is {node} + {path from nei to N-1} for each neighbor nei of node. This is a natural setting to use a recursion to form the answer.
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        def solve(node):
            if node == n-1 : return [[n-1]]
            ans = []
            for adj in graph[node] :
                for path in solve(adj):
                    ans.append([node] + path)
            return ans
        return solve(0)
        
                    
        
        





