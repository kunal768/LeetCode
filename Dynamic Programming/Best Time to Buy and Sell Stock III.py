class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fb, fs, sb, ss = float('inf'), 0, float('inf'), 0 
        
        for price in prices :
            fb = min(fb, price)
            fs = max(fs, price - fb)
            sb = min(sb, price - fs)
            ss = max(ss, price - sb)
        
        return ss
        
