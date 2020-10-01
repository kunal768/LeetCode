class RecentCounter:

    def __init__(self):
        self.recent = [] 
        

    def ping(self, t: int) -> int:
        self.recent.append(t)
        # Linear Search TLE 
        '''
        c = 0
        for i in self.recent :
            if i >= t-3000 and i <= t :
                c += 1
        return c
        '''
        
        # BSearch Accpeted 
        def issafe(mid) :
            return mid >= t-3000 and mid <= t
        
        l, h = 0, len(self.recent) - 1
        
        first, last = -1, -1
         
        while l <= h :
            mid = (l+h)//2
            if self.recent[mid] >= t - 3000 :
                if issafe(self.recent[mid]):
                    first = mid
                h = mid - 1
            else:
                l = mid + 1
        
        
        l, h = 0, len(self.recent) - 1
        while l <= h :
            mid = (l+h)//2
            if self.recent[mid] <= t :
                if issafe(self.recent[mid]):
                    last = mid 
                l = mid + 1
            else:
                h = mid - 1
                
                
        if last == -1 and first == -1 :
            return 0 
        
        return last - first + 1
            
                
                
        
        
        
        



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
