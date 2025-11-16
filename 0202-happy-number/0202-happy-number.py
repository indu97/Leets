class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n: int) -> int:
            total = 0
            while(n > 0):
                r = n % 10
                n = n // 10
                total += r*r
            return total

        seen = set()
        s = n
        while(s not in seen):
            if s == 1:
                return True
            seen.add(s)
            s = sumOfSquares(s)
        return False
