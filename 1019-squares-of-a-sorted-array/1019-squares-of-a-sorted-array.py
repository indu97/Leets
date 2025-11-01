class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)

        for i, x in enumerate(nums):
            squares[i] = nums[i] * nums[i]

        return sorted(squares)

