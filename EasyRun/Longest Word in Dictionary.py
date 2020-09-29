# For every word in the input list, we can check whether all prefixes of that word are in the input list by using a Set.
class Solution:
    def longestWord(self, words: List[str]) -> str:
        hs = set(words)
        ans = ""
        for word in words :
            if len(word) > len(ans) or len(word) == len(ans) and  ans > word :
                if all(word[:k] in hs for k in range(1,len(word))):
                    ans = word 
        return ans