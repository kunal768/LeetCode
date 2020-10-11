class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2 :
            return 0 
        deduct = prices[0]
        ans = 0 
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - deduct)
            # max difference, so least deduction and most selling
            deduct = min(deduct, prices[i])
        
        return ans
        
