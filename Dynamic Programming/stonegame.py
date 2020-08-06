 
'''
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

 

Note:

    2 <= piles.length <= 500
    piles.length is even.
    1 <= piles[i] <= 500
    sum(piles) is odd.

By observation : Due to given constraints Alex always wins the game 
since it can either take all the even indexed coins or the odd indexed coins 
if sum(evenindexed) > sum(oddindexed) Alex takes all even indexed else it takes all odd indexed and either is bound to be greater due to given constraints 
'''

#-- Solution by observation 
class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        return True

#-- Solution by Recursion 
#This even works without the given constraints

from functools import lru_cache
class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i,j):
            if i > j :
                return 0 
            return max(nums[i]-dfs(i+1,j), nums[j]-dfs(i,j-1))


#REFERENCE : https://binarysearch.io/problems/Candy-Race








