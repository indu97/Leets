class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)/2
        # a = list(set(nums))
        # for i in a:
        #     c = nums.count(i)
        #     if c > n:
        #         return i


        # Boyer-Moore Majority Vote Algorithm:
        votes = 0
        candidate = nums[0]
        for i in nums:
            if votes == 0:
                candidate = i
            if i == candidate:
                votes += 1
            else:
                votes -= 1
        return candidate