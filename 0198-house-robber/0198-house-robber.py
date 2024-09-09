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
        pen_ultimate = nums[0]
        ultimate = max(nums[1], nums[0])
        for i in range(2, n):
            temp = ultimate      
            ultimate = max(pen_ultimate + nums[i], ultimate)
            pen_ultimate = temp
        return ultimate