class Solution:
    def helper(self, i, dp) -> int:
        if i == 1 or i == 2:
            dp[i - 1] = i
            return dp[i - 1]
        elif dp[i - 1] != -1:
            return dp[i - 1]
        else:
            dp[i - 1] = self.helper(i - 1, dp) + self.helper(i - 2, dp)
            return dp[i - 1]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n)  
        return self.helper(n, dp)