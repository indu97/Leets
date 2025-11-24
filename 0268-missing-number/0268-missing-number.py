class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            num = nums[i]
            if nums[i] < n and nums[i] != i:
                nums[i], nums[num] = nums[num], nums[i]
            else:
                i += 1

        i = 0
        while i < n:
            if nums[i] != i:
                return i
            i += 1

        return n
