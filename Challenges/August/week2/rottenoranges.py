class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        q = []
        # d = 0
        fresh = 0 
        rotten = 0 
        empty = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2 :
                    q.append((i,j,0))
                    rotten += 1
                if grid[i][j] == 1 :
                    fresh += 1
                if grid[i][j] == 0 :
                    empty += 1
        
        if not fresh and not rotten and empty :
            return 0 
        if not rotten :
            return -1 
        if not fresh :
            return 0 
        
        
        poss = [(1,0),(-1,0),(0,1),(0,-1)]
        def isvalid(x,y):
            return x >= 0 and x < n and y >= 0 and y < m
        ans = 0 
        while q :
            x,y,z = q.pop(0)
            ans = max(ans,z)
            for i in range(4):
                ax,ay = x + poss[i][0],y+poss[i][1]
                if isvalid(ax,ay) and grid[ax][ay] == 1 :
                    grid[ax][ay] = 2 
                    q.append((ax,ay,z+1))
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return - 1
        return ans
            
                
        
