class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        # change all 0 to -1
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1
        
        maxx = 0 
        hashmap = {0:-1}
        
        curr = 0 
        for idx,val in enumerate(arr):
            curr += val
            if curr == 0 :
                maxx = idx + 1
            if not curr in hashmap:
                hashmap[curr] = idx 
            else:
                # length will be curr_index - index where first time 0 found 
                maxx = max(maxx, idx - hashmap[curr])
                
        return maxx
