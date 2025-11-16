class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        return self.isLooped(n, seen)

    def isLooped(self, n: int, seen) -> bool:
        s = self.sumOfSquares(n)
        if s == 1:
            return True
        if s in seen:
            return False
        else:
            seen.add(s)
            return self.isLooped(s, seen)

    def sumOfSquares(self, n: int) -> int:
        sum = 0
        while(n > 0):
            r = n % 10
            n = n // 10
            sum = sum + r*r
        return sum 