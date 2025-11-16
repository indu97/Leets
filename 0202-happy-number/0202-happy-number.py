class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n: int) -> int:
            sum = 0
            while(n > 0):
                r = n % 10
                n = n // 10
                sum = sum + r*r
            return sum

        seen = set()
        s = sumOfSquares(n)
        while(s not in seen):
            if s == 1:
                return True
            seen.add(s)
            s = sumOfSquares(s)
        return False
