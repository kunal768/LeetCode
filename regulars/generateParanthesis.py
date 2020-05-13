class Solution:
    def dfs(self,n,res,path,oc,cc):
        if cc < oc :
            return 
        if oc == 0 and cc == 0 :
            res.append(path)
            return 
        if oc :
            self.dfs(n,res,path+"(",oc-1,cc)
        if cc :
            self.dfs(n,res,path+")",oc,cc-1)
        
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n,res,"",n,n)
        return res
    
