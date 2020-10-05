class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, dividend, divisor):
        overflow = 2**31 - 1
        q, t = 0, 0
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        for i in range(31,-1,-1):
            if dividend - (divisor << i) >= t :
                # ye karo 
                t += divisor << i
                # and set lsb on q 
                q |= 1 << i
                
        return min(max(-overflow-1, sign*q), overflow)
