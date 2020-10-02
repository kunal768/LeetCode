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
