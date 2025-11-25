class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        n = len(nums)
        while(i < n):
            num = nums[i]
            if nums[i] != i+1 and nums[num - 1] != num:
                # switch 
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
            else:
                i += 1


        out = []
        i = 0
        for num in nums:
            if num != i + 1:
                out.append(i+1)
            i += 1
        return out
        
