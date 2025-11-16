class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n: int) -> int:
            total = 0
            while(n > 0):
                r = n % 10
                n = n // 10
                total += r*r
            return total

        slow = sumOfSquares(n)
        fast = sumOfSquares(slow)

        while(slow != fast):
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        
        if slow == 1:
            return True
        else: 
            return False
