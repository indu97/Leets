class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        for i in set(nums):
            c = nums.count(i)
            if c > n:
                return i