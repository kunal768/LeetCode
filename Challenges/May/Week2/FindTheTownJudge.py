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
  
# and then .... when i saw other solutions and came to know my solution was pretty stupid ... i realised this is a good method 
# of learning so without further ado .... 

# O(n) method and i didnt realise this is a Graph Concept
# Considet "trust" as a directed Graph -> then degree is the incoming and outgoing edges 
# if degree of a vertex == N-1 means its trusted by every other vertex making it the judge 
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # corner case 
        if len(trust) == 0:
            if N > 1 :
                return -1
            return 1
        
        degrees = [0]*(N+1)
        for (i,j) in trust :
            # they trust someone so outward edge
            degrees[i] -= 1
            # they are being trusted so inwards edge
            degrees[j] += 1
    
        for i in range(len(degrees)) :
            # if some vertex has degree N - 1 its the judge
            if degrees[i] == N - 1 :
                return i 
        return -1
                





