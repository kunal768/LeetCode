# my one time ac solution :)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        hashmap = defaultdict(lambda : set({}))
        for pair in trust :
            hashmap[pair[0]].add(pair[1])
            
        judge = None        
        
        for i in range(1,N+1) :
            if len(hashmap[i]) == 0 :
                judge = i 
        
        common = set({i for i in range(1,N+1)})
        
        for val in hashmap :
            if len(hashmap[val]) != 0 :
                common.intersection_update(hashmap[val])
                
                
        if len(common) != 1 :
            return -1
        elif common.pop() != judge  :
            return -1
        else:
            return judge
                
