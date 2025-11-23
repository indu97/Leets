class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        while(start < len(nums)):
            num = nums[start]
            if (num < len(nums) and num!= start):
                # swap
                nums[start], nums[num] = nums[num], nums[start]
            else:
                start += 1

        i = 0
        while( i < len(nums)):
            if nums[i] != i:
                return i
            i += 1

        return len(nums)