class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = int(math.sqrt(area))
        while l*w != area :
            if l*w > area :
                w -= 1
            else:
                l += 1
        return [l,w]