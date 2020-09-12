class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        poss = [i for i in range(1,10)]
        res = []
        def dfs(path,index):
            nonlocal res
            if index >= len(poss) :
                if len(path) == k and sum(path) == n :
                    if not path in res :
                        res.append(path)
                return 
            
            dfs(path,index+1)
            dfs(path+[poss[index]],index+1)
        
        dfs([],0)
        return sorted(res)
