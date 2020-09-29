class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def comp(xl,xr,yl,yr):
            return min(xr,yr) > max(xl,yl)
        
        return comp(rec1[0], rec1[2], rec2[0], rec2[2]) and comp(rec1[1], rec1[3], rec2[1], rec2[3])
    