class Solution:
    def helper(self, nums, idx, dp) -> int:
        if idx < 0 :
            return 0
        if dp[idx] == -1:
            dp[idx] = max(self.helper(nums, idx - 2, dp) + nums[idx], self.helper(nums, idx - 1, dp))
        return dp[idx]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        return self.helper(nums, n - 1, dp)