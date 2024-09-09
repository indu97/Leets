class Solution:
    # def helper(self, nums, idx, dp) -> int:
    #     if idx < 0 :
    #         return 0
    #     if dp[idx] == -1:
    #         dp[idx] = max(self.helper(nums, idx - 2, dp) + nums[idx], self.helper(nums, idx - 1, dp))
    #     return dp[idx]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp = [-1 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n-1]