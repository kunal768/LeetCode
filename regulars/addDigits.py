class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1 :
            return num
        else:
            ans = 0
            while (num) > 0 :
                ans += num%10
                num = num//10
            return self.addDigits(ans)
        