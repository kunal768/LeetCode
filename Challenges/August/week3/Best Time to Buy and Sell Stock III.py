class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxtotal = 0 
        first_profit = [0]*len(prices)
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            profit = prices[i] - min_price
            maxtotal = max(maxtotal,profit)
            first_profit[i] = maxtotal
        
        max_price = float('-inf')
        for j in range(len(prices)-1,0,-1):
            max_price = max(max_price,prices[j])
            profit = max_price - prices[j]
            maxtotal = max(maxtotal,first_profit[j-1]+profit)

        return maxtotal
        
