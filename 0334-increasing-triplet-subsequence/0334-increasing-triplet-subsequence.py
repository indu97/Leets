class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3: 
            return False

        first = second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
