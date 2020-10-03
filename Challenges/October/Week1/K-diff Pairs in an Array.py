class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        vis, c = set(), 0 
        if k == 0 :
            return sum(v > 1 for v in Counter(nums).values())
        for idx, val in enumerate(nums):
            c += (val - k in vis and val not in vis) + (val + k in vis and val not in vis)
            vis.add(val)
        return c
