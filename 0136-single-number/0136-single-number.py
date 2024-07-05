class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, count in c.items():
            if count == 1:
                return key
