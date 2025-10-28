class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        out = [0] * n

        for i in range(n):
            prefix[i] = prefix[i-1] * nums[i-1] if i!= 0 else 1
            suffix[n-i-1] = suffix[n-i] * nums[n-i] if i!= 0 else 1

        for i in range(n):
            out[i] = prefix[i] * suffix[i] 
        return out