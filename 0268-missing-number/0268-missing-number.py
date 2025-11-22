class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prev = 0
        if 0 not in nums:
            return 0
        elif n not in nums:
            return n
        else:
            for num in nums:
                if num != 0 :
                    if num - prev != 1:
                        return num - 1
                    prev = num