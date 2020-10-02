class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(index, path):
            if index >= n or sum(path) >= target :
                if path and sum(path) == target and path not in ans :
                    ans.append(path)
                return
            
            dfs(index, path+[candidates[index]])
            dfs(index+1, path+[candidates[index]])
            dfs(index+1, path)
            
        dfs(0, [])
        return ans

# Another Way 
class Solution:
    def dfs(self,candidates,res,path,target,index,n):
        if sum(path) == target or index >= n:
            res.append(path)
            return
        if sum(path) > target :
            return 
    
        for i in range(index,n):
            self.dfs(candidates,res,path+[candidates[i]],target,i,n)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates,res,[],target,0,len(candidates))
        return res
        
