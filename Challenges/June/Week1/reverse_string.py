def reverseFromMid(string,left,right):
    if len(string) < 1 or left > right :
        return ""
    n = len(string)
    while left >=0 and right < n :
        string[left],string[right] = string[right],string[left]
        left -= 1
        right += 1
    return string


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) < 1 :
            return s
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = n//2
        # if even
        if n & 1 == 0 :
            s = reverseFromMid(s,i-1,i)
        else:
            s = reverseFromMid(s,i,i)
        
