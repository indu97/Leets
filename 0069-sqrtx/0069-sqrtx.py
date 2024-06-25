class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0

        for i in range(x+1):    
            if i*i == x:
                result = i
                break
            elif i*i > x:
                result = i-1
                break
        return result
        