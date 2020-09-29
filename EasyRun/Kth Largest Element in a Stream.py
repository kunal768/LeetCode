class KthLargest(object): 

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pq = nums
        heapq.heapify(self.pq)
        self.k = k 
        while len(self.pq) > self.k :
            heapq.heappop(self.pq)
        

    def add(self, val):
        """
        :type val: inty
        :rtype: int
        """
        if len(self.pq) < self.k :
            heapq.heappush(self.pq, val)
        elif val > self.pq[0] :
            heapq.heapreplace(self.pq, val)
        
        return self.pq[0]
        
        
        
        # return nlargest(self.k, self.pq)[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)