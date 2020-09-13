# Extreme Brute Force - Simulation Based 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        mergelist = set()
        for interval in intervals :
            if max(interval[0],newInterval[0]) <= min(interval[1],newInterval[1]):
                mergelist.add(tuple(interval))
        ans = []
        for i in intervals : 
            if not tuple(i) in mergelist:
                ans.append(i)
        
                
        def merge(intervals):
            x0,x1 = min(x[0] for x in intervals),max(x[1] for x in intervals)
            return [x0,x1]
            
        if mergelist :
            mergelist.add(tuple(newInterval))
            new = merge(mergelist)
            ans.append(new)
            ans.sort(key = lambda x : (x[0],x[1]))
        else:
            ans.append(newInterval)
            ans.sort(key = lambda x : (x[0],x[1]))
        
        return ans
