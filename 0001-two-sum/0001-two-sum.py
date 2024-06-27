class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums:
                r = len(nums) - 1 - nums[::-1].index(res)
                if r != i:
                    return [i, r]
