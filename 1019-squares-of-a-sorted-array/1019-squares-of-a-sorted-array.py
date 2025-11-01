class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n
        if nums[0] >= 0:
            for i in range(n):
                out[i] = nums[i] * nums[i]
            return out
        
        m = n
        for i, x in enumerate(nums):
            if x >= 0:
                m = i
                break
        if m == n:
            for i in range(n):
                out[i] = nums[n-i-1] * nums[n-i-1]
            return out

        i, j, k = m-1, m, 0
        while(i >= 0 and j <= n-1):
            if abs(nums[i]) < nums[j]:
                out[k] = nums[i] * nums[i]
                i -= 1
            else:
                out[k] = nums[j] * nums[j]
                j += 1
            k += 1
        
        while i >= 0:
            out[k] = nums[i] * nums[i]
            i -= 1
            k += 1
        
        while j <= n-1:
            out[k] = nums[j] * nums[j]
            j += 1
            k += 1
        return out





