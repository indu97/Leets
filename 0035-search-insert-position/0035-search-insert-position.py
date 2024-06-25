class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        i = 2
        while(l<=r):
            i = ( l + r ) // 2
            if target > nums[i]:
                l = i + 1
            elif target < nums[i]:
                r = i - 1
            else:
                return i
        return l
        