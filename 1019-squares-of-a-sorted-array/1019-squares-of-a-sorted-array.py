class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n

        l, r, i = 0, n-1, n-1
        while l <= r:
            left = abs(nums[l])
            right = nums[r]
            if left > right:
                out[i] = left * left
                l += 1
            else:
                out[i] = right * right
                r -= 1
            i -= 1
        return out





