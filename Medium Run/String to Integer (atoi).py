class Solution:
    def myAtoi(self, s: str) -> int:
        if not s :
            return 0
        maxx = 2**31 - 1
        minn = -2**31 
        sign = 1
        res = 0 
        i = 0 
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i < len(s) and (s[i] == '+' or s[i] == '-' ) :
            sign = -1 if s[i] == '-' else 1 
            i += 1
        
        while i < len(s) and s[i] >= '0' and s[i] <= '9' :
            if res > maxx // 10 or ( res == maxx//10 and (ord(s[i]) - ord('0')) > maxx%10 ):
                return maxx if sign == 1 else minn
            
            res = res*10 + ord(s[i]) - ord('0')
            i += 1
        
        return res*sign 
