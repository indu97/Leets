class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = nums.count(0)
        n = len(nums)
        if z > 1:
            return [0] * n
        
        out = [1] * n

        for i in range(1, n):
            out[i] = out[i-1] * nums[i-1]

        s = 1
        for i in range(n-1, -1, -1):
            out[i] = out[i] * s
            s = s * nums[i]
        return out