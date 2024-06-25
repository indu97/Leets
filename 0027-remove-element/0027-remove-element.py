class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for idx, ele in enumerate(nums):
            if ele == val:
                count += 1
            else:
                if idx != 0:  
                    nums[idx-count] = ele
        return len(nums) - count 
        