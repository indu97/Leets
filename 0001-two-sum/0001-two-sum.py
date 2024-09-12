class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums:
                idx2 = nums.index(target - num)
                if idx != idx2:
                    return [idx, idx2]