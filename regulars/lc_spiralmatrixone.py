class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix :
            return []
        l,r,t,d = 0,len(matrix[0])-1,0,len(matrix)-1
        direction = 0 # 0 : L->R , 1 : T->D , 2 : R -> L , 3 : D -> T
        ans = []
        while l <= r and t <= d :
            if direction == 0 :
                for i in range(l,r+1):
                    ans.append(matrix[t][i]) 
                t += 1
            
            elif direction == 1 :
                for i in range(t,d+1) :
                    ans.append(matrix[i][r])
                r -= 1
                
            elif direction == 2 :
                for i in range(r,l-1,-1):
                    ans.append(matrix[d][i])
                d -= 1
            elif direction == 3 :
                for i in range(d,t-1,-1):
                    ans.append(matrix[i][l])
                l += 1
            direction = (direction+1)%4
        return ans
                
        
